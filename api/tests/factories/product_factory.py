import faker
from factory import django, LazyAttribute
from api.models.product import Product


fake = faker.Faker(["en_PH"])


class ProductFactory(django.DjangoModelFactory):
    class Meta:
        model = Product

    name = LazyAttribute(lambda x: fake.random_company_product())
    price = LazyAttribute(lambda x: fake.pydecimal(left_digits=4, right_digits=2, positive=True))
    stock = LazyAttribute(lambda x: fake.pyint(min_value=100, max_value=9999))
    is_deleted = False
