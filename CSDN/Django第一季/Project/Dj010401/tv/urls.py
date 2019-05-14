
from django.urls import path
from . import views

# ===== tv的urls =====
urlpatterns = [
    path('', views.index)
]
