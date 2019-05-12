from django.shortcuts import render

# Create your views here

data = {
    'index': {'pageindex':'0', 'img':'img/index.png', 'content':"===首页的具体内容==="},
    'tv': {'pageindex': '1', 'img': 'img/tv.png', 'content': "===电视剧的具体内容==="},
    'movie': {'pageindex': '2', 'img': 'img/movie.png', 'content': "===电影的具体内容==="},
    'zy': {'pageindex': '3', 'img': 'img/zy.png', 'content': "===综艺的具体内容==="},
}

def index(request):
    return render(request, 'index.html',context={'data': data["index"]})

def tv(request):
    return render(request, 'index.html',context={'data': data["tv"]})

def movie(request):
    return render(request, 'index.html',context={'data': data["movie"]})

def zy(request):
    return render(request, 'index.html',context={'data': data["zy"]})