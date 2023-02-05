from django.urls import path, include
from contact_queries import views
from .views import *

urlpatterns = [path("submit", views.contact_index, name="submit_message")]
