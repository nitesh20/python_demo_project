from django.contrib import admin
from .models import Role, UserRole, ManageUser

# Register your models here.

class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    # list_select_related = ('user', 'role')

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')

class ManageUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'manager')

admin.site.register(Role, RoleAdmin)
admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(ManageUser, ManageUserAdmin)
