from django.contrib.auth.admin import UserAdmin


class UserAdminView(UserAdmin):
    list_display = ('first_name', 'last_name', 'get_groups', 'email', 'is_staff', 'is_active',)
    list_filter = ('groups__name', 'is_staff', 'is_active',)
    search_fields = ('first_name', 'last_name', 'email',)
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

    ordering = ('-id',)

    def get_groups(self, obj):
        groups = []
        for group in obj.groups.all():
            groups.append(group.name)
        return ' '.join(groups)

    get_groups.short_description = 'Groups'
