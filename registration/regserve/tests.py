from django.http import response
from django.test import TestCase, Client
from .models import *
import io
from rest_framework.parsers import JSONParser
from .serializers import *

class DataTest(TestCase):
    def setUp(self):
        Student.objects.create(
            firstname = "First",
            lastname = "Student",
            idnumber = 100, 
            email = 'first@student.edu',
            schoolyear = 'SR', 
            major = 'CS',  
            gpa = '4.0'
        )
        Student.objects.create(
            firstname = "Second",
            lastname = "Student",
            idnumber = 100, 
            email = 'second@student.edu',
            schoolyear = 'SR', 
            major = 'ENG', 
            gpa = '2.0'
        )
        self.test_client = Client()
    def test_student_api(self):
        students_response = self.test_client.get('/regserve/data/students/')
        print(f'STUDENT API TEST: insde test, response is {students_response}\n')
        self.assertEqual(students_response.status_code, 200)
        print(f'STUDENT API TEST: insde test, response content is {students_response.content}\n')
        student_stream = io.BytesIO(students_response.content)
        print(f'STUDENT API TEST: insde test, student stream is {student_stream}\n')
        student_api_data = JSONParser().parse(stream=student_stream)
        print(f'STUDENT API TEST: insde test, student api data is {student_api_data}\n')
        first_student_data = student_api_data[0]
        print(f'STUDENT API TEST: insde test, first student data is {first_student_data} id is {first_student_data["id"]}\n')
        first_student_db = Student.objects.get(id=first_student_data['id'])
        print(f'STUDENT API TEST: insde test, first student db is {first_student_db}\n')
        first_student_serializer = StudentSerializer(first_student_db, data=first_student_data)
        print(f'STUDENT API TEST: insde test, first student serializer is {first_student_serializer}\n')
        print(f'STUDENT API TEST: insde test, first student serializer is valid? {first_student_serializer.is_valid()}\n')
        first_student_api = first_student_serializer.save()
        print(f'STUDENT API TEST: insde test, first student api is {first_student_api}\n')
        self.assertEqual(first_student_api, first_student_db)

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