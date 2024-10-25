from django.urls import path
from .views import user_login, user_logout, request_password_reset, reset_password

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('request-password-reset/', request_password_reset, name='request_password_reset'),
    path('reset-password/<uuid:token>/', reset_password, name='reset_password'),
]
