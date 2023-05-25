from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework import viewsets
from users.models import RegisteredUsers
from users.serializers import RegisterSerializer, LoginSerializer


class RegisterViewSet(GenericViewSet):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request) :
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = RegisteredUsers.objects.create_user(**serializer.validated_data)
        user.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        return Response(status=status.HTTP_200_OK)


class LoginViewSet(GenericViewSet):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            access = AccessToken.for_user(user)
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "user": user.username,
                    "token": str(refresh),
                    "access_token": str(access)
                }
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        return Response(status=status.HTTP_200_OK)
