from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    principals = models.CharField(max_length=20)

    def __str__(self):
        return reverse('basic_app:detail', kwargs={'pk': self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=CASCADE)