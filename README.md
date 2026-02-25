# Riskitera Blog

Blog corporativo de ciberseguridad en [blog.riskitera.com](https://blog.riskitera.com).

Hugo + Tailwind CSS + Fuse.js | Bilingue ES/EN

## Requisitos

- [Hugo](https://gohugo.io/installation/) >= 0.152 (extended)
- Node.js >= 18
- npm

## Desarrollo local

```bash
# 1. Clonar el repositorio
git clone https://github.com/riskitera/blog.git
cd blog

# 2. Instalar dependencias (Tailwind CSS)
make install

# 3. Arrancar servidor de desarrollo (con drafts y live reload)
make dev
```

El blog estara disponible en `http://localhost:1313/`.

### Otros comandos utiles

```bash
make serve          # Servidor sin drafts (simula produccion)
make build          # Build de produccion (minificado)
make clean          # Limpiar archivos generados
make lint           # Validar HTML y enlaces internos
```

### Crear contenido

```bash
# Nuevo post
make new-post SLUG=mi-post LANG=es

# Nuevo case study
make new-case SLUG=empresa LANG=es
```

Editar el fichero generado en `content/<lang>/posts/<slug>/index.md` y cambiar `draft: false` cuando este listo.

## Despliegue en Cloudflare Pages

### Configuracion inicial

1. Ir a [Cloudflare Dashboard](https://dash.cloudflare.com/) > **Workers & Pages** > **Create application** > **Pages**

2. Conectar el repositorio GitHub `riskitera/blog`

3. Configurar el build:

   | Campo | Valor |
   |-------|-------|
   | **Production branch** | `main` |
   | **Build command** | `npm run build:css && hugo --minify --gc` |
   | **Build output directory** | `public` |

4. Anadir variables de entorno:

   | Variable | Valor |
   |----------|-------|
   | `HUGO_VERSION` | `0.152.2` |
   | `NODE_VERSION` | `18` |

5. Pulsar **Save and Deploy**

### Dominio personalizado

1. En el proyecto de Pages, ir a **Custom domains**
2. Anadir `blog.riskitera.com`
3. Cloudflare configurara automaticamente el registro DNS CNAME

### Despliegue automatico

Cada push a `main` dispara un build y deploy automatico en Cloudflare Pages. No se necesita configuracion adicional.

### Preview deployments

Cloudflare Pages genera automaticamente un preview URL para cada pull request, permitiendo revisar cambios antes de mergear a `main`.

## Estructura del proyecto

```
blog/
├── hugo.toml                # Config Hugo multi-idioma
├── content/
│   ├── es/                  # Contenido en espanol (idioma principal)
│   │   ├── posts/           # Entradas del blog
│   │   ├── pages/           # Paginas estaticas
│   │   └── case-studies/    # Casos de exito
│   └── en/                  # Contenido en ingles
├── i18n/                    # Traducciones UI (es.toml, en.toml)
├── archetypes/              # Plantillas para nuevo contenido
├── themes/riskitera/        # Tema custom
│   ├── layouts/             # Templates Hugo
│   ├── assets/css/          # Tailwind (input.css -> output.css)
│   ├── static/js/           # JavaScript (search, menu)
│   └── static/images/       # Logo, favicon, OG
├── Makefile                 # Comandos de desarrollo
└── package.json             # Dependencias npm (Tailwind)
```
