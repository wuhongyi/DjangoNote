from django.urls import path
from . import views
# =====电影movie的urls=====

urlpatterns = [
    path("", views.index),
]