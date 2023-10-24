from django.contrib import admin
from .models import Grade, Board, MissionCategory, Mission, MissionRecord

class GradeAdmin(admin.ModelAdmin):
	list_display = ("id", "student", "semester", "subject", "grade")
	list_filter = ("semester", "subject")
	
class  BoardAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "content", "created_at")

class MissionCategoryAdmin(admin.ModelAdmin):
	list_display = ("id", "title")

class MissionAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "category")

class MissionRecordAdmin(admin.ModelAdmin):
	list_display = ("id", "student", "mission", "is_completed", "attempts", "created_at")

admin.site.register(Grade, GradeAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(MissionCategory, MissionCategoryAdmin)
admin.site.register(Mission, MissionAdmin)
admin.site.register(MissionRecord, MissionRecordAdmin)
