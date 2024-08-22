from django.contrib import admin

from .models import LogData


@admin.register(LogData)
class LogDataAdmin(admin.ModelAdmin):
    list_display = ['time', 'remote_ip', 'method', 'response_code']
    list_filter = ['method', 'response_code']
    search_fields = ['method', 'response_code']
