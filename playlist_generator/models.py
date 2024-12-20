from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255, blank=True)
    genre = models.CharField(max_length=255, blank=True)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    songs = models.ManyToManyField(Song)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Fields for playlist generation parameters
    mood = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']