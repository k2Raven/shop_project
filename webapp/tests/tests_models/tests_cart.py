from django.test import TestCase

from webapp.models import Product, Category, Cart
from webapp.tests.factories.category import CategoryFactory
from webapp.tests.factories.product import ProductFactory


class CartTestCase(TestCase):
    def setUp(self):
        # product1 = Product.objects.create(
        #     title='Product 1',
        #     description='Product 1 description',
        #     price=100,
        #     balance=10,
        #     image='https://via.placeholder.com/150',
        #     category=self.category
        # )
        # product2 = Product.objects.create(
        #     title='Product 2',
        #     description='Product 2 description',
        #     price=200,
        #     balance=10,
        #     image='https://via.placeholder.com/150',
        #     category=self.category
        # )
        # product3 = Product.objects.create(
        #     title='Product 3',
        #     description='Product 3 description',
        #     price=300,
        #     balance=10,
        #     image='https://via.placeholder.com/150',
        #     category=self.category
        # )
        # self.products = [product1, product2, product3]
        self.products = [
            ProductFactory.create(price=100, category=self.category),
            ProductFactory.create(price=200, category=self.category),
            ProductFactory.create(price=300, category=self.category),
        ]

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.category = CategoryFactory.create()
        return super().setUpClass()


    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()

    def test_get_full_total_price(self):
        for product in self.products:
            Cart.objects.create(product=product, qty=2)
        result = Cart.get_full_total_price()
        self.assertEqual(result, 1200)
