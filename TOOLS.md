# TOOLS.md - Herramientas y Configuración Local

## QMD - Base de Conocimiento Local

### Ubicación
- **Carpeta de conocimiento:** `~/knowledge`
- **Colección:** `conocimiento`
- **Índice:** `~/.cache/qmd/index.sqlite`

### Buscar información
Antes de responder preguntas técnicas o sobre proyectos, buscar en la base local:
```bash
# Búsqueda rápida por keywords (PREFERIR ESTA)
qmd search "mikrotik firewall" -c conocimiento

# Búsqueda semántica (si keywords no encuentra)
qmd vsearch "cómo configurar el router" -c conocimiento

# Ver documento específico
qmd get qmd://conocimiento/archivo.md
```

### Guardar conocimiento nuevo
Cuando Pablo comparta información importante (configs, soluciones, documentación):
```bash
# Crear archivo en ~/knowledge
echo "contenido" > ~/knowledge/nombre-descriptivo.md

# Re-indexar
qmd update

# Actualizar embeddings (solo si es necesario búsqueda semántica)
qmd embed
```

### Estructura recomendada para ~/knowledge
```
~/knowledge/
├── configs/          # Configuraciones de equipos
├── proyectos/        # Documentación de proyectos
├── soluciones/       # Problemas resueltos
├── procedimientos/   # Paso a paso de tareas comunes
└── referencias/      # Info técnica general
```

### Cuándo guardar
- Configuraciones que funcionaron
- Soluciones a problemas
- Procedimientos que Pablo pide repetidamente
- Información técnica específica del entorno

---

## Infraestructura

### SSH Hosts
- NUC: localhost (este servidor)
- Tailscale: activo para acceso remoto

### Estaciones YPF
- Cruz del Sur, Norte, Ameghino, General Acha, etc.
- Total: 8 estaciones en La Pampa

### Hardware disponible
- Raspberry Pi 3B+, 4, 5
- Routers MikroTik
- Cámaras Dahua
- Hailo-8 (aceleración IA)

---

## Notas
- Skills definen *cómo* funcionan las herramientas
- Este archivo tiene la configuración *específica* de Pablo
- Actualizar cuando cambie la infraestructura
