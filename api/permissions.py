from api.models import Roles
from rest_framework import permissions


class IsAdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_admin


class IsAdminOrReadOnlyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_admin

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_admin


class IsAuthorPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated
                and obj.author == request.user)


class IsModeratorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_moderator

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_moderator


class IsAuthorOrStuffOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return not request.user.is_anonymous()
        if request.method in ('PATCH', 'DELETE'):
            return (obj.author == request.user
                    or request.user.role == Roles.MODERATOR
                    or request.user.role == Roles.ADMIN)
        if request.method in permissions.SAFE_METHODS:
            return True
        return False
