import faker
from factory import django, LazyAttribute
from api.models.order import Order


fake = faker.Faker()


class OrderFactory(django.DjangoModelFactory):
    class Meta:
        model = Order

    date_time = LazyAttribute(lambda x: fake.date_time())

