---
title: "Analista SOC: roles N1, N2 y N3 explicados con detalle"
image: "cover.png"
description: "Guía completa sobre los roles de analista SOC: que hace cada nivel (N1, N2, N3), habilidades requeridas, herramientas, trayectoria profesional y salarios en España."
slug: "analista-soc-roles-n1-n2-n3"
date: 2026-04-09
lastmod: 2026-04-09
draft: false
tags: ["SOC", "Carreras", "Operaciones"]
categories: ["SOC"]
author: "David Moya"
translationKey: "soc-analyst-roles"
---

El analista de un Centro de Operaciones de Seguridad (SOC) es uno de los perfiles profesionales con mayor demanda en el mercado de ciberseguridad. Según datos del Observatorio Nacional de Tecnología y Sociedad (ONTSI), España necesitará cubrir más de 83.000 puestos de ciberseguridad entre 2025 y 2028, y los analistas SOC representan una parte significativa de esa demanda. Pero no todos los analistas SOC hacen lo mismo: el rol se estructura en tres niveles (N1, N2 y N3) con responsabilidades, habilidades y perfiles muy diferenciados.

<!--more-->

{{< key-takeaways >}}
- N1 (triaje): monitoriza alertas y ejecuta playbooks. Perfil: 1-2 años experiencia, Security+/CySA+
- N2 (incidentes): investiga en profundidad y coordina respuesta. Perfil: 3-5 años, GCIH/ECIH
- N3 (threat hunter): caza proactiva y análisis avanzado de malware. Perfil: 5+ años, GCFA/OSCP
- Un SOC 24/7 necesita mínimo 5-6 analistas N1 para cubrir turnos con vacaciones y bajas
- Salarios en España (2026): N1 25-35K EUR, N2 38-55K EUR, N3 55-80K EUR
{{< /key-takeaways >}}

## Qué es un analista SOC y que hace?

Un analista SOC es el profesional encargado de monitorizar, detectar, investigar y responder a las amenazas de ciberseguridad que afectan a una organización. Trabaja dentro de un Centro de Operaciones de Seguridad, utilizando herramientas especializadas como SIEM, EDR y SOAR para proteger los activos digitales de la empresa.

El trabajo del analista SOC es fundamentalmente operativo: se trata de estar en la primera línea de defensa, analizando en tiempo real las alertas de seguridad, investigando actividades sospechosas y ejecutando acciones de respuesta cuando se confirma un incidente. Es un rol que exige atención al detalle, capacidad de análisis bajo presión y actualización constante de conocimientos.

Si quieres entender el contexto completo en el que trabajan estos profesionales, te recomendamos nuestra [guía sobre como montar un SOC desde cero](/es/posts/2026/04/como-montar-soc-desde-cero/), donde explicamos la estructura, herramientas y procesos de un Centro de Operaciones de Seguridad.

## Qué hace un analista SOC N1?

El analista N1 (también llamado Tier 1 o analista de triaje) es el punto de entrada al mundo del SOC y la primera línea de defensa de la organización. Su función principal es monitorizar las alertas de seguridad en tiempo real, realizar un triaje inicial y determinar si requieren investigación adicional o si se trata de falsos positivos.

### Responsabilidades del N1

- **Monitorización continúa de alertas**: supervisa las consolas del SIEM, los paneles de EDR y otras herramientas de seguridad durante su turno, identificando las alertas que requieren atención.
- **Triaje y clasificación**: para cada alerta, el N1 realiza una evaluación rápida para determinar si es un verdadero positivo, un falso positivo o si requiere escalado a N2. Utiliza playbooks predefinidos para guiar su análisis.
- **Documentación**: registra cada alerta en el sistema de ticketing, documentando la información relevante, las acciones realizadas y la decisión tomada (cierre, escalado o respuesta).
- **Ejecución de playbooks básicos**: ante incidentes rutinarios (phishing confirmado, malware detectado por el antivirus, intentos de acceso fallidos repetidos), ejecuta los procedimientos de respuesta predefinidos.
- **Comunicación de escalados**: cuando una alerta requiere investigación avanzada, prepara un resumen claro y detallado para el analista N2.

### Habilidades requeridas para N1

**Conocimientos técnicos:**
- Fundamentos de redes: modelo TCP/IP, puertos y protocolos comunes (HTTP, HTTPS, DNS, SMTP, SSH, RDP), análisis básico de tráfico con Wireshark.
- Sistemas operativos: conocimiento funcional de Windows y Linux, capacidad de navegar por el sistema de archivos, revisar logs del sistema y entender procesos.
- Seguridad básica: tipos de amenazas (malware, phishing, denegación de servicio, fuerza bruta), vectores de ataque comunes, conceptos de autenticación y autorización.
- Herramientas SIEM: capacidad de navegar por la interfaz, realizar búsquedas básicas y entender la lógica de las alertas.

**Habilidades blandas:**
- Atención al detalle: la capacidad de distinguir una alerta real de un falso positivo depende de observar los detalles.
- Trabajo bajo presión: los turnos de SOC pueden ser intensos, con múltiples alertas simultaneas.
- Comunicación: documentar de forma clara y concisa es fundamental para que los escalados a N2 sean eficientes.
- Disciplina: seguir los playbooks y procedimientos sin atajos.

### Herramientas que usa el N1

- SIEM ([Splunk](https://www.splunk.com/), QRadar, [Elastic Security](https://www.elastic.co/security), [Microsoft Sentinel](https://azure.microsoft.com/products/microsoft-sentinel)) para monitorizar y buscar eventos.
- EDR (CrowdStrike, Defender for Endpoint, SentinelOne) para validar alertas en endpoints.
- Sistema de ticketing (ServiceNow, Jira, TheHive) para documentar y gestionar alertas.
- Herramientas de búsqueda de reputación: VirusTotal, AbuseIPDB, Shodan, OTX AlienVault.
- Playbooks y runbooks del SOC.

### Un día típico de un analista N1

El turno comienza con un handover del turno anterior: revisión de alertas pendientes, incidentes en curso y cualquier novedad relevante. Durante las siguientes 8-12 horas (dependiendo de la rotación), el analista revisa las alertas que llegan a la consola del SIEM, realizando triaje de cada una. En un turno activo, un N1 puede procesar entre 40 y 100 alertas. La mayoría serán falsos positivos o alertas de baja severidad que se cierran directamente. Entre un 10 y un 20 por ciento requerirá algun tipo de análisis adicional, y un porcentaje menor se escalara a N2.

## Qué hace un analista SOC N2?

El analista N2 (Tier 2 o analista de incidentes) es el investigador del SOC. Recibe las alertas escaladas por N1 y realiza un análisis en profundidad para determinar el alcance, la gravedad y el impacto del incidente. Es el responsable de coordinar la respuesta técnica.

### Responsabilidades del N2

- **Investigación profunda de incidentes**: analiza las alertas escaladas, correlacióna eventos de múltiples fuentes (SIEM, EDR, logs de aplicaciones, tráfico de red) y determina la naturaleza y el alcance del incidente.
- **Análisis de malware básico**: realiza análisis estático y dinámico básico de muestras sospechosas en sandboxes, identifica indicadores de compromiso (IoC) y evalúa el impacto potencial.
- **Forense preliminar**: recopila y preserva evidencias digitales, realiza análisis de memoria, disco y red cuando es necesario para entender la cadena de ataque.
- **Coordinación de la respuesta**: dirige las acciones de contención (aislamiento de hosts, bloqueo de IPs, revocación de credenciales) y trabaja con los equipos de TI para la remediación.
- **Desarrollo de reglas de detección**: basándose en los incidentes investigados, propone y desarrolla nuevas reglas de correlación para el SIEM y mejora los playbooks existentes.
- **Generación de informes**: redacta informes detallados de incidentes que incluyen la cronologia, el análisis técnico, las acciones realizadas y las recomendaciones.

### Habilidades requeridas para N2

**Conocimientos técnicos:**
- Análisis avanzado de logs: capacidad de correlaciónar eventos de múltiples fuentes para reconstruir la cadena de ataque completa.
- Conocimiento del framework [MITRE ATT&CK](https://attack.mitre.org/): mapeo de técnicas y tácticas de los atacantes para entender y documentar los incidentes.
- Análisis de malware: análisis estático (strings, hashes, imports, pe headers) y dinámico básico (ejecución en sandbox, análisis de comportamiento).
- Forense digital: adquisición de evidencias, análisis de memoria (Volatility), análisis de disco (Autopsy), análisis de tráfico de red (Wireshark, Zeek).
- Scripting: Python y/o PowerShell para automatizar táreas de investigación y análisis.
- Conocimiento profundo de ataques: técnicas de movimiento lateral, escalada de privilegios, persistencia, exfiltración de datos.

**Habilidades blandas:**
- Pensamiento analitico: capacidad de conectar puntos dispares para formar una imagen coherente del incidente.
- Gestión del estres: los incidentes graves generan presión por parte de la dirección y de los equipos afectados.
- Comunicación técnica: explicar hallazgos complejos tanto a audiencias técnicas como no técnicas.
- Mentorización: los N2 deben ayudar al desarrollo profesional de los N1.

### Herramientas que usa el N2

Además de todas las herramientas del N1, el analista N2 utiliza:
- SOAR (Palo Alto XSOAR, Splunk SOAR, Tines) para orquestar la respuesta.
- Herramientas forenses: Velociraptor, Autopsy, Volatility, FTK Imager.
- Sandboxes de malware: Any.Run, Joe Sandbox, Cuckoo Sandbox.
- Plataformas de inteligencia de amenazas: MISP, Recorded Future, Mandiant Advantage.
- Herramientas de análisis de red: Zeek, NetworkMiner, Arkime.
- Lenguajes de scripting: Python, PowerShell, Bash.

## Qué hace un analista SOC N3?

El analista N3 (Tier 3, threat hunter o analista senior) representa el nivel más alto de experiencia técnica dentro del SOC. Su rol trasciende la respuesta reactiva a incidentes: se centra en la caza proactiva de amenazas, el análisis avanzado y la mejora estratégica de las capacidades de detección.

### Responsabilidades del N3

- **Threat hunting proactivo**: fórmula hipótesis de amenazas basadas en inteligencia de amenazas, tendencias del sector y conocimiento del entorno, y las investiga activamente buscando indicios de compromiso que hayan eludido las detecciónes automatizadas.
- **Ingeniería inversa de malware**: análisis avanzado de muestras de malware, incluyendo desempaquetado, debugging, análisis de código y extracción de configuraciones y comunicaciones con servidores de mando y control (C2).
- **Forense digital avanzado**: investigaciónes complejas que pueden implicar múltiples sistemas, periodos temporales extensos y técnicas sofisticadas de ocultación por parte del atacante.
- **Desarrollo de inteligencia de amenazas**: analiza tendencias, genera informes estratégicos de amenazas y traduce la inteligencia en acciones concretas de mejora de la detección.
- **Arquitectura de detección**: diseña la estrategia de detección del SOC, define los casos de uso prioritarios basándose en MITRE ATT&CK y optimiza la eficacia global de las reglas.
- **Red teaming y purple teaming**: colabora con equipos de red team para validar las capacidades de detección y participa en ejercicios conjuntos (purple team) para mejorar la cobertura.
- **Mentorización y formación**: forma a los analistas N1 y N2, comparte conocimientos y eleva el nivel técnico global del equipo.

### Habilidades requeridas para N3

**Conocimientos técnicos:**
- Ingeniería inversa: uso fluido de herramientas como Ghidra, IDA Pro, x64dbg. Conocimiento de lenguaje ensamblador (x86/x64) y capacidad de analizar binarios complejos.
- Threat hunting: metodologías estructuradas de caza de amenazas, capacidad de formular y probar hipótesis, conocimiento profundo de TTPs de grupos APT.
- Desarrollo de detecciónes: creación de reglas Sigma, YARA, Snort/Suricata, escritura de consultas avanzadas en el lenguaje del SIEM.
- Programación: Python avanzado, capacidad de desarrollar herramientas propias para análisis, automatización e integración.
- Conocimiento profundo de infraestructura: Active Directory, entornos cloud (AWS, Azure, GCP), contenedores, arquitecturas de microservicios.
- Inteligencia de amenazas: modelos Diamond, Kill Chain, MITRE ATT&CK a nivel experto. Conocimiento de grupos APT relevantes para el sector.

**Habilidades blandas:**
- Pensamiento estratégico: capacidad de ver más allá del incidente individual y disenar mejoras sistemicas.
- Autonomia: los N3 trabajan con poca supervisión directa y deben ser capaces de planificar y ejecutar investigaciónes complejas de forma independiente.
- Liderazgo técnico: capacidad de influir en la dirección técnica del SOC sin necesariamente tener autoridad jerárquica directa.
- Comunicación ejecutiva: capacidad de traducir hallazgos técnicos complejos en riesgos de negocio comprensibles para la dirección.

### Herramientas que usa el N3

Además de las herramientas de N1 y N2:
- Ingeniería inversa: Ghidra, IDA Pro, x64dbg, Binary Ninja.
- Análisis de malware: Remnux, FlareVM, PEStudio, dnSpy.
- Desarrollo de detecciónes: Sigma (reglas de detección genéricas), YARA (detección de malware), Snort/Suricata (detección en red).
- Threat intelligence avanzada: STIX/TAXII, OpenCTI, MITRE ATT&CK Navigator.
- Entornos de laboratorio: máquinas virtuales dedicadas, redes aisladas para análisis de malware.
- Herramientas de desarrollo: Git, Docker, entornos de CI/CD para automatización de pipelines de análisis.

{{< cta type="tofu" text="Riskitera potencia a tus analistas SOC con triage automatizado por IA, reduciendo el ruido en N1 y liberando tiempo para N2 y N3." label="Descubrir más" >}}

## Cómo es la trayectoria profesional de un analista SOC?

La carrera de un analista SOC es una progresión natural que, con dedicación y formación continua, puede llevar desde un perfil junior hasta posiciones de liderazgo técnico o de gestión.

### Ruta típica

1. **Formación inicial** (0-1 año): grado en informática, ingeniería de telecomunicaciones o formación profesional en ciberseguridad. Certificaciones iniciales como CompTIA Security+ o CEH.

2. **Analista N1** (1-2 años): primer contacto con el SOC. Aprendizaje intensivo de herramientas, procesos y tipos de amenazas. Es la fase donde se construye la base práctica.

3. **Analista N2** (3-5 años): tras demostrar competencia en triaje y adquirir conocimientos más profundos de investigación y respuesta, el analista progresa a N2. Es común obtener certificaciones como GCIH, ECIH o BTL1 en esta fase.

4. **Analista N3 / Threat Hunter** (5+ años): requiere especialización en un area concreta (forense, malware, threat intelligence) y una visión estratégica de la seguridad. Certificaciones como GCFA, GREM, OSCP o GXPN marcan la diferencia.

5. **Roles avanzados** (7+ años): SOC Manager, responsable de threat intelligence, arquitecto de seguridad, CISO. La bifurcación entre la vía técnica y la vía de gestión se produce habitualmente entre los 5 y los 8 años de carrera.

### Formación continua

El campo de la ciberseguridad evoluciona a una velocidad que hace imprescindible la formación permanente:
- **Plataformas de práctica**: TryHackMe, HackTheBox, LetsDefend, CyberDefenders.
- **Competiciones CTF**: participar en Capture The Flag es una forma excelente de desarrollar habilidades prácticas.
- **Comunidad**: participación en grupos como el FIRST, CSIRT.es, o los eventos del [CCN-CERT](https://www.ccn-cert.cni.es/) (STIC Congress).
- **Conferencias**: RootedCON, Navaja Negra, CyberCamp ([INCIBE](https://www.incibe.es/)), h-c0n, Ekoparty.
- **Publicaciones y blogs**: lectura habitual de informes de amenazas de Mandiant, CrowdStrike, Microsoft Threat Intelligence, Recorded Future.

## Cuánto gana un analista SOC en España en 2026?

Los salarios en ciberseguridad en España han experimentado un crecimiento sostenido en los últimos años, impulsados por la escasez de talento y la creciente demanda regulatoria. Estos son los rangos salariales orientativos para 2026, basados en datos de portales de empleo, encuestas sectoriales y nuestra experiencia en el mercado:

### Analista N1
- **Junior (0-1 año de experiencia)**: 22.000 - 28.000 euros brutos anuales.
- **Con experiencia (1-2 años)**: 28.000 - 35.000 euros brutos anuales.
- En Madrid y Barcelona, los salarios tienden a situarse en la parte alta del rango. El trabajo en turnos nocturnos y fines de semana puede incluir complementos adicionales.

### Analista N2
- **3-4 años de experiencia**: 35.000 - 45.000 euros brutos anuales.
- **4-5 años con certificaciones**: 45.000 - 55.000 euros brutos anuales.
- Los perfiles con experiencia en respuesta a incidentes en sectores regulados (banca, energía, sanidad) suelen estar en la parte alta del rango.

### Analista N3 / Threat Hunter
- **5-7 años de experiencia**: 50.000 - 65.000 euros brutos anuales.
- **7+ años, altamente especializado**: 65.000 - 80.000 euros brutos anuales.
- Los perfiles excepcionales con especialización en ingeniería inversa de malware o threat hunting avanzado pueden superar los 80.000 euros, especialmente si trabajan para empresas internacionales con oficinas en España.

### SOC Manager
- **Experiencia media**: 55.000 - 70.000 euros brutos anuales.
- **SOC Manager senior en grandes organizaciones**: 70.000 - 95.000 euros brutos anuales.

Es importante senalar que el trabajo remoto ha ampliado las opciones: muchos analistas SOC españoles trabajan para empresas europeas o americanas con salarios significativamente superiores a los del mercado local.

El equipo SOC de Riskitera está formado por analistas de todos los niveles con experiencia en sectores regulados, ofreciendo servicios de monitorización, detección y respuesta 24/7 a organizaciones que necesitan capacidades SOC sin la complejidad de montarlo internamente.

## Cómo convertirse en analista SOC?

Para quienes quieran iniciar una carrera como analistas SOC, este es el camino recomendado:

### Paso 1: Formación base

Un grado universitario en informática, telecomunicaciones o ciberseguridad proporciona una base sólida, pero no es imprescindible. Los ciclos formativos de grado superior en ciberseguridad, administración de sistemas o desarrollo de aplicaciones también son puntos de entrada validos. Lo fundamental es tener buenos cimientos en redes, sistemas operativos y programación básica.

### Paso 2: Certificaciones iniciales

[CompTIA Security+](https://www.comptia.org/certifications/security) es la certificación más recomendada como punto de partida. También son útiles CompTIA Network+ (si necesitas reforzar redes) y la certificación SC-900 de Microsoft como primera aproximación a la seguridad cloud.

### Paso 3: Práctica en laboratorios

Plataformas como TryHackMe (especialmente las rutas de SOC Analyst y Cyber Defense), LetsDefend y CyberDefenders ofrecen entornos de práctica realistas que simulan el trabajo diario de un analista SOC. Dedicar 2-3 meses a estas plataformas antes de buscar empleo marca una diferencia notable en las entrevistas.

### Paso 4: Construir un perfil visible

Documenta tu aprendizaje en un blog técnico o en LinkedIn. Participa en CTF de tipo blue team (defensivos). Contribuye a proyectos de código abierto relacionados con seguridad. Los reclutadores valoran los perfiles que demuestran iniciativa y pasión por la ciberseguridad.

### Paso 5: Primer empleo

Busca posiciones de analista SOC N1, SOC junior o security analyst en empresas de servicios de ciberseguridad (MSSP/MDR), grandes consultoras o departamentos de seguridad de empresas medianas y grandes. Las empresas de servicios gestionados suelen ser el mejor punto de entrada porque exponen a los analistas a una variedad de tecnologías y tipos de incidentes.

{{< cta type="mofu" text="¿Buscas mejorar la eficiencia de tu equipo SOC? Descubre cómo Riskitera automatiza el triage y escala alertas con contexto." >}}

## Preguntas frecuentes

### Necesito un título universitario para ser analista SOC?

No es estrictamente necesario, aunque si es recomendable. Muchos analistas SOC exitosos provienen de formación profesional de grado superior en ciberseguridad o administración de sistemas. Lo que realmente importa es el conocimiento práctico demostrable: certificaciones reconocidas (CompTIA Security+, CySA+, GCIH), experiencia en laboratorios y plataformas de práctica, y la capacidad de analizar y resolver problemas técnicos. Dicho esto, un título universitario sigue siendo un requisito en muchas ofertas de empleo, especialmente en grandes corporaciones y en el sector público.

### Cuánto tiempo se tarda en pasar de N1 a N2?

La progresión típica de N1 a N2 es de 2 a 3 años, aunque depende de factores individuales como la capacidad de aprendizaje, la calidad de la mentorización recibida, el volumen y la complejidad de los incidentes gestionados, y la formación complementaria. Los analistas N1 que toman iniciativa para aprender fuera de su rol (participan en investigaciónes N2, estudian malware, desarrollan scripts de automatización) suelen progresar más rápido.

### Qué diferencia hay entre un analista SOC y un pentester?

Son roles complementarios pero distintos. El analista SOC es un perfil defensivo (blue team): detecta, investiga y responde a amenazas reales contra los sistemas de la organización. El pentester es un perfil ofensivo (red team): simula ataques para encontrar vulnerabilidades antes de que los atacantes reales las exploten. Ambos requieren conocimientos técnicos solidos, pero la mentalidad y las habilidades del día a día son diferentes. Algunos profesionales evolucionan hacia el purple teaming, que combina ambos enfoques.

### Es sostenible trabajar en turnos de SOC a largo plazo?

Los turnos rotativos (manana, tarde, noche) son una realidad del trabajo en SOC 24/7 y pueden generar desgaste si no se gestionan bien. La clave está en la organización del equipo: una rotación equilibrada con suficiente personal para cubrir vacaciones y descansos, políticas claras de compensación por nocturnidad y fines de semana, y una cultura que valore el bienestar del equipo. Muchos analistas trabajan en turnos durante los primeros años de su carrera (N1 y N2) y progresivamente migran a roles con horarios más regulares (N3, SOC Manager, ingeniería de detección) a medida que ganan experiencia.

### Qué idiomas necesita un analista SOC?

El español es obviamente necesario para el mercado laboral español. El inglés es imprescindible: la documentación técnica, los informes de amenazas, las comunidades profesionales y la mayoría de las herramientas están en ingles. Un nivel B2 o superior de inglés técnico es un requisito de facto para cualquier posición SOC. Otros idiomas (portugues, aleman, frances) son un plus, especialmente en SOC que dan servicio a clientes internacionales.
