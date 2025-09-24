from unicodedata import category
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from blogs.models import Blog, Category
from .forms import CategotryForm

@login_required(login_url='login')
def dashboard(request):
  category_count = Category.objects.all().count()
  blogs_count = Blog.objects.all().count()
  context = {
    'category_count':category_count,
    'blogs_count':blogs_count,
  }
  return render(request, 'dashboard/dashboard.html', context)

def categories(request):
  
  return render(request, 'dashboard/categories.html')

def blogslist(request):
  blogs = Blog.objects.all()
  context = {
    'blogs': blogs,
  }
  return render(request, 'dashboard/blogslist.html', context)

def add_category(request):
  if request.method =='POST':
    form = CategotryForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('categories')
  else:
    form = CategotryForm()
  context = {
    'form':form,
  }
  return render(request,'dashboard/add_category.html', context)

def edit_category(request, pk):
  category = get_object_or_404(Category, pk=pk)
  if request.method == 'POST':
    form = CategotryForm(request.POST, instance=category)
    if form.is_valid():
      form.save()
      return redirect('categories')
  form = CategotryForm(instance=category)
  context = {
    'form':form,
    'category':category,
  }
  return render(request, 'dashboard/edit_category.html',context)

def delete_category(request, pk):
  cat =  Category.objects.get(pk=pk)
  get_object_or_404(Category, pk=pk).delete()
  messages.success(request, f'Category "{cat}" is deleted successfully!')
  return redirect('categories')