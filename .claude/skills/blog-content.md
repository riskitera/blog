---
name: blog-content
description: Guia de contenido del blog Riskitera. Usar cuando se cree nuevo contenido, posts o case studies.
---

# Riskitera Blog Content Guide

## Tematicas del Blog

El blog cubre estas areas de ciberseguridad:

1. **GRC (Governance, Risk & Compliance)** -- ISO 27001, ENS, NIS2, SOC 2, GDPR, NIST CSF
2. **SOC (Security Operations Center)** -- Alertas, incidentes, respuesta automatizada, SIEM
3. **Threat Modeling** -- STRIDE, DFD, analisis de superficies de ataque
4. **Code Security** -- SAST, DAST, SCA, seguridad en CI/CD
5. **Workforce Orchestration** -- Automatizacion con IA, flujos de trabajo de seguridad

## Front Matter de Posts

```yaml
---
title: "Titulo descriptivo del articulo"
description: "Descripcion SEO de 150-160 caracteres max"
slug: "url-friendly-slug"
date: 2026-02-23
lastmod: 2026-02-23
draft: true
tags: ["GRC", "ISO 27001"]
categories: ["GRC"]
image: "featured.png"
author: "Riskitera Team"
translationKey: "unique-key-for-translations"
---
```

### Campos obligatorios
- title, description, slug, date, tags, translationKey

### Campos opcionales
- image (featured image en el directorio del post)
- lastmod (fecha ultima modificacion)
- categories
- author (default: "Riskitera Team")

## Front Matter de Case Studies

```yaml
---
title: "Nombre de la empresa - Titulo del caso"
description: "Descripcion SEO"
slug: "nombre-empresa"
date: 2026-02-23
draft: true
company: "Nombre de la Empresa"
industry: "Fintech"
logo: "logo.png"
translationKey: "empresa-case"
tags: ["GRC", "ISO 27001"]
---
```

## Tags Recomendados

GRC, SOC, Threat Modeling, Code Security, ISO 27001, ENS, NIS2, GDPR, SOC 2, NIST CSF, SAST, DAST, STRIDE, Automatizacion, IA, Compliance, Vulnerabilidades, Incidentes

## SEO Checklist para Posts

- [ ] Title < 60 caracteres
- [ ] Description entre 120-160 caracteres
- [ ] Slug descriptivo y corto (3-5 palabras max)
- [ ] Al menos 2 tags relevantes
- [ ] Featured image 1200x630px (para OG)
- [ ] translationKey unico y consistente entre idiomas
- [ ] H2 y H3 descriptivos para TOC
- [ ] <!--more--> despues del primer parrafo (para excerpt)

## Workflow Multi-idioma

1. Crear post en ES primero (`make new-post SLUG=mi-post LANG=es`)
2. Crear version EN con mismo translationKey (`make new-post SLUG=my-post LANG=en`)
3. Asegurar que ambos tienen el mismo translationKey
4. Adaptar (no traducir literalmente) el contenido
