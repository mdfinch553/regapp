from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.enums import Choices
from django.test.testcases import TestCase
from django.urls import reverse, reverse_lazy

class Person(models.Model):
    '''
    Abstract class that represents a person. Inherets from django.db models
    '''
    #attributes of a person
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    idnumber = models.PositiveBigIntegerField()
    email = models.EmailField(blank=True)
    datecreated = models.DateTimeField(blank=True, auto_now_add=True)
    datemodified = models.DateTimeField(blank=True, auto_now=True)

    @property
    def full_name(self):
        '''
        function that returns the first and last name of the person 
        '''
        return f'{self.firstname} {self.lastname}'
    
    class Meta:
        '''
        meta class allows us to define this class as an abstract class
        '''
        abstract = True
    
    def __str__(self):
        '''
        string information when class is printed
        '''
        return f'Name: {self.full_name}, Id Number {self.idnumber}, Email: {self.email}'

class Student(Person):
    '''
    class that represents a student, inherits from person abstract class
    '''

    #list defining possible years in school and their abbreviations
    YEAR_IN_SCHOOL = [
        ('FR', 'Freshman'), 
        ('SO', 'Sophomore'), 
        ('JR', 'Junior'), 
        ('SR', 'Senior'), 
        ('GR', 'Graduate')
    ]

    #list of possible majors and their abreviations 
    MAJORS = [
        ('CS', 'Computer Science'), 
        ('ENG', 'Engineering'), 
        ('SC', 'Science'), 
        ('BUS', 'Business'), 
        ('LAW', 'Law'), 
        ('NUR', 'Nursing'), 
        ('MAT', 'Math')
    ]

    #other attributes of students
    schoolyear = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL)
    major = models.CharField(max_length=3, choices=MAJORS) 
    gpa = models.FloatField(max_length=4, blank=True)

    def __str__(self):
        '''
        returns a descriptive string for a student object
        '''
        return f'StudentID: {self.id}: {super(Student, self).__str__()}, year in school: {self.schoolyear}, major: {self.major}'
    
    def get_absolute_url(self):
        '''
        function that returns that absolute url for the student model 
        '''
        return reverse_lazy('regserve:students')
