from rest_framework.routers import DefaultRouter
from .views import InventoryViewSet, InventoryHistoryViewSet


router = DefaultRouter()

router.register("inventory", InventoryViewSet, basename="inventory")
router.register("inventory-history", InventoryHistoryViewSet)

urlpatterns = router.urls