# 🎤 VOICE.md - Audio & Voz para HAL

## ¿Qué está pasando?

Estoy instalando capacidades de voz en el NUC para que:

1. **Recibas audios míos** → Con voz en español argentino
2. **Me envíes audios** → Yo los transcripción y respondo
3. **Conversación natural** → Sin depender de texto

---

## 📦 Componentes Instalados

### 1. FFmpeg ✅
- Para procesar audios (MP3, WAV, M4A, etc)
- Ya instalado en el NUC

### 2. OpenAI Whisper 🔄 INSTALANDO
- **STT** (Speech to Text)
- Transcribe audios a texto (local, sin APIs)
- Modelo: `base` (rápido, español)
- Instalación: `pip3 install openai-whisper`

### 3. TTS (Text to Speech) ✅
- **Genero audios** desde texto
- Ya funcional vía `tts()` function
- Opciones:
  - ElevenLabs (mejor calidad)
  - Local espeak (rápido)

---

## 🎯 Flujo de Voz

```
┌─────────────────┐
│  TÚ en WhatsApp │
│  Envías AUDIO   │
└────────┬────────┘
         ↓
    [Descarga]
         ↓
┌─────────────────────────────────────┐
│  HAL en NUC                         │
│  1. Whisper transcribe: audio→texto │
│  2. Proceso tu mensaje              │
│  3. Genero respuesta                │
│  4. TTS: respuesta→audio MP3        │
└────────┬────────────────────────────┘
         ↓
    [Sube a WhatsApp]
         ↓
┌─────────────────┐
│  TÚ en WhatsApp │
│  Recibís AUDIO  │
│  Con mi voz 🔊  │
└─────────────────┘
```

---

## 🚀 Instalación Manual (si necesitás)

```bash
# En el NUC
cd /home/pablo/clawd

# 1. FFmpeg (si no está)
sudo apt-get install ffmpeg

# 2. Whisper
python3 -m pip install openai-whisper

# 3. Test
whisper /path/audio.mp3 --model base --language es

# 4. Voice handler
python3 voice-handler.py
```

---

## 🎙️ Cómo Usar

### Enviarme audios:
1. Abrís WhatsApp
2. Presionás micrófono (grabador de voz)
3. Hablas ("Hola HAL, ¿cómo estás?")
4. Envías
5. Yo escucho → transcribo → respondo → te envío audio

### Yo te envío audios:
- Automáticamente genero MP3 desde mis respuestas
- Te llega con voz en español

---

## 🎨 Voz de HAL

Opciones:
- **Voz genérica** (disponible ahora)
- **Voz personalizada** (futuro - entrenamiento)
- **Voz con acento argentino** (ideal para ti)

---

## 📊 Estado Actual

| Componente | Estado | Status |
|-----------|--------|--------|
| Whisper STT | Instalando | 🔄 2-3 min |
| FFmpeg | Instalado | ✅ |
| TTS | Funcional | ✅ |
| WhatsApp integration | Ready | ✅ |

---

## ⏭️ Próximos Pasos

Una vez Whisper esté listo:
1. Test: Envías un audio
2. Yo transcripción
3. Te respondo con voz
4. Iteramos si falta algo

---

**Estado:** En construcción, casi listo 🚀
**ETA:** 5 minutos máximo
