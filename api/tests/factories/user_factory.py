import faker
from factory import django, LazyAttribute
from django.contrib.auth import get_user_model


User = get_user_model()
fake = faker.Faker()


class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = User

    username = LazyAttribute(lambda x: fake.user_name())
    password = LazyAttribute(lambda x: fake.password())
    first_name = LazyAttribute(lambda x: fake.first_name())
    last_name = LazyAttribute(lambda x: fake.last_name())

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        user = manager.create_user(*args, **kwargs)
        setattr(user, "_password", kwargs["password"])
        return user
