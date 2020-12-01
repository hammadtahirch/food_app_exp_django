from django.urls import path
from .views.api.user_view import LoginView


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),

    # path('api-token-auth/', views.obtain_auth_token),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]