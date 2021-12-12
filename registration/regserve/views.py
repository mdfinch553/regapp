from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import DeleteView
from rest_framework import generics
from .serializers import *
from django import forms
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

def index(request):
    '''
    returns httpresponse from django backend
    '''
    return HttpResponse("Hello from django backend")

class StudentListCreate(generics.ListCreateAPIView):
    '''
    get list of students
    '''
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentListForm(ListView):
    '''
    Class that uses django ListView to display students
    '''
    model = Student

class StudentCreateForm(CreateView, ListView):
    '''
    Class that uses django CreateView to allow user to create a new student 
    and ListView to display students
    '''
    model = Student
    fields = ['firstname', 'lastname', 'idnumber', 'schoolyear', 'major', 'gpa']

class StudentEditForm(UpdateView):
    '''
    Class that uses django UpdateView to allow user to edit an existing student
    '''
    model = Student
    template_name = 'regserve/student_edit_form.html'
    fields = ['firstname', 'lastname', 'idnumber', 'schoolyear', 'major', 'gpa']

class StudentDeleteForm(DeleteView):
    '''
    Class that uses django DeleteView to allow user to delete an existing student
    '''
    model = Student
    template_name = 'regserve/student_delete_form.html'
    success_url="/regserve/students/"

class SelectStudentForm(forms.Form):
    '''
    Django form to allow user to enter an id for the student they wish to delete 
    '''
    student_id = forms.IntegerField()

class SelectStudentToDeleteForm(FormView, ListView):
    '''
    Class that uses django Formview to allow user to enter the id of student they wish to delete 
    and ListView to display students
    '''
    model = Student
    form_class = SelectStudentForm
    template_name = 'regserve/select_students_to_delete_form.html'
    student_id = 0

    def form_valid(self, form):
        '''
        get data from form to determine which student to delete

        Args: 
        form: the form that the user can enter the id into 
        '''
        #get the data from the form
        self.get_student_id(form.cleaned_data)
        #redirect to editing url
        self.get_success_url()

        return super(SelectStudentToDeleteForm, self).form_valid(form)

    def get_student_id(self, valid_data):
        '''
        gets the student id of the student the student being deleted from form input 
        
        Args: 
        valid_data: data from form 
        '''
        self.student_id = valid_data["student_id"]
    
    def get_success_url(self):
        '''
        Redirect user to edit student page once form has been submitted 
        '''
        return f'/regserve/{self.student_id}/deletestudent'

class SelectStudentToEditForm(FormView, ListView):
    '''
    Class that uses django Formview to allow user to enter the id of student they wish to edit
    and ListView to display students
    '''
    model = Student
    form_class = SelectStudentForm
    template_name = 'regserve/select_students_to_edit_form.html'
    student_id = 0

    def form_valid(self, form):
        '''
        get data from form to determine which student to edit 

        Args: 
        form: the form that the user can enter the id into 
        '''
        #get the data from the form
        self.get_student_id(form.cleaned_data)
        #redirect to editing url
        self.get_success_url()

        return super(SelectStudentToEditForm, self).form_valid(form)

    def get_student_id(self, valid_data):
        '''
        gets the student id of the student the student being editing from form input 
        
        Args: 
        valid_data: data from form 
        '''
        self.student_id = valid_data["student_id"]

    
    def get_success_url(self):
        '''
        Redirect user to edit student page once form has been submitted 
        '''
        return f'/regserve/{self.student_id}/editstudent'