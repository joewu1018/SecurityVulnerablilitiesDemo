from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, unique=True)
    studentId = models.CharField(max_length=10, blank=True, unique=True)
    grade = models.FloatField(blank=True, null=True)
    register_year = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    GENDER_CHOICES = (
        ('M', '男性'),
        ('F', '女性'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    birth_date = models.DateField(blank=True,null=True)
    LECTURE_CHOICES = (
        ('CB', '計算機概論'),
        ('student', '計算機網路'),
        ('engineer', '微積分'),
        ('developer', '線性代數'),
        ('designer', '離散數學'),
        ('accountant', '程式設計'),
    )
    lecture = models.CharField(max_length=100, choices=LECTURE_CHOICES, blank=True, null=True)  # 職業欄位，最大長度為 100，選項限定在 OCCUPATION_CHOICES 中
    
    def __str__(self):
        return self.name
