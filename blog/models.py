from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import (
    FroalaField,
)  # Using FroalaField for writing perfect blogs


class Blogs(models.Model):
    title = models.TextField(null=False)
    content = FroalaField()  # Using FroalaField for writing perfect blogs
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, blank=True, null=True
    )
    designation = models.CharField(max_length=60, null=False)
    author_fb = models.URLField(null=False)
    author_google = models.URLField(null=False)
    author_instagram = models.URLField(null=False)
    author_twitter = models.URLField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="images/blog_thumbnails")

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"


class Comments(models.Model):
    blog = models.ForeignKey(
        Blogs, on_delete=models.CASCADE, default=None, blank=True, null=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, blank=True, null=True
    )  # for authenticated user's comment
    anonymous_user = models.CharField(
        max_length=100, null=True, blank=True
    )  # for comment by anonymous user
    person_email = models.EmailField(
        max_length=100, null=True, blank=True
    )  # for comment by anonymous user
    comment = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        if self.user is None:
            return f"On '{self.blog.title}' by {self.anonymous_user}"
        return f"On '{self.blog.title}' by {self.user}"
