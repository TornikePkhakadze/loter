from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    grade = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)


class Teacher(models.Model):

    firstname = models.CharField(max_length=50)  
    lasname = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    years_of_experience = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

class Class(models.Model):
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
