from django.urls import path 

from . import views 

app_name = 'regserve'

urlpatterns = [
    path('/students/', views.StudentListForm.as_view(), name="students"),
    path('/createstudent/', views.StudentCreateForm.as_view(), name="create_students"),
    path('/editstudent/', views.SelectStudentToEditForm.as_view(), name="select_students_to_edit"),
    path('/<pk>/editstudent/', views.StudentEditForm.as_view(), name="edit_students"),
    path('/deletestudent/', views.SelectStudentToDeleteForm.as_view(), name="select_students_to_delete"),
    path('/<pk>/deletestudent/', views.StudentDeleteForm.as_view(), name="delete_students"),
    path('/data/students/', views.StudentListCreate.as_view()),
    path('', views.index, name='index')
]