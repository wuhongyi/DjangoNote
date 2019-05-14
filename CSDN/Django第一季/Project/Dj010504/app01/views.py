from django.shortcuts import render,reverse,redirect

# Create your views here.

def index(request):
    username = request.GET.get('username')
    if username:
        return render(request, 'app01\index.html')
    else:
        return redirect(reverse('app01:login'))

def login(request):
    return render(request, 'app01\login.html')