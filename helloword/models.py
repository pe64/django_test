# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
     name=models.CharField(max_length=20)


class Employee1(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Company(models.Model):
    full_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    tel = models.CharField(max_length=15,blank=True)

class Product(models.Model):
    product_name = models.CharField(max_length=30)
    #price = models.FloatField()
    stock = models.IntegerField(max_length=5)
    company = models.ForeignKey(Company)

class userinfo(models.Model):
    USER_TYPE_LIST = (
        (1, 'user'),
        (2, 'admin'),
    )

    user_type = models.IntegerField(choices=USER_TYPE_LIST, default=1)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    memo = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to="upload")