from django.contrib.auth.admin import UserAdmin

from accounts.forms.admin_user import UserCreationFrom, UserChangeFrom


class UserAdmin(UserAdmin):
    add_form = UserCreationFrom
    form = UserChangeFrom
    list_display = ('first_name', 'last_name', 'email', 'is_staff', 'is_active',)
    list_filter = ('first_name', 'last_name', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'created_at',
                'updated_at')}
         ),
    )
    search_fields = ('first_name', 'last_name', 'email',)
    ordering = ('id',)
