from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blogs.models import Blog, Category

class CategotryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = '__all__'
    
class BlogPostForm(forms.ModelForm):
  class Meta:
    model = Blog
    fields = ['title', 'category','featured_image','short_description','blog_body','status', 'is_featured']
    labels = {
      'title': 'Blog Title',
      'blog_body':'Description',
      'is_featured':'Is featured?'
    }
    
class AddUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']
    
  
class EditUserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']