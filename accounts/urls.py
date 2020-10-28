from django.urls import path

from .views.auth_token import AuthTokenView
from .views.user import LoginView
from rest_framework.authtoken import views


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),

    # path('api-token-auth/', views.obtain_auth_token),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]