---
name: blog-branding
description: Referencia de branding visual del blog Riskitera. Usar cuando se modifiquen estilos, layouts o componentes visuales.
---

# Riskitera Blog Branding

## Paleta de Colores (Tailwind custom: rk-*)

| Token CSS | Hex | Uso |
|-----------|-----|-----|
| bg-rk-bg | #0b1220 | Fondo principal del sitio |
| bg-rk-card | #111827 | Fondo de cards y secciones |
| bg-rk-card-hover | #1a2332 | Estado hover de cards |
| border-rk-border | #1e2d3d | Bordes sutiles |
| text-rk-text | #e6eaf2 | Texto principal (blanco suave) |
| text-rk-text-secondary | #8892a4 | Texto secundario (gris azulado) |
| text-rk-blue / bg-rk-blue | #3b82f6 | Acento primario: CTAs, links, logo |
| text-rk-violet / bg-rk-violet | #8b5cf6 | Gradientes, highlights especiales |
| text-rk-cyan / bg-rk-cyan | #06b6d4 | Acento secundario, hover links |

## Gradientes

- Hero text: `bg-gradient-to-r from-rk-blue to-rk-violet` (clase: .gradient-text)
- Backgrounds sutiles: `bg-gradient-to-b from-rk-bg to-rk-card`

## Componentes CSS predefinidos

- `.gradient-text` -- Texto con gradiente azul->violeta
- `.card` -- Card con fondo oscuro, borde sutil, hover
- `.btn-primary` -- Boton azul solido
- `.btn-outline` -- Boton con borde, transparente

## Tipografia

Font stack: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto

Para contenido de articulos usar `prose` classes de @tailwindcss/typography con override dark.

## Responsive Breakpoints

- sm: 640px (mobile landscape)
- md: 768px (tablet)
- lg: 1024px (desktop)
- xl: 1280px (wide desktop)

## Grid de Posts

- Mobile: 1 columna
- md: 2 columnas
- lg: 3 columnas

## Estilo General

- Dark theme enterprise, minimalista
- Bordes sutiles, no sombras pesadas
- Transiciones suaves (transition-colors)
- Header sticky con backdrop-blur
- Referencia visual: https://demo.riskitera.com/
