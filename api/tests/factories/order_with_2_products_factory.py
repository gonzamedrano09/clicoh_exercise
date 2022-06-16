import factory
from api.tests.factories.order_factory import OrderFactory
from api.tests.factories.order_detail_factory import OrderDetailFactory


class OrderWith2ProductsFactory(OrderFactory):

    order_detail_1 = factory.RelatedFactory(
        OrderDetailFactory,
        factory_related_name="order"
    )
    order_detail_2 = factory.RelatedFactory(
        OrderDetailFactory,
        factory_related_name="order"
    )
