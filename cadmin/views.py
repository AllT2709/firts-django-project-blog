from django.urls.base import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import get_list_or_404, redirect
from django.urls import reverse_lazy

from firstblog.forms import PostForm
from firstblog.views import Post


class PostAdd(CreateView):
  template_name='cadmin/post_add.html'
  form_class = PostForm
  success_url = reverse_lazy('post_add')

class PostUpdate(UpdateView):
  template_name = 'cadmin/post_update.html'
  form_class = PostForm
  model=Post

  def get_success_url(self):
    pk = self.kwargs['pk']
    return reverse('post_detail', kwargs={'pk': pk})

class PostDelete(DeleteView):
  model=Post
  template_name='cadmin/post_confirm_delete.html'
  success_url =reverse_lazy('post_list')