from django.urls import path, include
from .views import *

urlpatterns = [
    path("create/", create_blog, name="createBlog"),
    path("<int:id>/comments/", show_comments, name="showComments"),
    path("", blog, name="allBlog"),
    path("<int:id>", blogpage, name="blogpost"),
]
