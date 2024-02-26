from rest_framework import permissions
from .permissions import IsEditorStaffPermission

class StaffEditorMixinPermissions():
    permission_classes = [permissions.IsAdminUser, IsEditorStaffPermission]



class UserQuerySetMixin():
    user_field = 'user'
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup = {}
        lookup[self.user_field] = user
        # print("lookup", lookup)  
        qs = super().get_queryset(*args, **kwargs)
        if user.is_staff: # if admin make him see every thing 
            return qs
        return qs.filter(**lookup) # self.user = self.request.user