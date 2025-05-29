from django.urls import path
from . import views

urlpatterns = [
    path("write/", views.write_post, name="write_post"),
    path("view/<int:post_id>", views.view_post, name="view_post"),
    path("answer/submit/", views.submit_answer, name="submit_answer"),
    path("like/<int:answer_id>/", views.like_answer, name="like_answer")
]