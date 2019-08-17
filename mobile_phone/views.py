from django.shortcuts import render, redirect

# Create your views here.
from .forms import (
    user_mobile_phone_form
)
from .models import (
    user_phone
)

def edit_user_phone(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_phone_form_data = user_mobile_phone_form(request.POST, )
            if user_phone_form_data.is_valid():
                form = user_phone_form_data.save(commit=False)
                form.userMobilePhone = request.user
                form.save()
               # messages.success(request, 'Note saved!',extra_tags='create_note')
            return redirect('edit_mobile_phone')
        else:
            try:
                found_u_p_data = user_phone.objects.get(userMobilePhone=request.user.pk)
                data = {'phoneCountryCode': found_u_p_data.phoneCountryCode, "phoneNumber" : found_u_p_data.phoneNumber}
                user_phone_form_data = user_mobile_phone_form(initial=data)
            except:
                user_phone_form_data = user_mobile_phone_form()
            
            return render (request, 'mobile_phone/edit_user_phone.html', {'user_phone_form_data' : user_phone_form_data})
    else:
        return render(request,'index.html')