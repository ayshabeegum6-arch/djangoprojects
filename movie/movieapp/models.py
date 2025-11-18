from django.db import models

class Movie(models.Model):
    title=models.CharField(max_length=20)
    director=models.CharField(max_length=20)
    year=models.IntegerField(max_length=20)
    language=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images')
    description=models.TextField()

