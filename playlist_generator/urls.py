from django.urls import path
from .views import SongListView, PlaylistGeneratorView

urlpatterns = [
    path('songs/', SongListView.as_view(), name='song-list'),
    path('generate-playlist/', PlaylistGeneratorView.as_view(), name='generate-playlist'),
]