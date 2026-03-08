from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Sale, Expense
from .serializers import (
    SaleSerializer,
    SaleCreateSerializer,
    ExpenseSerializer
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .services import create_sale


class SaleViewSet(viewsets.ModelViewSet):

    queryset = Sale.objects.prefetch_related("items").all().order_by("-created_at")

    serializer_class = SaleSerializer

    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = [
        "cashier",
        "created_at"
    ]

    ordering_fields = [
        "created_at",
        "total_amount",
        "total_profit"
    ]


    def create(self, request):

        serializer = SaleCreateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        try:

            sale = create_sale(
                cashier=request.user,
                items=serializer.validated_data["items"]
            )

            return Response(
                SaleSerializer(sale).data,
                status=status.HTTP_201_CREATED
            )

        except ValueError as e:

            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class ExpenseViewSet(viewsets.ModelViewSet):

    queryset = Expense.objects.all().order_by("-created_at")

    serializer_class = ExpenseSerializer

    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    search_fields = ["title"]

    ordering_fields = ["amount", "created_at"]