from django.shortcuts import render
from datetime import datetime
# Create your views here.

def index(request):
    return render(request,'index.html', context={'num':0})


def tv(request):
    return render(request, 'index.html', context={'num':1})


