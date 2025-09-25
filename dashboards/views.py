from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
# from django.template.defaultfilters import slugify


from blogs.models import Blog, Category
from .forms import BlogPostForm, CategotryForm

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

def posts(request):
  blogs = Blog.objects.all().order_by('-created_at')
  context = {
    'blogs': blogs,
  }
  return render(request, 'dashboard/posts.html', context)

def add_post(request):
  if request.method == 'POST':
    form = BlogPostForm(request.POST, request.FILES)
    if form.is_valid():
      blog = form.save(commit=False)
      blog.author = request.user
      form.save()
      title = form.cleaned_data['title']
      blog.slug = slugify(title) +'-'+str(blog.id)
      blog.save()
      return redirect('posts')
  else:
    form = BlogPostForm()
  context ={
    'form' : form,
  }
  return render(request, 'dashboard/add_post.html', context)

def delete_post(request, pk):
  get_object_or_404(Blog, pk=pk).delete()
  messages.success(request, 'blog deleted successfully!')
  return redirect('posts')

def edit_post(request, pk):
  post = get_object_or_404(Blog, pk=pk)
  if request.method == 'POST':
    form = BlogPostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      post = form.save()
      #title = post.title
      title = form.cleaned_data['title']
      post.slug = slugify(title)+'-'+str(post.id)
      post.save()
      return redirect('posts')
  form = BlogPostForm(instance=post)
  context = {
    'form':form,
    'post':post,
  }
  return render(request, 'dashboard/edit_post.html', context)