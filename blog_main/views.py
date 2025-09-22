from django.shortcuts import render

from aboutusfeatures.models import About
from blogs.models import Blog, Category


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