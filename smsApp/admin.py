from django.contrib import admin
from .models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone', 'date_added')

admin.site.register(Student, StudentAdmin)