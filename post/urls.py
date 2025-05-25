from django.urls import path
from . import views

urlpatterns = [
    path("write/", views.write_post, name="write_post")
]