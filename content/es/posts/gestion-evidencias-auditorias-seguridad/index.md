---
title: "Gestion de evidencias en auditorias de seguridad: workflow completo"
description: "Workflow completo para la gestion de evidencias en auditorias de seguridad: recopilacion, clasificacion, almacenamiento, trazabilidad y presentacion ante auditores externos."
slug: "gestion-evidencias-auditorias-seguridad"
date: 2026-06-09
publishDate: 2026-06-09
lastmod: 2026-06-09
draft: false
tags: ["GRC", "Auditoria", "Compliance"]
categories: ["GRC"]
author: "David Moya"
keyword: "gestion evidencias auditoria"
funnel: "mofu"
---

Workflow completo para la gestion de evidencias en auditorias de seguridad: recopilacion, clasificacion, almacenamiento, trazabilidad y presentacion ante auditores externos.

<!--more-->

{{< key-takeaways >}}
- Una evidencia de auditoria es cualquier registro verificable que demuestra la implementacion y eficacia de un control de seguridad: logs, capturas, informes, registros de formacion, actas de reunion.
- El ciclo de vida de una evidencia tiene 5 fases: identificacion, recopilacion, clasificacion, almacenamiento y presentacion, cada una con requisitos de integridad y trazabilidad.
- La cadena de custodia garantiza que la evidencia no ha sido alterada: hash de integridad, timestamps, registro de accesos y control de versiones son obligatorios.
- El 43% de las no conformidades en auditorias ISO 27001 se deben a evidencias ausentes, desactualizadas o mal vinculadas a controles, no a falta de controles reales.
- La automatizacion de la recopilacion de evidencias reduce el tiempo de preparacion de auditorias entre un 50% y un 70%, eliminando el cuello de botella operativo mas comun.
{{< /key-takeaways >}}

## Que son las evidencias en una auditoria de seguridad?

Una evidencia de auditoria es cualquier informacion verificable que demuestra que un control de seguridad esta implementado, funciona correctamente y se mantiene en el tiempo. No es un documento teorico. No es una politica escrita que nadie cumple. Es la prueba tangible de que lo que dices que haces, realmente lo haces.

Cuando un auditor externo revisa tu sistema de gestion de seguridad (ya sea bajo [ISO 27001](https://www.iso.org/standard/27001), [ENS](https://www.boe.es/eli/es/rd/2022/05/03/311) o [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555)), no se conforma con declaraciones verbales ni con documentos genericos. Necesita evidencias concretas, actualizadas y trazables que demuestren tres cosas:

1. **Existencia del control.** Que el control esta definido, documentado y asignado a un responsable.
2. **Implementacion efectiva.** Que el control se ejecuta en la practica, no solo en la teoria.
3. **Eficacia continuada.** Que el control funciona segun lo previsto y se revisa periodicamente.

La norma [ISO 19011](https://www.iso.org/standard/70017.html) (directrices para auditorias de sistemas de gestion) define las evidencias como "registros, declaraciones de hechos u otra informacion que son pertinentes para los criterios de auditoria y que son verificables". La clave esta en ese ultimo adjetivo: verificable. Si no puedes demostrar la autenticidad y la integridad de la evidencia, no sirve.

En la practica, la mayoria de las organizaciones fallan no porque les falten controles, sino porque no pueden demostrarlos. Un estudio de BSI (British Standards Institution) sobre auditorias ISO 27001 en Europa revela que el 43% de las no conformidades estan relacionadas con evidencias insuficientes o mal gestionadas, no con la ausencia de controles de seguridad.

## Que tipos de evidencias existen?

Las evidencias se clasifican segun su naturaleza, su origen y su grado de automatizacion.

### Por naturaleza

**Evidencias documentales.** Politicas aprobadas, procedimientos operativos, [planes directores de seguridad](/es/posts/2026/04/plan-director-seguridad-plantilla/), actas de comites, registros de formacion, contratos con clausulas de seguridad, informes de revision por la direccion.

**Evidencias tecnicas.** Logs de sistemas, configuraciones de firewalls, resultados de escaneos de vulnerabilidades, informes de pentesting, capturas de configuracion de SIEM, registros de backups, dashboards de monitoring.

**Evidencias operativas.** Registros de gestion de incidentes, tickets resueltos de parcheo, registros de cambios (change management), actas de revisiones de acceso, resultados de simulacros de phishing, informes de [respuesta a incidentes](/es/posts/2026/04/respuesta-incidentes-seguridad-playbook/).

**Evidencias de terceros.** Certificados de proveedores (ISO 27001, SOC 2), informes de auditorias externas anteriores, resultados de analisis de riesgo de proveedores, clausulas contractuales verificadas.

### Por origen

**Evidencias primarias (directas).** Generadas por tus propios sistemas: logs, configuraciones, registros automatizados. Son las mas fiables para un auditor porque no dependen de la interpretacion humana.

**Evidencias secundarias (indirectas).** Documentos creados por personas: actas, informes, declaraciones. Validas, pero el auditor puede cuestionar su objetividad.

**Evidencias de observacion.** Lo que el auditor observa directamente durante la auditoria in situ: que los empleados bloquean sus pantallas, que el CPD tiene control de acceso fisico, que el SOC esta operativo.

### Por grado de automatizacion

**Evidencias manuales.** Requieren intervencion humana para su generacion: capturas de pantalla hechas a mano, informes Word rellenados manualmente, actas escaneadas.

**Evidencias semi-automatizadas.** Se generan con herramientas pero requieren intervencion para recopilarlas: exportar un informe del SIEM, ejecutar un script que genera un reporte, extraer metricas de un dashboard.

**Evidencias automatizadas.** Se recopilan sin intervencion humana: colectores que extraen configuraciones periodicamente, integraciones API que recogen logs, monitores que generan evidencias de disponibilidad. Este es el objetivo para al menos el 60% de tus evidencias.

## Como recopilar evidencias de forma eficiente?

La recopilacion de evidencias es el cuello de botella de toda auditoria. Sin una estrategia clara, se convierte en una carrera contrarreloj de ultima hora donde todo el equipo busca desesperadamente capturas de pantalla, logs y documentos que demuestren cumplimiento.

### Paso 1: Mapear controles a evidencias requeridas

Antes de recopilar, define que evidencia necesitas para cada control. Crea una matriz de controles-evidencias:

| Control | Framework | Evidencia requerida | Tipo | Frecuencia | Responsable |
|---------|-----------|-------------------|------|------------|-------------|
| Gestion de accesos privilegiados | ENS op.acc.4 | Lista de cuentas privilegiadas + revision trimestral | Tecnica | Trimestral | Administrador de sistemas |
| Formacion en seguridad | ISO 27001 A.6.3 | Registro de asistencia + certificados | Documental | Anual | RRHH |
| Backup y recuperacion | ENS op.cont.1 | Logs de backup + informe de prueba de restauracion | Tecnica | Mensual | Operaciones |
| Gestion de vulnerabilidades | NIS2 art.21 | Informe de escaneo + plan de remediacion | Tecnica | Mensual | Seguridad |

Este mapeo es la base de todo. Sin el, no sabes que recopilar, con que frecuencia ni quien es responsable.

Si tu organizacion trabaja con multiples frameworks ([diferencias ENS vs ISO 27001](/es/posts/2026/04/diferencias-ens-iso-27001/)), el mapeo cruzado de controles te permite vincular una misma evidencia a varios requisitos. Una evidencia de revision de accesos, por ejemplo, sirve simultaneamente para ENS, ISO 27001 y [RGPD](https://eur-lex.europa.eu/eli/reg/2016/679).

### Paso 2: Definir la frecuencia de recopilacion

No todas las evidencias se recopilan con la misma frecuencia. La regla general:

- **Evidencias de politicas y procedimientos:** Cuando cambian (evento) + revision anual minima.
- **Evidencias de configuracion:** Al menos trimestral, idealmente mensual.
- **Evidencias de monitoring y logs:** Continuo (automatizado) con snapshots periodicos.
- **Evidencias de formacion:** Al finalizar cada sesion de formacion + registro anual consolidado.
- **Evidencias de gestion de incidentes:** Por cada incidente + informe consolidado trimestral.
- **Evidencias de revision por la direccion:** Segun la frecuencia de reuniones del comite (tipicamente semestral o anual).

### Paso 3: Establecer responsables claros

Cada evidencia debe tener un responsable asignado. No un equipo, no un departamento: una persona con nombre y apellidos. Si "todos son responsables", nadie lo es.

El responsable de la evidencia no siempre es el responsable del control. El CISO puede ser responsable del control de gestion de vulnerabilidades, pero el responsable de la evidencia (el informe de escaneo) puede ser el analista de vulnerabilidades.

### Paso 4: Establecer colectores automatizados

Para cada evidencia tecnica, evalua si puedes automatizar su recopilacion:

- **Logs de sistemas.** Configura tu [SIEM](/es/posts/2026/04/que-es-un-siem-para-que-sirve/) para exportar automaticamente resaltados periodicos vinculados a controles.
- **Configuraciones de red.** Scripts que capturan configuraciones de firewalls, switches y routers a intervalos regulares.
- **Estado de parcheo.** Informes automaticos de tu herramienta de gestion de parches.
- **Resultados de escaneos.** Integracion con tu herramienta de vulnerabilidades para importar informes automaticamente.
- **Registros de acceso.** Exportacion automatica desde tu directorio activo o IAM.

{{< cta type="tofu" text="Riskitera mapea automaticamente controles ENS, NIS2 e ISO 27001, reduciendo el esfuerzo manual un 70%." label="Ver como" >}}

## Como clasificar y almacenar evidencias?

Una vez recopilada, la evidencia necesita ser clasificada, indexada y almacenada de forma que sea facilmente recuperable y su integridad este garantizada.

### Taxonomia de clasificacion

Define una taxonomia consistente para clasificar evidencias. Un esquema que funciona bien:

**Nivel 1: Framework.** ENS, ISO 27001, RGPD, NIS2.
**Nivel 2: Dominio/Clausula.** Para ENS: Marco organizativo, Marco operacional, Medidas de proteccion. Para ISO 27001: Clausulas 4-10 + Anexo A.
**Nivel 3: Control especifico.** Codigo del control (ej. ENS op.acc.4, ISO A.8.2).
**Nivel 4: Tipo de evidencia.** Politica, configuracion, log, informe, registro.
**Nivel 5: Periodo.** Ano-trimestre o ano-mes.

### Nomenclatura de archivos

Adopta una convencion de nombres que permita identificar la evidencia sin abrirla:

`[FRAMEWORK]-[CONTROL]-[TIPO]-[FECHA].[extension]`

Ejemplos:
- `ENS-op.acc.4-revision_accesos_privilegiados-2026Q2.pdf`
- `ISO27001-A8.2-escaneo_vulnerabilidades-202606.xlsx`
- `RGPD-art32-informe_cifrado_datos-2026Q2.pdf`

### Requisitos de almacenamiento

**Integridad.** Cada evidencia debe tener un hash (SHA-256 como minimo) calculado en el momento de su almacenamiento. Esto permite verificar que no ha sido alterada.

**Disponibilidad.** Las evidencias deben ser accesibles durante el periodo de retencion exigido por cada framework. Para ENS Alto, el [CCN-CERT](https://www.ccn-cert.cni.es/) recomienda conservar registros de auditoria durante 5 anos.

**Confidencialidad.** Muchas evidencias contienen informacion sensible (configuraciones de seguridad, resultados de pentesting, datos de vulnerabilidades). El acceso debe estar restringido a quienes lo necesiten: equipo de compliance, auditores autorizados, direccion.

**Ubicacion.** Para organizaciones sujetas a ENS, los datos deben residir en infraestructuras que cumplan los requisitos del esquema. Para [RGPD](https://eur-lex.europa.eu/eli/reg/2016/679), los datos personales deben estar en la UE salvo que existan garantias adecuadas. Esto descarta almacenar evidencias en servicios cloud sin verificar la ubicacion de los datos.

### Estructura de repositorio

Un repositorio de evidencias bien organizado sigue una estructura que refleja la taxonomia:

```
/evidencias/
├── ENS/
│   ├── marco-organizativo/
│   │   ├── org.1-politica-seguridad/
│   │   └── org.2-normativa-seguridad/
│   ├── marco-operacional/
│   │   ├── op.acc.4-acceso-privilegiado/
│   │   │   ├── 2026-Q1/
│   │   │   ├── 2026-Q2/
│   │   │   └── ...
│   │   └── op.cont.1-backup/
│   └── medidas-proteccion/
├── ISO27001/
│   ├── A5-politicas/
│   ├── A6-organizacion/
│   └── A8-gestion-activos/
├── RGPD/
│   ├── art30-rat/
│   ├── art32-medidas-tecnicas/
│   └── art35-eipd/
└── multi-framework/   ← evidencias compartidas entre frameworks
```

La carpeta `multi-framework` es clave. Una evidencia de revision de accesos puede servir para ENS, ISO 27001 y RGPD. En lugar de duplicarla, almacenala una vez y vinculala a los tres frameworks.

## Como garantizar la trazabilidad de las evidencias?

La trazabilidad es lo que convierte un archivo suelto en una evidencia valida para auditoria. Necesitas poder demostrar:

- **Quien genero la evidencia.** Autor o sistema de origen.
- **Cuando se genero.** Timestamp fiable (idealmente de un servidor NTP sincronizado).
- **Que contiene.** Descripcion del alcance de la evidencia.
- **Que no ha sido alterada.** Hash de integridad, control de versiones.
- **Quien ha accedido a ella.** Registro de accesos.
- **A que control(es) responde.** Vinculacion explicita con los controles del framework.

### Cadena de custodia digital

La cadena de custodia es un concepto tomado de la investigacion forense que aplica perfectamente a las evidencias de auditoria. Consiste en documentar cada operacion realizada sobre la evidencia:

| Fecha/hora | Accion | Usuario/Sistema | Detalle |
|------------|--------|----------------|---------|
| 2026-06-01 08:15 | Generacion | Script automatico v2.3 | Escaneo de vulnerabilidades Nessus |
| 2026-06-01 08:16 | Almacenamiento | Sistema de evidencias | Hash SHA-256: a1b2c3... |
| 2026-06-01 10:30 | Revision | Ana Garcia (analista) | Verificacion de resultados |
| 2026-06-01 11:00 | Vinculacion | Sistema de evidencias | Vinculada a ENS op.exp.6, ISO A.8.8 |
| 2026-06-15 09:00 | Acceso lectura | Pedro Martinez (auditor) | Revision de auditoria interna |

### Versionado de evidencias

Algunas evidencias se actualizan periodicamente (politicas, procedimientos, registros de activos). Es imprescindible mantener el historial de versiones:

- **Version vigente** marcada claramente.
- **Versiones anteriores** accesibles para demostrar la evolucion temporal.
- **Registro de cambios** con fecha, autor y descripcion del cambio.
- **Aprobacion formal** de cada nueva version por el responsable autorizado.

### Sellado de tiempo

Para evidencias criticas, considera el uso de sellos de tiempo cualificados (TSA, Time Stamping Authority) conforme al reglamento eIDAS. Un sello de tiempo cualificado proporciona prueba legal de que la evidencia existia en un momento determinado y no ha sido modificada desde entonces.

En Espana, proveedores como la FNMT-RCM ofrecen servicios de sellado de tiempo cualificado que son especialmente relevantes para evidencias de ENS Alto.

## Como presentar evidencias ante un auditor externo?

La presentacion de evidencias es el momento de la verdad. Un auditor experimentado evalua no solo el contenido de las evidencias, sino la forma en que las presentas. Una presentacion desordenada genera desconfianza; una presentacion estructurada y fluida genera confianza.

### Preparacion previa a la auditoria

**Paquete de evidencias por control.** Prepara un paquete para cada control que incluya: descripcion del control, responsable, evidencia(s) asociada(s), fecha de ultima revision, estado de cumplimiento.

**Indice de evidencias.** Un documento maestro que liste todas las evidencias disponibles, su ubicacion, su vinculacion a controles y su estado de vigencia. El auditor debe poder navegar el indice y localizar cualquier evidencia en menos de 2 minutos.

**Sesion de dry run.** Antes de la auditoria real, haz una simulacion interna. Pide a un colega que actue como auditor y solicite evidencias aleatorias. Si tardas mas de 5 minutos en localizar una evidencia, tienes un problema.

### Durante la auditoria

**Acceso controlado.** Da al auditor acceso de solo lectura al repositorio de evidencias. No le des acceso completo a tus sistemas. Si necesita ver algo en vivo, muestra tu la pantalla.

**Respuestas con evidencia, no con palabras.** Cuando el auditor pregunte "como gestionais los accesos privilegiados?", no respondas con una explicacion verbal de 10 minutos. Muestra la politica de accesos, el registro de cuentas privilegiadas, el log de la ultima revision trimestral y el informe de la herramienta PAM.

**Registro de solicitudes.** Documenta cada evidencia solicitada por el auditor y el resultado de la solicitud (proporcionada, no disponible, parcialmente disponible). Esto te servira para mejorar tu repositorio de cara a futuras auditorias.

### Errores comunes en la presentacion

**Evidencias vencidas.** Presentar un escaneo de vulnerabilidades de hace 8 meses cuando el auditor espera evidencia del ultimo trimestre. Solucion: define calendarios de renovacion y alertas automaticas.

**Evidencias genericas.** Un informe que dice "los backups se realizan correctamente" sin datos concretos: fechas, volumenes, tiempos de restauracion, resultado de la ultima prueba. Los auditores quieren datos, no declaraciones.

**Evidencias desvinculadas.** Tener la evidencia pero no poder vincularla rapidamente al control que la requiere. El auditor pregunta por el control ENS op.cont.1 y tardas 20 minutos en encontrar el informe de backup correspondiente.

**Ausencia de evidencia de eficacia.** Demostrar que el control existe (tenemos una politica de backup) pero no que funciona (la ultima restauracion de prueba fue exitosa el 15 de mayo de 2026, con un RTO de 4 horas sobre un objetivo de 8 horas).

## Como automatizar la gestion de evidencias?

La automatizacion es la diferencia entre un proceso de auditoria que consume 400 horas y uno que consume 100. Veamos como implementarla de forma practica.

### Nivel 1: Automatizacion basica (scripts + tareas programadas)

Si tu presupuesto es limitado, empieza con scripts que automaticen la recopilacion de las evidencias tecnicas mas frecuentes:

- **Script de inventario de activos.** Ejecutar semanalmente, exportar a CSV.
- **Script de revision de accesos.** Exportar la lista de usuarios activos del directorio, comparar con la lista autorizada.
- **Exportacion automatica de logs.** Configurar el SIEM para generar resaltados semanales por categoria.
- **Tarea de verificacion de backups.** Comprobar automaticamente que los backups se completaron y registrar el resultado.

Limitaciones: requiere mantenimiento manual de los scripts, no hay vinculacion automatica con controles, la trazabilidad depende de la disciplina del equipo.

### Nivel 2: Automatizacion intermedia (plataforma GRC basica)

Una [plataforma GRC](/es/posts/2026/04/como-elegir-plataforma-grc/) anade la capa de gestion que los scripts no ofrecen:

- **Vinculacion automatica evidencia-control.** La plataforma sabe que evidencia corresponde a cada control y alerta cuando falta o esta vencida.
- **Workflows de aprobacion.** El responsable del control recibe una notificacion, revisa la evidencia y la aprueba con un clic.
- **Dashboard de estado.** Vision en tiempo real de cuantas evidencias estan vigentes, cuantas vencen en los proximos 30 dias y cuantas faltan.
- **Calendario de recopilacion.** La plataforma genera recordatorios automaticos a los responsables.

### Nivel 3: Automatizacion avanzada (integraciones API + IA)

El nivel mas maduro combina integraciones nativas con sistemas fuente y capacidades de inteligencia artificial:

- **Colectores API.** Integraciones directas con tu SIEM, tu herramienta de vulnerabilidades, tu directorio activo, tu ticketing y tu cloud. Las evidencias se recopilan automaticamente sin intervencion humana.
- **Clasificacion automatica.** La IA clasifica la evidencia, la vincula al control correcto y detecta anomalias (por ejemplo, una evidencia que muestra un gap de seguridad).
- **Generacion de narrativa.** La IA genera borradores de los informes de auditoria a partir de las evidencias recopiladas, que el responsable solo necesita revisar y aprobar.
- **Alertas predictivas.** El sistema predice que evidencias van a vencer antes de la proxima auditoria y genera alertas proactivas.

Riskitera opera en este nivel, con colectores automatizados que extraen evidencias de sistemas fuente, mapeo cruzado multi-framework y generacion asistida por IA de informes para auditores.

### Metricas de automatizacion

Mide el progreso de tu automatizacion con estos indicadores:

| Metrica | Baseline (manual) | Objetivo (automatizado) |
|---------|-------------------|------------------------|
| % evidencias recopiladas automaticamente | 0 - 10% | >60% |
| Tiempo medio de recopilacion por evidencia | 30 - 60 min | <5 min |
| Evidencias con hash de integridad | 0% | 100% |
| Evidencias vinculadas a controles | 40 - 60% | >95% |
| Tiempo de preparacion de auditoria | 200 - 400 h | 50 - 100 h |

## Alineacion con ISO 19011 y marcos de auditoria

La gestion de evidencias no ocurre en el vacio. Debe alinearse con los marcos de auditoria reconocidos que los auditores utilizan.

### ISO 19011: directrices para auditorias de sistemas de gestion

ISO 19011 establece los principios que guian la evaluacion de evidencias:

- **Suficiencia.** Hay evidencias suficientes para sustentar las conclusiones de la auditoria?
- **Pertinencia.** Las evidencias son relevantes para los criterios de auditoria evaluados?
- **Fiabilidad.** Las evidencias son fiables (fuentes verificables, integridad demostrable)?

Para satisfacer estos tres principios, tu sistema de gestion de evidencias debe garantizar que cada control tiene evidencia suficiente (no una sola evidencia, sino multiples fuentes que se corroboran), pertinente (vinculada explicitamente al control) y fiable (con hash, timestamp y cadena de custodia).

### Guias CCN-STIC para ENS

El [CCN-CERT](https://www.ccn-cert.cni.es/) publica guias especificas para la evidenciacion de controles ENS. Las mas relevantes:

- **CCN-STIC 802.** Guia de auditoria del ENS. Define que evidencias espera un auditor para cada control.
- **CCN-STIC 804.** Guia de implantacion del ENS. Incluye orientaciones sobre como documentar la implementacion de controles.
- **CCN-STIC 808.** Verificacion del cumplimiento. Establece los criterios de verificacion que aplican los auditores.

Si tu organizacion esta sujeta a ENS, estas guias son la referencia definitiva para saber que evidencias necesitas para cada nivel ([diferencias entre ENS Alto, Medio y Bajo](/es/posts/2026/04/ens-alto-medio-bajo-diferencias/)).

### ISAE 3402 / SOC 2 para proveedores de servicios

Si eres proveedor de servicios y tus clientes te exigen un informe SOC 2 o ISAE 3402, las evidencias deben cubrir un periodo continuo (tipicamente 6-12 meses) y demostrar la eficacia operativa de los controles a lo largo de todo ese periodo, no solo en un momento puntual. Esto requiere evidencias recurrentes y automatizadas que demuestren consistencia temporal.

## Errores fatales en la gestion de evidencias

Tras anos de auditorias, los errores se repiten. Estos son los mas frecuentes y como evitarlos.

### El sindrome del ultimo momento

Empezar a recopilar evidencias una semana antes de la auditoria. El resultado: evidencias incompletas, documentos fabricados a toda prisa, equipo estresado y auditores que detectan la improvisacion. La solucion: recopilacion continua, no puntual. Si las evidencias se generan y almacenan a lo largo del ano, la preparacion de la auditoria se reduce a verificar que todo esta completo y actualizado.

### La evidencia de cajon

Politicas y procedimientos que se escribieron para pasar la auditoria y nunca mas se revisaron. Un auditor experimentado detecta una politica "de cajon" en segundos: pide un ejemplo de aplicacion reciente y no hay ninguno. La solucion: cada politica debe tener evidencias de aplicacion real, no solo de existencia.

### La evidencia duplicada inconsistente

Copias de la misma evidencia en distintas ubicaciones con versiones diferentes. El auditor pregunta por el procedimiento de gestion de cambios y le muestras una version en el SharePoint y otra en la wiki interna, con contenido contradictorio. La solucion: repositorio unico como fuente de verdad, con enlaces (no copias) desde otros sistemas.

### La evidencia sin contexto

Un log de 10.000 lineas que "demuestra" el control de monitoring. El auditor no va a leer 10.000 lineas. Necesita un resumen ejecutivo que explique que muestra el log, que periodo cubre, que anomalias se detectaron y que acciones se tomaron. La solucion: cada evidencia tecnica debe acompanarse de una nota de contexto que la haga interpretable.

{{< cta type="bofu" text="Empieza tu PoC y descubre cuanto tiempo ahorras en cada ciclo de auditoria." label="Iniciar PoC" >}}


**Articulos relacionados:**
- [Auditoria Seguridad Informatica Guia](/es/posts/2026/04/auditoria-seguridad-informatica-guia/)
- [Automatizar auditorias de seguridad con IA](/es/posts/2026/04/automatizar-auditorias-seguridad-ia/)
- [ROI de una plataforma GRC](/es/posts/2026/07/roi-plataforma-grc-calcular/)
- [Plan director de seguridad: plantilla](/es/posts/2026/04/plan-director-seguridad-plantilla/)

## Preguntas frecuentes

### Cuanto tiempo deben conservarse las evidencias de auditoria?

Depende del framework. Para ISO 27001, la norma no especifica un periodo minimo, pero la practica habitual es conservar evidencias al menos 3 anos (dos ciclos de certificacion). Para ENS Alto, el CCN-CERT recomienda 5 anos para registros de auditoria. Para RGPD, las evidencias de cumplimiento deben conservarse mientras exista la obligacion de demostrar el cumplimiento y, en caso de inspeccion de la [AEPD](https://www.aepd.es/), la prescripcion de infracciones muy graves es de 3 anos. La regla segura: conservar al menos 5 anos las evidencias criticas y 3 anos las operativas.

### Es necesario firmar digitalmente todas las evidencias?

No es obligatorio en la mayoria de frameworks, pero si altamente recomendable para evidencias criticas (politicas aprobadas, informes de auditoria, actas de comite de seguridad). Para evidencias tecnicas automatizadas, un hash de integridad (SHA-256) con timestamp de un servidor NTP sincronizado suele ser suficiente. Para organizaciones sujetas a ENS Alto en administraciones publicas, el uso de firma electronica cualificada (conforme a eIDAS y la Ley 39/2015) puede ser exigido por el auditor para determinados documentos.

### Que pasa si un auditor solicita una evidencia que no tenemos?

Es un escenario habitual. Lo peor que puedes hacer es inventar una evidencia sobre la marcha. El auditor lo detectara. Lo correcto: reconocer la carencia, explicar por que no existe (no se habia identificado como necesaria, el control se implemento recientemente, el sistema no genera ese tipo de registro), proponer un plan de accion con fecha concreta para subsanarla, y documentar todo como hallazgo interno. Una no conformidad menor por evidencia ausente es preferible a una no conformidad mayor por evidencia falsificada.

### Como gestionar evidencias cuando hay multiples auditores (interno, externo, regulador)?

Usa un repositorio unico con permisos diferenciados. El auditor interno tiene acceso completo. El auditor externo de certificacion tiene acceso a las evidencias vinculadas a su alcance. El regulador (por ejemplo, [ENISA](https://www.enisa.europa.eu/) para NIS2 o la AEPD para RGPD) tiene acceso solo a lo que solicite formalmente. Nunca des acceso indiscriminado. Y registra cada acceso en la cadena de custodia.

### Puedo usar un repositorio en la nube (Google Drive, SharePoint) para almacenar evidencias?

Puedes, con condiciones. Verifica que el proveedor cloud almacena los datos en la UE (requisito RGPD). Asegurate de que tienes control de acceso granular (no basta con compartir una carpeta con "todos"). Implementa versionado (que las herramientas cloud suelen ofrecer nativamente). Y anade una capa de hash de integridad, porque las herramientas cloud no lo hacen por defecto. Para organizaciones con ENS Alto, verifica que el proveedor cumple con los requisitos de la guia CCN-STIC 823 (uso de servicios en la nube). Una plataforma GRC dedicada es siempre preferible porque integra almacenamiento, trazabilidad, vinculacion a controles y hash de integridad en un unico sistema.
