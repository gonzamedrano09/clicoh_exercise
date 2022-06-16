from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


def get_authenticated_api_client(username, password):
    client = APIClient()

    data = {
        "username": username,
        "password": password
    }
    response = client.post(reverse("token_obtain_pair"), data)

    if response.status_code == status.HTTP_200_OK:
        client.credentials(HTTP_AUTHORIZATION="Bearer %s" % response.data["access"])
        return client
    else:
        return None
