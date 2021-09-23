from django.forms import ModelForm, widgets
from django import forms
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError

from .models import Author,Post,Category,Tag

class PostForm(ModelForm):
  class Meta:
    model=Post
    fields=('title','content','author','category','tags')
    
    widgets = {
      'title': forms.TextInput(attrs={"class":"form-control"}),
      'content': forms.Textarea(attrs={"class":"form-control"}),
      'author': forms.Select(attrs={"class":"form-control"}),
      'category': forms.Select(attrs={"class":"form-control"}),
      'tags': forms.SelectMultiple(attrs={"class":"form-control"}),
    }

  def clean(self):
    cleaned_data = super(PostForm,self).clean()
    title = cleaned_data.get('title')
    if title:
      cleaned_data['slug'] = slugify(title)
    return cleaned_data

""" class CategoryForm(ModelForm):
  class Meta:
    model=Category
    fields= '__all__'

  def clean_name(self):
    n = self.cleaned_data['name']
    if n.lower() == 'tag' or n.lower() == 'add' or n.lower() == 'update':
      raise ValidationError(f"Category name can't be {n}")
    return n
  
  def clean_slug(self):
    return self.cleaned_data['slug'].lower()

class TagForm(ModelForm):
  class Meta:
    model = Tag
    fields = '__all__'
  
  def clean_name(self):
    n = self.cleaned_data['name']
    if n.lower() == 'tag' or n.lower() == 'add' or n.lower() == 'update':
      raise ValidationError(f"Tag name can't be {n}")
    return n

  def clean_slug(self):
    return self.cleaned_data['slug'].lower()


class AuthorForm(ModelForm):
  class Meta:
    model =Author
    fields = '__all__'

  def clean_name(self):
    name = self.cleaned_data['name']
    name_l = name.lower()
    if name_l == 'admin' or name_l == 'author':
      raise ValidationError("Author name can't be 'admin/author'")
    return name_l

  def clean_email(self):
    return self.cleaned_data['email'].lower() """