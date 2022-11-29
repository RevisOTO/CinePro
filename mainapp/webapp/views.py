from django.shortcuts import render
from gestorapp.models import *

# Create your views here.
def inicioCine(request):
    return render(request,'inicio.html')