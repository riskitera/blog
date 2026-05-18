---
title: "Como montar un SOC desde cero: guía práctica para empresas"
image: "cover.png"
description: "Guía completa para crear un Centro de Operaciones de Seguridad (SOC): tipos, roles del equipo, herramientas necesarias, procesos, costes y errores comunes a evitar."
slug: "como-montar-soc-desde-cero"
date: 2026-04-04
lastmod: 2026-04-04
draft: false
tags: ["SOC", "Operaciones", "SIEM"]
categories: ["SOC"]
author: "David Moya"
translationKey: "soc-guide"
---

Un Centro de Operaciones de Seguridad (SOC) es el núcleo de la capacidad de detección y respuesta ante amenazas de una organización. Es el equipo, los procesos y la tecnología que trabajan de forma coordinada para monitorizar, analizar y responder a incidentes de ciberseguridad las 24 horas del día, los 365 días del año. Montar un SOC desde cero es un proyecto complejo, pero con la planificación adecuada, cualquier empresa de tamaño mediano o grande puede hacerlo de forma eficaz.

<!--more-->

{{< key-takeaways >}}
- Tres modelos: SOC interno (700K-1.5M EUR/año), externalizado (96K-300K EUR/año) o híbrido (250K-500K EUR/año)
- Equipo mínimo 24/7: 5-6 analistas N1, 2-3 N2, 1-2 N3, más SOC Manager e ingeniero de detección
- Stack tecnológico esencial: SIEM + EDR + SOAR + plataforma de threat intelligence
- Métricas clave: MTTD, MTTR, tasa de falsos positivos y cobertura MITRE ATT&CK
- Error más común: empezar por la tecnología en lugar de por los procesos y casos de uso
{{< /key-takeaways >}}

## ¿Qué es un SOC y por que lo necesita tu empresa?

Un SOC (Security Operations Center) es una función centralizada que emplea personas, procesos y tecnología para monitorizar y mejorar continuamente la postura de seguridad de una organización, al tiempo que previene, detecta, analiza y responde a incidentes de ciberseguridad.

Según el informe de [INCIBE](https://www.incibe.es/) sobre el estado de la ciberseguridad empresarial en España (2025), el tiempo medio de detección de un incidente de seguridad en empresas sin SOC es de 197 días, frente a los 38 días de media en empresas con un SOC operativo. Esta diferencia es crítica: cada día que una amenaza permanece sin detectar en tus sistemas incrementa exponencialmente el daño potencial.

Las razones principales para contar con un SOC son:

- **Detección temprana de amenazas**: la monitorización continua permite identificar actividades sospechosas antes de que se conviertan en incidentes graves.
- **Respuesta rápida a incidentes**: un equipo dedicado puede contener una amenaza en minutos u horas, en lugar de días o semanas.
- **Cumplimiento normativo**: regulaciones como [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555), [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554), el [ENS](https://www.boe.es/eli/es/rd/2022/05/03/311) y la [ISO 27001](https://www.iso.org/standard/27001) exigen capacidades de monitorización y respuesta a incidentes que, en la práctica, requieren un SOC.
- **Visibilidad global**: el SOC proporciona una visión unificada del estado de seguridad de toda la organización.
- **Reducción de costes por incidente**: según IBM, el coste medio de una brecha de datos en Europa fue de 4,3 millones de euros en 2025. Las organizaciones con SOC redujeron ese coste en un 40 por ciento de media.

## ¿Qué tipos de SOC existen: interno, externo o híbrido?

Antes de disenar tu SOC, la primera decisión estratégica es elegir el modelo operativo.

### SOC interno (in-house)

La organización construye y opera su propio SOC con personal, tecnología e infraestructura propios.

**Ventajas:**
- Control total sobre los procesos y los datos.
- Conocimiento profundo del entorno y contexto de negocio.
- Capacidad de personalización máxima.
- Alineación directa con los objetivos de la organización.

**Desventajas:**
- Coste elevado: infraestructura, licencias, salarios de un equipo que opera 24/7.
- Dificultad para reclutar y retener talento especializado en un mercado con alta demanda.
- Tiempo de puesta en marcha largo (12-18 meses para un SOC maduro).
- Riesgo de fatiga del equipo si no se dimensiona correctamente.

### SOC externo (MSSP/MDR)

La organización contrata un proveedor externo de servicios de seguridad gestionada (MSSP) o de detección y respuesta gestionada (MDR) para que opere el SOC.

**Ventajas:**
- Operativo desde el primer día.
- Coste predecible y generalmente inferior al SOC interno.
- Acceso a talento especializado y a inteligencia de amenazas global.
- Escalabilidad inmediata.

**Desventajas:**
- Menor control sobre los procesos y la priorización.
- Dependencia de un tercero para una función crítica.
- Posible falta de contexto de negocio.
- Limitaciones en la personalización de las reglas de detección.

### SOC híbrido

Combina un equipo interno reducido con el apoyo de un proveedor externo. Es el modelo más adoptado por empresas medianas en España.

**Ventajas:**
- Equilibrio entre control y coste.
- El equipo interno aporta contexto de negocio; el proveedor aporta cobertura 24/7 y capacidades avanzadas.
- Flexibilidad para escalar según necesidades.
- Transferencia de conocimiento entre el equipo interno y el proveedor.

**Desventajas:**
- Requiere una buena coordinación entre equipos interno y externo.
- Necesidad de definir claramente roles, responsabilidades y escalados.
- Gestión de dos culturas operativas distintas.

Según datos de INCIBE, en 2025 el 34 por ciento de las empresas medianas y grandes españolas con SOC operaban un modelo híbrido, el 41 por ciento externalizaban completamente y el 25 por ciento mantenían un SOC interno puro.

## ¿Qué roles necesita un equipo SOC?

El equipo de un SOC se organiza en tres niveles (tiers) con funciones, habilidades y responsabilidades diferenciadas. Si quieres profundizar en cada perfil profesional, te recomendamos nuestro artículo sobre [analistas SOC: roles N1, N2 y N3 explicados con detalle](/es/posts/2026/04/analista-soc-roles-n1-n2-n3/).

### Nivel 1 (N1): Analista de triaje

Los analistas N1 son la primera línea de defensa. Su función principal es monitorizar las alertas generadas por las herramientas de seguridad, realizar un triaje inicial y escalar las alertas que requieran investigación adicional.

**Responsabilidades:**
- Monitorización continúa de alertas del SIEM, EDR, IDS/IPS y otras fuentes.
- Triaje y clasificación inicial de alertas (verdadero positivo, falso positivo, requiere escalado).
- Documentación básica de cada alerta en el sistema de ticketing.
- Ejecución de playbooks predefinidos para incidentes rutinarios.
- Escalado a N2 de las alertas que requieran investigación.

**Perfil típico:** 1-2 años de experiencia en TI o ciberseguridad. Conocimientos básicos de redes, sistemas operativos y herramientas SIEM. Capacidad de trabajar en turnos.

Según el *SANS 2024 SOC Survey*, el equipo medio de un SOC con cobertura 24/7 oscila entre 11 y 25 personas, y los SOC que operan con menos de 10 analistas reportan niveles de madurez significativamente inferiores en detección y respuesta. Un SOC 24/7 necesita un mínimo de 5-6 analistas N1 para cubrir los tres turnos con cobertura de vacaciones y bajas.

### Nivel 2 (N2): Analista de incidentes

Los analistas N2 investigan en profundidad las alertas escaladas por N1, determinan el alcance y la gravedad de los incidentes y coordinan la respuesta.

**Responsabilidades:**
- Investigación profunda de alertas escaladas.
- Correlación de eventos de múltiples fuentes para determinar el alcance del incidente.
- Análisis de malware básico y forense preliminar.
- Coordinación de la respuesta a incidentes.
- Desarrollo y mejora de reglas de detección y playbooks.
- Generación de informes de incidentes.

**Perfil típico:** 3-5 años de experiencia en ciberseguridad. Conocimientos avanzados de análisis de amenazas, forense digital y respuesta a incidentes. Experiencia con herramientas SIEM, EDR y SOAR.

Un SOC maduro necesita al menos 2-3 analistas N2.

### Nivel 3 (N3): Analista senior / Threat hunter

Los analistas N3 son los perfiles más experimentados del SOC. Se dedican a la caza proactiva de amenazas, al análisis avanzado de malware y a la mejora continua de las capacidades de detección.

**Responsabilidades:**
- Threat hunting proactivo: búsqueda de amenazas que han eludido los mecanismos de detección automatizados.
- Análisis avanzado de malware (ingeniería inversa).
- Forense digital avanzado.
- Desarrollo de inteligencia de amenazas aplicada.
- Diseno de arquitectura de detección y optimización de reglas.
- Asesoria técnica en incidentes complejos.
- Mentorización de analistas N1 y N2.

**Perfil típico:** 5 o más años de experiencia en ciberseguridad. Especialización en forense, malware analysis o threat intelligence. Certificaciones avanzadas (GCFA, GREM, OSCP).

Un SOC típico cuenta con 1-2 analistas N3.

### Otros roles clave

- **SOC Manager**: responsable de la operación global del SOC, gestión del equipo, definición de métricas y KPI, y relación con la dirección.
- **Ingeniero de detección**: desarrolla y mantiene las reglas de correlación, los casos de uso y la infraestructura del SIEM.
- **Ingeniero de automatización (SOAR)**: desarrolla playbooks automatizados y gestiona la plataforma SOAR.

## Stack tecnológico del SOC: SIEM, EDR, SOAR y TIP

La tecnología es uno de los tres pilares del SOC, junto con las personas y los procesos.

### SIEM (Security Information and Event Management)

El SIEM es la herramienta central del SOC. Recopila logs de toda la infraestructura, los normaliza, los correlacióna y genera alertas. Para una guía detallada sobre [qué es un SIEM y como funciona](/es/posts/2026/04/que-es-un-siem-para-que-sirve/), consulta nuestro artículo dedicado.

Opciones principales en el mercado:
- **[Splunk](https://www.splunk.com/) Enterprise Security**: lider de mercado, potente pero costoso.
- **[Microsoft Sentinel](https://azure.microsoft.com/products/microsoft-sentinel)**: solución cloud nativa, ideal para entornos Microsoft/Azure.
- **IBM QRadar**: robusto, con buenas capacidades de correlación out-of-the-box.
- **[Elastic Security](https://www.elastic.co/security)**: basado en Elasticsearch, con una opción open source.
- **Google Chronicle (SecOps)**: enfoque cloud con capacidades de análisis a escala.

### EDR (Endpoint Detection and Response)

Proporciona visibilidad y capacidad de respuesta a nivel de endpoint (servidores, estaciones de trabajo, dispositivos móviles):
- CrowdStrike Falcon.
- Microsoft Defender for Endpoint.
- SentinelOne.
- Carbon Black (VMware).

### SOAR (Security Orchestration, Automation and Response)

Automatiza la respuesta a incidentes mediante playbooks predefinidos y orquesta las herramientas de seguridad:
- Palo Alto XSOAR (anteriormente Demisto).
- Splunk SOAR (anteriormente Phantom).
- IBM QRadar SOAR.
- Shuffle (open source).
- Tines.

### Otras herramientas

- **NDR (Network Detection and Response)**: Darktrace, Vectra AI, ExtraHop.
- **Plataforma de Threat Intelligence**: MISP (open source), Anomali, Recorded Future.
- **Sistema de ticketing**: ServiceNow, Jira Service Management, TheHive.
- **Herramientas forenses**: Velociraptor, Autopsy, Volatility.
- **Gestión de vulnerabilidades**: Qualys, Tenable, Rapid7.

{{< cta type="tofu" text="Montar un SOC requiere las herramientas adecuadas. Riskitera integra SIEM, correlación y triage con IA en una sola plataforma." label="Conocer más" >}}

## ¿Cuáles son los procesos fundamentales de un SOC?

La tecnología sin procesos bien definidos es inutil. Estos son los procesos esenciales:

### Gestión de alertas

Define un flujo claro desde la generación de la alerta hasta su cierre:
1. Recepción y registro de la alerta.
2. Triaje inicial (N1): clasificación de severidad y determinación de acción.
3. Investigación (N2): análisis detallado si procede.
4. Respuesta: ejecución de acciones de contención y remediación.
5. Cierre: documentación final y lecciones aprendidas.

### Respuesta a incidentes

Basado en marcos reconocidos como el [NIST SP 800-61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) o las guías del [CCN-CERT](https://www.ccn-cert.cni.es/):
1. Preparación.
2. Detección y análisis.
3. Contención.
4. Erradicación.
5. Recuperación.
6. Lecciones aprendidas.

### Threat hunting

Proceso proactivo de búsqueda de amenazas:
1. Formulación de hipótesis basada en inteligencia de amenazas.
2. Recopilación de datos relevantes.
3. Investigación y análisis.
4. Documentación de hallazgos.
5. Conversión de hallazgos en nuevas reglas de detección.

### Gestión de casos de uso

Los casos de uso son las reglas de detección que alimentan el SIEM:
1. Identificación de amenazas relevantes (basada en [MITRE ATT&CK](https://attack.mitre.org/)).
2. Diseno de la lógica de detección.
3. Implementación en el SIEM.
4. Prueba y validación.
5. Operación y ajuste continuo.

### Métricas y KPI

Mide la eficacia del SOC con métricas clave:
- **MTTD (Mean Time to Detect)**: tiempo medio desde que ocurre un incidente hasta que se detecta.
- **MTTR (Mean Time to Respond)**: tiempo medio desde la detección hasta la contención.
- **Tasa de falsos positivos**: porcentaje de alertas que resultan ser falsos positivos.
- **Volumen de alertas por analista**: indicador de carga de trabajo.
- **Cobertura MITRE ATT&CK**: porcentaje de técnicas del framework cubiertas por reglas de detección.

## De 96K a 1.5M EUR/año: rangos de coste según modelo SOC

El coste de un SOC varía enormemente según el modelo, el tamaño y la madurez deseada. Estas son referencias orientativas para el mercado español en 2026:

### SOC interno

- **Personal** (equipo mínimo para 24/7: 8-10 personas): entre 450.000 y 700.000 euros anuales en salarios y costes asociados.
- **Tecnología** (SIEM, EDR, SOAR, infraestructura): entre 150.000 y 500.000 euros anuales en licencias, dependiendo del volumen de datos y las herramientas elegidas.
- **Infraestructura física**: entre 50.000 y 200.000 euros de inversión inicial (sala de operaciones, monitores, servidores).
- **Formación y certificaciones**: entre 30.000 y 60.000 euros anuales.
- **Coste total estimado primer año**: entre 700.000 y 1.500.000 euros.
- **Coste anual recurrente**: entre 650.000 y 1.200.000 euros.

### SOC externalizado (MSSP/MDR)

- **Coste típico para una empresa mediana**: entre 8.000 y 25.000 euros mensuales (96.000 a 300.000 euros anuales), dependiendo del alcance del servicio, el número de fuentes de datos y los SLA contratados.

### SOC híbrido

- **Equipo interno reducido** (3-4 personas): entre 180.000 y 320.000 euros anuales.
- **Servicio MSSP complementario**: entre 5.000 y 15.000 euros mensuales.
- **Coste total estimado**: entre 250.000 y 500.000 euros anuales.

Riskitera ofrece servicios de SOC gestionado 24/7 con un modelo flexible que se adapta a las necesidades de cada organización, combinando analistas experimentados con tecnología avanzada de detección y respuesta.

## Los 5 errores que hunden un SOC antes del primer año

Estos son los errores que vemos con más frecuencia en organizaciones que intentan montar un SOC:

### Empezar por la tecnología en lugar de por los procesos

Muchas empresas invierten en herramientas caras antes de definir qué quieren detectar, como van a responder y quien va a operar el SOC. La tecnología debe servir a los procesos, no al reves.

### Subestimar las necesidades de personal

Un SOC 24/7 requiere más personal del que parece. Contar con solo dos o tres analistas para cubrir turnos de noche, fines de semana, vacaciones y bajas es una receta para el burnout y la rotación.

### No definir casos de uso antes de desplegar el SIEM

Conectar todas las fuentes de logs al SIEM sin haber definido que se quiere detectar genera un volumen insostenible de alertas, la mayoría irrelevantes. Es mejor empezar con 20-30 casos de uso bien afinados y crecer gradualmente.

### Ignorar la fatiga de alertas

Si los analistas reciben cientos de alertas diarias, la mayoría falsos positivos, dejaran de prestar atención. El tuning continuo de las reglas de detección y la automatización mediante SOAR son esenciales.

### No medir la eficacia

Sin métricas claras (MTTD, MTTR, tasa de falsos positivos), es imposible saber si el SOC esta funcionando o si es simplemente un centro de monitorización pasivo.

### Olvidar la formación continua

El panorama de amenazas cambia constantemente. Un equipo SOC que no se forma continuamente quedará obsoleto en meses. Destina presupuesto y tiempo para certificaciones, ejercicios de red team y participación en comunidades de seguridad.

{{< cta type="mofu" text="¿Planificando tu SOC? Solicita una evaluación gratuita y descubre cómo Riskitera reduce el tiempo de despliegue." >}}

## Preguntas frecuentes

### ¿A partir de qué tamaño de empresa tiene sentido un SOC?

No existe un umbral único. Como referencia general, las empresas con más de 200-300 empleados, que operan en sectores regulados o que manejan datos sensibles, suelen beneficiarse de un SOC, aunque sea en modelo externalizado o híbrido. La decisión depende más del perfil de riesgo que del tamaño: una fintech con 50 empleados pero que procesa millones de transacciones puede necesitar un SOC antes que una empresa industrial de 500 empleados con baja exposición digital.

### ¿Cuánto tiempo se tarda en montar un SOC desde cero?

Para un SOC interno con capacidad operativa básica (cobertura 8x5, casos de uso iniciales, equipo formado), entre 6 y 9 meses. Para alcanzar un SOC maduro con cobertura 24/7, threat hunting proactivo y automatización avanzada, entre 18 y 24 meses. Un SOC externalizado puede estar operativo en 4-8 semanas.

### ¿Puedo montar un SOC solo con herramientas open source?

Tecnicamente si. Elastic Security como SIEM, [Wazuh](https://wazuh.com/) como EDR, Shuffle como SOAR, MISP como plataforma de inteligencia y TheHive como sistema de ticketing forman un stack funcional. El coste de licencias será mínimo, pero necesitaras personal con experiencia para desplegar, configurar, mantener y operar estas herramientas, lo que puede suponer un coste mayor en personal cualificado.

### ¿Qué certificaciones debería tener el equipo del SOC?

Las certificaciones más valoradas en el mercado español para equipos SOC son: [CompTIA Security+](https://www.comptia.org/certifications/security) y CySA+ para N1, GCIH y ECIH para N2, y GCFA, GREM u OSCP para N3. Para el SOC Manager, CISM o [CISSP](https://www.isc2.org/certifications/cissp). Las certificaciones específicas de fabricantes (Splunk Certified Power User, Microsoft SC-200) también son muy útiles para los roles de ingeniería.

### ¿Cómo se mide el ROI de un SOC?

El ROI del SOC se mide comparando el coste del SOC con el coste evitado por incidentes. Las métricas clave son: reducción del tiempo de detección (MTTD), reducción del tiempo de respuesta (MTTR), número de incidentes contenidos antes de que causaran daño, reducción del coste medio por incidente y ahorro en sanciones regulatorias evitadas. Según el Ponemon Institute, las organizaciones con SOC maduro reducen el coste medio por brecha de datos en un 40 a 50 por ciento.
