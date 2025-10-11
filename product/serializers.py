from rest_framework import serializers
from .models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "slug")

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "category",
            "category_id",
            "stock_quantity",
            "image_url",
            "created_at",
            "created_by",
        )

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Product name cannot be empty")
        return value

    def validate(self, data):
        price = data.get("price") if "price" in data else getattr(self.instance, "price", None)
        stock = data.get("stock_quantity") if "stock_quantity" in data else getattr(self.instance, "stock_quantity", None)
        if price is None:
            raise serializers.ValidationError({"price": "Price is required."})
        if stock is None:
            raise serializers.ValidationError({"stock_quantity": "Stock quantity is required."})
        if price < 0:
            raise serializers.ValidationError({"price": "Price must be non-negative."})
        if stock < 0:
            raise serializers.ValidationError({"stock_quantity": "Stock must be non-negative."})
        return data

class ProductDetailSerializer(ProductSerializer):
    # include reviews if implemented
    reviews = serializers.SerializerMethodField()

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ("reviews",)

    def get_reviews(self, obj):
        # minimal; you can expand with serializer
        return [{"user": r.user.username, "rating": r.rating, "comment": r.comment} for r in getattr(obj, "reviews", []).all()]

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = ("id", "product", "user", "rating", "comment", "created_at")
        read_only_fields = ("user", "created_at")
