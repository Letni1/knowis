from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = "Owners only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.create_user == request.user


class IsUserOrReadOnly(BasePermission):
    message = "Owners only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


class IsUser(BasePermission):
    message = "Owners only"

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
