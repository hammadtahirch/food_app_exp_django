from django.contrib import admin
from django import forms

from accounts.models.user import User
from shops.models import Shop
from shops.views.shop_setting_admin_view import ShopSettingAdminView
from shops.views.shop_timing_admin_view import ShopTimingAdminView


class ShopChangeFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_id'].queryset = User.objects.filter(groups__name="shop_keeper")

    class Meta:
        model = Shop
        fields = (
            "name", "slug", "address", "city", "province", "country", "is_active", "is_close", "user_id"
        )


class ShopAdminView(admin.ModelAdmin):
    list_display = ("name", "address", "city", "province", "country", "is_active")
    list_filter = ("name", "address")
    search_fields = ("name__startswith", "address__startswith")
    prepopulated_fields = {"slug": ("name",)}
    form = ShopChangeFrom
    fieldsets = (
        (None,
         {"fields": ("name", "slug", "address", "city", "province", "country", "is_active", "is_close", "user_id")}
         ),
    )

    def add_view(self, request, extra_content=None):
        self.inlines = [ShopSettingAdminView]
        return super(ShopAdminView, self).add_view(request)

    def change_view(self, request, object_id, extra_content=None):
        self.inlines = [ShopTimingAdminView, ShopSettingAdminView]
        return super(ShopAdminView, self).change_view(request, object_id)
