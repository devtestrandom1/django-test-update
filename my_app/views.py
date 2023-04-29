from django.shortcuts import render, redirect
from .models import Profile
from .forms import CustomUserChangeForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

def index(request):
  context = {
    'profiles' : Profile.objects.all()
  }
  return render(request, 'index.html', context)


def registerUser(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = UserCreationForm()
  return render(request, 'register.html', {'form': form})


def loginUser(request):
  return render(request, 'base/login_register.html')

@login_required(login_url = 'register')
def update_user(request):
  form = CustomUserChangeForm(instance=request.user)
  if request.method == 'POST':
    form = CustomUserChangeForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      messages.success(request, 'Profile updated successfully.')
      return redirect('index')
  return render(request, "update_user.html", {'form': form})