---
title: "Plan director de seguridad: plantilla y guia paso a paso"
description: "Guia completa para elaborar un plan director de seguridad de la informacion: estructura, contenido minimo, priorizacion de proyectos, presupuesto y plantilla descargable."
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

Guia completa para elaborar un plan director de seguridad de la informacion: estructura, contenido minimo, priorizacion de proyectos, presupuesto y plantilla descargable.

<!--more-->

{{< key-takeaways >}}
- El plan director de seguridad es el documento estrategico que alinea la ciberseguridad con los objetivos de negocio y el cumplimiento normativo (ENS, NIS2, ISO 27001).
- Su estructura minima incluye alcance, analisis de riesgos, plan de accion con proyectos priorizados, presupuesto estimado y KPIs de seguimiento.
- La duracion tipica es de 12 a 36 meses, con revisiones trimestrales y un ciclo completo de mejora continua.
- Conseguir la aprobacion de la direccion requiere traducir riesgos tecnicos en impacto economico y regulatorio.
- Errores comunes como omitir la fase de analisis previo o no asignar responsables concretos pueden invalidar todo el esfuerzo.
{{< /key-takeaways >}}

## Que es un plan director de seguridad

Un plan director de seguridad (PDS) es el documento estrategico que define como una organizacion va a proteger sus activos de informacion durante un periodo determinado, normalmente entre uno y tres anos. No es un documento tecnico aislado: es la hoja de ruta que conecta la estrategia de negocio con las medidas de proteccion necesarias para operar con garantias.

El PDS responde a tres preguntas fundamentales:

1. **Donde estamos ahora** en materia de seguridad (analisis de situacion actual).
2. **Donde queremos llegar** (nivel de madurez objetivo, requisitos normativos).
3. **Como vamos a llegar** (proyectos, recursos, plazos, responsables).

A diferencia de una politica de seguridad (que establece principios generales) o de un procedimiento operativo (que detalla como ejecutar una tarea concreta), el plan director opera a nivel estrategico. Es el puente entre la declaracion de intenciones de la alta direccion y la ejecucion tecnica del equipo de seguridad.

### Base legal y normativa

El [Esquema Nacional de Seguridad (ENS)](https://www.boe.es/eli/es/rd/2022/05/03/311), regulado por el Real Decreto 311/2022, establece en su articulo 12 la obligatoriedad de que las administraciones publicas y sus proveedores cuenten con una planificacion adecuada de la seguridad. Aunque no usa literalmente el termino "plan director", el ENS exige:

- Un analisis de riesgos proporcional a la categoria del sistema.
- Medidas de seguridad organizativas, operacionales y de proteccion.
- Un proceso de mejora continua documentado.
- Auditorias periodicas (al menos cada dos anos para categoria Alta).

El [Centro Criptologico Nacional (CCN-CERT)](https://www.ccn-cert.cni.es/) publica la serie de guias CCN-STIC 800 que detalla como elaborar e implementar estos planes. En particular, la guia CCN-STIC 825 proporciona un marco de referencia para la gestion de la seguridad de la informacion que es directamente aplicable al PDS.

Mas alla del ambito publico, normativas como [ISO 27001](https://www.iso.org/standard/27001) (clausula 6.2, objetivos de seguridad y planificacion para conseguirlos), la directiva [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555) y el reglamento [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554) para el sector financiero exigen planificacion estrategica equivalente. Cualquier empresa que quiera certificarse o demostrar cumplimiento normativo necesita un PDS formal.

### Quien necesita un plan director

La respuesta corta: toda organizacion que gestione informacion con valor. La respuesta larga depende del contexto:

- **Administraciones publicas**: obligatorio por el ENS.
- **Operadores de servicios esenciales**: obligatorio por NIS2 (transposicion nacional).
- **Entidades financieras**: obligatorio por DORA (aplicable desde enero 2025).
- **Empresas con certificacion ISO 27001**: necesario para cumplir las clausulas 6 y 8.
- **Pymes y startups**: recomendable cuando gestionan datos personales, propiedad intelectual o infraestructura critica de clientes.

La diferencia entre tener un PDS y no tenerlo es la diferencia entre reaccionar a incidentes (modo bombero) y gestionar la seguridad de forma proactiva con recursos asignados y objetivos medibles.

## Estructura y contenido minimo del plan director

Un PDS completo se organiza en secciones que van desde el contexto estrategico hasta los detalles de ejecucion. A continuacion se describe cada seccion con el nivel de detalle necesario para que el documento sea operativo.

### Seccion 1: Resumen ejecutivo

El resumen ejecutivo es la primera pagina que leera la direccion. Debe contener:

- Objetivo del plan en una frase.
- Periodo de vigencia (ej. enero 2026 a diciembre 2027).
- Presupuesto total estimado.
- Principales riesgos identificados (3 a 5 como maximo).
- Beneficios esperados (reduccion de riesgo, cumplimiento normativo, ventaja competitiva).

No debe superar las dos paginas. Si la direccion no entiende el resumen, no aprobara el presupuesto.

### Seccion 2: Alcance y contexto

Define los limites del plan:

- **Alcance organizativo**: que unidades de negocio, filiales o departamentos cubre.
- **Alcance tecnologico**: que sistemas, redes, aplicaciones y servicios cloud estan incluidos.
- **Alcance geografico**: ubicaciones fisicas, centros de datos, teletrabajo.
- **Exclusiones explicitas**: que queda fuera y por que (ej. "se excluye la filial en proceso de desinversion").

El contexto incluye:

- Marco normativo aplicable (ENS, NIS2, DORA, RGPD, sectorial).
- Estructura organizativa del area de seguridad.
- Estado de madurez actual (resultado del analisis previo).
- Dependencias con otros planes corporativos (plan de continuidad, plan tecnologico).

### Seccion 3: Analisis de la situacion actual

Esta seccion documenta el punto de partida. Es el diagnostico que justifica todo lo demas. Incluye:

**Inventario de activos**: catalogacion de los activos de informacion criticos, agrupados por tipo (informacion, servicios, aplicaciones, equipamiento, instalaciones, personas). El [CCN-CERT](https://www.ccn-cert.cni.es/) recomienda usar la herramienta PILAR o la metodologia MAGERIT para esta tarea.

**Analisis de riesgos**: identificacion de amenazas, vulnerabilidades y calculo del riesgo residual. El ENS exige que el analisis sea proporcional a la categoria del sistema. Para categoria Alta, se necesita un analisis formal con metodologia reconocida (MAGERIT, NIST SP 800-30, ISO 27005).

**Evaluacion de madurez**: comparacion del estado actual con un marco de referencia. Las opciones mas habituales son:

| Marco | Niveles | Aplicacion |
|-------|---------|------------|
| CMMI para seguridad | 1-5 (Inicial a Optimizado) | General |
| ENS (CCN-STIC 804) | Basica, Media, Alta | Sector publico espanol |
| NIST CSF | Tiers 1-4 | General, muy usado en EE.UU. |
| CIS Controls v8 | IG1, IG2, IG3 | Priorizacion practica |

**Gap analysis**: diferencia entre el estado actual y el objetivo. Cada gap se convierte en un proyecto o accion dentro del plan.

### Seccion 4: Objetivos estrategicos de seguridad

Los objetivos deben ser SMART (especificos, medibles, alcanzables, relevantes, temporales). Ejemplos:

- "Alcanzar certificacion ENS categoria Alta antes del Q4 2027."
- "Reducir el tiempo medio de deteccion (MTTD) de incidentes de 72h a 8h en 12 meses."
- "Implementar MFA en el 100% de los accesos remotos antes del Q2 2026."
- "Reducir el numero de vulnerabilidades criticas sin parchear a menos de 5 en cualquier momento."

Cada objetivo debe tener un responsable, un indicador de medida y una fecha limite.

### Seccion 5: Plan de accion (proyectos de seguridad)

El nucleo del PDS. Cada proyecto se documenta con una ficha que incluye:

- **Codigo y nombre**: ej. PDS-2026-001: Despliegue de SIEM.
- **Objetivo**: que gap o riesgo aborda.
- **Alcance**: sistemas o procesos afectados.
- **Responsable**: persona o equipo.
- **Plazo**: fecha inicio, fecha fin, hitos intermedios.
- **Presupuesto estimado**: desglosado en CAPEX y OPEX.
- **Dependencias**: otros proyectos que deben completarse antes.
- **Prioridad**: resultado de la priorizacion (ver seccion correspondiente).
- **KPI asociado**: como se medira el exito.

Ejemplos tipicos de proyectos en un PDS:

1. Implantacion o mejora del SIEM.
2. Programa de concienciacion y formacion.
3. Gestion de identidades y accesos (IAM/PAM).
4. Segmentacion de red.
5. Plan de respuesta a incidentes.
6. Gestion de vulnerabilidades.
7. Backup y recuperacion ante desastres.
8. Seguridad en el desarrollo (DevSecOps).
9. Proteccion de endpoints (EDR/XDR).
10. Cumplimiento normativo especifico (ENS, NIS2, DORA).

### Seccion 6: Presupuesto

Se detalla en la seccion especifica mas adelante, pero el PDS debe incluir al menos:

- Presupuesto total por anualidad.
- Desglose por proyecto.
- Separacion CAPEX (inversiones) y OPEX (gastos recurrentes).
- Reserva para contingencias (10-15% recomendado).

### Seccion 7: Cronograma

Un diagrama de Gantt o timeline que muestre:

- Distribucion de proyectos en el tiempo.
- Dependencias entre proyectos.
- Hitos clave y puntos de revision.
- Alineacion con ciclos presupuestarios de la organizacion.

### Seccion 8: Gobernanza y seguimiento

- Comite de seguridad: composicion, frecuencia de reuniones, competencias.
- Cuadro de mando con KPIs (ver seccion dedicada).
- Frecuencia de revision del plan (trimestral recomendado).
- Procedimiento de cambios al plan (quien aprueba modificaciones de alcance o presupuesto).
- Reporting a la direccion: formato, frecuencia, destinatarios.

### Seccion 9: KPIs y metricas

Los indicadores clave deben cubrir las cuatro perspectivas:

**Riesgo**:
- Numero de riesgos criticos sin tratar.
- Porcentaje de reduccion de riesgo respecto al baseline.
- Cobertura de controles sobre activos criticos.

**Operaciones**:
- MTTD (tiempo medio de deteccion).
- MTTR (tiempo medio de respuesta/resolucion).
- Numero de incidentes por severidad y mes.
- Porcentaje de vulnerabilidades criticas parcheadas en SLA.

**Cumplimiento**:
- Porcentaje de controles ENS/NIS2/ISO implementados.
- Hallazgos de auditoria abiertos vs cerrados.
- Dias de retraso en acciones correctivas.

**Personas**:
- Porcentaje de empleados que completaron la formacion.
- Tasa de click en simulaciones de phishing.
- Cobertura de personal certificado (CISSP, CISM, CEH).

## Como se elabora un plan director paso a paso

El proceso de elaboracion sigue una secuencia logica que no conviene alterar. Saltarse pasos (especialmente el analisis de situacion) es el error mas frecuente y el mas costoso.

### Paso 1: Obten el compromiso de la direccion

Antes de empezar a trabajar, necesitas dos cosas de la alta direccion:

1. **Mandato formal**: un documento (puede ser un acta de comite) que encargue la elaboracion del PDS, nombre al responsable y asigne recursos para el proyecto.
2. **Sponsor ejecutivo**: un miembro del comite de direccion que respalda el proyecto y facilite el acceso a las distintas areas.

Sin este paso, el PDS sera un ejercicio academico que nadie implementara.

### Paso 2: Define el alcance

Reune al sponsor, al CISO (o responsable de seguridad), al CIO y a los responsables de las areas principales. En una sesion de 2 a 4 horas, acuerda:

- Que unidades de negocio entran.
- Que marco normativo aplica.
- Nivel de profundidad del analisis de riesgos.
- Plazo para entregar el borrador del PDS.

### Paso 3: Analiza la situacion actual

Dedica entre 4 y 8 semanas a este paso. Las actividades son:

1. **Inventario de activos**: recopila la informacion de CMDB, entrevistas con responsables de area, documentacion existente.
2. **Analisis de riesgos**: aplica la metodologia seleccionada (MAGERIT si es sector publico, ISO 27005 o NIST si es privado). Identifica amenazas, vulnerabilidades, calcula impacto y probabilidad.
3. **Evaluacion de madurez**: aplica el framework elegido. Entrevista a los responsables de cada dominio, revisa evidencias, puntua cada control.
4. **Gap analysis**: compara el estado actual con el objetivo. Cada gap se anota como un posible proyecto.

### Paso 4: Define los objetivos estrategicos

Con el gap analysis sobre la mesa, establece los objetivos. Prioriza por:

- Requisitos legales y regulatorios (no negociables).
- Riesgos criticos (impacto alto, probabilidad alta).
- Quick wins (bajo coste, alto impacto visible).
- Requisitos de negocio (habilitadores de nuevos servicios o mercados).

### Paso 5: Disena los proyectos de seguridad

Para cada gap relevante, crea una ficha de proyecto con la informacion descrita en la seccion de estructura. Agrupa los proyectos en dominios (personas, procesos, tecnologia) y establece dependencias.

### Paso 6: Prioriza y temporaliza

Usa una matriz de priorizacion (ver seccion dedicada). Distribuye los proyectos en el timeline respetando dependencias, capacidad del equipo y ciclos presupuestarios.

### Paso 7: Estima el presupuesto

Solicita estimaciones a proveedores, consulta benchmarks del sector, incluye costes internos (horas de personal) y externos (consultoria, licencias, hardware).

### Paso 8: Documenta y presenta

Redacta el documento completo. Prepara una presentacion ejecutiva de 15 a 20 diapositivas para la direccion. Incluye al menos:

- Los 5 riesgos principales y su impacto economico potencial.
- El coste del plan vs el coste de no hacer nada (analisis coste-beneficio).
- El roadmap visual con los hitos principales.
- Los beneficios tangibles (cumplimiento, reduccion de riesgo, eficiencia).

### Paso 9: Aprueba y ejecuta

Presenta al comite de direccion. Incorpora feedback. Obtiene la aprobacion formal. Comunica el plan a toda la organizacion (al menos el resumen ejecutivo y los hitos que afectan a cada area).

### Paso 10: Monitoriza y revisa

El plan no es un documento estatico. Establece:

- Reuniones trimestrales de seguimiento con el comite de seguridad.
- Revision anual completa del plan (o antes si hay cambios significativos en el contexto).
- Actualizacion del analisis de riesgos ante nuevas amenazas o cambios organizativos.

{{< cta type="tofu" text="Riskitera evalua tu postura de seguridad y te muestra los gaps de cumplimiento en minutos." label="Evaluar postura" >}}

## Como priorizar proyectos de seguridad

No todos los proyectos pueden ejecutarse a la vez. La priorizacion es critica para asignar recursos limitados a las acciones que generan mayor impacto.

### Matriz de priorizacion

El metodo mas practico combina dos ejes:

| | Impacto Alto | Impacto Bajo |
|---|---|---|
| **Esfuerzo Bajo** | Quick wins (hacer primero) | Rellenar huecos (hacer si sobra capacidad) |
| **Esfuerzo Alto** | Proyectos estrategicos (planificar bien) | Aparcar (no justificables ahora) |

### Criterios de priorizacion

Cada proyecto se evalua contra estos criterios (puntuacion 1 a 5):

1. **Reduccion de riesgo**: cuanto baja el nivel de riesgo residual.
2. **Requisito normativo**: si es obligatorio para cumplimiento (ENS, NIS2, DORA).
3. **Impacto en negocio**: si habilita nuevas capacidades o protege ingresos.
4. **Complejidad de implementacion**: recursos, tiempo, dependencias tecnicas.
5. **Madurez organizativa**: si la organizacion esta preparada para absorber el cambio.
6. **Visibilidad**: si es un proyecto que la direccion percibe como valioso (no subestimes este criterio).

La puntuacion ponderada genera un ranking que se cruza con las dependencias tecnicas para producir el cronograma final.

### Ejemplo practico de priorizacion

Supongamos un PDS con 10 proyectos. Tras la evaluacion:

| Proyecto | Riesgo | Normativo | Negocio | Complejidad | Total |
|----------|--------|-----------|---------|-------------|-------|
| MFA accesos remotos | 5 | 5 | 3 | 2 | 15 |
| SIEM/SOC | 4 | 4 | 3 | 4 | 15 |
| Formacion empleados | 3 | 4 | 2 | 1 | 10 |
| Segmentacion red | 4 | 3 | 2 | 4 | 13 |
| Backup y DR | 5 | 3 | 4 | 3 | 15 |

En este caso, MFA, SIEM y Backup comparten puntuacion maxima. MFA tiene la menor complejidad, asi que seria el primer quick win. El SIEM tiene mayor complejidad, asi que requiere mas planificacion y se programa para un segundo trimestre.

## Como estimar el presupuesto del plan director

El presupuesto es donde muchos PDS se caen. Si la estimacion no es realista, la direccion no aprueba; si es demasiado optimista, los proyectos se quedan sin fondos a medio camino.

### Categorias de coste

Cada proyecto del PDS genera costes en estas categorias:

**CAPEX (inversiones)**:
- Hardware (firewalls, servidores, appliances).
- Licencias de software (perpetuas).
- Infraestructura (cableado, CPD, obra civil).
- Consultoria de implementacion.

**OPEX (gasto recurrente anual)**:
- Suscripciones SaaS (SIEM cloud, EDR, IAM).
- Mantenimiento y soporte de hardware.
- Personal dedicado (salarios, formacion).
- Servicios gestionados (SOC externo, pentesting periodico).
- Seguros ciber.

### Benchmarks del sector

Los datos del sector ayudan a contextualizar el presupuesto:

- **Gasto en seguridad como porcentaje de TI**: la media en Europa se situa entre el 8% y el 14% del presupuesto de TI. Organizaciones con requisitos regulatorios altos (finanzas, sanidad) superan el 15%.
- **Coste medio de un SOC interno basico**: entre 300.000 EUR y 600.000 EUR anuales (personal, herramientas, infraestructura) para una organizacion mediana.
- **SOC gestionado (MSSP)**: entre 5.000 EUR y 25.000 EUR mensuales dependiendo del alcance.
- **Programa de concienciacion**: entre 5.000 EUR y 30.000 EUR anuales dependiendo del tamano de la plantilla y la plataforma elegida.
- **Auditoria ENS**: entre 15.000 EUR y 50.000 EUR por ciclo de auditoria, segun el alcance.

### Como presentar el presupuesto a la direccion

La direccion no quiere ver una lista de partidas tecnicas. Quiere entender la relacion coste-beneficio. Prepara:

1. **Escenario de no hacer nada**: coste estimado de un incidente grave (downtime, multas RGPD, dano reputacional). Usa datos de informes como el IBM Cost of a Data Breach.
2. **ROI del plan**: reduccion de riesgo cuantificada vs inversion. Ejemplo: "Invertir 200.000 EUR en el programa de seguridad reduce el riesgo esperado de un incidente de 1.2M EUR en un 70%".
3. **Comparacion con el mercado**: "Nuestro gasto actual en seguridad es del 4% de TI. La media del sector es del 12%. Proponemos alcanzar el 10% en dos anos".
4. **Plan de pagos**: distribuir el presupuesto en anualidades facilita la aprobacion. Prioriza las inversiones que generan retorno rapido en el primer ano.

## Cronograma de 12 meses: ejemplo practico

Un PDS de 12 meses para una organizacion mediana (200 a 500 empleados) podria seguir este esquema:

### Trimestre 1 (meses 1 a 3): Fundamentos

- **Mes 1**: Constituir comite de seguridad. Aprobar politica de seguridad. Inventario de activos criticos.
- **Mes 2**: Analisis de riesgos inicial. Evaluacion de madurez baseline.
- **Mes 3**: Despliegue de MFA en accesos remotos (quick win). Inicio del programa de concienciacion (primer modulo).

### Trimestre 2 (meses 4 a 6): Visibilidad

- **Mes 4**: Seleccion e implantacion del SIEM (si no existe) o mejora de reglas.
- **Mes 5**: Revision y hardening de configuraciones (CIS Benchmarks). Gestion de vulnerabilidades: primer escaneo completo.
- **Mes 6**: Plan de respuesta a incidentes documentado y primer ejercicio tabletop.

### Trimestre 3 (meses 7 a 9): Proteccion

- **Mes 7**: Despliegue de EDR/XDR en endpoints criticos.
- **Mes 8**: Segmentacion de red (fase 1: separacion IT/OT, DMZ).
- **Mes 9**: Revision de gestion de identidades y accesos. Implementacion de PAM para cuentas privilegiadas.

### Trimestre 4 (meses 10 a 12): Madurez y continuidad

- **Mes 10**: Pruebas de recuperacion ante desastres. Validacion de backups.
- **Mes 11**: Auditoria interna del PDS. Medicion de KPIs vs baseline.
- **Mes 12**: Informe de cierre del primer ciclo. Presentacion de resultados a la direccion. Planificacion del segundo ano.

Este cronograma es una referencia. Cada organizacion debe adaptarlo a su contexto, pero el principio es siempre el mismo: fundamentos primero, proteccion despues, madurez continua.

## Como conseguir la aprobacion de la direccion

La mayor barrera para un PDS no es tecnica: es politica. Convencer a la direccion requiere hablar su idioma.

### Traduce riesgos tecnicos a impacto de negocio

La direccion no entiende (ni necesita entender) que es un exploit de dia cero. Pero entiende perfectamente:

- "Si un ransomware cifra nuestros sistemas, estaremos parados entre 5 y 15 dias. El coste estimado es de 50.000 EUR por dia de inactividad mas el rescate potencial."
- "Si sufrimos una brecha de datos personales, la multa RGPD puede llegar al 4% de la facturacion anual."
- "Tres de nuestros clientes principales exigen certificacion ENS/ISO 27001 para renovar contrato. Sin ella, perdemos 1.5M EUR en renovaciones."

### Usa el lenguaje del comite de direccion

| En lugar de... | Di... |
|---|---|
| "Necesitamos un SIEM" | "Necesitamos detectar ataques antes de que causen dano, como hacen el 80% de las empresas de nuestro tamano" |
| "Hay 47 vulnerabilidades criticas" | "Tenemos 47 puertas abiertas que un atacante puede usar para entrar en nuestros sistemas" |
| "Falta segmentacion de red" | "Si un atacante entra, puede moverse libremente por toda la organizacion. Queremos compartimentar para limitar el dano" |

### Estructura de la presentacion ejecutiva

1. **Contexto regulatorio**: que nos obliga la ley (2 slides).
2. **Estado actual**: resultado del analisis, principales riesgos (3 slides).
3. **Que puede pasar si no actuamos**: escenarios de impacto con cifras (2 slides).
4. **El plan propuesto**: roadmap visual, proyectos principales (3 slides).
5. **Presupuesto y ROI**: inversion vs riesgo evitado (2 slides).
6. **Solicitud concreta**: aprobacion del presupuesto y del mandato (1 slide).

Un error comun: presentar 40 diapositivas llenas de jerga tecnica. Maximo 15, lenguaje ejecutivo, cifras de negocio.

## Plantilla: secciones detalladas del PDS

A continuacion se describe la plantilla completa que puedes usar como base para tu plan director. Cada seccion incluye su contenido esperado y la extension orientativa.

### 1. Portada y control de versiones (1 pagina)

- Titulo: "Plan Director de Seguridad de la Informacion [Nombre Organizacion]".
- Periodo de vigencia.
- Version, fecha, autor, revisores, aprobador.
- Clasificacion del documento (confidencial, uso interno).

### 2. Resumen ejecutivo (1 a 2 paginas)

- Objetivo del plan.
- Principales hallazgos del analisis.
- Proyectos prioritarios.
- Presupuesto total.
- Resultado esperado.

### 3. Alcance y contexto (2 a 3 paginas)

- Alcance organizativo, tecnologico, geografico.
- Marco normativo aplicable.
- Estructura de gobernanza de seguridad.
- Relacion con otros planes corporativos.

### 4. Analisis de situacion actual (10 a 15 paginas)

- Inventario de activos criticos (resumen; detalle en anexo).
- Analisis de riesgos (metodologia, resultados, mapa de calor).
- Evaluacion de madurez (tabla de puntuaciones por dominio).
- Gap analysis (tabla de brechas con prioridad).

### 5. Objetivos estrategicos (2 a 3 paginas)

- Lista de objetivos SMART.
- Alineacion con objetivos de negocio.
- Indicadores de medida por objetivo.

### 6. Plan de accion (10 a 20 paginas)

- Fichas de proyecto (una por proyecto).
- Tabla resumen con prioridades y plazos.
- Diagrama de dependencias.

### 7. Cronograma (2 a 3 paginas)

- Diagrama de Gantt o timeline.
- Hitos clave y puntos de revision.

### 8. Presupuesto (3 a 5 paginas)

- Resumen por anualidad.
- Desglose por proyecto (CAPEX/OPEX).
- Reserva de contingencias.
- Analisis coste-beneficio.

### 9. Gobernanza y seguimiento (2 a 3 paginas)

- Comite de seguridad: composicion y funcionamiento.
- Cuadro de mando (KPIs).
- Procedimiento de revision y actualizacion.
- Reporting a la direccion.

### 10. Anexos

- Detalle del inventario de activos.
- Informe completo de analisis de riesgos.
- Detalle de la evaluacion de madurez.
- Glosario de terminos.
- Referencias normativas.

## Que errores evitar al crear un plan director

Tras anos trabajando en proyectos GRC, estos son los errores mas frecuentes que invalidan un PDS o lo convierten en papel mojado:

### Error 1: Saltarse el analisis de situacion

Es el error mas grave. Sin un diagnostico real, el PDS es una lista de deseos sin base. Los proyectos no estaran priorizados por riesgo real, sino por intuicion o por la ultima noticia de ciberseguridad que leyo el CIO.

### Error 2: No involucrar a la direccion desde el principio

Si la direccion solo ve el PDS cuando esta terminado, lo mas probable es que lo cuestione, lo modifique radicalmente o lo aparque. Involucra al sponsor ejecutivo en los hitos clave: kick-off, resultados del analisis, priorizacion, presupuesto.

### Error 3: Plan excesivamente ambicioso

Un PDS con 30 proyectos en 12 meses para un equipo de seguridad de tres personas es inviable. Mejor 8 proyectos bien ejecutados que 30 a medias. La priorizacion existe para esto.

### Error 4: No asignar responsables concretos

"El departamento de TI se encargara" no es una asignacion valida. Cada proyecto necesita un nombre y un apellido como responsable, con capacidad y autoridad para ejecutarlo.

### Error 5: KPIs ausentes o irrelevantes

Sin metricas, no hay forma de saber si el plan funciona. Y las metricas deben ser relevantes: "numero de reglas de firewall" no dice nada; "porcentaje de incidentes detectados en menos de 4 horas" si.

### Error 6: No presupuestar el mantenimiento

Muchos PDS incluyen el coste de implementar una solucion pero olvidan el coste de operarla. Un SIEM sin personal que revise las alertas es una inversion desperdiciada.

### Error 7: Documento estatico que nadie revisa

El PDS debe revisarse trimestralmente como minimo. Las amenazas cambian, la organizacion cambia, el presupuesto cambia. Un plan de 2024 ejecutado sin modificaciones en 2026 probablemente no cubra los riesgos actuales.

### Error 8: Copiar plantillas genericas sin adaptar

Internet esta lleno de plantillas de PDS. Usarlas como punto de partida esta bien; copiarlas tal cual sin adaptar al contexto de la organizacion es un error que los auditores detectan en cinco minutos.

{{< cta type="bofu" text="Empieza tu PoC de 90 dias con Riskitera y automatiza el compliance desde el primer dia." label="Iniciar PoC" >}}


**Articulos relacionados:**
- [Analisis Riesgos Ciberseguridad Paso A Paso](/es/posts/2026/04/analisis-riesgos-ciberseguridad-paso-a-paso/)
- [Politicas Seguridad Informatica Como Crearlas](/es/posts/2026/04/politicas-seguridad-informatica-como-crearlas/)

## Preguntas frecuentes

### Cuanto tiempo se tarda en elaborar un plan director de seguridad?

Depende del tamano y complejidad de la organizacion. Para una pyme de 100 a 300 empleados, entre 6 y 10 semanas es un plazo realista. Para una organizacion grande (mas de 1.000 empleados, multiples sedes, regulacion sectorial), puede llevar de 3 a 6 meses. La fase que mas tiempo consume es el analisis de riesgos y la evaluacion de madurez, que requiere entrevistas con multiples areas y recopilacion de evidencias. No conviene acortar esta fase: un diagnostico superficial produce un plan superficial.

### Es obligatorio tener un plan director de seguridad?

Depende del sector y la normativa aplicable. Para administraciones publicas espanolas y sus proveedores, el ENS (RD 311/2022) exige una planificacion formal de la seguridad. La directiva NIS2 obliga a operadores de servicios esenciales e importantes a contar con medidas de gestion de riesgos documentadas. DORA impone requisitos similares al sector financiero. ISO 27001, aunque voluntaria, exige planificacion de objetivos de seguridad (clausula 6.2). Aunque para empresas privadas fuera de estos ambitos no existe una obligacion directa, tener un PDS es la forma mas eficaz de demostrar diligencia debida en caso de incidente o inspeccion de la AEPD.

### Cual es la diferencia entre un plan director y una politica de seguridad?

La politica de seguridad es un documento de alto nivel que establece los principios, compromisos y directrices generales de la organizacion en materia de seguridad. Es relativamente corta (5 a 15 paginas), rara vez cambia y aplica a toda la organizacion. El plan director, en cambio, es el documento operativo que traduce esos principios en proyectos concretos con plazos, responsables y presupuesto. Tiene vigencia temporal (1 a 3 anos) y se revisa periodicamente. La politica dice "que queremos conseguir"; el PDS dice "como, cuando y con que recursos".

### Puedo usar herramientas automatizadas para elaborar el plan director?

Si, y cada vez es mas recomendable. Herramientas de GRC como las que ofrece Riskitera automatizan la recopilacion de evidencias, el analisis de gaps contra marcos normativos (ENS, NIS2, ISO 27001) y la generacion de informes de madurez. Esto reduce el tiempo de la fase de diagnostico y mejora la precision. La herramienta PILAR del CCN-CERT es la referencia para el analisis de riesgos bajo MAGERIT en el ambito publico. Sin embargo, la herramienta no sustituye el juicio humano: la priorizacion de proyectos, la estimacion de presupuesto y la negociacion con la direccion requieren experiencia y conocimiento del contexto.

### Con que frecuencia hay que actualizar el plan director?

El PDS debe revisarse formalmente al menos una vez al ano, con seguimiento trimestral de avance. Ademas, debe actualizarse de forma extraordinaria cuando se produzcan cambios significativos: una nueva normativa aplicable, un incidente grave, una fusion o adquisicion, un cambio importante en la infraestructura tecnologica o una modificacion sustancial del presupuesto. El ENS exige que el analisis de riesgos se revise cuando cambian las condiciones que lo motivaron. En la practica, un PDS que no se ha tocado en mas de 18 meses probablemente no refleje la situacion real de la organizacion.
