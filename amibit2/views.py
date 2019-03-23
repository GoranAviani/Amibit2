
#Location of non app single pages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

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
   HTTP_URL = "http://"
   HTTPS_URL = "https://"

   text = request.GET.get('search_bar')

   if text[0:2+1] == "go ":
      return redirect(HTTP_URL+text[3:])
   elif text[0:3+1] == "goo ":
      return redirect(HTTP_URL+"www.google.com/?#q="+(text[4:]))
   elif text[0:3+1] == "ddg ":
      return redirect(HTTP_URL+"www.duckduckgo.com/?q="+(text[4:]))
   else:
      return redirect(HTTP_URL+"www.duckduckgo.com/?q="+(text))

   return redirect('index')

