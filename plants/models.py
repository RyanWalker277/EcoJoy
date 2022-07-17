from statistics import mode
from tkinter import Image
from django.db import models

# Create your models here.


class Ratings(models.Model):
    ratings = models.IntegerField(default=0, null=False)
    username = models.TextField(max_length=30, null=False)
    reason = models.TextField(null=False)
    comments = models.TextField(null=False)


class Plants(models.Model):

    CATEGORY_CHOICES = (
        ("1", "cat1"),
        ("2", "cat2"),
        ("3", "cat3"),
        ("4", "cat4"),
        ("5", "cat5"),
        ("6", "cat6"),
        ("7", "cat7"),
        ("8", "cat8"),
    )

    name = models.CharField(max_length=30, null=False)
    price = models.IntegerField(default=0, null=False)
    code = models.CharField(max_length=8, null=False)
    category = models.TextField(null=False,  choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='media/images')
    short_description = models.TextField(null=False)
    long_description = models.TextField(null=False)
    reviews = models.ForeignKey(Ratings , on_delete = models.CASCADE)
