from django.views.generic import ListView, DetailView
from .models import Author, Tag, Category, Post

class ListPost(ListView):
  template_name = 'firstblog/post_list.html'
  model = Post

class DetailPost(DetailView):
  model = Post


class PostByCategory(ListView):
  model=Post
  template_name = 'firstblog/post_by_category.html'

  def get_queryset(self, **kwars):
    category_slug = self.kwargs['category_slug']
    return super().get_queryset().filter(category__slug=category_slug)
    """ queryset = Post.objects.filter(category__slug=category_slug)
    return queryset """

  def get_context_data(self, **kwargs):
    context = super(PostByCategory,self).get_context_data(**kwargs)
    category_slug = self.kwargs['category_slug']
    category = Category.objects.get(slug=category_slug)
    context['category'] = category
    return context

class PostByTag(ListView):
  model=Post
  template_name = 'firstblog/post_by_tag.html'

  def get_queryset(self, **kwars):
    tag_slug = self.kwargs['tag_slug']
    return super().get_queryset().filter(tags__slug=tag_slug)
    """ queryset = Post.objects.filter(tag__slug=tag_slug)
    return queryset """

  def get_context_data(self, **kwargs):
    context = super(PostByTag,self).get_context_data(**kwargs)
    tag_slug = self.kwargs['tag_slug']
    tag = Tag.objects.get(slug=tag_slug)
    context['tag'] = tag
    return context
