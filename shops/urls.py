from django.urls import path


urlpatterns = [
    path('shop_registration', RegistrationView.as_view(), name='registration'),
]
