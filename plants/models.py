from statistics import mode

# from tkinter import Image
from django.db import models

# Create your models here.


class Ratings(models.Model):
    ratings = models.IntegerField(default=0, null=False)
    username = models.TextField(max_length=30, null=False)
    reason = models.TextField(null=False)
    comments = models.TextField(null=False)


class Plants(models.Model):
    CATEGORY_CHOICES = (
        ("1", "Outdoor Plants"),
        ("2", "Indoor Plants"),
        ("3", "Decorative Plants"),
        ("4", "Medicinal Plants"),
        ("5", "Onamental Plants"),
        ("6", "Aquatic Plants"),
        ("7", "Wines"),
        ("8", "Fruit Bearing Plants"),
    )

    name = models.CharField(max_length=30, null=False)
    price = models.IntegerField(default=0, null=False)
    code = models.CharField(max_length=8, null=False)
    category = models.TextField(null=False, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="images/plants")
    short_description = models.TextField(null=False)
    long_description = models.TextField(null=False)
    location = models.TextField(null=False)
    reviews = models.ForeignKey(Ratings, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
