from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    category_name = serializers.ReadOnlyField(source="category.name")

    profit_margin = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "category_name",
            "cost_price",
            "selling_price",
            "profit_margin",
            "created_at",
        ]

    def get_profit_margin(self, obj):

        return obj.selling_price - obj.cost_price