from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from .models import PasswordResetRequest, LoginLog
from django.core.mail import send_mail
from django.conf import settings
import uuid
from datetime import timedelta

def request_password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            token = uuid.uuid4()  # Yeni token oluştur
            expired_at = timezone.now() + timedelta(hours=1)  # 1 saat geçerli

            # Token'i veritabanına kaydet
            PasswordResetRequest.objects.create(user=user, token=token, expired_at=expired_at)

            # Şifre sıfırlama e-postası gönder
            reset_link = f"{request.build_absolute_uri('/reset-password/')}{token}/"
            send_mail(
                'Password Reset Request',
                f'You requested a password reset. Click the link to reset your password: {reset_link}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Password reset email has been sent.')
        except User.DoesNotExist:
            messages.error(request, 'User with this email does not exist.')

    return render(request, 'request_password_reset.html')


def reset_password(request, token):
    password_reset_request = get_object_or_404(PasswordResetRequest, token=token)

    if password_reset_request.is_expired():
        messages.error(request, 'This password reset link has expired.')
        return redirect('request_password_reset')

    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        user = password_reset_request.user
        user.set_password(new_password)
        user.save()
        
        # Token'i kullanıldıktan sonra sil
        password_reset_request.delete()
        
        messages.success(request, 'Your password has been reset successfully.')
        return redirect('login')

    return render(request, 'reset_password.html', {'token': token})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        ip_address = request.META.get('REMOTE_ADDR')

        if user is not None:
            login(request, user)
            LoginLog.objects.create(user=user, success=True, ip_address=ip_address)
            return redirect('home')
        else:
            LoginLog.objects.create(user=None, success=False, ip_address=ip_address)
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def login_logs(request):
    logs = LoginLog.objects.all().order_by('-timestamp')
    return render(request, 'login_logs.html', {'logs': logs})


def base(request):
    return render(request, 'login/base.html')

def auth_creative(request):
    return render(request, 'login/auth-404-creative.html')

def auth_login(request):
    return render(request, "login/auth-login-creative.html")

def auth_maintenance(request):
    return render(request, "login/auth-maintenance-creative.html")

def auth_register(request):
    return render(request, "login/auth-register-creative.html")

def auth_reset(request):
    return render(request, "login/auth-reset-creative.html")

def auth_resetting(request):
    return render(request, "login/auth-resetting-creative.html")

def auth_verify(request):
    return render(request, "login/auth-verify-creative.html")