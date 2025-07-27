from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'role')

    def __str__(self):
        return f"{self.user.username} - {self.role.name}"

class ManageUser(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_user')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_manager')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('manager', 'user')
    
    def __str__(self):
        return f"{self.user.username} -> {self.manager.username}"
    
