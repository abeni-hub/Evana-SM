from django.db import models
from users.models import User
from products.models import Product


class Sale(models.Model):

    cashier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    total_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["created_at"]),
            models.Index(fields=["cashier"]),
        ]

    def __str__(self):
        return f"Sale #{self.id}"


class SaleItem(models.Model):

    sale = models.ForeignKey(Sale, related_name="items", on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    quantity = models.IntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    cost_price = models.DecimalField(max_digits=10, decimal_places=2)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    profit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


class Expense(models.Model):

    title = models.CharField(max_length=200)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title