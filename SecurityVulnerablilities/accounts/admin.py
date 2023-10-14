from django.contrib import admin
from .models import Student, Grade

class StudentAdmin(admin.ModelAdmin):
	list_display = ("username", "studentId", "email", "is_staff")
	list_filter = ("gender",)
	search_fields=('id',)

class GradeAdmin(admin.ModelAdmin):
	list_display = ("student", "semester", "subject", "grade")
	list_filter = ("semester", "subject")

admin.site.register(Grade, GradeAdmin)
admin.site.register(Student, StudentAdmin)
