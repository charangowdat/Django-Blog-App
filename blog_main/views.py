from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

from aboutusfeatures.models import About
from blogs.models import Blog, Category
from .forms import RegistrationForm


def home(request):
  featured_post = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
  posts = Blog.objects.filter(is_featured=False, status = 'Published')
  try:
    about = About.objects.get()
  except:
    about=None
  context = {
    
    'featured_post':featured_post,
    'posts':posts,
    'about':about,
  }
  return render(request, 'home.html', context)

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'You account has been registered successfully!')
      return redirect('login')
  else:
    form = RegistrationForm()
  context = {
    'form': form,
    }
  return render(request, 'register.html', context)

def login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = auth.authenticate(username=username,password=password)
      if user is not None:
        auth.login(request, user)
        messages.success(request, "You have successfully loged in!")
        return redirect('dashboard')
      messages.warning(request, "Wrong credentials!")
      return redirect('login')
  else:
    form = AuthenticationForm()
  context={
    'form':form,
  }
  return render(request, 'login.html', context)

def logout(request):
  auth.logout(request)
  messages.success(request,'You have Logged out!')
  return redirect('home')