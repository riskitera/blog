---
title: "Ciberseguridad en banca: como cumplir DORA paso a paso"
description: "Guia practica para entidades bancarias y fintech sobre como cumplir el reglamento DORA: requisitos tecnicos, gestion de riesgos TIC, pruebas de resiliencia y plazos de implementacion."
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

Guia practica para entidades bancarias y fintech sobre como cumplir el reglamento DORA: requisitos tecnicos, gestion de riesgos TIC, pruebas de resiliencia y plazos de implementacion.

<!--more-->

## Como afecta DORA a los bancos y entidades financieras?

El Reglamento DORA (Digital Operational Resilience Act, Reglamento UE 2022/2554) es de aplicacion directa desde enero de 2025 para todas las entidades financieras de la UE. Esto incluye bancos, aseguradoras, gestoras de fondos, empresas de servicios de inversion, entidades de pago, fintech con licencia y proveedores criticos de servicios TIC.

El cambio fundamental que introduce DORA es que la resiliencia digital deja de ser una recomendacion y se convierte en una obligacion legal supervisada. Las autoridades competentes (en Espana, el Banco de Espana y la CNMV) tienen potestad para inspeccionar, exigir correcciones y sancionar.

Para los bancos espanoles, DORA se superpone al marco de supervision existente (EBA Guidelines on ICT and Security Risk Management) pero eleva el nivel de exigencia en cinco areas clave: gestion de riesgos TIC, notificacion de incidentes, pruebas de resiliencia, gestion de proveedores y comparticion de informacion.

El impacto operativo es significativo. Segun un estudio de McKinsey de 2025, el 68% de las entidades financieras europeas necesitaron reorganizar sus funciones de IT y riesgo para cumplir con DORA. El coste medio de adaptacion para un banco mediano europeo se estima entre 2 y 5 millones de euros, dependiendo del nivel de madurez previo.

## Cuales son los requisitos tecnicos de DORA para banca?

DORA estructura sus requisitos en cinco pilares. Cada uno tiene implicaciones tecnicas directas:

**Pilar 1: Gestion de riesgos TIC.** Las entidades deben mantener un marco de gestion de riesgos TIC documentado, aprobado por el organo de direccion y revisado al menos anualmente. Esto incluye: inventario actualizado de activos TIC, analisis de riesgos con metodologia formal, politicas de seguridad de la informacion, gestion de identidades y accesos, cifrado de datos en reposo y en transito, y planes de continuidad y recuperacion.

**Pilar 2: Notificacion de incidentes.** Las entidades deben clasificar los incidentes TIC segun criterios definidos por las ESAs (European Supervisory Authorities). Los incidentes graves requieren tres notificaciones: inicial (dentro de 4 horas desde la clasificacion), intermedia (dentro de 72 horas) y final (dentro de 1 mes). La clasificacion se basa en: clientes afectados, duracion, perdida de datos, impacto economico, criticidad de los servicios y extension geografica.

**Pilar 3: Pruebas de resiliencia operativa digital.** Todas las entidades deben realizar pruebas basicas (analisis de vulnerabilidades, escaneos de red, revisiones de codigo) al menos anualmente. Las entidades significativas deben realizar pruebas TLPT (Threat-Led Penetration Testing) al menos cada tres anos, bajo el marco TIBER-EU.

**Pilar 4: Gestion de riesgos de terceros TIC.** Requisitos contractuales minimos con proveedores TIC, registro de contratos con proveedores, estrategia de salida documentada para cada proveedor critico, y evaluacion de riesgos de concentracion.

**Pilar 5: Comparticion de informacion.** DORA fomenta (sin obligar) la participacion en redes de comparticion de inteligencia sobre ciberamenazas entre entidades financieras.

## Como implementar la gestion de riesgos TIC que exige DORA?

La gestion de riesgos TIC de DORA requiere un enfoque sistematico. Estos son los pasos clave para una entidad bancaria:

**1. Inventario de activos TIC.** Catalogar todos los activos de informacion, sistemas, redes y dependencias externas. No es un inventario de IT clasico: DORA exige vincular cada activo a las funciones de negocio que soporta y clasificarlo segun su criticidad. Los activos que soportan funciones criticas o importantes (core banking, sistemas de pago, canales digitales) reciben requisitos adicionales.

**2. Analisis de riesgos formalizado.** Evaluar amenazas, vulnerabilidades e impacto para cada activo critico. DORA no prescribe una metodologia concreta (puedes usar MAGERIT, ISO 27005, FAIR o NIST RMF), pero exige que sea documentada, repetible y revisada al menos anualmente.

**3. Politicas de proteccion.** Documentar e implementar politicas de: control de accesos (principio de minimo privilegio), segmentacion de redes, cifrado (TLS 1.2+ en transito, AES-256 en reposo), gestion de parches (con SLAs segun criticidad), seguridad en el desarrollo (SDLC seguro) y gestion de logs (retencion minima alineada con requisitos regulatorios).

**4. Deteccion y respuesta.** Implementar capacidades de monitorizacion continua (SIEM, EDR, NDR), definir umbrales de alerta, establecer procedimientos de escalado y tener un equipo o servicio de respuesta a incidentes operativo 24/7.

**5. Continuidad y recuperacion.** Planes de continuidad de negocio (BCP) y recuperacion ante desastres (DRP) probados al menos anualmente. DORA exige RPO y RTO definidos para cada funcion critica y pruebas documentadas que demuestren que se cumplen.

**6. Gobernanza.** El organo de direccion (consejo de administracion) es responsable ultimo de la gestion de riesgos TIC. Debe aprobar el marco, supervisar su ejecucion y recibir formacion especifica en riesgos digitales.

{{< cta type="tofu" text="Riskitera cubre los requisitos tecnicos de DORA, ENS y NIS2 con una arquitectura soberana." label="Ver arquitectura" >}}

## Que pruebas de resiliencia operativa son obligatorias?

DORA establece dos niveles de pruebas:

**Pruebas basicas (todas las entidades).** Deben realizarse al menos anualmente sobre los sistemas y aplicaciones TIC criticos:
- Analisis de vulnerabilidades (escaneos automatizados + validacion manual)
- Pruebas de seguridad de red y de perimetro
- Analisis de gaps de seguridad
- Revisiones de codigo fuente (para sistemas desarrollados internamente)
- Pruebas de rendimiento y capacidad
- Pruebas de compatibilidad y migracion
- Pruebas de escenarios de crisis (tabletop exercises)

**Pruebas TLPT (entidades significativas).** Las entidades identificadas como significativas por su autoridad supervisora deben realizar pruebas TLPT al menos cada tres anos. Estas pruebas siguen el marco TIBER-EU (adaptado en Espana como TIBER-ES por el Banco de Espana) y consisten en:
1. Fase de Threat Intelligence: un equipo externo analiza las amenazas reales que enfrenta la entidad
2. Fase de Red Team: un equipo de ataque externo simula las tacticas, tecnicas y procedimientos de los actores de amenaza identificados
3. Fase de Blue Team: se evalua la capacidad de deteccion y respuesta del equipo interno
4. Informe y remediacion: documentacion de hallazgos, plan de remediacion con plazos y seguimiento

Los criterios para determinar si una entidad es "significativa" incluyen: tamano (activos totales), interconexion con el sistema financiero, complejidad de la infraestructura TIC y si presta servicios criticos a otras entidades.

Las pruebas TLPT deben ser ejecutadas por proveedores externos certificados. Los resultados son confidenciales pero deben compartirse con la autoridad supervisora.

## Como gestionar proveedores TIC criticos bajo DORA?

La gestion de terceros es uno de los aspectos mas exigentes de DORA para los bancos, especialmente por la dependencia creciente de servicios cloud, fintech y proveedores de software.

**Clasificacion de proveedores.** Cada entidad debe clasificar sus proveedores TIC segun la criticidad de la funcion que soportan. Un proveedor es critico si su fallo, degradacion o interrupcion pondria en riesgo la continuidad de funciones criticas o importantes del banco.

**Requisitos contractuales minimos.** DORA define clausulas obligatorias en los contratos con proveedores TIC:
- Descripcion completa de servicios con SLAs medibles
- Localizacion de datos y procesamiento (pais y region)
- Disponibilidad, autenticidad, integridad y confidencialidad de datos
- Derecho de acceso, inspeccion y auditoria por parte de la entidad y del regulador
- Notificacion de incidentes que afecten a los servicios prestados
- Plan de continuidad del servicio
- Estrategia de salida con periodos de transicion adecuados
- Obligacion de cooperar en caso de resolucion de la entidad financiera

**Registro de proveedores.** Las entidades deben mantener un registro actualizado de todos los contratos con proveedores TIC y reportarlo anualmente a su autoridad supervisora. Las ESAs mantendran un registro centralizado europeo.

**Riesgo de concentracion.** DORA introduce el concepto de proveedor critico a nivel europeo. Si un proveedor TIC (por ejemplo, un gran hiperescalar cloud) es designado como critico por las ESAs, queda sujeto a supervision directa europea con capacidad sancionadora.

**Estrategia de salida.** Para cada proveedor critico, el banco debe tener documentada una estrategia de salida viable que permita migrar el servicio a otro proveedor o internalizarlo sin interrupcion de funciones criticas.

## Cual es el calendario de implementacion para banca?

DORA fue publicado en el Diario Oficial de la UE en diciembre de 2022 y es de aplicacion desde el 17 de enero de 2025. No hay periodo transitorio: las entidades deben cumplir todos los requisitos desde esa fecha.

Sin embargo, la implementacion practica sigue un calendario mas granular:

**Enero 2025.** Aplicacion completa del Reglamento. Las entidades deben tener operativos: marco de gestion de riesgos TIC, clasificacion de incidentes, registro de proveedores, politicas de continuidad.

**Abril 2025.** Publicacion de los estandares tecnicos regulatorios (RTS) e implementacion tecnica (ITS) finales por las ESAs. Estos detallan los formatos de notificacion de incidentes, las plantillas del registro de proveedores y los criterios de clasificacion de funciones criticas.

**2025-2026.** Periodo de adaptacion practica. Las autoridades supervisoras estan realizando inspecciones de "readiness" y exigiendo planes de remediacion para las entidades que presentan gaps. No es un periodo de gracia formal, pero las primeras sanciones se esperan para entidades con deficiencias graves sin plan de correccion.

**2025-2027.** Primera ronda de pruebas TLPT para entidades significativas. El Banco de Espana esta definiendo el listado de entidades sujetas y la planificacion de pruebas.

**2026 en adelante.** Regimen sancionador plenamente operativo. Revision periodica del marco por la Comision Europea (prevista para enero de 2028).

## Que sanciones aplican a entidades financieras que incumplan?

DORA delega la definicion del regimen sancionador en los Estados miembros, pero establece requisitos minimos. Las autoridades competentes deben tener la potestad de:

- Emitir requerimientos de cese de practicas que vulneren DORA
- Exigir medidas correctivas con plazos vinculantes
- Imponer sanciones administrativas pecuniarias

En Espana, el regimen sancionador se integra en la Ley del Mercado de Valores, la Ley de Ordenacion, Supervision y Solvencia de Entidades de Credito y normativa sectorial aplicable. Las sanciones pueden incluir:

**Para entidades financieras:**
- Multas de hasta el 1% del volumen de negocios medio diario del ano anterior, impuestas de forma diaria hasta que se corrija el incumplimiento
- Amonestaciones publicas identificando a la entidad y la infraccion
- Suspension temporal de actividades

**Para proveedores TIC criticos designados:**
- Multas de hasta el 1% del volumen de negocios medio diario mundial del ano anterior
- Multas coercitivas diarias hasta corregir la situacion
- Publicacion de las resoluciones sancionadoras

**Para miembros del organo de direccion:**
- Responsabilidad personal por incumplimiento de sus obligaciones de gobernanza TIC
- Posibles sanciones administrativas individuales

El impacto reputacional de una sancion publica por incumplimiento de DORA puede ser mas danino que la multa economica, especialmente en un sector donde la confianza es el activo fundamental.


{{< cta type="bofu" text="Agenda una demo tecnica para tu sector y valida la integracion con tu infraestructura." label="Agenda demo" >}}


**Articulos relacionados:**
- [Dora Reglamento Ciberseguridad Financiera](/es/posts/2026/04/dora-reglamento-ciberseguridad-financiera/)

## Preguntas frecuentes

**DORA aplica a fintech y neobancos?**
Si. DORA aplica a todas las entidades financieras reguladas en la UE, incluyendo entidades de pago, entidades de dinero electronico y proveedores de servicios de criptoactivos autorizados bajo MiCA. Las fintech con licencia bancaria o de servicios de pago estan sujetas a los mismos requisitos que los bancos tradicionales.

**Que diferencia hay entre DORA y las guias EBA de riesgos TIC?**
Las guias EBA (EBA/GL/2019/04) eran recomendaciones de "cumplir o explicar" (comply or explain). DORA es un reglamento de aplicacion directa con capacidad sancionadora. DORA absorbe y eleva el nivel de las guias EBA, anadiendo requisitos nuevos como las pruebas TLPT obligatorias y la supervision directa de proveedores criticos.

**Si mi banco ya cumple ENS Alto, cumple tambien DORA?**
No automaticamente. ENS Alto y DORA tienen solapamientos significativos (gestion de riesgos, continuidad, control de accesos), pero DORA introduce requisitos especificos que el ENS no cubre: notificacion de incidentes con plazos determinados, pruebas TLPT, requisitos contractuales detallados para proveedores TIC y registro centralizado de contratos. Un banco que cumple ENS Alto tiene buena base, pero necesita un analisis de gaps especifico para DORA.

**Cuanto cuesta adaptarse a DORA para un banco mediano?**
Depende del nivel de madurez previo. Para un banco mediano espanol con una postura de seguridad razonable (ENS Alto o ISO 27001 certificado), el coste de adaptacion se estima entre 500.000 y 2 millones de euros, incluyendo consultoria, herramientas, personal y pruebas TLPT. Para entidades con menor madurez, puede superar los 5 millones.

**Como se coordinan DORA y NIS2 para bancos?**
DORA es lex specialis frente a NIS2 para el sector financiero. Esto significa que los bancos cumplen NIS2 a traves de DORA: los requisitos de DORA son mas especificos y exigentes que los de NIS2 para este sector. No hay doble cumplimiento, pero la entidad debe poder demostrar ante ambos marcos.
