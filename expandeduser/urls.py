from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.sign_up.as_view(), name='signup'),
    path('', include('social_django.urls', namespace='social')),

]