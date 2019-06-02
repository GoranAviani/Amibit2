from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from .forms import (
    user_signup_form,
    user_profile_form
)
from django.contrib.auth import (
    update_session_auth_hash,
)
from django.contrib.auth.forms import PasswordChangeForm



#class sign_up(generic.CreateView):
#    form_class = custom_user_creation_form
#    success_url = reverse_lazy('dashboard') #TODO 
#    template_name = 'signup.html'

def sign_up_user(request):
    if request.method == 'POST':
        signup_form = user_signup_form(request.POST)
        if signup_form.is_valid():
            form = signup_form.save()
            form.refresh_from_db()
            form.save()
            raw_password = signup_form.cleaned_data.get('password1')
            #form1 = authenticate(username=form.username, password=raw_password)
            #login(request, form1)
            return redirect('dashboard')
    else:
        signup_form = user_signup_form()
        return render(request, 'signup.html', {'signup_form': signup_form})



def user_settings_menu(request):
    if request.user.is_authenticated:
        return render(
            request,
            'expanded_user/user_settings_menu.html',
            )
    else:
       return render(request,'index.html')

def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'expanded_user/user_profile.html')
    else:
        return render(request,'index.html')
    
def edit_user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_profile_form_data = user_profile_form(request.POST, instance = request.user)
            if user_profile_form_data.is_valid():
                user_profile_form_data.save()
                return redirect('user_profile')
        else:
            user_profile_form_data = user_profile_form(instance=request.user)
            return render (request, 'expanded_user/edit_user_profile.html', {'user_profile_form_data' : user_profile_form_data})
    else:
        return render(request,'index.html')

def edit_user_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            change_password_form = PasswordChangeForm(data = request.POST, user = request.user) #PasswordChangeForm is inbuilt in Django
            currentUser = request.user
            if change_password_form.is_valid():
                change_password_form.save()
                update_session_auth_hash(request, change_password_form.user) 
                return render(request,'expanded_user/change_user_password_done.html')
            else:
                change_password_form=PasswordChangeForm(user = request.user)
                return render (request, 'expanded_user/change_user_password.html', {'change_password_form' : change_password_form})
        else:
            change_password_form=PasswordChangeForm(user = request.user)
            return render (request, 'expanded_user/change_user_password.html', {'change_password_form' : change_password_form})
    else:
        return render(request,'index.html') 