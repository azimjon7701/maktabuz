from django.db import models
from django.contrib.auth.models import User

class Parent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=30,null=True)
    description = models.CharField(max_length=100,null=True)
    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name
