from django.db import models
from django.utils import timezone

# Create your models here.

class Cardiology(models.Model):
	title = models.CharField(max_length=255, help_text="Enter Patient Name")

class Endocrinology(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
