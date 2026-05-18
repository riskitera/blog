---
title: "Threat Intelligence para empresas españolas: como empezar sin presupuesto"
description: "Guía práctica para que empresas españolas comiencen con threat intelligence sin presupuesto: fuentes gratuitas, herramientas open source, integración con el SOC y maduración del programa."
slug: "threat-intelligence-empresas-empezar"
date: 2026-07-04
publishDate: 2026-07-04
lastmod: 2026-07-04
draft: false
tags: ["CTI", "Threat Intelligence", "Herramientas"]
categories: ["CTI"]
author: "David Moya"
keyword: "threat intelligence empresas"
funnel: "mofu"
---

Guía práctica para que empresas españolas comiencen con threat intelligence sin presupuesto: fuentes gratuitas, herramientas open source, integración con el SOC y maduración del programa.

<!--more-->

{{< key-takeaways >}}
- La threat intelligence no requiere presupuesto inicial: las fuentes públicas españolas (CCN-CERT, INCIBE-CERT) y las plataformas gratuitas (AlienVault OTX, Abuse.ch) cubren el 80% de las necesidades de una PYME.
- Un programa de CTI efectivo sigue el ciclo de inteligencia: requisitos de los stakeholders, recolección, procesamiento, análisis y diseminación.
- MISP open source permite gestionar, correlaciónar y compartir indicadores de compromiso sin coste de licencia, integrando con cualquier SIEM.
- El error más común es confundir feeds de IOCs con threat intelligence. Los indicadores sin contexto son datos, no inteligencia.
- La operacionalización de la inteligencia (convertirla en reglas SIEM, políticas de bloqueo y decisiones de negocio) es lo que diferencia un programa funcional de uno decorativo.
{{< /key-takeaways >}}

## Qué es la threat intelligence y por que la necesita tu empresa

La Threat Intelligence (CTI, Cyber Threat Intelligence) es el proceso de recopilar, procesar y analizar información sobre amenazas cibernéticas para tomar decisiones informadas. No es una herramienta ni un producto. Es una función que transforma datos en bruto (IPs maliciosas, hashes de malware, reportes de vulnerabilidades) en conocimiento accionable para proteger tu organización.

La distinción clave es entre **datos**, **información** e **inteligencia**:

- **Dato.** Una IP aparece en una lista de comando y control: `185.220.101.42`.
- **Información.** Esa IP está asociada al malware Emotet y se usa como servidor C2 desde hace 3 días.
- **Inteligencia.** Emotet está distribuyendo phishing masivo contra el sector financiero español esta semana, usando adjuntos de Excel con macros. Tu empresa es del sector financiero, tus usuarios usan Excel y no tienes bloqueadas las macros en adjuntos externos. Acción recomendada: bloquear macros en documentos de origen externo y añadir la IP al blocklist del firewall.

### Por que las empresas españolas la necesitan especialmente

España ocupa posiciones destacadas en los rankings europeos de ciberataques recibidos. Según los datos del [CCN-CERT](https://www.ccn-cert.cni.es/), el organismo de respuesta a incidentes del Centro Criptológico Nacional, los incidentes gestionados han crecido un 25% interanual de media en los últimos cinco años. [INCIBE-CERT](https://www.incibe.es/incibe-cert), el CERT de referencia para empresas y ciudadanos, gestión más de 118.000 incidentes en su último informe anual.

Las empresas españolas enfrentan amenazas específicas:

- **Ransomware dirigido.** Grupos como Lockbit y Cl0p han atacado activamente a empresas españolas de infraestructura, sanidad y administración pública.
- **Phishing localizado.** Campañas en español que suplantan a Correos, la Agencia Tributaria, bancos locales (CaixaBank, BBVA, Santander) y la Seguridad Social.
- **Ciberespionaje.** Actores estatales con interés en sectores estratégicos españoles: defensa, energía, telecomunicaciones y diplomacia.
- **Fraude al CEO (BEC).** Especialmente dirigido a PYMES con procesos de pago poco formalizados.

Un programa de threat intelligence, incluso básico, permite a tu empresa pasar de una postura reactiva ("nos han atacado, que hacemos") a una proactiva ("sabemos que este tipo de ataque está activo contra nuestro sector, ya hemos implementado las contramedidas").

## El ciclo de inteligencia: estructura de un programa CTI

La threat intelligence no es suscribirse a feeds y olvidarse. Es un proceso cíclico con fases bien definidas. El modelo clásico de inteligencia (usado por agencias de inteligencia y adaptado a ciberseguridad) tiene cinco fases:

### Fase 1: Requisitos de inteligencia (Planning and Direction)

Antes de recopilar nada, necesitas saber qué información necesita tu organización. Los requisitos vienen de los stakeholders:

- **CISO / Responsable de seguridad.** "Necesito saber qué actores de amenaza están atacando nuestro sector en España y que técnicas usan."
- **Equipo SOC.** "Necesito IOCs frescos para alimentar las reglas del SIEM y el EDR."
- **Equipo de IT.** "Necesito saber qué vulnerabilidades están siendo explotadas activamente para priorizar el parcheo."
- **Dirección general.** "Necesito entender el nivel de riesgo ciber de la empresa en términos de negocio."

Los requisitos se formalizan como **Intelligence Requirements (IRs)**. Ejemplo:

| ID | Requisito | Stakeholder | Frecuencia |
|---|---|---|---|
| IR-01 | Actores de amenaza activos contra sector financiero en España | CISO | Mensual |
| IR-02 | IOCs asociados a campañas de phishing en español | SOC | Diaria |
| IR-03 | Vulnerabilidades críticas explotadas in-the-wild en software de nuestro stack | IT | Semanal |
| IR-04 | Tendencias de riesgo ciber para informe trimestral a comité | Dirección | Trimestral |

Sin requisitos claros, el programa de CTI se convierte en una actividad de "recopilar todo" que no aporta valor a nadie.

### Fase 2: Recolección (Collection)

Con los requisitos definidos, sabes que buscar. Las fuentes de recolección se clasifican en:

- **OSINT (Open Source Intelligence).** Fuentes públicas: feeds de IOCs, blogs de investigadores, reportes de vendors, foros de seguridad, redes sociales. Es el 80% de la inteligencia para una empresa con presupuesto cero.
- **SIGINT/TECHINT (Technical Intelligence).** Telemetría interna: logs del SIEM, alertas del EDR, sandbox de malware, honeypots. Datos que generas tu.
- **HUMINT (Human Intelligence).** Relaciones con otros CERTs, grupos de compartición sectorial (ISACs), contactos en la comunidad de seguridad.
- **Comercial.** Feeds y plataformas de pago: Recorded Future, Mandiant, CrowdStrike Intel. Solo cuando el presupuesto lo permita.

### Fase 3: Procesamiento (Processing)

Los datos en bruto no son útiles directamente. El procesamiento incluye:

- **Normalización.** Convertir datos de múltiples fuentes a un formato común (STIX 2.1 es el estándar).
- **Deduplicación.** Eliminar IOCs duplicados entre fuentes.
- **Enriquecimiento.** Añadir contexto a los IOCs: geolocalización de IPs, resolución DNS histórica, asociación con malware familias, score de confianza.
- **Validación.** Verificar que los IOCs son relevantes (no caducados, no falsos positivos conocidos).

### Fase 4: Análisis (Analysis)

El análisis transforma información procesada en inteligencia accionable. Aquí es donde el analista de CTI aporta valor:

- **Correlación.** Conectar IOCs individuales en campañas coherentes. Esas 15 IPs no son 15 amenazas separadas: son la infraestructura C2 de una campaña de Emotet.
- **Atribución (cuando es posible).** Vincular actividad con actores conocidos. No siempre es posible ni necesario para una empresa.
- **Evaluación de relevancia.** De toda la información disponible, que es relevante para tu organización específica?
- **Recomendaciones.** El producto de inteligencia siempre debe incluir acciones recomendadas. Un informe sin recomendaciones es un paper académico, no inteligencia.

### Fase 5: Diseminación (Dissemination)

La inteligencia que no llega al consumidor adecuado en el momento adecuado no sirve. Los productos de inteligencia típicos son:

- **Tactical.** IOCs para el SOC (diario): IPs, dominios, hashes para reglas de detección.
- **Operational.** Informes de campaña para el equipo de respuesta (semanal): TTPs, infraestructura, kill chain del atacante.
- **Strategic.** Briefings para dirección (trimestral): tendencias de amenaza, evaluación de riesgo, recomendaciones de inversión.

## Fuentes de threat intelligence gratuitas para empresas españolas

El ecosistema de fuentes gratuitas es sorprendentemente completo. Una empresa puede construir un programa CTI funcional sin gastar un euro en licencias de feeds.

### Fuentes institucionales españolas

**CCN-CERT (Centro Criptológico Nacional).** El CERT gubernamental español pública:

- Alertas y avisos sobre amenazas activas contra España.
- La herramienta LUCIA para gestión de incidentes (disponible para administraciones públicas y operadores de servicios esenciales).
- Guías CCN-STIC con configuraciones de seguridad para sistemas.
- El portal REYES (acceso restringido) con IOCs y análisis de malware.

Si tu empresa es operador de servicios esenciales o trabaja con la administración pública, el acceso a CCN-CERT es prioritario.

**INCIBE-CERT.** El CERT de referencia para empresas y ciudadanos. Ofrece:

- Avisos de seguridad y vulnerabilidades.
- Informes mensuales de actividad maliciosa en España.
- El servicio de Alerta Temprana (SAT) para empresas.
- Guías y herramientas gratuitas de ciberseguridad.

### Plataformas de compartición de IOCs

**[AlienVault OTX](https://otx.alienvault.com/) (Open Threat Exchange).** La plataforma de threat intelligence comunitaria más grande del mundo. Permite:

- Buscar IOCs por IP, dominio, hash o CVE.
- Suscribirse a "pulses" (colecciones de IOCs sobre una amenaza específica).
- Crear y compartir tus propios pulses.
- Integración vía API con SIEMs y herramientas de seguridad.
- Es gratuita con registro.

**Abuse.ch.** Proyecto suizo que mantiene varios feeds de IOCs de alta calidad:

- **URLhaus.** URLs de distribución de malware.
- **MalwareBazaar.** Muestras de malware con hashes y metadata.
- **ThreatFox.** IOCs de diversas amenazas con contexto.
- **Feodo Tracker.** Infraestructura C2 de botnets bancarias.

Todos los feeds son gratuitos, actualizados múltiples veces al día y con buena tasa de precisión.

**VirusTotal.** La cuenta gratuita permite:

- Buscar hashes, IPs, dominios y URLs.
- Ver resultados de análisis multi-motor.
- Relaciones entre muestras (grafos de pivoting básico).

La cuenta gratuita tiene limitaciones de API (500 peticiones/día), pero es suficiente para un programa CTI inicial.

### Feeds de vulnerabilidades

- **NVD (National Vulnerability Database).** Base de datos completa de CVEs con scoring CVSS.
- **CISA KEV (Known Exploited Vulnerabilities).** Lista de vulnerabilidades que CISA confirma explotadas activamente. Actualización frecuente. Esencial para priorizar parcheo.
- **Exploit-DB.** Base de datos de exploits públicos vinculados a CVEs.

### Fuentes de inteligencia estratégica

- **ENISA Threat Landscape.** Informe anual de la agencia europea de ciberseguridad. Panorama de amenazas europeo con datos cuantitativos.
- **Reportes de vendors.** CrowdStrike, Mandiant, Palo Alto Unit42, Cisco Talos, ESET, Kaspersky. Publican reportes gratuitos sobre campañas y actores de amenaza. Sesgo hacia sus clientes, pero son información valiosa.
- **Blogs de investigadores.** The DFIR Report (análisis detallados de intrusiones reales), BleepingComputer (noticias), KrebsOnSecurity (investigaciónes).

## Herramientas open source para CTI

Las herramientas son el esqueleto operativo del programa. Estas cuatro cubren las necesidades básicas sin coste de licencia.

### MISP: la plataforma central

[MISP](https://www.misp-project.org/) (Malware Information Sharing Platform) es la herramienta de referencia para gestión de threat intelligence. Desarrollada originalmente por el CERT del ejercito belga (CIRCL), es usada por CERTs nacionales, empresas y organizaciones de todo el mundo.

Funcionalidades clave:

- **Gestión de eventos y atributos.** Cada amenaza se modela como un evento con atributos (IPs, dominios, hashes, emails, etc.) tipados y categorizados.
- **Taxonomías y galaxias.** Sistema de etiquetado estandarizado que incluye MITRE ATT&CK, TLP (Traffic Light Protocol), sectores afectados y tipos de amenaza.
- **Correlación automática.** MISP correlacióna automáticamente atributos entre eventos, revelando conexiones entre campañas aparentemente independientes.
- **Compartición.** Diseñado para compartir inteligencia entre organizaciones de confianza. Soporta comunidades de compartición (sharing groups) con control granular de visibilidad.
- **Integración.** API REST completa. Modulos de exportación a formatos STIX, CSV, IDS (Snort/Suricata), OpenIOC. Integración nativa con SIEMs vía syslog o API.
- **Feeds integrados.** Permite suscribirse a feeds externos (Abuse.ch, CIRCL, AlienVault OTX) directamente desde la interfaz.

Desplegar MISP requiere un servidor Linux (Ubuntu/Debian recomendado). La instalación vía Docker simplifica el proceso:

```bash
# Despliegue básico con Docker
git clone https://github.com/MISP/misp-docker.git
cd misp-docker
cp template.env .env
# Editar .env con la configuración local
docker compose up -d
```

Para una empresa con un equipo de seguridad de 2-5 personas, MISP es la herramienta que más valor aporta por hora invertida.

### OpenCTI: visualización y análisis avanzado

OpenCTI (Open Cyber Threat Intelligence) es una plataforma de gestión de CTI desarrollada por Filigran (empresa francesa). Complementa a MISP con:

- **Knowledge graph.** Visualiza relaciones entre actores, campañas, malware, vulnerabilidades e indicadores en un grafo interactivo.
- **Modelo de datos STIX 2.1 nativo.** Todo se almacena en formato estándar.
- **Conectores.** Más de 100 conectores para importar datos de feeds, CERTs, vendors y otras plataformas (incluido MISP).
- **Dashboards analiticos.** Paneles para monitorizar tendencias, actores activos y actividad por sector.

OpenCTI es más exigente en recursos que MISP (necesita Elasticsearch/OpenSearch, RabbitMQ, Redis y MinIO), pero proporciona capacidades analiticas superiores.

### TheHive: gestión de casos de respuesta

TheHive no es estrictamente una herramienta de CTI, pero se integra con el ecosistema. Es una plataforma de gestión de incidentes que conecta directamente con MISP y Cortex (motor de análisis automatizado). El flujo típico:

1. Un IOC de MISP genera una alerta en TheHive.
2. El analista SOC escala la alerta a caso.
3. Cortex enriquece automáticamente los observables (IPs, dominios, hashes) con múltiples fuentes.
4. El analista documenta la investigación y las acciones de respuesta.

### Yeti: para empezar rápido

Si MISP y OpenCTI te parecen demasiado para empezar, Yeti es una alternativa más ligera. Es una plataforma de CTI minimalista que permite:

- Almacenar indicadores y observables.
- Asociarlos con entidades (actores, campañas, malware).
- Buscar y pivotar entre relaciones.
- Exportar en formatos estándar.

Yeti es ideal para un equipo de 1-2 personas que quiere estructurar su inteligencia antes de invertir en plataformas más complejas.

## Cómo integrar threat intelligence en tu SOC

La inteligencia que no se operacionaliza es información muerta. La integración con el SOC es donde el programa CTI genera retorno real.

### Nivel 1: Feeds de IOCs en el SIEM

El primer paso es alimentar tu SIEM con IOCs de tus fuentes. Esto permite detección automática cuando un IOC aparece en tus logs:

**Integración típica MISP a SIEM:**

```python
# Ejemplo: exportar IOCs de MISP a formato SIEM
# usando PyMISP (cliente Python oficial)

from pymisp import PyMISP

misp = PyMISP('https://misp.internal', 'API_KEY', ssl=False)

# Obtener IOCs de las últimas 24 horas
# con TLP:WHITE o TLP:GREEN (compartibles internamente)
events = misp.search(
    timestamp='1d',
    tags=['tlp:white', 'tlp:green'],
    type_attribute=['ip-dst', 'domain', 'md5', 'sha256'],
    pythonify=True
)

# Formatear para ingesta en SIEM
for event in events:
    for attr in event.attributes:
        print(f"{attr.type},{attr.value},{event.info}")
```

Reglas prácticas para la ingesta de IOCs:

- **TTL (Time to Live).** Los IOCs tienen fecha de caducidad. Una IP de C2 activa hoy puede ser reasignada a un uso legítimo en 30 días. Configura TTL de 30 días para IPs, 90 días para dominios y 180 días para hashes.
- **Nivel de confianza.** No todos los IOCs tienen la misma fiabilidad. MISP permite asignar niveles de confianza. Solo automatiza bloqueos con IOCs de confianza alta.
- **Contexto.** Un IOC sin contexto genera alertas que el analista no puede investigar eficientemente. Incluye siempre la referencia al evento/campaña de origen.

### Nivel 2: Reglas de detección basadas en TTPs

Los IOCs son útiles pero efimeros. Los atacantes cambian de infraestructura constantemente. Las detecciónes basadas en TTPs (tácticas, técnicas y procedimientos) son más duraderas porque detectan el comportamiento, no el indicador.

Ejemplo: en lugar de bloquear las 50 IPs de la infraestructura C2 de Emotet (que cambian cada semana), detecta el patrón de comportamiento de Emotet:

- Documento Office con macro que ejecuta PowerShell.
- PowerShell descarga un payload de una URL con patrón `/wp-content/` o `/wp-admin/`.
- El payload se escribe en `%APPDATA%` o `%TEMP%`.
- El proceso se comunica periódicamente (beaconing) con intervalos regulares.

Esa detección basada en comportamiento funciona independientemente de que IPs o dominios use el atacante esta semana.

### Nivel 3: Enriquecimiento automático de alertas

Cuando el SOC recibe una alerta, el analista necesita contexto para decidir si es un verdadero positivo. El enriquecimiento automático con CTI reduce drasticamente el tiempo de triaje:

1. **Alerta del SIEM.** "Conexión saliente a IP 185.220.101.42 desde servidor de contabilidad."
2. **Enriquecimiento automático.** La IP está en MISP como C2 de Emotet (confianza alta, reportado hace 2 días por Abuse.ch). Asociada a táctica T1071.001 (Application Layer Protocol: Web Protocols).
3. **Decisión del analista.** Con ese contexto, el analista escala inmediatamente en lugar de perder 30 minutos investigando la IP manualmente.

Herramientas como Cortex (asociado a TheHive) o los módulos de enriquecimiento de MISP automatizan este proceso.

### Nivel 4: Threat hunting proactivo

La inteligencia alimenta las hipótesis de threat hunting. El proceso:

1. El equipo de CTI pública un informe: "APT28 está usando la técnica T1218.011 (Signed Binary Proxy Execution: Rundll32) para evadir detecciónes en campañas contra gobierno europeo."
2. El threat hunter fórmula la hipótesis: "Es posible que APT28 haya comprometido nuestro entorno usando rundll32 para ejecutar DLLs maliciosas."
3. El hunter busca en la telemetría histórica: ejecuciones de rundll32 con argumentos inusuales, rundll32 cargando DLLs desde ubicaciones temporales, rundll32 estableciendo conexiones de red.
4. Si encuentra actividad sospechosa, escala. Si no, documenta la búsqueda y la convierte en una regla de detección permanente.

{{< cta type="tofu" text="Riskitera integra threat intelligence con detección y respuesta automatizada. IA soberana que operacionaliza tu inteligencia sin que los datos salgan de tu infraestructura." label="Ver demo CTI" >}}

## Cómo construir tu programa de CTI desde cero: plan de 90 días

Si empiezas sin nada, este es un roadmap realista para 90 días con un equipo de 1-2 personas dedicando parcialmente su tiempo.

### Días 1-30: Fundamentos

**Semana 1-2: Requisitos y fuentes.**

- Reúne a los stakeholders (CISO, SOC lead, IT manager) y documenta 5-8 Intelligence Requirements.
- Registrate en AlienVault OTX, Abuse.ch y VirusTotal. Configura alertas email.
- Suscríbete a las listas de CCN-CERT e INCIBE-CERT.

**Semana 3-4: Primera herramienta.**

- Despliega MISP en un servidor interno (puede ser una VM con 4 CPU, 8 GB RAM, 100 GB disco).
- Configura los feeds integrados: CIRCL OSINT Feed, Abuse.ch URLhaus y MalwareBazaar, Botvrij.eu.
- Habilita la sincronización automática de feeds (cada 6 horas es suficiente para empezar).

### Días 31-60: Integración

**Semana 5-6: Conexión con el SIEM.**

- Configura la exportación de IOCs desde MISP al SIEM (vía API, syslog o ficheros CSV programados).
- Crea las reglas de correlación básicas: "match" de IOCs de MISP contra logs de DNS, proxy y firewall.
- Ajusta TTL y niveles de confianza para minimizar falsos positivos.

**Semana 7-8: Primer producto de inteligencia.**

- Escribe tu primer informe semanal de CTI. Formato sugerido:
  - Resumen ejecutivo (3-5 líneas).
  - Amenazas activas relevantes para la organización.
  - IOCs nuevos incorporados al SIEM.
  - Recomendaciones de acción.
- Distribuye a los stakeholders definidos en los Intelligence Requirements.

### Días 61-90: Maduración

**Semana 9-10: Enriquecimiento y automatización.**

- Configura Cortex o los módulos de enriquecimiento de MISP para automatizar el contexto de IOCs.
- Implementa un workflow: alerta SIEM con match de IOC -> enriquecimiento automático -> ticket con contexto al analista.

**Semana 11-12: Revisión y ajuste.**

- Revisa los Intelligence Requirements con los stakeholders. Han cambiado las necesidades?
- Evalua la calidad de los feeds: cuales generan más verdaderos positivos? Cuáles solo ruido?
- Documenta el proceso y crea un runbook para el analista de CTI.

Al final de los 90 días tendras: un MISP operativo con feeds automatizados, integración básica con el SIEM, un producto de inteligencia semanal y un proceso documentado. No es un programa de CTI maduro, pero es funcional y genera valor desde el primer mes.

## Errores comunes al empezar con threat intelligence

Estos errores los cometemos casi todos al principio. Reconocerlos te ahorra meses de esfuerzo mal dirigido.

### Error 1: Confundir feeds de IOCs con threat intelligence

Suscribirse a 20 feeds de IOCs y volcarlos en el SIEM no es threat intelligence. Es datos sin procesar generando alertas. La inteligencia requiere análisis, contexto y relevancia para tu organización. Un analista que recibe 500 alertas diarias de "match de IOC" sin contexto abandona el programa en dos semanas.

**Solución.** Menos feeds, mejor curados. Empieza con 3-4 fuentes de alta calidad (Abuse.ch, AlienVault OTX, CIRCL) y añade contexto a cada IOC antes de ingesta.

### Error 2: No definir requisitos de inteligencia

Sin requisitos claros, el programa CTI se convierte en "recopilar todo lo interesante". El resultado es un MISP con 500.000 atributos que nadie consulta y un analista de CTI que no sabe si esta aportando valor.

**Solución.** Dedica la primera semana exclusivamente a definir IRs con los stakeholders. Revisalos trimestralmente.

### Error 3: No operacionalizar la inteligencia

El informe de CTI más brillante no sirve de nada si no se traduce en acciones: reglas en el SIEM, bloqueos en el firewall, priorización de parcheo, formación a usuarios. La inteligencia que se queda en un PDF compartido por email y que nadie lee es desperdicio.

**Solución.** Cada producto de inteligencia debe incluir acciones concretas y un responsable asignado. Mide la tasa de acciones implementadas.

### Error 4: Querer cubrir todo desde el primer día

Intentar monitorizar la dark web, analizar malware en sandbox, hacer atribución de APTs y mantener una plataforma de compartición con 15 organizaciones... con una persona y medio día a la semana.

**Solución.** El plan de 90 días anterior es realista. Empieza con feeds básicos, un MISP y un informe semanal. Crece cuando demuestres valor.

### Error 5: No medir el impacto del programa

Si no puedes demostrar que el programa CTI aporta valor, será el primero en perder presupuesto (o tiempo de personal). Las métricas mínimas:

- Número de IOCs que generaron verdaderos positivos en el SIEM.
- Tiempo medio de detección antes y después del programa CTI.
- Número de acciones preventivas implementadas gracias a inteligencia (parches priorizados, reglas creadas, bloqueos aplicados).
- Feedback cualitativo de los stakeholders.

## Cuándo invertir en threat intelligence de pago

La pregunta no es "debería pagar por CTI?" sino "en que momento mi programa necesita fuentes comerciales?"

### Señales de que necesitas fuentes comerciales

- **Los feeds gratuitos ya no cubren tus requisitos.** Necesitas inteligencia específica de tu sector (financiero, energético, sanitario) que no está disponible en fuentes públicas.
- **Necesitas atribución y análisis de actores.** Los feeds gratuitos proporcionan IOCs. Los servicios comerciales (Recorded Future, Mandiant, CrowdStrike) proporcionan análisis de actores, campañas y predicciones.
- **Tu equipo no tiene capacidad de análisis.** Si solo puedes consumir inteligencia ya procesada, un servicio comercial que entregue reportes listos para consumir puede tener sentido.
- **Necesitas monitorizar la dark web.** La monitorización de foros, mercados y canales de Telegram donde se venden credenciales o se planifican ataques requiere herramientas especializadas (y precauciones legales).
- **Compliance o regulación lo exige.** Sectores regulados (banca, infraestructuras críticas) pueden tener requisitos de compartición o consumo de inteligencia que las fuentes gratuitas no satisfacen documentalmente.

### Qué evaluar en un proveedor comercial

Si decides invertir, evalúa:

- **Relevancia geográfica.** El proveedor tiene cobertura de amenazas en España y Europa? Un proveedor enfocado en amenazas de Asia-Pacifico no te aporta tanto.
- **Formatos de entrega.** Soporta STIX 2.1? Tiene API? Se integra con tu SIEM y tu MISP? Si los datos llegan en PDF y hay que copiar IOCs a mano, el valor cae drasticamente.
- **Frescura.** Cual es la latencia entre la detección de una amenaza y la publicación del IOC o el reporte? En threat intelligence tactica, horas importan.
- **Accionabilidad.** Los productos incluyen recomendaciones concretas o solo descripciones?

### Opciones intermedias

Antes de contratar un servicio premium (que puede costar desde 15.000 EUR/año hasta cifras de seis dígitos), considera opciones intermedias:

- **ISACs sectoriales.** Los centros de compartición sectorial (financiero, energético, sanitario) proporcionan inteligencia relevante y específica. En España, el CCN coordina algunos de estos grupos.
- **FIRST y TF-CSIRT.** Comunidades de CERTs donde se comparte inteligencia entre miembros.
- **Programas de compartición de vendors.** Cisco Talos, Microsoft MSTIC y otros publican inteligencia de alta calidad gratuitamente.

## El modelo de madurez CTI: donde estas y donde quieres llegar

Para medir la evolución de tu programa, usa este modelo simplificado de cinco niveles:

| Nivel | Nombre | Descripción |
|---|---|---|
| 0 | Inexistente | No hay actividad de CTI |
| 1 | Reactivo | Se consultan fuentes ad-hoc cuando ocurre un incidente |
| 2 | Básico | Feeds de IOCs integrados en SIEM, informe periódico |
| 3 | Funcional | MISP operativo, requisitos definidos, integración con SOC, hunting basado en CTI |
| 4 | Avanzado | Análisis propio de campañas, compartición con comunidad, métricas de impacto |
| 5 | Optimizado | CTI integrada en todas las decisiones de seguridad, automatización end-to-end, predicción |

La mayoría de empresas españolas están en nivel 0 o 1. Llegar a nivel 2-3 en 6 meses es un objetivo realista y suficiente para generar valor tangible.

{{< cta type="bofu" text="Solicita una demo personalizada y descubre cómo Riskitera integra threat intelligence, detección automatizada y respuesta con IA soberana, sin que tus datos salgan de España." label="Solicitar demo" >}}


**Artículos relacionados:**
- [Iocs En Ciberseguridad Que Son](/es/posts/2026/04/iocs-en-ciberseguridad-que-son/)
- [Threat Hunting Guía Practica](/es/posts/2026/04/threat-hunting-guia-practica/)

## Preguntas frecuentes

### Cuantas personas necesito para un programa de CTI básico?

Una persona dedicando el 50% de su tiempo puede mantener un programa de nivel 2 (feeds integrados, informe semanal). Para nivel 3 (MISP operativo, hunting basado en CTI, análisis propio), necesitas al menos una persona a tiempo completo. En muchas PYMES españolas, el rol de CTI lo asume un analista SOC senior como función complementaria. Lo importante no es el número de personas sino la constancia: 4 horas a la semana de CTI consistente aportan más valor que 40 horas puntuales una vez al trimestre.

### Es legal monitorizar la dark web para obtener threat intelligence?

La observación pasiva de foros y mercados dark web accesibles (sin registrarse ni interactuar) es generalmente legal en España. Sin embargo, hay líneas que no debes cruzar: comprar credenciales robadas (aunque sean de tu propia empresa), interactuar con actores de amenaza haciéndote pasar por comprador, o acceder a sistemas cerrados sin autorización. La recomendación es limitar la monitorización dark web a servicios especializados que operan dentro del marco legal y dejar la investigación activa a las FCSE (Fuerzas y Cuerpos de Seguridad del Estado).

### Cómo priorizo entre tantas fuentes de IOCs gratuitas?

Empieza por calidad, no por cantidad. Tres fuentes bien integradas aportan más que quince mal gestionadas. Para una empresa española, la combinación recomendada es: (1) Abuse.ch (URLhaus + MalwareBazaar + ThreatFox) por su alta calidad y frescura; (2) AlienVault OTX por su amplitud y facilidad de integración; (3) CCN-CERT/INCIBE-CERT por su relevancia geográfica. Anade más fuentes solo cuando hayas validado que las primeras generan verdaderos positivos en tu entorno y no saturan al equipo.

### Qué diferencia hay entre MISP y OpenCTI? Cuál debería usar?

MISP es mejor para la gestión operativa de IOCs: recopilar, normalizar, compartir y exportar indicadores al SIEM. OpenCTI es mejor para análisis y visualización: grafos de relaciones, dashboards y modelado de actores de amenaza. Para empezar, MISP es la opción recomendada porque es más ligero, tiene más documentación y cubre el caso de uso más básico (feeds a SIEM). Cuando tu programa madure al nivel 3-4 y necesites capacidades analiticas avanzadas, añade OpenCTI como capa de análisis encima de MISP (ambos se integran nativamente).

### Cómo justificó el tiempo invertido en CTI ante dirección?

El argumento más efectivo son las acciones preventivas documentadas. Lleva un registro de cada vez que la inteligencia genero una acción: "El 15 de marzo, un IOC de MISP detecto una conexión a infraestructura C2 de Emotet desde un puesto de contabilidad. Se aisle el equipo en 4 minutos y se evite la propagación." Ese tipo de ejemplos concretos, con impacto estimado (coste medio de un incidente de ransomware en España según INCIBE: entre 100.000 y 2M EUR para PYMES), son mucho más convincentes que métricas abstractas como "número de IOCs procesados".
