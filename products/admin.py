from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "created_at")


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "category",
        "cost_price",
        "selling_price",
        "created_at",
    )

    list_filter = ("category",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)