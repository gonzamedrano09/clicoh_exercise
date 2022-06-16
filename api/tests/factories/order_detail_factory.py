import factory
import faker
from api.models.order_detail import OrderDetail
from api.models.order import Order
from api.models.product import Product


fake = faker.Faker()


class OrderDetailFactory(factory.Factory):
    class Meta:
        model = OrderDetail

    order = factory.SubFactory(Order)
    product = factory.SubFactory(Product)
    quantity = fake.pyint(min_value=1, max_value=30)
