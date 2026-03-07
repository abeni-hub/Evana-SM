from django.db.models import Sum, F
from django.utils import timezone
from datetime import timedelta

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from sales.models import Sale, SaleItem
from inventory.models import Inventory


class ReportViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    # DAILY SALES
    @action(detail=False, methods=["get"])
    def daily_sales(self, request):

        today = timezone.now().date()

        sales = Sale.objects.filter(created_at__date=today)

        total_sales = sales.aggregate(
            total=Sum("total_amount")
        )["total"] or 0

        total_profit = sales.aggregate(
            total=Sum("total_profit")
        )["total"] or 0

        return Response({
            "date": today,
            "total_sales": total_sales,
            "total_profit": total_profit
        })

    # MONTHLY SALES
    @action(detail=False, methods=["get"])
    def monthly_sales(self, request):

        today = timezone.now()

        start_month = today.replace(day=1)

        sales = Sale.objects.filter(created_at__gte=start_month)

        total_sales = sales.aggregate(
            total=Sum("total_amount")
        )["total"] or 0

        total_profit = sales.aggregate(
            total=Sum("total_profit")
        )["total"] or 0

        return Response({
            "month": today.strftime("%B"),
            "total_sales": total_sales,
            "total_profit": total_profit
        })

    # TOP SELLING PRODUCTS
    @action(detail=False, methods=["get"])
    def top_products(self, request):

        products = (
            SaleItem.objects
            .values("product__name")
            .annotate(total_sold=Sum("quantity"))
            .order_by("-total_sold")[:5]
        )

        return Response(products)

    # LOW STOCK PRODUCTS
    @action(detail=False, methods=["get"])
    def low_stock(self, request):

        items = Inventory.objects.filter(quantity__lt=10)

        data = []

        for item in items:

            data.append({
                "product": item.product.name,
                "quantity": item.quantity
            })

        return Response(data)