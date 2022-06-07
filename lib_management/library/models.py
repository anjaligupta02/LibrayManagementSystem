#####library.model.py
from django.db import models

# Create your models here.
class Books(models.Model):
	id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=30)
	position = models.IntegerField()
	state = 1
	path = models.CharField(max_length=200)


class BookDetail(models.Model):
	BOOK_ID = models.IntegerField()
	TITLE = models.CharField(max_length=30)
	NAME = models.CharField(max_length=30)
	POSITION = models.CharField(max_length=10)


