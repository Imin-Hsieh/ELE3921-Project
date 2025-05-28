from django.urls import path
from . import views

urlpatterns = [
    path("view/<int:post_id>", views.view_profile, name="view_profile")
]