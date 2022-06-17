import faker
from factory import django, SubFactory, LazyAttribute
from api.models.order_detail import OrderDetail
from api.tests.factories.order_factory import OrderFactory
from api.tests.factories.product_factory import ProductFactory


fake = faker.Faker()


class OrderDetailFactory(django.DjangoModelFactory):
    class Meta:
        model = OrderDetail

    order = SubFactory(OrderFactory)
    product = SubFactory(ProductFactory)
    quantity = LazyAttribute(lambda x: fake.pyint(min_value=1, max_value=30))
