from django.db import models
from users.models import User
from products.models import Product

class Sale(models.Model):

    cashier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

class SaleItem(models.Model):

    sale = models.ForeignKey(Sale, related_name="items", on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
class Expense(models.Model):

    title = models.CharField(max_length=200)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)