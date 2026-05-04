---
title: "Como una fintech obtuvo la certificación ISO 27001 y cumplió DORA en 6 meses"
description: "Caso de estudio real: una fintech española de 180 empleados implemento ISO 27001, DORA y monitorización SOC con Riskitera, reduciendo un 65% el tiempo de certificación."
slug: "fintech-grc-compliance"
date: 2026-03-12
lastmod: 2026-04-28
draft: false
company: "NovaPay"
industry: "Fintech"
translationKey: "fintech-case"
tags: ["GRC", "ISO 27001", "Fintech", "DORA", "Compliance"]
author: "David Moya"
---

> **Nota de confidencialidad:** Los nombres de la empresa y las personas mencionadas en este caso de estudio son ficticios para proteger la confidencialidad del cliente. Los datos del proyecto, los plazos, las métricas y los resultados descritos son reales y corresponden a un proyecto completado en 2026.

<!--more-->

## Contexto de la empresa

NovaPay es una fintech española fundada en 2019 que ofrece servicios de procesamiento de pagos y open banking para comercios medianos. Con 180 empleados distribuidos entre Madrid y Lisboa, procesa más de 2 millones de transacciones mensuales para unos 400 comercios en España y Portugal.

Hasta principios de 2026, NovaPay gestionaba la seguridad de forma reactiva: un equipo de tres personas (un responsable de seguridad y dos ingenieros de infraestructura) cubria tanto las operaciones de TI como la ciberseguridad, sin procesos formalizados ni herramientas específicas de GRC.

## El desafio: cumplir con dos normativas a la vez y en plazo

En enero de 2026, NovaPay se enfrento a una confluencia de obligaciones regulatorias:

**ISO 27001.** Su principal partner bancario (una entidad de credito española) comunico que a partir de septiembre de 2026 exigiria la certificación ISO 27001 a todos los proveedores tecnológicos que procesaran datos de tarjetas. Sin la certificación, NovaPay perderia el contrato que representaba el 35% de su facturación.

**DORA (Reglamento de Resiliencia Operativa Digital).** Como proveedor crítico de servicios TIC para entidades financieras, NovaPay entró en el ámbito del Reglamento DORA. Esto implicaba demostrar capacidades de gestión de riesgos TIC, notificación de incidentes, pruebas de resiliencia y gestión de terceros que no tenian documentadas.

**Plazo.** Disponian de 8 meses como máximo. La media del sector para una certificación ISO 27001 desde cero es de 12 a 18 meses según los datos del Foro Internacional de Certificación Acreditada (IAF).

**Equipo.** Tres personas dedicadas a seguridad, sin experiencia previa en procesos de certificación ni en gestión formal de riesgos. El presupuesto asignado era de 45.000 euros para consultoría y herramientas, excluyendo la auditoría de certificación.

### Los problemas concretos que encontramos

Cuando realizamos la evaluación inicial con NovaPay, identificamos seis brechas críticas:

1. **Sin política de seguridad aprobada.** Existian documentos internos de configuración, pero nada que cumpliera los requisitos formales de ISO 27001 cláusula 5.2 ni del artículo 6 de DORA.

2. **Análisis de riesgos inexistente.** Las decisiones de seguridad se tomaban por intuición del equipo técnico. No habia inventario de activos de información, ni identificación formal de amenazas, ni criterios de aceptación de riesgo aprobados por la dirección.

3. **Herramientas aisladas.** Usaban Jira para tickets de seguridad, hojas de calculo para el registro de incidentes, un directorio compartido para documentos de políticas y correo electrónico para la comunicación de alertas. No habia trazabilidad entre controles, evidencias y riesgos.

4. **Sin monitorización continua.** No tenian SIEM ni capacidad de detección centralizada. Los logs se almacenaban en los propios servidores sin correlación ni alertas automatizadas. El tiempo medio de detección de incidentes (MTTD) era desconocido.

5. **Gestión de proveedores informal.** Trabajaban con 12 proveedores tecnológicos (cloud, pasarela de pagos, CDN, antifraude) sin evaluaciones de seguridad documentadas. DORA exige un registro de proveedores TIC críticos con evaluaciones periódicas.

6. **Sin programa de concienciación.** El personal no habia recibido formación en ciberseguridad. Tanto ISO 27001 (Anexo A, control A.6.3) como DORA (artículo 13.6) lo exigen expresamente.

## La solución: implementación con Riskitera

El proyecto se estructuro en tres fases de dos meses cada una, con revisiones quincenales de progreso.

### Fase 1 (semanas 1 a 8): Fundamentos

**Evaluación de riesgos con MAGERIT.** Utilizamos el modulo de análisis de riesgos de Riskitera para realizar el inventario de activos (identificamos 847 activos de información), mapear amenazas del catálogo MAGERIT y calcular el riesgo inherente. Lo que normalmente lleva 6 a 8 semanas con hojas de calculo, se completo en 3 semanas gracias a la automatización del catálogo de amenazas y la generación automática de valoraciones iniciales basadas en el tipo de activo.

El resultado fue un registro de riesgos con 124 escenarios de riesgo valorados, 23 de ellos por encima del umbral de aceptación definido por la dirección.

**Declaración de aplicabilidad.** Riskitera genero automáticamente la declaración de aplicabilidad (SoA) mapeando los 93 controles del Anexo A de ISO 27001:2022 contra los riesgos identificados, indicando cuales eran aplicables, cuales no y la justificación. El equipo de NovaPay reviso y ajusto el documento en 2 días en lugar de las 2 a 3 semanas habituales.

**Marco documental.** Generamos el esqueleto de las 12 políticas requeridas (seguridad de la información, control de acceso, clasificación de la información, gestión de incidentes, continuidad de negocio, criptografia, gestión de proveedores, seguridad en RRHH, seguridad física, desarrollo seguro, gestión de activos y cumplimiento). El equipo de NovaPay las adapto a su contexto con el soporte de plantillas y guías integradas en la plataforma.

### Fase 2 (semanas 9 a 16): Implementación de controles

**Mapeo dual ISO 27001 + DORA.** Uno de los retos específicos del proyecto era que NovaPay necesitaba cumplir con dos marcos simultaneamente. Riskitera mantiene una matriz de correspondencia entre los controles de ISO 27001 Anexo A y los requisitos de los artículos 5 a 15 de DORA. Esto permitio identificar que el 68% de los controles tenian cobertura cruzada: implementar un control para ISO 27001 satisfacia simultaneamente un requisito DORA. El equipo pudo priorizar estos controles de doble cobertura y evitar duplicación de esfuerzos.

**Evidence Vault.** Configuramos la recopilación automática de evidencias conectando las fuentes de datos de NovaPay: AWS CloudTrail para logs de infraestructura, GitHub para cambios de código, Azure AD para gestión de accesos, y el sistema de ticketing para gestión de cambios e incidentes. Cada evidencia se almacena con hash SHA-256 y timestamp verificable, formando una cadena de custodia auditable.

Al final de esta fase, el 78% de las evidencias requeridas se recopilaban automáticamente sin intervención manual.

**Despliegue de monitorización.** Integramos las fuentes de logs críticas (firewalls, WAF, sistemas de autenticación, bases de datos de transacciones) en el modulo de correlación de Riskitera. Definimos 35 reglas de detección iniciales mapeadas a MITRE ATT&CK, priorizando las técnicas más relevantes para el sector fintech: acceso con credenciales robadas (T1078), movimiento lateral (T1021), exfiltración por canal C2 (T1041) y manipulación de datos financieros.

### Fase 3 (semanas 17 a 24): Afinado, formación y auditoría

**Programa de concienciación.** Se implemento un programa de formación para los 180 empleados que incluia un modulo online de 45 minutos sobre fundamentos de ciberseguridad, simulaciones de phishing mensuales (la tasa de clic bajo del 34% al 8% en tres meses) y formación específica para el equipo de desarrollo sobre OWASP Top 10 y desarrollo seguro.

**Registro de proveedores TIC.** Para cumplir con DORA, catalogamos los 12 proveedores tecnológicos de NovaPay, clasificamos 4 como críticos (AWS, la pasarela de pagos, el proveedor de antifraude y el CDN) y documentamos las evaluaciones de seguridad, los SLA y los planes de contingencia para cada uno.

**Simulacro de auditoría interna.** Antes de la auditoría de certificación, realizamos una auditoría interna completa utilizando los checklists de Riskitera alineados con ISO 19011. Se identificaron 7 no conformidades menores que se corrigieron en 10 días.

**Auditoría de certificación.** La auditoría externa (Fase 1 + Fase 2) se completo en la semana 24 del proyecto. El auditor destaco positivamente la trazabilidad completa entre riesgos, controles y evidencias, y la capacidad de la plataforma para generar informes de cumplimiento en tiempo real durante la propia auditoría.

## Resultados

| Metrica | Antes | Después | Mejora |
|---|---|---|---|
| Tiempo hasta certificación ISO 27001 | N/A | 6 meses | 50-65% menos que la media del sector |
| Controles ISO 27001 Anexo A documentados | 0/93 | 93/93 | 100% cobertura |
| Requisitos DORA cubiertos | 0% | 87% | Pendiente: pruebas TLPT avanzadas |
| Tiempo de recopilación de evidencias | ~40 h/mes (manual) | ~6 h/mes | 85% reducción |
| MTTD (tiempo medio de detección) | Desconocido | 4.2 horas | Medible por primera vez |
| Tasa de clic en simulaciones de phishing | 34% | 8% | 76% reducción |
| Proveedores TIC evaluados formalmente | 0/12 | 12/12 | 100% cobertura |
| No conformidades en auditoría de certificación | N/A | 0 mayores, 2 menores | Por debajo de la media del sector |

### Impacto en el negocio

El resultado más relevante para NovaPay no fue la certificación en si, sino su impacto comercial:

- **Contrato bancario renovado** por tres años, con un incremento del 15% en volumen procesado.
- **Dos nuevos clientes en Portugal** que exigian ISO 27001 como requisito previo a la contratación.
- **Reducción del coste del seguro cibernetico** en un 22% en la renovación anual, gracias a la documentación de controles y la monitorización continua.
- **Base sólida para NIS2.** Con el SGSI implementado, NovaPay estima que la adaptación a los requisitos adicionales de NIS2 (cuando se complete la transposición en España) requerirá un esfuerzo incremental de 4 a 6 semanas, en lugar de un proyecto completo desde cero.

## Lecciones aprendidas

**El apoyo de la dirección fue determinante.** El CEO de NovaPay asistio a la reunion de kick-off y a las revisiones mensuales. Cuando el equipo de desarrollo pidio aplazar la formación en desarrollo seguro por presión de roadmap, la dirección intervino para mantener el calendario. Sin ese respaldo, el proyecto habría sufrido retrasos.

**El mapeo dual ISO 27001 + DORA ahorro un 30% de esfuerzo.** Abordar ambos marcos como proyectos independientes habría duplicado gran parte del trabajo documental y de implementación de controles. La matriz de correspondencia de Riskitera fue clave para evitar esa duplicación.

**Las evidencias automatizadas cambiaron la percepción del equipo.** El mayor escepticismo inicial del equipo de NovaPay era que el SGSI se convertiria en un "ejercicio de papeles" que consumiria tiempo sin aportar valor operativo. Cuando vieron que el 78% de las evidencias se recopilaban automáticamente y que la plataforma generaba los informes de revisión de la dirección con datos reales, la percepción cambio: el sistema no era burocracia, sino visibilidad.

**La monitorización continua detecto un incidente real.** Durante la fase 3 del proyecto, las reglas de detección identificaron un intento de acceso no autorizado a una API interna desde una IP asociada a un proxy comercial. El equipo lo contuvo en 90 minutos. Antes de la implementación, este tipo de actividad habría pasado completamente desapercibida.
