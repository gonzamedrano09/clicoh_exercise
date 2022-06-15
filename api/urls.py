from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.routers.user_router import UserRouter
from api.views.user_view import UserViewSet
from api.views.product_view import ProductViewSet
from api.views.order_view import OrderViewSet


# Routers (viewsets)

user_router = UserRouter()
router = DefaultRouter()

user_router.register(r"users", UserViewSet, basename="users")
router.register(r"products", ProductViewSet, basename="products")
router.register(r"orders", OrderViewSet, basename="orders")


# Url patterns

urlpatterns = [

    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

] + user_router.urls + router.urls
