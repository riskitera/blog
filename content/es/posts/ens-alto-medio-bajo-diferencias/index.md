---
title: "ENS Alto vs Medio vs Bajo: diferencias, requisitos y como elegir categoria"
description: "Comparativa detallada de los tres niveles del Esquema Nacional de Seguridad (ENS): criterios de categorizacion, medidas obligatorias por nivel y como elegir la categoria correcta para tu organizacion."
slug: "ens-alto-medio-bajo-diferencias"
date: 2026-05-05
publishDate: 2026-05-05
lastmod: 2026-05-05
draft: false
tags: ["ENS", "Compliance", "Seguridad"]
categories: ["Compliance"]
author: "Riskitera Team"
keyword: "ENS alto medio bajo"
funnel: "tofu"
---

El Esquema Nacional de Seguridad (ENS) clasifica los sistemas de informacion en tres niveles: bajo, medio y alto. Esta categorizacion determina las medidas de seguridad que cada organizacion debe implementar y el tipo de auditoria al que debe someterse. Segun el CCN-CERT, mas del 40% de las organizaciones publicas espanolas categorizan incorrectamente sus sistemas, lo que genera problemas en la auditoria y en la proteccion real de la informacion. En esta guia detallamos las diferencias entre cada nivel, los criterios para elegir y los costes asociados.

<!--more-->

## Que diferencias hay entre ENS Alto, Medio y Bajo?

Los tres niveles del ENS reflejan el impacto que un incidente de seguridad tendria sobre la organizacion, los servicios publicos y los ciudadanos. El Real Decreto 311/2022 define cada nivel en funcion de cinco dimensiones de seguridad: confidencialidad, integridad, disponibilidad, autenticidad y trazabilidad.

**Nivel Bajo** se aplica cuando un incidente tendria un impacto limitado. Ejemplo tipico: un portal web informativo de un ayuntamiento que no gestiona datos personales sensibles. Las consecuencias de una brecha serian menores y no afectarian a derechos fundamentales.

**Nivel Medio** corresponde a sistemas donde un incidente tendria un impacto grave pero no catastrofico. Ejemplo: la sede electronica de un ayuntamiento que gestiona tramites con datos personales, o un sistema de gestion tributaria municipal. Un incidente afectaria a servicios publicos y a datos de ciudadanos.

**Nivel Alto** se reserva para sistemas donde un incidente tendria consecuencias muy graves. Ejemplo: sistemas sanitarios con historiales clinicos, infraestructuras criticas, o sistemas que gestionen datos de menores o victimas de violencia de genero. Un incidente comprometeria derechos fundamentales o la seguridad publica.

| Dimension | Bajo | Medio | Alto |
|-----------|------|-------|------|
| Impacto de un incidente | Limitado | Grave | Muy grave |
| Datos personales sensibles | No | Posible | Si |
| Servicios criticos afectados | No | Parcialmente | Directamente |
| Medidas de seguridad | 36 basicas | 36 basicas + refuerzos | 36 basicas + refuerzos + medidas adicionales |
| Tipo de auditoria | Autoevaluacion | Auditoria formal bienal | Auditoria formal bienal + certificacion |

## Como se categoriza un sistema en el ENS?

La categorizacion se realiza evaluando cada sistema de informacion en las cinco dimensiones de seguridad. Para cada dimension, se determina el impacto que tendria un incidente y se asigna un nivel (bajo, medio o alto). El nivel global del sistema es el maximo de los niveles asignados a cada dimension.

El CCN proporciona la herramienta PILAR para realizar esta categorizacion de forma sistematica. El proceso implica:

1. **Identificar los activos de informacion** que gestiona el sistema
2. **Evaluar el impacto** de una perdida de confidencialidad, integridad, disponibilidad, autenticidad o trazabilidad para cada activo
3. **Asignar el nivel** correspondiente a cada dimension
4. **Determinar el nivel global** como el maximo de todas las dimensiones

La evaluacion del impacto debe considerar factores concretos: si el sistema gestiona datos personales (articulo 9 del RGPD), si soporta servicios esenciales para los ciudadanos, si afecta a infraestructuras criticas y si un incidente tendria consecuencias legales, economicas o reputacionales significativas.

Segun las guias CCN-STIC 803 y 804, los responsables de la informacion y del servicio son quienes determinan la categorizacion, no el equipo tecnico. Esta decision debe estar documentada y aprobada formalmente.

## Que medidas de seguridad exige cada nivel?

El ENS define 36 familias de medidas de seguridad organizadas en tres marcos: organizativo, operacional y de proteccion. Cada medida tiene requisitos que varian segun el nivel del sistema.

**Medidas organizativas** (comunes a todos los niveles):
- Politica de seguridad aprobada por la direccion
- Normativa de seguridad documentada
- Procedimientos de seguridad operativos
- Proceso de autorizacion de acceso

**Diferencias clave por nivel:**

Para **nivel bajo**, las medidas se implementan en su version basica. El control de acceso puede ser simple (usuario y contrasena), los registros de actividad son basicos y la gestion de incidentes es reactiva.

Para **nivel medio**, se exigen refuerzos significativos: autenticacion de doble factor en accesos remotos, registros de actividad detallados con retencion minima de un ano, gestion de incidentes con procedimientos formalizados, cifrado de datos en transito y copias de seguridad verificadas periodicamente.

Para **nivel alto**, se anaden medidas avanzadas: autenticacion multifactor para todos los accesos, monitorizacion continua de la seguridad (SOC o equivalente), pruebas de penetracion periodicas, segregacion de redes, cifrado de datos en reposo, y auditoria de trazas con integridad garantizada.

{{< cta type="tofu" text="Riskitera mapea automaticamente controles ENS, NIS2 e ISO 27001, reduciendo el esfuerzo manual un 70%." label="Ver como" >}}

## Como elegir la categoria ENS correcta para tu organizacion?

La eleccion no es discrecional: depende del tipo de informacion que gestionas y de los servicios que prestas. Sin embargo, existen criterios practicos que ayudan a determinar el nivel correcto:

**Categoriza como nivel bajo** si tu sistema:
- No gestiona datos personales mas alla de datos de contacto basicos
- Ofrece informacion publica sin interaccion con ciudadanos
- No soporta servicios esenciales
- Un fallo no afectaria a derechos de terceros

**Categoriza como nivel medio** si tu sistema:
- Gestiona datos personales de ciudadanos (padron, tributos, licencias)
- Soporta tramitacion electronica o sede electronica
- Un fallo interrumpiria servicios publicos durante horas o dias
- Maneja datos economicos o contractuales

**Categoriza como nivel alto** si tu sistema:
- Gestiona datos de categorias especiales (salud, menores, victimas)
- Soporta infraestructuras criticas o servicios esenciales
- Un fallo comprometeria derechos fundamentales
- Maneja informacion clasificada o secretos oficiales

La recomendacion del CCN es categorizar siempre con un enfoque conservador: ante la duda entre dos niveles, elegir el superior. Recategorizar a la baja despues de una auditoria es mas complicado que implementar medidas adicionales desde el inicio.

## Que pasa si categorizo mal mi sistema?

Una categorizacion incorrecta tiene consecuencias directas en la auditoria de cumplimiento y en la proteccion real de la organizacion.

**Si categorizas por debajo del nivel real:**
- La auditoria detectara que las medidas implementadas son insuficientes para los riesgos reales
- El informe de auditoria reflejara no conformidades criticas
- En caso de incidente, la organizacion podria enfrentar responsabilidades agravadas por negligencia en la categorizacion
- El CCN puede exigir una recategorizacion y la implementacion urgente de medidas adicionales

**Si categorizas por encima del nivel necesario:**
- Implementaras medidas de seguridad innecesariamente costosas
- Los plazos de implementacion se alargan sin beneficio proporcional
- Los recursos (presupuesto, personal) se desvian de otras prioridades
- La auditoria sera mas exigente y costosa de lo necesario

Segun datos del CCN-CERT de 2025, los errores mas frecuentes de categorizacion son: no considerar los datos personales que gestiona el sistema, no evaluar el impacto en los ciudadanos (solo en la organizacion), y categorizar todos los sistemas al mismo nivel sin analisis individual.

## Cuanto cuesta implementar cada nivel del ENS?

Los costes varian enormemente segun el tamano de la organizacion, el estado actual de su seguridad y el numero de sistemas a certificar. Estas son referencias del mercado espanol en 2026:

| Concepto | Nivel Bajo | Nivel Medio | Nivel Alto |
|----------|-----------|-------------|------------|
| Consultoria y gap analysis | 5.000 - 15.000 EUR | 15.000 - 40.000 EUR | 30.000 - 80.000 EUR |
| Implementacion de medidas | 3.000 - 10.000 EUR | 20.000 - 60.000 EUR | 50.000 - 200.000 EUR |
| Auditoria | Autoevaluacion (interno) | 8.000 - 15.000 EUR | 12.000 - 25.000 EUR |
| Mantenimiento anual | 2.000 - 5.000 EUR | 10.000 - 25.000 EUR | 25.000 - 60.000 EUR |
| **Total primer ano** | **10.000 - 30.000 EUR** | **43.000 - 115.000 EUR** | **92.000 - 305.000 EUR** |

Las herramientas gratuitas del CCN (PILAR, INES, LUCIA, microCLAUDIA) reducen significativamente el coste para administraciones publicas. Las plataformas GRC como Riskitera automatizan la gestion de controles y evidencias, reduciendo el coste operativo recurrente entre un 40% y un 70%.

## Como se relacionan los niveles del ENS con ISO 27001?

El ENS y la ISO 27001 comparten muchos controles, pero no son equivalentes. Una organizacion certificada en ISO 27001 tiene entre un 60% y un 70% del camino recorrido para el ENS, segun estimaciones del CCN.

Las principales diferencias:
- **ISO 27001 no tiene niveles**: aplica los mismos requisitos a todos los sistemas
- **ENS tiene medidas prescriptivas**: ISO 27001 permite elegir controles; el ENS los impone segun el nivel
- **ENS exige herramientas CCN**: para el sector publico, el uso de PILAR e INES es obligatorio
- **Auditoria diferente**: ISO 27001 requiere auditoria de un organismo acreditado por ENAC; el ENS acepta auditores del sector publico

Para organizaciones que deben cumplir ambos marcos, la recomendacion es implementarlos de forma coordinada: usar el analisis de riesgos de ISO 27001 como base para la categorizacion ENS, y mapear los controles del Anexo A de ISO 27001 a las medidas del ENS para evitar duplicar esfuerzos.

{{< cta type="mofu" text="Automatiza la recopilacion de evidencias y el seguimiento de controles con Riskitera." >}}

**Articulos relacionados:**
- [Que es el Esquema Nacional de Seguridad (ENS)](/es/posts/2026/04/que-es-esquema-nacional-seguridad-ens/)
- [Guia practica: ISO 27001 para Startups](/es/posts/2026/02/guia-iso-27001-startups/)

## Preguntas frecuentes

### Puede un sistema tener nivel alto en una dimension y bajo en otra?

Si. La categorizacion se realiza dimension por dimension. Un sistema puede tener nivel alto en confidencialidad (gestiona datos sensibles) y nivel bajo en disponibilidad (no es critico que este caido unas horas). El nivel global del sistema sera el maximo de todas las dimensiones, es decir, alto en este ejemplo.

### Cada cuanto hay que revisar la categorizacion?

La categorizacion debe revisarse al menos cada dos anos (coincidiendo con el ciclo de auditoria) o siempre que haya cambios significativos en el sistema: nuevos tipos de datos, nuevos servicios, cambios en la infraestructura o modificaciones normativas. El RD 311/2022 exige que la categorizacion sea un proceso vivo, no un ejercicio puntual.

### Los proveedores tecnologicos del sector publico necesitan certificarse en ENS?

Si. Desde la entrada en vigor del RD 311/2022, los proveedores que gestionan sistemas de informacion para la administracion publica deben cumplir con el ENS en el nivel correspondiente al sistema que gestionan. Esto afecta a empresas de desarrollo de software, hosting, servicios cloud y consultoria TIC que trabajan con el sector publico.

### Que pasa si mi organizacion no cumple el ENS?

El incumplimiento del ENS puede resultar en la imposibilidad de contratar con la administracion publica, responsabilidades administrativas en caso de incidente, y danos reputacionales. Aunque el ENS no establece sanciones economicas directas como el RGPD, el CCN puede publicar el estado de cumplimiento de las entidades y exigir planes de adecuacion con plazos concretos.

### Es posible obtener una certificacion ENS que cubra varios niveles?

Si. Una organizacion puede certificar diferentes sistemas en diferentes niveles dentro de la misma auditoria. Es comun que un ayuntamiento tenga su portal web en nivel bajo, la sede electronica en nivel medio y el sistema de policia local en nivel alto, todo bajo un mismo marco de cumplimiento ENS.
