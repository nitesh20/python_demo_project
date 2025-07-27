from rest_framework.permissions import BasePermission

class HasRole(BasePermission):
  def has_permission(self, request, view):
    required_roles = getattr(view, 'required_role', None)

    print(f"[Permission Check] Required Roles from view: {required_roles}")

    if required_roles:
      user_roles = request.user.user_roles.values_list('role__name', flat=True)
      print(f"User: {request.user.username}")
      print("User Roles:", list(request.user.user_roles.values_list('role__name', flat=True)))
      print("Required Roles:", required_roles)
      return any(role in user_roles for role in required_roles)
    return False