"""amibit2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('expandeduser.urls')),
    path('nl/', include('notelink.urls')),
    path('search/', views.search_bar, name='search_bar'), #search/ is used in base.html
    path('user_phone/', include('mobile_phone.urls')),
    path('weather_app/', include('weather.urls')),

    #path('about/', views.about, name='about'), 
    #path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'), 
    path('sms_panel/', views.sms_panel, name='sms_panel'),
]
