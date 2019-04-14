from django.contrib import admin

# Register your models here.

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import create_link_form
from .models import link, note


class link_admin(admin.ModelAdmin):
    list_display = ("linkName" , "linkUrl" , "linkUser")
    list_filter = ("linkName", "linkUrl" , "linkUser")
    search_fields= ("linkName","linkUrl","linkUser")



class note_admin(admin.ModelAdmin):
    list_display = ("noteTitle" , "noteTimestamp" , "noteUser")
    list_filter = ("noteTitle", "noteTimestamp" , "noteUser")
    search_fields= ("noteTitle","noteTimestamp","noteUser")

admin.site.register(link, link_admin)
admin.site.register(note, note_admin)