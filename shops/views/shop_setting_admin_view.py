from django.contrib import admin

from shops.models import ShopSetting


class ShopSettingAdminView(admin.TabularInline):
    model = ShopSetting
    exclude = ["created_at", "updated_at", "deleted_at"]
    search_fields = ["zone"]
