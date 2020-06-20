from django.contrib import admin

from accounts.models.models import User
from accounts.services.admin_user import UserAdmin

admin.site.register(User, UserAdmin)
