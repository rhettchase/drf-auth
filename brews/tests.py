from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Brew


class BrewTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        cls.testuser1.save()

        test_brew = Brew.objects.create(
            owner=cls.testuser1,
            name="Pale Ale",
            brew_type="PA",
            brewery="Sierra Nevada",
            description="Like Pale Ale, hopped to perfection and unshakable.",
        )
        test_brew.save()

    def setUp(self):
        # Log in testuser1 before each test
        self.client.force_authenticate(user=self.testuser1)

    def test_brews_model(self):
        brew = Brew.objects.get(id=1)
        actual_owner = str(brew.owner)
        actual_name = str(brew.name)
        actual_brew_type = str(brew.brew_type)
        actual_brewery = str(brew.brewery)
        actual_description = str(brew.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Pale Ale")
        self.assertEqual(actual_brew_type, "PA")
        self.assertEqual(actual_brewery, "Sierra Nevada")
        self.assertEqual(
            actual_description, "Like Pale Ale, hopped to perfection and unshakable."
        )

    def test_get_brew_list(self):
        url = reverse("brew_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        brews = response.data
        self.assertEqual(len(brews), 1)
        self.assertEqual(brews[0]["name"], "Pale Ale")

    def test_get_brew_by_id(self):
        url = reverse("brew_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        brew = response.data
        self.assertEqual(brew["name"], "Pale Ale")

    def test_create_brew(self):
        url = reverse("brew_list")
        data = {
            "owner": 1,
            "name": "beer",
            "brew_type": "IPA",
            "brewery": "Stone",
            "description": "the best hops"
            }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        brews = Brew.objects.all()
        self.assertEqual(len(brews), 2)
        self.assertEqual(Brew.objects.get(id=2).name, "beer")

    def test_update_brew(self):
        url = reverse("brew_detail", args=(1,))
        data = {
            "id:": 1,
            "owner": 1,
            "name": "blueberry IPA",
            "brew_type": "IPA",
            "brewery": "Athletic",
            "description": "the best hops"
            }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        brew = Brew.objects.get(id=1)
        self.assertEqual(brew.name, data["name"])
        self.assertEqual(brew.owner.id, data["owner"])
        self.assertEqual(brew.description, data["description"])

    def test_delete_brew(self):
        url = reverse("brew_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        brews = Brew.objects.all()
        self.assertEqual(len(brews), 0)
        

