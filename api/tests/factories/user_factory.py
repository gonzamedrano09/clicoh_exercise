import factory
import faker
from django.contrib.auth import get_user_model


User = get_user_model()
fake = faker.Faker()


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = fake.user_name()
    password = fake.password()
    first_name = fake.first_name()
    last_name = fake.last_name()

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)
