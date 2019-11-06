from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk','name','age','email')

admin.site.register(Student, StudentAdmin)