from django.db import models
from datetime import datetime


class Instructor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True)
    is_bestseller = models.BooleanField(default=False)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    date_hired = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    instructor = models.ForeignKey(Instructor, null=True, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True)
    price = models.FloatField(default=0)
    length = models.FloatField()
    rating = models.FloatField(null=True)
    bestseller = models.BooleanField(default=False)
    subtitle = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
