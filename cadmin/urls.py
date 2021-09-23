from django.urls import path
from .views import PostAdd,PostUpdate,PostDelete

urlpatterns = [
  path('post/add/', PostAdd.as_view(), name='post_add'),
  path('post/update/<int:pk>', PostUpdate.as_view(), name='post_update'),
  path('post/delete/<int:pk>', PostDelete.as_view(), name='post_delete'),
]