from django.urls import path
from . import views

#  ==== home下的urls ====
urlpatterns = [
    path('', views.index)
]