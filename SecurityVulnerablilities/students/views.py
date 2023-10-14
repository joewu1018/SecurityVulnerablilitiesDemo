from django.shortcuts import render
from .forms import SearchForm, StudentsForm
from accounts.models import Student
from .models import Grade
from django.db.models import Case, When, Value, CharField

def grade_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data['studentId']
            results = Grade.objects.raw(
                """
                SELECT s.id, g.semester, g.subject, g.grade, s.studentId, s.username
                FROM students_grade AS g
                INNER JOIN accounts_student AS s
                ON g.student_id = s.id 
                WHERE s.studentId = %s OR s.studentId = '*'
                """, 
                [student]
            )
    else:
        form = SearchForm()
    return render(request, "accounts/grade_search.html", locals())

def student_maintenance(request):
    student = Student.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
    else:
        form = StudentsForm(instance=student)
    return render(request, "accounts/student_maintenance.html", locals())

def xss_vulnerable(request):
    if request.method == 'POST':
        message = request.POST.get('message')
    return render(request, 'accounts/xss.html', locals())
