from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from shops.models.shop import Shop


class ShopSetting(models.Model):
    class Meta:
        app_label = "shops"
        db_table = "shop_settings"

    charge_to_shop = models.IntegerField(null=True)  # we will store percent in column and charge to shop accordingly
    food_prep_time = models.IntegerField(null=True, blank=True)  # food preparation time.
    shop_rating = models.IntegerField(null=True,
                                      blank=True)  # this shop rating. basis of this we render shops and market .
    currency = models.IntegerField(null=True,
                                   blank=True)  # this shop rating. basis of this we render shops and market .
    time_zone = models.CharField(max_length=100, null=True,
                                 blank=True)  # this shop rating. basis of this we render shops and market .
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True)
    shop_id = models.OneToOneField(Shop, verbose_name=_("shop_id"), on_delete=models.CASCADE)
