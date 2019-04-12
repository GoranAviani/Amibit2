from django.contrib import admin

# Register your models here.

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import create_link_form
from .models import link

class link_admin(UserAdmin):
    
    form = create_link_form
    model = link
  #  list_display = ['link_user','link_name','link_url']
  #  fieldsets = (
  #  (None, {'fields': ('link_user', 'link_name', 'link_url')}),
  # ('Link info', {'fields': ( 'link_name', 'link_url',)}),
  # )

#admin.site.register(link, link_admin)
admin.site.register(link)