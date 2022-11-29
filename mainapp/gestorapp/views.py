from django.shortcuts import render,get_object_or_404,redirect
from gestorapp.forms import *
from gestorapp.models import *

# Create your views here.

def nuevoUser(request):
    if request.method == "POST":
        formaUser = UserForm(request.POST)
        if formaUser.is_valid():
            formaUser.save()
            return redirect('index')
    else:
        formaUser = UserForm()
        return render(request,'login.html',{'formaUser':formaUser})