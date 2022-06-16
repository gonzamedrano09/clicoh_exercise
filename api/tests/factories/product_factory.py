import factory
import faker
from api.models.product import Product


fake = faker.Faker()


class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = fake.random_company_product()
    price = fake.pydecimal(left_digits=4, right_digits=2, positive=True)
    stock = fake.pyint(min_value=100, max_value=9999)
    is_deleted = False
