from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import *

def index(request):
    return HttpResponse("Hello from django backend")

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer