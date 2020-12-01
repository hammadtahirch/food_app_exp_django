from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from accounts.serializer.user_login_serializer import UserLoginSerializer


# this view helps to authenticate user on basis of email and password
class LoginView(APIView):
    def post(self, request, format=None):
        user_serializer = UserLoginSerializer(data=request.data)
        if not user_serializer.is_valid():
            return Response(user_serializer.errors, status=HTTP_404_NOT_FOUND)

        is_user = authenticate(
            email=request.data["email"],
            password=request.data["password"],

        )
        if not is_user:
            return Response({'Message': 'Invalid Credentials or activate account'}, status=HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=is_user)
        user_hammad = UserLoginSerializer(is_user)
        return Response(
            {
                "user": user_hammad.data,
                "token": token.key,

            })


class RegistrationView(APIView):
    def post(self, request, format=None):
        pass
