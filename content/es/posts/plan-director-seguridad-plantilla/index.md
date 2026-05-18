---
title: "Plan director de seguridad: plantilla y guía pasó a pasó"
description: "Guía completa para elaborar un plan director de seguridad de la información: estructura, contenido mínimo, priorización de proyectos, presupuesto y plantilla descargable."
slug: "plan-director-seguridad-plantilla"
date: 2026-06-13
publishDate: 2026-06-13
lastmod: 2026-06-13
draft: false
tags: ["GRC", "Seguridad", "Compliance"]
categories: ["GRC"]
author: "David Moya"
keyword: "plan director seguridad"
funnel: "mofu"
---

Guía completa para elaborar un plan director de seguridad de la información: estructura, contenido mínimo, priorización de proyectos, presupuesto y plantilla descargable.

<!--more-->

{{< key-takeaways >}}
- El plan director de seguridad es el documento estratégico que alinea la ciberseguridad con los objetivos de negocio y el cumplimiento normativo (ENS, NIS2, ISO 27001).
- Su estructura mínima incluye alcance, análisis de riesgos, plan de acción con proyectos priorizados, presupuesto estimado y KPIs de seguimiento.
- La duración típica es de 12 a 36 meses, con revisiones trimestrales y un ciclo completo de mejora continua.
- Conseguir la aprobación de la dirección requiere traducir riesgos técnicos en impacto económico y regulatorio.
- Errores comunes como omitir la fase de análisis previo o no asignar responsables concretos pueden invalidar todo el esfuerzo.
{{< /key-takeaways >}}

## Qué es un plan director de seguridad

Un plan director de seguridad (PDS) es el documento estratégico que define como una organización va a proteger sus activos de información durante un periodo determinado, normalmente entre uno y tres años. No es un documento técnico aislado: es la hoja de ruta que conecta la estrategia de negocio con las medidas de protección necesarias para operar con garantías.

El PDS responde a tres preguntas fundamentales:

1. **Donde estamos ahora** en materia de seguridad (análisis de situación actual).
2. **Donde queremos llegar** (nivel de madurez objetivo, requisitos normativos).
3. **Como vamos a llegar** (proyectos, recursos, plazos, responsables).

A diferencia de una política de seguridad (que establece principios generales) o de un procedimiento operativo (que detalla cómo ejecutar una tarea concreta), el plan director opera a nivel estratégico. Es el puente entre la declaración de intenciones de la alta dirección y la ejecución técnica del equipo de seguridad.

### Base legal y normativa

El [Esquema Nacional de Seguridad (ENS)](https://www.boe.es/eli/es/rd/2022/05/03/311), regulado por el Real Decreto 311/2022, establece en su artículo 12 la obligatoriedad de que las administraciones públicas y sus proveedores cuenten con una planificación adecuada de la seguridad. Aunque no usa literalmente el término "plan director", el ENS exige:

- Un análisis de riesgos proporcional a la categoría del sistema.
- Medidas de seguridad organizativas, operacionales y de protección.
- Un proceso de mejora continua documentado.
- Auditorías periódicas (al menos cada dos años para categoría Alta).

El [Centro Criptológico Nacional (CCN-CERT)](https://www.ccn-cert.cni.es/) pública la serie de guías CCN-STIC 800 que detalla cómo elaborar e implementar estos planes. En particular, la guía CCN-STIC 825 proporciona un marco de referencia para la gestión de la seguridad de la información qué es directamente aplicable al PDS.

Más allá del ámbito público, normativas como [ISO 27001](https://www.iso.org/standard/27001) (cláusula 6.2, objetivos de seguridad y planificación para conseguirlos), la directiva [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555) y el reglamento [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554) para el sector financiero exigen planificación estratégica equivalente. Cualquier empresa que quiera certificarse o demostrar cumplimiento normativo necesita un PDS formal.

### Quien necesita un plan director

La respuesta corta: toda organización que gestione información con valor. La respuesta larga depende del contexto:

- **Administraciones públicas**: obligatorio por el ENS.
- **Operadores de servicios esenciales**: obligatorio por NIS2 (transposición nacional).
- **Entidades financieras**: obligatorio por DORA (aplicable desde enero 2025).
- **Empresas con certificación ISO 27001**: necesario para cumplir las cláusulas 6 y 8.
- **Pymes y startups**: recomendable cuando gestionan datos personales, propiedad intelectual o infraestructura crítica de clientes.

La diferencia entre tener un PDS y no tenerlo es la diferencia entre reaccionar a incidentes (modo bombero) y gestionar la seguridad de forma proactiva con recursos asignados y objetivos medibles.

## Estructura y contenido mínimo del plan director

Un PDS completo se organiza en secciones que van desde el contexto estratégico hasta los detalles de ejecución. A continuación se describe cada sección con el nivel de detalle necesario para que el documento sea operativo.

### Sección 1: Resumen ejecutivo

El resumen ejecutivo es la primera página que leera la dirección. Debe contener:

- Objetivo del plan en una frase.
- Periodo de vigencia (ej. enero 2026 a diciembre 2027).
- Presupuesto total estimado.
- Principales riesgos identificados (3 a 5 como máximo).
- Beneficios esperados (reducción de riesgo, cumplimiento normativo, ventaja competitiva).

No debe superar las dos páginas. Si la dirección no entiende el resumen, no aprobara el presupuesto.

### Sección 2: Alcance y contexto

Define los límites del plan:

- **Alcance organizativo**: que unidades de negocio, filiales o departamentos cubre.
- **Alcance tecnológico**: que sistemas, redes, aplicaciones y servicios cloud están incluidos.
- **Alcance geográfico**: ubicaciones físicas, centros de datos, teletrabajo.
- **Exclusiones explícitas**: que queda fuera y por que (ej. "se excluye la filial en proceso de desinversión").

El contexto incluye:

- Marco normativo aplicable (ENS, NIS2, DORA, RGPD, sectorial).
- Estructura organizativa del area de seguridad.
- Estado de madurez actual (resultado del análisis previo).
- Dependencias con otros planes corporativos (plan de continuidad, plan tecnológico).

### Sección 3: Análisis de la situación actual

Esta sección documenta el punto de partida. Es el diagnóstico que justifica todo lo demás. Incluye:

**Inventario de activos**: catalogación de los activos de información críticos, agrupados por tipo (información, servicios, aplicaciones, equipamiento, instalaciones, personas). El [CCN-CERT](https://www.ccn-cert.cni.es/) recomienda usar la herramienta PILAR o la metodología MAGERIT para esta tarea.

**Análisis de riesgos**: identificación de amenazas, vulnerabilidades y cálculo del riesgo residual. El ENS exige que el análisis sea proporcional a la categoría del sistema. Para categoría Alta, se necesita un análisis formal con metodología reconocida (MAGERIT, NIST SP 800-30, ISO 27005).

**Evaluación de madurez**: comparación del estado actual con un marco de referencia. Las opciones más habituales son:

| Marco | Niveles | Aplicación |
|-------|---------|------------|
| CMMI para seguridad | 1-5 (Inicial a Optimizado) | General |
| ENS (CCN-STIC 804) | Básica, Media, Alta | Sector público español |
| NIST CSF | Tiers 1-4 | General, muy usado en EE.UU. |
| CIS Controls v8 | IG1, IG2, IG3 | Priorización práctica |

**Gap analysis**: diferencia entre el estado actual y el objetivo. Cada gap se convierte en un proyecto o acción dentro del plan.

### Sección 4: Objetivos estratégicos de seguridad

Los objetivos deben ser SMART (específicos, medibles, alcanzables, relevantes, temporales). Ejemplos:

- "Alcanzar certificación ENS categoría Alta antes del Q4 2027."
- "Reducir el tiempo medio de detección (MTTD) de incidentes de 72h a 8h en 12 meses."
- "Implementar MFA en el 100% de los accesos remotos antes del Q2 2026."
- "Reducir el número de vulnerabilidades críticas sin parchear a menos de 5 en cualquier momento."

Cada objetivo debe tener un responsable, un indicador de medida y una fecha límite.

### Sección 5: Plan de acción (proyectos de seguridad)

El núcleo del PDS. Cada proyecto se documenta con una ficha que incluye:

- **Código y nombre**: ej. PDS-2026-001: Despliegue de SIEM.
- **Objetivo**: que gap o riesgo aborda.
- **Alcance**: sistemas o procesos afectados.
- **Responsable**: persona o equipo.
- **Plazo**: fecha inicio, fecha fin, hitos intermedios.
- **Presupuesto estimado**: desglosado en CAPEX y OPEX.
- **Dependencias**: otros proyectos que deben completarse antes.
- **Prioridad**: resultado de la priorización (ver sección correspondiente).
- **KPI asociado**: como se medira el éxito.

Ejemplos típicos de proyectos en un PDS:

1. Implantación o mejora del SIEM.
2. Programa de concienciación y formación.
3. Gestión de identidades y accesos (IAM/PAM).
4. Segmentación de red.
5. Plan de respuesta a incidentes.
6. Gestión de vulnerabilidades.
7. Backup y recuperación ante desastres.
8. Seguridad en el desarrollo (DevSecOps).
9. Protección de endpoints (EDR/XDR).
10. Cumplimiento normativo específico (ENS, NIS2, DORA).

### Sección 6: Presupuesto

Se detalla en la sección específica más adelante, pero el PDS debe incluir al menos:

- Presupuesto total por anualidad.
- Desglose por proyecto.
- Separación CAPEX (inversiones) y OPEX (gastos recurrentes).
- Reserva para contingencias (10-15% recomendado).

### Sección 7: Cronograma

Un diagrama de Gantt o timeline que muestre:

- Distribución de proyectos en el tiempo.
- Dependencias entre proyectos.
- Hitos clave y puntos de revisión.
- Alineación con ciclos presupuestarios de la organización.

### Sección 8: Gobernanza y seguimiento

- Comité de seguridad: composición, frecuencia de reuniones, competencias.
- Cuadro de mando con KPIs (ver sección dedicada).
- Frecuencia de revisión del plan (trimestral recomendado).
- Procedimiento de cambios al plan (quien aprueba modificaciones de alcance o presupuesto).
- Reporting a la dirección: formato, frecuencia, destinatarios.

### Sección 9: KPIs y métricas

Los indicadores clave deben cubrir las cuatro perspectivas:

**Riesgo**:
- Número de riesgos críticos sin tratar.
- Porcentaje de reducción de riesgo respecto al baseline.
- Cobertura de controles sobre activos críticos.

**Operaciones**:
- MTTD (tiempo medio de detección).
- MTTR (tiempo medio de respuesta/resolución).
- Número de incidentes por severidad y mes.
- Porcentaje de vulnerabilidades críticas parcheadas en SLA.

**Cumplimiento**:
- Porcentaje de controles ENS/NIS2/ISO implementados.
- Hallazgos de auditoría abiertos vs cerrados.
- Días de retraso en acciones correctivas.

**Personas**:
- Porcentaje de empleados que completaron la formación.
- Tasa de click en simulaciones de phishing.
- Cobertura de personal certificado (CISSP, CISM, CEH).

## Elaboración del plan director en 6 fases: del diagnóstico al seguimiento

El proceso de elaboración sigue una secuencia lógica que no conviene alterar. Saltarse pasos (especialmente el análisis de situación) es el error más frecuente y el más costoso.

### Paso 1: Obtén el compromiso de la dirección

Antes de empezar a trabajar, necesitas dos cosas de la alta dirección:

1. **Mandato formal**: un documento (puede ser un acta de comite) que encargue la elaboración del PDS, nombre al responsable y asigne recursos para el proyecto.
2. **Sponsor ejecutivo**: un miembro del comité de dirección que respalda el proyecto y facilite el acceso a las distintas areas.

Sin este pasó, el PDS será un ejercicio académico que nadie implementara.

### Paso 2: Define el alcance

Reúne al sponsor, al CISO (o responsable de seguridad), al CIO y a los responsables de las áreas principales. En una sesión de 2 a 4 horas, acuerda:

- Que unidades de negocio entran.
- Que marco normativo aplica.
- Nivel de profundidad del análisis de riesgos.
- Plazo para entregar el borrador del PDS.

### Paso 3: Analiza la situación actual

Dedica entre 4 y 8 semanas a este pasó. Las actividades son:

1. **Inventario de activos**: recopila la información de CMDB, entrevistas con responsables de area, documentación existente.
2. **Análisis de riesgos**: aplica la metodología seleccionada (MAGERIT si es sector público, ISO 27005 o NIST si es privado). Identifica amenazas, vulnerabilidades, calcula impacto y probabilidad.
3. **Evaluación de madurez**: aplica el framework elegido. Entrevista a los responsables de cada dominio, revisa evidencias, puntua cada control.
4. **Gap analysis**: compara el estado actual con el objetivo. Cada gap se anota como un posible proyecto.

### Paso 4: Define los objetivos estratégicos

Con el gap analysis sobre la mesa, establece los objetivos. Prioriza por:

- Requisitos legales y regulatorios (no negociables).
- Riesgos críticos (impacto alto, probabilidad alta).
- Quick wins (bajo coste, alto impacto visible).
- Requisitos de negocio (habilitadores de nuevos servicios o mercados).

### Paso 5: Disena los proyectos de seguridad

Para cada gap relevante, crea una ficha de proyecto con la información descrita en la sección de estructura. Agrupa los proyectos en dominios (personas, procesos, tecnología) y establece dependencias.

### Paso 6: Prioriza y temporaliza

Usa una matriz de priorización (ver sección dedicada). Distribuye los proyectos en el timeline respetando dependencias, capacidad del equipo y ciclos presupuestarios.

### Paso 7: Estima el presupuesto

Solicita estimaciones a proveedores, consulta benchmarks del sector, incluye costes internos (horas de personal) y externos (consultoría, licencias, hardware).

### Paso 8: Documenta y presenta

Redacta el documento completo. Prepara una presentación ejecutiva de 15 a 20 diapositivas para la dirección. Incluye al menos:

- Los 5 riesgos principales y su impacto económico potencial.
- El coste del plan vs el coste de no hacer nada (análisis coste-beneficio).
- El roadmap visual con los hitos principales.
- Los beneficios tangibles (cumplimiento, reducción de riesgo, eficiencia).

### Paso 9: Aprueba y ejecuta

Presenta al comité de dirección. Incorpora feedback. Obtiene la aprobación formal. Comunica el plan a toda la organización (al menos el resumen ejecutivo y los hitos que afectan a cada area).

### Paso 10: Monitoriza y revisa

El plan no es un documento estático. Establece:

- Reuniónes trimestrales de seguimiento con el comité de seguridad.
- Revisión anual completa del plan (o antes si hay cambios significativos en el contexto).
- Actualización del análisis de riesgos ante nuevas amenazas o cambios organizativos.

{{< cta type="tofu" text="Riskitera evalua tu postura de seguridad y te muestra los gaps de cumplimiento en minutos." label="Evaluar postura" >}}

## Matriz de priorización: impacto, urgencia y coste de cada proyecto

No todos los proyectos pueden ejecutarse a la vez. La priorización es crítica para asignar recursos limitados a las acciones que generan mayor impacto.

### Matriz de priorización

El método más práctico combina dos ejes:

| | Impacto Alto | Impacto Bajo |
|---|---|---|
| **Esfuerzo Bajo** | Quick wins (hacer primero) | Rellenar huecos (hacer si sobra capacidad) |
| **Esfuerzo Alto** | Proyectos estratégicos (planificar bien) | Aparcar (no justificables ahora) |

### Criterios de priorización

Cada proyecto se evalúa contra estos criterios (puntuación 1 a 5):

1. **Reducción de riesgo**: cuanto baja el nivel de riesgo residual.
2. **Requisito normativo**: si es obligatorio para cumplimiento (ENS, NIS2, DORA).
3. **Impacto en negocio**: si habilita nuevas capacidades o protege ingresos.
4. **Complejidad de implementación**: recursos, tiempo, dependencias técnicas.
5. **Madurez organizativa**: si la organización está preparada para absorber el cambio.
6. **Visibilidad**: si es un proyecto que la dirección percibe como valioso (no subestimes este criterio).

La puntuación ponderada genera un ranking que se cruza con las dependencias técnicas para producir el cronograma final.

### Ejemplo práctico de priorización

Supongamos un PDS con 10 proyectos. Tras la evaluación:

| Proyecto | Riesgo | Normativo | Negocio | Complejidad | Total |
|----------|--------|-----------|---------|-------------|-------|
| MFA accesos remotos | 5 | 5 | 3 | 2 | 15 |
| SIEM/SOC | 4 | 4 | 3 | 4 | 15 |
| Formación empleados | 3 | 4 | 2 | 1 | 10 |
| Segmentación red | 4 | 3 | 2 | 4 | 13 |
| Backup y DR | 5 | 3 | 4 | 3 | 15 |

En este caso, MFA, SIEM y Backup comparten puntuación máxima. MFA tiene la menor complejidad, así que sería el primer quick win. El SIEM tiene mayor complejidad, así que requiere más planificación y se programa para un segundo trimestre.

## Cómo estimar el presupuesto del plan director

El presupuesto es donde muchos PDS se caen. Si la estimación no es realista, la dirección no aprueba; si es demasiado optimista, los proyectos se quedan sin fondos a medio camino.

### Categorías de coste

Cada proyecto del PDS genera costes en estas categorías:

**CAPEX (inversiones)**:
- Hardware (firewalls, servidores, appliances).
- Licencias de software (perpetuas).
- Infraestructura (cableado, CPD, obra civil).
- Consultoría de implementación.

**OPEX (gasto recurrente anual)**:
- Suscripciones SaaS (SIEM cloud, EDR, IAM).
- Mantenimiento y soporte de hardware.
- Personal dedicado (salarios, formación).
- Servicios gestionados (SOC externo, pentesting periódico).
- Seguros ciber.

### Benchmarks del sector

Los datos del sector ayudan a contextualizar el presupuesto:

- **Gasto en seguridad como porcentaje de TI**: la media en Europa se sitúa entre el 8% y el 14% del presupuesto de TI. Organizaciones con requisitos regulatorios altos (finanzas, sanidad) superan el 15%.
- **Coste medio de un SOC interno básico**: entre 300.000 EUR y 600.000 EUR anuales (personal, herramientas, infraestructura) para una organización mediana.
- **SOC gestionado (MSSP)**: entre 5.000 EUR y 25.000 EUR mensuales dependiendo del alcance.
- **Programa de concienciación**: entre 5.000 EUR y 30.000 EUR anuales dependiendo del tamaño de la plantilla y la plataforma elegida.
- **Auditoría ENS**: entre 15.000 EUR y 50.000 EUR por ciclo de auditoría, según el alcance.

### Cómo presentar el presupuesto a la dirección

La dirección no quiere ver una lista de partidas técnicas. Quiere entender la relación coste-beneficio. Prepara:

1. **Escenario de no hacer nada**: coste estimado de un incidente grave (downtime, multas RGPD, daño reputacional). Usa datos de informes como el IBM Cost of a Data Breach.
2. **ROI del plan**: reducción de riesgo cuantificada vs inversión. Ejemplo: "Invertir 200.000 EUR en el programa de seguridad reduce el riesgo esperado de un incidente de 1.2M EUR en un 70%".
3. **Comparación con el mercado**: "Nuestro gasto actual en seguridad es del 4% de TI. La media del sector es del 12%. Proponemos alcanzar el 10% en dos años".
4. **Plan de pagos**: distribuir el presupuesto en anualidades facilita la aprobación. Prioriza las inversiones que generan retorno rápido en el primer año.

## Cronograma de 12 meses: ejemplo práctico

Un PDS de 12 meses para una organización mediana (200 a 500 empleados) podría seguir este esquema:

### Trimestre 1 (meses 1 a 3): Fundamentos

- **Mes 1**: Constituir comité de seguridad. Aprobar política de seguridad. Inventario de activos críticos.
- **Mes 2**: Análisis de riesgos inicial. Evaluación de madurez baseline.
- **Mes 3**: Despliegue de MFA en accesos remotos (quick win). Inicio del programa de concienciación (primer modulo).

### Trimestre 2 (meses 4 a 6): Visibilidad

- **Mes 4**: Selección e implantación del SIEM (si no existe) o mejora de reglas.
- **Mes 5**: Revisión y hardening de configuraciones (CIS Benchmarks). Gestión de vulnerabilidades: primer escaneo completo.
- **Mes 6**: Plan de respuesta a incidentes documentado y primer ejercicio tabletop.

### Trimestre 3 (meses 7 a 9): Protección

- **Mes 7**: Despliegue de EDR/XDR en endpoints críticos.
- **Mes 8**: Segmentación de red (fase 1: separación IT/OT, DMZ).
- **Mes 9**: Revisión de gestión de identidades y accesos. Implementación de PAM para cuentas privilegiadas.

### Trimestre 4 (meses 10 a 12): Madurez y continuidad

- **Mes 10**: Pruebas de recuperación ante desastres. Validación de backups.
- **Mes 11**: Auditoría interna del PDS. Medición de KPIs vs baseline.
- **Mes 12**: Informe de cierre del primer ciclo. Presentación de resultados a la dirección. Planificación del segundo año.

Este cronograma es una referencia. Cada organización debe adaptarlo a su contexto, pero el principio es siempre el mismo: fundamentos primero, protección después, madurez continua.

## Cómo conseguir la aprobación de la dirección

La mayor barrera para un PDS no es técnica: es política. Convencer a la dirección requiere hablar su idioma.

### Traduce riesgos técnicos a impacto de negocio

La dirección no entiende (ni necesita entender) que es un exploit de día cero. Pero entiende perfectamente:

- "Si un ransomware cifra nuestros sistemas, estaremos parados entre 5 y 15 días. El coste estimado es de 50.000 EUR por día de inactividad más el rescate potencial."
- "Si sufrimos una brecha de datos personales, la multa RGPD puede llegar al 4% de la facturación anual."
- "Tres de nuestros clientes principales exigen certificación ENS/ISO 27001 para renovar contrato. Sin ella, perdemos 1.5M EUR en renovaciones."

### Usa el lenguaje del comité de dirección

| En lugar de... | Di... |
|---|---|
| "Necesitamos un SIEM" | "Necesitamos detectar ataques antes de que causen daño, como hacen el 80% de las empresas de nuestro tamaño" |
| "Hay 47 vulnerabilidades críticas" | "Tenemos 47 puertas abiertas que un atacante puede usar para entrar en nuestros sistemas" |
| "Falta segmentación de red" | "Si un atacante entra, puede moverse libremente por toda la organización. Queremos compartimentar para limitar el daño" |

### Estructura de la presentación ejecutiva

1. **Contexto regulatorio**: que nos obliga la ley (2 slides).
2. **Estado actual**: resultado del análisis, principales riesgos (3 slides).
3. **Que puede pasar si no actuamos**: escenarios de impacto con cifras (2 slides).
4. **El plan propuesto**: roadmap visual, proyectos principales (3 slides).
5. **Presupuesto y ROI**: inversión vs riesgo evitado (2 slides).
6. **Solicitud concreta**: aprobación del presupuesto y del mandato (1 slide).

Un error común: presentar 40 diapositivas llenas de jerga técnica. Máximo 15, lenguaje ejecutivo, cifras de negocio.

## Plantilla: secciones detalladas del PDS

A continuación se describe la plantilla completa que puedes usar como base para tu plan director. Cada sección incluye su contenido esperado y la extensión orientativa.

### 1. Portada y control de versiones (1 página)

- Titulo: "Plan Director de Seguridad de la Información [Nombre Organización]".
- Periodo de vigencia.
- Versión, fecha, autor, revisores, aprobador.
- Clasificación del documento (confidencial, uso interno).

### 2. Resumen ejecutivo (1 a 2 páginas)

- Objetivo del plan.
- Principales hallazgos del análisis.
- Proyectos prioritarios.
- Presupuesto total.
- Resultado esperado.

### 3. Alcance y contexto (2 a 3 páginas)

- Alcance organizativo, tecnológico, geográfico.
- Marco normativo aplicable.
- Estructura de gobernanza de seguridad.
- Relación con otros planes corporativos.

### 4. Análisis de situación actual (10 a 15 páginas)

- Inventario de activos críticos (resumen; detalle en anexo).
- Análisis de riesgos (metodología, resultados, mapa de calor).
- Evaluación de madurez (tabla de puntuaciones por dominio).
- Gap analysis (tabla de brechas con prioridad).

### 5. Objetivos estratégicos (2 a 3 páginas)

- Lista de objetivos SMART.
- Alineación con objetivos de negocio.
- Indicadores de medida por objetivo.

### 6. Plan de acción (10 a 20 páginas)

- Fichas de proyecto (una por proyecto).
- Tabla resumen con prioridades y plazos.
- Diagrama de dependencias.

### 7. Cronograma (2 a 3 páginas)

- Diagrama de Gantt o timeline.
- Hitos clave y puntos de revisión.

### 8. Presupuesto (3 a 5 páginas)

- Resumen por anualidad.
- Desglose por proyecto (CAPEX/OPEX).
- Reserva de contingencias.
- Análisis coste-beneficio.

### 9. Gobernanza y seguimiento (2 a 3 páginas)

- Comité de seguridad: composición y funcionamiento.
- Cuadro de mando (KPIs).
- Procedimiento de revisión y actualización.
- Reporting a la dirección.

### 10. Anexos

- Detalle del inventario de activos.
- Informe completo de análisis de riesgos.
- Detalle de la evaluación de madurez.
- Glosario de términos.
- Referencias normativas.

## Errores que invalidan un plan director de seguridad

Tras años trabajando en proyectos GRC, estos son los errores más frecuentes que invalidan un PDS o lo convierten en papel mojado:

### Error 1: Saltarse el análisis de situación

Es el error más grave. Sin un diagnóstico real, el PDS es una lista de deseos sin base. Los proyectos no estarán priorizados por riesgo real, sino por intuición o por la última noticia de ciberseguridad que leyo el CIO.

### Error 2: No involucrar a la dirección desde el principio

Si la dirección solo ve el PDS cuando esta terminado, lo más probable es que lo cuestione, lo modifique radicalmente o lo aparque. Involucra al sponsor ejecutivo en los hitos clave: kick-off, resultados del análisis, priorización, presupuesto.

### Error 3: Plan excesivamente ambicioso

Un PDS con 30 proyectos en 12 meses para un equipo de seguridad de tres personas es inviable. Mejor 8 proyectos bien ejecutados que 30 a medias. La priorización existe para esto.

### Error 4: No asignar responsables concretos

"El departamento de TI se encargara" no es una asignación válida. Cada proyecto necesita un nombre y un apellido como responsable, con capacidad y autoridad para ejecutarlo.

### Error 5: KPIs ausentes o irrelevantes

Sin métricas, no hay forma de saber si el plan funciona. Y las métricas deben ser relevantes: "número de reglas de firewall" no dice nada; "porcentaje de incidentes detectados en menos de 4 horas" si.

### Error 6: No presupuestar el mantenimiento

Muchos PDS incluyen el coste de implementar una solución pero olvidan el coste de operarla. Un SIEM sin personal que revise las alertas es una inversión desperdiciada.

### Error 7: Documento estático que nadie revisa

El PDS debe revisarse trimestralmente como mínimo. Las amenazas cambian, la organización cambia, el presupuesto cambia. Un plan de 2024 ejecutado sin modificaciones en 2026 probablemente no cubra los riesgos actuales.

### Error 8: Copiar plantillas genéricas sin adaptar

Internet esta lleno de plantillas de PDS. Usarlas como punto de partida está bien; copiarlas tal cual sin adaptar al contexto de la organización es un error que los auditores detectan en cinco minutos.

{{< cta type="bofu" text="Empieza tu PoC de 90 días con Riskitera y automatiza el compliance desde el primer dia." label="Iniciar PoC" >}}


**Artículos relacionados:**
- [Análisis Riesgos Ciberseguridad Paso A Paso](/es/posts/2026/04/análisis-riesgos-ciberseguridad-paso-a-paso/)
- [Políticas Seguridad Informatica Como Crearlas](/es/posts/2026/04/politicas-seguridad-informatica-como-crearlas/)

## Preguntas frecuentes

### Cuánto tiempo se tarda en elaborar un plan director de seguridad?

Depende del tamaño y complejidad de la organización. Para una pyme de 100 a 300 empleados, entre 6 y 10 semanas es un plazo realista. Para una organización grande (más de 1.000 empleados, múltiples sedes, regulación sectorial), puede llevar de 3 a 6 meses. La fase que más tiempo consume es el análisis de riesgos y la evaluación de madurez, que requiere entrevistas con múltiples áreas y recopilación de evidencias. No conviene acortar esta fase: un diagnóstico superficial produce un plan superficial.

### Es obligatorio tener un plan director de seguridad?

Depende del sector y la normativa aplicable. Para administraciones públicas españolas y sus proveedores, el ENS (RD 311/2022) exige una planificación formal de la seguridad. La directiva NIS2 obliga a operadores de servicios esenciales e importantes a contar con medidas de gestión de riesgos documentadas. DORA impone requisitos similares al sector financiero. ISO 27001, aunque voluntaria, exige planificación de objetivos de seguridad (cláusula 6.2). Aunque para empresas privadas fuera de estos ámbitos no existe una obligación directa, tener un PDS es la forma más eficaz de demostrar diligencia debida en caso de incidente o inspección de la AEPD.

### Cuál es la diferencia entre un plan director y una política de seguridad?

La política de seguridad es un documento de alto nivel que establece los principios, compromisos y directrices generales de la organización en materia de seguridad. Es relativamente corta (5 a 15 páginas), rara vez cambia y aplica a toda la organización. El plan director, en cambio, es el documento operativo que traduce esos principios en proyectos concretos con plazos, responsables y presupuesto. Tiene vigencia temporal (1 a 3 años) y se revisa periódicamente. La política dice "que queremos conseguir"; el PDS dice "como, cuando y con que recursos".

### Puedo usar herramientas automatizadas para elaborar el plan director?

Sí, y cada vez es más recomendable. Herramientas de GRC como las que ofrece Riskitera automatizan la recopilación de evidencias, el análisis de gaps contra marcos normativos (ENS, NIS2, ISO 27001) y la generación de informes de madurez. Esto reduce el tiempo de la fase de diagnóstico y mejora la precisión. La herramienta PILAR del CCN-CERT es la referencia para el análisis de riesgos bajo MAGERIT en el ámbito público. Sin embargo, la herramienta no sustituye el juicio humano: la priorización de proyectos, la estimación de presupuesto y la negociación con la dirección requieren experiencia y conocimiento del contexto.

### Con que frecuencia hay que actualizar el plan director?

El PDS debe revisarse formalmente al menos una vez al año, con seguimiento trimestral de avance. Además, debe actualizarse de forma extraordinaria cuando se produzcan cambios significativos: una nueva normativa aplicable, un incidente grave, una fusión o adquisición, un cambio importante en la infraestructura tecnológica o una modificación sustancial del presupuesto. El ENS exige que el análisis de riesgos se revise cuando cambian las condiciones que lo motivaron. En la práctica, un PDS que no se ha tocado en más de 18 meses probablemente no refleje la situación real de la organización.
