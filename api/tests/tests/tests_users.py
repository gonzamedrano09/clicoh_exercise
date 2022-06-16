import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.tests.utils import get_authenticated_api_client
from api.tests.factories.user_factory import UserFactory


class UserTests(APITestCase):

    def setUp(self):

        self.user = UserFactory()
        self.client = get_authenticated_api_client(self.user.username, self.user._password)
        self.anonymous_client = APIClient()

    def test_create_user(self):
        new_user = UserFactory.build()
        data = {
            "username": new_user.username,
            "password": new_user.password,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name
        }
        
        response = self.client.post(reverse("users-list"), data)
        result = json.loads(response.content)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", result)
        self.assertIn("username", result)
        self.assertIn("first_name", result)
        self.assertIn("last_name", result)

        del result["id"]
        del data["password"]

        self.assertEqual(result, data)

    def test_change_password_user(self):
        other_user = UserFactory.build()
        data = {
            "password": other_user.password,
        }

        response = self.client.post(reverse("users-change-password"), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {
            "username": self.user.username,
            "password": other_user.password
        }
        response = self.anonymous_client.post(reverse("token_obtain_pair"), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_user(self):
        data = {
            "username": self.user.username,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name
        }

        response = self.client.get(reverse("users-list"))
        result = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("id", result)
        self.assertIn("username", result)
        self.assertIn("first_name", result)
        self.assertIn("last_name", result)

        del result["id"]

        self.assertEqual(result, data)

    def test_destroy_user(self):
        response = self.client.delete(reverse("users-list"))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
