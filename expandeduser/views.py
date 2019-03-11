from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from .forms import custom_user_creation_form

class sign_up(generic.CreateView):
    form_class = custom_user_creation_form
    success_url = reverse_lazy('login') #TODO 
    template_name = 'signup.html'