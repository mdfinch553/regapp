from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    studentid = models.PositiveIntegerField(blank=True, validators={MinValueValidator(1)})
