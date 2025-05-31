from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("professionals/", views.professionals_view, name="professionals_list"),
    path("institutions/", views.institutions_view, name="institutions_list")
]