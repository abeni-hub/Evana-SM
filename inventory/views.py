from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from .models import Inventory, InventoryHistory
from .serializers import InventorySerializer, InventoryHistorySerializer
from .services import InventoryService
from .permissions import IsAdminOnly

from django.db import models

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class InventoryViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Inventory.objects.select_related("product").all()

    serializer_class = InventorySerializer

    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    search_fields = [
        "product__name"
    ]

    ordering_fields = [
        "quantity"
    ]

    @action(detail=True, methods=["post"], permission_classes=[IsAdminOnly])
    def add_stock(self, request, pk=None):

        inventory = self.get_object()

        quantity = int(request.data.get("quantity"))

        note = request.data.get("note")

        InventoryService.add_stock(
            inventory.product,
            quantity,
            request.user,
            note
        )

        return Response({"message": "Stock added successfully"})

    @action(detail=True, methods=["post"], permission_classes=[IsAdminOnly])
    def remove_stock(self, request, pk=None):

        inventory = self.get_object()

        quantity = int(request.data.get("quantity"))

        note = request.data.get("note")

        InventoryService.remove_stock(
            inventory.product,
            quantity,
            request.user,
            note
        )

        return Response({"message": "Stock removed successfully"})

    @action(detail=False, methods=["get"])
    def low_stock(self, request):

        items = Inventory.objects.filter(
            quantity__lte=models.F("low_stock_threshold")
        )

        serializer = self.get_serializer(items, many=True)

        return Response(serializer.data)


class InventoryHistoryViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = (
        InventoryHistory.objects
        .select_related("product", "user")
        .all()
        .order_by("-created_at")
    )

    serializer_class = InventoryHistorySerializer

    permission_classes = [IsAuthenticated]