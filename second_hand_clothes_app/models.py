from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class ClothesList(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='image/')
    price = models.IntegerField(default=0)
    seller = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=200)
    comment = ArrayField(models.TextField(blank=True), blank=True)

regular_user = {"username": "regular", "password": "regular"}
admin_user = {"username": "admin", "password": "admin"}

        
    