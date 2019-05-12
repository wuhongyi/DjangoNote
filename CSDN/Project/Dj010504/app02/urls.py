from django.urls import path
from . import views

# 为 app02的url设定命名空间
app_name = 'app02'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
]