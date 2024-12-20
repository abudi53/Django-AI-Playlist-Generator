import os
import json
import google.generativeai as genai
from django.conf import settings

class GeminiService:
    def __init__(self):
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp')

    def generate_playlist(self, mood: str, genre: str, activity: str) -> list:
        prompt = (
            f"Generate a playlist of 5 songs that match these criteria:\n"
            f"Mood: {mood}\n"
            f"Genre: {genre}\n"
            f"Activity: {activity}\n\n"
            f"Return only a JSON array with this format:\n"
            f'[{{"title": "Song Title", "artist": "Artist Name"}}]'
        )

        try:
            response = self.model.generate_content(prompt)
            # Clean up the response text
            text = response.text.strip()
            
            # Remove markdown code blocks if present
            if '```json' in text:
                text = text.replace('```json', '').replace('```', '')
            elif '```' in text:
                text = text.replace('```', '')
                
            # Clean up any extra whitespace and newlines
            text = text.strip()
                        
            # Parse JSON
            try:
                playlist = json.loads(text)
                if not isinstance(playlist, list):
                    raise ValueError("Response is not a JSON array")
                return playlist
            except json.JSONDecodeError as je:
                print(f"JSON Decode Error: {je}, Text: {text}")  # Debug print
                raise ValueError(f"Invalid JSON format: {je}")
                
        except Exception as e:
            raise ValueError(f"Error generating playlist: {str(e)}")