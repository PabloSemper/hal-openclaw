# Protocolo Operativo — Cámaras Norte

## Objetivo
Estandarizar cómo HAL revisa cámaras de Norte, cómo informa resultados y cómo deja evidencia verificable.

## Flujo obligatorio (sin excepción)
1. **Captura / revisión** de cámaras activas (RTSP o nodo, según disponibilidad).
   - Si el pedido es “panorama”, “mirá Norte”, “analizá Norte” o equivalente: la captura debe ser **en vivo al momento del pedido**.
2. **Análisis operativo** con estos puntos mínimos:
   - Ocupación (baja/media/alta)
   - Estado de caja/personal
   - Riesgos visibles (incidentes, obstrucciones, conflicto)
   - Calidad de imagen (contraluz, enfoque, etc.)
   - Semáforo final (🟢/🟡/🔴)
3. **Respuesta al usuario** en texto corto y claro, incluyendo siempre:
   - "Captura en vivo: SÍ/NO"
   - "Hora de captura"
   - "Antigüedad (min)"
4. **Persistencia obligatoria**:
   - Registrar evento en `memory/YYYY-MM-DD.md`
   - Si hay valor duradero, actualizar `MEMORY.md`
   - Guardar informe `.md` en `security_reports/YYYY-MM-DD/ypf-norte/`
5. **Trazabilidad**:
   - Commit git con mensaje explícito del evento.

## Plantilla oficial de informe (copiar/pegar)
- Fecha/hora:
- CAM1:
- CAM2:
- Ocupación:
- Caja/personal:
- Riesgos:
- Calidad de imagen:
- Semáforo:
- Recomendación:
- Evidencia:
- Commit:

## Regla de ejecución a pedido de Pablo
Cuando Pablo pida: **"analizá Norte"**, **"mirá Norte"**, **"traeme informe Norte"** o equivalente:
1. HAL ejecuta captura de CAM1 y CAM2.
2. HAL entrega informe en esta plantilla oficial.
3. HAL adjunta/manda capturas si se las pide.
4. HAL registra en `memory/YYYY-MM-DD.md`.
5. HAL guarda `.md` en `security_reports/YYYY-MM-DD/ypf-norte/`.
6. HAL hace commit para trazabilidad.

## Verificación (Pablo)
```bash
git -C /home/pablo/.openclaw/workspace log --oneline -n 20
grep -RIn "Norte\|camera\|cámara\|semáforo" /home/pablo/.openclaw/workspace/memory /home/pablo/.openclaw/workspace/security_reports /home/pablo/.openclaw/workspace/MEMORY.md
```

## Estado actual conocido
- Existe plantilla: `security_reports/PLANTILLA_INFORME_TIENDA_FULL.md`
- Existe informe puntual: `security_reports/2026-02-26/ypf-norte/INFORME_TIENDA_FULL_2026-02-26_1254-1258.md`
- Faltaba protocolo global explícito: este archivo lo corrige.
