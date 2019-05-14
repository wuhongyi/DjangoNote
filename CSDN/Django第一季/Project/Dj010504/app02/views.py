from django.shortcuts import render,reverse,redirect

# Create your views here.

def index(request):
    username = request.GET.get('username')
    if username:
        return render(request, 'app02\index.html')
    else:
        return redirect(reverse('app02:login'))
        # 跳转到命名空间为app02下的login

def login(request):
    return render(request, 'app02\login.html')