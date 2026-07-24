---
title: "Reglamento DORA: guia practica para entidades financieras"
image: "cover.png"
description: "Guia completa del Reglamento DORA (Digital Operational Resilience Act): a quien aplica, requisitos tecnicos, plazos, TLPT y como preparar tu entidad financiera para el cumplimiento."
slug: "reglamento-dora-guia-practica"
date: 2026-07-24
publishDate: 2026-07-24
lastmod: 2026-07-24
draft: false
tags: ["DORA", "Compliance", "Sector Financiero", "Resiliencia Digital"]
categories: ["Compliance"]
author: "David Moya"
keyword: "reglamento dora"
funnel: "mofu"
---

Guia completa del Reglamento DORA: que es, a quien aplica, requisitos tecnicos, plazos y como preparar tu entidad financiera para cumplir con la resiliencia operativa digital.

<!--more-->

> **TL;DR:** DORA (Reglamento UE 2022/2554) obliga a bancos, aseguradoras, gestoras de fondos y proveedores TIC criticos a garantizar resiliencia operativa digital. Aplica desde enero 2025. Exige gestion de riesgos TIC, notificacion de incidentes en 4 horas, pruebas de resiliencia (incluyendo TLPT) y supervision de proveedores terceros. Las sanciones pueden alcanzar el 1% de la facturacion diaria.

## Que es DORA

El **Reglamento DORA** (Digital Operational Resilience Act, Reglamento UE 2022/2554) es la normativa europea que establece requisitos uniformes de resiliencia operativa digital para el sector financiero. Entro en vigor en enero de 2023 y es de **aplicacion obligatoria desde el 17 de enero de 2025**.

A diferencia de una directiva (que cada pais transpone), DORA es un reglamento: se aplica directamente en todos los Estados miembros sin necesidad de transposicion nacional. En Espana, esto significa que las entidades financieras deben cumplirlo sin esperar a una ley española especifica.

### Por que existe DORA

El sector financiero depende completamente de la tecnologia. Un fallo en los sistemas de un banco, una brecha en una aseguradora o un ataque a un proveedor cloud puede tener impacto sistemico. DORA nace tras incidentes como:

- El ataque a SWIFT (robo de 81 millones de dolares al Banco Central de Bangladesh)
- Los ataques DDoS coordinados contra bancos europeos
- La caida de proveedores cloud que afecto a multiples entidades simultaneamente
- El aumento de ransomware dirigido al sector financiero (Travelex, CNA Financial)

Antes de DORA, cada pais tenia requisitos diferentes y las directrices de la EBA/EIOPA/ESMA eran insuficientes. DORA unifica y eleva el nivel de exigencia.

## A quien aplica DORA

DORA aplica a **21 tipos de entidades financieras**, entre ellas:

- Entidades de credito (bancos)
- Empresas de inversion
- Entidades de pago y de dinero electronico
- Empresas de seguros y reaseguros
- Fondos de pensiones
- Gestoras de fondos de inversion (UCITS, AIFM)
- Proveedores de servicios de criptoactivos
- Agencias de calificacion crediticia
- Centrales de datos (trade repositories)

Y de forma critica: **proveedores terceros de servicios TIC** que sean designados como criticos por las autoridades europeas de supervision (ESAs). Esto incluye proveedores cloud (AWS, Azure, GCP), proveedores de software core bancario y empresas de ciberseguridad que presten servicios criticos.

### Proporcionalidad

DORA aplica el principio de proporcionalidad: las microempresas y entidades pequenas tienen requisitos simplificados. Pero incluso las entidades mas pequenas deben cumplir los requisitos basicos de gestion de riesgos TIC y notificacion de incidentes.

## Los 5 pilares de DORA

### Pilar 1: Gestion de riesgos TIC (Arts. 5-16)

La entidad debe establecer un **marco de gestion de riesgos TIC** que incluya:

- Estrategia de resiliencia digital aprobada por el organo de direccion
- Inventario completo de activos TIC y dependencias
- Politicas de seguridad, control de accesos, cifrado y gestion de claves
- Deteccion de actividades anomalas y amenazas
- Planes de continuidad de negocio y recuperacion ante desastres
- Programas de formacion y concienciacion

**Requisito clave:** El organo de direccion (consejo de administracion) es directamente responsable de la gestion de riesgos TIC. No vale delegar y olvidar.

### Pilar 2: Notificacion de incidentes (Arts. 17-23)

Las entidades deben clasificar los incidentes TIC segun criterios armonizados y notificar los **incidentes graves** a la autoridad competente:

| Fase | Plazo | Contenido |
|------|-------|-----------|
| Notificacion inicial | 4 horas desde clasificacion | Naturaleza del incidente, impacto inicial |
| Informe intermedio | 72 horas | Actualizacion del impacto, medidas adoptadas |
| Informe final | 1 mes | Analisis de causa raiz, lecciones aprendidas |

Un incidente se clasifica como grave si cumple criterios de: clientes afectados, duracion, extension geografica, impacto en datos, criticidad de servicios o perdida economica.

### Pilar 3: Pruebas de resiliencia (Arts. 24-27)

Dos niveles de pruebas:

**Pruebas basicas (todas las entidades):**
- Tests de vulnerabilidades
- Analisis de codigo fuente abierto
- Evaluaciones de seguridad de red
- Analisis de gaps
- Pruebas de continuidad de negocio

**TLPT (Threat-Led Penetration Testing) para entidades significativas:**
- Pruebas de penetracion avanzadas basadas en inteligencia de amenazas
- Ejecutadas por equipos de red team externos
- Siguiendo el framework TIBER-EU
- Frecuencia: al menos cada 3 anos
- Supervisadas por la autoridad competente

### Pilar 4: Gestion de riesgos de terceros TIC (Arts. 28-44)

DORA introduce requisitos estrictos para la gestion de proveedores TIC:

- Registro completo de todos los acuerdos contractuales con proveedores TIC
- Evaluacion de riesgos antes de contratar
- Clausulas contractuales obligatorias (SLA, auditorias, planes de salida, localizacion de datos)
- Estrategia de concentracion: no depender excesivamente de un solo proveedor
- Planes de salida para migrar servicios criticos

**Proveedores TIC criticos** designados por las ESAs estaran sujetos a supervision directa europea a traves de un "Lead Overseer" (supervisor principal).

### Pilar 5: Comparticion de informacion (Art. 45)

DORA promueve el intercambio voluntario de informacion sobre amenazas entre entidades financieras, dentro de comunidades de confianza y respetando la proteccion de datos.

## Timeline y plazos

| Fecha | Hito |
|-------|------|
| Nov 2022 | Publicacion DORA en DOUE |
| Ene 2023 | Entrada en vigor |
| Ene 2024 | Publicacion RTS/ITS (estandares tecnicos) |
| **Ene 2025** | **Aplicacion obligatoria** |
| 2025 | Designacion de proveedores TIC criticos |
| 2025-2026 | Primeras inspecciones y auditorias |
| 2026+ | Primeros TLPT obligatorios |

## Como prepararse: checklist practico

### Fase 1: Evaluacion (3 meses)

- [ ] Gap analysis contra los 5 pilares de DORA
- [ ] Inventario de activos TIC y dependencias criticas
- [ ] Mapeo de proveedores TIC y evaluacion de concentracion
- [ ] Evaluacion de la madurez actual del marco de riesgos TIC

### Fase 2: Diseño (3 meses)

- [ ] Actualizar el marco de gestion de riesgos TIC
- [ ] Definir politica de clasificacion y notificacion de incidentes
- [ ] Diseñar programa de pruebas de resiliencia
- [ ] Revisar contratos con proveedores TIC (clausulas DORA)
- [ ] Definir plan de formacion para el organo de direccion

### Fase 3: Implementacion (6-12 meses)

- [ ] Desplegar capacidades de deteccion y respuesta (SOC, EDR, SIEM)
- [ ] Implementar proceso de notificacion de incidentes (4h/72h/1m)
- [ ] Ejecutar primera ronda de pruebas de resiliencia
- [ ] Actualizar contratos con proveedores criticos
- [ ] Registrar acuerdos TIC en el registro obligatorio
- [ ] Formar al consejo de administracion

### Fase 4: Mejora continua

- [ ] Programar pruebas TLPT (si aplica) cada 3 anos
- [ ] Revisar y actualizar el marco de riesgos TIC anualmente
- [ ] Participar en ejercicios sectoriales de ciberresiliencia
- [ ] Actualizar el registro de proveedores TIC

## DORA vs ENS vs NIS2

| Aspecto | DORA | ENS | NIS2 |
|---------|------|-----|------|
| Sector | Financiero | Sector publico | Entidades esenciales e importantes |
| Tipo | Reglamento UE (directo) | Real Decreto (nacional) | Directiva UE (requiere transposicion) |
| Aplicacion | Ene 2025 | Mayo 2024 (actualizacion) | Oct 2024 (transposicion) |
| Notificacion | 4h + 72h + 1 mes | 72h al CCN-CERT | 24h + 72h + 1 mes |
| Pruebas | TLPT obligatorio (entidades significativas) | Auditorias bienales | Pruebas periodicas |
| Proveedores | Supervision directa de proveedores criticos | Extiende a proveedores del SP | Cadena de suministro |

Las entidades que ya cumplen ENS o ISO 27001 tienen parte del trabajo hecho, pero DORA añade requisitos especificos del sector financiero (TLPT, registro de proveedores TIC, notificacion en 4 horas) que van mas alla.

## Sanciones

DORA no establece sanciones especificas en el reglamento, sino que delega en los Estados miembros y las autoridades competentes nacionales. Sin embargo:

- Las autoridades pueden imponer **multas de hasta el 1% de la facturacion diaria** media global del ejercicio anterior, por cada dia de incumplimiento
- Para proveedores TIC criticos, el Lead Overseer puede imponer multas periodicas coercitivas
- Los Estados miembros pueden establecer sanciones penales adicionales

En Espana, el Banco de Espana, la CNMV y la DGSFP son las autoridades competentes segun el tipo de entidad.

## Como puede ayudar Riskitera

[Riskitera](https://riskitera.com) es una plataforma GRC con IA que facilita el cumplimiento de DORA:

- **Gap analysis automatizado** contra los 5 pilares de DORA
- **Gestion de riesgos TIC** con inventario de activos y proveedores
- **Workflow de incidentes** con los plazos de notificacion (4h/72h/1m)
- **Dashboard de compliance** para reporting al organo de direccion
- **SOC integrado** con capacidades de deteccion y respuesta

Solicita una demo en [riskitera.com](https://riskitera.com) o contacta en info@riskitera.com.
