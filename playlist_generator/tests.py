from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Song
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class SongModelTest(TestCase):
    def setUp(self):
        self.song = Song.objects.create(
            title="Test Song",
            artist="Test Artist",
            album="test album",
            genre="Rock",
            release_date="2021-01-01"
        )
    def test_song_creation(self):
        self.assertEqual(self.song.title, "Test Song")
        self.assertEqual(self.song.artist, "Test Artist")
        self.assertEqual(self.song.album, "test album")
        self.assertEqual(self.song.genre, "Rock")
        self.assertEqual(self.song.release_date, "2021-01-01")

class SongAPIViewTest(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        # Create test song
        self.song = Song.objects.create(
            title="Test Song",
            artist="Test Artist",
            album="test album",
            genre="Rock",
            release_date="2021-01-01"
        )
        # Authenticate
        self.client.force_authenticate(user=self.user)

    def test_get_songs(self):
        response = self.client.get(reverse('song-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Song")