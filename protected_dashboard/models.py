from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Result(models.Model):
	#One's results from a particular exam.
	title = models.CharField(max_length=50)
	score = models.IntegerField()
	max_score = models.IntegerField()
	student = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
	return self.title