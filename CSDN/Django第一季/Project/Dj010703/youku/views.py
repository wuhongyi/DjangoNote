from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'base.html')


def index(request):
    return render(request, 'index.html', context={'pageindex':'0'})

def tv(request):
    return render(request, 'tv.html', context={'pageindex':'1'})

def movie(request):
    return render(request, 'movie.html', context={'pageindex':'2'})

def zy(request):
    return render(request, 'zy.html', context={'pageindex':'3'})



