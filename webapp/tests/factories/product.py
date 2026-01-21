import factory
from factory.django import DjangoModelFactory

from webapp.models import Product


class ProductFactory(DjangoModelFactory):
    title = factory.Sequence(lambda n: f'Product {n}')
    description = factory.Faker('text')
    price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    image = factory.Faker('url')
    balance = factory.Faker('pyint', min_value=10, max_value=100)
    category = factory.SubFactory('webapp.tests.factories.category.CategoryFactory')


    class Meta:
        model = Product
