#!/usr/bin/env python3
"""
Audio Handler for HAL
Detect: Audio message → Respond with audio (Agustín voice)
Detect: Text message → Respond with text
"""

import os
import json
from pathlib import Path

ELEVENLABS_CONFIG = {
    "api_key": os.getenv("ELEVENLABS_API_KEY"),  # Set in .env
    "voice_id": "KqSsYz0buWgkvSbaGn1n",  # Agustín
    "model_id": "eleven_monolingual_v1"
}

class AudioHandler:
    def __init__(self):
        self.config = ELEVENLABS_CONFIG
    
    def detect_message_type(self, message):
        """
        Detecta si el mensaje es audio o texto
        Retorna: "audio" o "text"
        """
        if hasattr(message, 'media') and message.media:
            return "audio"
        elif hasattr(message, 'text') and message.text:
            return "text"
        return None
    
    def handle_audio_message(self, audio_path, transcription):
        """
        Si recibe AUDIO:
        1. Transcribe con Whisper
        2. Procesa la respuesta
        3. Genera AUDIO con voz Agustín
        4. Envía audio de vuelta
        """
        print(f"📥 Audio recibido: {audio_path}")
        print(f"📝 Transcripción: {transcription}")
        
        # Aquí va: Procesar con HAL, generar respuesta
        # Luego: Convertir respuesta a audio con ElevenLabs
        # Finalmente: Enviar audio
        
        return "audio_response.mp3"
    
    def handle_text_message(self, text):
        """
        Si recibe TEXTO:
        1. Procesa normalmente
        2. Responde con TEXTO
        """
        print(f"📝 Texto recibido: {text}")
        
        # Procesar con HAL, generar respuesta texto
        
        return "text_response"

if __name__ == "__main__":
    handler = AudioHandler()
    print("✅ Audio Handler ready")
    print(f"   Voice: Agustín (ID: {handler.config['voice_id']})")
    print(f"   Rule: Audio → Audio response, Text → Text response")
