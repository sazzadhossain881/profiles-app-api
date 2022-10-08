from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """allow user to edit their own profile"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

class UpdateOwnFeed(permissions.BasePermission):
    """allow user to update their own status"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
