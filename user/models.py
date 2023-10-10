from django.db import models

class User(models.Model):
    email = models.EmailField(primary_key=True)
    password=models.CharField(max_length=255)
    role=models.CharField(max_length=255)
    pin = models.CharField(unique=True,max_length=4)
    token=models.CharField(unique=True,max_length=255)