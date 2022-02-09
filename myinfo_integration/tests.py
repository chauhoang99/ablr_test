from django.test import Client
from django.test import TestCase
from django.urls import reverse


class TestView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_homepage_view(self):
        self.client.get(reverse('homepage'))

    def test_myinfo_auth_view(self):
        self.client.get(reverse('auth'))

    def test_callback_view(self):
        self.client.get(reverse('callback') + '?code=testing')
