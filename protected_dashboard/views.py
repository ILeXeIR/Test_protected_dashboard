#from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

# Create your views here.
#@login_required
#def index(request):
#	return render(request, "protected_dashboard/index.html")

class ResultsView(LoginRequiredMixin, ListView):
	model = Result
	template_name = "protected_dashboard/index.html"
	context_object_name = "results"

	def get_queryset(self):
		return Result.objects.filter(student=self.request.user)