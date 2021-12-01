from django.http import response
from django.test import TestCase, Client
from .models import *

class DataTest(TestCase):
    def setUp(self):
        Student.objects.create(
            firstname = "First",
            lastname = "Student",
            idnumber = 100, 
            email = 'first@student.edu',
            schoolyear = 'SR', 
            major = 'CS', 
            gpa = '4.0', 
        )
        Student.objects.create(
            firstname = "Second",
            lastname = "Student",
            idnumber = 100, 
            email = 'second@student.edu',
            schoolyear = 'SR', 
            major = 'ENG', 
            gpa = '2.0', 
        )
    def test_student(self):
        student_list = Student.objects.all()
        for student in student_list: 
            print(f'Inside test student current student is {student}')
        student = student_list[0]
        self.assertEqual(student.id, 1)
        self.assertEqual(student.full_name, 'First Student')
        self.assertEqual(student.idnumber, 100)
        self.assertEqual(student.major, 'CS')
        self.assertEqual(student.gpa, 4.0)

class SimpleTest(TestCase):
    def setUp(self):
        self.test_client = Client()
    def test_response(self):
        response = self.test_client.get('/regserve')
        print(f'Inside HW test, response is {response}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Hello from django backend")