from django.urls import path
from . import views

urlpatterns = [
    path("write/", views.write_post, name="write_post"),
    path("view/<int:post_id>", views.view_post, name="view_post"),
    path("answer/submit/", views.submit_answer, "submit_answer")
]