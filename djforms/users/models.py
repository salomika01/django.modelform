from django.db import models


class User(models.Model):
    name: models.CharField(max_length=40)
    lastname: models.CharField(max_length=40)
    country: models.CharField
    age: models.IntegerField




