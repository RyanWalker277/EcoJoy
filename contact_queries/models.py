from django.db import models

class User_Messages(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    Subject = models.TextField()
    Description = models.TextField()
    

