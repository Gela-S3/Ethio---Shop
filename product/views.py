from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Product, Brand, Category
from .serializers import ProductSerializer, BrandSerializer, CategorySerializer


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """A simple ViewSet for viewing and editing categories."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer #new serializer added

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    """A simple ViewSet for viewing and editing products."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer #new serializer added

    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

class BrandViewSet(viewsets.ModelViewSet):
    """A simple ViewSet for viewing and editing brands."""

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer #new serializer added

    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)