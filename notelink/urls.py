from django.urls import path, include
from . import views

urlpatterns = [

    path('create/link/', views.create_link, name='create_link'),
    path('update/link/<int:id>', views.update_link, name='update_link'),
]