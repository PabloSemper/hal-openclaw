# 🐳 HAL OpenClaw - Docker Deployment

HAL ahora es **containerizado** y puede ejecutarse en cualquier máquina con Docker.

## Arquitectura

```
┌─────────────────────────────────┐
│   Docker Container              │
│  ┌──────────────────────────┐   │
│  │ HAL OpenClaw (Main)      │   │
│  │ - Node.js + OpenClaw     │   │
│  │ - Python tools           │   │
│  │ - SSH (puerto 22)        │   │
│  │ - Gateway (18789)        │   │
│  └──────────────────────────┘   │
│  ┌──────────────────────────┐   │
│  │ Ollama (Embeddings)      │   │
│  │ - nomic-embed-text       │   │
│  │ - Puerto 11434           │   │
│  └──────────────────────────┘   │
└─────────────────────────────────┘
```

## Instalación

### Prerequisitos
- Docker 20.10+
- Docker Compose 2.0+
- 4GB RAM mínimo
- 10GB espacio disco

### Quick Start

```bash
# 1. Clone el repo
git clone https://github.com/PabloSemper/hal-openclaw.git
cd hal-openclaw

# 2. Build images
docker-compose build

# 3. Start services
docker-compose up -d

# 4. Verify
docker-compose ps
```

## Uso

### SSH a HAL
```bash
ssh pablo@localhost
# Password: 25851069
```

### Ver logs
```bash
docker-compose logs -f hal
docker-compose logs -f ollama
```

### Ejecutar comandos
```bash
docker-compose exec hal python3 /home/pablo/clawd/tuya-smartlife.py
docker-compose exec hal smbclient -L 192.168.100.155 -N
```

### Actualizar código
```bash
cd /home/pablo/clawd
git pull origin main
docker-compose restart hal
```

## Deployment en Cloud

### AWS EC2 / DigitalOcean / Linode

```bash
# 1. SSH a servidor
ssh user@your-server-ip

# 2. Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# 3. Clone HAL
git clone https://github.com/PabloSemper/hal-openclaw.git
cd hal-openclaw

# 4. Start
docker-compose up -d

# 5. Access
ssh pablo@localhost
```

### Con GPU (para cracking WiFi)

Edita `docker-compose.yml`:

```yaml
services:
  hal:
    # ... resto de config ...
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
```

Requiere: `nvidia-docker` instalado

## Variables de Entorno

```bash
# .env (crear en raíz del proyecto)
OPENCLAW_MODE=production
OLLAMA_HOST=http://ollama:11434
GITHUB_TOKEN=ghp_...
TAILSCALE_TOKEN=tskey_...
```

## Persistencia

Todos los datos importantes en volumes:

```
./memory/          → Archivos de memoria (local)
./MEMORY.md        → Long-term memory
./SOUL.md          → Identidad de HAL
OLLAMA DATA        → Vector embeddings
SSH KEYS           → Para autenticación
```

## Escalabilidad

Futura: Multi-node cluster

```yaml
# hal-master (control plane)
# hal-worker-1 (GPU cracking)
# hal-worker-2 (Tailscale routing)
# hal-worker-3 (Pentesting tools)
```

## Troubleshooting

### Container no inicia
```bash
docker-compose logs hal
docker-compose down -v  # Reset
docker-compose up --build
```

### SSH no funciona
```bash
docker-compose exec hal sudo sshd -D
```

### Ollama no responde
```bash
docker-compose logs ollama
docker-compose restart ollama
```

## Próximos Pasos

1. **Push a Docker Hub** (público o privado)
2. **Kubernetes deployment** (para escalar)
3. **Auto-scaling** basado en carga
4. **Multi-cloud** (AWS + DigitalOcean + GCP)

---

**Estado:** Dockerización Fase 1 completada ✅
**Próximo:** Deployment a VPS con GPU
