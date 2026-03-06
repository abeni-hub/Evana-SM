from django.db import models
from products.models import Product
from users.models import User


class Inventory(models.Model):

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name="inventory"
    )

    quantity = models.PositiveIntegerField(default=0)

    low_stock_threshold = models.PositiveIntegerField(default=5)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

    @property
    def is_low_stock(self):
        return self.quantity <= self.low_stock_threshold


class InventoryHistory(models.Model):

    ACTION_TYPES = (
        ("ADD", "Stock Added"),
        ("REMOVE", "Stock Removed"),
        ("ADJUST", "Stock Adjusted"),
        ("SALE", "Sale Deduction"),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    action = models.CharField(max_length=20, choices=ACTION_TYPES)

    quantity = models.IntegerField()

    previous_stock = models.IntegerField()

    new_stock = models.IntegerField()

    note = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.action}"