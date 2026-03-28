# OpenClaw: Capacidades & Skills Detallados

## 📋 CAPACIDADES PRINCIPALES (Fuentes verificadas)

Según documentación oficial: `/home/pablo/.npm-global/lib/node_modules/openclaw/docs/concepts/features.md`

### Canales de Comunicación
- ✅ **WhatsApp** (via Baileys - WhatsApp Web automation)
- ✅ **Telegram** (bot support via grammY)
- ✅ **Discord** (channels.discord.js)
- ✅ **iMessage** (macOS via local imsg CLI)
- 🔌 **Mattermost** (plugin support)

### Routing & Sessions
- ✅ **Multi-agent routing** - Isolated sessions por workspace o sender
- ✅ **Direct chats** - Collapse a sesión `main` compartida
- ✅ **Group chats** - Soporte con mention-based activation
- ✅ **Agent bridge** - Pi en RPC mode con tool streaming

### Media & I/O
- ✅ **Images** (entrada y salida)
- ✅ **Audio** (grabación, transcripción opcional)
- ✅ **Documents** (PDFs, archivos varios)
- ✅ **Voice transcription hook** - Integración STT

### UI & Apps
- ✅ **Web Control UI** - Dashboard web
- ✅ **macOS Companion App** - Menu bar, native integration
- ✅ **iOS Node** - Pairing, Canvas support
- ✅ **Android Node** - Pairing, Canvas, chat, camera

### Autenticación & Modelos
- ✅ **OAuth Subscription Auth** - Anthropic y OpenAI
- ✅ **Streaming & Chunking** - Para respuestas largas
- ✅ **Pi Coding Agent** - Reemplazo de Claude/Codex/Gemini (legacy removed)

---

## 🛠️ SKILLS INSTALADOS EN WORKSPACE

Ubicación: `/home/pablo/clawd/skills/` (19 skills)

### 1. **Automatización & Navegación**
| Skill | Función | Status |
|-------|---------|--------|
| `agent-browser` | Navegación web automatizada (Playwright headless) | ✅ Instalado |
| `agent-browser-tekken` | Fast Rust-based browser automation | ✅ Instalado |
| `web-scraper` | Web scraping configurable (BM25 + vectors) | ✅ Instalado |

### 2. **Búsqueda & Información**
| Skill | Función | Status |
|-------|---------|--------|
| `web-search-plus` | Búsqueda unificada (Serper, Tavily, Exa, You.com, SearXNG) | ✅ Instalado |
| `summarize` | Resumen de URLs, PDFs, imágenes, audio, YouTube | ✅ Instalado |
| `qmd` | Búsqueda local BM25 + vectors + rerank (MCP mode) | ✅ Instalado |

### 3. **Desarrollo & Código**
| Skill | Función | Status |
|-------|---------|--------|
| `github` | Interacción GitHub (issues, PRs, CI runs, API) | ✅ Instalado |
| `readme-generator` | Auto-generate README.md analizando proyectos | ✅ Instalado |
| `db-backup` | Scripts backup automáticos (PG, MySQL, SQLite, MongoDB) | ✅ Instalado |
| `skill-creator` | Crear/actualizar AgentSkills con assets | ✅ Instalado |

### 4. **IA & Visión**
| Skill | Función | Status |
|-------|---------|--------|
| `nano-banana-ultra` | Generación de imágenes (Gemini 3 Pro) | ✅ Instalado |
| `openai-whisper` | STT local (sin API key) | ✅ Instalado |

### 5. **Criptomonedas & Trading**
| Skill | Función | Status |
|-------|---------|--------|
| `binance-pro` | Binance integración completa (spot, futures 125x, staking) | ✅ Instalado |
| `binance-hunter` | AI market analysis + auto-risk (125x leverage) | ✅ Instalado |

### 6. **Seguridad & Hardening**
| Skill | Función | Status |
|-------|---------|--------|
| `dont-hack-me` | Security self-check para Clawdbot (config audit + auto-fix) | ✅ Instalado |
| `prompt-guard` | Token-optimized prompt injection defense (500+ patterns) | ✅ Instalado |

### 7. **Utilidades & Helpers**
| Skill | Función | Status |
|-------|---------|--------|
| `find-skills` | Descubrir e instalar skills cuando el usuario lo pide | ✅ Instalado |
| `predictme` | Predicción (mercados, deportes, eventos) | ✅ Instalado |
| `camsnap` | Captura de frames/clips desde RTSP/ONVIF | ✅ Instalado |

---

## 🎯 CAPACIDADES DEL SISTEMA (Skills Framework)

Según: `/home/pablo/.npm-global/lib/node_modules/openclaw/docs/tools/skills.md`

### Gating & Load Rules
- ✅ **Precedencia:** Workspace > Managed > Bundled skills
- ✅ **Filtros por:** Binarios requeridos, variables env, config flags, SO
- ✅ **Metadata gating:** Secure load-time filtering
- ✅ **Plugin skills:** Skills pueden venir empaquetados en plugins

### ClawHub Registry
- 🔗 **URL:** https://clawhub.com
- ✅ **Comandos:** `clawhub install`, `clawhub update --all`, `clawhub sync`
- ✅ **Instalación:** En `./skills` o workspace configurado
- ✅ **Público + privado:** Skills públicos + custom privados

### Config & API Keys
- ✅ **Inyección env:** Por skill, scoped a agent run
- ✅ **Secret management:** Vía `skills.entries.<key>.apiKey`
- ✅ **Hot reload:** Skills watcher auto-refresh en cambios SKILL.md
- ✅ **Sandboxing:** Skills pueden ejecutarse en contenedores Docker

### Token Impact
- 📊 **Base overhead:** 195 caracteres (cuando ≥1 skill)
- 📊 **Por skill:** 97 caracteres + length(name + description + location)
- 📊 **Estimado:** ~24 tokens por skill (OpenAI-style)

---

## 🚀 CARACTERÍSTICAS ADICIONALES

### Canales de Comunicación Avanzados
- **Agent Bridge:** Pi en RPC mode con **tool streaming** (no solo respuestas)
- **Multi-agent routing:** Cada sender/workspace obtiene sesión aislada
- **Media attachments:** Imágenes, audio, docs con context awareness

### Debugging & Observabilidad
- ✅ **OpenClaw logs:** Full audit trail
- ✅ **Session snapshots:** Estado de skills al iniciar sesión
- ✅ **Remote node probes:** macOS nodes como sistema de extensión
- ✅ **Watcher mode:** Auto-refresh de skills en cambios

### Seguridad
- ✅ **Plugin auth gating:** Requerimientos de config/env
- ✅ **Sandbox support:** Ejecutar skills en contenedores aislados
- ✅ **Trusted proxy headers:** Para reverse proxy setups
- ✅ **Prompt guard:** Inyección defense (500+ patrones)

---

## 📊 ECOSISTEMA TOTAL

**Skills instalados:** 19
**Canales soportados:** 5 (WhatsApp, Telegram, Discord, iMessage, Mattermost)
**Plataformas:** macOS, Linux, Windows (parcial)
**Nodes:** iOS (full), Android (full)
**Modelos:** Anthropic (native), OpenAI (oauth)

---

## 🔗 FUENTES VERIFICADAS

1. **Skills framework:** `/home/pablo/.npm-global/lib/node_modules/openclaw/docs/tools/skills.md`
2. **Features generales:** `/home/pablo/.npm-global/lib/node_modules/openclaw/docs/concepts/features.md`
3. **Skills instalados:** `/home/pablo/clawd/skills/` (19 directorios)
4. **ClawHub registry:** https://clawhub.com
5. **Documentación oficial:** https://docs.openclaw.ai
6. **GitHub:** https://github.com/openclaw/openclaw

---

**Actualizado:** 2026-02-14
**Nota:** Todas las capacidades son funcionales y verificadas en el workspace local.
