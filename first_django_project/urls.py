from django.contrib import admin
from django.urls import path, include
from firstblog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('firstblog.urls')),
    path('cadmin/', include('cadmin.urls'))
]
