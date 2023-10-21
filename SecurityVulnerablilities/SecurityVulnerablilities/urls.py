"""SecurityVulnerablilities URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import accounts.views as accounts
import students.views as students

urlpatterns = [
    path('admin/', admin.site.urls),
    # 首頁
    path('', accounts.index, name='Index'),
    # 登入
    path('login/', accounts.sign_in, name='Login'),
    # 登出
    path('logout/',accounts.log_out, name='Logout'),
    # 註冊
    path('register/', accounts.register, name='Register'),
    # 下載檔案
    path('download/', accounts.download_file, name='DownloadFile'),
    # 學生成績查詢
    path('grade_search/', students.grade_search, name='GradeSearch'),
    # 學生資料維護
    path('student_maintenance/', students.student_maintenance, name='StudentMaintenance'),
    # XSS
    path('xss/', students.xss_vulnerable, name='XSS'),
    # SQL Injection
    path('sql_injection/', students.sql_injection_vulnerable, name='SqlInjection'),
    # Quiz
    path('quiz/', students.quiz,name='Quiz')
]
