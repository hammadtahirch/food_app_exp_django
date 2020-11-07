from django.contrib import admin

from accounts.models.user import User
from accounts.views.user_admin_view import UserAdminView

admin.site.register(User, UserAdminView)
