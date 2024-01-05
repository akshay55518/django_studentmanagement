from django.db import models

# Create your models here.

class Student(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    class1=models.CharField(max_length=10)
    email=models.EmailField()
    regno=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=100)
    Value=models.IntegerField()
    user_type=models.CharField(max_length=10)
    
class Teacher(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    email=models.EmailField()
    unid=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=100)
    Value=models.IntegerField()
    user_type=models.CharField(max_length=10)
    
    
    