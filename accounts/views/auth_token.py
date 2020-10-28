from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from accounts.models.user import User


class AuthTokenView(APIView):

    # this function helps to generate auth token
    def post(self, request):
        user_object = User.objects.get(email=request.data.get("email"))
        token = Token.object.get_or_create(user=user_object)
        content = {'message': token.key}
        return Response(content)
