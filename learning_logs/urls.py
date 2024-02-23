"""Defines URL patterns for learning logs"""

from django.urls import re_path
from . import views

urlpatterns = [
    # Homepage
    re_path(r"^$", views.index, name="index")
]
