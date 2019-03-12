
#Location of non app single pages
from django.shortcuts import render, redirect


def index(request):
   # if request.user.is_authenticated:
   #     return redirect('dashboard')
   # else:

    return render(request,'index.html')