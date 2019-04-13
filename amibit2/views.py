
#Location of non app single pages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .myModules.search_bar import *
from notelink.models import link


def index(request):
#   return render(request,'index.html')

   if request.user.is_authenticated:
      return redirect('dashboard')
   else:
      return render(request,'index.html')

def dashboard(request):
   if request.user.is_authenticated:
         queryUserLink = link.objects.filter(linkUser=request.user).order_by('-id')
       #  queryNote = Note.objects.filter(note_user=request.user).order_by('-note_timestamp')
         return render(request, 'dashboard.html', {
         'queryUserLink': queryUserLink,
        # 'queryNote': queryNote,
         })
   else:
        #if user is not authenticated inform him of that
        return render(request, 'otherPages/not_authenticaded.html')





  

#this is a search that is called from base.html
def search_bar(request):
   text = request.GET.get('search_bar')  
   return redirect(get_web_url(text))

   #return redirect('index')

def about(request):
    return render(
    request,
    'otherPages/about.html'
)
def contact(request):
    return render(
    request,
    'otherPages/contact.html'
)