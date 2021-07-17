from django.db import models
from django.contrib.auth.models import User
class Staff(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    speciality = models.CharField(max_length=150)
    image = models.ImageField(null=True)
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
    @property
    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name
