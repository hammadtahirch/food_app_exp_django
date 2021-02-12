from django.urls import path
from .views.api.user_view import CustomerLoginView, DriverLoginView, ShopKeeperLoginView, \
    CustomerRegistrationView

urlpatterns = [
    path('customer_login', CustomerLoginView.as_view(), name='customer_login'),
    path('driver_login', DriverLoginView.as_view(), name='driver_login'),
    path('shop_keeper_login', ShopKeeperLoginView.as_view(), name='shop_keeper_login'),


    path('customer_registration', CustomerRegistrationView.as_view(), name='registration')
]
