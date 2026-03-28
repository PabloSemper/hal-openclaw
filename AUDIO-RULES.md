# 🎤 AUDIO RULES - HAL Response Protocol

## LA REGLA DEFINITIVA

### Si recibe AUDIO:
```
Audio WhatsApp → Whisper STT → Transcribe → Process → Generate response → ElevenLabs TTS (Agustín) → Audio WhatsApp
```
**Pablo envía:** 🎙️ Audio
**HAL responde:** 🔊 Audio (voz Agustín)

### Si recibe TEXTO:
```
Texto WhatsApp → Process → Generate response → Texto WhatsApp
```
**Pablo envía:** 📝 Texto
**HAL responde:** 📝 Texto

---

## CONFIGURACIÓN

**Voz Oficial:**
- ID: `QK4xDwo9ESPHA4JNUpX3`
- Nombre: **Tomás**
- Acento: **Argentine Spanish (es-AR)**
- Género: **Masculino**
- Características: Pausado, profesional, claro

**STT (Speech to Text):**
- Herramienta: **Whisper OpenAI**
- Modelo: `base`
- Idioma: Spanish

**TTS (Text to Speech):**
- Provider: **ElevenLabs**
- Modelo: `eleven_multilingual_v2`
- Voz: **Tomás**
- Stability: 0.75
- Similarity: 0.75

---

## ZONA HORARIA

**SIEMPRE:** Mostrar hora como `HH:MM La Pampa`

Ejemplos:
- ✅ "Son las 22:15 La Pampa"
- ✅ "09:30 La Pampa"
- ❌ "00:15 UTC"
- ❌ "10:15 AM"

---

## IMPLEMENTACIÓN

Archivo: `audio-handler.py`
- Detecta tipo de mensaje (audio/texto)
- Enruta respuesta según tipo
- Genera audio con Agustín si es necesario

---

**Status:** ✅ DEFINITIVO
**Date:** 2026-02-12 22:11 La Pampa
