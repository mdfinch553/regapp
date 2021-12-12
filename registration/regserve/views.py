from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import DeleteView
from rest_framework import generics
from .serializers import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

def index(request):
    return HttpResponse("Hello from django backend")

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentListForm(ListView):
    model = Student

class StudentCreateForm(CreateView, ListView):
    model = Student
    fields = ['firstname', 'lastname', 'idnumber', 'schoolyear', 'major', 'gpa']

class StudentEditForm(UpdateView):
    model = Student
    template_name = 'regserve/student_edit_form.html'
    fields = ['firstname', 'lastname', 'idnumber', 'schoolyear', 'major', 'gpa']
class StudentDeleteForm(DeleteView):
    model = Student
    template_name = 'regserve/student_delete_form.html'
    success_url="/regserve/students/"