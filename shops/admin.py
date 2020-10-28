from django.contrib import admin

# Register your models here.
from shops.models import Shop
from shops.views.shop_admin import ShopAdmin

admin.site.register(Shop, ShopAdmin)
