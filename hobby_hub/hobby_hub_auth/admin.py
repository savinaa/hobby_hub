from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from hobby_hub.hobby_hub_auth.models import HobbyHubUser


@admin.register(HobbyHubUser)
class HobbyHubAdmin(UserAdmin):
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('email',)
    ordering = ('email',)