---
title: "Threat Hunting: como cazar amenazas antes de que ataquen"
description: "Guia practica de threat hunting: metodologias PEAK y TaHiTI, herramientas SIEM y EDR, reglas Sigma, integracion con MITRE ATT&CK y como construir un programa de caza de amenazas eficaz."
slug: "threat-hunting-guia-practica"
date: 2026-04-06
lastmod: 2026-04-06
draft: false
tags: ["Threat Hunting", "CTI", "SOC"]
categories: ["CTI"]
author: "Riskitera Team"
translationKey: "threat-hunting-guide"
---

El threat hunting, o caza proactiva de amenazas, es la disciplina de buscar activamente indicios de actividad maliciosa en los sistemas y redes de una organizacion sin esperar a que una alerta automatizada lo senale. En un entorno donde el tiempo medio de permanencia de un atacante en una red comprometida supera los 200 dias segun diversos estudios del sector, la capacidad de detectar amenazas antes de que causen dano real se ha convertido en un diferenciador critico. Esta guia explica que es el threat hunting, que metodologias existen, que herramientas se necesitan y como construir un programa eficaz desde cero.

<!--more-->

## Que es el threat hunting

El threat hunting es una actividad de seguridad ofensiva en la que analistas cualificados buscan de forma proactiva amenazas que han eludido los controles de deteccion automatizados. A diferencia de la monitorizacion tradicional basada en alertas, donde el sistema notifica al analista cuando algo anomalo ocurre, el hunting invierte el flujo: es el analista quien formula hipotesis sobre posibles compromisiones y busca evidencias que las confirmen o descarten.

Esta actividad se fundamenta en una premisa realista: ningun sistema de deteccion es perfecto. Los atacantes sofisticados, especialmente los grupos APT (Advanced Persistent Threat), invierten recursos significativos en evadir firewalls, antivirus, EDR y SIEM. El threat hunting asume que las defensas pueden haber sido superadas y busca las huellas que el adversario inevitablemente deja en el entorno.

El SANS Institute define tres niveles de madurez en threat hunting. En el nivel inicial (HM0), la organizacion depende exclusivamente de alertas automatizadas. En el nivel intermedio (HM1-HM2), se realizan busquedas basadas en indicadores y se comienzan a formular hipotesis. En el nivel avanzado (HM3-HM4), el hunting es sistematico, basado en inteligencia y con automatizacion personalizada. La mayoria de organizaciones se situan entre HM0 y HM1, lo que representa un area de mejora significativa.

## Deteccion reactiva frente a caza proactiva

Comprender la diferencia entre deteccion reactiva y hunting proactivo es fundamental para valorar la importancia de esta disciplina.

### Deteccion reactiva

La deteccion reactiva se basa en reglas, firmas y modelos predefinidos que generan alertas cuando se detecta actividad coincidente. Un SIEM genera una alerta cuando un log coincide con una regla de correlacion. Un EDR bloquea un archivo cuyo hash aparece en su base de firmas. Un IDS detecta trafico que coincide con un patron conocido.

Este enfoque tiene valor y es necesario, pero presenta limitaciones fundamentales: solo detecta lo que esta previamente definido como malicioso. Si el atacante utiliza tecnicas no cubiertas por las reglas, herramientas nuevas o modificaciones de malware conocido, la deteccion reactiva falla silenciosamente.

### Caza proactiva

El threat hunting no depende de alertas previas. El hunter analiza datos con una hipotesis en mente, buscando anomalias, patrones inusuales o comportamientos que, aunque no activen alertas, puedan indicar una compromision. Por ejemplo, un hunter puede buscar procesos que realizan conexiones de red inusuales para su funcion, cuentas de servicio que inician sesion de forma interactiva o transferencias de datos masivas a horas inusuales.

La caza proactiva complementa la deteccion reactiva. Los hallazgos del hunting frecuentemente se traducen en nuevas reglas de deteccion que mejoran la capacidad reactiva de la organizacion, creando un ciclo virtuoso de mejora continua.

## Hunting basado en hipotesis

El enfoque mas efectivo para el threat hunting es la formulacion de hipotesis estructuradas. Este metodo proporciona direccion, alcance y criterios de evaluacion claros para cada campana de caza.

### Formulacion de la hipotesis

Una hipotesis de hunting debe ser especifica, comprobable y relevante para la organizacion. Una buena hipotesis sigue la estructura: "Es posible que [tipo de adversario] este utilizando [tecnica especifica] contra [activo o sistema concreto] para lograr [objetivo tactico]".

Ejemplo: "Es posible que un atacante este utilizando la tecnica T1053.005 (Scheduled Task/Job: Scheduled Task) para mantener persistencia en nuestros servidores Windows de produccion". Esta hipotesis especifica la tecnica, el entorno objetivo y el proposito del adversario.

Las fuentes para generar hipotesis incluyen la inteligencia de amenazas (informes de grupos que atacan el sector), el framework [MITRE ATT&CK](/es/posts/mitre-attack-que-es-como-usarlo/) (tecnicas con puntos ciegos en la deteccion), las evaluaciones de riesgos (activos criticos insuficientemente monitorizados) y los incidentes recientes en organizaciones similares.

### Recopilacion y analisis de datos

Una vez formulada la hipotesis, el hunter identifica las fuentes de datos necesarias y ejecuta las consultas correspondientes. Para la hipotesis anterior, se consultarian los logs de creacion de tareas programadas en Windows (Event ID 4698), las tareas programadas existentes en los servidores y cualquier ejecucion reciente de schtasks.exe con parametros inusuales.

El analisis combina consultas estructuradas (queries especificas en el SIEM) con exploracion no estructurada (revision manual de resultados buscando anomalias). La experiencia del analista es determinante en esta fase.

### Documentacion y cierre

Independientemente del resultado, cada campana de hunting debe documentarse: hipotesis, fuentes de datos consultadas, consultas ejecutadas, hallazgos y conclusiones. Si se confirma la hipotesis, se inicia un proceso de respuesta a incidentes. Si se descarta, los datos recopilados enriquecen la comprension del entorno y las consultas pueden convertirse en detecciones automatizadas permanentes.

## Metodologias de threat hunting

Existen varios marcos metodologicos que proporcionan estructura y repetibilidad al proceso de hunting.

### PEAK (Prepare, Execute, and Act with Knowledge)

Desarrollado por SANS, el framework PEAK estructura el hunting en tres fases. La fase de preparacion incluye la seleccion de hipotesis, la identificacion de fuentes de datos y la verificacion de que los datos necesarios estan disponibles y son accesibles. La fase de ejecucion comprende la busqueda activa, el analisis de datos y la documentacion de hallazgos. La fase de actuacion transforma los resultados en acciones: nuevas detecciones, mejoras en la visibilidad de datos, recomendaciones de hardenening o informes de incidentes.

PEAK distingue ademas entre tres tipos de hunts: basados en hipotesis (descritos anteriormente), basados en modelos (utilizan modelos estadisticos o de machine learning para identificar anomalias) y basados en linea base (establecen el comportamiento normal y buscan desviaciones).

### TaHiTI (Targeted Hunting integrating Threat Intelligence)

Desarrollado por la organizacion holandesa FI-ISAC (Financial Institutions Information Sharing and Analysis Centre), TaHiTI es un framework especificamente disenado para integrar la inteligencia de amenazas en el proceso de hunting. Su principal aportacion es un flujo de trabajo detallado que conecta la inteligencia (informes de amenazas, IOCs, TTPs de grupos relevantes) con la generacion de hipotesis y la ejecucion de campanas de caza.

TaHiTI define tres fases principales: iniciacion (recopilacion de inteligencia y generacion de hipotesis), hunting (ejecucion de la busqueda y analisis de resultados) y finalizacion (documentacion, creacion de detecciones y retroalimentacion al ciclo de inteligencia).

### Modelo de madurez del Sqrrl (ahora AWS)

Este modelo define cuatro niveles de madurez en hunting: nivel 0 (sin hunting, solo deteccion reactiva), nivel 1 (hunting basado en IOCs y busquedas ad hoc), nivel 2 (hunting basado en hipotesis con procedimientos definidos) y nivel 3 (hunting automatizado con modelos predictivos y machine learning). Proporciona un camino claro de evolucion para organizaciones en diferentes etapas de madurez.

## Herramientas para threat hunting

El hunter necesita acceso a datos ricos y herramientas que permitan consultarlos, analizarlos y visualizarlos de forma flexible.

### SIEM como plataforma de hunting

El SIEM es la herramienta central para la mayoria de campanas de hunting, ya que concentra logs de multiples fuentes en un repositorio centralizado con capacidades de busqueda. Las plataformas modernas como Elasticsearch (ELK Stack), Splunk o Microsoft Sentinel proporcionan lenguajes de consulta potentes que permiten al hunter formular busquedas complejas sobre grandes volumenes de datos historicos.

La clave para un hunting eficaz con SIEM es la calidad y amplitud de los datos ingestados. Si los logs relevantes no se estan recogiendo, ninguna consulta podra encontrar las evidencias buscadas.

### EDR (Endpoint Detection and Response)

Las soluciones EDR proporcionan visibilidad granular sobre la actividad de los endpoints: procesos creados, conexiones de red, modificaciones del sistema de archivos, cambios en el registro y actividad en memoria. Para hunting centrado en endpoints, el EDR ofrece datos que el SIEM tipicamente no recoge, como las relaciones padre-hijo entre procesos o la carga de DLLs.

### Reglas Sigma

Sigma es un formato abierto para describir detecciones de forma generica, independiente del SIEM. Las reglas Sigma se escriben en YAML y pueden convertirse automaticamente en consultas para Splunk, Elasticsearch, Microsoft Sentinel y otras plataformas. El repositorio oficial de reglas Sigma en GitHub contiene mas de 3.000 reglas, muchas de ellas mapeadas contra tecnicas de MITRE ATT&CK.

Para hunting, las reglas Sigma proporcionan un punto de partida valioso: el hunter puede seleccionar reglas relevantes para su hipotesis, convertirlas al formato de su SIEM y ejecutarlas como consultas exploratorias.

### Herramientas especializadas

**Velociraptor** es una plataforma open source para triaje y respuesta de endpoints que permite ejecutar consultas VQL (Velociraptor Query Language) contra flotas de maquinas de forma remota y en tiempo real. Es especialmente util para hunting a escala.

**OSQuery** permite consultar el estado de sistemas operativos como si fueran bases de datos SQL. Los hunters pueden ejecutar consultas como "SELECT * FROM processes WHERE on_disk = 0" para encontrar procesos ejecutandose desde memoria sin archivo en disco.

**Jupyter Notebooks** se utilizan cada vez mas para hunting avanzado, combinando la ejecucion de consultas al SIEM con analisis estadistico y visualizacion en un entorno interactivo y reproducible.

## Habilidades necesarias para el threat hunter

El threat hunting requiere un perfil profesional multidisciplinar que combina conocimientos tecnicos profundos con capacidad analitica.

### Conocimiento de sistemas operativos

El hunter debe entender en detalle como funcionan Windows, Linux y macOS a nivel de sistema: procesos, servicios, registro, sistema de archivos, mecanismos de autenticacion y logging nativo. Sin este conocimiento, es imposible distinguir actividad normal de actividad sospechosa.

### Analisis de red

La capacidad de analizar trafico de red, comprender protocolos, identificar comunicaciones C2 y detectar exfiltracion de datos es esencial. Herramientas como Wireshark y Zeek son parte del arsenal habitual del hunter.

### Inteligencia de amenazas

Comprender el panorama de amenazas, los grupos adversarios relevantes para la organizacion y sus TTPs permite formular hipotesis informadas y priorizar las campanas de hunting.

### Capacidad analitica

El hunting es fundamentalmente un ejercicio de analisis. El hunter debe ser capaz de correlacionar datos de multiples fuentes, identificar patrones sutiles y mantener la atencion al detalle durante investigaciones extensas. Los [analistas de SOC con experiencia](/es/posts/analista-soc-roles-n1-n2-n3/) en niveles N2 y N3 suelen ser los mejores candidatos para roles de threat hunting.

### Programacion y scripting

La automatizacion de consultas, el procesamiento de datos a escala y la creacion de herramientas personalizadas requieren conocimientos de Python, PowerShell o Bash. Muchos hunters avanzados desarrollan sus propias herramientas y scripts para tareas recurrentes.

## Construir un programa de threat hunting

Implementar un programa de hunting estructurado requiere planificacion, recursos y compromiso organizacional.

### Paso 1: Evaluar la madurez actual

Antes de iniciar un programa de hunting, es necesario evaluar la madurez actual de las operaciones de seguridad. El hunting requiere datos (logs completos y accesibles), herramientas (SIEM con capacidad de busqueda historica) y personal cualificado. Si los fundamentos de monitorizacion y deteccion reactiva no estan establecidos, deben construirse primero.

### Paso 2: Definir el alcance y los objetivos

El programa debe comenzar con un alcance realista. Es preferible iniciar con campanas de hunting semanales enfocadas en los activos mas criticos que intentar cubrir todo el entorno desde el primer dia. Los objetivos deben incluir tanto la deteccion de amenazas como la mejora de la postura de seguridad (nuevas detecciones, mejoras en la visibilidad de datos).

### Paso 3: Establecer el proceso

Definir un proceso repetible que incluya la generacion de hipotesis (alimentada por inteligencia de amenazas y evaluaciones de riesgo), la planificacion de la campana (fuentes de datos, herramientas, duracion), la ejecucion, la documentacion y la retroalimentacion (conversion de hallazgos en detecciones automatizadas y mejoras en la visibilidad).

### Paso 4: Asignar recursos

El hunting requiere tiempo dedicado de analistas cualificados. Es dificil hacer hunting efectivo si los analistas estan permanentemente absorbidos por la cola de alertas del SOC. Muchas organizaciones asignan un porcentaje fijo del tiempo de los analistas senior a actividades de hunting, o disponen de un rol dedicado.

### Paso 5: Medir y evolucionar

Sin metricas, es imposible demostrar el valor del programa y justificar su continuidad. Las metricas de proceso y resultado son esenciales para la evolucion del programa. Riskitera incluye capacidades de threat hunting proactivo en su plataforma SOC, integrando la generacion de hipotesis con la inteligencia de amenazas y automatizando la ejecucion de busquedas sobre los datos centralizados.

## Metricas de un programa de threat hunting

Medir la eficacia del hunting es un reto frecuente. Estas son las metricas mas relevantes:

**Campanas ejecutadas por periodo:** mide la cadencia del programa. Un programa maduro ejecuta multiples campanas por semana o mes.

**Hipotesis generadas versus confirmadas:** el porcentaje de hipotesis que resultan en hallazgos reales indica la calidad de la generacion de hipotesis y la inteligencia que la alimenta.

**Detecciones creadas a partir de hunting:** cada campana de hunting deberia producir nuevas reglas de deteccion o mejorar las existentes. Esta metrica mide la contribucion del hunting a la mejora continua.

**Tiempo medio de investigacion:** el tiempo que tarda un hunter en completar una campana, desde la formulacion de la hipotesis hasta la documentacion de resultados.

**Hallazgos criticos:** numero de compromisos reales, malware no detectado, configuraciones peligrosas o puntos ciegos de seguridad descubiertos a traves del hunting.

**Mejoras en la visibilidad de datos:** campanas que revelan que fuentes de datos necesarias no estan siendo recogidas, lo que conduce a mejoras en la infraestructura de logging.

## Errores comunes en threat hunting

**Confundir hunting con respuesta a alertas.** Investigar alertas del SIEM no es threat hunting. El hunting es proactivo y no depende de alertas previas. Muchas organizaciones creen que hacen hunting cuando en realidad estan haciendo triaje avanzado de alertas.

**No documentar los resultados negativos.** Una campana de hunting que no encuentra evidencias de compromiso sigue siendo valiosa: confirma que, hasta donde se ha podido verificar, la organizacion no esta comprometida en el area investigada. Ademas, las consultas desarrolladas pueden reutilizarse.

**Depender exclusivamente de herramientas automatizadas.** Las herramientas de hunting automatizado tienen valor, pero no sustituyen al analisis humano. Los atacantes avanzados estan disenados para evadir deteccion automatizada, y es el juicio del hunter lo que marca la diferencia.

**No cerrar el ciclo.** El hunting debe alimentar la deteccion reactiva. Si los hallazgos no se convierten en detecciones automatizadas, la organizacion dependera siempre de campanas manuales para detectar las mismas amenazas.

## Preguntas frecuentes

### Cual es la diferencia entre threat hunting y penetration testing

El penetration testing simula un ataque desde fuera de la organizacion para identificar vulnerabilidades explotables. El threat hunting busca evidencias de que un atacante real ya esta dentro de la red. El pentest es ofensivo y puntual; el hunting es defensivo y continuo. Ambos son complementarios: los hallazgos de un pentest pueden alimentar las hipotesis de hunting y viceversa.

### Necesito un equipo dedicado para hacer threat hunting

No necesariamente. Muchas organizaciones comienzan asignando un porcentaje del tiempo de sus analistas de SOC de nivel N2 o N3 a actividades de hunting. A medida que el programa madura y demuestra valor, puede justificarse un equipo o al menos un rol dedicado. Lo importante es que el tiempo asignado al hunting este protegido y no se consuma en la gestion de alertas diarias.

### Que datos necesito recoger antes de empezar a hacer hunting

Como minimo, se necesitan logs de autenticacion (logins exitosos y fallidos), logs de creacion y ejecucion de procesos (Event ID 4688 en Windows o auditd en Linux), logs de conexiones de red (firewall, proxy, DNS) y logs de acceso a archivos criticos. Cuanta mayor visibilidad se tenga del entorno, mas efectivo sera el hunting. Las configuraciones de Sysmon para Windows son especialmente valiosas.

### Con que frecuencia debo realizar campanas de hunting

La frecuencia depende de los recursos disponibles y la madurez del programa. Un programa inicial puede empezar con una campana quincenal o mensual. Un programa maduro ejecuta multiples campanas por semana, con duraciones variables segun la complejidad de la hipotesis. Lo mas importante es mantener la cadencia y no dejar que el hunting se suspenda cuando el SOC esta bajo presion por otros incidentes.

### Como elijo las hipotesis de hunting mas relevantes

La priorizacion de hipotesis debe basarse en tres factores: la inteligencia de amenazas (que grupos atacan tu sector y que tecnicas utilizan), la evaluacion de riesgos (que activos son mas criticos y cuales tienen menor cobertura de deteccion) y los puntos ciegos conocidos (tecnicas de MITRE ATT&CK que la organizacion no puede detectar actualmente). Las guias del CCN-CERT sobre amenazas relevantes para el sector publico espanol y los informes de ENISA Threat Landscape son recursos valiosos para contextualizar las hipotesis en el ambito europeo.
