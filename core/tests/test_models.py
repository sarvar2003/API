from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Tests for models"""

    def test_create_user_with_email_successful(self):
        """Test creating user with email"""
        email = 'test@gmail.com'
        password = 'secret1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that new users email is normalized"""
        email = 'testy@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'secret5625')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpass')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'super@gmail.com',
            'superpass1234'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)