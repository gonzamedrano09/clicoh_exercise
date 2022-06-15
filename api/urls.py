from rest_framework.routers import DefaultRouter
from api.routers.user_router import UserRouter
from api.views.user_view import UserViewSet
from api.views.product_view import ProductViewSet
from api.views.order_view import OrderViewSet


user_router = UserRouter()
router = DefaultRouter()

user_router.register(r"users", UserViewSet, basename="users")
router.register(r"products", ProductViewSet, basename="products")
router.register(r"orders", OrderViewSet, basename="orders")

urlpatterns = user_router.urls + router.urls
