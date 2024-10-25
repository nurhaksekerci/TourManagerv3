from django.contrib import admin
from .models import PasswordResetRequest, LoginLog

@admin.register(PasswordResetRequest)
class PasswordResetRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'created_at', 'expired_at', 'is_expired')

@admin.register(LoginLog)
class LoginLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'ip_address', 'success')
