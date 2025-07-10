from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_rutina/', include('app_rutina.urls')),
    path('', include('app_rutina.urls')), 
]