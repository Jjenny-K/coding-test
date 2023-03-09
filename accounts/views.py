from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from accounts.models import User
from accounts.serializers import UserSignupSerializer, \
                              UserLoginSerializer, \
                              UserLogoutSerializer, \
                              UserSerializer
from accounts.permissions import IsOwnerOrReadOnly


class UserViewset(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):

    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'signup':
            return UserSignupSerializer
        elif self.action == 'login':
            return UserLoginSerializer
        elif self.action == 'logout':
            return UserLogoutSerializer
        else:
            return UserSerializer

    def get_permissions(self):
        if self.action in ('signup', 'login'):
            permission_class = (AllowAny,)
        else:
            permission_class = (IsOwnerOrReadOnly,)

        return [permission() for permission in permission_class]

    @action(methods=['post'], detail=False)
    def signup(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response({'message': f'{serializer.data["username"]}님 가입을 환영합니다.'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            # 로그인 시 refresh_token 쿠키 저장
            response = Response(status=status.HTTP_200_OK)
            data = {'user': serializer.validated_data['user'].email,
                    'access_token': serializer.validated_data['access']}

            response.data = data
            response.set_cookie(key='refresh_token', value=serializer.validated_data['refresh'], httponly=True)

            return response

    @action(methods=['post'], detail=False)
    def logout(self, request):
        # 쿠키에서 refresh_token을 제거하여 로그아웃
        response = Response({'message': 'Logout success'}, status=status.HTTP_202_ACCEPTED)

        response.delete_cookie('refresh_token')

        return response
