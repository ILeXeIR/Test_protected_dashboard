from django.test import TestCase
from requests import head

DOMAIN = "http://127.0.0.1:8000/"

PAGES_NO_AUTH = ("users/login/", "users/register/")
PAGES_NO_AUTH = (DOMAIN + page for page in PAGES_NO_AUTH)

PAGES_WITH_AUTH = ("",)
PAGES_WITH_AUTH = (DOMAIN + page for page in PAGES_WITH_AUTH)

class PagesTest(TestCase):
	def test_status_code_200(self):
		for page in PAGES_NO_AUTH:
			response = head(page)
			self.assertEqual(response.status_code, 200)

	def test_status_code_302(self):
		for page in PAGES_WITH_AUTH:
			response = head(page)
			self.assertEqual(response.status_code, 302)