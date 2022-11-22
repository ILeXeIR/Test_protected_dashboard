from django.db import models
from users.models import CustomUser

# Create your models here.
class Result(models.Model):
	#One's results from a particular exam.
	title = models.CharField(max_length=50)
	score = models.IntegerField()
	max_score = models.IntegerField()
	student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

def __str__(self):
	return self.title