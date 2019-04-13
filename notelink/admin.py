from django.contrib import admin

# Register your models here.

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import create_link_form
from .models import link


class link_admin(admin.ModelAdmin):
    list_display = ("linkName" , "linkUrl" , "linkUser")
    list_filter = ("linkName", "linkUrl" , "linkUser")
    search_fields= ("linkName","linkUrl","linkUser")


admin.site.register(link, link_admin)
#admin.site.register(link)