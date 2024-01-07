from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout
from django.http import HttpResponseNotAllowed, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile


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

login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # Profile doesn't exist, create it
        Profile.objects.create(user=request.user)
        profile = request.user.profile

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been successfully updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {'u_form': u_form, 'p_form': p_form, 'title': 'Profile'}
    return render(request, 'users/profile.html', context)
