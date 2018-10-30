from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50, null=False)
    price = models.FloatField(null=True)
    pages = models.IntegerField(null=False)

class Author(models.Model):
    name = models.CharField(max_length=20, null=False)
    gender = models.CharField(max_length=1, null=False)
    ratings = models.IntegerField(null=True)

class Student(models.Model):
    name = models.CharField(max_length=30, null=False)
    gender = models.CharField(max_length=1, null=False)
    roll = models.IntegerField(null=False)
    marks = models.FloatField(null=True)

    def get_grade(self):
        marks = self.marks
        if marks > 100 or marks < 0:
            return 'I'
        elif marks >= 70:
            return 'A'
        elif marks >= 60:
            return 'B'
        elif marks >= 40:
            return 'C'
        else:
            return 'F'

    def get_males():
        return Student.objects.filter(gender='m')
