from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    principals = models.CharField(max_length=20)

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=CASCADE)