from pyexpat import model
from django.db import models

# Create your models here.

class Comments(models.Model):
    Name = models.CharField(max_length=60 , default=0 , null=False)
    Email = models.EmailField(null=False)
    Comment = models.TextField(null=False)

class Blogs(models.Model):
    Title = models.CharField(max_length=60, null=False)
    Content = models.TextField(null=False)
    Author = models.CharField(max_length=60, null=False)
    author_fb = models.URLField(null=False)
    author_google = models.URLField(null=False)
    author_instagram = models.URLField(null=False)
    author_twitter = models.URLField(null=False)
    comments = models.ForeignKey(Comments , on_delete = models.CASCADE)