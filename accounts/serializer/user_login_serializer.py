from rest_framework import serializers

from .group_serializer import GroupSerializer
from ..models.user import User


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    groups = GroupSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
            'is_staff',
            'is_active',
            'groups',
        )
