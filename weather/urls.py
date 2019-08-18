from django.urls import path
from . import views

urlpatterns = [
    path('send_daily_forecast/', views.send_daily_forecast_to_all, name='send_daily_forecast'),
    
]