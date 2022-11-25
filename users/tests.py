from django.test import TestCase
from .models import CustomUser
from .forms import LoginForm, RegisterForm

# Create your tests here.
class CustomUserTestCase(TestCase):

	@classmethod
	def setUpTestData(cls):
		cls.user = CustomUser.objects.create(username="user1", email="user1@example.com", 
			password="Zaq12wsx")
		cls.email = cls.user._meta.get_field("email")

	def test_email_unique(self):
		#Test unique=True for email field
		real_unique = getattr(self.email, "unique")
		self.assertTrue(real_unique)

class LoginFormTests(TestCase):
	def test_username_field_label(self):
		#Test a label of username field
		form = LoginForm()
		username_label = form.fields["username"].label

		self.assertEqual(username_label, "Email Address")
