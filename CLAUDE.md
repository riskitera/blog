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
