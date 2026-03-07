from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from users.permissions import IsAdminUserRole
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


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
    search_fields = ["name", "description"]
    ordering_fields = ["name", "price"]

    def get_queryset(self):

        queryset = super().get_queryset()

        category = self.request.query_params.get("category")

        if category:
            queryset = queryset.filter(category_id=category)

        return queryset