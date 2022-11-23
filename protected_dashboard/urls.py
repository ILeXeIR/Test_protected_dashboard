#URLs for app "protected_dashboard"

from django.urls import path
from .views import *

app_name = "protected_dashboard"
urlpatterns = [
	path("", ResultsView.as_view(), name="index"),
]
