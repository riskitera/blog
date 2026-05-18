---
title: "Gestión de evidencias en auditorías de seguridad: workflow completo"
description: "Workflow completo para la gestión de evidencias en auditorías de seguridad: recopilación, clasificación, almacenamiento, trazabilidad y presentación ante auditores externos."
slug: "gestion-evidencias-auditorias-seguridad"
date: 2026-06-09
publishDate: 2026-06-09
lastmod: 2026-06-09
draft: false
tags: ["GRC", "Auditoría", "Compliance"]
categories: ["GRC"]
author: "David Moya"
keyword: "gestion evidencias auditoria"
funnel: "mofu"
---

Workflow completo para la gestión de evidencias en auditorías de seguridad: recopilación, clasificación, almacenamiento, trazabilidad y presentación ante auditores externos.

<!--more-->

{{< key-takeaways >}}
- Una evidencia de auditoría es cualquier registro verificable que demuestra la implementación y eficacia de un control de seguridad: logs, capturas, informes, registros de formación, actas de reunion.
- El ciclo de vida de una evidencia tiene 5 fases: identificación, recopilación, clasificación, almacenamiento y presentación, cada una con requisitos de integridad y trazabilidad.
- La cadena de custodia garantiza que la evidencia no ha sido alterada: hash de integridad, timestamps, registro de accesos y control de versiones son obligatorios.
- El 43% de las no conformidades en auditorías ISO 27001 se deben a evidencias ausentes, desactualizadas o mal vinculadas a controles, no a falta de controles reales.
- La automatización de la recopilación de evidencias reduce el tiempo de preparación de auditorías entre un 50% y un 70%, eliminando el cuello de botella operativo más común.
{{< /key-takeaways >}}

## Qué son las evidencias en una auditoría de seguridad?

Una evidencia de auditoría es cualquier información verificable que demuestra que un control de seguridad esta implementado, funciona correctamente y se mantiene en el tiempo. No es un documento teórico. No es una política escrita que nadie cumple. Es la prueba tangible de que lo que dices que haces, realmente lo haces.

Cuando un auditor externo revisa tu sistema de gestión de seguridad (ya sea bajo [ISO 27001](https://www.iso.org/standard/27001), [ENS](https://www.boe.es/eli/es/rd/2022/05/03/311) o [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555)), no se conforma con declaraciones verbales ni con documentos genéricos. Necesita evidencias concretas, actualizadas y trazables que demuestren tres cosas:

1. **Existencia del control.** Que el control está definido, documentado y asignado a un responsable.
2. **Implementación efectiva.** Que el control se ejecuta en la práctica, no solo en la teoría.
3. **Eficacia continuada.** Que el control funciona según lo previsto y se revisa periódicamente.

La norma [ISO 19011](https://www.iso.org/standard/70017.html) (directrices para auditorías de sistemas de gestión) define las evidencias como "registros, declaraciones de hechos u otra información que son pertinentes para los criterios de auditoría y que son verificables". La clave está en ese último adjetivo: verificable. Si no puedes demostrar la autenticidad y la integridad de la evidencia, no sirve.

En la práctica, la mayoría de las organizaciones fallan no porque les falten controles, sino porque no pueden demostrarlos. Un estudio de BSI (British Standards Institution) sobre auditorías ISO 27001 en Europa revela que el 43% de las no conformidades están relacionadas con evidencias insuficientes o mal gestionadas, no con la ausencia de controles de seguridad.

## Qué tipos de evidencias existen?

Las evidencias se clasifican según su naturaleza, su origen y su grado de automatización.

### Por naturaleza

**Evidencias documentales.** Políticas aprobadas, procedimientos operativos, [planes directores de seguridad](/es/posts/2026/04/plan-director-seguridad-plantilla/), actas de comites, registros de formación, contratos con cláusulas de seguridad, informes de revisión por la dirección.

**Evidencias técnicas.** Logs de sistemas, configuraciones de firewalls, resultados de escaneos de vulnerabilidades, informes de pentesting, capturas de configuración de SIEM, registros de backups, dashboards de monitoring.

**Evidencias operativas.** Registros de gestión de incidentes, tickets resueltos de parcheo, registros de cambios (change management), actas de revisiones de acceso, resultados de simulacros de phishing, informes de [respuesta a incidentes](/es/posts/2026/04/respuesta-incidentes-seguridad-playbook/).

**Evidencias de terceros.** Certificados de proveedores (ISO 27001, SOC 2), informes de auditorías externas anteriores, resultados de análisis de riesgo de proveedores, cláusulas contractuales verificadas.

### Por origen

**Evidencias primarias (directas).** Generadas por tus propios sistemas: logs, configuraciones, registros automatizados. Son las más fiables para un auditor porque no dependen de la interpretación humana.

**Evidencias secundarias (indirectas).** Documentos creados por personas: actas, informes, declaraciones. Validas, pero el auditor puede cuestionar su objetividad.

**Evidencias de observación.** Lo que el auditor observa directamente durante la auditoría in situ: que los empleados bloquean sus pantallas, que el CPD tiene control de acceso físico, que el SOC esta operativo.

### Por grado de automatización

**Evidencias manuales.** Requieren intervención humana para su generación: capturas de pantalla hechas a mano, informes Word rellenados manualmente, actas escaneadas.

**Evidencias semi-automatizadas.** Se generan con herramientas pero requieren intervención para recopilarlas: exportar un informe del SIEM, ejecutar un script que genera un reporte, extraer métricas de un dashboard.

**Evidencias automatizadas.** Se recopilan sin intervención humana: colectores que extraen configuraciones periódicamente, integraciónes API que recogen logs, monitores que generan evidencias de disponibilidad. Este es el objetivo para al menos el 60% de tus evidencias.

## Cómo recopilar evidencias de forma eficiente?

La recopilación de evidencias es el cuello de botella de toda auditoría. Sin una estrategia clara, se convierte en una carrera contrarreloj de última hora donde todo el equipo busca desesperadamente capturas de pantalla, logs y documentos que demuestren cumplimiento.

### Paso 1: Mapear controles a evidencias requeridas

Antes de recopilar, define que evidencia necesitas para cada control. Crea una matriz de controles-evidencias:

| Control | Framework | Evidencia requerida | Tipo | Frecuencia | Responsable |
|---------|-----------|-------------------|------|------------|-------------|
| Gestión de accesos privilegiados | ENS op.acc.4 | Lista de cuentas privilegiadas + revisión trimestral | Técnica | Trimestral | Administrador de sistemas |
| Formación en seguridad | ISO 27001 A.6.3 | Registro de asistencia + certificados | Documental | Anual | RRHH |
| Backup y recuperación | ENS op.cont.1 | Logs de backup + informe de prueba de restauración | Técnica | Mensual | Operaciones |
| Gestión de vulnerabilidades | NIS2 art.21 | Informe de escaneo + plan de remediación | Técnica | Mensual | Seguridad |

Este mapeo es la base de todo. Sin el, no sabes que recopilar, con que frecuencia ni quien es responsable.

Si tu organización trabaja con múltiples frameworks ([diferencias ENS vs ISO 27001](/es/posts/2026/04/diferencias-ens-iso-27001/)), el mapeo cruzado de controles te permite vincular una misma evidencia a varios requisitos. Una evidencia de revisión de accesos, por ejemplo, sirve simultáneamente para ENS, ISO 27001 y [RGPD](https://eur-lex.europa.eu/eli/reg/2016/679).

### Paso 2: Definir la frecuencia de recopilación

No todas las evidencias se recopilan con la misma frecuencia. La regla general:

- **Evidencias de políticas y procedimientos:** Cuando cambian (evento) + revisión anual mínima.
- **Evidencias de configuración:** Al menos trimestral, idealmente mensual.
- **Evidencias de monitoring y logs:** Continuo (automatizado) con snapshots periódicos.
- **Evidencias de formación:** Al finalizar cada sesión de formación + registro anual consolidado.
- **Evidencias de gestión de incidentes:** Por cada incidente + informe consolidado trimestral.
- **Evidencias de revisión por la dirección:** Según la frecuencia de reuniones del comité (típicamente semestral o anual).

### Paso 3: Establecer responsables claros

Cada evidencia debe tener un responsable asignado. No un equipo, no un departamento: una persona con nombre y apellidos. Si "todos son responsables", nadie lo es.

El responsable de la evidencia no siempre es el responsable del control. El CISO puede ser responsable del control de gestión de vulnerabilidades, pero el responsable de la evidencia (el informe de escaneo) puede ser el analista de vulnerabilidades.

### Paso 4: Establecer colectores automatizados

Para cada evidencia técnica, evalúa si puedes automatizar su recopilación:

- **Logs de sistemas.** Configura tu [SIEM](/es/posts/2026/04/que-es-un-siem-para-que-sirve/) para exportar automáticamente resaltados periódicos vinculados a controles.
- **Configuraciones de red.** Scripts que capturan configuraciones de firewalls, switches y routers a intervalos regulares.
- **Estado de parcheo.** Informes automáticos de tu herramienta de gestión de parches.
- **Resultados de escaneos.** Integración con tu herramienta de vulnerabilidades para importar informes automáticamente.
- **Registros de acceso.** Exportación automática desde tu directorio activo o IAM.

{{< cta type="tofu" text="Riskitera mapea automáticamente controles ENS, NIS2 e ISO 27001, reduciendo el esfuerzo manual un 70%." label="Ver cómo" >}}

## Cómo clasificar y almacenar evidencias?

Una vez recopilada, la evidencia necesita ser clasificada, indexada y almacenada de forma que sea fácilmente recuperable y su integridad este garantizada.

### Taxonomia de clasificación

Define una taxonomía consistente para clasificar evidencias. Un esquema que funciona bien:

**Nivel 1: Framework.** ENS, ISO 27001, RGPD, NIS2.
**Nivel 2: Dominio/Clausula.** Para ENS: Marco organizativo, Marco operacional, Medidas de protección. Para ISO 27001: Clausulas 4-10 + Anexo A.
**Nivel 3: Control específico.** Código del control (ej. ENS op.acc.4, ISO A.8.2).
**Nivel 4: Tipo de evidencia.** Política, configuración, log, informe, registro.
**Nivel 5: Periodo.** Año-trimestre o año-mes.

### Nomenclatura de archivos

Adopta una convención de nombres que permita identificar la evidencia sin abrirla:

`[FRAMEWORK]-[CONTROL]-[TIPO]-[FECHA].[extensión]`

Ejemplos:
- `ENS-op.acc.4-revision_accesos_privilegiados-2026Q2.pdf`
- `ISO27001-A8.2-escaneo_vulnerabilidades-202606.xlsx`
- `RGPD-art32-informe_cifrado_datos-2026Q2.pdf`

### Requisitos de almacenamiento

**Integridad.** Cada evidencia debe tener un hash (SHA-256 como mínimo) calculado en el momento de su almacenamiento. Esto permite verificar que no ha sido alterada.

**Disponibilidad.** Las evidencias deben ser accesibles durante el periodo de retención exigido por cada framework. Para ENS Alto, el [CCN-CERT](https://www.ccn-cert.cni.es/) recomienda conservar registros de auditoría durante 5 años.

**Confidencialidad.** Muchas evidencias contienen información sensible (configuraciones de seguridad, resultados de pentesting, datos de vulnerabilidades). El acceso debe estar restringido a quienes lo necesiten: equipo de compliance, auditores autorizados, dirección.

**Ubicación.** Para organizaciones sujetas a ENS, los datos deben residir en infraestructuras que cumplan los requisitos del esquema. Para [RGPD](https://eur-lex.europa.eu/eli/reg/2016/679), los datos personales deben estar en la UE salvo que existan garantías adecuadas. Esto descarta almacenar evidencias en servicios cloud sin verificar la ubicación de los datos.

### Estructura de repositorio

Un repositorio de evidencias bien organizado sigue una estructura que refleja la taxonomía:

```
/evidencias/
├── ENS/
│   ├── marco-organizativo/
│   │   ├── org.1-política-seguridad/
│   │   └── org.2-normativa-seguridad/
│   ├── marco-operacional/
│   │   ├── op.acc.4-acceso-privilegiado/
│   │   │   ├── 2026-Q1/
│   │   │   ├── 2026-Q2/
│   │   │   └── ...
│   │   └── op.cont.1-backup/
│   └── medidas-protección/
├── ISO27001/
│   ├── A5-políticas/
│   ├── A6-organización/
│   └── A8-gestión-activos/
├── RGPD/
│   ├── art30-rat/
│   ├── art32-medidas-técnicas/
│   └── art35-eipd/
└── multi-framework/   ← evidencias compartidas entre frameworks
```

La carpeta `multi-framework` es clave. Una evidencia de revisión de accesos puede servir para ENS, ISO 27001 y RGPD. En lugar de duplicarla, almacenala una vez y vinculala a los tres frameworks.

## Cómo garantizar la trazabilidad de las evidencias?

La trazabilidad es lo que convierte un archivo suelto en una evidencia válida para auditoría. Necesitas poder demostrar:

- **Quien genero la evidencia.** Autor o sistema de origen.
- **Cuando se genero.** Timestamp fiable (idealmente de un servidor NTP sincronizado).
- **Que contiene.** Descripción del alcance de la evidencia.
- **Que no ha sido alterada.** Hash de integridad, control de versiones.
- **Quien ha accedido a ella.** Registro de accesos.
- **A que control(es) responde.** Vinculación explícita con los controles del framework.

### Cadena de custodia digital

La cadena de custodia es un concepto tomado de la investigación forense que aplica perfectamente a las evidencias de auditoría. Consiste en documentar cada operación realizada sobre la evidencia:

| Fecha/hora | Acción | Usuario/Sistema | Detalle |
|------------|--------|----------------|---------|
| 2026-06-01 08:15 | Generación | Script automático v2.3 | Escaneo de vulnerabilidades Nessus |
| 2026-06-01 08:16 | Almacenamiento | Sistema de evidencias | Hash SHA-256: a1b2c3... |
| 2026-06-01 10:30 | Revisión | Ana Garcia (analista) | Verificación de resultados |
| 2026-06-01 11:00 | Vinculación | Sistema de evidencias | Vinculada a ENS op.exp.6, ISO A.8.8 |
| 2026-06-15 09:00 | Acceso lectura | Pedro Martinez (auditor) | Revisión de auditoría interna |

### Versionado de evidencias

Algunas evidencias se actualizan periódicamente (políticas, procedimientos, registros de activos). Es imprescindible mantener el historial de versiones:

- **Versión vigente** marcada claramente.
- **Versiones anteriores** accesibles para demostrar la evolución temporal.
- **Registro de cambios** con fecha, autor y descripción del cambio.
- **Aprobación formal** de cada nueva versión por el responsable autorizado.

### Sellado de tiempo

Para evidencias críticas, considera el uso de sellos de tiempo cualificados (TSA, Time Stamping Authority) conforme al reglamento eIDAS. Un sello de tiempo cualificado proporciona prueba legal de que la evidencia existia en un momento determinado y no ha sido modificada desde entonces.

En España, proveedores como la FNMT-RCM ofrecen servicios de sellado de tiempo cualificado que son especialmente relevantes para evidencias de ENS Alto.

## Cómo presentar evidencias ante un auditor externo?

La presentación de evidencias es el momento de la verdad. Un auditor experimentado evalúa no solo el contenido de las evidencias, sino la forma en que las presentas. Una presentación desordenada genera desconfianza; una presentación estructurada y fluida genera confianza.

### Preparación previa a la auditoría

**Paquete de evidencias por control.** Prepara un paquete para cada control que incluya: descripción del control, responsable, evidencia(s) asociada(s), fecha de última revisión, estado de cumplimiento.

**Indice de evidencias.** Un documento maestro que liste todas las evidencias disponibles, su ubicación, su vinculación a controles y su estado de vigencia. El auditor debe poder navegar el índice y localizar cualquier evidencia en menos de 2 minutos.

**Sesión de dry run.** Antes de la auditoría real, haz una simulación interna. Pide a un colega que actue como auditor y solicite evidencias aleatorias. Si tardas más de 5 minutos en localizar una evidencia, tienes un problema.

### Durante la auditoría

**Acceso controlado.** Da al auditor acceso de solo lectura al repositorio de evidencias. No le des acceso completo a tus sistemas. Si necesita ver algo en vivo, muestra tu la pantalla.

**Respuestas con evidencia, no con palabras.** Cuando el auditor pregunte "como gestionais los accesos privilegiados?", no respondas con una explicación verbal de 10 minutos. Muestra la política de accesos, el registro de cuentas privilegiadas, el log de la última revisión trimestral y el informe de la herramienta PAM.

**Registro de solicitudes.** Documenta cada evidencia solicitada por el auditor y el resultado de la solicitud (proporcionada, no disponible, parcialmente disponible). Esto te servirá para mejorar tu repositorio de cara a futuras auditorías.

### Errores comunes en la presentación

**Evidencias vencidas.** Presentar un escaneo de vulnerabilidades de hace 8 meses cuando el auditor espera evidencia del último trimestre. Solución: define calendarios de renovación y alertas automáticas.

**Evidencias genéricas.** Un informe que dice "los backups se realizan correctamente" sin datos concretos: fechas, volúmenes, tiempos de restauración, resultado de la última prueba. Los auditores quieren datos, no declaraciones.

**Evidencias desvinculadas.** Tener la evidencia pero no poder vincularla rápidamente al control que la requiere. El auditor pregunta por el control ENS op.cont.1 y tardas 20 minutos en encontrar el informe de backup correspondiente.

**Ausencia de evidencia de eficacia.** Demostrar que el control existe (tenemos una política de backup) pero no que funciona (la última restauración de prueba fue exitosa el 15 de mayo de 2026, con un RTO de 4 horas sobre un objetivo de 8 horas).

## Cómo automatizar la gestión de evidencias?

La automatización es la diferencia entre un proceso de auditoría que consume 400 horas y uno que consume 100. Veamos como implementarla de forma práctica.

### Nivel 1: Automatización básica (scripts + táreas programadas)

Si tu presupuesto es limitado, empieza con scripts que automaticen la recopilación de las evidencias técnicas más frecuentes:

- **Script de inventario de activos.** Ejecutar semanalmente, exportar a CSV.
- **Script de revisión de accesos.** Exportar la lista de usuarios activos del directorio, comparar con la lista autorizada.
- **Exportación automática de logs.** Configurar el SIEM para generar resaltados semanales por categoría.
- **Tarea de verificación de backups.** Comprobar automáticamente que los backups se completaron y registrar el resultado.

Limitaciones: requiere mantenimiento manual de los scripts, no hay vinculación automática con controles, la trazabilidad depende de la disciplina del equipo.

### Nivel 2: Automatización intermedia (plataforma GRC básica)

Una [plataforma GRC](/es/posts/2026/04/como-elegir-plataforma-grc/) añade la capa de gestión que los scripts no ofrecen:

- **Vinculación automática evidencia-control.** La plataforma sabe que evidencia corresponde a cada control y alerta cuando falta o esta vencida.
- **Workflows de aprobación.** El responsable del control recibe una notificación, revisa la evidencia y la aprueba con un clic.
- **Dashboard de estado.** Visión en tiempo real de cuantas evidencias están vigentes, cuantas vencen en los próximos 30 días y cuantas faltan.
- **Calendario de recopilación.** La plataforma genera recordatorios automáticos a los responsables.

### Nivel 3: Automatización avanzada (integraciónes API + IA)

El nivel más maduro combina integraciónes nativas con sistemas fuente y capacidades de inteligencia artificial:

- **Colectores API.** Integraciónes directas con tu SIEM, tu herramienta de vulnerabilidades, tu directorio activo, tu ticketing y tu cloud. Las evidencias se recopilan automáticamente sin intervención humana.
- **Clasificación automática.** La IA clasifica la evidencia, la vincula al control correcto y detecta anomalías (por ejemplo, una evidencia que muestra un gap de seguridad).
- **Generación de narrativa.** La IA genera borradores de los informes de auditoría a partir de las evidencias recopiladas, que el responsable solo necesita revisar y aprobar.
- **Alertas predictivas.** El sistema predice que evidencias van a vencer antes de la próxima auditoría y genera alertas proactivas.

Riskitera opera en este nivel, con colectores automatizados que extraen evidencias de sistemas fuente, mapeo cruzado multi-framework y generación asistida por IA de informes para auditores.

### Métricas de automatización

Mide el progreso de tu automatización con estos indicadores:

| Métrica | Baseline (manual) | Objetivo (automatizado) |
|---------|-------------------|------------------------|
| % evidencias recopiladas automáticamente | 0 - 10% | >60% |
| Tiempo medio de recopilación por evidencia | 30 - 60 min | <5 min |
| Evidencias con hash de integridad | 0% | 100% |
| Evidencias vinculadas a controles | 40 - 60% | >95% |
| Tiempo de preparación de auditoría | 200 - 400 h | 50 - 100 h |

## Alineación con ISO 19011 y marcos de auditoría

La gestión de evidencias no ocurre en el vacio. Debe alinearse con los marcos de auditoría reconocidos que los auditores utilizan.

### ISO 19011: directrices para auditorías de sistemas de gestión

ISO 19011 establece los principios que guían la evaluación de evidencias:

- **Suficiencia.** Hay evidencias suficientes para sustentar las conclusiones de la auditoría?
- **Pertinencia.** Las evidencias son relevantes para los criterios de auditoría evaluados?
- **Fiabilidad.** Las evidencias son fiables (fuentes verificables, integridad demostrable)?

Para satisfacer estos tres principios, tu sistema de gestión de evidencias debe garantizar que cada control tiene evidencia suficiente (no una sola evidencia, sino múltiples fuentes que se corroboran), pertinente (vinculada explícitamente al control) y fiable (con hash, timestamp y cadena de custodia).

### Guías CCN-STIC para ENS

El [CCN-CERT](https://www.ccn-cert.cni.es/) pública guías específicas para la evidenciación de controles ENS. Las más relevantes:

- **CCN-STIC 802.** Guía de auditoría del ENS. Define que evidencias espera un auditor para cada control.
- **CCN-STIC 804.** Guía de implantación del ENS. Incluye orientaciones sobre como documentar la implementación de controles.
- **CCN-STIC 808.** Verificación del cumplimiento. Establece los criterios de verificación que aplican los auditores.

Si tu organización está sujeta a ENS, estas guías son la referencia definitiva para saber qué evidencias necesitas para cada nivel ([diferencias entre ENS Alto, Medio y Bajo](/es/posts/2026/04/ens-alto-medio-bajo-diferencias/)).

### ISAE 3402 / SOC 2 para proveedores de servicios

Si eres proveedor de servicios y tus clientes te exigen un informe SOC 2 o ISAE 3402, las evidencias deben cubrir un periodo continuo (típicamente 6-12 meses) y demostrar la eficacia operativa de los controles a lo largo de todo ese periodo, no solo en un momento puntual. Esto requiere evidencias recurrentes y automatizadas que demuestren consistencia temporal.

## Errores fatales en la gestión de evidencias

Tras años de auditorías, los errores se repiten. Estos son los más frecuentes y como evitarlos.

### El sindrome del último momento

Empezar a recopilar evidencias una semana antes de la auditoría. El resultado: evidencias incompletas, documentos fabricados a toda prisa, equipo estresado y auditores que detectan la improvisación. La solución: recopilación continúa, no puntual. Si las evidencias se generan y almacenan a lo largo del año, la preparación de la auditoría se reduce a verificar que todo está completo y actualizado.

### La evidencia de cajon

Políticas y procedimientos que se escribieron para pasar la auditoría y nunca más se revisaron. Un auditor experimentado detecta una política "de cajon" en segundos: pide un ejemplo de aplicación reciente y no hay ninguno. La solución: cada política debe tener evidencias de aplicación real, no solo de existencia.

### La evidencia duplicada inconsistente

Copias de la misma evidencia en distintas ubicaciones con versiones diferentes. El auditor pregunta por el procedimiento de gestión de cambios y le muestras una versión en el SharePoint y otra en la wiki interna, con contenido contradictorio. La solución: repositorio único como fuente de verdad, con enlaces (no copias) desde otros sistemas.

### La evidencia sin contexto

Un log de 10.000 líneas que "demuestra" el control de monitoring. El auditor no va a leer 10.000 líneas. Necesita un resumen ejecutivo que explique que muestra el log, que periodo cubre, que anomalías se detectaron y que acciones se tomaron. La solución: cada evidencia técnica debe acompañarse de una nota de contexto que la haga interpretable.

{{< cta type="bofu" text="Empieza tu PoC y descubre cuanto tiempo ahorras en cada ciclo de auditoría." label="Iniciar PoC" >}}


**Artículos relacionados:**
- [Auditoría Seguridad Informatica Guia](/es/posts/2026/04/auditoria-seguridad-informatica-guia/)
- [Automatizar auditorías de seguridad con IA](/es/posts/2026/04/automatizar-auditorias-seguridad-ia/)
- [ROI de una plataforma GRC](/es/posts/2026/07/roi-plataforma-grc-calcular/)
- [Plan director de seguridad: plantilla](/es/posts/2026/04/plan-director-seguridad-plantilla/)

## Preguntas frecuentes

### Cuánto tiempo deben conservarse las evidencias de auditoría?

Depende del framework. Para ISO 27001, la norma no específica un periodo mínimo, pero la práctica habitual es conservar evidencias al menos 3 años (dos ciclos de certificación). Para ENS Alto, el CCN-CERT recomienda 5 años para registros de auditoría. Para RGPD, las evidencias de cumplimiento deben conservarse mientras exista la obligación de demostrar el cumplimiento y, en caso de inspección de la [AEPD](https://www.aepd.es/), la prescripción de infracciones muy graves es de 3 años. La regla segura: conservar al menos 5 años las evidencias críticas y 3 años las operativas.

### Es necesario firmar digitalmente todas las evidencias?

No es obligatorio en la mayoría de frameworks, pero si altamente recomendable para evidencias críticas (políticas aprobadas, informes de auditoría, actas de comité de seguridad). Para evidencias técnicas automatizadas, un hash de integridad (SHA-256) con timestamp de un servidor NTP sincronizado suele ser suficiente. Para organizaciones sujetas a ENS Alto en administraciones públicas, el uso de firma electrónica cualificada (conforme a eIDAS y la Ley 39/2015) puede ser exigido por el auditor para determinados documentos.

### Qué pasa si un auditor solicita una evidencia que no tenemos?

Es un escenario habitual. Lo peor que puedes hacer es inventar una evidencia sobre la marcha. El auditor lo detectara. Lo correcto: reconocer la carencia, explicar por que no existe (no se habia identificado como necesaria, el control se implemento recientemente, el sistema no genera ese tipo de registro), proponer un plan de acción con fecha concreta para subsanarla, y documentar todo como hallazgo interno. Una no conformidad menor por evidencia ausente es preferible a una no conformidad mayor por evidencia falsificada.

### Cómo gestionar evidencias cuando hay múltiples auditores (interno, externo, regulador)?

Usa un repositorio único con permisos diferenciados. El auditor interno tiene acceso completo. El auditor externo de certificación tiene acceso a las evidencias vinculadas a su alcance. El regulador (por ejemplo, [ENISA](https://www.enisa.europa.eu/) para NIS2 o la AEPD para RGPD) tiene acceso solo a lo que solicite formalmente. Nunca des acceso indiscriminado. Y registra cada acceso en la cadena de custodia.

### Puedo usar un repositorio en la nube (Google Drive, SharePoint) para almacenar evidencias?

Puedes, con condiciones. Verifica que el proveedor cloud almacena los datos en la UE (requisito RGPD). Asegurate de que tienes control de acceso granular (no basta con compartir una carpeta con "todos"). Implementa versionado (que las herramientas cloud suelen ofrecer nativamente). Y añade una capa de hash de integridad, porque las herramientas cloud no lo hacen por defecto. Para organizaciones con ENS Alto, verifica que el proveedor cumple con los requisitos de la guía CCN-STIC 823 (uso de servicios en la nube). Una plataforma GRC dedicada es siempre preferible porque integra almacenamiento, trazabilidad, vinculación a controles y hash de integridad en un único sistema.
