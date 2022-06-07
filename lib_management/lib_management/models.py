#####library.model.py
from django.db import models

# Create your models here.
class Books(models.Model):
	id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=30)
	position = models.IntegerField()
	state = 1
