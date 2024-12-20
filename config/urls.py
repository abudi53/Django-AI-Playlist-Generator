from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('playlist_generator.urls')),
    path('api/auth/', include('user.urls')),
]