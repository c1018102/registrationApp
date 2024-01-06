from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'moduleregistrationsystem/home.html', {'title': 'Welcome'})
def aboutus(request):
    return render(request, 'moduleregistrationsystem/aboutus.html', {'title': 'About'})
def contactus(request):
    return render(request, 'moduleregistrationsystem/contactus.html', {'title': 'Contact'})
def modules(request):
    return render(request, 'moduleregistrationsystem/modules.html', {'title': 'Modules'})


# Create your views here.
