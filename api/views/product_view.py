from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models.product import Product
from api.serializers.product_serializers.product_serializer import ProductSerializer
from api.serializers.product_serializers.product_update_serializer import ProductUpdateSerializer
from api.serializers.product_serializers.product_update_stock_serializer import ProductUpdateStockSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.filter(is_deleted=False)

    def get_serializer_class(self):
        if self.action in ["create", "retrieve", "list"]:
            return ProductSerializer
        elif self.action in ["update", "partial_update"]:
            return ProductUpdateSerializer
        elif self.action == "update_stock":
            return ProductUpdateStockSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

    @action(detail=True, url_path="update-stock", methods=["put", "patch"])
    def update_stock(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
