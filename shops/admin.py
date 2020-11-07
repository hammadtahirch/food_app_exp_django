from django.contrib import admin

# Register your models here.
from shops.models import Shop
from shops.views.shop_admin_view import ShopAdminView

admin.site.register(Shop, ShopAdminView)
