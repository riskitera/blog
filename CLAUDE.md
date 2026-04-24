# Riskitera Blog

Blog corporativo de ciberseguridad en blog.riskitera.com

## Tech Stack

- Hugo 0.152+ (static site generator)
- Tailwind CSS 3.4 + @tailwindcss/typography
- Fuse.js 7 (client-side search)
- Deploy: Cloudflare Pages

## Comandos

```bash
make help        # Ver todos los comandos
make install     # Instalar dependencias npm
make dev         # Servidor de desarrollo con live reload
make build       # Build produccion (minified)
make new-post SLUG=mi-post LANG=es   # Nuevo post
make new-case SLUG=empresa LANG=es   # Nuevo case study
make clean       # Limpiar archivos generados
make deploy      # Build + instrucciones deploy
```

## Estructura

```
blog/
├── hugo.toml          # Config Hugo multi-idioma
├── content/
│   ├── es/            # Contenido español (idioma principal)
│   │   ├── posts/     # Entradas del blog
│   │   ├── pages/     # Paginas estaticas
│   │   └── case-studies/
│   └── en/            # Contenido ingles
├── i18n/              # Traducciones UI (es.toml, en.toml)
├── archetypes/        # Plantillas maestras (posts, case-studies)
└── themes/riskitera/  # Tema custom
    ├── layouts/       # Templates Hugo
    ├── assets/css/    # Tailwind (input.css → output.css)
    ├── static/js/     # JavaScript (search, menu)
    └── static/images/ # Logo, favicon, OG
```

## Multi-idioma

- Idioma principal: ES (`defaultContentLanguage = "es"`)
- Segundo idioma: EN
- Vincular traducciones: usar mismo `translationKey` en front matter
- URLs: `/:lang/posts/:year/:month/:slug/`

## Workflow para nuevo contenido

1. `make new-post SLUG=mi-slug LANG=es`
2. Editar content/es/posts/mi-slug/index.md
3. Crear version EN con mismo `translationKey`
4. Cambiar `draft: false` cuando listo
5. `make dev` para preview

## Skills disponibles

- blog-branding: Paleta de colores, tipografia, estilos del tema
- blog-content: Tematicas del blog, estructura de front matter, SEO

## Commits

- Formato: `<type>(blog): <subject>`
- Autor: Dani (cr0hn@cr0hn.com)

<!-- wiki-brain:start -->
## Wiki Knowledge Base (segundo cerebro de David)

Path: /Users/pedri77/Documents/Claude_proyectos/Claude/claude-obsidian

Cuando necesites contexto que no está en este proyecto:
1. Lee `wiki/hot.md` (contexto reciente, ~500 palabras)
2. Si no basta, lee `wiki/index.md` (catálogo maestro)
3. Para dominios, lee `wiki/entities/_index.md`, `wiki/concepts/_index.md` o `wiki/sources/_index.md`
4. Solo después drillea páginas individuales

Entry points clave:
- Perfil del owner: `wiki/entities/David Moya.md`
- Portfolio de proyectos: `wiki/entities/Portfolio Riskitera.md`
- Jerga y acrónimos: `wiki/meta/glossary.md`
- Protocolo de lectura: `wiki/_brain/cowork-protocol.md`

NO leas el wiki para preguntas genéricas de código o tareas ajenas al dominio de este proyecto.

## Reglas de estilo (aplicar en todos los proyectos)

- Español por defecto. Inglés solo para código y términos técnicos.
- Respuestas cortas, sin preámbulo ni resumen redundante.
- Sin em dashes ni `--` como puntuación. Usar puntos, comas, dos puntos, paréntesis.
- Tool calls en paralelo cuando sean independientes.
- Challengear ideas, no asentir por asentir.
<!-- wiki-brain:end -->
