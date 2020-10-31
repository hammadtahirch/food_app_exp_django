from django.apps import AppConfig


class ShopsConfig(AppConfig):
    name = 'shops'
    label = 'shops'

    def ready(self):
        import shops.services.shop_signals  # noqa
