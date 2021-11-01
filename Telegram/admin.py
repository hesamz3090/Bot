from django.contrib import admin
from .models import *


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'date')
    search_fields = ('id', 'user_id', 'date')
