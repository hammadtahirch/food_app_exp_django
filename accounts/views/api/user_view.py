from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_422_UNPROCESSABLE_ENTITY
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from accounts.serializer.user_create_serializer import UserCreateSerializer
from accounts.serializer.user_login_serializer import UserLoginSerializer
from accounts.services.user_service import UserService


class CustomerLoginView(APIView):
    """
    This view helps to validate customer credentials
    """

    def post(self, request):
        """
        This function only calls on post .
        """
        user_serializer = UserLoginSerializer(data=request.data)
        if not user_serializer.is_valid():
            return Response(user_serializer.errors, status=HTTP_404_NOT_FOUND)

        is_user = authenticate(
            email=request.data["email"],
            password=request.data["password"],

        )
        if not is_user:
            return Response({'Message': 'Oh Ho! Invalid Credentials or activate account'}, status=HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=is_user)
        user_hammad = UserLoginSerializer(is_user)
        return Response(
            {
                "user": user_hammad.data,
                "token": token.key,

            }, HTTP_200_OK)


class DriverLoginView(APIView):
    """
    This view helps to validate driver credentials
    """

    def post(self, request):
        """
        This function will call only on post
        """
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

            }, HTTP_200_OK)


class ShopKeeperLoginView(APIView):
    """
    This view helps to validate shop keeper credentials.
    """

    def post(self, request):
        user_serializer = UserLoginSerializer(data=request.data)
        if not user_serializer.is_valid():
            return Response(user_serializer.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)

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

            }, HTTP_200_OK)


class CustomerRegistrationView(APIView):
    """
    This view helps to create customer in db.
    """

    def __init__(self):
        """
        initializer of above call
        """
        self.__user_service = UserService()

    def post(self, request):
        """
        this function calls on post
        """
        request_data = request.data
        serializer = UserCreateSerializer(data=request_data, context={"method": request.method})
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)
        user_object = self.__user_service.create_customer(request_data)
        create_user_serializer = UserCreateSerializer(user_object)
        return Response(
            {
                "user": create_user_serializer.data
            }, HTTP_200_OK)
