import faker
from factory import django, SubFactory, LazyAttribute
from api.models.order_detail import OrderDetail
from api.models.order import Order
from api.models.product import Product


fake = faker.Faker()


class OrderDetailFactory(django.DjangoModelFactory):
    class Meta:
        model = OrderDetail

    order = SubFactory(Order)
    product = SubFactory(Product)
    quantity = LazyAttribute(fake.pyint(min_value=1, max_value=30))
