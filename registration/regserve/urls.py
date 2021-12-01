from django.urls import path 

from . import views 

application = 'regserve'

urlpatterns = [
    path('data/students/', )
    path('', views.index, name='index'),
]