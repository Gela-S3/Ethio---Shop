from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.utils import timezone

User = settings.AUTH_USER_MODEL  # default 'auth.User' or your custom user model

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)], default=0.00)
    category = models.ForeignKey(Category, related_name="products", null=True, on_delete=models.PROTECT)
    stock_quantity = models.PositiveIntegerField(default=0)
    image_url = models.URLField(blank=True)  # or use ImageField if storing files
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)  # manager user

    class Meta:
        ordering = ("-created_at",)
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name

    def reduce_stock(self, amount=1):
        if amount <= 0:
            return
        if self.stock_quantity < amount:
            raise ValueError("Not enough stock")
        self.stock_quantity -= amount
        self.save()

class Review(models.Model):
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=5)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
