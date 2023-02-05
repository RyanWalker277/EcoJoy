from django.db import models


class User_Messages(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=60, null=True)
    Subject = models.CharField(max_length=90, null=True)
    Description = models.TextField(null=True)
