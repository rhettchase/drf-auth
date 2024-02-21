from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # safe for reading
        if request.method in permissions.SAFE_METHODS:
            return True

        # if we're allowing the owner to be null in Model
        # then this will check for that case and allow access
        if obj.owner is None:
            return True

        # can only make changes to stuff if you are the owner
        return obj.owner == request.user