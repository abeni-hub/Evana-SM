from django.urls import path

from .views import (
    CreateSaleView,
    SaleListView,
    ExpenseListCreateView
)

urlpatterns = [

    path("create/", CreateSaleView.as_view()),

    path("", SaleListView.as_view()),

    path("expenses/", ExpenseListCreateView.as_view()),

]