from rest_framework import viewsets
from api.models.order import Order
from api.serializers.order_serializers.order_serializer import OrderSerializer
from api.serializers.order_serializers.order_update_serializer import OrderUpdateSerializer


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "retrieve", "list"]:
            return OrderSerializer
        elif self.action in ["update", "partial_update"]:
            return OrderUpdateSerializer

    def perform_destroy(self, instance):
        # Increase product stock
        for order_detail in instance.order_details:
            order_detail.product += order_detail.quantity
            order_detail.product.save()

        # Remove order details
        instance.products.clear()

        instance.delete()
