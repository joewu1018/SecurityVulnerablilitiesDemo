from django.contrib import admin
from .models import Grade, Board

class GradeAdmin(admin.ModelAdmin):
	list_display = ("id", "student", "semester", "subject", "grade")
	list_filter = ("semester", "subject")
	
class  BoardAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "content", "created_at")

admin.site.register(Grade, GradeAdmin)
admin.site.register(Board, BoardAdmin)
