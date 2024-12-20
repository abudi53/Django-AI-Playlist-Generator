from django.contrib import admin
from django.urls import path, include
from playlist_generator.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('playlist_generator.urls')),
    path('api/auth/', include('user.urls')),
]