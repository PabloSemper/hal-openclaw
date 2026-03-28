# TOOLS.md - Infraestructura Grupo Norte SRL

## Pablo
Pablo Semper. Administrador técnico de Grupo Norte SRL, La Pampa, Argentina.
Prefiere respuestas directas, pasos claros y soluciones prácticas.

## Servidor principal
- Host: serveria, IP local: 192.168.68.70
- OS: Ubuntu 24.04 LTS
- GPU: RTX 3080 Ti 12GB
- Ollama puerto: 11434
- OpenClaw gateway: 18789

## Estaciones YPF (8 estaciones en La Pampa)
- YPF Norte — RPi5, supervisor: Juan, empleados: Matías, Miriam, Celeste, Fabio
- YPF Ameghino — RPi4, empleados: Luciano
- YPF Cruz del Sur — RPi5
- Red: Tailscale VPN entre todas las estaciones

## Capacidades del agente
- Ejecutar bash, Python, scripts
- Leer/escribir archivos
- Diagnóstico de red: ping, nmap, traceroute
- Gestión de servicios systemd

## Proyectos activos
- Audio monitoring: AssemblyAI (Norte) + Whisper local (Ameghino)
- Video analytics: Hailo-8L + RTSP streams Dahua DVR
- Dashboard ventas: Supabase/Lovable
- HAL en NUC (100.89.112.80): OpenClaw + Claude API
