from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from users.permissions import IsAdminUserRole
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    search_fields = ["name"]
    ordering_fields = ["name"]


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.select_related("category").all()

    serializer_class = ProductSerializer

    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category"]
    search_fields = ["name"]
    ordering_fields = ["name"]
    # POS FAST SEARCH
    @action(detail=False, methods=["get"], url_path="search")

    def search_products(self, request):

        query = request.query_params.get("q", "").strip()

        # minimum 3 letters
        if len(query) < 3:
            return Response([])

        products = Product.objects.filter(
            Q(name__icontains=query)
        ).select_related("category")[:10]

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    def get_queryset(self):

        queryset = super().get_queryset()

        category = self.request.query_params.get("category")

        if category:
            queryset = queryset.filter(category_id=category)

        return queryset