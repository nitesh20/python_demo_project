from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'assigned_to', 'assigned_by']

admin.site.register(Task, TaskAdmin)