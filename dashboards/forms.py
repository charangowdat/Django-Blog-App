from django import forms

from blogs.models import Category

class CategotryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = '__all__'
  