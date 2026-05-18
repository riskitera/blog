---
title: "Guía completa DORA para entidades financieras: 12 requisitos técnicos"
description: "Desglose técnico de los 12 requisitos principales de DORA para entidades financieras: gestión de riesgos TIC, reporting, pruebas de resiliencia, terceros y compartición de información."
slug: "guia-dora-entidades-financieras-requisitos"
date: 2026-07-16
publishDate: 2026-07-16
lastmod: 2026-07-16
draft: false
tags: ["DORA", "Banca", "Compliance"]
categories: ["Compliance"]
author: "David Moya"
keyword: "guia DORA entidades financieras"
funnel: "mofu"
---

Desglose técnico de los 12 requisitos principales de DORA para entidades financieras: gestión de riesgos TIC, reporting, pruebas de resiliencia, terceros y compartición de información.

<!--more-->

{{< key-takeaways >}}
- DORA establece 12 requisitos técnicos agrupados en 5 pilares que afectan a bancos, aseguradoras, gestoras de fondos y proveedores TIC críticos en la Unión Europea.
- La gestión de riesgos TIC (Artículos 6 a 16) exige un marco de gobernanza con responsabilidad directa del órgano de dirección y revisión anual obligatoria.
- El reporting de incidentes (Artículos 17 a 23) obliga a clasificar y notificar incidentes graves a las autoridades competentes en plazos de 4 horas, 72 horas y 1 mes.
- Las pruebas de resiliencia digital (Artículos 24 a 27) incluyen tests básicos anuales y pruebas TLPT avanzadas cada tres años para entidades significativas.
- La gestión de riesgo de terceros (Artículos 28 a 44) impone un marco de supervisión directa de la UE sobre proveedores TIC críticos, con poder sancionador.
{{< /key-takeaways >}}

## ¿Qué es DORA y por qué importa a las entidades financieras?

El [Reglamento (UE) 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554), conocido como DORA (Digital Operational Resilience Act), es la primera normativa europea que establece requisitos uniformes de resiliencia operativa digital para el sector financiero. Entró en vigor en enero de 2023 y su aplicación es obligatoria desde el 17 de enero de 2025.

A diferencia de directivas anteriores que dejaban margen de transposición a cada estado miembro, DORA es un reglamento de aplicación directa. Esto significa que todas las entidades financieras de la UE (bancos, aseguradoras, empresas de inversión, gestoras de fondos, entidades de pago, proveedores de servicios de criptoactivos y otros 20 tipos de entidades) deben cumplir exactamente los mismos requisitos.

El contexto es claro: la dependencia del sector financiero respecto a la tecnología ha crecido exponencialmente. Un fallo en un proveedor cloud, un ciberataque a un sistema de pagos o una interrupción prolongada de servicios TIC puede generar un efecto cascada con impacto sistémico. DORA aborda esta realidad con un enfoque integral que va más allá de la ciberseguridad tradicional.

### Relación con NIS2 e ISO 27001

DORA no existe en el vacío. La [Directiva NIS2 (UE) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555) establece requisitos de ciberseguridad para sectores esenciales e importantes, incluido el financiero. Sin embargo, DORA prevalece como lex specialis para el sector financiero: cuando ambas normas cubren el mismo aspecto, se aplica DORA.

[ISO 27001](https://www.iso.org/standard/27001) sigue siendo un marco de referencia válido para la implementación práctica, pero no sustituye el cumplimiento de DORA. Muchas entidades financieras que ya tienen certificación ISO 27001 descubren que necesitan reforzar áreas específicas, como la gestión de riesgo de terceros TIC o las pruebas TLPT.

### Los 5 pilares de DORA

DORA se estructura en torno a 5 pilares fundamentales, de los que derivan los 12 requisitos técnicos que analizamos en esta guía:

1. **Gestión de riesgos TIC** (Artículos 6 a 16)
2. **Gestión, clasificación y notificación de incidentes TIC** (Artículos 17 a 23)
3. **Pruebas de resiliencia operativa digital** (Artículos 24 a 27)
4. **Gestión de riesgo de terceros proveedores TIC** (Artículos 28 a 44)
5. **Acuerdos de intercambio de información** (Artículo 45)

Vamos a desglosar cada uno con sus requisitos técnicos concretos.

## Pilar 1: Gestión de riesgos TIC (Artículos 6 a 16)

Este pilar es la columna vertebral de DORA. Define el marco de gobierno y los procesos que cada entidad financiera debe establecer para identificar, proteger, detectar, responder y recuperarse de riesgos relacionados con las TIC.

### Requisito 1: Marco de gobernanza TIC (Artículo 5)

El órgano de dirección de la entidad financiera tiene la responsabilidad última y directa de la gestión de riesgos TIC. No se trata de delegar en el CISO y olvidarse. DORA exige que el consejo de administración:

- Defina, apruebe y supervise la implementación de la estrategia de resiliencia operativa digital.
- Establezca funciones y responsabilidades claras para todas las cuestiones relacionadas con las TIC.
- Asigne presupuesto suficiente para la formación en resiliencia digital, tanto para empleados como para los propios miembros del órgano de dirección.
- Revise y apruebe la política de continuidad de negocio TIC al menos una vez al año.

En la práctica, esto implica que la ciberseguridad deja de ser un tema exclusivo del área técnica. Los directivos deben demostrar conocimiento y participación activa. Las actas del consejo deben reflejar que se han revisado los informes de riesgo TIC, los resultados de las pruebas de resiliencia y el estado de los proveedores críticos.

### Requisito 2: Marco de gestión de riesgos TIC (Artículos 6 a 9)

Toda entidad financiera debe documentar y mantener un marco de gestión de riesgos TIC sólido que incluya:

- **Identificación**: inventario completo de todos los activos TIC (hardware, software, datos, procesos), con clasificación por criticidad y mapeo de dependencias. Cada activo debe tener un propietario asignado.
- **Protección y prevención**: políticas de seguridad que cubran control de acceso, cifrado, segmentación de redes, gestión de parches, hardening de sistemas y formación continua del personal.
- **Detección**: mecanismos para identificar anomalías y actividad sospechosa en tiempo real. Esto incluye SIEM, correlación de eventos, monitorización de endpoints y análisis de comportamiento.
- **Respuesta y recuperación**: planes documentados y probados para la contención, erradicación y recuperación ante incidentes TIC, con tiempos de recuperación (RTO) y puntos de recuperación (RPO) definidos.

Un ejemplo práctico: un banco mediano necesita documentar que su sistema de banca online depende de tres proveedores cloud, dos pasarelas de pago y un proveedor de autenticación. Debe tener mapeadas las dependencias cruzadas, de forma que si el proveedor de autenticación cae, el plan de recuperación contemple alternativas específicas con tiempos concretos.

### Requisito 3: Estrategia de resiliencia operativa digital (Artículo 6.8)

Más allá del marco de gestión, DORA exige una estrategia de resiliencia que debe:

- Explicar como el marco de gestión de riesgos TIC apoya la estrategia de negocio.
- Establecer el nivel de tolerancia al riesgo TIC aprobado por el órgano de dirección.
- Incluir objetivos claros de seguridad de la información, con KPIs medibles.
- Describir la arquitectura TIC objetivo y como la entidad planea evolucionar hacia ella.
- Definir mecanismos para detectar incidentes, responder y recuperarse de ellos.

Esta estrategia no es un documento estático. Debe revisarse al menos anualmente o tras incidentes significativos, cambios importantes en la arquitectura TIC o resultados relevantes de pruebas de resiliencia.

### Requisito 4: Políticas de seguridad TIC (Artículos 9 a 16)

DORA detalla requisitos específicos para áreas concretas de la seguridad:

- **Gestión de identidades y acceso** (Artículo 9.4b): principio de mínimo privilegio, revisión periódica de permisos, autenticación multifactor para sistemas críticos.
- **Gestión de cambios TIC** (Artículo 9.4e): procedimientos formales para cambios en sistemas, con evaluación de impacto, pruebas previas y capacidad de rollback.
- **Cifrado** (Artículo 10): política de cifrado en tránsito y en reposo adaptada a la clasificación de los datos.
- **Seguridad de redes** (Artículo 11): segmentación adecuada, monitorización del tráfico, protección perimetral y gestión de conexiones remotas.
- **Gestión de la continuidad de negocio TIC** (Artículos 11 y 12): planes de continuidad probados, sitios de recuperación, comunicaciones de crisis y planes de comunicación externa.
- **Aprendizaje y evolución** (Artículo 13): las entidades deben aprender de incidentes propios y ajenos, integrando las lecciones en la mejora continua del marco.

## Pilar 2: Gestión, clasificación y notificación de incidentes TIC (Artículos 17 a 23)

Este pilar establece un proceso armonizado para toda la UE en la gestión de incidentes relacionados con las TIC. El objetivo es doble: asegurar que las entidades gestionan los incidentes de forma eficaz y que las autoridades supervisoras tienen visibilidad en tiempo útil.

### Requisito 5: Proceso de gestión de incidentes (Artículo 17)

Las entidades financieras deben establecer un proceso de gestión de incidentes TIC que incluya:

- Indicadores de alerta temprana para la detección rápida de incidentes.
- Procedimientos para identificar, registrar, clasificar y notificar incidentes TIC.
- Roles y responsabilidades claros, incluida la activación de planes de respuesta.
- Planes de comunicación interna (incluida escalación a alta dirección) y externa (incluidos clientes afectados).
- Procedimientos para la preservación de evidencias forenses.
- Análisis post-incidente obligatorio para incidentes graves, con identificación de causas raíz y acciones correctivas.

### Requisito 6: Clasificación de incidentes (Artículo 18)

DORA establece criterios armonizados para clasificar los incidentes TIC. Los criterios principales son:

| Criterio | Descripción |
|---|---|
| Número de clientes afectados | Umbrales absolutos y relativos respecto a la base total |
| Duración del incidente | Tiempo desde detección hasta resolución completa |
| Extensión geográfica | Número de estados miembros afectados |
| Pérdidas de datos | Volumen y criticidad de los datos comprometidos |
| Criticidad de los servicios | Impacto en servicios críticos o funciones esenciales |
| Impacto económico | Costes directos e indirectos estimados |

Un incidente se clasifica como **grave** cuando supera los umbrales establecidos en al menos uno de estos criterios. Las Autoridades Europeas de Supervisión (ESAs) han publicado normas técnicas de regulación (RTS) que detallan los umbrales concretos.

### Requisito 7: Notificación de incidentes graves (Artículos 19 a 23)

El régimen de notificación es uno de los aspectos más operativos de DORA. Las entidades deben enviar tres tipos de notificaciones a su autoridad competente:

1. **Notificación inicial**: dentro de las **4 horas** desde la clasificación del incidente como grave (y no más de 24 horas desde la detección). Debe incluir información básica sobre el incidente, el impacto estimado y las primeras medidas adoptadas.
2. **Notificación intermedia**: dentro de las **72 horas** desde la notificación inicial. Actualiza la información con datos más concretos sobre el alcance, la causa raíz identificada y las acciones de remediación en curso.
3. **Informe final**: dentro de **1 mes** desde el envío de la notificación intermedia. Incluye el análisis completo de causas raíz, el impacto real, las medidas correctivas implementadas y las lecciones aprendidas.

Para ilustrar el impacto operativo: si una entidad detecta un ataque de ransomware a las 10:00 del lunes, debe clasificarlo antes de las 10:00 del martes, enviar la notificación inicial antes de las 14:00 del martes (si clasifica a las 10:00), la notificación intermedia antes del jueves, y el informe final antes de un mes después. Estos plazos son exigentes y requieren procesos bien engrasados.

Además, DORA contempla la posibilidad de que las entidades notifiquen voluntariamente ciberamenazas significativas, aunque no hayan materializado un incidente. Esto alimenta el sistema de inteligencia colectiva del sector.

{{< cta type="tofu" text="Riskitera cubre los requisitos técnicos de DORA, ENS y NIS2 con una arquitectura soberana. Automatiza la clasificación de incidentes y genera notificaciones conformes a los plazos regulatorios." label="Ver arquitectura" >}}

## Pilar 3: Pruebas de resiliencia operativa digital (Artículos 24 a 27)

Cumplir DORA no es solo tener documentación y políticas. Las entidades deben demostrar que sus sistemas y procesos funcionan bajo presión real. Este pilar establece un programa de pruebas obligatorio con dos niveles de exigencia.

### Requisito 8: Programa general de pruebas (Artículo 24 y 25)

Todas las entidades financieras cubiertas por DORA deben establecer un programa de pruebas de resiliencia operativa digital. Este programa debe:

- Formar parte integral del marco de gestión de riesgos TIC.
- Cubrir todos los sistemas, procesos y personal que soportan funciones críticas o importantes.
- Ejecutarse al menos **una vez al año** para los sistemas y aplicaciones críticos.
- Ser proporcional al tamaño de la entidad y a la naturaleza de sus servicios.

Las pruebas básicas que DORA contempla incluyen:

- **Evaluaciones de vulnerabilidades**: escaneos regulares de todos los sistemas TIC, con remediación priorizada según criticidad.
- **Pruebas de rendimiento**: verificación de que los sistemas soportan los volúmenes de operación esperados, incluidos picos de demanda.
- **Pruebas de penetración**: tests ofensivos que simulan ataques reales contra la infraestructura, las aplicaciones y las interfaces.
- **Pruebas de código fuente abierto**: revisión de componentes open source utilizados, incluyendo análisis de vulnerabilidades conocidas (CVE).
- **Pruebas de compatibilidad**: verificación de que los cambios en sistemas no afectan la interoperabilidad.
- **Pruebas de continuidad de negocio**: simulacros de recuperación ante desastres, incluida la activación de sitios secundarios.
- **Pruebas de escenarios**: simulación de escenarios de amenazas realistas basados en inteligencia de amenazas actual.

### Requisito 9: Pruebas avanzadas TLPT (Artículos 26 y 27)

Las pruebas TLPT (Threat-Led Penetration Testing) son el nivel más exigente del programa de pruebas de DORA. Están inspiradas en el marco TIBER-EU del Banco Central Europeo, pero ahora tienen base legal vinculante.

Las TLPT son obligatorias para entidades **identificadas por las autoridades competentes** como significativas en términos de riesgo sistemico. Los criterios incluyen tamaño, cuota de mercado, interconexion con el sistema financiero y naturaleza de los servicios prestados.

Caracteristicas clave de las TLPT:

- Se ejecutan al menos cada **3 años**.
- Deben cubrir varias o todas las funciones críticas o importantes de la entidad.
- Se realizan en el entorno de **producción en vivo**.
- Deben ser ejecutadas por **testers externos** independientes, certificados y con experiencia demostrable.
- El equipo de inteligencia de amenazas (threat intelligence) que define los escenarios debe ser independiente del equipo de testeo (red team).
- La entidad debe involucrar a un equipo interno de defensa (blue team) que no sepa que las pruebas se están realizando (para medir la capacidad real de detección).

Un aspecto importante: los proveedores TIC críticos de la entidad pueden verse incluidos en el alcance de las TLPT. Esto significa que una entidad financiera puede necesitar coordinar pruebas en vivo que afecten a la infraestructura de sus proveedores cloud, con las complejidades logísticas y contractuales que ello implica.

Al finalizar las TLPT, la entidad debe presentar a la autoridad competente un informe resumido con los hallazgos, las evidencias de remediación y la certificación del tester externo.

## Pilar 4: Gestión de riesgo de terceros proveedores TIC (Artículos 28 a 44)

Este pilar es probablemente el más disruptivo de DORA. Reconoce que la resiliencia de una entidad financiera depende directamente de la resiliencia de sus proveedores tecnológicos, y establece un marco de supervisión sin precedentes.

### Requisito 10: Principios generales de gestión de terceros TIC (Artículos 28 a 30)

Las entidades financieras deben gestionar el riesgo de terceros proveedores TIC como parte integral de su marco de gestión de riesgos. Esto implica:

- **Registro de proveedores**: mantener un registro actualizado de todos los acuerdos contractuales con proveedores TIC, clasificados por criticidad. Este registro debe estar disponible para las autoridades competentes.
- **Evaluación previa a la contratación**: antes de contratar un proveedor TIC para funciones críticas, realizar una evaluación de riesgos que incluya capacidad técnica, situación financiera, concentración de riesgo y ubicación geográfica del procesamiento de datos.
- **Estrategia de salida**: cada acuerdo con un proveedor crítico debe contemplar un plan de salida viable, con periodos de transición adecuados y sin degradación del servicio.
- **Concentración de riesgo**: evitar la dependencia excesiva de un único proveedor TIC para funciones críticas. Las autoridades supervisoras evaluaran el riesgo de concentración a nivel de mercado.

Un ejemplo concreto: si un banco utiliza AWS para su core bancario, Azure para el sistema de pagos y Google Cloud para analítica, DORA exige que documente las dependencias, los riesgos de concentración (tres hyperscalers estadounidenses), las alternativas viables y los planes de salida para cada uno.

### Requisito 11: Clausulas contractuales obligatorias (Artículos 30 a 32)

DORA establece un listado mínimo de cláusulas que deben incluirse en los contratos con proveedores TIC que soporten funciones críticas o importantes:

- Descripción clara y completa de los servicios prestados, incluidos niveles de servicio (SLA) cuantificables.
- Ubicación del procesamiento de datos (incluidos centros de datos y países).
- Obligación del proveedor de asistir en caso de incidente TIC.
- Derechos de acceso, inspección y auditoría por parte de la entidad y de las autoridades supervisoras.
- Garantias de disponibilidad, autenticidad, integridad y confidencialidad de los datos.
- Obligación de cooperar con las autoridades de supervisión del marco de oversight.
- Clausulas de terminación y planes de salida con periodos de transición adecuados.
- Obligación de notificar cualquier subcontratación que afecte a funciones críticas.

Estas cláusulas no son negociables. Si un proveedor cloud se niega a incluir derechos de auditoría o a especificar la ubicación del procesamiento, la entidad financiera no puede contratarlo para funciones críticas. Esto ha forzado a los grandes proveedores tecnológicos a adaptar sus condiciones contractuales para el mercado financiero europeo.

### Requisito 12: Marco de supervisión de proveedores TIC críticos (Artículos 31 a 44)

Esta es la innovación más significativa de DORA: un marco de supervisión directa de la UE sobre proveedores TIC designados como críticos. Las ESAs (EBA, EIOPA y ESMA), junto con la Comisión Europea, designan que proveedores son críticos basándose en:

- El carácter sistemico del proveedor para el sector financiero.
- El grado de dependencia de las entidades financieras respecto a dicho proveedor.
- La sustituibilidad del proveedor.

Para cada proveedor crítico, se designa un **supervisor principal** (Lead Overseer) entre las tres ESAs. Este supervisor tiene poderes significativos:

- Solicitar información y documentación completa.
- Realizar inspecciones in situ y remotas.
- Emitir recomendaciones vinculantes.
- Imponer multas coercitivas de hasta el 1% de la facturación diaria global del proveedor en caso de incumplimiento.

Este marco es especialmente relevante para los grandes hyperscalers (AWS, Azure, Google Cloud), los proveedores SaaS financieros y las empresas de infraestructura crítica (telecomunicaciones, centros de datos). Por primera vez, la UE puede supervisar directamente a proveedores tecnológicos que, aunque no sean entidades financieras, son críticos para la estabilidad del sistema financiero.

## Pilar 5: Acuerdos de intercambio de información (Artículo 45)

### Compartición de información sobre ciberamenazas

DORA fomenta (sin obligar) el intercambio de información sobre ciberamenazas entre entidades financieras. El Artículo 45 establece que las entidades pueden participar en acuerdos de intercambio de información siempre que:

- La participación sea voluntaria.
- Se protejan los datos personales y la información confidencial de negocio.
- Los acuerdos se notifiquen a las autoridades competentes.
- Se compartan indicadores de compromiso (IoC), tácticas, técnicas y procedimientos (TTP), alertas de ciberseguridad e información sobre herramientas de análisis.

Aunque este pilar es voluntario, las autoridades supervisoras lo valoran positivamente. Las entidades que participan en ISACs (Information Sharing and Analysis Centers) sectoriales están mejor posicionadas para cumplir con DORA, ya que demuestran un enfoque proactivo hacia la resiliencia.

El intercambio de información es especialmente valioso en el sector financiero por la naturaleza interconectada de las operaciones. Un ataque dirigido a una entidad puede ser precursor de campañas más amplias. Compartir inteligencia de amenazas permite al sector anticiparse colectivamente.

## Plazos y calendario de cumplimiento

DORA establece un calendario claro, con la mayoría de obligaciones ya aplicables:

| Hito | Fecha |
|---|---|
| Entrada en vigor del Reglamento | 16 enero 2023 |
| Aplicación obligatoria | 17 enero 2025 |
| Publicación de RTS/ITS por las ESAs | A lo largo de 2024-2025 |
| Primera ronda de designación de proveedores críticos | 2025 |
| Primera ronda de TLPT (entidades significativas) | Antes de enero 2028 |

Las entidades que aún no han completado su adaptación deben priorizar las áreas de mayor riesgo: la gestión de terceros TIC (por la complejidad contractual), el proceso de notificación de incidentes (por los plazos estrictos) y el marco de gobernanza (por la responsabilidad directa del órgano de dirección).

## Guía práctica de implementación: por donde empezar

Para las entidades que necesitan estructurar su programa de cumplimiento, esta es una hoja de ruta pragmatica:

### Fase 1: Diagnostico (semanas 1 a 4)

- Realizar un gap analysis entre la situación actual y los 12 requisitos de DORA.
- Identificar las funciones críticas e importantes de la entidad.
- Inventariar todos los proveedores TIC y clasificarlos por criticidad.
- Evaluar la madurez del proceso de gestión de incidentes actual.

### Fase 2: Diseno del marco (semanas 5 a 12)

- Establecer la gobernanza: roles, responsabilidades, comites, líneas de reporte al órgano de dirección.
- Diseñar el marco de gestión de riesgos TIC alineado con los Artículos 6 a 16.
- Definir el proceso de clasificación y notificación de incidentes conforme a los Artículos 17 a 23.
- Revisar y actualizar todos los contratos con proveedores TIC críticos.

### Fase 3: Implementación (semanas 13 a 24)

- Desplegar las políticas y procedimientos aprobados.
- Implementar controles técnicos pendientes (cifrado, segmentación, monitorización).
- Formar al personal, incluido el órgano de dirección.
- Establecer el programa de pruebas de resiliencia.

### Fase 4: Validación y mejora continua (semanas 25 en adelante)

- Ejecutar la primera ronda de pruebas de resiliencia.
- Realizar un simulacro de notificación de incidentes.
- Auditar el cumplimiento del marco y documentar las evidencias.
- Planificar la preparación para TLPT si la entidad es designada como significativa.

{{< cta type="bofu" text="Agenda una demo técnica para tu sector y valida la integración con tu infraestructura. Riskitera automatiza el cumplimiento de DORA con IA soberana y alojamiento 100% en la UE." label="Agenda demo" >}}

## Sanciones por incumplimiento

DORA no establece un régimen sancionador propio con cuantías fijas (a diferencia de GDPR). En su lugar, delega en las autoridades competentes nacionales la imposición de sanciones administrativas y medidas correctivas. Sin embargo, las multas coercitivas para proveedores TIC críticos si están definidas a nivel europeo: hasta el 1% de la facturación diaria global media del ejercicio anterior, por cada día de incumplimiento.

En la práctica, las autoridades nacionales (como el Banco de España o la CNMV) pueden imponer sanciones significativas bajo sus marcos regulatorios existentes, reforzados por DORA. Además, el incumplimiento de DORA puede ser un agravante en procedimientos sancionadores relacionados con otros marcos (como MiFID II o Solvencia II).

**Artículos relacionados:**
- [Dora Reglamento Ciberseguridad Financiera](/es/posts/2026/04/dora-reglamento-ciberseguridad-financiera/)

## Preguntas frecuentes

### ¿Qué entidades financieras están obligadas a cumplir DORA?

DORA se aplica a más de 20 tipos de entidades financieras: entidades de crédito, empresas de inversión, entidades de pago, entidades de dinero electrónico, empresas de seguros y reaseguros, fondos de pensiones de empleo, proveedores de servicios de criptoactivos, depositarios centrales de valores, sociedades de gestión, agencias de calificación crediticia y, de forma relevante, proveedores TIC terceros que prestan servicios a cualquiera de estos. Las microempresas tienen un régimen simplificado, pero no están exentas.

### ¿En qué se diferencia DORA de NIS2 para el sector financiero?

NIS2 establece requisitos generales de ciberseguridad para sectores esenciales e importantes, mientras que DORA es el régimen específico (lex specialis) para el sector financiero. Cuando ambas normas se solapan, se aplica DORA. Las diferencias principales son: DORA tiene requisitos más detallados sobre gestión de terceros TIC, establece un marco de supervisión directa sobre proveedores críticos (que NIS2 no contempla) e impone pruebas TLPT obligatorias. NIS2, por su parte, tiene un alcance sectorial más amplio y sus propios mecanismos de notificación de incidentes.

### ¿Qué pasa si un proveedor cloud se niega a incluir las cláusulas contractuales que exige DORA?

La entidad financiera no puede utilizar ese proveedor para funciones críticas o importantes si no cumple con los requisitos contractuales del Artículo 30. En la práctica, los principales proveedores cloud (AWS, Azure, Google Cloud) ya han adaptado sus condiciones contractuales para el mercado financiero europeo. Si un proveedor se niega, la entidad debe buscar alternativas o reclasificar la función como no crítica (si esto es justificable). La autoridad supervisora puede cuestionar cualquier clasificación que considere artificialmente baja.

### ¿Es obligatorio realizar pruebas TLPT para todas las entidades?

No. Las pruebas TLPT solo son obligatorias para entidades que las autoridades competentes identifiquen como significativas en términos de riesgo sistemico. Los criterios incluyen tamaño, cuota de mercado, interconexion con el sistema financiero y naturaleza de los servicios. Tipicamente, esto incluye a los grandes bancos, aseguradoras sistemicas y plataformas de mercados. Las demás entidades deben realizar pruebas de resiliencia básicas (evaluaciones de vulnerabilidades, pruebas de penetración, simulacros de continuidad), pero no TLPT.

### ¿Cuánto tiempo lleva implementar el cumplimiento completo de DORA?

El tiempo de implementación depende de la madurez de la entidad. Una entidad con certificación ISO 27001 y procesos de gestión de riesgos TIC consolidados puede necesitar entre 6 y 12 meses para cubrir los gaps específicos de DORA (especialmente en gestión de terceros y preparación para TLPT). Para entidades con menor madurez, el proceso puede extenderse a 12 o 18 meses. La clave es empezar con un gap analysis riguroso que permita priorizar las áreas de mayor riesgo y mayor distancia respecto a los requisitos.
