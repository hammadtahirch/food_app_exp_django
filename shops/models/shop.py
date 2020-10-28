from django.db import models
from django.utils import timezone
from accounts.models.user import User
from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    class Meta:
        app_label = 'shops'
        db_table = 'shops'

    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    province = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, null=True, blank=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, null=True, blank=True)
    slug = models.CharField(max_length=255, null=True, unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True)
    user_id = models.ForeignKey(User, verbose_name=_("user_id"), on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['name', 'address', 'user']

    def __str__(self):
        return self.name
