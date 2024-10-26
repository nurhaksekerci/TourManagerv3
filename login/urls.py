from django.urls import path
from .views import user_login, request_password_reset, reset_password

from .views import *
urlpatterns = [
    path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),
    path('request-password-reset/', request_password_reset, name='request_password_reset'),
    path('reset-password/<uuid:token>/', reset_password, name='reset_password'),
    path('base/', base, name='base'),
    path('auth-creative/', auth_creative, name='auth_creative'),
    path('auth-login/', auth_login, name='auth_login'),
    path('auth-maintenance/', auth_maintenance, name='auth_maintenance'),
    path('auth-register/<int:id>/', auth_register, name='auth_register'),
    path('auth-company/', auth_company, name='auth_company'),
    path('auth-reset/', auth_reset, name='auth_reset'),
    path('auth-resetting/', auth_resetting, name='auth_resetting'),
    path('auth-verify/', auth_verify, name='auth_verify'),
]
