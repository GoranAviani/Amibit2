from django.shortcuts import render, redirect
from .forms import (
    create_link_form
)


# Create your views here.
def create_link(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            create_link_form_data = create_link_form(request.POST)
            if create_link_form_data.is_valid():
                form = create_link_form_data.save(commit=False)
                #form.link_name = create_link_form_data.linkName
                #form.link_url = create_link_form_data.linkUrl
                form.link_user = request.user
                #Check does the link have http or https in the beginning
                #form.link_url = add_HTTP_to_linkurl(form.link_url)
                form.save()
               # messages.success(request, 'Link saved!',extra_tags='create_link')
            return redirect('dashboard')
        else:
            create_link_form_data = create_link_form()
            return render(request, 'note_link/create_link.html', {'create_link_form_data': create_link_form_data})
    else:
        # if user is not authenticated inform him of that
        return render(request,'otherPages/not_authenticaded.html')
