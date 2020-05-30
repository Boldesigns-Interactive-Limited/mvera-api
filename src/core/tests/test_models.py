from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):

  def test_create_user_with_email_successful(self):
    """ Test that creating a new user with an email is successful"""
    email = 'test@mvera.co.ke'
    password = 'test@123'
    first_name = 'Odhiambo'
    last_name = 'Ochieng'
    phone = '254710000000'

    user = get_user_model().objects.create_user(
      email=email, password=password
    )

    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))


  def test_new_user_address_normalized(self):
    """Test that the email for a new user is normalized"""
    email = 'test@GMAIL.COM'
    user = get_user_model().objects.create_user(email=email)

    self.assertEqual(user.email, email.lower())

  def test_new_user_invalid_email(self):
    """Test creating user with no email raises error"""
    with self.assertRaises(ValueError):
      get_user_model().objects.create_user(None, '90320932')

  def test_create_new_super_user(self):
    """ Test creating a new superuser """
    user = get_user_model().objects.create_superuser(
      'test@gmail.com',
      'pass123'
    )

    self.assertTrue(user.is_superuser)
    self.assertTrue(user.is_staff)