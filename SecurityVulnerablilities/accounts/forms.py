from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentsForm(forms.Form):
    name = forms.CharField(
        label='姓名', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    studentId = forms.CharField(
        label='學號', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    register_year = forms.IntegerField(
        label='入學年份', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    phone_number = forms.CharField(
        label='電話', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        label='信箱',
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    gender = forms.ChoiceField(
        label='性別',
        choices=[('', '請選擇性別'), ('M', '男性'), ('F', '女性')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    birth_date = forms.DateField(
        label='生日',
        widget=forms.DateInput(attrs={'class': 'form-control'})
    )

    subject = forms.ChoiceField(
        label='科目',
        choices=[('', '請選擇科目'), ('IC', '計算機概論'), ('CN', '計算機網路'), ('C', '微積分'), ('LN', '線性代數'), ('DM', '離散數學'), ('P', '程式設計'),],
        widget=forms.Select(attrs={'class': 'form-control'})
    )