---
title: "Ciberseguridad en banca: cómo cumplir DORA paso a paso"
description: "Guía práctica para entidades bancarias y fintech sobre cómo cumplir el reglamento DORA: requisitos técnicos, gestión de riesgos TIC, pruebas de resiliencia y plazos de implementación."
slug: "ciberseguridad-banca-dora"
date: 2026-05-19
publishDate: 2026-05-19
lastmod: 2026-05-19
draft: false
tags: ["DORA", "Banca", "Fintech", "Compliance"]
categories: ["Compliance"]
author: "David Moya"
keyword: "DORA bancos"
funnel: "mofu"
---

Guía práctica para entidades bancarias y fintech sobre cómo cumplir el reglamento DORA: requisitos técnicos, gestión de riesgos TIC, pruebas de resiliencia y plazos de implementación.

<!--more-->

## ¿Cómo afecta DORA a los bancos y entidades financieras?

El Reglamento DORA (Digital Operational Resilience Act, Reglamento UE 2022/2554) es de aplicación directa desde enero de 2025 para todas las entidades financieras de la UE. Esto incluye bancos, aseguradoras, gestoras de fondos, empresas de servicios de inversión, entidades de pago, fintech con licencia y proveedores críticos de servicios TIC.

El cambio fundamental que introduce DORA es que la resiliencia digital deja de ser una recomendación y se convierte en una obligación legal supervisada. Las autoridades competentes (en España, el Banco de España y la CNMV) tienen potestad para inspeccionar, exigir correcciones y sancionar.

Para los bancos españoles, DORA se superpone al marco de supervisión existente (EBA Guidelines on ICT and Security Risk Management) pero eleva el nivel de exigencia en cinco áreas clave: gestión de riesgos TIC, notificación de incidentes, pruebas de resiliencia, gestión de proveedores y compartición de información.

El impacto operativo es significativo. Según un estudio de McKinsey de 2025, el 68% de las entidades financieras europeas necesitaron reorganizar sus funciones de IT y riesgo para cumplir con DORA. El coste medio de adaptación para un banco mediano europeo se estima entre 2 y 5 millones de euros, dependiendo del nivel de madurez previo.

## ¿Cuáles son los requisitos técnicos de DORA para banca?

DORA estructura sus requisitos en cinco pilares. Cada uno tiene implicaciones técnicas directas:

**Pilar 1: Gestión de riesgos TIC.** Las entidades deben mantener un marco de gestión de riesgos TIC documentado, aprobado por el órgano de dirección y revisado al menos anualmente. Esto incluye: inventario actualizado de activos TIC, análisis de riesgos con metodología formal, políticas de seguridad de la información, gestión de identidades y accesos, cifrado de datos en reposo y en tránsito, y planes de continuidad y recuperación.

**Pilar 2: Notificación de incidentes.** Las entidades deben clasificar los incidentes TIC según criterios definidos por las ESAs (European Supervisory Authorities). Los incidentes graves requieren tres notificaciones: inicial (dentro de 4 horas desde la clasificación), intermedia (dentro de 72 horas) y final (dentro de 1 mes). La clasificación se basa en: clientes afectados, duración, pérdida de datos, impacto económico, criticidad de los servicios y extensión geográfica.

**Pilar 3: Pruebas de resiliencia operativa digital.** Todas las entidades deben realizar pruebas básicas (análisis de vulnerabilidades, escaneos de red, revisiones de código) al menos anualmente. Las entidades significativas deben realizar pruebas TLPT (Threat-Led Penetration Testing) al menos cada tres años, bajo el marco TIBER-EU.

**Pilar 4: Gestión de riesgos de terceros TIC.** Requisitos contractuales mínimos con proveedores TIC, registro de contratos con proveedores, estrategia de salida documentada para cada proveedor crítico, y evaluación de riesgos de concentración.

**Pilar 5: Compartición de información.** DORA fomenta (sin obligar) la participación en redes de compartición de inteligencia sobre ciberamenazas entre entidades financieras.

## ¿Cómo implementar la gestión de riesgos TIC que exige DORA?

La gestión de riesgos TIC de DORA requiere un enfoque sistemático. Estos son los pasos clave para una entidad bancaria:

**1. Inventario de activos TIC.** Catalogar todos los activos de información, sistemas, redes y dependencias externas. No es un inventario de IT clásico: DORA exige vincular cada activo a las funciones de negocio que soporta y clasificarlo según su criticidad. Los activos que soportan funciones críticas o importantes (core banking, sistemas de pago, canales digitales) reciben requisitos adicionales.

**2. Análisis de riesgos formalizado.** Evaluar amenazas, vulnerabilidades e impacto para cada activo crítico. DORA no prescribe una metodología concreta (puedes usar MAGERIT, ISO 27005, FAIR o NIST RMF), pero exige que sea documentada, repetible y revisada al menos anualmente.

**3. Políticas de protección.** Documentar e implementar políticas de: control de accesos (principio de mínimo privilegio), segmentación de redes, cifrado (TLS 1.2+ en tránsito, AES-256 en reposo), gestión de parches (con SLAs según criticidad), seguridad en el desarrollo (SDLC seguro) y gestión de logs (retención mínima alineada con requisitos regulatorios).

**4. Detección y respuesta.** Implementar capacidades de monitorización continua (SIEM, EDR, NDR), definir umbrales de alerta, establecer procedimientos de escalado y tener un equipo o servicio de respuesta a incidentes operativo 24/7.

**5. Continuidad y recuperación.** Planes de continuidad de negocio (BCP) y recuperación ante desastres (DRP) probados al menos anualmente. DORA exige RPO y RTO definidos para cada función crítica y pruebas documentadas que demuestren que se cumplen.

**6. Gobernanza.** El órgano de dirección (consejo de administración) es responsable último de la gestión de riesgos TIC. Debe aprobar el marco, supervisar su ejecución y recibir formación específica en riesgos digitales.

{{< cta type="tofu" text="Riskitera cubre los requisitos técnicos de DORA, ENS y NIS2 con una arquitectura soberana." label="Ver arquitectura" >}}

## ¿Qué pruebas de resiliencia operativa son obligatorias?

DORA establece dos niveles de pruebas:

**Pruebas básicas (todas las entidades).** Deben realizarse al menos anualmente sobre los sistemas y aplicaciones TIC críticos:
- Análisis de vulnerabilidades (escaneos automatizados + validación manual)
- Pruebas de seguridad de red y de perímetro
- Análisis de gaps de seguridad
- Revisiones de código fuente (para sistemas desarrollados internamente)
- Pruebas de rendimiento y capacidad
- Pruebas de compatibilidad y migración
- Pruebas de escenarios de crisis (tabletop exercises)

**Pruebas TLPT (entidades significativas).** Las entidades identificadas como significativas por su autoridad supervisora deben realizar pruebas TLPT al menos cada tres años. Estas pruebas siguen el marco TIBER-EU (adaptado en España como TIBER-ES por el Banco de España) y consisten en:
1. Fase de Threat Intelligence: un equipo externo analiza las amenazas reales que enfrenta la entidad
2. Fase de Red Team: un equipo de ataque externo simula las tácticas, técnicas y procedimientos de los actores de amenaza identificados
3. Fase de Blue Team: se evalúa la capacidad de detección y respuesta del equipo interno
4. Informe y remediación: documentación de hallazgos, plan de remediación con plazos y seguimiento

Los criterios para determinar si una entidad es "significativa" incluyen: tamaño (activos totales), interconexión con el sistema financiero, complejidad de la infraestructura TIC y si presta servicios críticos a otras entidades.

Las pruebas TLPT deben ser ejecutadas por proveedores externos certificados. Los resultados son confidenciales pero deben compartirse con la autoridad supervisora.

## ¿Cómo gestionar proveedores TIC críticos bajo DORA?

La gestión de terceros es uno de los aspectos más exigentes de DORA para los bancos, especialmente por la dependencia creciente de servicios cloud, fintech y proveedores de software.

**Clasificación de proveedores.** Cada entidad debe clasificar sus proveedores TIC según la criticidad de la función que soportan. Un proveedor es crítico si su fallo, degradación o interrupción pondría en riesgo la continuidad de funciones críticas o importantes del banco.

**Requisitos contractuales mínimos.** DORA define cláusulas obligatorias en los contratos con proveedores TIC:
- Descripción completa de servicios con SLAs medibles
- Localización de datos y procesamiento (país y región)
- Disponibilidad, autenticidad, integridad y confidencialidad de datos
- Derecho de acceso, inspección y auditoría por parte de la entidad y del regulador
- Notificación de incidentes que afecten a los servicios prestados
- Plan de continuidad del servicio
- Estrategia de salida con periodos de transición adecuados
- Obligación de cooperar en caso de resolución de la entidad financiera

**Registro de proveedores.** Las entidades deben mantener un registro actualizado de todos los contratos con proveedores TIC y reportarlo anualmente a su autoridad supervisora. Las ESAs mantendrán un registro centralizado europeo.

**Riesgo de concentración.** DORA introduce el concepto de proveedor crítico a nivel europeo. Si un proveedor TIC (por ejemplo, un gran hiperescalar cloud) es designado como crítico por las ESAs, queda sujeto a supervisión directa europea con capacidad sancionadora.

**Estrategia de salida.** Para cada proveedor crítico, el banco debe tener documentada una estrategia de salida viable que permita migrar el servicio a otro proveedor o internalizarlo sin interrupción de funciones críticas.

## ¿Cuál es el calendario de implementación para banca?

DORA fue publicado en el Diario Oficial de la UE en diciembre de 2022 y es de aplicación desde el 17 de enero de 2025. No hay periodo transitorio: las entidades deben cumplir todos los requisitos desde esa fecha.

Sin embargo, la implementación práctica sigue un calendario más granular:

**Enero 2025.** Aplicación completa del Reglamento. Las entidades deben tener operativos: marco de gestión de riesgos TIC, clasificación de incidentes, registro de proveedores, políticas de continuidad.

**Abril 2025.** Publicación de los estándares técnicos regulatorios (RTS) e implementación técnica (ITS) finales por las ESAs. Estos detallan los formatos de notificación de incidentes, las plantillas del registro de proveedores y los criterios de clasificación de funciones críticas.

**2025-2026.** Periodo de adaptación práctica. Las autoridades supervisoras están realizando inspecciones de "readiness" y exigiendo planes de remediación para las entidades que presentan gaps. No es un periodo de gracia formal, pero las primeras sanciones se esperan para entidades con deficiencias graves sin plan de corrección.

**2025-2027.** Primera ronda de pruebas TLPT para entidades significativas. El Banco de España está definiendo el listado de entidades sujetas y la planificación de pruebas.

**2026 en adelante.** Régimen sancionador plenamente operativo. Revisión periódica del marco por la Comisión Europea (prevista para enero de 2028).

## ¿Qué sanciones aplican a entidades financieras que incumplan?

DORA delega la definición del régimen sancionador en los Estados miembros, pero establece requisitos mínimos. Las autoridades competentes deben tener la potestad de:

- Emitir requerimientos de cese de prácticas que vulneren DORA
- Exigir medidas correctivas con plazos vinculantes
- Imponer sanciones administrativas pecuniarias

En España, el régimen sancionador se integra en la Ley del Mercado de Valores, la Ley de Ordenación, Supervisión y Solvencia de Entidades de Crédito y normativa sectorial aplicable. Las sanciones pueden incluir:

**Para entidades financieras:**
- Multas de hasta el 1% del volumen de negocios medio diario del año anterior, impuestas de forma diaria hasta que se corrija el incumplimiento
- Amonestaciones públicas identificando a la entidad y la infracción
- Suspensión temporal de actividades

**Para proveedores TIC críticos designados:**
- Multas de hasta el 1% del volumen de negocios medio diario mundial del año anterior
- Multas coercitivas diarias hasta corregir la situación
- Publicación de las resoluciones sancionadoras

**Para miembros del órgano de dirección:**
- Responsabilidad personal por incumplimiento de sus obligaciones de gobernanza TIC
- Posibles sanciones administrativas individuales

El impacto reputacional de una sanción pública por incumplimiento de DORA puede ser más dañino que la multa económica, especialmente en un sector donde la confianza es el activo fundamental.


{{< cta type="bofu" text="Agenda una demo técnica para tu sector y valida la integración con tu infraestructura." label="Agenda demo" >}}


**Artículos relacionados:**
- [Dora Reglamento Ciberseguridad Financiera](/es/posts/2026/04/dora-reglamento-ciberseguridad-financiera/)

## Dudas habituales

**¿DORA aplica a fintech y neobancos?**
Sí. DORA aplica a todas las entidades financieras reguladas en la UE, incluyendo entidades de pago, entidades de dinero electrónico y proveedores de servicios de criptoactivos autorizados bajo MiCA. Las fintech con licencia bancaria o de servicios de pago están sujetas a los mismos requisitos que los bancos tradicionales.

**¿Qué diferencia hay entre DORA y las guías EBA de riesgos TIC?**
Las guías EBA (EBA/GL/2019/04) eran recomendaciones de "cumplir o explicar" (comply or explain). DORA es un reglamento de aplicación directa con capacidad sancionadora. DORA absorbe y eleva el nivel de las guías EBA, añadiendo requisitos nuevos como las pruebas TLPT obligatorias y la supervisión directa de proveedores críticos.

**¿Si mi banco ya cumple ENS Alto, cumple también DORA?**
No automáticamente. ENS Alto y DORA tienen solapamientos significativos (gestión de riesgos, continuidad, control de accesos), pero DORA introduce requisitos específicos que el ENS no cubre: notificación de incidentes con plazos determinados, pruebas TLPT, requisitos contractuales detallados para proveedores TIC y registro centralizado de contratos. Un banco que cumple ENS Alto tiene buena base, pero necesita un análisis de gaps específico para DORA.

**¿Cuánto cuesta adaptarse a DORA para un banco mediano?**
Depende del nivel de madurez previo. Para un banco mediano español con una postura de seguridad razonable (ENS Alto o ISO 27001 certificado), el coste de adaptación se estima entre 500.000 y 2 millones de euros, incluyendo consultoría, herramientas, personal y pruebas TLPT. Para entidades con menor madurez, puede superar los 5 millones.

**¿Cómo se coordinan DORA y NIS2 para bancos?**
DORA es lex specialis frente a NIS2 para el sector financiero. Esto significa que los bancos cumplen NIS2 a través de DORA: los requisitos de DORA son más específicos y exigentes que los de NIS2 para este sector. No hay doble cumplimiento, pero la entidad debe poder demostrar ante ambos marcos.
