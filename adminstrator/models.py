from django.db import models


# Create your models here60


class mydata(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    utype=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)