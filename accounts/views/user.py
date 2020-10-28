from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)
from ..services.user_service import userService
from ..models.user import User
from ..serializer.user_serializer import (
    UserSerializer,
    UserSignInSerializer
    )

class LoginView(APIView):

    def post(self, request, *args, **kwargs):

        signin_serializer = UserSignInSerializer(data=request.data)
        if not signin_serializer.is_valid():
            return Response(signin_serializer.errors, status=HTTP_400_BAD_REQUEST)

        user = authenticate(
            email=request.data["email"],
            password=request.data["password"]
        )
        if not user:
           return Response({'detail': 'Invalid Credentials or activate account'}, status=HTTP_404_NOT_FOUND)
        
        token, _ = Token.objects.get_or_create(user=user)
        # The implementation will be described further
        user_serialized = UserSerializer(user)
        
        return Response({
            'user': user_serialized.data,
            'expires_in': '',
            'token': token.key
        }, status=HTTP_200_OK)
