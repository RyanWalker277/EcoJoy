from django.db import models


class Testimonials(models.Model):
    name = models.CharField(max_length=60, null=False)
    testimonial = models.TextField(null=False)
    display_picture = models.ImageField(null=False, upload_to="images/testimonials")

    def __str__(self) -> str:
        return self.name
