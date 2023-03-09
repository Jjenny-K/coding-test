from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """ 인증받은 사용자 본인의 정보가 아닐경우 권한 제한 """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # GET, HEAD, OPTIONS 요청의 경우 허용
            return True

        if request.user.is_authenticated:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # GET, HEAD, OPTIONS 요청의 경우 허용
            return True

        if request.user.is_authenticated and request.COOKIES.get('refresh_token'):
            if hasattr(obj, 'email'):
                return obj.email == request.user.email
            else:
                return False

        return False
