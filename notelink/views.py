from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    create_link_form,
    create_note_form
)
from .myModules.link_calculations import check_url_link
from .models import link


# Create your views here.
def create_link(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            create_link_form_data = create_link_form(request.POST)
            if create_link_form_data.is_valid():
                form = create_link_form_data.save(commit=False)
                form.linkUser = request.user
                #Check does the link have http or https in the beginning
                form.linkUrl = check_url_link(form.linkUrl) #TODO
                form.save()
               # messages.success(request, 'Link saved!',extra_tags='create_link')
            return redirect('dashboard')
        else:
            create_link_form_data = create_link_form()
            return render(request, 'note_link/create_link.html', {'create_link_form_data': create_link_form_data})
    else:
        return render(request,'otherPages/not_authenticaded.html')


def update_link(request, id):
    updatedLink = get_object_or_404(link, id=id)
    if request.user.is_authenticated:
        if updatedLink.linkUser == request.user:
            if request.method == 'POST':
                update_link_form_data = create_link_form(request.POST)
                if update_link_form_data.is_valid():
                    form = update_link_form_data.save(commit=False)
                    form.id = id
                    form.linkUser = request.user
                    # Check does the link have http or https in the beginning
                    form.linkUrl = check_url_link(form.linkUrl)
                    form.save()
                    return redirect('dashboard')
            else:
                update_link_form_data = create_link_form(instance = updatedLink)
                return render(request, 'note_link/update_link.html', {'update_link_form_data': update_link_form_data})
        else:
            return render(request, 'perasis/not_owner.html') #TODO
    else:
        return render(request,'otherPages/not_authenticaded.html')



def delete_link(request, id):
    deletedLink = get_object_or_404(link, id=id)
    if request.user.is_authenticated:
        if deletedLink.linkUser == request.user:
            deletedLink.delete()
            return redirect('dashboard')
        else:
            return render(request,'perasis/not_owner.html') #TODO
    else:
        # if user is not authenticated inform him of that
        return render(request, 'otherPages/not_authenticaded.html')


def create_note(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            create_note_form_data = create_note_form(request.POST)
            if create_note_form_data.is_valid():
                form = create_note_form_data.save(commit=False)
                form.noteUser = request.user
                #Check does the link have http or https in the beginning
                form.save()
               # messages.success(request, 'Note saved!',extra_tags='create_note')
            return redirect('dashboard')
        else:
            create_note_form_data = create_note_form()
            return render(request, 'note_link/create_note.html', {'create_note_form_data': create_note_form_data})
    else:
        return render(request,'otherPages/not_authenticaded.html')
