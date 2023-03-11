from rest_framework import permissions


class QuestionIsOwnerOrReadOnly(permissions.BasePermission):
    """ 인증받은 사용자 본인이 작성한 문제 정보가 아닐경우 권한 제한 """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # GET, HEAD, OPTIONS 요청의 경우 허용
            return True

        if request.user.is_authenticated and request.COOKIES.get('refresh_token'):
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # GET, HEAD, OPTIONS 요청의 경우 허용
            return True

        if request.user.is_authenticated and request.COOKIES.get('refresh_token'):
            if hasattr(obj.user, 'email'):
                return obj.user.email == request.user.email
            else:
                return False

        return False


class AnswerIsOwner(permissions.BasePermission):
    """ 인증받은 사용자 본인이 작성한 답안 및 해설 정보가 아닐경우 권한 제한 """
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.COOKIES.get('refresh_token'):
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.COOKIES.get('refresh_token'):
            if hasattr(obj.user, 'email'):
                return obj.user.email == request.user.email
            else:
                return False

        return False
