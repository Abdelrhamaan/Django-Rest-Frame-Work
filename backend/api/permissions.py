from rest_framework import permissions



class IsEditorStaffPermission(permissions.DjangoModelPermissions):
    # new way 
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'], # override get permission to prevent user from retrive data
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    #  you don't need this part id you add IsAdminUser
    #  permission_classes = [permissions.IsAdminUser, IsEditorStaffPermission] # ---> make custom permissions

    def has_permission(self, request, view): 
        print(request.user.get_all_permissions())

        if not request.user.is_staff:
            return False
        
        return super().has_permission(request, view)


    # old way 
    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm('products.add_products'): # (app_name).(action)_(model_name)
    #             return True
    #         if user.has_perm('products.delete_products'):
    #             return True
    #         if user.has_perm('products.change_products'):
    #             return True
    #         if user.has_perm('products.view_products'):
    #             return True
    #         return False
    #     return False