from rest_framework import serializers

from .models import Sale, SaleItem, Expense


class SaleItemSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = SaleItem
        fields = [
            "id",
            "product",
            "product_name",
            "quantity",
            "price",
            "subtotal",
            "profit"
        ]


class SaleSerializer(serializers.ModelSerializer):

    items = SaleItemSerializer(many=True, read_only=True)

    class Meta:
        model = Sale
        fields = [
            "id",
            "cashier",
            "total_amount",
            "total_profit",
            "created_at",
            "items"
        ]


class SaleCreateItemSerializer(serializers.Serializer):

    product = serializers.IntegerField()

    quantity = serializers.IntegerField()


class SaleCreateSerializer(serializers.Serializer):

    items = SaleCreateItemSerializer(many=True)


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = "__all__"