from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import DeleteView
from rest_framework import generics
from .serializers import *
from django import forms
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

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

class SelectStudentForm(forms.Form):
    student_id = forms.IntegerField()

class SelectStudentToDeleteForm(FormView, ListView):
    model = Student
    form_class = SelectStudentForm
    template_name = 'regserve/select_students_to_delete_form.html'
    student_id = 0

    def form_valid(self, form):
        self.get_student_id(form.cleaned_data)
        self.get_success_url()
        return super(SelectStudentToDeleteForm, self).form_valid(form)

    def get_student_id(self, valid_data):
        self.student_id = valid_data["student_id"]
        print("student_id_is", self.student_id)
    
    def get_success_url(self):
        return f'/regserve/{self.student_id}/deletestudent'

class SelectStudentToEditForm(FormView, ListView):
    model = Student
    form_class = SelectStudentForm
    template_name = 'regserve/select_students_to_edit_form.html'
    student_id = 0

    def form_valid(self, form):
        self.get_student_id(form.cleaned_data)
        self.get_success_url()
        return super(SelectStudentToEditForm, self).form_valid(form)

    def get_student_id(self, valid_data):
        self.student_id = valid_data["student_id"]
        print("student_id_is", self.student_id)
    
    def get_success_url(self):
        return f'/regserve/{self.student_id}/editstudent'