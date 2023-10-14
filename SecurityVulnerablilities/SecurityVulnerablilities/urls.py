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
    path('xss/', accounts.xss_vulnerable, name='XSS'),
    path('grade_search/', accounts.grade_search, name='GradeSearch'),
    path('student_maintenance/', accounts.student_maintenance, name='StudentMaintenance'),
    path('download/', accounts.download_file, name='DownloadFile'),
]
