from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.http import HttpResponseNotAllowed, HttpResponse
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Now you can login!')
            return redirect('login')
        else:
            messages.warning(request, 'Unable to create account!')
        return redirect('moduleregistrationsystem:home')
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form , 'title': 'Student Registration'})
    
from django.contrib.auth import logout
from django.http import HttpResponseNotAllowed

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    else:
        return HttpResponseNotAllowed(['POST'])
def handle_logout(request):
    return HttpResponse("Method Not Allowed", status=405)

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'title': 'Profile'})

