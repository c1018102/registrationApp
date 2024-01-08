from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .forms import AddModule
from .models import Module
from .forms import ModuleSelectionForm

def home(request):
    return render(request, 'moduleregistrationsystem/home.html', {'title': 'Welcome'})
def aboutus(request):
    return render(request, 'moduleregistrationsystem/aboutus.html', {'title': 'About'})
def contactus(request):
    return render(request, 'moduleregistrationsystem/contactus.html', {'title': 'Contact'})
def modules(request):
    modules = Module.objects.all()

    if request.method == 'POST':
        form = ModuleSelectionForm(request.POST)
        if form.is_valid():
            selected_modules = form.cleaned_data['users']
            # Associate selected modules with the logged-in user
            request.user.module_set.set(selected_modules)
    else:
        form = ModuleSelectionForm()

    user_modules = request.user.module_set.all()
    return render(request, 'moduleregistrationsystem/modules.html', {'title': 'Modules', 'modules': modules, 'form': form, 'user_modules': user_modules})

def add_module(request):
    if request.method == 'POST':
        form = AddModule(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Module Added!')
            return redirect('moduleregistrationsystem/add_module.html')
        else:
            messages.warning(request, 'Unable to add module!')
        return redirect('moduleregistrationsystem/add_module.html')
    else:
        form = AddModule()
        return render(request, 'moduleregistrationsystem/add_module.html', {'form': form , 'title': 'Add Module'})
