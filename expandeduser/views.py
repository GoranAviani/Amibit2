from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from .forms import custom_user_creation_form

class sign_up(generic.CreateView):
    form_class = custom_user_creation_form
    success_url = reverse_lazy('dashboard') #TODO 
    template_name = 'signup.html'

def user_settings_menu(request):
     return render(
         request,
        'expanded_user/user_settings_menu.html',
)

'''
def user_info_edit_profile(request):
    if request.method == 'POST':
        user_info_form = UserInfo(request.POST, instance = request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return redirect('user_info')
        else:
            user_info_form = UserInfo(instance=request.user)
            return render (request, 'user/user_info_edit_profile.html', {'user_info_form' : user_info_form})

    else:
        user_info_form = UserInfo(instance=request.user)
    return render (request, 'user/user_info_edit_profile.html', {'user_info_form' : user_info_form})

'''