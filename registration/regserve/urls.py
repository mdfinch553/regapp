from django.urls import path 

from . import views 

app_name = 'regserve'

urlpatterns = [
    path('/students/', views.StudentListForm.as_view(), name="students"),
    path('/createstudent/', views.StudentCreateForm.as_view(), name="create_students"),
    path('/data/students/', views.StudentListCreate.as_view()),
    path('', views.index, name='index')
]