from django import forms
from .models import Blogs


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ["content"]
