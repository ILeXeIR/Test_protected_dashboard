#URLs for app "protected_dashboard"

from django.urls import path
from . import views

app_name = "protected_dashboard"
urlpatterns = [
	path("", views.index, name="index"),
]
