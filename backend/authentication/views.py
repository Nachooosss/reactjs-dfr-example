from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from rest_framework import generics, status, serializers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer, ListUserSerializer
from .models import CustomUser
from django.dispatch import receiver
from datetime import datetime


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            raise serializers.ValidationError(
                'Las credenciales no son válidas')


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)


class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch']

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user


class UsersView(viewsets.ModelViewSet):
    serializer_class = ListUserSerializer
    queryset = CustomUser.objects.all()
