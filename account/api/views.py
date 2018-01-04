from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser
)

from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView
    )

from account.serializers import (
    UserCreateSerializer, 
    UserLoginSerializer, 
    UserUpdateSerializer, 
    UserListSerializer, 
    UserDetailSerializer) 

from django.contrib.auth import get_user_model
from .permissions import OnlyUserNotAdmin

User = get_user_model()

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserDetailAPIView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserDeleteAPIView(DestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class OnlyAdminUserListAPIView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class OnlyAdminUserUpdateAPIView(UpdateAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)