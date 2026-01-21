from django.test import TestCase
from http import HTTPStatus

from webapp.models import Cart
from webapp.tests.factories.category import CategoryFactory
from webapp.tests.factories.product import ProductFactory


class CartTestCase(TestCase):
    def setUp(self):
        self.products = [
            ProductFactory.create(price=100, balance=2, category=self.category),
            ProductFactory.create(price=200, balance=4,  category=self.category),
            ProductFactory.create(price=300, balance=0,  category=self.category),
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

    def test_add_to_cart__product_balance_gt_zero_success(self):
        response = self.client.get(f'/products/{self.products[0].id}/add_to_cart/')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Cart.objects.count(), 1)
        self.assertEqual(Cart.objects.first().product, self.products[0])
        self.assertEqual(Cart.objects.first().qty, 1)

        response = self.client.get(f'/products/{self.products[0].id}/add_to_cart/')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Cart.objects.count(), 1)
        self.assertEqual(Cart.objects.first().qty, 2)

        response = self.client.get(f'/products/{self.products[0].id}/add_to_cart/')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Cart.objects.count(), 1)
        self.assertEqual(Cart.objects.first().qty, 2)

    def test_add_to_cart__product_balance_eq_zero_failure(self):
        response = self.client.get(f'/products/{self.products[2].id}/add_to_cart/')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Cart.objects.count(), 0)
