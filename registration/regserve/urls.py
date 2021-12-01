from django.urls import path 

from . import views 

application = 'regserve'

urlpatterns = [
    path('data/students/', views.StudentListCreate.asView)
    path('', views.index, name='index'),
]