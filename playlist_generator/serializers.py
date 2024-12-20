from rest_framework import serializers
from . import models

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Playlist
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = '__all__'

class PlaylistGenerationRequestSerializer(serializers.Serializer):
    mood = serializers.CharField(max_length=100)
    genre = serializers.CharField(max_length=100)
    activity = serializers.CharField(max_length=100)

class GeneratedSongSerializer(serializers.Serializer):
    title = serializers.CharField()
    artist = serializers.CharField()