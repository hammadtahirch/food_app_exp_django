from django.contrib import admin

from shops.models.shop_timing import ShopTiming


class ShopTimingAdmin(admin.TabularInline):
    model = ShopTiming
    extra = 1
    list_display = ("day",
                    "delivery_start_time",
                    "delivery_end_time",
                    "pick_up_start_time",
                    "pick_up_end_time",
                    "shop_id"
                    )
    fieldsets = (
        (None,
         {'fields':
             (
                 "day",
                 "delivery_start_time",
                 "delivery_end_time",
                 "pick_up_start_time",
                 "pick_up_end_time"
             )}),
    )
