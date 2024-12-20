from rest_framework import serializers
from . import models


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = '__all__'

class PlaylistDetailSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)
    
    class Meta:
        model = models.Playlist
        fields = ['id', 'name', 'description', 'songs', 'mood', 'genre', 'activity', 'created_at']
        read_only_fields = ['user']

class PlaylistGenerationRequestSerializer(serializers.Serializer):
    mood = serializers.CharField(max_length=100)
    genre = serializers.CharField(max_length=100)
    activity = serializers.CharField(max_length=100)

class GeneratedSongSerializer(serializers.Serializer):
    title = serializers.CharField()
    artist = serializers.CharField()