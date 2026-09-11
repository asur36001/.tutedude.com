from django.test import TestCase
from django.urls import reverse

from .models import Movie
from .models import ShortVideo


class MovieModelTest(TestCase):
    def test_string_representation(self):
        movie = Movie(title='Test Movie')
        self.assertEqual(str(movie), 'Test Movie')


class HomeViewTest(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class ShortsAnalyticsTest(TestCase):
    def setUp(self):
        self.short = ShortVideo.objects.create(
            title='A great hook',
            youtube_url='https://www.youtube.com/shorts/abc123',
            views=1000,
            likes=80,
            comments=20,
        )

    def test_dashboard_shows_stored_metrics(self):
        response = self.client.get(reverse('shorts_dashboard'))
        self.assertContains(response, '1000')
        self.assertContains(response, '10.0%')

    def test_analytics_api_returns_no_playback_controls(self):
        response = self.client.get(reverse('shorts_analytics_api'))
        self.assertEqual(response.status_code, 200)
        short = response.json()['shorts'][0]
        self.assertEqual(short['title'], 'A great hook')
        self.assertEqual(short['engagement_rate'], 10.0)
