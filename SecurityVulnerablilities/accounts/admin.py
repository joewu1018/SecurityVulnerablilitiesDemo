from django.contrib import admin
from .models import Student

class AccountAdmin(admin.ModelAdmin):
	list_display = ("id", "user", "name", "studentId", "email")
	list_filter = ("gender",)
	search_fields=('id',)
admin.site.register(Student, AccountAdmin)
