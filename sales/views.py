from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Sale, Expense
from .serializers import (
    SaleSerializer,
    SaleCreateSerializer,
    ExpenseSerializer
)

from .services import create_sale


class CreateSaleView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

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


class SaleListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        sales = Sale.objects.all().order_by("-created_at")

        serializer = SaleSerializer(sales, many=True)

        return Response(serializer.data)


class ExpenseListCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        expenses = Expense.objects.all().order_by("-created_at")

        serializer = ExpenseSerializer(expenses, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = ExpenseSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)