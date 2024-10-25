from django.urls import path
from .views import create_monthly_shift_schedule

urlpatterns = [
    path('create-shift-schedule/', create_monthly_shift_schedule, name='create_shift_schedule'),
]
