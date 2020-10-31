from django.db.models.signals import post_save
from django.dispatch import receiver
from shops.models.shop import Shop
from shops.models.shop_timing import ShopTiming


@receiver(post_save, sender=Shop)
def create_user_profile(sender, instance, created, **kwargs):
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if created:
        for day_name in week_days:
            shop_timing = ShopTiming()
            shop_timing.day = day_name
            shop_timing.delivery_start_time = '9:00:00'
            shop_timing.delivery_end_time = '20:00:00'
            shop_timing.pick_up_start_time = '9:00:00'
            shop_timing.pick_up_end_time = '20:00:00'
            shop_timing.shop_id = instance
            shop_timing.save()
