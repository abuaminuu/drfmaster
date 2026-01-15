from rest_framework import permissions

class IsOwnerOrReadonly(permissions.BasePermission):
    """
    Custom permission to allow only owner of object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS (safe requests verbs).
        if request.method in permissions.SAFE_METHODS:
            return True

        # otherwise, write permissions are only allowed to the owner of the object
        return obj.owner == request.user
