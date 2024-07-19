# Django
from django.test import TestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class ClientManagerTestCase(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            email="test@example.com", username="testuser", 
            password="password"
        )
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(
            email="admin@example.com", username="admin", 
            password="adminpassword"
        )
        self.assertEqual(superuser.email, "admin@example.com")
        self.assertEqual(superuser.username, "admin")
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_active)

class ClientModelTestCase(TestCase):

    def test_client_model(self):
        client = User.objects.create_user(
            email="client@example.com", username="clientuser", 
            password="clientpassword"
        )
        self.assertEqual(client.email, "client@example.com")
        self.assertEqual(client.username, "clientuser")
        self.assertEqual(str(client), "clientuser client@example.com")
        self.assertFalse(client.is_staff)
        self.assertFalse(client.is_superuser)
        self.assertTrue(client.is_active)
