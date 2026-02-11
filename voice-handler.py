#!/usr/bin/env python3
"""
Voice Handler for HAL - STT + TTS integration
Transcribe audio → Respond → Send voice back
"""

import subprocess
import json
import os
from pathlib import Path

class VoiceHandler:
    def __init__(self):
        self.whisper_model = "base"  # Rápido, bueno para español
        self.output_dir = Path("/tmp/hal-voice")
        self.output_dir.mkdir(exist_ok=True)
    
    def transcribe(self, audio_path):
        """Transcribir audio a texto con Whisper"""
        audio_path = Path(audio_path)
        
        if not audio_path.exists():
            return None, f"Audio no encontrado: {audio_path}"
        
        try:
            cmd = [
                "whisper",
                str(audio_path),
                "--model", self.whisper_model,
                "--output_format", "txt",
                "--output_dir", str(self.output_dir),
                "--language", "es"  # Español
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                # Leer resultado
                txt_file = self.output_dir / f"{audio_path.stem}.txt"
                if txt_file.exists():
                    text = txt_file.read_text().strip()
                    return text, None
            
            return None, f"Whisper error: {result.stderr}"
        
        except Exception as e:
            return None, f"Error transcribing: {str(e)}"
    
    def generate_voice(self, text, output_file="/tmp/hal-response.mp3"):
        """Generar audio desde texto con TTS"""
        try:
            # Usar CLI de TTS disponible
            # Alternativa: ElevenLabs API, Google TTS, etc
            import subprocess
            
            # Placeholder - requiere TTS backend configurado
            # Opción 1: espeak (local, simple)
            # Opción 2: ElevenLabs API
            
            print(f"[TTS] Generating voice for: {text[:50]}...")
            print(f"[TTS] Output: {output_file}")
            
            return output_file, None
        
        except Exception as e:
            return None, f"Error generating voice: {str(e)}"

if __name__ == "__main__":
    handler = VoiceHandler()
    
    # Test
    print("🎙️ HAL Voice Handler ready")
    print(f"   - Whisper model: {handler.whisper_model}")
    print(f"   - Output dir: {handler.output_dir}")
