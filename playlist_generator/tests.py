from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Song, Playlist
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from unittest.mock import patch


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

# class MockGeminiService:
#     def generate_playlist(self, mood: str, genre: str, activity: str) -> list:
#         return [
#             {"title": "Test Song 1", "artist": "Test Artist 1"},
#             {"title": "Test Song 2", "artist": "Test Artist 2"},
#         ]
class PlaylistGeneratorTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
        self.url = reverse('generate-playlist')
        # self.patcher = patch('playlist_generator.views.GeminiService', return_value=MockGeminiService())
        # self.patcher.start()

    # def tearDown(self):
    #     self.patcher.stop()

    # @patch('playlist_generator.views.GeminiService')
    # def test_generate_playlist(self, mock_service):
    def test_generate_playlist(self):
        # mock_service.return_value = MockGeminiService()
        data = {
            'mood': 'happy',
            'genre': 'pop',
            'activity': 'workout'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.data, list))
        self.assertTrue(len(response.data) > 0)
        self.assertIn('title', response.data[0])
        self.assertIn('artist', response.data[0])

    def test_invalid_request(self):
        data = {'mood': 'happy'}  # Missing required fields
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class PlaylistAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        self.playlist_data = {
            'name': 'Test Playlist',
            'description': 'Test Description',
            'mood': 'happy',
            'genre': 'pop',
            'activity': 'workout'
        }

    def test_create_playlist(self):
        url = reverse('playlist-list')
        response = self.client.post(url, self.playlist_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Playlist.objects.count(), 1)
        self.assertEqual(Playlist.objects.get().name, 'Test Playlist')

    def test_list_playlists(self):
        Playlist.objects.create(user=self.user, **self.playlist_data)
        url = reverse('playlist-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete_playlist(self):
        playlist = Playlist.objects.create(user=self.user, **self.playlist_data)
        url = reverse('playlist-detail', kwargs={'pk': playlist.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Playlist.objects.count(), 0)