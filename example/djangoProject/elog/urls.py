from django.urls import path

from . import views

app_name = 'elog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sortRunType/', views.IndexView.as_view(), name='indexRunTypeSorted'),
    path('logForm/', views.logForm, name="logForm"),
    path('logForm/prevLog/', views.logFormWithPrev, name="logFormWithPrev"),
    path('logForm/addLog/', views.addLog, name="addLog"),
    path('logDetail/<int:pk>/', views.DetailView.as_view(), name="logDetail"),
    path('logDetail/<int:pk>/modifyLog/', views.modifyLog, name="modifyLog"),
    path('numData/', views.numData, name="numData"),
    path('graph/', views.graph, name="graph"),
]
