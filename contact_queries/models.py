from django.db import models

class User_Messages(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(null=False)
    Subject = models.TextField(null=False)
    Description = models.TextField(null=False)

