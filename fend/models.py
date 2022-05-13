from django.db import models
from django import forms


class People_Details(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    image = models.ImageField(upload_to='test')



class SearchImages(models.Model):
    image = models.ImageField(upload_to='test/searched')