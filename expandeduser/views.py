from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect

from .forms import (
    custom_user_creation_form,
    user_profile_form
)

from django.contrib.auth.forms import PasswordChangeForm



class sign_up(generic.CreateView):
    form_class = custom_user_creation_form
    success_url = reverse_lazy('dashboard') #TODO 
    template_name = 'signup.html'

def user_settings_menu(request):
     return render(
         request,
        'expanded_user/user_settings_menu.html',
)

def user_profile(request):
    return render(request,'expanded_user/user_profile.html')

def edit_user_profile(request):
    if request.method == 'POST':
        user_profile_form_data = user_profile_form(request.POST, instance = request.user)
        if user_profile_form_data.is_valid():
            user_profile_form_data.save()
            return redirect('user_profile')
    else:
        user_profile_form_data = user_profile_form(instance=request.user)
        return render (request, 'expanded_user/edit_user_profile.html', {'user_profile_form_data' : user_profile_form_data})


def edit_user_password(request):
    if request.method == 'POST':
        change_password_form_data = PasswordChangeForm(data = request.POST, user = request.user) #PasswordChangeForm inbuilt in django

        if change_password_form_data.is_valid():
            change_password_form_data.save()
            change_password_form_data(request, change_password_form_data.user)
            return redirect('user_profile')
        else:
            change_password_form_data=PasswordChangeForm(user = request.user)
            return render (request, 'expanded_user/change_user_password.html', {'change_password_form_data' : change_password_form_data})
    else:
        change_password_form_data=PasswordChangeForm(user = request.user)
    return render (request, 'expanded_user/change_user_password.html', {'change_password_form_data' : change_password_form_data})