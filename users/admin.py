from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "username",
        "email",
        "role",
        "is_active",
        "date_joined",
    )

    list_filter = ("role", "is_active")

    search_fields = ("username", "email")


admin.site.register(User, UserAdmin)