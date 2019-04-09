
#Location of non app single pages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from amibit2.custom_modules.search_bar import *


def index(request):
#   return render(request,'index.html')

   if request.user.is_authenticated:
      return redirect('dashboard')
   else:
      return render(request,'index.html')

def dashboard(request):
   #return redirect('dashboard')
   return render(request,'dashboard.html')
  

#this is called from base.html
def search_bar(request):
   text = request.GET.get('search_bar')  
   return redirect(get_web_url(text))

   #return redirect('index')

def about(request):
    return render(
    request,
    'otherPages/about.html'
)
