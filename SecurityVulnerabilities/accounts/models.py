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