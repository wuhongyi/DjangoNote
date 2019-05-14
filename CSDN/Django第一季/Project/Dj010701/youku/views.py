from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def tv(request):
    return render(request, 'tv.html')

def movie(request):
    return render(request, 'movie.html')

def zy(request):
    return render(request, 'zy.html')