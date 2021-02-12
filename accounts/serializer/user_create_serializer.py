from rest_framework import serializers

from accounts.models import User
from accounts.serializer.group_serializer import GroupSerializer


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True, error_messages={
        "blank": "Oh Ho! email is required."
    })
    password = serializers.CharField(required=True, error_messages={
        "blank": "Oh Ho! password is required."
    })
    first_name = serializers.CharField(required=True, error_messages={
        "blank": "Oh Ho! first name is required."
    })
    last_name = serializers.CharField(required=True, error_messages={
        "blank": "Oh Ho! last name is required."
    })

    groups = GroupSerializer(read_only=True, many=True)

    def validate_email(self, email):
        if self.context.get("method") == 'POST':
            is_user_exist = User.objects.filter(email=email).exists()
            if is_user_exist:
                raise serializers.ValidationError("Oh Ho! this email already in use.")

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
            'groups',
        )
