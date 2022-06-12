from rest_framework import serializers
from api.models.order import Order
from api.models.order_detail import OrderDetail
from api.serializers.order_detail_serializer.order_detail_serializer import OrderDetailSerializer


class OrderUpdateSerializer(serializers.ModelSerializer):

    order_details = OrderDetailSerializer(many=True)

    def validate_order_details(self, value):
        products = []
        for order_detail in value:
            product = order_detail.get("product")
            if product in products:
                raise serializers.ValidationError("There can only be one order detail per product.")
            products.append(product)
        return value

    def update(self, instance, validated_data):
        for order_detail in instance.order_details:
            order_detail.product += order_detail.quantity
            order_detail.product.save()
        instance.products.clear()

        order_details_data = validated_data.pop("order_details")

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        for order_detail_data in order_details_data:
            order_detail = OrderDetail.objects.create(order=instance, **order_detail_data)
            order_detail.product.stock -= order_detail.quantity
            order_detail.product.save()

        return instance

    class Meta:
        model = Order
        fields = ["id", "date_time", "order_details"]
