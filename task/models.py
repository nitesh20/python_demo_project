from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task')
    assigned_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='task_assigned_by')
    created_at = models.DateTimeField(auto_now_add=True)

    
