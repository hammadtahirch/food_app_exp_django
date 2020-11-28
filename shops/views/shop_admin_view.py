from django.contrib import admin
from django import forms

from accounts.models.user import User
from food_delivery_app import settings
from shops.models import Shop
from shops.views.shop_setting_admin_view import ShopSettingAdminView
from shops.views.shop_timing_admin_view import ShopTimingAdminView


class ShopChangeFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(groups__name="shop_keeper")

    class Meta:
        model = Shop
        fields = (
            "name", "slug", "address", "city", "province", "country", "postal_code", "disclaimer", "is_active",
            "is_close"
        )


class ShopAdminView(admin.ModelAdmin):
    list_display = ("name", "address", "city", "province", "country", "is_active")
    list_filter = ("name", "address")
    search_fields = ("name__startswith", "address__startswith")
    prepopulated_fields = {"slug": ("name",)}
    form = ShopChangeFrom
    fieldsets = (
        (None,
         {"fields": (
             "name", "image_url", "slug", "address", "longitude", "latitude", "city", "province", "country",
             "postal_code",
             "disclaimer", "is_active", "is_close",
             "user")}
         ),
    )
    actions = ["duplicate_shop"]

    def add_view(self, request, extra_content=None):
        self.inlines = [ShopSettingAdminView]
        return super(ShopAdminView, self).add_view(request)

    def change_view(self, request, object_id, extra_content=None):
        self.inlines = [ShopTimingAdminView, ShopSettingAdminView]
        return super(ShopAdminView, self).change_view(request, object_id)

    # this class is used to add css and js fines in admin templates
    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/google_place_autocomplete.css',)
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?libraries=places&v=weekly&key={}'.format(
                    settings.GOOGLE_MAPS_API_KEY),
                'js/admin/google_place_autocomplete_admin.js',
            )

    # this action helps to create duplicate shops.
    def duplicate_shop(self, request, queryset):
        selected_int = queryset.values_list('id', flat=True)
        print(len(selected_int))

    duplicate_shop.short_description = "Duplicate Shop"
