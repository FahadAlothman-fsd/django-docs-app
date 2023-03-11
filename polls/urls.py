from django.urls import path

from . import views


question_id_route = "<int:question_id>"

app_name = "polls"

urlpatterns = [
    path("", views.index, name="index"),
    path(f"specifics/{question_id_route}/", views.detail, name="detail"),
    path(f"{question_id_route}/results/", views.results, name="results"),
    path(f"{question_id_route}/vote/", views.vote, name="vote"),
]
