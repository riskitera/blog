---
title: "Analista SOC: roles N1, N2 y N3 explicados con detalle"
image: "cover.png"
description: "Guia completa sobre los roles de analista SOC: que hace cada nivel (N1, N2, N3), habilidades requeridas, herramientas, trayectoria profesional y salarios en Espana."
slug: "analista-soc-roles-n1-n2-n3"
date: 2026-04-09
lastmod: 2026-04-09
draft: false
tags: ["SOC", "Carreras", "Operaciones"]
categories: ["SOC"]
author: "David Moya"
translationKey: "soc-analyst-roles"
---

El analista de un Centro de Operaciones de Seguridad (SOC) es uno de los perfiles profesionales con mayor demanda en el mercado de ciberseguridad. Segun datos del Observatorio Nacional de Tecnologia y Sociedad (ONTSI), Espana necesitara cubrir mas de 83.000 puestos de ciberseguridad entre 2025 y 2028, y los analistas SOC representan una parte significativa de esa demanda. Pero no todos los analistas SOC hacen lo mismo: el rol se estructura en tres niveles (N1, N2 y N3) con responsabilidades, habilidades y perfiles muy diferenciados.

<!--more-->

{{< key-takeaways >}}
- N1 (triaje): monitoriza alertas y ejecuta playbooks. Perfil: 1-2 anos experiencia, Security+/CySA+
- N2 (incidentes): investiga en profundidad y coordina respuesta. Perfil: 3-5 anos, GCIH/ECIH
- N3 (threat hunter): caza proactiva y analisis avanzado de malware. Perfil: 5+ anos, GCFA/OSCP
- Un SOC 24/7 necesita minimo 5-6 analistas N1 para cubrir turnos con vacaciones y bajas
- Salarios en Espana (2026): N1 25-35K EUR, N2 38-55K EUR, N3 55-80K EUR
{{< /key-takeaways >}}

## Que es un analista SOC y que hace?

Un analista SOC es el profesional encargado de monitorizar, detectar, investigar y responder a las amenazas de ciberseguridad que afectan a una organizacion. Trabaja dentro de un Centro de Operaciones de Seguridad, utilizando herramientas especializadas como SIEM, EDR y SOAR para proteger los activos digitales de la empresa.

El trabajo del analista SOC es fundamentalmente operativo: se trata de estar en la primera linea de defensa, analizando en tiempo real las alertas de seguridad, investigando actividades sospechosas y ejecutando acciones de respuesta cuando se confirma un incidente. Es un rol que exige atencion al detalle, capacidad de analisis bajo presion y actualizacion constante de conocimientos.

Si quieres entender el contexto completo en el que trabajan estos profesionales, te recomendamos nuestra [guia sobre como montar un SOC desde cero](/es/posts/2026/04/como-montar-soc-desde-cero/), donde explicamos la estructura, herramientas y procesos de un Centro de Operaciones de Seguridad.

## Que hace un analista SOC N1?

El analista N1 (tambien llamado Tier 1 o analista de triaje) es el punto de entrada al mundo del SOC y la primera linea de defensa de la organizacion. Su funcion principal es monitorizar las alertas de seguridad en tiempo real, realizar un triaje inicial y determinar si requieren investigacion adicional o si se trata de falsos positivos.

### Responsabilidades del N1

- **Monitorizacion continua de alertas**: supervisa las consolas del SIEM, los paneles de EDR y otras herramientas de seguridad durante su turno, identificando las alertas que requieren atencion.
- **Triaje y clasificacion**: para cada alerta, el N1 realiza una evaluacion rapida para determinar si es un verdadero positivo, un falso positivo o si requiere escalado a N2. Utiliza playbooks predefinidos para guiar su analisis.
- **Documentacion**: registra cada alerta en el sistema de ticketing, documentando la informacion relevante, las acciones realizadas y la decision tomada (cierre, escalado o respuesta).
- **Ejecucion de playbooks basicos**: ante incidentes rutinarios (phishing confirmado, malware detectado por el antivirus, intentos de acceso fallidos repetidos), ejecuta los procedimientos de respuesta predefinidos.
- **Comunicacion de escalados**: cuando una alerta requiere investigacion avanzada, prepara un resumen claro y detallado para el analista N2.

### Habilidades requeridas para N1

**Conocimientos tecnicos:**
- Fundamentos de redes: modelo TCP/IP, puertos y protocolos comunes (HTTP, HTTPS, DNS, SMTP, SSH, RDP), analisis basico de trafico con Wireshark.
- Sistemas operativos: conocimiento funcional de Windows y Linux, capacidad de navegar por el sistema de archivos, revisar logs del sistema y entender procesos.
- Seguridad basica: tipos de amenazas (malware, phishing, denegacion de servicio, fuerza bruta), vectores de ataque comunes, conceptos de autenticacion y autorizacion.
- Herramientas SIEM: capacidad de navegar por la interfaz, realizar busquedas basicas y entender la logica de las alertas.

**Habilidades blandas:**
- Atencion al detalle: la capacidad de distinguir una alerta real de un falso positivo depende de observar los detalles.
- Trabajo bajo presion: los turnos de SOC pueden ser intensos, con multiples alertas simultaneas.
- Comunicacion: documentar de forma clara y concisa es fundamental para que los escalados a N2 sean eficientes.
- Disciplina: seguir los playbooks y procedimientos sin atajos.

### Herramientas que usa el N1

- SIEM ([Splunk](https://www.splunk.com/), QRadar, [Elastic Security](https://www.elastic.co/security), [Microsoft Sentinel](https://azure.microsoft.com/products/microsoft-sentinel)) para monitorizar y buscar eventos.
- EDR (CrowdStrike, Defender for Endpoint, SentinelOne) para validar alertas en endpoints.
- Sistema de ticketing (ServiceNow, Jira, TheHive) para documentar y gestionar alertas.
- Herramientas de busqueda de reputacion: VirusTotal, AbuseIPDB, Shodan, OTX AlienVault.
- Playbooks y runbooks del SOC.

### Un dia tipico de un analista N1

El turno comienza con un handover del turno anterior: revision de alertas pendientes, incidentes en curso y cualquier novedad relevante. Durante las siguientes 8-12 horas (dependiendo de la rotacion), el analista revisa las alertas que llegan a la consola del SIEM, realizando triaje de cada una. En un turno activo, un N1 puede procesar entre 40 y 100 alertas. La mayoria seran falsos positivos o alertas de baja severidad que se cierran directamente. Entre un 10 y un 20 por ciento requerira algun tipo de analisis adicional, y un porcentaje menor se escalara a N2.

## Que hace un analista SOC N2?

El analista N2 (Tier 2 o analista de incidentes) es el investigador del SOC. Recibe las alertas escaladas por N1 y realiza un analisis en profundidad para determinar el alcance, la gravedad y el impacto del incidente. Es el responsable de coordinar la respuesta tecnica.

### Responsabilidades del N2

- **Investigacion profunda de incidentes**: analiza las alertas escaladas, correlaciona eventos de multiples fuentes (SIEM, EDR, logs de aplicaciones, trafico de red) y determina la naturaleza y el alcance del incidente.
- **Analisis de malware basico**: realiza analisis estatico y dinamico basico de muestras sospechosas en sandboxes, identifica indicadores de compromiso (IoC) y evalua el impacto potencial.
- **Forense preliminar**: recopila y preserva evidencias digitales, realiza analisis de memoria, disco y red cuando es necesario para entender la cadena de ataque.
- **Coordinacion de la respuesta**: dirige las acciones de contencion (aislamiento de hosts, bloqueo de IPs, revocacion de credenciales) y trabaja con los equipos de TI para la remediacion.
- **Desarrollo de reglas de deteccion**: basandose en los incidentes investigados, propone y desarrolla nuevas reglas de correlacion para el SIEM y mejora los playbooks existentes.
- **Generacion de informes**: redacta informes detallados de incidentes que incluyen la cronologia, el analisis tecnico, las acciones realizadas y las recomendaciones.

### Habilidades requeridas para N2

**Conocimientos tecnicos:**
- Analisis avanzado de logs: capacidad de correlacionar eventos de multiples fuentes para reconstruir la cadena de ataque completa.
- Conocimiento del framework [MITRE ATT&CK](https://attack.mitre.org/): mapeo de tecnicas y tacticas de los atacantes para entender y documentar los incidentes.
- Analisis de malware: analisis estatico (strings, hashes, imports, pe headers) y dinamico basico (ejecucion en sandbox, analisis de comportamiento).
- Forense digital: adquisicion de evidencias, analisis de memoria (Volatility), analisis de disco (Autopsy), analisis de trafico de red (Wireshark, Zeek).
- Scripting: Python y/o PowerShell para automatizar tareas de investigacion y analisis.
- Conocimiento profundo de ataques: tecnicas de movimiento lateral, escalada de privilegios, persistencia, exfiltracion de datos.

**Habilidades blandas:**
- Pensamiento analitico: capacidad de conectar puntos dispares para formar una imagen coherente del incidente.
- Gestion del estres: los incidentes graves generan presion por parte de la direccion y de los equipos afectados.
- Comunicacion tecnica: explicar hallazgos complejos tanto a audiencias tecnicas como no tecnicas.
- Mentorizacion: los N2 deben ayudar al desarrollo profesional de los N1.

### Herramientas que usa el N2

Ademas de todas las herramientas del N1, el analista N2 utiliza:
- SOAR (Palo Alto XSOAR, Splunk SOAR, Tines) para orquestar la respuesta.
- Herramientas forenses: Velociraptor, Autopsy, Volatility, FTK Imager.
- Sandboxes de malware: Any.Run, Joe Sandbox, Cuckoo Sandbox.
- Plataformas de inteligencia de amenazas: MISP, Recorded Future, Mandiant Advantage.
- Herramientas de analisis de red: Zeek, NetworkMiner, Arkime.
- Lenguajes de scripting: Python, PowerShell, Bash.

## Que hace un analista SOC N3?

El analista N3 (Tier 3, threat hunter o analista senior) representa el nivel mas alto de experiencia tecnica dentro del SOC. Su rol trasciende la respuesta reactiva a incidentes: se centra en la caza proactiva de amenazas, el analisis avanzado y la mejora estrategica de las capacidades de deteccion.

### Responsabilidades del N3

- **Threat hunting proactivo**: formula hipotesis de amenazas basadas en inteligencia de amenazas, tendencias del sector y conocimiento del entorno, y las investiga activamente buscando indicios de compromiso que hayan eludido las detecciones automatizadas.
- **Ingenieria inversa de malware**: analisis avanzado de muestras de malware, incluyendo desempaquetado, debugging, analisis de codigo y extraccion de configuraciones y comunicaciones con servidores de mando y control (C2).
- **Forense digital avanzado**: investigaciones complejas que pueden implicar multiples sistemas, periodos temporales extensos y tecnicas sofisticadas de ocultacion por parte del atacante.
- **Desarrollo de inteligencia de amenazas**: analiza tendencias, genera informes estrategicos de amenazas y traduce la inteligencia en acciones concretas de mejora de la deteccion.
- **Arquitectura de deteccion**: disena la estrategia de deteccion del SOC, define los casos de uso prioritarios basandose en MITRE ATT&CK y optimiza la eficacia global de las reglas.
- **Red teaming y purple teaming**: colabora con equipos de red team para validar las capacidades de deteccion y participa en ejercicios conjuntos (purple team) para mejorar la cobertura.
- **Mentorizacion y formacion**: forma a los analistas N1 y N2, comparte conocimientos y eleva el nivel tecnico global del equipo.

### Habilidades requeridas para N3

**Conocimientos tecnicos:**
- Ingenieria inversa: uso fluido de herramientas como Ghidra, IDA Pro, x64dbg. Conocimiento de lenguaje ensamblador (x86/x64) y capacidad de analizar binarios complejos.
- Threat hunting: metodologias estructuradas de caza de amenazas, capacidad de formular y probar hipotesis, conocimiento profundo de TTPs de grupos APT.
- Desarrollo de detecciones: creacion de reglas Sigma, YARA, Snort/Suricata, escritura de consultas avanzadas en el lenguaje del SIEM.
- Programacion: Python avanzado, capacidad de desarrollar herramientas propias para analisis, automatizacion e integracion.
- Conocimiento profundo de infraestructura: Active Directory, entornos cloud (AWS, Azure, GCP), contenedores, arquitecturas de microservicios.
- Inteligencia de amenazas: modelos Diamond, Kill Chain, MITRE ATT&CK a nivel experto. Conocimiento de grupos APT relevantes para el sector.

**Habilidades blandas:**
- Pensamiento estrategico: capacidad de ver mas alla del incidente individual y disenar mejoras sistemicas.
- Autonomia: los N3 trabajan con poca supervision directa y deben ser capaces de planificar y ejecutar investigaciones complejas de forma independiente.
- Liderazgo tecnico: capacidad de influir en la direccion tecnica del SOC sin necesariamente tener autoridad jerarquica directa.
- Comunicacion ejecutiva: capacidad de traducir hallazgos tecnicos complejos en riesgos de negocio comprensibles para la direccion.

### Herramientas que usa el N3

Ademas de las herramientas de N1 y N2:
- Ingenieria inversa: Ghidra, IDA Pro, x64dbg, Binary Ninja.
- Analisis de malware: Remnux, FlareVM, PEStudio, dnSpy.
- Desarrollo de detecciones: Sigma (reglas de deteccion genericas), YARA (deteccion de malware), Snort/Suricata (deteccion en red).
- Threat intelligence avanzada: STIX/TAXII, OpenCTI, MITRE ATT&CK Navigator.
- Entornos de laboratorio: maquinas virtuales dedicadas, redes aisladas para analisis de malware.
- Herramientas de desarrollo: Git, Docker, entornos de CI/CD para automatizacion de pipelines de analisis.

{{< cta type="tofu" text="Riskitera potencia a tus analistas SOC con triage automatizado por IA, reduciendo el ruido en N1 y liberando tiempo para N2 y N3." label="Descubrir mas" >}}

## Como es la trayectoria profesional de un analista SOC?

La carrera de un analista SOC es una progresion natural que, con dedicacion y formacion continua, puede llevar desde un perfil junior hasta posiciones de liderazgo tecnico o de gestion.

### Ruta tipica

1. **Formacion inicial** (0-1 ano): grado en informatica, ingenieria de telecomunicaciones o formacion profesional en ciberseguridad. Certificaciones iniciales como CompTIA Security+ o CEH.

2. **Analista N1** (1-2 anos): primer contacto con el SOC. Aprendizaje intensivo de herramientas, procesos y tipos de amenazas. Es la fase donde se construye la base practica.

3. **Analista N2** (3-5 anos): tras demostrar competencia en triaje y adquirir conocimientos mas profundos de investigacion y respuesta, el analista progresa a N2. Es comun obtener certificaciones como GCIH, ECIH o BTL1 en esta fase.

4. **Analista N3 / Threat Hunter** (5+ anos): requiere especializacion en un area concreta (forense, malware, threat intelligence) y una vision estrategica de la seguridad. Certificaciones como GCFA, GREM, OSCP o GXPN marcan la diferencia.

5. **Roles avanzados** (7+ anos): SOC Manager, responsable de threat intelligence, arquitecto de seguridad, CISO. La bifurcacion entre la via tecnica y la via de gestion se produce habitualmente entre los 5 y los 8 anos de carrera.

### Formacion continua

El campo de la ciberseguridad evoluciona a una velocidad que hace imprescindible la formacion permanente:
- **Plataformas de practica**: TryHackMe, HackTheBox, LetsDefend, CyberDefenders.
- **Competiciones CTF**: participar en Capture The Flag es una forma excelente de desarrollar habilidades practicas.
- **Comunidad**: participacion en grupos como el FIRST, CSIRT.es, o los eventos del [CCN-CERT](https://www.ccn-cert.cni.es/) (STIC Congress).
- **Conferencias**: RootedCON, Navaja Negra, CyberCamp ([INCIBE](https://www.incibe.es/)), h-c0n, Ekoparty.
- **Publicaciones y blogs**: lectura habitual de informes de amenazas de Mandiant, CrowdStrike, Microsoft Threat Intelligence, Recorded Future.

## Cuanto gana un analista SOC en Espana en 2026?

Los salarios en ciberseguridad en Espana han experimentado un crecimiento sostenido en los ultimos anos, impulsados por la escasez de talento y la creciente demanda regulatoria. Estos son los rangos salariales orientativos para 2026, basados en datos de portales de empleo, encuestas sectoriales y nuestra experiencia en el mercado:

### Analista N1
- **Junior (0-1 ano de experiencia)**: 22.000 - 28.000 euros brutos anuales.
- **Con experiencia (1-2 anos)**: 28.000 - 35.000 euros brutos anuales.
- En Madrid y Barcelona, los salarios tienden a situarse en la parte alta del rango. El trabajo en turnos nocturnos y fines de semana puede incluir complementos adicionales.

### Analista N2
- **3-4 anos de experiencia**: 35.000 - 45.000 euros brutos anuales.
- **4-5 anos con certificaciones**: 45.000 - 55.000 euros brutos anuales.
- Los perfiles con experiencia en respuesta a incidentes en sectores regulados (banca, energia, sanidad) suelen estar en la parte alta del rango.

### Analista N3 / Threat Hunter
- **5-7 anos de experiencia**: 50.000 - 65.000 euros brutos anuales.
- **7+ anos, altamente especializado**: 65.000 - 80.000 euros brutos anuales.
- Los perfiles excepcionales con especializacion en ingenieria inversa de malware o threat hunting avanzado pueden superar los 80.000 euros, especialmente si trabajan para empresas internacionales con oficinas en Espana.

### SOC Manager
- **Experiencia media**: 55.000 - 70.000 euros brutos anuales.
- **SOC Manager senior en grandes organizaciones**: 70.000 - 95.000 euros brutos anuales.

Es importante senalar que el trabajo remoto ha ampliado las opciones: muchos analistas SOC espanoles trabajan para empresas europeas o americanas con salarios significativamente superiores a los del mercado local.

El equipo SOC de Riskitera esta formado por analistas de todos los niveles con experiencia en sectores regulados, ofreciendo servicios de monitorizacion, deteccion y respuesta 24/7 a organizaciones que necesitan capacidades SOC sin la complejidad de montarlo internamente.

## Como convertirse en analista SOC?

Para quienes quieran iniciar una carrera como analistas SOC, este es el camino recomendado:

### Paso 1: Formacion base

Un grado universitario en informatica, telecomunicaciones o ciberseguridad proporciona una base solida, pero no es imprescindible. Los ciclos formativos de grado superior en ciberseguridad, administracion de sistemas o desarrollo de aplicaciones tambien son puntos de entrada validos. Lo fundamental es tener buenos cimientos en redes, sistemas operativos y programacion basica.

### Paso 2: Certificaciones iniciales

[CompTIA Security+](https://www.comptia.org/certifications/security) es la certificacion mas recomendada como punto de partida. Tambien son utiles CompTIA Network+ (si necesitas reforzar redes) y la certificacion SC-900 de Microsoft como primera aproximacion a la seguridad cloud.

### Paso 3: Practica en laboratorios

Plataformas como TryHackMe (especialmente las rutas de SOC Analyst y Cyber Defense), LetsDefend y CyberDefenders ofrecen entornos de practica realistas que simulan el trabajo diario de un analista SOC. Dedicar 2-3 meses a estas plataformas antes de buscar empleo marca una diferencia notable en las entrevistas.

### Paso 4: Construir un perfil visible

Documenta tu aprendizaje en un blog tecnico o en LinkedIn. Participa en CTF de tipo blue team (defensivos). Contribuye a proyectos de codigo abierto relacionados con seguridad. Los reclutadores valoran los perfiles que demuestran iniciativa y pasion por la ciberseguridad.

### Paso 5: Primer empleo

Busca posiciones de analista SOC N1, SOC junior o security analyst en empresas de servicios de ciberseguridad (MSSP/MDR), grandes consultoras o departamentos de seguridad de empresas medianas y grandes. Las empresas de servicios gestionados suelen ser el mejor punto de entrada porque exponen a los analistas a una variedad de tecnologias y tipos de incidentes.

{{< cta type="mofu" text="¿Buscas mejorar la eficiencia de tu equipo SOC? Descubre como Riskitera automatiza el triage y escala alertas con contexto." >}}

## Preguntas frecuentes

### Necesito un titulo universitario para ser analista SOC?

No es estrictamente necesario, aunque si es recomendable. Muchos analistas SOC exitosos provienen de formacion profesional de grado superior en ciberseguridad o administracion de sistemas. Lo que realmente importa es el conocimiento practico demostrable: certificaciones reconocidas (CompTIA Security+, CySA+, GCIH), experiencia en laboratorios y plataformas de practica, y la capacidad de analizar y resolver problemas tecnicos. Dicho esto, un titulo universitario sigue siendo un requisito en muchas ofertas de empleo, especialmente en grandes corporaciones y en el sector publico.

### Cuanto tiempo se tarda en pasar de N1 a N2?

La progresion tipica de N1 a N2 es de 2 a 3 anos, aunque depende de factores individuales como la capacidad de aprendizaje, la calidad de la mentorizacion recibida, el volumen y la complejidad de los incidentes gestionados, y la formacion complementaria. Los analistas N1 que toman iniciativa para aprender fuera de su rol (participan en investigaciones N2, estudian malware, desarrollan scripts de automatizacion) suelen progresar mas rapido.

### Que diferencia hay entre un analista SOC y un pentester?

Son roles complementarios pero distintos. El analista SOC es un perfil defensivo (blue team): detecta, investiga y responde a amenazas reales contra los sistemas de la organizacion. El pentester es un perfil ofensivo (red team): simula ataques para encontrar vulnerabilidades antes de que los atacantes reales las exploten. Ambos requieren conocimientos tecnicos solidos, pero la mentalidad y las habilidades del dia a dia son diferentes. Algunos profesionales evolucionan hacia el purple teaming, que combina ambos enfoques.

### Es sostenible trabajar en turnos de SOC a largo plazo?

Los turnos rotativos (manana, tarde, noche) son una realidad del trabajo en SOC 24/7 y pueden generar desgaste si no se gestionan bien. La clave esta en la organizacion del equipo: una rotacion equilibrada con suficiente personal para cubrir vacaciones y descansos, politicas claras de compensacion por nocturnidad y fines de semana, y una cultura que valore el bienestar del equipo. Muchos analistas trabajan en turnos durante los primeros anos de su carrera (N1 y N2) y progresivamente migran a roles con horarios mas regulares (N3, SOC Manager, ingenieria de deteccion) a medida que ganan experiencia.

### Que idiomas necesita un analista SOC?

El espanol es obviamente necesario para el mercado laboral espanol. El ingles es imprescindible: la documentacion tecnica, los informes de amenazas, las comunidades profesionales y la mayoria de las herramientas estan en ingles. Un nivel B2 o superior de ingles tecnico es un requisito de facto para cualquier posicion SOC. Otros idiomas (portugues, aleman, frances) son un plus, especialmente en SOC que dan servicio a clientes internacionales.
