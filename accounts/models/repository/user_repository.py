from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group

from accounts.models import User


class UserRepository:
    """
    This class helps to maintain all user database activity.
    """

    def create_user(self, request):
        """
        this function helps to create user in db
        Return user object
        """
        request.update(password=make_password(request["password"]))
        created_user = User.objects.create(**request)
        return created_user

    def assign_user_group(self, group_name, user_instance):
        """
        This function helps to assign user group to related user
        Return nothing
        """
        group = Group.objects.get(name=group_name)
        user_instance.groups.add(group)
