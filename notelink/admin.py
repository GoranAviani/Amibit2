from django.contrib import admin

# Register your models here.

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import create_link_form
from .models import link


class link_admin(admin.ModelAdmin):
    list_display = ("link_name" , "link_url" , "link_user")
    list_filter = ("link_name", "link_url" , "link_user")
    search_fields= ("link_name","link_url","link_user")


admin.site.register(link, link_admin)
#admin.site.register(link)