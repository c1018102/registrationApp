from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'moduleregistrationsystem/home.html')
def aboutus(request):
    return render(request, 'moduleregistrationsystem/aboutus.html')
def contactus(request):
    return render(request, 'moduleregistrationsystem/contactus.html')
def modules(request):
    return render(request, 'moduleregistrationsystem/modules.html')




# Create your views here.
