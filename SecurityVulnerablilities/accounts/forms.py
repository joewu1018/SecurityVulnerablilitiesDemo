from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Student

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Student
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):

    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    remember_me = forms.BooleanField(
        label="記住我",
        required=False, 
        widget=forms.CheckboxInput()
    )
    
class StudentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'studentId', 'register_year', 'phone_number', 'email', 'gender', 'birth_date']
        labels = {
            'username': '姓名',
            'studentId': '學號',
            'register_year': '入學年份',
            'phone_number': '電話',
            'email': '信箱',
            'gender': '性別',
            'birth_date': '生日',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'studentId': forms.TextInput(attrs={'class': 'form-control'}),
            'register_year': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class SearchForm(forms.Form):
    name = forms.CharField(
        label='姓名', 
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    studentId = forms.CharField(
        label='學號', 
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    semester = forms.IntegerField(
        label='學期', 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    subject = forms.ChoiceField(
        label='科目',
        required=False,
        choices=[('', '請選擇科目'), ('IC', '計算機概論'), ('CN', '計算機網路'), ('C', '微積分'), ('LN', '線性代數'), ('DM', '離散數學'), ('P', '程式設計'),],
        widget=forms.Select(attrs={'class': 'form-control'})
    )