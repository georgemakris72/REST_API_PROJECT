from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self,request,view,obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True #safe methods are get, if they want to change or delete this will not be true so on to next step

        return obj.id==request.user.id #Will return true if it is in fact current users id,so checking if object user is trying to change is same id as user. if not permission will be denied.
