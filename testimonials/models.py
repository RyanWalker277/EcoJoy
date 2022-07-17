from django.db import models

class Testimonials(models.Model):
    name = models.CharField(max_length=60, null=False)
    designation = models.TextField(null=False)
    testimonial = models.TextField(null=False)
    display_picture = models.ImageField(null=False)
