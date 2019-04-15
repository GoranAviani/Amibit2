from django.urls import path, include
from . import views

urlpatterns = [

    path('create/link/', views.create_link, name='create_link'),
    path('update/link/<int:id>', views.update_link, name='update_link'),
    path('delete/link/<int:id>', views.delete_link, name='delete_link'),

    path('create/note/', views.create_note, name='create_note'),
    path('update/note/<int:id>', views.update_note, name='update_note'),
    
]