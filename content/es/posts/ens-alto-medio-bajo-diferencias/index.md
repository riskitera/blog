---
title: "ENS Alto vs Medio vs Bajo: diferencias, requisitos y como elegir categoría"
description: "Comparativa detallada de los tres niveles del Esquema Nacional de Seguridad (ENS): criterios de categorización, medidas obligatorias por nivel y como elegir la categoría correcta para tu organización."
slug: "ens-alto-medio-bajo-diferencias"
date: 2026-05-05
publishDate: 2026-05-05
lastmod: 2026-05-05
draft: false
tags: ["ENS", "Compliance", "Seguridad"]
categories: ["Compliance"]
author: "David Moya"
keyword: "ENS alto medio bajo"
funnel: "tofu"
---

El Esquema Nacional de Seguridad (ENS) clasifica los sistemas de información en tres niveles: bajo, medio y alto. Esta categorización determina las medidas de seguridad que cada organización debe implementar y el tipo de auditoría al que debe someterse. Según el CCN-CERT, más del 40% de las organizaciones públicas españolas categorizan incorrectamente sus sistemas, lo que genera problemas en la auditoría y en la protección real de la información. En esta guía detallamos las diferencias entre cada nivel, los criterios para elegir y los costes asociados.

<!--more-->

## Qué diferencias hay entre ENS Alto, Medio y Bajo?

Los tres niveles del ENS reflejan el impacto que un incidente de seguridad tendría sobre la organización, los servicios públicos y los ciudadanos. El Real Decreto 311/2022 define cada nivel en función de cinco dimensiones de seguridad: confidencialidad, integridad, disponibilidad, autenticidad y trazabilidad.

**Nivel Bajo** se aplica cuando un incidente tendría un impacto limitado. Ejemplo típico: un portal web informativo de un ayuntamiento que no gestiona datos personales sensibles. Las consecuencias de una brecha serían menores y no afectarían a derechos fundamentales.

**Nivel Medio** corresponde a sistemas donde un incidente tendría un impacto grave pero no catastrófico. Ejemplo: la sede electrónica de un ayuntamiento que gestiona trámites con datos personales, o un sistema de gestión tributaria municipal. Un incidente afectaría a servicios públicos y a datos de ciudadanos.

**Nivel Alto** se reserva para sistemas donde un incidente tendría consecuencias muy graves. Ejemplo: sistemas sanitarios con historiales clinicos, infraestructuras críticas, o sistemas que gestionen datos de menores o victimas de violencia de genero. Un incidente comprometeria derechos fundamentales o la seguridad pública.

| Dimensión | Bajo | Medio | Alto |
|-----------|------|-------|------|
| Impacto de un incidente | Limitado | Grave | Muy grave |
| Datos personales sensibles | No | Posible | Si |
| Servicios críticos afectados | No | Parcialmente | Directamente |
| Medidas de seguridad | 36 básicas | 36 básicas + refuerzos | 36 básicas + refuerzos + medidas adicionales |
| Tipo de auditoría | Autoevaluación | Auditoría formal bienal | Auditoría formal bienal + certificación |

## Cómo se categoriza un sistema en el ENS?

La categorización se realiza evaluando cada sistema de información en las cinco dimensiones de seguridad. Para cada dimensión, se determina el impacto que tendría un incidente y se asigna un nivel (bajo, medio o alto). El nivel global del sistema es el máximo de los niveles asignados a cada dimensión.

El CCN proporciona la herramienta PILAR para realizar esta categorización de forma sistemática. El proceso implica:

1. **Identificar los activos de información** que gestiona el sistema
2. **Evaluar el impacto** de una perdida de confidencialidad, integridad, disponibilidad, autenticidad o trazabilidad para cada activo
3. **Asignar el nivel** correspondiente a cada dimensión
4. **Determinar el nivel global** como el máximo de todas las dimensiones

La evaluación del impacto debe considerar factores concretos: si el sistema gestiona datos personales (artículo 9 del RGPD), si soporta servicios esenciales para los ciudadanos, si afecta a infraestructuras críticas y si un incidente tendría consecuencias legales, económicas o reputacionales significativas.

Según las guías CCN-STIC 803 y 804, los responsables de la información y del servicio son quienes determinan la categorización, no el equipo técnico. Esta decisión debe estar documentada y aprobada formalmente.

## Qué medidas de seguridad exige cada nivel?

El ENS define 36 familias de medidas de seguridad organizadas en tres marcos: organizativo, operacional y de protección. Cada medida tiene requisitos que varían según el nivel del sistema.

**Medidas organizativas** (comunes a todos los niveles):
- Política de seguridad aprobada por la dirección
- Normativa de seguridad documentada
- Procedimientos de seguridad operativos
- Proceso de autorización de acceso

**Diferencias clave por nivel:**

Para **nivel bajo**, las medidas se implementan en su versión básica. El control de acceso puede ser simple (usuario y contrasena), los registros de actividad son básicos y la gestión de incidentes es reactiva.

Para **nivel medio**, se exigen refuerzos significativos: autenticación de doble factor en accesos remotos, registros de actividad detallados con retención mínima de un año, gestión de incidentes con procedimientos formalizados, cifrado de datos en tránsito y copias de seguridad verificadas periodicamente.

Para **nivel alto**, se anaden medidas avanzadas: autenticación multifactor para todos los accesos, monitorización continua de la seguridad (SOC o equivalente), pruebas de penetración periódicas, segregación de redes, cifrado de datos en reposo, y auditoría de trazas con integridad garantizada.

{{< cta type="tofu" text="Riskitera mapea automaticamente controles ENS, NIS2 e ISO 27001, reduciendo el esfuerzo manual un 70%." label="Ver cómo" >}}

## Cómo elegir la categoría ENS correcta para tu organización?

La elección no es discrecional: depende del tipo de información que gestionas y de los servicios que prestas. Sin embargo, existen criterios prácticos que ayudan a determinar el nivel correcto:

**Categoriza como nivel bajo** si tu sistema:
- No gestiona datos personales más allá de datos de contacto básicos
- Ofrece información pública sin interacción con ciudadanos
- No soporta servicios esenciales
- Un fallo no afectaría a derechos de terceros

**Categoriza como nivel medio** si tu sistema:
- Gestiona datos personales de ciudadanos (padrón, tributos, licencias)
- Soporta tramitación electrónica o sede electrónica
- Un fallo interrumpiria servicios públicos durante horas o días
- Maneja datos económicos o contractuales

**Categoriza como nivel alto** si tu sistema:
- Gestiona datos de categorías especiales (salud, menores, victimas)
- Soporta infraestructuras críticas o servicios esenciales
- Un fallo comprometeria derechos fundamentales
- Maneja información clasificada o secretos oficiales

La recomendación del CCN es categorizar siempre con un enfoque conservador: ante la duda entre dos niveles, elegir el superior. Recategorizar a la baja después de una auditoría es más complicado que implementar medidas adicionales desde el inicio.

## Qué pasa si categorizo mal mi sistema?

Una categorización incorrecta tiene consecuencias directas en la auditoría de cumplimiento y en la protección real de la organización.

**Si categorizas por debajo del nivel real:**
- La auditoría detectara que las medidas implementadas son insuficientes para los riesgos reales
- El informe de auditoría reflejara no conformidades críticas
- En caso de incidente, la organización podría enfrentar responsabilidades agravadas por negligencia en la categorización
- El CCN puede exigir una recategorización y la implementación urgente de medidas adicionales

**Si categorizas por encima del nivel necesario:**
- Implementaras medidas de seguridad innecesariamente costosas
- Los plazos de implementación se alargan sin beneficio proporcional
- Los recursos (presupuesto, personal) se desvian de otras prioridades
- La auditoría será más exigente y costosa de lo necesario

Según datos del CCN-CERT de 2025, los errores más frecuentes de categorización son: no considerar los datos personales que gestiona el sistema, no evaluar el impacto en los ciudadanos (solo en la organización), y categorizar todos los sistemas al mismo nivel sin análisis individual.

## Cuánto cuesta implementar cada nivel del ENS?

Los costes varían enormemente según el tamaño de la organización, el estado actual de su seguridad y el número de sistemas a certificar. Estas son referencias del mercado español en 2026:

| Concepto | Nivel Bajo | Nivel Medio | Nivel Alto |
|----------|-----------|-------------|------------|
| Consultoria y gap analysis | 5.000 - 15.000 EUR | 15.000 - 40.000 EUR | 30.000 - 80.000 EUR |
| Implementación de medidas | 3.000 - 10.000 EUR | 20.000 - 60.000 EUR | 50.000 - 200.000 EUR |
| Auditoría | Autoevaluación (interno) | 8.000 - 15.000 EUR | 12.000 - 25.000 EUR |
| Mantenimiento anual | 2.000 - 5.000 EUR | 10.000 - 25.000 EUR | 25.000 - 60.000 EUR |
| **Total primer año** | **10.000 - 30.000 EUR** | **43.000 - 115.000 EUR** | **92.000 - 305.000 EUR** |

Las herramientas gratuitas del CCN (PILAR, INES, LUCIA, microCLAUDIA) reducen significativamente el coste para administraciones públicas. Las plataformas GRC como Riskitera automatizan la gestión de controles y evidencias, reduciendo el coste operativo recurrente entre un 40% y un 70%.

## Cómo se relacionan los niveles del ENS con ISO 27001?

El ENS y la ISO 27001 comparten muchos controles, pero no son equivalentes. Una organización certificada en ISO 27001 tiene entre un 60% y un 70% del camino recorrido para el ENS, según estimaciones del CCN.

Las principales diferencias:
- **ISO 27001 no tiene niveles**: aplica los mismos requisitos a todos los sistemas
- **ENS tiene medidas prescriptivas**: ISO 27001 permite elegir controles; el ENS los impone según el nivel
- **ENS exige herramientas CCN**: para el sector público, el uso de PILAR e INES es obligatorio
- **Auditoría diferente**: ISO 27001 requiere auditoría de un organismo acreditado por ENAC; el ENS acepta auditores del sector público

Para organizaciones que deben cumplir ambos marcos, la recomendación es implementarlos de forma coordinada: usar el análisis de riesgos de ISO 27001 como base para la categorización ENS, y mapear los controles del Anexo A de ISO 27001 a las medidas del ENS para evitar duplicar esfuerzos.

{{< cta type="mofu" text="Automatiza la recopilacion de evidencias y el seguimiento de controles con Riskitera." >}}

**Artículos relacionados:**
- [Qué es el Esquema Nacional de Seguridad (ENS)](/es/posts/2026/04/que-es-esquema-nacional-seguridad-ens/)
- [Guía práctica: ISO 27001 para Startups](/es/posts/2026/02/guia-iso-27001-startups/)

## Preguntas frecuentes

### Puede un sistema tener nivel alto en una dimensión y bajo en otra?

Sí. La categorización se realiza dimensión por dimensión. Un sistema puede tener nivel alto en confidencialidad (gestiona datos sensibles) y nivel bajo en disponibilidad (no es crítico que este caido unas horas). El nivel global del sistema será el máximo de todas las dimensiones, es decir, alto en este ejemplo.

### Cada cuanto hay que revisar la categorización?

La categorización debe revisarse al menos cada dos años (coincidiendo con el ciclo de auditoría) o siempre que haya cambios significativos en el sistema: nuevos tipos de datos, nuevos servicios, cambios en la infraestructura o modificaciones normativas. El RD 311/2022 exige que la categorización sea un proceso vivo, no un ejercicio puntual.

### Los proveedores tecnológicos del sector público necesitan certificarse en ENS?

Sí. Desde la entrada en vigor del RD 311/2022, los proveedores que gestionan sistemas de información para la administración pública deben cumplir con el ENS en el nivel correspondiente al sistema que gestionan. Esto afecta a empresas de desarrollo de software, hosting, servicios cloud y consultoría TIC que trabajan con el sector público.

### Qué pasa si mi organización no cumple el ENS?

El incumplimiento del ENS puede resultar en la imposibilidad de contratar con la administración pública, responsabilidades administrativas en caso de incidente, y daños reputacionales. Aunque el ENS no establece sanciones económicas directas como el RGPD, el CCN puede publicar el estado de cumplimiento de las entidades y exigir planes de adecuación con plazos concretos.

### Es posible obtener una certificación ENS que cubra varios niveles?

Sí. Una organización puede certificar diferentes sistemas en diferentes niveles dentro de la misma auditoría. Es común que un ayuntamiento tenga su portal web en nivel bajo, la sede electrónica en nivel medio y el sistema de policía local en nivel alto, todo bajo un mismo marco de cumplimiento ENS.
