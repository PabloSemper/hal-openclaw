# 🔍 INVESTIGACIÓN PROFUNDA: Nuevos Skills OpenClaw 2026

**Fecha:** 14 de Febrero de 2026  
**Versión de OpenClaw:** 2026.2.3-1  
**Investigador:** Subagent specializado

---

## Tabla de Contenidos

1. [Web Search Plus (Intelligent Auto-Routing)](#1-web-search-plus--intelligent-auto-routing)
2. [Device Pairing (iOS/Android)](#2-device-pairing-iosandroid)
3. [Feishu/Lark Plugin](#3-feishulark-plugin)
4. [QMD Memory Backend](#4-qmd-memory-backend)
5. [Embedding Providers (OpenAI, Gemini, Local)](#5-embedding-providers)
6. [Healthcheck Skill](#6-healthcheck-skill)

---

## 1. Web Search Plus 🔍 (Intelligent Auto-Routing)

### ¿Qué es?

**Web-search-plus** es un skill unificado que proporciona búsqueda web inteligente con **enrutamiento automático** entre 5 proveedores diferentes. A diferencia de `web_search` nativo de OpenClaw (que solo usa Brave), este skill elige automáticamente el mejor proveedor para cada consulta.

**Nombre en skill list:** `web-search-plus`  
**Estado:** ✓ Ready  
**Versión:** 2.6.1

### ¿Qué diferencia tiene de otras búsquedas?

| Aspecto | Brave Search (OpenClaw nativo) | Web-Search-Plus |
|--------|---|---|
| **Proveedores** | 1 (Brave) | 5 (Serper, Tavily, Exa, You.com, SearXNG) |
| **Selección** | Manual o nativa | Automática inteligente |
| **Análisis** | Búsqueda tradicional | Multi-signal analysis |
| **Casos de uso** | General | Especializado por tipo de query |
| **Costo** | 1 proveedor | 5 opciones (algunas gratis) |
| **Privacidad** | Brave | Incluye SearXNG (self-hosted) |

### Proveedores disponibles

#### 1. **Serper** (Google Search API)
- **Mejor para:** Shopping, local, precios
- **Velocidad:** ⚡⚡⚡ (Más rápido)
- **Precisión:** ⭐⭐⭐
- **Free tier:** 2,500 búsquedas/mes (sin tarjeta de crédito)
- **Casos de uso reales:**
  ```bash
  "iPhone 16 Pro Max price"          → Detecta shopping
  "best pizza near me"               → Detecta local
  "weather Berlin"                   → Consulta rápida
  ```

#### 2. **Tavily** (AI Research Search)
- **Mejor para:** Investigación profunda, academic papers
- **Velocidad:** ⚡⚡
- **Precisión:** ⭐⭐⭐
- **Free tier:** 1,000 búsquedas/mes
- **Ventajas:** Retorna contenido completo (raw_content), no solo snippets
- **Casos de uso reales:**
  ```bash
  "How does quantum entanglement work"     → Research profunda
  "Climate change studies 2024"            → Papers académicos
  "Explain machine learning"               → Explicaciones detalladas
  ```

#### 3. **Exa** (Neural/Semantic Search)
- **Mejor para:** Búsquedas por similitud, startups, papers
- **Velocidad:** ⚡⚡
- **Precisión semántica:** ⭐⭐⭐ (La mejor)
- **Free tier:** 1,000 búsquedas/mes
- **Ventajas:** "Similar to X", encuentra URLs conceptualmente similares
- **Casos de uso reales:**
  ```bash
  "companies similar to Notion"       → URL similar (similarity search)
  "startups like Stripe Series C"     → Descubrimiento de compañías
  "transformer papers arxiv"          → Research papers
  ```

#### 4. **You.com** (RAG/Real-time)
- **Mejor para:** Real-time info, LLM context, noticias
- **Velocidad:** ⚡⚡⚡
- **Precisión:** ⭐⭐⭐
- **Free tier:** Limitado, requiere testing
- **Ventajas:** Snippets optimizados para LLMs, combina web + news
- **Casos de uso reales:**
  ```bash
  "latest AI regulation news"         → Real-time
  "summarize key points on crypto"    → RAG-ready snippets
  "breaking tech news today"          → Combined web + news
  ```

#### 5. **SearXNG** (Privacy-First/Self-Hosted)
- **Mejor para:** Privacidad, multi-fuente, $0 costo
- **Velocidad:** ⚡⚡
- **Privacidad:** ⭐⭐⭐⭐⭐ (Si es self-hosted)
- **Costo:** **GRATIS** ($5/mes VPS si lo alojas)
- **Ventajas:** 70+ search engines, sin tracking
- **Casos de uso reales:**
  ```bash
  "search privately without tracking"        → Privacidad
  "alternative search engines"               → Multi-source
  "linux distros"                            → Resultados diversos
  ```

### Cómo funciona el Auto-Routing

El skill analiza tu consulta usando **5 señales**:

1. **Intent Classification:** Shopping vs Research vs Discovery vs RAG vs Privacy
2. **Linguistic Patterns:** "how much" (precio) vs "how does" (research)
3. **Entity Detection:** Productos+marcas, URLs, dominios
4. **Complexity Analysis:** Queries largas favorecen research providers
5. **Confidence Scoring:** Sabe qué tan confiado está en su decisión

### Ejemplo práctico de auto-routing

```bash
# Consulta de compra → Serper
python3 scripts/search.py -q "MacBook Pro M3 Max price"
# Routing decision: "MacBook" (product) + "price" → Serper (68% confidence)

# Consulta de investigación → Tavily
python3 scripts/search.py -q "how does quantum entanglement work"
# Routing decision: "how does" (explicación) → Tavily (86% HIGH confidence)

# Búsqueda semántica → Exa
python3 scripts/search.py -q "companies like Stripe"
# Routing decision: "companies like" (similarity) → Exa (100% HIGH confidence)

# Info real-time → You.com
python3 scripts/search.py -q "summarize latest AI news"
# Routing decision: "latest" + "AI news" → You.com (68% MEDIUM confidence)

# Privacidad → SearXNG
python3 scripts/search.py -q "search privately without tracking"
# Routing decision: "privately", "tracking" → SearXNG (74% HIGH confidence)
```

### Configuración técnica

**Ubicación del skill:** `/home/pablo/clawd/skills/web-search-plus/`

**Setup interactivo:**
```bash
cd /home/pablo/clawd/skills/web-search-plus/
python3 scripts/setup.py
```

**config.json:**
```json
{
  "defaults": {
    "provider": "serper",
    "max_results": 5
  },
  "auto_routing": {
    "enabled": true,
    "fallback_provider": "serper",
    "confidence_threshold": 0.3,
    "disabled_providers": []
  },
  "serper": {"country": "us", "language": "en"},
  "tavily": {"depth": "advanced"},
  "exa": {"type": "neural"},
  "you": {"country": "US", "include_news": true},
  "searxng": {"instance_url": "https://your-instance.example.com"}
}
```

### Casos de uso reales

#### 📱 Workflow: Comparativa de productos
```bash
# 1. Specs del producto (→ Serper)
python3 scripts/search.py -q "iPhone 16 Pro Max specifications"

# 2. Precios comparativos (→ Serper)
python3 scripts/search.py -q "iPhone 16 Pro Max best price 2024"

# 3. Reseñas detalladas (→ Tavily)
python3 scripts/search.py -p tavily -q "iPhone 16 Pro Max review analysis" --depth advanced
```

#### 🏢 Workflow: Análisis competitivo
```bash
# 1. Encontrar competidores (→ Exa)
python3 scripts/search.py -q "companies like Notion"

# 2. Productos similares (→ Exa)
python3 scripts/search.py -p exa --similar-url "https://notion.so"

# 3. Comparativa profunda (→ Tavily)
python3 scripts/search.py -p tavily -q "Notion vs Coda detailed comparison" --depth advanced
```

### Ventajas técnicas

✅ **Fallback automático:** Si un proveedor falla → intenta el siguiente  
✅ **Confidence scoring:** Sabes qué tan confiada está la decisión  
✅ **Override manual:** Force `-p serper` si quieres un proveedor específico  
✅ **Debug:** `--explain-routing` te muestra exactamente por qué eligió un proveedor  
✅ **Free tier:** 4,500+ búsquedas/mes gratis combinando todos los free tiers  

---

## 2. Device Pairing (iOS/Android) 📱

### ¿Qué es?

**Device Pairing** es un sistema que permite emparejar dispositivos iOS/Android con tu gateway de OpenClaw. Habilita acceso remoto seguro, token-based, a través de WebSocket sin exponer endpoints públicos.

**Introducido en:** OpenClaw 2026  
**CLI Principal:** `openclaw devices` y `openclaw nodes`  
**Modelo de seguridad:** Token rotativo, autorización explícita

### Conceptos clave

| Término | Significado |
|---------|------------|
| **Node** | Dispositivo iOS/Android que se conecta al gateway |
| **Gateway** | Servidor central que maneja pairing y auth |
| **Pending Request** | Dispositivo solicitando acceso (requiere aprobación) |
| **Paired Node** | Dispositivo aprobado con token válido |
| **Token** | Credencial de autenticación (se rota en cada re-pairing) |

### Arquitectura de flujo

```
Device iOS/Android
    ↓ (WS connect + pairing request)
Gateway (evalúa)
    ↓ (emite node.pair.requested event)
Control UI / CLI
    ↓ (Approve/Reject)
Gateway (genera token nuevo)
    ↓ (emite node.pair.resolved event)
Device (reconnecta con token)
    ↓ (paired + conectado)
Active Session
```

### Comandos disponibles

#### Listar dispositivos pendientes y emparejados
```bash
# Mostrar todos
openclaw devices list

# JSON para scripting
openclaw devices list --json

# Alternativamente con nodes
openclaw nodes pending
openclaw nodes status
```

#### Aprobar pairing
```bash
openclaw devices approve <requestId>

# Ejemplo real:
openclaw devices approve req_abc123def456
```

#### Rechazar pairing
```bash
openclaw devices reject <requestId>
```

#### Rotar token de dispositivo
```bash
openclaw devices rotate --device <deviceId> --role operator \
  --scope operator.read --scope operator.write

# Ejemplo:
openclaw devices rotate --device node_ipad_living_room --role operator
```

#### Revocar acceso
```bash
openclaw devices revoke --device <deviceId> --role operator

# Ejemplo:
openclaw devices revoke --device node_ipad_living_room --role operator
```

#### Renombrar dispositivo
```bash
openclaw nodes rename --node <id|name|ip> --name "Living Room iPad"

# Ejemplo:
openclaw nodes rename --node "192.168.1.50" --name "My AI iPad"
```

### Requisitos para emparejamiento

#### Del dispositivo (iOS/Android)
- ✅ App compatible de OpenClaw (future client)
- ✅ Conectividad a red (WiFi o cellular)
- ✅ Puede estar en LAN o remoto (vía Tailscale/VPN)

#### Del Gateway
- ✅ OpenClaw corriendo (`openclaw gateway status`)
- ✅ WebSocket endpoint accesible
- ✅ Permisos: `operator.pairing` o `operator.admin`

#### Configuración
```json5
{
  gateway: {
    nodes: {
      pairing: {
        enabled: true,
        requestExpiry: 300000  // 5 minutos
      }
    }
  }
}
```

### Flujo paso a paso: Emparejar un iPad

1. **En el iPad:** Abre app OpenClaw → "Pair with Gateway"
2. **En el Gateway:** `openclaw devices list` → ves `req_xxx` pending
3. **Decisión:**
   ```bash
   # Aprobar
   openclaw devices approve req_xxx
   # O rechazar
   openclaw devices reject req_xxx
   ```
4. **En el iPad:** Automáticamente recibe token nuevo
5. **Verificar:**
   ```bash
   openclaw nodes status
   # Output: "My AI iPad" (connected, paired)
   ```

### Seguridad y tokens

**Características:**
- ✅ Tokens se rotan en cada aprobación (nunca se reutilizan)
- ✅ Requests expiran en 5 minutos (configurable)
- ✅ Auto-approval opcional si hay SSH verificado (macOS)
- ✅ Permisos granulares por role y scope

**Almacenamiento local (privado):**
```
~/.openclaw/
├── nodes/
│   ├── paired.json      # Dispositivos emparejados (contiene tokens)
│   └── pending.json     # Requests pendientes
```

⚠️ **Nota:** `paired.json` contiene secrets → trátalo como sensible

### Casos de uso reales

#### Caso 1: Monitoreo remoto desde iPad
```bash
# En gateway (setup)
openclaw devices list
# Output: req_ipad_monitor pending

openclaw devices approve req_ipad_monitor

# En iPad: Ya conectado, puede monitorear alertas en tiempo real
```

#### Caso 2: Múltiples dispositivos en oficina
```bash
# Registra varios dispositivos
openclaw devices list
# Output: 
#   - ipad_desk (paired)
#   - ipad_conference (paired)
#   - iphone_emergency (pending)

# Rechaza el emergency iPhone
openclaw devices reject iphone_emergency

# Rota tokens trimestralmente
openclaw devices rotate --device ipad_desk --role operator
```

#### Caso 3: Revocar acceso comprometido
```bash
# Si un iPad se pierde
openclaw devices revoke --device ipad_office --role operator

# El dispositivo pierde acceso inmediatamente
```

### Detalles técnicos

**Protocolo:**
- WebSocket (no requiere HTTP público)
- Event-driven: `node.pair.requested`, `node.pair.resolved`
- RPC methods: `node.pair.request`, `node.pair.list`, `node.pair.approve`, `node.pair.reject`

**Idempotencia:**
```javascript
// Llamar node.pair.request múltiples veces del mismo dispositivo
// retorna el MISMO pending request (no duplica)
```

**Fallback silencioso (macOS):**
Si la app de macOS detecta SSH válido al mismo gateway host, intenta auto-aprobación (puede fallar y vuelve a prompt normal).

---

## 3. Feishu/Lark Plugin 🐉

### ¿Qué es?

**Feishu/Lark** es un plugin de canal que conecta OpenClaw a Feishu (plataforma de team chat usado por empresas chinas) o Lark (versión global). Usa **WebSocket de larga conexión** (sin webhook público).

**Introducido en:** OpenClaw 2026.2.2  
**Status:** ✓ Ready, produce en version 2026.2.2+  
**Plugin:** `@openclaw/feishu`

### Características principales

| Característica | Descripción |
|---|---|
| **Bot WebSocket** | Conexión de larga duración (event subscription sin webhook) |
| **Mensajes DM** | Policy: pairing, allowlist, open, disabled |
| **Grupos** | Puede requerir @mention o responder libre |
| **Multimedios** | Texto, imágenes, archivos, audio, video, stickers |
| **Comandos** | `/status`, `/reset`, `/model` |
| **Real-time** | Responde inmediatamente (sin polling) |

### Setup paso a paso

#### Paso 1: Crear app en Feishu Open Platform

1. Ve a https://open.feishu.cn/app (Feishu) o https://open.larksuite.com/app (Lark)
2. **Create enterprise app**
3. Completa: app name, description, icon
4. En **Credentials & Basic Info** copia:
   - **App ID** (formato: `cli_xxx`)
   - **App Secret** (mantener secreto)

#### Paso 2: Configurar permisos

En **Permissions**, importa batch:

```json
{
  "scopes": {
    "tenant": [
      "aily:file:read",
      "aily:file:write",
      "application:application.app_message_stats.overview:readonly",
      "application:application:self_manage",
      "application:bot.menu:write",
      "contact:user.employee_id:readonly",
      "corehr:file:download",
      "event:ip_list",
      "im:chat.access_event.bot_p2p_chat:read",
      "im:chat.members:bot_access",
      "im:message",
      "im:message.group_at_msg:readonly",
      "im:message.p2p_msg:readonly",
      "im:message:readonly",
      "im:message:send_as_bot",
      "im:resource"
    ]
  }
}
```

#### Paso 3: Habilitar Bot

En **App Capability** → **Bot**:
- Enable bot capability
- Set bot name

#### Paso 4: Configurar Event Subscription

⚠️ **Primero:** Asegurate que `openclaw channels add` ya está ejecutado

En **Event Subscription**:
1. Choose: **Use long connection to receive events** (WebSocket)
2. Add event: `im.message.receive_v1`

#### Paso 5: Publicar app

1. Create version en **Version Management & Release**
2. Submit for review
3. Wait for admin approval (usualmente auto-aprobado)

### Configuración en OpenClaw

#### Opción A: Wizard (recomendado)

```bash
openclaw channels add
# Selecciona "Feishu"
# Pega App ID y App Secret
```

#### Opción B: Manual (config file)

Edita `~/.openclaw/openclaw.json`:

```json5
{
  channels: {
    feishu: {
      enabled: true,
      domain: "feishu",    // o "lark" para global
      dmPolicy: "pairing",
      groupPolicy: "open",
      blockStreaming: true,
      accounts: {
        main: {
          appId: "cli_xxx",
          appSecret: "xxx",
          botName: "My AI assistant"
        }
      }
    }
  }
}
```

#### Opción C: Environment variables

```bash
export FEISHU_APP_ID="cli_xxx"
export FEISHU_APP_SECRET="xxx"
```

### Políticas de acceso

#### DM Policy (Direct Messages)

```json5
"dmPolicy": "pairing"     // Default: unknown users get pairing code
"dmPolicy": "allowlist"   // Only users in allowFrom
"dmPolicy": "open"        // Allow all (requiere "*" en allowFrom)
"dmPolicy": "disabled"    // Disable DMs
```

**Ejemplo: Allowlist custom**
```json5
{
  channels: {
    feishu: {
      dmPolicy: "allowlist",
      allowFrom: ["ou_user_123", "ou_user_456"]
    }
  }
}
```

#### Group Policy (Grupo Chats)

```json5
"groupPolicy": "open"        // Allow todos en grupos (default)
"groupPolicy": "allowlist"   // Only users in groupAllowFrom
"groupPolicy": "disabled"    // Disable group messages
```

**Ejemplo: Allowlist de grupos específicos**
```json5
{
  channels: {
    feishu: {
      groupPolicy: "allowlist",
      groupAllowFrom: ["ou_dept_eng", "ou_dept_product"],
      groups: {
        "oc_group_123": { requireMention: false }
      }
    }
  }
}
```

### Cómo obtener IDs

#### Group IDs (chat_id)

Formato: `oc_xxx`

**Método 1 (recomendado):**
1. Start gateway
2. @mention bot en el grupo
3. Run `openclaw logs --follow`
4. Busca `chat_id` en los logs

**Método 2:**
Usa Feishu API debugger para listar grupos

#### User IDs (open_id)

Formato: `ou_xxx`

**Método 1:**
1. Start gateway
2. DM el bot
3. Run `openclaw logs --follow`
4. Busca `open_id`

**Método 2:**
Checkea pairing requests: `openclaw pairing list feishu`

### Tipos de mensaje soportados

**Recibir:**
- ✅ Text
- ✅ Images
- ✅ Files
- ✅ Audio
- ✅ Video
- ✅ Stickers

**Enviar:**
- ✅ Text
- ✅ Images
- ✅ Files
- ✅ Audio
- ⚠️ Rich text (soporte parcial)

### Limitaciones conocidas

- Feishu no soporta edición de mensajes → `blockStreaming: true` (espera respuesta completa)
- Máximo 2000 caracteres por chunk (`textChunkLimit`)
- Máximo 30MB para media (`mediaMaxMb`)

### Caso de uso real: Setup para equipo de ingeniería

```json5
{
  channels: {
    feishu: {
      enabled: true,
      domain: "feishu",
      dmPolicy: "pairing",
      groupPolicy: "allowlist",
      
      groupAllowFrom: ["ou_dept_engineering"],
      
      accounts: {
        main: {
          appId: "cli_engineeringbot",
          appSecret: "${FEISHU_SECRET}",
          botName: "🤖 Engineering AI"
        }
      },
      
      groups: {
        "oc_eng_general": {
          requireMention: true,     // Requiere @mention
          enabled: true
        },
        "oc_ai_research": {
          requireMention: false,    // Responde sin @mention
          enabled: true
        },
        "oc_internal_admin": {
          requireMention: true,
          enabled: false             // Disabled
        }
      }
    }
  }
}
```

---

## 4. QMD Memory Backend 🧠

### ¿Qué es?

**QMD** es un backend experimental de búsqueda de memoria que reemplaza el indexador SQLite integrado de OpenClaw. Es un **sidecar local-first** que combina **BM25 (keyword) + vectores + reranking**.

**Introducido en:** OpenClaw 2026.2.2  
**Status:** Experimental, opt-in  
**Binario:** `qmd` CLI  
**Repositorio:** https://github.com/tobi/qmd

### Cómo difiere de SQLite nativo

| Aspecto | SQLite (default) | QMD |
|--------|---|---|
| **Búsqueda** | Vector + FTS5 BM25 | Vector + BM25 + Reranking |
| **Velocidad** | Rápido | Más rápido (C + Bun) |
| **Modelos** | Local llama-cpp o remote | Auto-descarga GGUF |
| **Presición** | Buena | Excelente (reranking) |
| **Datos** | In-memory search | SQLite + índices |
| **Extensibilidad** | Limitado | MCP mode |
| **Fallback** | N/A | SQLite automático si falla |

### Prerequisitos

```bash
# 1. Bun (JavaScript runtime)
curl -fsSL https://bun.sh/install | bash

# 2. QMD CLI
bun install -g github.com/tobi/qmd
# O descargar release: https://github.com/tobi/qmd/releases

# 3. SQLite con extensiones
brew install sqlite           # macOS
sudo apt install sqlite3      # Linux
```

### Configuración

**Habilitar QMD en config:**

```json5
{
  agents: {
    defaults: {
      memory: {
        backend: "qmd",       // Switch del SQLite al QMD
        citations: "auto",    // Show source files
        
        qmd: {
          command: "qmd",                    // Path del binario
          includeDefaultMemory: true,        // Auto-index MEMORY.md + memory/
          update: {
            interval: "5m",                  // Refrescar cada 5 minutos
            debounceMs: 15000,               // Debounce cambios de archivos
            onBoot: true                     // Actualizar al iniciar
          },
          limits: {
            maxResults: 6,                   // Máximo 6 resultados
            maxSnippetChars: 800,            // Máximo 800 chars por snippet
            maxInjectedChars: 4000,          // Total chars inyectados al prompt
            timeoutMs: 4000                  // Timeout de búsqueda
          },
          paths: [
            { name: "docs", path: "~/notes", pattern: "**/*.md" },
            { name: "team-wiki", path: "/srv/shared-docs" }
          ]
        }
      }
    }
  }
}
```

### Ubicación del estado de QMD

```
~/.openclaw/
├── agents/
│   └── main/
│       └── qmd/
│           ├── xdg-config/        # Configuración
│           ├── xdg-cache/         # Cache (modelos GGUF)
│           └── index.yml          # Definición de colecciones
```

OpenClaw **automáticamente** genera `index.yml` desde `memory.qmd.paths`.

### Flujo de búsqueda con QMD

```
Agent pregunta via memory_search("How to deploy on Kubernetes")
    ↓
OpenClaw envía a QMD: qmd query "How to deploy on Kubernetes" --json
    ↓
QMD ejecuta:
  1. BM25 search (keywords "deploy", "kubernetes")
  2. Vector search (significado semántico)
  3. Reranking (mejora results)
    ↓
QMD retorna JSON con snippets + paths + scores
    ↓
OpenClaw inyecta al context del agente
    ↓
Agent responde con conocimiento indexado
```

### Tools disponibles

#### `memory_search` 
Busca semánticamente en memoria (Markdown)

```python
# Parámetros
query: str              # Required
limit: int             # Default: 6 (maxResults)
minScore: float        # Default: 0.0

# Retorna
{
  "results": [
    {
      "text": "snippet...",
      "path": "MEMORY.md",
      "lineStart": 42,
      "lineEnd": 48,
      "score": 0.87,
      "source": "qmd/memory-root/MEMORY.md#L42-L48"
    }
  ],
  "backend": "qmd",
  "timeTakenMs": 234
}
```

#### `memory_get`
Lee archivo específico de memoria

```python
# Parámetros
path: str              # workspace-relative (ej: "MEMORY.md")
offset: int            # Starting line (1-indexed)
limit: int             # Number of lines
```

### Caso de uso real: Indexar múltiples fuentes

```json5
{
  agents: {
    defaults: {
      memory: {
        backend: "qmd",
        
        qmd: {
          includeDefaultMemory: true,  // Auto-indexa MEMORY.md + memory/
          
          paths: [
            {
              name: "project-docs",
              path: "~/projects/myapp/docs",
              pattern: "**/*.md"
            },
            {
              name: "architecture",
              path: "~/architecture-decisions",
              pattern: "*.md"
            },
            {
              name: "api-reference",
              path: "/srv/api-docs/generated.md"
            }
          ],
          
          limits: {
            maxResults: 8,
            maxSnippetChars: 1000,
            timeoutMs: 5000
          }
        }
      }
    }
  }
}
```

### Modelos que QMD descarga automáticamente

**Query expansion model:**
```
hf:ggml-org/gpt2-medium-GGUF/gpt2-medium.gguf (~350MB)
```

**Reranker model:**
```
hf:intfloat/jina-colbert-v2-bilingual-GGUF/jina-colbert-v2-bilingual-q8_0.gguf (~600MB)
```

Descarga **automática** en primera búsqueda (lento la primera vez, después cachéado).

### Fallback automático

Si QMD falla o se cuelga:
- ✅ OpenClaw vuelve a **SQLite automáticamente**
- ✅ No hay ruptura de memoria_search
- ✅ Log warning: `"qmd search failed, falling back to builtin"`

### Búsqueda híbrida (BM25 + Vectores)

QMD combina automáticamente:
- **BM25:** Perfecto para tokens exactos (IDs, code symbols, errores)
- **Vector:** Perfecto para significado semántico ("same as...", paráfrasis)

**Ejemplo:**
```
Query: "firebase auth tokens"

BM25 match: "firebase", "auth", "tokens" (exacto)
Vector match: "authentication mechanisms", "JWT handling" (semántico)

QMD fusion: Ambos scores + reranking
Result: Top matches contienen tanto info de firebase como auth general
```

### Performance

| Operación | Tiempo típico |
|---|---|
| Primera búsqueda | 2-3s (descarga modelos) |
| Búsquedas siguientes | 200-400ms |
| Reindex 100 docs | 5-10s |
| Fallback a SQLite | <50ms |

### Sesiones (Experimental)

Opcionalmente indexa transcripts de sesiones:

```json5
{
  agents: {
    defaults: {
      memory: {
        backend: "qmd",
        qmd: {
          sessions: {
            enabled: true,
            retentionDays: 30,
            exportDir: "~/.openclaw/agents/main/qmd/sessions/"
          }
        }
      }
    }
  }
}
```

---

## 5. Embedding Providers (OpenAI, Gemini, Local)

### ¿Qué es?

Los **Embedding Providers** son servicios que convierten texto a vectores numéricos para búsqueda semántica en memoria y otros contextos.

**Status:** Built-in (no es nuevo en 2026, pero importante contexto)

### Proveedores disponibles

#### 1. **OpenAI** (Recomendado)

```json5
{
  agents: {
    defaults: {
      memorySearch: {
        provider: "openai",
        model: "text-embedding-3-small",
        fallback: "openai",
        
        remote: {
          baseUrl: "https://api.openai.com/v1",
          apiKey: "sk-...",
          batch: {
            enabled: true,
            concurrency: 2
          }
        }
      }
    }
  }
}
```

**Velocidad:** ⚡⚡⚡ Batch API muy rápido  
**Costo:** Barato (~$0.02 per 1M tokens)  
**Precisión:** ⭐⭐⭐

#### 2. **Gemini** (Google)

```json5
{
  agents: {
    defaults: {
      memorySearch: {
        provider: "gemini",
        model: "gemini-embedding-001",
        
        remote: {
          apiKey: "AIzaSy...",
          baseUrl: "https://generativelanguage.googleapis.com/v1beta/models"
        }
      }
    }
  }
}
```

**Velocidad:** ⚡⚡ Requiere polling  
**Costo:** Gratis (Google API)  
**Precisión:** ⭐⭐⭐

#### 3. **Local** (Offline)

```json5
{
  agents: {
    defaults: {
      memorySearch: {
        provider: "local",
        
        local: {
          modelPath: "hf:ggml-org/embeddinggemma-300M-GGUF/embeddinggemma-300M-Q8_0.gguf",
          modelCacheDir: "~/.cache/llamacpp"
        }
      }
    }
  }
}
```

**Ventajas:** ✅ Completamente offline, ✅ Sin API keys  
**Desventajas:** ⚠️ Lento (primera descarga ~600MB)  
**Precisión:** ⭐⭐

### ¿Voyage AI es soportado?

**Respuesta:** No encontré soporte explícito para **Voyage AI** embeddings en OpenClaw 2026.

Los proveedores principales soportados son:
- OpenAI (text-embedding-3-small/large)
- Gemini (gemini-embedding-001)
- Local (llama-cpp)

**Posibilidad futura:** Voyage AI es un provider de embeddings de alta calidad, pero requeriría que OpenClaw agregue soporte explícito (no está en el roadmap visible).

---

## 6. Healthcheck Skill ✅

### ¿Qué es?

**Healthcheck** es un skill para auditar y endurecimiento de seguridad del host que ejecuta OpenClaw. Evalúa postura de seguridad y aligns con tolerancia de riesgo del usuario.

**Introducido en:** OpenClaw 2026.2.2  
**Status:** ✓ Ready  
**Propósito:** Security audit, hardening, risk assessment

### ¿Qué audita?

#### Nivel 1: Sistema Operativo

```
✓ OS type + version
✓ Privilege level (root vs user)
✓ Disk encryption status (FileVault/LUKS/BitLocker)
✓ Automatic security updates
✓ Firewall status
✓ Listening ports/services
```

#### Nivel 2: OpenClaw Security

```
✓ openclaw security audit (built-in)
✓ File permissions (gateway creds, tokens)
✓ Gateway bind address (localhost vs exposed)
✓ OpenClaw version + update status
✓ Browser control (2FA check)
✓ Cron jobs registrados
```

#### Nivel 3: Backup + Recovery

```
✓ Backup system status (Time Machine, snapshots)
✓ Backup recency (current o stale?)
✓ System restore readiness
```

### Cómo invocarlo

#### Opción A: Interactivo en chat

```
User: "Run a security check"
User: "Do a security audit"
User: "Help me harden my machine"

OpenClaw: Inicia healthcheck skill
```

#### Opción B: CLI directo

```bash
# Recomendado: Usa el agente con modelo SOTA
openclaw agent --agent main --model anthropic/claude-opus-4-5 \
  --prompt "Run healthcheck and harden my VPS"
```

#### Opción C: Cron scheduling

```bash
# Auditoría semanal automática
openclaw cron add \
  --name "healthcheck:security-audit" \
  --schedule "0 3 * * 0" \
  --command "openclaw agent --prompt 'Run security audit'"
```

### Flujo de ejecución

```
1. Model self-check
   └─ ¿Modelo es SOTA? (Opus 4.5+, GPT 5.2+)
   └─ Recomienda upgrade si es necesario

2. Establish context (read-only)
   └─ Detecta OS, privilege, acceso, red, backups
   └─ Solicita permission once para checks read-only

3. OpenClaw security audit
   └─ openclaw security audit --deep
   └─ openclaw security audit --fix (optional)

4. Version check
   └─ openclaw update status

5. Determine risk tolerance
   └─ Home/Workstation Balanced (default)
   └─ VPS Hardened
   └─ Developer Convenience
   └─ Custom

6. Produce remediation plan
   └─ Muestra plan before any changes

7. Execute with confirmations
   └─ Each step requiere approval explicit
   └─ Puede rollback

8. Verify + report
   └─ Re-checa firewall, ports, access, version
```

### Perfiles de riesgo disponibles

#### 1. **Home/Workstation Balanced** (Más común)

```
✅ Firewall: ON con defaults razonables
✅ Remote access: LAN-only o Tailscale
✅ SSH: Key-only, root disabled (recomendado)
✅ Updates: Auto (recomendado)
✅ Encryption: FileVault/LUKS (fuerte)
```

**Caso de uso:** Laptop personal, desarrollo local

#### 2. **VPS Hardened** (Producción)

```
✅ Firewall: Deny-by-default (inbound)
✅ Open ports: SSH (22) + gateway (custom)
✅ SSH: Key-only, no root login, rate limit
✅ Updates: Automatic + reboot
✅ Encryption: LUKS mandatory
✅ Fail2ban + monitoring
```

**Caso de uso:** Servidor remoto exposible a internet

#### 3. **Developer Convenience**

```
✅ Firewall: ON pero permisivo
✅ Services: Local dev tools allowed
✅ Exposure warnings explícitos
✅ Still audited
```

**Caso de uso:** Dev environment con múltiples servicios

#### 4. **Custom**

Define tus propios requisitos (puertos, servicios, politicas)

### Confirmaciones requeridas

El skill solicita aprobación explícita para:

- 🔧 Cambios de firewall
- 🔑 Config SSH/RDP
- 📦 Install/remove paquetes
- ⚙️ Enable/disable servicios
- 👤 Cambios de user/group
- ⏰ Schedule tasks
- 🔐 Update policies

### Caso de uso real: Hardening de VPS producción

```bash
# 1. Inicia audit
openclaw agent --model anthropic/claude-opus-4-5 \
  --prompt "Run healthcheck and harden this VPS for production"

# Skill output:
# - OS: Ubuntu 22.04 LTS (OK)
# - Privilege: ubuntu (good)
# - Access: SSH + Tailscale (good)
# - Firewall: ufw inactive (⚠️ needs enable)
# - SSH: PasswordAuth enabled (⚠️ critical)
# - Backups: snapshots enabled (good)

# 2. Presenta plan:
# Step 1: Enable ufw + allow 22,443,custom_port
# Step 2: Disable SSH password auth
# Step 3: Disable root login
# Step 4: Schedule weekly security audit

# 3. User aprueba paso a paso

# 4. Skill ejecuta + verifica
# Final report: ✅ VPS Hardened profile achieved
```

### Output y auditoría

**Logs guardados en:**
```
~/.openclaw/agents/main/logs/healthcheck/
├── YYYY-MM-DD-HH-MM-audit.json
└── YYYY-MM-DD-HH-MM-remediation.log
```

**Memory capture (opcional):**
```
Puede guardar resumen a memory/YYYY-MM-DD.md
(redacted de secrets, hostnames, IPs)
```

### Scheduling periódico

```bash
# Daily audit (3 AM)
openclaw cron add \
  --name "healthcheck:security-audit-daily" \
  --schedule "0 3 * * *" \
  --command "openclaw agent --prompt 'Quick security audit'"

# Weekly version check (Sundays 9 AM)
openclaw cron add \
  --name "healthcheck:version-check-weekly" \
  --schedule "0 9 * * 0" \
  --command "openclaw update status"
```

---

## Comparativa resumida de los 6 skills

| Skill | Propósito | Nuevo en 2026 | Status | Complejidad |
|---|---|---|---|---|
| **Web-search-plus** | Multi-provider web search + auto-routing | Parcial (web-search-plus es custom) | ✓ Ready | Media |
| **Device Pairing** | Emparejar iOS/Android remoto | Sí | ✓ Ready | Media |
| **Feishu/Lark** | Conectar a team chat Feishu | ✓ 2026.2.2 | ✓ Ready | Baja |
| **QMD Memory** | BM25 + vectors + reranking para memoria | ✓ 2026.2.2 | Experimental | Alta |
| **Embeddings** | Vectorización (OpenAI/Gemini/Local) | No (built-in) | ✓ Ready | Baja |
| **Healthcheck** | Security audit + hardening | ✓ 2026.2.2 | ✓ Ready | Media |

---

## Conclusión

**OpenClaw 2026** trajo **3 skills principales nuevos:**
1. ✅ **Feishu/Lark Plugin** - Integración con team chat asiático
2. ✅ **QMD Memory Backend** - Búsqueda avanzada con reranking
3. ✅ **Healthcheck Skill** - Auditoría de seguridad

**Mejoras a skills existentes:**
- 🔍 **Web-search-plus**: Auto-routing inteligente entre 5 proveedores
- 📱 **Device Pairing**: CLI maturo con token rotation
- 🧠 **Embeddings**: Soporte para OpenAI batch, Gemini, local

**Técnicamente destacable:**
- QMD es el "game-changer" para búsqueda semántica avanzada
- Feishu abre OpenClaw a mercado asiático
- Web-search-plus elimina "paralysis of choice" en búsquedas

---

**Documento generado:** 2026-02-14 20:52 UTC  
**Fuentes:** OpenClaw 2026.2.3-1, docs oficiales, skills instalados

