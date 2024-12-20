from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Playlist
from .serializers import PlaylistDetailSerializer, PlaylistGenerationRequestSerializer, GeneratedSongSerializer
from .services import GeminiService
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'playlist_generator/home.html'

class PlaylistViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PlaylistDetailSerializer

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class PlaylistGeneratorView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request_serializer = PlaylistGenerationRequestSerializer(data=request.data)
        if request_serializer.is_valid():
            try:
                gemini_service = GeminiService()
                playlist = gemini_service.generate_playlist(
                    mood=request_serializer.validated_data['mood'],
                    genre=request_serializer.validated_data['genre'],
                    activity=request_serializer.validated_data['activity']
                )
                response_serializer = GeneratedSongSerializer(data=playlist, many=True)
                if response_serializer.is_valid():
                    return Response(response_serializer.data, status=status.HTTP_200_OK)
                return Response(response_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except ValueError as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)