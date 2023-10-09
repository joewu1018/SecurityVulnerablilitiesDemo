from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "accounts/index.html")

def xss_vulnerable(request):
    if request.method == 'POST':
        message = request.POST.get('message')
    return render(request, 'accounts/xss.html', locals())

def search(request):
    return render(request, "accounts/search.html")

def update(request):
    return render(request, "accounts/update.html")