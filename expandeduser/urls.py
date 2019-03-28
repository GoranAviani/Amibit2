from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.sign_up.as_view(), name='signup'),
    path('', include('social_django.urls', namespace='social')),

    path('setttings/', views.user_settings_menu, name='user_settings_menu'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit-info/', views.edit_user_profile, name='edit_user_profile'),
    path('profile/edit-password/', views.edit_user_password, name='edit_user_password'),

]