from rest_framework import serializers
from .models import Inventory, InventoryHistory


class InventorySerializer(serializers.ModelSerializer):

    product_name = serializers.ReadOnlyField(source="product.name")

    is_low_stock = serializers.ReadOnlyField()

    class Meta:
        model = Inventory
        fields = [
            "id",
            "product",
            "product_name",
            "quantity",
            "low_stock_threshold",
            "is_low_stock",
            "updated_at",
        ]


class InventoryHistorySerializer(serializers.ModelSerializer):

    product_name = serializers.ReadOnlyField(source="product.name")

    user_name = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = InventoryHistory
        fields = "__all__"