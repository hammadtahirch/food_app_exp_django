from django.db import models
from django.utils import timezone
from accounts.models.user import User
from shops.models.shop import Shop
from django.utils.translation import gettext_lazy as _


class Cart(models.Model):
    class Meta:
        app_label = "orders"
        db_table = "carts"

    country = models.CharField(max_length=10, null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    type = models.CharField(max_length=10, null=True, blank=True)
    sub_total = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    delivery_fee = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True)
    shop = models.ForeignKey(Shop, verbose_name=_("shop_id"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("user_id"), on_delete=models.CASCADE)

    def __str__(self):
        return self.country
