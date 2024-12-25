# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('myservice')  # Redirect to your home page
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def welcome(request):
    return render(request, 'accounts/welcome.html')

from django.contrib.auth.views import LoginView

class login(LoginView):
    template_name = 'accounts/login.html'

def custom_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

