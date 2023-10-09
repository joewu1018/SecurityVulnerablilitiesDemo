from django.shortcuts import render
from accounts.forms import StudentsForm
# Create your views here.

def index(request):
    return render(request, "accounts/index.html")

def xss_vulnerable(request):
    if request.method == 'POST':
        message = request.POST.get('message')
    return render(request, 'accounts/xss.html', locals())

def search(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
    else:
        form = StudentsForm()        
    return render(request, "accounts/search.html", locals())

def update(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
    else:
        form = StudentsForm()
    return render(request, "accounts/update.html", locals())