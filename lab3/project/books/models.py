from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    publish_date = models.DateTimeField("publish date")