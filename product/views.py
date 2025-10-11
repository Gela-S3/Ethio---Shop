from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer, ReviewSerializer
from .filters import ProductFilter
from .permissions import IsAuthenticatedOrReadOnlyForWrite
from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnlyForWrite]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category", "created_by").all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnlyForWrite]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ["name", "description", "category__name"]
    ordering_fields = ["price", "created_at", "name"]

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return ProductDetailSerializer
        return ProductSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=["post"], url_path="purchase", permission_classes=[IsAuthenticatedOrReadOnlyForWrite])
    def purchase(self, request, pk=None):
        """
        Example endpoint to 'purchase' a product and reduce stock.
        Body: {"quantity": 1}
        """
        product = self.get_object()
        quantity = int(request.data.get("quantity", 1))
        if quantity <= 0:
            return Response({"detail": "Quantity must be greater than 0."}, status=status.HTTP_400_BAD_REQUEST)
        if product.stock_quantity < quantity:
            return Response({"detail": "Not enough stock."}, status=status.HTTP_400_BAD_REQUEST)
        product.reduce_stock(quantity)
        return Response({"detail": "Purchase successful.", "remaining_stock": product.stock_quantity})

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.select_related("user", "product").all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnlyForWrite]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
