from django.db import models
from region.models import Region,User
from staff.models import Staff
from parents.models import Parent
class School(models.Model):
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    school_number = models.IntegerField()
    school_name = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
class Class(models.Model):
    class_number = models.IntegerField()
    class_char = models.CharField(max_length=10)
    curator = models.ForeignKey(Staff,on_delete=models.SET_NULL,null=True)
class Pupil(models.Model):
    clas = models.ForeignKey(Class,on_delete=models.SET_NULL,null=True)
    full_name = models.CharField(max_length=100)
    parent = models.ForeignKey(Parent,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(null=True)
    birth_day = models.DateField(null=True)
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
class New(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=200)
    published_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=True)
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
class Event(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=True)
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
class Course(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=True)
    mentor = models.ForeignKey(Staff,on_delete=models.SET_NULL,null=True)
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
class Subject(models.Model):
    subject_name = models.CharField(max_length=50)

