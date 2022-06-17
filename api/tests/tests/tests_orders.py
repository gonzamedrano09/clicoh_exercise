import json
from decimal import Decimal
from datetime import datetime
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from api.tests.utils import get_authenticated_api_client
from api.tests.factories.user_factory import UserFactory
from api.tests.factories.order_factory import OrderFactory
from api.tests.factories.product_factory import ProductFactory
from api.tests.factories.order_detail_factory import OrderDetailFactory
from api.tests.factories.order_with_2_products_factory import OrderWith2ProductsFactory


class OrderTests(APITestCase):

    def setUp(self):
        self.order = OrderWith2ProductsFactory()
        self.user = UserFactory()
        self.client = get_authenticated_api_client(self.user.username, self.user._password)

    def test_create_order(self):
        new_order = OrderFactory.build()
        new_order_detail_1 = OrderDetailFactory.build(product=ProductFactory())
        new_order_detail_2 = OrderDetailFactory.build(product=ProductFactory())
        data = {
            "date_time": datetime.strftime(new_order.date_time, "%Y-%m-%dT%H:%M:%SZ"),
            "order_details": [
                {
                    "product": new_order_detail_1.product.id,
                    "quantity": new_order_detail_1.quantity
                },
                {
                    "product": new_order_detail_2.product.id,
                    "quantity": new_order_detail_2.quantity
                }
            ]
        }

        response = self.client.post(reverse("orders-list"), json.dumps(data), content_type="application/json")
        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", result)
        self.assertIn("date_time", result)
        self.assertIn("order_details", result)

        del result["id"]
        del result["total"]
        del result["total_usd"]
        result["order_details"][0] = {
            "product": result["order_details"][0]["product"]["id"],
            "quantity": result["order_details"][0]["quantity"]
        }
        result["order_details"][1] = {
            "product": result["order_details"][1]["product"]["id"],
            "quantity": result["order_details"][1]["quantity"]
        }

        self.assertEqual(result, data)

    def test_update_order(self):
        other_order = OrderFactory.build()
        other_order_detail_1 = OrderDetailFactory.build(product=ProductFactory())
        other_order_detail_2 = OrderDetailFactory.build(product=ProductFactory())
        data = {
            "date_time": datetime.strftime(other_order.date_time, "%Y-%m-%dT%H:%M:%SZ"),
            "order_details": [
                {
                    "product": other_order_detail_1.product.id,
                    "quantity": other_order_detail_1.quantity
                },
                {
                    "product": other_order_detail_2.product.id,
                    "quantity": other_order_detail_2.quantity
                }
            ]
        }

        response = self.client.put(reverse("orders-detail", kwargs={"pk": self.order.id}), json.dumps(data),
                                   content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_order(self):
        other_order = OrderFactory.build()
        data = {
            "date_time": datetime.strftime(other_order.date_time, "%Y-%m-%dT%H:%M:%SZ")
        }

        response = self.client.patch(reverse("orders-detail", kwargs={"pk": self.order.id}), json.dumps(data),
                                     content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_product(self):
        data = {
            "id": self.order.id,
            "date_time": datetime.strftime(self.order.date_time, "%Y-%m-%dT%H:%M:%SZ"),
            "order_details": [
                {
                    "product": {
                        "id": self.order.order_details.first().product.id,
                        "name": self.order.order_details.first().product.name,
                        "price": self.order.order_details.first().product.price,
                        "stock": self.order.order_details.first().product.stock
                    },
                    "quantity": self.order.order_details.first().quantity
                },
                {
                    "product": {
                        "id": self.order.order_details.last().product.id,
                        "name": self.order.order_details.last().product.name,
                        "price": self.order.order_details.last().product.price,
                        "stock": self.order.order_details.last().product.stock
                    },
                    "quantity": self.order.order_details.last().quantity
                },
            ]
        }

        response = self.client.get(reverse("orders-detail", kwargs={"pk": self.order.id}))
        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("id", result)
        self.assertIn("date_time", result)
        self.assertIn("order_details", result)

        del result["total"]
        del result["total_usd"]
        result["order_details"][0]["product"]["price"] = Decimal(result["order_details"][0]["product"]["price"])
        result["order_details"][1]["product"]["price"] = Decimal(result["order_details"][1]["product"]["price"])

        self.assertEqual(result, data)

    def test_list_products(self):
        other_order = OrderWith2ProductsFactory()
        data = [
            {
                "id": self.order.id,
                "date_time": datetime.strftime(self.order.date_time, "%Y-%m-%dT%H:%M:%SZ"),
                "order_details": [
                    {
                        "product": {
                            "id": self.order.order_details.first().product.id,
                            "name": self.order.order_details.first().product.name,
                            "price": self.order.order_details.first().product.price,
                            "stock": self.order.order_details.first().product.stock
                        },
                        "quantity": self.order.order_details.first().quantity
                    },
                    {
                        "product": {
                            "id": self.order.order_details.last().product.id,
                            "name": self.order.order_details.last().product.name,
                            "price": self.order.order_details.last().product.price,
                            "stock": self.order.order_details.last().product.stock
                        },
                        "quantity": self.order.order_details.last().quantity
                    },
                ]
            },
            {
                "id": other_order.id,
                "date_time": datetime.strftime(other_order.date_time, "%Y-%m-%dT%H:%M:%SZ"),
                "order_details": [
                    {
                        "product": {
                            "id": other_order.order_details.first().product.id,
                            "name": other_order.order_details.first().product.name,
                            "price": other_order.order_details.first().product.price,
                            "stock": other_order.order_details.first().product.stock
                        },
                        "quantity": other_order.order_details.first().quantity
                    },
                    {
                        "product": {
                            "id": other_order.order_details.last().product.id,
                            "name": other_order.order_details.last().product.name,
                            "price": other_order.order_details.last().product.price,
                            "stock": other_order.order_details.last().product.stock
                        },
                        "quantity": other_order.order_details.last().quantity
                    },
                ]
            }
        ]

        response = self.client.get(reverse("orders-list"))
        result = json.loads(response.content)["results"]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("id", result[0])
        self.assertIn("date_time", result[0])
        self.assertIn("order_details", result[0])
        self.assertIn("id", result[1])
        self.assertIn("date_time", result[1])
        self.assertIn("order_details", result[1])

        del result[0]["total"]
        del result[0]["total_usd"]
        result[0]["order_details"][0]["product"]["price"] = Decimal(result[0]["order_details"][0]["product"]["price"])
        result[0]["order_details"][1]["product"]["price"] = Decimal(result[0]["order_details"][1]["product"]["price"])
        del result[1]["total"]
        del result[1]["total_usd"]
        result[1]["order_details"][0]["product"]["price"] = Decimal(result[1]["order_details"][0]["product"]["price"])
        result[1]["order_details"][1]["product"]["price"] = Decimal(result[1]["order_details"][1]["product"]["price"])

        self.assertEqual(result, data)

    def test_destroy_order(self):
        response = self.client.delete(reverse("orders-detail", kwargs={"pk": self.order.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
