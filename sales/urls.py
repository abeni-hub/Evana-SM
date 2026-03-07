from rest_framework.routers import DefaultRouter

from .views import SaleViewSet, ExpenseViewSet


router = DefaultRouter()

router.register("sales", SaleViewSet, basename="sales")

router.register("expenses", ExpenseViewSet, basename="expenses")

urlpatterns = router.urls