---
title: "Cómo hacer un análisis de riesgos en ciberseguridad paso a paso"
image: "cover.png"
description: "Guía paso a paso para realizar un análisis de riesgos en ciberseguridad: metodologías MAGERIT, FAIR, ISO 27005 y NIST RMF, inventario de activos, evaluación de amenazas, cálculo y tratamiento de riesgos."
slug: "análisis-riesgos-ciberseguridad-paso-a-paso"
date: 2026-03-15
lastmod: 2026-03-15
draft: false
tags: ["GRC", "Riesgos", "Metodología"]
categories: ["GRC"]
author: "David Moya"
translationKey: "risk-analysis-guide"
---

El análisis de riesgos es el proceso fundamental que permite a una organización identificar, evaluar y priorizar las amenazas a las que están expuestos sus activos de información. Sin un análisis de riesgos riguroso, las decisiones de seguridad se toman por intuición, lo que inevitablemente conduce a inversiones desproporcionadas en áreas de bajo riesgo y protección insuficiente donde realmente importa. Según datos del Informe de Amenazas de [ENISA](https://www.enisa.europa.eu/), más del 60 por ciento de las pymes europeas que sufrieron un ciberataque grave no habían realizado un análisis de riesgos formal previo. Esta guía detalla el proceso completo, las metodologías disponibles y los errores que conviene evitar.

<!--more-->

{{< key-takeaways >}}
- El análisis de riesgos es obligatorio por ENS, RGPD, NIS2, DORA e ISO 27001
- Principales metodologías: MAGERIT (referencia en España), FAIR (cuantitativa), ISO 27005 y NIST RMF
- Proceso en 7 pasos: alcance, inventario de activos, amenazas, vulnerabilidades, cálculo, priorización y tratamiento
- Debe revisarse al menos anualmente y actualizarse ante cambios significativos
- La herramienta PILAR del CCN facilita el análisis siguiendo MAGERIT
{{< /key-takeaways >}}

## ¿Por qué es imprescindible el análisis de riesgos en ciberseguridad?

El análisis de riesgos en ciberseguridad no es un ejercicio académico ni un requisito burocrático: es la base sobre la que se construye toda la estrategia de seguridad de una organización. Sus beneficios son concretos y medibles.

En primer lugar, permite asignar recursos de forma racional. Los presupuestos de seguridad son siempre limitados, y el análisis de riesgos identifica dónde cada euro invertido genera mayor reducción de riesgo. Sin esta información, las organizaciones tienden a invertir en tecnología de moda en lugar de abordar los riesgos reales.

En segundo lugar, es un requisito normativo. Regulaciones como el Esquema Nacional de Seguridad (ENS), el [RGPD](https://eur-lex.europa.eu/eli/reg/2016/679), la Directiva [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555), [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554) y el estándar [ISO 27001](/es/posts/guia-iso-27001-startups/) exigen la realización de análisis de riesgos como requisito fundamental. El artículo 32 del RGPD establece explícitamente que las medidas de seguridad deben ser proporcionales al riesgo, lo que presupone que se ha realizado una evaluación formal.

En tercer lugar, facilita la comunicación con la dirección. Un registro de riesgos bien elaborado traduce amenazas técnicas a términos de impacto empresarial (pérdida económica, interrupción del servicio, daño reputacional), permitiendo que los responsables de negocio tomen decisiones informadas.

Finalmente, proporciona un marco para la mejora continua. El análisis de riesgos no es un documento estático sino un proceso cíclico que se actualiza ante cambios en el entorno de amenazas, la infraestructura tecnológica o los requisitos de negocio.

## ¿Qué metodologías de análisis de riesgos existen?

Existen diversas metodologías reconocidas internacionalmente. La elección depende del contexto normativo, el sector y la madurez de la organización.

### MAGERIT

MAGERIT (Metodología de Análisis y Gestión de Riesgos de los Sistemas de Información) es la metodología oficial del gobierno español, desarrollada por el Consejo Superior de Administración Electrónica y mantenida por el [CCN](https://www.ccn-cert.cni.es/). Es la metodología de referencia para el cumplimiento del [Esquema Nacional de Seguridad (ENS)](/es/posts/que-es-esquema-nacional-seguridad-ens/) y es ampliamente utilizada en el sector público español y en empresas que trabajan con la administración.

MAGERIT se estructura en tres libros: el método (que describe el proceso), el catálogo de elementos (que proporciona inventarios tipificados de activos, amenazas y salvaguardas) y la guía de técnicas (que detalla técnicas complementarias como análisis de impacto o árboles de ataque).

Su enfoque es cualitativo-cuantitativo, permitiendo valorar activos y riesgos tanto en escalas numéricas como en categorías. El CCN proporciona la herramienta [PILAR](https://www.ccn-cert.cni.es/herramientas-de-ciberseguridad/ear-pilar.html) como soporte oficial para la realización de análisis MAGERIT, facilitando significativamente el proceso.

### [FAIR](https://www.fairinstitute.org/) (Factor Analysis of Information Risk)

FAIR es el único modelo cuantitativo estandarizado (por The Open Group) para medir el riesgo en términos financieros. A diferencia de las metodologías cualitativas que clasifican riesgos como "alto", "medio" o "bajo", FAIR calcula la pérdida esperada en unidades monetarias, utilizando distribuciones de probabilidad.

El modelo descompone el riesgo en factores como la frecuencia de eventos de amenaza, la probabilidad de que el evento resulte en pérdida, la magnitud de la pérdida primaria y la magnitud de las pérdidas secundarias (regulatorias, reputacionales). Esta descomposición permite identificar con precisión qué factores contribuyen más al riesgo total.

FAIR es especialmente útil para comunicar riesgos a la dirección financiera y para priorizar inversiones con base en el retorno de reducción de riesgo. Sin embargo, requiere datos históricos que no siempre están disponibles, especialmente en organizaciones menos maduras.

### [ISO 27005](https://www.iso.org/standard/80585.html)

ISO 27005 es el estándar internacional que proporciona directrices para la gestión de riesgos de seguridad de la información en el contexto de un sistema de gestión basado en ISO 27001. No prescribe una metodología concreta sino que establece un marco de proceso: establecimiento del contexto, identificación de riesgos, análisis de riesgos, evaluación de riesgos, tratamiento de riesgos y comunicación.

Su principal ventaja es la alineación directa con ISO 27001, lo que facilita la certificación. Es suficientemente flexible para adaptarse a organizaciones de cualquier tamaño y sector, permitiendo enfoques tanto cualitativos como cuantitativos.

### NIST Risk Management Framework (RMF)

El NIST RMF, descrito en la publicación especial [SP 800-37](https://csrc.nist.gov/pubs/sp/800/37/r2/final), define un proceso de gestión de riesgos en siete pasos: preparar, categorizar, seleccionar controles, implementar controles, evaluar controles, autorizar y monitorizar. Complementado con la guía [SP 800-30](https://csrc.nist.gov/pubs/sp/800/30/r1/final) para evaluación de riesgos, proporciona un marco completo y detallado.

Aunque es de origen estadounidense, el NIST RMF es ampliamente utilizado internacionalmente debido a la calidad de su documentación y la disponibilidad gratuita de todas sus publicaciones. ENISA lo referencia como uno de los marcos de referencia en sus guías de gestión de riesgos.

## ¿Cómo hacer un análisis de riesgos paso a paso?

Independientemente de la metodología elegida, el proceso de análisis de riesgos sigue una secuencia lógica común.

### Paso 1: Definición del alcance y contexto

Antes de comenzar el análisis, es imprescindible definir con claridad qué se va a analizar. El alcance puede abarcar toda la organización, un departamento, un sistema de información concreto o un proceso de negocio.

La definición del contexto incluye identificar los requisitos legales y normativos aplicables (ENS, RGPD, NIS2, ISO 27001), comprender los objetivos de negocio y la tolerancia al riesgo de la dirección, identificar las partes interesadas y sus expectativas y delimitar las fronteras tecnológicas y organizativas del análisis.

Un error frecuente es definir un alcance demasiado amplio para los recursos disponibles. Es preferible un análisis exhaustivo de un alcance reducido que un análisis superficial de toda la organización.

### Paso 2: Inventario de activos

Los activos son los elementos que tienen valor para la organización y que, por tanto, necesitan protección. El inventario debe ser exhaustivo dentro del alcance definido e incluir:

**Activos de información:** bases de datos de clientes, propiedad intelectual, documentación financiera, registros de empleados, planes estratégicos.

**Activos tecnológicos:** servidores, estaciones de trabajo, dispositivos de red, aplicaciones, servicios cloud, dispositivos móviles.

**Activos de soporte:** instalaciones físicas, suministro eléctrico, climatización, enlaces de comunicaciones.

**Activos humanos:** personal clave, conocimiento especializado no documentado.

Cada activo debe valorarse en función de su importancia para la organización, considerando las dimensiones de confidencialidad, integridad y disponibilidad. Un servidor de base de datos con información de clientes tendrá una valoración alta en confidencialidad, mientras que un servidor web público priorizará la disponibilidad.

MAGERIT proporciona un catálogo completo de tipos de activos que facilita este proceso. La herramienta PILAR del CCN permite gestionar inventarios de activos siguiendo esta clasificación.

### Paso 3: Identificación de amenazas

Para cada activo o grupo de activos, se identifican las amenazas que podrían causar un incidente de seguridad. Las amenazas se clasifican generalmente en:

**Amenazas naturales:** inundaciones, terremotos, incendios naturales, tormentas eléctricas.

**Amenazas industriales:** fallos eléctricos, fallos de climatización, fugas de agua, fallos de hardware.

**Amenazas humanas no intencionadas:** errores de configuración, eliminación accidental de datos, envío de información al destinatario equivocado.

**Amenazas humanas intencionadas:** ataques externos (ransomware, phishing, DDoS, APT), amenazas internas (empleados descontentos, espionaje industrial), ataques de ingeniería social.

Los catálogos de amenazas de MAGERIT y la taxonomía de amenazas de ENISA proporcionan listas completas que ayudan a no omitir amenazas relevantes. Los informes periódicos de [INCIBE](https://www.incibe.es/) sobre incidentes en España y el ENISA Threat Landscape ofrecen datos actualizados sobre la prevalencia de cada tipo de amenaza.

### Paso 4: Identificación de vulnerabilidades

Las vulnerabilidades son debilidades en los activos o en sus controles de seguridad que podrían ser explotadas por las amenazas identificadas. La identificación de vulnerabilidades se realiza mediante:

**Análisis técnico:** escaneos de vulnerabilidades, tests de penetración, revisiones de configuración, análisis de código fuente.

**Análisis organizativo:** revisión de políticas de seguridad, evaluación de procesos de gestión de accesos, verificación de procedimientos de backup y recuperación.

**Análisis del factor humano:** evaluación de la concienciación en seguridad, revisión de programas de formación, pruebas de phishing simulado.

Cada vulnerabilidad se valora en términos de facilidad de explotación y grado de exposición del activo afectado.

### Paso 5: Cálculo del riesgo

El riesgo se calcula combinando la probabilidad de que una amenaza explote una vulnerabilidad con el impacto que tendría para la organización. La fórmula básica es:

**Riesgo = Probabilidad x Impacto**

En enfoques cualitativos, tanto la probabilidad como el impacto se expresan en escalas categóricas (muy bajo, bajo, medio, alto, muy alto) y se combinan mediante matrices de riesgo predefinidas. En enfoques cuantitativos como FAIR, ambos factores se expresan en valores numéricos (frecuencia anual y pérdida monetaria estimada).

La probabilidad se estima considerando la frecuencia histórica de la amenaza, la motivación y capacidad de los potenciales atacantes, la facilidad de explotación de las vulnerabilidades y la eficacia de los controles existentes.

El impacto se evalúa en múltiples dimensiones: impacto financiero directo (coste de recuperación, pérdida de ingresos), impacto regulatorio (sanciones, multas), impacto reputacional (pérdida de confianza de clientes), impacto operativo (interrupción de servicios) e impacto legal (litigios, responsabilidades).

### Paso 6: Evaluación y priorización

Una vez calculado el riesgo de cada escenario, se evalúa comparándolo con los criterios de aceptación de riesgo definidos por la organización. Los riesgos que superan el umbral de aceptación requieren tratamiento; los que se sitúan por debajo pueden aceptarse formalmente.

La priorización ordena los riesgos de mayor a menor, permitiendo asignar recursos a los riesgos más críticos primero. Una representación visual mediante mapas de calor (heat maps) facilita la comunicación de los resultados a la dirección.

### Paso 7: Tratamiento de riesgos

Para cada riesgo que supera el umbral de aceptación, se selecciona una estrategia de tratamiento:

**Mitigar:** implementar controles de seguridad que reduzcan la probabilidad o el impacto. Es la opción más común. Ejemplos: instalar un EDR, implementar MFA, realizar copias de seguridad cifradas.

**Transferir:** trasladar el riesgo a un tercero, típicamente mediante un seguro cibernético o la externalización del servicio a un proveedor especializado con SLAs definidos.

**Evitar:** eliminar la actividad o el activo que genera el riesgo. Por ejemplo, dejar de almacenar datos que no son necesarios para el negocio.

**Aceptar:** reconocer formalmente el riesgo sin tomar medidas adicionales. Solo es apropiado para riesgos que se sitúan dentro de la tolerancia definida por la dirección. La aceptación debe documentarse con la aprobación explícita de un responsable autorizado.

Para cada medida de mitigación, se define un plan de implementación con responsables, plazos, recursos necesarios y métricas de eficacia.

{{< cta type="tofu" text="Riskitera automatiza el análisis de riesgos con IA, mapeando amenazas a controles ENS e ISO 27001." label="Ver cómo funciona" >}}

## ¿Qué herramientas se usan para el análisis de riesgos?

### PILAR

Desarrollada por el CCN, PILAR es la herramienta de referencia para análisis MAGERIT. Soporta todo el proceso de análisis de riesgos, desde el inventario de activos hasta la generación de informes, incluyendo los catálogos oficiales de amenazas y salvaguardas. Existe una versión simplificada (microPILAR) para organizaciones pequeñas.

### Herramientas comerciales

Plataformas como Archer (RSA), ServiceNow GRC y OneTrust proporcionan módulos completos de gestión de riesgos con workflows automatizados, dashboards en tiempo real e integración con otras funciones GRC. Riskitera automatiza el proceso de análisis de riesgos con inteligencia artificial, facilitando la identificación de activos, la evaluación de amenazas y la generación de planes de tratamiento alineados con los requisitos normativos aplicables.

### Hojas de cálculo

Aunque no son ideales para análisis complejos, las hojas de cálculo siguen siendo una herramienta válida para organizaciones pequeñas que realizan su primer análisis de riesgos. Lo importante es que la herramienta no se convierta en un obstáculo para iniciar el proceso.

## ¿Cómo se elabora un registro de riesgos?

El registro de riesgos es el documento central que consolida los resultados del análisis. Cada entrada del registro debe incluir:

- Identificador único del riesgo
- Descripción del escenario de riesgo
- Activos afectados
- Amenaza y vulnerabilidad asociadas
- Valoración de probabilidad e impacto
- Nivel de riesgo inherente (antes de controles)
- Controles existentes y su eficacia
- Nivel de riesgo residual (después de controles)
- Estrategia de tratamiento seleccionada
- Responsable del riesgo (risk owner)
- Estado del plan de tratamiento
- Fecha de la última revisión

El registro de riesgos debe revisarse al menos trimestralmente y actualizarse ante cualquier cambio significativo en el entorno de amenazas, la infraestructura o los requisitos de negocio.

## ¿Cuáles son los errores comunes en el análisis de riesgos?

**Realizar el análisis una única vez.** El análisis de riesgos es un proceso continuo, no un proyecto puntual. Los riesgos evolucionan constantemente y un análisis de hace dos años puede estar completamente desactualizado.

**Sobrevalorar los riesgos tecnológicos e infravalorar los organizativos.** Muchas organizaciones se centran en vulnerabilidades técnicas y descuidan riesgos como la falta de concienciación del personal, la ausencia de procedimientos de respuesta a incidentes o la dependencia de proveedores críticos sin controles contractuales.

**No involucrar a los responsables de negocio.** El análisis de riesgos no es responsabilidad exclusiva del departamento de TI o seguridad. Los responsables de negocio deben participar en la valoración de activos y en la definición de la tolerancia al riesgo, ya que son quienes mejor comprenden el impacto real de un incidente en las operaciones.

**Utilizar escalas de valoración ambiguas.** Las escalas cualitativas deben estar claramente definidas con criterios objetivos. Si "probabilidad alta" significa cosas diferentes para cada evaluador, los resultados serán inconsistentes y poco fiables.

**Ignorar el riesgo residual.** Tras implementar controles, siempre queda un riesgo residual que debe evaluarse y compararse con el umbral de aceptación. Asumir que los controles eliminan el riesgo completamente es un error peligroso.

## ¿Cómo hacer un análisis de riesgos eficaz?

Empezar con lo crítico. No intentes analizar todo a la vez. Identifica los 10 o 20 activos más críticos y comienza por ellos. Un análisis profundo de los activos esenciales aporta más valor que un análisis superficial de todo el inventario.

Utilizar múltiples fuentes de información. No te limites a entrevistas: complementa con escaneos técnicos, revisión de incidentes históricos, informes del sector y estadísticas de organismos como INCIBE y ENISA.

Documentar las asunciones. Toda valoración de probabilidad e impacto implica asunciones. Documentarlas permite revisar y actualizar el análisis cuando la información disponible cambia.

Vincular riesgos con objetivos de negocio. Los riesgos que amenazan directamente los objetivos estratégicos de la organización deben recibir máxima atención, independientemente de su naturaleza técnica.

Automatizar donde sea posible. El inventario de activos tecnológicos, el escaneo de vulnerabilidades y la monitorización de controles pueden automatizarse para mantener el análisis actualizado de forma continua.

{{< cta type="mofu" text="Simplifica tu próximo análisis de riesgos con una plataforma que integra MAGERIT, FAIR y registro de riesgos automatizado." >}}

## Lo que más preguntan los equipos de seguridad

### ¿Cada cuánto debo actualizar el análisis de riesgos

El análisis de riesgos debe revisarse como mínimo anualmente de forma completa. Además, debe actualizarse ante cambios significativos: incorporación de nuevos sistemas o servicios, cambios en la normativa aplicable, incidentes de seguridad relevantes (propios o del sector), cambios organizativos importantes o resultados de auditorías. Las normas ISO 27001 y el ENS exigen la revisión periódica del análisis de riesgos como requisito de cumplimiento.

### ¿Qué metodología es mejor para una pyme

Para una pyme española, MAGERIT con la herramienta microPILAR es una opción sólida que facilita el cumplimiento del ENS si aplica. ISO 27005 es adecuada si la organización aspira a la certificación ISO 27001. Para pymes que quieren un enfoque práctico sin formalismos excesivos, el marco [NIST CSF](https://www.nist.gov/cyberframework) incluye una función de evaluación de riesgos accesible. Lo importante no es elegir la metodología perfecta sino comenzar el proceso con la que mejor se adapte a los recursos disponibles.

### ¿Necesito un consultor externo para hacer el análisis de riesgos

No es estrictamente necesario, pero es recomendable para organizaciones que realizan el análisis por primera vez o que carecen de personal con experiencia en gestión de riesgos. Un consultor externo aporta perspectiva independiente, conocimiento de mejores prácticas y experiencia de otros sectores. En cualquier caso, el conocimiento interno de la organización es insustituible: el consultor facilita el proceso, pero los responsables de negocio y TI deben participar activamente.

### ¿Cómo integro el análisis de riesgos con el cumplimiento normativo

El análisis de riesgos es el eje central que conecta todos los requisitos normativos. Las medidas de seguridad exigidas por el ENS, ISO 27001, NIS2 o RGPD deben ser proporcionales al riesgo identificado. Un análisis de riesgos bien realizado justifica las medidas implementadas, identifica las brechas de cumplimiento y prioriza las acciones correctivas. Es recomendable mapear los riesgos contra los requisitos de cada normativa aplicable para asegurar la cobertura completa.

### ¿Qué hago si la dirección no apoya el proceso de análisis de riesgos

La clave es comunicar el valor en términos de negocio, no en términos técnicos. Presenta datos concretos: el coste medio de una brecha de datos en el sector, las sanciones regulatorias aplicables, ejemplos de incidentes en organizaciones comparables y el coste de no actuar frente al coste de realizar el análisis. Los informes de INCIBE y ENISA proporcionan estadísticas que pueden utilizarse para este propósito. Si la organización está sujeta a normativas que exigen el análisis de riesgos, el argumento regulatorio es adicional e ineludible.
