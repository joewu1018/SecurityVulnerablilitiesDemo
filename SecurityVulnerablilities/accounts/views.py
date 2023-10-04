from django.shortcuts import render

# Create your views here.

def index(requests):
    return render(requests, "accounts/index.html")

def xss_vulnerable(request):
    if request.method == 'POST':
        message = request.POST.get('message')
    return render(request, 'accounts/xss.html', locals())