from django.db import models

# Create your models here.
class Employee(models.Model):
    name =models.CharField(max_length=20)
    salary =models.CharField(max_length=20)
    date =models.DateField()

class Student(models.Model):
    name =models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    mark =models.CharField(max_length=3)