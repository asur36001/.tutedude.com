from django.test import TestCase
from django.urls import reverse

from .models import Movie


class MovieModelTest(TestCase):
    def test_string_representation(self):
        movie = Movie(title='Test Movie')
        self.assertEqual(str(movie), 'Test Movie')


class HomeViewTest(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
