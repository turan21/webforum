from rest_framework.permissions import BasePermission, SAFE_METHODS


class ForumPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or
                    (request.user and request.user.is_authenticated and request.user.author))

    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS or
                    (request.user and request.user.is_authenticated and
                     obj.author == request.user.author))


class CommentPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or
                    (request.user and request.user.is_authenticated and request.user.author) or
                    request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS or
                    (request.user and request.user.is_authenticated and
                     obj.author == request.user.author) or
                    request.user.is_staff)
