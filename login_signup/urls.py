from django.urls import path, include
from login_signup import views
from .views import *

urlpatterns = [
    path("", views.google, name="login"),
]
