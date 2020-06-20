from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models.models import User


class UserCreationFrom(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')


class UserChangeFrom(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
