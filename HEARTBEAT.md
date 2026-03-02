# HEARTBEAT.md - Automatic Maintenance Tasks

## On Every Heartbeat

### 1. Initialize Daily Memory
```bash
python3 /home/pablo/init_memory.py
```
- Crea `memory/YYYY-MM-DD.md` si no existe
- Template base para notas del día
- No sobrescribe si ya existe

### 2. Extract Memory Facts (cada 3h)
```bash
python3 /home/pablo/memory_extractor.py
```
- Lee `memory/*.md` de últimos 30 días
- Extrae hechos importantes (decisiones, configs, lecciones)
- Guarda en `facts.jsonl`
- Mantiene solo últimos 7 días

### 3. Inject Memory into Prompt (cada 3h, +15min)
```bash
python3 /home/pablo/inject_memory.py
```
- Lee `facts.jsonl` recientes
- Actualiza `[Recent Memory]` en system prompt
- HAL ya tiene contexto en próxima sesión

---

## Cron Jobs Registered

✅ **init_daily_memory** - 00:00 cada día
✅ **extract_memory_facts** - Cada 3 horas (00:00, 03:00, 06:00...)
✅ **inject_memory_prompt** - Cada 3 horas +15min (00:15, 03:15, 06:15...)

Los 3 scripts funcionan en paralelo + automático via cron + manual en heartbeat.

---

## What Gets Saved

### `memory/YYYY-MM-DD.md`
- Daily notes en formato markdown
- Creado automáticamente al inicio del día
- HAL actualiza manualmente durante la sesión
- Cualquier evento/decisión importante va aquí

### `facts.jsonl`
```json
{
  "timestamp": "2026-02-20T09:15:00",
  "date": "2026-02-20",
  "category": "decision|config|lesson|goal",
  "text": "Texto del fact",
  "extracted_by": "memory_extractor.py"
}
```

### `system-prompt.txt` (updated)
```
[Recent Memory - Last 7 Days]

- [DECISION] 2026-02-20: Mission Control frontend built
- [CONFIG] 2026-02-20: NextJS + Tailwind setup complete
- [LESSON] 2026-02-19: Memory persistence is critical
```

---

## Result: Continuidad Entre Sesiones

```
Sesión 1:
  └─ HAL hace cosas
  └─ Auto-guarda en memory/YYYY-MM-DD.md
  └─ Extractor corre c/3h → facts.jsonl
  └─ Inyector corre c/3h → system prompt

Sesión 2:
  └─ HAL despierta con [Recent Memory] en su prompt
  └─ Recuerda lo importante de sesión anterior
  └─ Continuidad garantizada
```

---

**Implementado:** 2026-02-20 09:17
**Scrips:** 
- `/home/pablo/init_memory.py`
- `/home/pablo/memory_extractor.py`
- `/home/pablo/inject_memory.py`
