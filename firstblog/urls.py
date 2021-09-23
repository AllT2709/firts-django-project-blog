from django.urls import path
from .views import ListPost, DetailPost, PostByCategory, PostByTag

urlpatterns = [
  path('',ListPost.as_view(), name='post_list'),
  path('<int:pk>/',DetailPost.as_view(), name='post_detail'),
  path('category/<category_slug>/',PostByCategory.as_view(), name='post_by_category'),
  path('tag/<tag_slug>/',PostByTag.as_view(), name='post_by_tag')
]