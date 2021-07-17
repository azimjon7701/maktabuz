from django.db import models
from django.contrib.auth.models import User
class Region(models.Model):
    region_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200,null=True)
    admin = models.OneToOneField(User,on_delete=models.CASCADE)

