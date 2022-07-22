from tkinter import image_types
from django.db import models
from django.forms import DateTimeField

# Create your models here.

class Comments(models.Model):
    Name = models.CharField(max_length=60 , default=0 , null=False)
    Email = models.EmailField(null=False)
    Comment = models.TextField(null=False)

class Blogs(models.Model):
    Title = models.TextField(null=False)
    Content = models.TextField(null=False)
    Author = models.CharField(max_length=60, null=False)
    designation = models.CharField(max_length=60, null=False)
    author_fb = models.URLField(null=False)
    author_google = models.URLField(null=False)
    author_instagram = models.URLField(null=False)
    author_twitter = models.URLField(null=False)
    comments = models.ForeignKey(Comments , on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images/blog_thumbnails')