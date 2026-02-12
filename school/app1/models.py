from  django.contrib.auth.models import User
from django.db import models
class School(models.Model):

    school_name=models.CharField(max_length=50)
    principal=models.CharField(max_length=30)
    place=models.CharField(max_length=40)



class Student(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    place=models.CharField(max_length=30)
    school_name = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True,related_name="students")
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)