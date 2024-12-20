from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PlaylistGeneratorView, PlaylistViewSet, HomeView

router = DefaultRouter()
router.register(r'playlists', PlaylistViewSet, basename='playlist')

urlpatterns = [
    path('generate-playlist/', PlaylistGeneratorView.as_view(), name='generate-playlist'),
    path('', include(router.urls)),
]