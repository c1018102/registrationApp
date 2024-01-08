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
def delete_module(request):
    return render(request, 'moduleregistrationsystem/delete_module.html', {'title': 'Delete Modules'})
def add_module(request):
    if request.method == 'POST':
        form = AddModule(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Module Added!')
            return redirect('login')
        else:
            messages.warning(request, 'Unable to add module!')
        return redirect('add_module.html')
    else:
        form = AddModule()
        return render(request, 'moduleregistrationsystem/add_module.html', {'form': form , 'title': 'Add Module'})

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .forms import AddModule
from .models import Module

def edit_module(request, module_id):
    module = get_object_or_404(Module, pk=module_id)

    if request.method == 'POST':
        form = EditModule(request.POST, instance=module)
        if form.is_valid():
            form.save()
            messages.success(request, 'Module updated successfully!')
            return redirect('moduleregistrationsystem:modules')  # Use the correct namespace
    else:
        form = EditModule(instance=module)

    return render(request, 'moduleregistrationsystem/edit_module.html', {'form': form, 'module': module})
