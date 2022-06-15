from django.contrib import admin

from .models import Teams, Student, Teacher


@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    """кафедра"""
    search_fields = ('name',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """Преподаватель"""
    list_filter = ('teams_teacher',)
    search_fields = ('first_name', 'middle_nam', 'last_name', 'teams_teacher')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Студент"""

    list_filter = ('teams_student',)
    search_fields = ('first_name', 'middle_name', 'last_name', 'teams_student')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
