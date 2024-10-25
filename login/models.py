from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class PasswordResetRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='password_reset_requests')
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Şifre sıfırlama token'i
    created_at = models.DateTimeField(auto_now_add=True)  # Oluşturulma tarihi
    expired_at = models.DateTimeField()  # Token'in geçerlilik süresi

    def is_expired(self):
        """Token'in süresi dolmuş mu kontrolü."""
        return timezone.now() > self.expired_at

    def __str__(self):
        return f"Password Reset Request for {self.user.username} - {self.token}"


class LoginLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_logs')
    timestamp = models.DateTimeField(auto_now_add=True)  # Giriş zamanı
    ip_address = models.GenericIPAddressField(null=True, blank=True)  # IP adresi
    success = models.BooleanField(default=False)  # Giriş başarılı mı?

    def __str__(self):
        return f"{self.user.username} - {self.timestamp} - {'Success' if self.success else 'Failed'}"
