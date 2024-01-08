from django.contrib import admin
from django.http import HttpResponse

def my_custom_view(request):
    return HttpResponse("To add a module - visit http://localhost:8000/add_module")

# Register your models here.
