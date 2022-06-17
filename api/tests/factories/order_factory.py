import faker
from factory import django, LazyAttribute
from pytz import timezone
from django.conf import settings
from api.models.order import Order


fake = faker.Faker()


class OrderFactory(django.DjangoModelFactory):
    class Meta:
        model = Order

    date_time = LazyAttribute(lambda x: fake.date_time(timezone(settings.TIME_ZONE)))

