from django.urls import reverse, resolve
from django.test import TestCase

from .views import home_page

# Create your tests here.


class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_match_resolve_path_with_reverse_url_name(self):
        resolve_path = resolve('/')
        reverse_url_name = reverse('lists:home_page')
        self.assertEqual(resolve_path, reverse_url_name)
