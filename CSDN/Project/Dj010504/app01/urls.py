from django.urls import path
from . import views

# 为 app01的url设定命名空间
app_name = 'app01'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
]