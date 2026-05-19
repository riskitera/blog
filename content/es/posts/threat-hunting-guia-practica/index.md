---
title: "Threat Hunting: cómo cazar amenazas antes de que ataquen"
image: "cover.png"
description: "Guía práctica de threat hunting: metodologías PEAK y TaHiTI, herramientas SIEM y EDR, reglas Sigma, integración con MITRE ATT&CK y cómo construir un programa de caza de amenazas eficaz."
slug: "threat-hunting-guia-practica"
date: 2026-04-24
lastmod: 2026-04-24
draft: false
tags: ["Threat Hunting", "CTI", "SOC"]
categories: ["CTI"]
author: "David Moya"
translationKey: "threat-hunting-guide"
---

El threat hunting, o caza proactiva de amenazas, es la disciplina de buscar activamente indicios de actividad maliciosa en los sistemas y redes de una organización sin esperar a que una alerta automatizada lo señale. En un entorno donde el tiempo medio de permanencia de un atacante en una red comprometida supera los 200 días según diversos estudios del sector, la capacidad de detectar amenazas antes de que causen daño real se ha convertido en un diferenciador crítico. Esta guía explica qué es el threat hunting, qué metodologías existen, qué herramientas se necesitan y cómo construir un programa eficaz desde cero.

<!--more-->

{{< key-takeaways >}}
- Threat hunting es la búsqueda proactiva de amenazas que han eludido las defensas automatizadas
- Metodologías principales: PEAK (Splunk) y TaHiTI (Trusted Automated Hunting Intelligence)
- Requiere hipótesis basadas en inteligencia de amenazas y conocimiento del entorno
- Herramientas clave: SIEM para consultas, EDR para telemetría de endpoints y reglas Sigma para detección portable
- Los hallazgos del hunting deben convertirse en nuevas reglas de detección automatizada
{{< /key-takeaways >}}

## ¿Qué es el threat hunting y por qué es necesario?

El threat hunting es una actividad de seguridad ofensiva en la que analistas cualificados buscan de forma proactiva amenazas que han eludido los controles de detección automatizados. A diferencia de la monitorización tradicional basada en alertas, donde el sistema notifica al analista cuando algo anómalo ocurre, el hunting invierte el flujo: es el analista quien formula hipótesis sobre posibles compromisiones y busca evidencias que las confirmen o descarten.

Esta actividad se fundamenta en una premisa realista: ningún sistema de detección es perfecto. Los atacantes sofisticados, especialmente los grupos APT (Advanced Persistent Threat), invierten recursos significativos en evadir firewalls, antivirus, EDR y SIEM. El threat hunting asume que las defensas pueden haber sido superadas y busca las huellas que el adversario inevitablemente deja en el entorno.

El SANS Institute define tres niveles de madurez en threat hunting. En el nivel inicial (HM0), la organización depende exclusivamente de alertas automatizadas. En el nivel intermedio (HM1-HM2), se realizan búsquedas basadas en indicadores y se comienzan a formular hipótesis. En el nivel avanzado (HM3-HM4), el hunting es sistemático, basado en inteligencia y con automatización personalizada. La mayoría de organizaciones se sitúan entre HM0 y HM1, lo que representa un área de mejora significativa.

## Detección reactiva vs threat hunting proactivo: dos filosofías opuestas

Comprender la diferencia entre detección reactiva y hunting proactivo es fundamental para valorar la importancia de esta disciplina.

### Detección reactiva

La detección reactiva se basa en reglas, firmas y modelos predefinidos que generan alertas cuando se detecta actividad coincidente. Un SIEM genera una alerta cuando un log coincide con una regla de correlación. Un EDR bloquea un archivo cuyo hash aparece en su base de firmas. Un IDS detecta tráfico que coincide con un patrón conocido.

Este enfoque tiene valor y es necesario, pero presenta limitaciones fundamentales: solo detecta lo que está previamente definido como malicioso. Si el atacante utiliza técnicas no cubiertas por las reglas, herramientas nuevas o modificaciones de malware conocido, la detección reactiva falla silenciosamente.

### Caza proactiva

El threat hunting no depende de alertas previas. El hunter analiza datos con una hipótesis en mente, buscando anomalías, patrones inusuales o comportamientos que, aunque no activen alertas, puedan indicar una compromisión. Por ejemplo, un hunter puede buscar procesos que realizan conexiones de red inusuales para su función, cuentas de servicio que inician sesión de forma interactiva o transferencias de datos masivas a horas inusuales.

La caza proactiva complementa la detección reactiva. Los hallazgos del hunting frecuentemente se traducen en nuevas reglas de detección que mejoran la capacidad reactiva de la organización, creando un ciclo virtuoso de mejora continua.

## ¿Cómo funciona el threat hunting basado en hipótesis?

El enfoque más efectivo para el threat hunting es la formulación de hipótesis estructuradas. Este método proporciona dirección, alcance y criterios de evaluación claros para cada campaña de caza.

### Formulación de la hipótesis

Una hipótesis de hunting debe ser específica, comprobable y relevante para la organización. Una buena hipótesis sigue la estructura: "Es posible que [tipo de adversario] esté utilizando [técnica específica] contra [activo o sistema concreto] para lograr [objetivo táctico]".

Ejemplo: "Es posible que un atacante esté utilizando la técnica T1053.005 (Scheduled Task/Job: Scheduled Task) para mantener persistencia en nuestros servidores Windows de producción". Esta hipótesis específica la técnica, el entorno objetivo y el propósito del adversario.

Las fuentes para generar hipótesis incluyen la inteligencia de amenazas (informes de grupos que atacan el sector), el framework [MITRE ATT&CK](/es/posts/mitre-attack-que-es-como-usarlo/) (técnicas con puntos ciegos en la detección), las evaluaciones de riesgos (activos críticos insuficientemente monitorizados) y los incidentes recientes en organizaciones similares.

### Recopilación y análisis de datos

Una vez formulada la hipótesis, el hunter identifica las fuentes de datos necesarias y ejecuta las consultas correspondientes. Para la hipótesis anterior, se consultarían los logs de creación de tareas programadas en Windows (Event ID 4698), las tareas programadas existentes en los servidores y cualquier ejecución reciente de schtasks.exe con parámetros inusuales.

El análisis combina consultas estructuradas (queries específicas en el SIEM) con exploración no estructurada (revisión manual de resultados buscando anomalías). La experiencia del analista es determinante en esta fase.

### Documentación y cierre

Independientemente del resultado, cada campaña de hunting debe documentarse: hipótesis, fuentes de datos consultadas, consultas ejecutadas, hallazgos y conclusiones. Si se confirma la hipótesis, se inicia un proceso de respuesta a incidentes. Si se descarta, los datos recopilados enriquecen la comprensión del entorno y las consultas pueden convertirse en detecciones automatizadas permanentes.

## ¿Qué metodologías de threat hunting existen?

Existen varios marcos metodológicos que proporcionan estructura y repetibilidad al proceso de hunting.

### [PEAK](https://www.splunk.com/en_us/blog/security/peak-threat-hunting-framework.html) (Prepare, Execute, and Act with Knowledge)

Desarrollado por SANS, el framework PEAK estructura el hunting en tres fases. La fase de preparación incluye la selección de hipótesis, la identificación de fuentes de datos y la verificación de que los datos necesarios están disponibles y son accesibles. La fase de ejecución comprende la búsqueda activa, el análisis de datos y la documentación de hallazgos. La fase de actuación transforma los resultados en acciones: nuevas detecciones, mejoras en la visibilidad de datos, recomendaciones de hardening o informes de incidentes.

PEAK distingue además entre tres tipos de hunts: basados en hipótesis (descritos anteriormente), basados en modelos (utilizan modelos estadísticos o de machine learning para identificar anomalías) y basados en línea base (establecen el comportamiento normal y buscan desviaciones).

### TaHiTI (Targeted Hunting integrating Threat Intelligence)

Desarrollado por la organización holandesa FI-ISAC (Financial Institutions Information Sharing and Analysis Centre), TaHiTI es un framework específicamente diseñado para integrar la inteligencia de amenazas en el proceso de hunting. Su principal aportación es un flujo de trabajo detallado que conecta la inteligencia (informes de amenazas, IOCs, TTPs de grupos relevantes) con la generación de hipótesis y la ejecución de campañas de caza.

TaHiTI define tres fases principales: iniciación (recopilación de inteligencia y generación de hipótesis), hunting (ejecución de la búsqueda y análisis de resultados) y finalización (documentación, creación de detecciones y retroalimentación al ciclo de inteligencia).

### Modelo de madurez del Sqrrl (ahora AWS)

Este modelo define cuatro niveles de madurez en hunting: nivel 0 (sin hunting, solo detección reactiva), nivel 1 (hunting basado en IOCs y búsquedas ad hoc), nivel 2 (hunting basado en hipótesis con procedimientos definidos) y nivel 3 (hunting automatizado con modelos predictivos y machine learning). Proporciona un camino claro de evolución para organizaciones en diferentes etapas de madurez.

## Toolkit del threat hunter: SIEM, EDR, sandbox y OSINT

El hunter necesita acceso a datos ricos y herramientas que permitan consultarlos, analizarlos y visualizarlos de forma flexible.

### SIEM como plataforma de hunting

El SIEM es la herramienta central para la mayoría de campañas de hunting, ya que concentra logs de múltiples fuentes en un repositorio centralizado con capacidades de búsqueda. Las plataformas modernas como Elasticsearch (ELK Stack), Splunk o Microsoft Sentinel proporcionan lenguajes de consulta potentes que permiten al hunter formular búsquedas complejas sobre grandes volúmenes de datos históricos.

La clave para un hunting eficaz con SIEM es la calidad y amplitud de los datos ingestados. Si los logs relevantes no se están recogiendo, ninguna consulta podrá encontrar las evidencias buscadas.

### EDR (Endpoint Detection and Response)

Las soluciones EDR proporcionan visibilidad granular sobre la actividad de los endpoints: procesos creados, conexiones de red, modificaciones del sistema de archivos, cambios en el registro y actividad en memoria. Para hunting centrado en endpoints, el EDR ofrece datos que el SIEM típicamente no recoge, como las relaciones padre-hijo entre procesos o la carga de DLLs.

### Reglas Sigma

[Sigma](https://github.com/SigmaHQ/sigma) es un formato abierto para describir detecciones de forma genérica, independiente del SIEM. Las reglas Sigma se escriben en YAML y pueden convertirse automáticamente en consultas para Splunk, Elasticsearch, Microsoft Sentinel y otras plataformas. El repositorio oficial de reglas Sigma en GitHub contiene más de 3.000 reglas, muchas de ellas mapeadas contra técnicas de MITRE ATT&CK.

Para hunting, las reglas Sigma proporcionan un punto de partida valioso: el hunter puede seleccionar reglas relevantes para su hipótesis, convertirlas al formato de su SIEM y ejecutarlas como consultas exploratorias.

### Herramientas especializadas

**Velociraptor** es una plataforma open source para triaje y respuesta de endpoints que permite ejecutar consultas VQL (Velociraptor Query Language) contra flotas de máquinas de forma remota y en tiempo real. Es especialmente útil para hunting a escala.

**OSQuery** permite consultar el estado de sistemas operativos como si fueran bases de datos SQL. Los hunters pueden ejecutar consultas como "SELECT * FROM processes WHERE on_disk = 0" para encontrar procesos ejecutándose desde memoria sin archivo en disco.

**Jupyter Notebooks** se utilizan cada vez más para hunting avanzado, combinando la ejecución de consultas al SIEM con análisis estadístico y visualización en un entorno interactivo y reproducible.

## Perfil técnico del threat hunter: habilidades imprescindibles

El threat hunting requiere un perfil profesional multidisciplinar que combina conocimientos técnicos profundos con capacidad analítica.

### Conocimiento de sistemas operativos

El hunter debe entender en detalle cómo funcionan Windows, Linux y macOS a nivel de sistema: procesos, servicios, registro, sistema de archivos, mecanismos de autenticación y logging nativo. Sin este conocimiento, es imposible distinguir actividad normal de actividad sospechosa.

### Análisis de red

La capacidad de analizar tráfico de red, comprender protocolos, identificar comunicaciones C2 y detectar exfiltración de datos es esencial. Herramientas como Wireshark y Zeek son parte del arsenal habitual del hunter.

### Inteligencia de amenazas

Comprender el panorama de amenazas, los grupos adversarios relevantes para la organización y sus TTPs permite formular hipótesis informadas y priorizar las campañas de hunting.

### Capacidad analítica

El hunting es fundamentalmente un ejercicio de análisis. El hunter debe ser capaz de correlacionar datos de múltiples fuentes, identificar patrones sutiles y mantener la atención al detalle durante investigaciones extensas. Los [analistas de SOC con experiencia](/es/posts/analista-soc-roles-n1-n2-n3/) en niveles N2 y N3 suelen ser los mejores candidatos para roles de threat hunting.

### Programación y scripting

La automatización de consultas, el procesamiento de datos a escala y la creación de herramientas personalizadas requieren conocimientos de Python, PowerShell o Bash. Muchos hunters avanzados desarrollan sus propias herramientas y scripts para tareas recurrentes.

{{< cta type="tofu" text="Riskitera potencia tu programa de threat hunting con hipótesis generadas por IA y correlación automática de telemetría." label="Explorar" >}}

## ¿Cómo construir un programa de threat hunting?

Implementar un programa de hunting estructurado requiere planificación, recursos y compromiso organizacional.

### Paso 1: Evaluar la madurez actual

Antes de iniciar un programa de hunting, es necesario evaluar la madurez actual de las operaciones de seguridad. El hunting requiere datos (logs completos y accesibles), herramientas (SIEM con capacidad de búsqueda histórica) y personal cualificado. Si los fundamentos de monitorización y detección reactiva no están establecidos, deben construirse primero.

### Paso 2: Definir el alcance y los objetivos

El programa debe comenzar con un alcance realista. Es preferible iniciar con campañas de hunting semanales enfocadas en los activos más críticos que intentar cubrir todo el entorno desde el primer día. Los objetivos deben incluir tanto la detección de amenazas como la mejora de la postura de seguridad (nuevas detecciones, mejoras en la visibilidad de datos).

### Paso 3: Establecer el proceso

Definir un proceso repetible que incluya la generación de hipótesis (alimentada por inteligencia de amenazas y evaluaciones de riesgo), la planificación de la campaña (fuentes de datos, herramientas, duración), la ejecución, la documentación y la retroalimentación (conversión de hallazgos en detecciones automatizadas y mejoras en la visibilidad).

### Paso 4: Asignar recursos

El hunting requiere tiempo dedicado de analistas cualificados. Es difícil hacer hunting efectivo si los analistas están permanentemente absorbidos por la cola de alertas del SOC. Muchas organizaciones asignan un porcentaje fijo del tiempo de los analistas senior a actividades de hunting, o disponen de un rol dedicado.

### Paso 5: Medir y evolucionar

Sin métricas, es imposible demostrar el valor del programa y justificar su continuidad. Las métricas de proceso y resultado son esenciales para la evolución del programa. Riskitera incluye capacidades de threat hunting proactivo en su plataforma SOC, integrando la generación de hipótesis con la inteligencia de amenazas y automatizando la ejecución de búsquedas sobre los datos centralizados.

## ¿Cómo medir la eficacia del threat hunting?

Medir la eficacia del hunting es un reto frecuente. Estas son las métricas más relevantes:

**Campañas ejecutadas por periodo:** mide la cadencia del programa. Un programa maduro ejecuta múltiples campañas por semana o mes.

**Hipótesis generadas versus confirmadas:** el porcentaje de hipótesis que resultan en hallazgos reales indica la calidad de la generación de hipótesis y la inteligencia que la alimenta.

**Detecciones creadas a partir de hunting:** cada campaña de hunting debería producir nuevas reglas de detección o mejorar las existentes. Esta métrica mide la contribución del hunting a la mejora continua.

**Tiempo medio de investigación:** el tiempo que tarda un hunter en completar una campaña, desde la formulación de la hipótesis hasta la documentación de resultados.

**Hallazgos críticos:** número de compromisos reales, malware no detectado, configuraciones peligrosas o puntos ciegos de seguridad descubiertos a través del hunting.

**Mejoras en la visibilidad de datos:** campañas que revelan que fuentes de datos necesarias no están siendo recogidas, lo que conduce a mejoras en la infraestructura de logging.

## Errores comunes en threat hunting

**Confundir hunting con respuesta a alertas.** Investigar alertas del SIEM no es threat hunting. El hunting es proactivo y no depende de alertas previas. Muchas organizaciones creen que hacen hunting cuando en realidad están haciendo triaje avanzado de alertas.

**No documentar los resultados negativos.** Una campaña de hunting que no encuentra evidencias de compromiso sigue siendo valiosa: confirma que, hasta donde se ha podido verificar, la organización no está comprometida en el área investigada. Además, las consultas desarrolladas pueden reutilizarse.

**Depender exclusivamente de herramientas automatizadas.** Las herramientas de hunting automatizado tienen valor, pero no sustituyen al análisis humano. Los atacantes avanzados están diseñados para evadir detección automatizada, y es el juicio del hunter lo que marca la diferencia.

**No cerrar el ciclo.** El hunting debe alimentar la detección reactiva. Si los hallazgos no se convierten en detecciones automatizadas, la organización dependerá siempre de campañas manuales para detectar las mismas amenazas.

{{< cta type="mofu" text="Lleva tu threat hunting al siguiente nivel con una plataforma que conecta hipótesis, detecciones y evidencias de compliance." >}}

## Preguntas frecuentes

### ¿Cuál es la diferencia entre threat hunting y penetration testing?

El penetration testing simula un ataque desde fuera de la organización para identificar vulnerabilidades explotables. El threat hunting busca evidencias de que un atacante real ya está dentro de la red. El pentest es ofensivo y puntual; el hunting es defensivo y continuo. Ambos son complementarios: los hallazgos de un pentest pueden alimentar las hipótesis de hunting y viceversa.

### ¿Necesito un equipo dedicado para hacer threat hunting?

No necesariamente. Muchas organizaciones comienzan asignando un porcentaje del tiempo de sus analistas de SOC de nivel N2 o N3 a actividades de hunting. A medida que el programa madura y demuestra valor, puede justificarse un equipo o al menos un rol dedicado. Lo importante es que el tiempo asignado al hunting esté protegido y no se consuma en la gestión de alertas diarias.

### ¿Qué datos necesito recoger antes de empezar a hacer hunting?

Como mínimo, se necesitan logs de autenticación (logins exitosos y fallidos), logs de creación y ejecución de procesos (Event ID 4688 en Windows o auditd en Linux), logs de conexiones de red (firewall, proxy, DNS) y logs de acceso a archivos críticos. Cuanta mayor visibilidad se tenga del entorno, más efectivo será el hunting. Las configuraciones de Sysmon para Windows son especialmente valiosas.

### ¿Con qué frecuencia debo realizar campañas de hunting?

La frecuencia depende de los recursos disponibles y la madurez del programa. Un programa inicial puede empezar con una campaña quincenal o mensual. Un programa maduro ejecuta múltiples campañas por semana, con duraciones variables según la complejidad de la hipótesis. Lo más importante es mantener la cadencia y no dejar que el hunting se suspenda cuando el SOC está bajo presión por otros incidentes.

### ¿Cómo elijo las hipótesis de hunting más relevantes?

La priorización de hipótesis debe basarse en tres factores: la inteligencia de amenazas (qué grupos atacan tu sector y qué técnicas utilizan), la evaluación de riesgos (qué activos son más críticos y cuáles tienen menor cobertura de detección) y los puntos ciegos conocidos (técnicas de MITRE ATT&CK que la organización no puede detectar actualmente). Las guías del [CCN-CERT](https://www.ccn-cert.cni.es/) sobre amenazas relevantes para el sector público español y los informes de [ENISA](https://www.enisa.europa.eu/) Threat Landscape son recursos valiosos para contextualizar las hipótesis en el ámbito europeo.
