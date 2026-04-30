---
title: "Como una fintech obtuvo la certificacion ISO 27001 y cumplio DORA en 6 meses"
description: "Caso de estudio real: una fintech espanola de 180 empleados implemento ISO 27001, DORA y monitorizacion SOC con Riskitera, reduciendo un 65% el tiempo de certificacion."
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

> **Nota de confidencialidad:** Los nombres de la empresa y las personas mencionadas en este caso de estudio son ficticios para proteger la confidencialidad del cliente. Los datos del proyecto, los plazos, las metricas y los resultados descritos son reales y corresponden a un proyecto completado en 2026.

<!--more-->

## Contexto de la empresa

NovaPay es una fintech espanola fundada en 2019 que ofrece servicios de procesamiento de pagos y open banking para comercios medianos. Con 180 empleados distribuidos entre Madrid y Lisboa, procesa mas de 2 millones de transacciones mensuales para unos 400 comercios en Espana y Portugal.

Hasta principios de 2026, NovaPay gestionaba la seguridad de forma reactiva: un equipo de tres personas (un responsable de seguridad y dos ingenieros de infraestructura) cubria tanto las operaciones de TI como la ciberseguridad, sin procesos formalizados ni herramientas especificas de GRC.

## El desafio: cumplir con dos normativas a la vez y en plazo

En enero de 2026, NovaPay se enfrento a una confluencia de obligaciones regulatorias:

**ISO 27001.** Su principal partner bancario (una entidad de credito espanola) comunico que a partir de septiembre de 2026 exigiria la certificacion ISO 27001 a todos los proveedores tecnologicos que procesaran datos de tarjetas. Sin la certificacion, NovaPay perderia el contrato que representaba el 35% de su facturacion.

**DORA (Reglamento de Resiliencia Operativa Digital).** Como proveedor critico de servicios TIC para entidades financieras, NovaPay entro en el ambito del Reglamento DORA. Esto implicaba demostrar capacidades de gestion de riesgos TIC, notificacion de incidentes, pruebas de resiliencia y gestion de terceros que no tenian documentadas.

**Plazo.** Disponian de 8 meses como maximo. La media del sector para una certificacion ISO 27001 desde cero es de 12 a 18 meses segun los datos del Foro Internacional de Certificacion Acreditada (IAF).

**Equipo.** Tres personas dedicadas a seguridad, sin experiencia previa en procesos de certificacion ni en gestion formal de riesgos. El presupuesto asignado era de 45.000 euros para consultoria y herramientas, excluyendo la auditoria de certificacion.

### Los problemas concretos que encontramos

Cuando realizamos la evaluacion inicial con NovaPay, identificamos seis brechas criticas:

1. **Sin politica de seguridad aprobada.** Existian documentos internos de configuracion, pero nada que cumpliera los requisitos formales de ISO 27001 clausula 5.2 ni del articulo 6 de DORA.

2. **Analisis de riesgos inexistente.** Las decisiones de seguridad se tomaban por intuicion del equipo tecnico. No habia inventario de activos de informacion, ni identificacion formal de amenazas, ni criterios de aceptacion de riesgo aprobados por la direccion.

3. **Herramientas aisladas.** Usaban Jira para tickets de seguridad, hojas de calculo para el registro de incidentes, un directorio compartido para documentos de politicas y correo electronico para la comunicacion de alertas. No habia trazabilidad entre controles, evidencias y riesgos.

4. **Sin monitorizacion continua.** No tenian SIEM ni capacidad de deteccion centralizada. Los logs se almacenaban en los propios servidores sin correlacion ni alertas automatizadas. El tiempo medio de deteccion de incidentes (MTTD) era desconocido.

5. **Gestion de proveedores informal.** Trabajaban con 12 proveedores tecnologicos (cloud, pasarela de pagos, CDN, antifraude) sin evaluaciones de seguridad documentadas. DORA exige un registro de proveedores TIC criticos con evaluaciones periodicas.

6. **Sin programa de concienciacion.** El personal no habia recibido formacion en ciberseguridad. Tanto ISO 27001 (Anexo A, control A.6.3) como DORA (articulo 13.6) lo exigen expresamente.

## La solucion: implementacion con Riskitera

El proyecto se estructuro en tres fases de dos meses cada una, con revisiones quincenales de progreso.

### Fase 1 (semanas 1 a 8): Fundamentos

**Evaluacion de riesgos con MAGERIT.** Utilizamos el modulo de analisis de riesgos de Riskitera para realizar el inventario de activos (identificamos 847 activos de informacion), mapear amenazas del catalogo MAGERIT y calcular el riesgo inherente. Lo que normalmente lleva 6 a 8 semanas con hojas de calculo, se completo en 3 semanas gracias a la automatizacion del catalogo de amenazas y la generacion automatica de valoraciones iniciales basadas en el tipo de activo.

El resultado fue un registro de riesgos con 124 escenarios de riesgo valorados, 23 de ellos por encima del umbral de aceptacion definido por la direccion.

**Declaracion de aplicabilidad.** Riskitera genero automaticamente la declaracion de aplicabilidad (SoA) mapeando los 93 controles del Anexo A de ISO 27001:2022 contra los riesgos identificados, indicando cuales eran aplicables, cuales no y la justificacion. El equipo de NovaPay reviso y ajusto el documento en 2 dias en lugar de las 2 a 3 semanas habituales.

**Marco documental.** Generamos el esqueleto de las 12 politicas requeridas (seguridad de la informacion, control de acceso, clasificacion de la informacion, gestion de incidentes, continuidad de negocio, criptografia, gestion de proveedores, seguridad en RRHH, seguridad fisica, desarrollo seguro, gestion de activos y cumplimiento). El equipo de NovaPay las adapto a su contexto con el soporte de plantillas y guias integradas en la plataforma.

### Fase 2 (semanas 9 a 16): Implementacion de controles

**Mapeo dual ISO 27001 + DORA.** Uno de los retos especificos del proyecto era que NovaPay necesitaba cumplir con dos marcos simultaneamente. Riskitera mantiene una matriz de correspondencia entre los controles de ISO 27001 Anexo A y los requisitos de los articulos 5 a 15 de DORA. Esto permitio identificar que el 68% de los controles tenian cobertura cruzada: implementar un control para ISO 27001 satisfacia simultaneamente un requisito DORA. El equipo pudo priorizar estos controles de doble cobertura y evitar duplicacion de esfuerzos.

**Evidence Vault.** Configuramos la recopilacion automatica de evidencias conectando las fuentes de datos de NovaPay: AWS CloudTrail para logs de infraestructura, GitHub para cambios de codigo, Azure AD para gestion de accesos, y el sistema de ticketing para gestion de cambios e incidentes. Cada evidencia se almacena con hash SHA-256 y timestamp verificable, formando una cadena de custodia auditable.

Al final de esta fase, el 78% de las evidencias requeridas se recopilaban automaticamente sin intervencion manual.

**Despliegue de monitorizacion.** Integramos las fuentes de logs criticas (firewalls, WAF, sistemas de autenticacion, bases de datos de transacciones) en el modulo de correlacion de Riskitera. Definimos 35 reglas de deteccion iniciales mapeadas a MITRE ATT&CK, priorizando las tecnicas mas relevantes para el sector fintech: acceso con credenciales robadas (T1078), movimiento lateral (T1021), exfiltracion por canal C2 (T1041) y manipulacion de datos financieros.

### Fase 3 (semanas 17 a 24): Afinado, formacion y auditoria

**Programa de concienciacion.** Se implemento un programa de formacion para los 180 empleados que incluia un modulo online de 45 minutos sobre fundamentos de ciberseguridad, simulaciones de phishing mensuales (la tasa de clic bajo del 34% al 8% en tres meses) y formacion especifica para el equipo de desarrollo sobre OWASP Top 10 y desarrollo seguro.

**Registro de proveedores TIC.** Para cumplir con DORA, catalogamos los 12 proveedores tecnologicos de NovaPay, clasificamos 4 como criticos (AWS, la pasarela de pagos, el proveedor de antifraude y el CDN) y documentamos las evaluaciones de seguridad, los SLA y los planes de contingencia para cada uno.

**Simulacro de auditoria interna.** Antes de la auditoria de certificacion, realizamos una auditoria interna completa utilizando los checklists de Riskitera alineados con ISO 19011. Se identificaron 7 no conformidades menores que se corrigieron en 10 dias.

**Auditoria de certificacion.** La auditoria externa (Fase 1 + Fase 2) se completo en la semana 24 del proyecto. El auditor destaco positivamente la trazabilidad completa entre riesgos, controles y evidencias, y la capacidad de la plataforma para generar informes de cumplimiento en tiempo real durante la propia auditoria.

## Resultados

| Metrica | Antes | Despues | Mejora |
|---|---|---|---|
| Tiempo hasta certificacion ISO 27001 | N/A | 6 meses | 50-65% menos que la media del sector |
| Controles ISO 27001 Anexo A documentados | 0/93 | 93/93 | 100% cobertura |
| Requisitos DORA cubiertos | 0% | 87% | Pendiente: pruebas TLPT avanzadas |
| Tiempo de recopilacion de evidencias | ~40 h/mes (manual) | ~6 h/mes | 85% reduccion |
| MTTD (tiempo medio de deteccion) | Desconocido | 4.2 horas | Medible por primera vez |
| Tasa de clic en simulaciones de phishing | 34% | 8% | 76% reduccion |
| Proveedores TIC evaluados formalmente | 0/12 | 12/12 | 100% cobertura |
| No conformidades en auditoria de certificacion | N/A | 0 mayores, 2 menores | Por debajo de la media del sector |

### Impacto en el negocio

El resultado mas relevante para NovaPay no fue la certificacion en si, sino su impacto comercial:

- **Contrato bancario renovado** por tres anos, con un incremento del 15% en volumen procesado.
- **Dos nuevos clientes en Portugal** que exigian ISO 27001 como requisito previo a la contratacion.
- **Reduccion del coste del seguro cibernetico** en un 22% en la renovacion anual, gracias a la documentacion de controles y la monitorizacion continua.
- **Base solida para NIS2.** Con el SGSI implementado, NovaPay estima que la adaptacion a los requisitos adicionales de NIS2 (cuando se complete la transposicion en Espana) requerira un esfuerzo incremental de 4 a 6 semanas, en lugar de un proyecto completo desde cero.

## Lecciones aprendidas

**El apoyo de la direccion fue determinante.** El CEO de NovaPay asistio a la reunion de kick-off y a las revisiones mensuales. Cuando el equipo de desarrollo pidio aplazar la formacion en desarrollo seguro por presion de roadmap, la direccion intervino para mantener el calendario. Sin ese respaldo, el proyecto habria sufrido retrasos.

**El mapeo dual ISO 27001 + DORA ahorro un 30% de esfuerzo.** Abordar ambos marcos como proyectos independientes habria duplicado gran parte del trabajo documental y de implementacion de controles. La matriz de correspondencia de Riskitera fue clave para evitar esa duplicacion.

**Las evidencias automatizadas cambiaron la percepcion del equipo.** El mayor escepticismo inicial del equipo de NovaPay era que el SGSI se convertiria en un "ejercicio de papeles" que consumiria tiempo sin aportar valor operativo. Cuando vieron que el 78% de las evidencias se recopilaban automaticamente y que la plataforma generaba los informes de revision de la direccion con datos reales, la percepcion cambio: el sistema no era burocracia, sino visibilidad.

**La monitorizacion continua detecto un incidente real.** Durante la fase 3 del proyecto, las reglas de deteccion identificaron un intento de acceso no autorizado a una API interna desde una IP asociada a un proxy comercial. El equipo lo contuvo en 90 minutos. Antes de la implementacion, este tipo de actividad habria pasado completamente desapercibida.
