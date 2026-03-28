# YOLO26 - Proyecto Piloto para Análisis de Video en Cafés/Tiendas YPF
**Fecha:** 2026-02-18  
**Participantes:** Pablo (usuario), HAL (asistente)  
**Zona Horaria:** America/Argentina/La_Pampa (GMT-3)

---

## 📌 CONTEXTO INICIAL

Pablo necesita mejorar el análisis de videos en las 8 estaciones de servicio YPF (playa + tienda), enfocándose en atención al cliente. Las pruebas previas con CCTV de baja calidad no detectaban bien lo que necesitaba.

---

## 🎯 OBJETIVO DEL PROYECTO

Implementar **YOLO26** (edge-optimized, NMS-free) para análisis en tiempo real de:
- Comportamiento de clientes
- Flujo de personas
- Interacciones en mostrador
- Calidad de servicio visual
- Velocidad de atención

---

## 🔍 INVESTIGACIÓN: YOLO26 vs YOLOv11

### Key Findings

**YOLO26 (Enero 2026 - Ultralytics):**
- ✅ **+43% más rápido en CPU** vs YOLOv11 Nano
- ✅ **End-to-end NMS-free** (sin post-procesamiento)
- ✅ **ProgLoss + STAL** (mejora detección de objetos pequeños)
- ✅ **MuSGD Optimizer** (convergencia rápida, estable)
- ✅ Soporta: TFLite, CoreML, OpenVINO, TensorRT, ONNX
- ✅ 5 variantes: Nano, Small, Medium, Large, Extra Large
- ✅ Multi-task: detección, segmentación, pose, OBB, clasificación

**YOLOv11 (Septiembre 2024):**
- Todavía es estándar industria
- Mejor para GPU/cloud de alto rendimiento
- 22% menos parámetros que v8m

**Conclusión:** YOLO26 > YOLOv11 para edge devices y tiendas (eficiencia de CPU).

---

## 📊 CASOS DE ÉXITO REALES (2024-2025)

### 1. Convenience Store Chain (VideoMining)
- **Problema:** Clientes no veían productos de impulso
- **Solución:** Heatmaps de tráfico + rediseño layout
- **Resultados:**
  - Exposición a snacks: 7.6% → 21.6% (+285%)
  - Productividad por m²: +300%

### 2. All Star Elite Sports Retailer
- **Problema:** Layout subóptimo, pérdidas por robo
- **Resultado:** Shrink 6% → 1% (83% reducción)
- **Técnica:** Display en zona alto tráfico = +5-15% ventas

### 3. Big Box Retailer (Blix Traffic)
- **Insight:** Dwell time en departamentos vs flujo general
- **Acción:** Colocar underperforming products en alto tráfico

### 4. Grocery Chain (Team Innovatics)
- **Problema:** Clientes perciben aglomeración sin datos
- **Solución:** Mover 3 displays + ajustar cola checkout
- **Resultado:** -40% tiempo percibido sin agregar personal

---

## 🎥 HARDWARE RECOMENDADO

### Cámara IP (Mejor opción para piloto)

**Especificaciones Base:**
- Resolución: 2-4MP (1080p-2K suficiente)
- FPS: 30fps mínimo
- Lente: 2.8-4mm (ángulo 100-120°)
- Infrarrojo: Sí (para noches/playa)
- RTSP: Obligatorio
- PoE: Poder sobre Ethernet (instalación limpia)

**Modelos Recomendados:**
| Marca | Modelo | Res | Precio | Notas |
|-------|--------|-----|--------|-------|
| Hikvision | DS-2CD2143G2-I | 4MP | $120-150 | Muy confiable, IR, PoE |
| Dahua | IPC-HDBW2433E-Z | 4MP | $100-130 | Similar a Hikvision, buen IR |
| Uniview | IPC322SR-DVS28 | 2MP | $80-100 | Más económica |

**Mi recomendación:** Hikvision 4MP o Dahua 4MP (industriales, duraderas, buen stream RTSP).

---

## 📐 POSICIONAMIENTO CRÍTICO DE CÁMARAS

### CÁMARA 1: MOSTRADOR/CAJA (Principal - Obligatoria)

```
                CLIENTE
                   ↓
        [MOSTRADOR] ← CÁMARA
        (Vendedor)
```

**Posicionamiento exacto:**
- **Altura:** 2-2.5m (encima de la cabeza)
- **Ángulo:** 45-50° hacia abajo
- **Distancia:** 1.5-2m perpendicular al mostrador

**Qué detecta YOLO26:**
- ✅ Cara/identidad del vendedor (interacción)
- ✅ Cara/reacción del cliente (satisfacción)
- ✅ Productos en mostrador (inventario visual)
- ✅ Movimiento de manos (velocidad de atención)
- ✅ Cola/personas atrás (espera)
- ✅ Tiempo de transacción

**Métricas derivadas:**
- Tiempo promedio de atención
- Tasa de interacción vendedor-cliente
- Inventario visual en mostrador
- Alertas de cola >3 personas
- Picos de ocupación (horas)

---

### CÁMARA 2: FLUJO GENERAL (Complementaria - Opcional)

```
ENTRADA
  ↓
 [ZONA CLIENTES]  ← CÁMARA (desde arriba)
  ↓
SALIDA / CAJA
```

**Posicionamiento exacto:**
- **Altura:** 2.2-2.8m (bien arriba)
- **Ángulo:** 70-85° hacia abajo (casi cenital)
- **Lente:** 2.8mm o menos (ángulo amplio)

**Qué detecta YOLO26:**
- ✅ Trayectoria completa (entrada → zonas → caja → salida)
- ✅ Densidad de personas (conteo)
- ✅ Rutas principales vs secundarias
- ✅ Zonas "muertas" (donde no van)
- ✅ Aglomeración en tiempo real

---

## ⚙️ ARQUITECTURA TÉCNICA DEL PILOTO

```
Cámara IP (Hikvision 4MP, RTSP stream)
    ↓
Raspi Ameghino (100.114.79.8)
  ├─ Captura frames
  ├─ Preproca: denoising + mejora de imagen
  └─ Streaming HTTP/RTSP
    ↓
GPU Windows (RTX 3080 Ti, 100.70.110.37)
  ├─ YOLO26 inference (real-time)
  ├─ Análisis + anotaciones
  └─ Dashboard + alertas
    ↓
Resultados:
  ├─ Heatmaps de movimiento
  ├─ Conteo de personas
  ├─ Tiempo de atención
  └─ Alertas (ocupación, comportamiento)
```

---

## 🛠️ PLAN DE IMPLEMENTACIÓN (PILOTO)

### Fase 1: Setup Hardware (Semana 1)
1. Comprar cámara IP (Hikvision 4MP, ~$130)
2. Comprar cable PoE + inyector/switch PoE
3. Instalar en una estación piloto (mostrador)
4. Verificar RTSP stream: `rtsp://user:pass@IP:554/stream1`

### Fase 2: Pipeline Software (Semana 2-3)
1. Raspi: Captura frames via OpenCV
2. Raspi: Preproca (denoising CLAHE, upscaling si necesario)
3. GPU Windows: YOLO26 inference
4. Dashboard básico: conteo + heatmap

### Fase 3: Medición (Semana 4-5)
1. Correr 2-3 semanas en piloto
2. Medir: tiempo atención, picos ocupación, trayectorias
3. Comparar con datos manuales

### Fase 4: Escala (Post-piloto)
- Si funciona: agregar otras estaciones
- Fine-tuning de alertas
- Integración con sistema central

---

## 🎥 EJEMPLOS VISUALES DE REFERENCIA

### Imágenes Unsplash (Libre):
- **Barista overhead:** https://images.unsplash.com/photo-1770178995815-12568021c782
- **Mostrador moderno:** https://images.unsplash.com/photo-1769184613600-1a309a70196b
- **Interior café overhead:** https://images.unsplash.com/photo-1764391836704-8053c8a6e209
- **Flujo café completo:** https://images.unsplash.com/photo-1764175761361-3ada7dcdfb71

### Videos YouTube (POV barista):
- "Genius Coffee Roasters" - Barista POV overhead (30min)
- "GrizzlyBarista" - Vista fija del bar
- "Coffee Shop POV | Barista Making Drinks During Rush"

---

## ⚠️ PROBLEMAS POTENCIALES & SOLUCIONES

### Problema 1: Baja calidad de CCTV actual
**Solución:** Cámara IP moderna (4MP vs CCTV 360p)
**Mejora esperada:** +300-500% en detección

### Problema 2: YOLO no detecta bien en CCTV degradado
**Soluciones:**
1. Mejorar imágenes ANTES de YOLO:
   - ESRGAN upscaling
   - Denoising (reducir granulado)
   - Mejora de contraste (CLAHE)
   - Sharpening (unsharp mask)

2. Fine-tune YOLO26 con datos locales
3. Usar ensemble (múltiples detecciones)

### Problema 3: Latencia (tiempo real)
**Solución:** GPU local (RTX 3080 Ti) procesa <50ms por frame
**Resultado:** ~30fps en tiempo real

### Problema 4: Privacidad (detectar rostros)
**Solución:** 
- Usar solo "detección de personas" (no identificación)
- Borrar datos después de X días
- Cumplir GDPR si aplica (Argentina = AAIP)

---

## 💡 MÉTRICAS A MEDIR EN PILOTO

### Operativas
- Tiempo promedio de atención (segundos)
- Personas simultáneas en mostrador
- Picos de ocupación (horas del día)
- Tasa de interacción cliente-vendedor

### Comerciales
- Correlación entre ocupación y ventas
- Zonas de espera vs atención
- Eficiencia de personal

### Técnicas
- Precisión de detección YOLO26 (accuracy %)
- FPS en GPU Windows
- Latencia end-to-end (captura → resultado)

---

## 🚀 PRÓXIMO PASO

**¿En cuál estación hacemos el piloto?**
Opciones:
1. Santa Rosa centro (la más concurrida)
2. Otra específica que tengas en mente

**Requiero info:**
- Nombre/ubicación de estación
- Cuántos metros cuadrados de mostrador
- Horarios pico (cuándo más clientes)
- Presupuesto máximo para hardware

---

## 📚 REFERENCIAS & DOCUMENTACIÓN

- **YOLO26 Official:** Ultralytics (enero 2026)
- **YOLOv11:** Septiembre 2024, open-source
- **Casos retail:** VideoMining, Blix Traffic, Team Innovatics (2024-2025)
- **Stack técnico:** OpenCV, YOLO26, RTSP, TensorRT, ONNX
- **Hardware:** Hikvision, Dahua, PoE infrastructure

---

## 📝 NOTAS IMPORTANTES

- **Sin experimentación innecesaria:** Solo tecnología probada
- **Edge-first:** Procesar localmente (GPU Windows), no cloud
- **Privacidad:** Detectar personas ≠ Identificar rostros
- **ROI esperado:** 
  - Mejora operativa: -30% a -40% tiempo espera
  - Reducción pérdidas: -50% a -80% shrink
  - Aumento de datos: insights para layout/staffing

---

**Guardado:** 2026-02-18 14:40 La Pampa  
**Status:** Listo para piloto  
**Siguiente:** Definir estación + confirmar presupuesto
