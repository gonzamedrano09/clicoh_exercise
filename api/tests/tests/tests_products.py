import json
from decimal import Decimal
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from api.tests.utils import get_authenticated_api_client
from api.tests.factories.user_factory import UserFactory
from api.tests.factories.product_factory import ProductFactory


class ProductTests(APITestCase):

    def setUp(self):
        self.product = ProductFactory()
        self.user = UserFactory()
        self.client = get_authenticated_api_client(self.user.username, self.user._password)

    def test_create_product(self):
        new_product = ProductFactory.build()
        data = {
            "name": new_product.name,
            "price": new_product.price,
            "stock": new_product.stock
        }

        response = self.client.post(reverse("products-list"), data)
        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", result)
        self.assertIn("name", result)
        self.assertIn("price", result)
        self.assertIn("stock", result)

        del result["id"]
        result["price"] = Decimal(result["price"])

        self.assertEqual(result, data)

    def test_update_product(self):
        other_product = ProductFactory.build()
        data = {
            "name": other_product.name,
            "price": other_product.price
        }

        response = self.client.put(reverse("products-detail", kwargs={"pk": self.product.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_product(self):
        other_product = ProductFactory.build()
        data = {
            "price": other_product.price
        }

        response = self.client.patch(reverse("products-detail", kwargs={"pk": self.product.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_stock(self):
        other_product = ProductFactory.build()
        data = {
            "stock": other_product.stock,
        }

        response = self.client.put(reverse("products-update-stock", kwargs={"pk": self.product.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_product(self):
        data = {
            "id": self.product.id,
            "name": self.product.name,
            "price": self.product.price,
            "stock": self.product.stock
        }

        response = self.client.get(reverse("products-detail", kwargs={"pk": self.product.id}))
        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("id", result)
        self.assertIn("name", result)
        self.assertIn("price", result)
        self.assertIn("stock", result)

        result["price"] = Decimal(result["price"])

        self.assertEqual(result, data)

    def test_list_products(self):
        other_product = ProductFactory()
        data = [
            {
                "id": self.product.id,
                "name": self.product.name,
                "price": self.product.price,
                "stock": self.product.stock
            },
            {
                "id": other_product.id,
                "name": other_product.name,
                "price": other_product.price,
                "stock": other_product.stock
            }
        ]

        response = self.client.get(reverse("products-list"))
        result = json.loads(response.content)["results"]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("id", result[0])
        self.assertIn("name", result[0])
        self.assertIn("price", result[0])
        self.assertIn("stock", result[0])
        self.assertIn("id", result[1])
        self.assertIn("name", result[1])
        self.assertIn("price", result[1])
        self.assertIn("stock", result[1])

        result[0]["price"] = Decimal(result[0]["price"])
        result[1]["price"] = Decimal(result[1]["price"])

        self.assertEqual(result, data)

    def test_destroy_product(self):
        response = self.client.delete(reverse("products-detail", kwargs={"pk": self.product.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
