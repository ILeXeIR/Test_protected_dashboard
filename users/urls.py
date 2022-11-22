#URLs for app "users"

from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views import LoginView, RegisterView

app_name = "users"
urlpatterns = [
	path("logout/", auth_views.LogoutView.as_view(), name="logout"),
	path("login/", LoginView.as_view(), name="login"),
	path('register/', RegisterView.as_view(), name='register')
]

