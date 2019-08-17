from django.shortcuts import render

# Create your views here.
from .forms import (
    user_mobile_phone_form
)


def edit_user_phone(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_profile_form_data = user_profile_form(request.POST, instance = request.user)
            if user_profile_form_data.is_valid():
                user_profile_form_data.save()
                return redirect('user_profile')
        else:
            user_phone_form_data = user_mobile_phone_form(instance=request.user)
            return render (request, 'mobile_phone/edit_user_phone.html', {'user_phone_form_data' : user_phone_form_data})
    else:
        return render(request,'index.html')