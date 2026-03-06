from django.db import transaction
from .models import Inventory, InventoryHistory


class InventoryService:

    @staticmethod
    @transaction.atomic
    def add_stock(product, quantity, user, note=None):

        inventory = Inventory.objects.select_for_update().get(product=product)

        previous = inventory.quantity

        inventory.quantity += quantity

        inventory.save()

        InventoryHistory.objects.create(
            product=product,
            user=user,
            action="ADD",
            quantity=quantity,
            previous_stock=previous,
            new_stock=inventory.quantity,
            note=note
        )

        return inventory


    @staticmethod
    @transaction.atomic
    def remove_stock(product, quantity, user, note=None):

        inventory = Inventory.objects.select_for_update().get(product=product)

        if inventory.quantity < quantity:
            raise ValueError("Not enough stock")

        previous = inventory.quantity

        inventory.quantity -= quantity

        inventory.save()

        InventoryHistory.objects.create(
            product=product,
            user=user,
            action="REMOVE",
            quantity=quantity,
            previous_stock=previous,
            new_stock=inventory.quantity,
            note=note
        )

        return inventory