from rest_framework.routers import DefaultRouter
from api.views.product_view import ProductViewSet
from api.views.order_view import OrderViewSet


router = DefaultRouter()

router.register(r"products", ProductViewSet, basename="products")
router.register(r"orders", OrderViewSet, basename="orders")

urlpatterns = router.urls
