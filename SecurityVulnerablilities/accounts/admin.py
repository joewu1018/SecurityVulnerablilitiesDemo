from django.contrib import admin
from .models import Student, Grade

class AccountAdmin(admin.ModelAdmin):
	list_display = ("username", "studentId", "email", "is_staff")
	list_filter = ("gender",)
	search_fields=('id',)

admin.site.register(Grade)
admin.site.register(Student, AccountAdmin)
