from ..models.user import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class userService:
    def loginUser(loginCredentials):
        user1 = authenticate(
            email=loginCredentials["email"],
            password=loginCredentials["password"]
        )
        if user1 is not None:
            token = Token.objects.get_or_create(user=user1)
            print(token.key)
        else:
            print("user not fine")

