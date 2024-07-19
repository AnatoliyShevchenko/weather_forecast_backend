# Django
from django.test import TestCase

# Local
from auths.models import Client
from .models import Search


class SearchModelTestCase(TestCase):

    def setUp(self):
        self.client = Client.objects.create(
            email="test@example.com", username="testuser", 
            password="password"
        )

    def test_search_model_creation(self):
        search = Search.objects.create(
            client=self.client, city="New York", count=10
        )
        self.assertEqual(search.client, self.client)
        self.assertEqual(search.city, "New York")
        self.assertEqual(search.count, 10)

    def test_search_model_str_method(self):
        search = Search.objects.create(
            client=self.client, city="Paris", count=5
        )
        self.assertEqual(str(search), f"{search.client} Paris 5")
