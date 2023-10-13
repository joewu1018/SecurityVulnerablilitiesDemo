from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Student(AbstractUser):
    studentId = models.CharField(max_length=10, blank=True, unique=True)
    register_year = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True, unique=True)
    GENDER_CHOICES = (
        ('M', '男性'),
        ('F', '女性'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    birth_date = models.DateField(blank=True,null=True)
    
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.IntegerField()
    SUBJECT_CHOICES = (
        ('IC', '計算機概論'),
        ('CN', '計算機網路'),
        ('C', '微積分'),
        ('LN', '線性代數'),
        ('DM', '離散數學'),
        ('P', '程式設計'),
    )
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    grade = models.FloatField()
    
    def __str__(self):
        return self.student.username + ' ' + self.subject + ' ' + str(self.grade)