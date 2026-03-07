from django.db import transaction

from products.models import Product
from inventory.models import Inventory

from .models import Sale, SaleItem


def create_sale(cashier, items):

    with transaction.atomic():

        sale = Sale.objects.create(cashier=cashier)

        total_amount = 0
        total_profit = 0

        for item in items:

            product_id = item["product"]
            quantity = item["quantity"]

            product = Product.objects.get(id=product_id)

            inventory = Inventory.objects.get(product=product)

            if inventory.quantity < quantity:
                raise ValueError(f"Not enough stock for {product.name}")

            price = product.selling_price
            cost = product.cost_price

            subtotal = price * quantity
            profit = (price - cost) * quantity

            SaleItem.objects.create(
                sale=sale,
                product=product,
                quantity=quantity,
                price=price,
                cost_price=cost,
                subtotal=subtotal,
                profit=profit
            )

            inventory.quantity -= quantity
            inventory.save()

            total_amount += subtotal
            total_profit += profit

        sale.total_amount = total_amount
        sale.total_profit = total_profit
        sale.save()

        return sale