from rest_framework import serializers
from api.models.order import Order
from api.models.order_detail import OrderDetail
from api.serializers.order_detail_serializer.order_detail_serializer import OrderDetailSerializer


class OrderUpdateSerializer(serializers.ModelSerializer):

    order_details = OrderDetailSerializer(many=True)

    total = serializers.SerializerMethodField()
    total_usd = serializers.SerializerMethodField()

    def get_total(self, obj):
        return obj.get_total

    def get_total_usd(self, obj):
        return obj.get_total_usd

    def validate_order_details(self, value):
        if len(value) == 0:
            raise serializers.ValidationError("At least one order detail is needed.")

        products = []
        for order_detail in value:
            product = order_detail.get("product")
            if product in products:
                raise serializers.ValidationError("There can only be one order detail per product.")
            products.append(product)
        return value

    def update(self, instance, validated_data):
        # Check if new order details were sent to pop order details
        exists_order_details = validated_data.get("order_details") is not None
        order_details_data = []
        if exists_order_details:
            order_details_data = validated_data.pop("order_details")

        # Update order
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Check if new order details prevent changes due to a partial update
        if exists_order_details:

            # Increase product stock
            for order_detail in instance.order_details.all():
                order_detail.product.stock += order_detail.quantity
                order_detail.product.save()

            # Remove old order details
            instance.products.clear()

            # Generate new order details
            for order_detail_data in order_details_data:
                order_detail = OrderDetail.objects.create(order=instance, **order_detail_data)

                # Update stock after product increase
                order_detail.product.refresh_from_db(fields=["stock"])

                # Reduce the stock of products
                order_detail.product.stock -= order_detail.quantity
                order_detail.product.save()

        return instance

    class Meta:
        model = Order
        fields = ["id", "date_time", "order_details", "total", "total_usd"]
