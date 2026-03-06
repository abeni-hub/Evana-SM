from django.contrib import admin
from .models import Inventory, InventoryHistory


class InventoryAdmin(admin.ModelAdmin):

    list_display = (
        "product",
        "quantity",
        "low_stock_threshold",
        "updated_at",
    )

    search_fields = ("product__name",)


class InventoryHistoryAdmin(admin.ModelAdmin):

    list_display = (
        "product",
        "action",
        "quantity",
        "user",
        "created_at",
    )

    list_filter = ("action",)


admin.site.register(Inventory, InventoryAdmin)
admin.site.register(InventoryHistory, InventoryHistoryAdmin)