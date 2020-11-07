from django.utils import timezone

from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models.user import User


class DriverAvailability(models.Model):
    class Meta:
        app_label = "accounts"
        app_label = "accounts"

    day_name = models.CharField(max_length=10)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True)

    user_id = models.ForeignKey(User, verbose_name=_("user_id"), on_delete=models.CASCADE)
