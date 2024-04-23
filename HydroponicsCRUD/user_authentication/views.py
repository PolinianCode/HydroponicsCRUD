from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegister(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        re_password = request.data.get('re_password')
        email = request.data.get('email')

        if password != re_password:
            return Response({'message': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        if username and password and email:
            user = User.objects.create_user(username, email, password)
            user.save()

            refresh = RefreshToken.for_user(user)

            return Response({'message': 'User created', 'refreshToken': str(refresh), 'accessToken': str(refresh.access_token)}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    def get(self, request):
        logout(request)
        return Response({'message': 'User logged out'}, status=status.HTTP_200_OK)


class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({'message': 'User logged in', 'refreshToken': str(refresh), 'accessToken': str(refresh.access_token)}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid data'}, status=status.HTTP_401_UNAUTHORIZED)
