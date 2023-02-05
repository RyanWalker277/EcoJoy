from django.db import models

# Create your models here.


class Portfolio_Images(models.Model):
    image = models.ImageField(upload_to="media/portfolio_images")
