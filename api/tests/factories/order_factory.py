import factory
import faker
from api.models.order import Order


fake = faker.Faker()


class OrderFactory(factory.Factory):
    class Meta:
        model = Order

    date_time = fake.date_time()

