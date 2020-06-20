from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from accounts.views.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        app_label = "accounts"

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100, default=None)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email
