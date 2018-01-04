from rest_framework import permissions


class OnlyUserNotAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        print("kwon")
        if not request.user.is_superuser:
            return True


    def has_object_permission(self, request, view, obj):
        print("kwon1")
        if request.user.is_superuser:
            return True
        elif view.action == 'retrieve':
            return obj == request.user or request.user.is_staff