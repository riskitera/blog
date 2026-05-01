---
title: "Threat Intelligence para empresas espanolas: como empezar sin presupuesto"
description: "Guia practica para que empresas espanolas comiencen con threat intelligence sin presupuesto: fuentes gratuitas, herramientas open source, integracion con el SOC y maduracion del programa."
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

Guia practica para que empresas espanolas comiencen con threat intelligence sin presupuesto: fuentes gratuitas, herramientas open source, integracion con el SOC y maduracion del programa.

<!--more-->

{{< key-takeaways >}}
- La threat intelligence no requiere presupuesto inicial: las fuentes publicas espanolas (CCN-CERT, INCIBE-CERT) y las plataformas gratuitas (AlienVault OTX, Abuse.ch) cubren el 80% de las necesidades de una PYME.
- Un programa de CTI efectivo sigue el ciclo de inteligencia: requisitos de los stakeholders, recoleccion, procesamiento, analisis y diseminacion.
- MISP open source permite gestionar, correlacionar y compartir indicadores de compromiso sin coste de licencia, integrando con cualquier SIEM.
- El error mas comun es confundir feeds de IOCs con threat intelligence. Los indicadores sin contexto son datos, no inteligencia.
- La operacionalizacion de la inteligencia (convertirla en reglas SIEM, politicas de bloqueo y decisiones de negocio) es lo que diferencia un programa funcional de uno decorativo.
{{< /key-takeaways >}}

## Que es la threat intelligence y por que la necesita tu empresa

La Threat Intelligence (CTI, Cyber Threat Intelligence) es el proceso de recopilar, procesar y analizar informacion sobre amenazas ciberneticas para tomar decisiones informadas. No es una herramienta ni un producto. Es una funcion que transforma datos en bruto (IPs maliciosas, hashes de malware, reportes de vulnerabilidades) en conocimiento accionable para proteger tu organizacion.

La distincion clave es entre **datos**, **informacion** e **inteligencia**:

- **Dato.** Una IP aparece en una lista de comando y control: `185.220.101.42`.
- **Informacion.** Esa IP esta asociada al malware Emotet y se usa como servidor C2 desde hace 3 dias.
- **Inteligencia.** Emotet esta distribuyendo phishing masivo contra el sector financiero espanol esta semana, usando adjuntos de Excel con macros. Tu empresa es del sector financiero, tus usuarios usan Excel y no tienes bloqueadas las macros en adjuntos externos. Accion recomendada: bloquear macros en documentos de origen externo y anadir la IP al blocklist del firewall.

### Por que las empresas espanolas la necesitan especialmente

Espana ocupa posiciones destacadas en los rankings europeos de ciberataques recibidos. Segun los datos del [CCN-CERT](https://www.ccn-cert.cni.es/), el organismo de respuesta a incidentes del Centro Criptologico Nacional, los incidentes gestionados han crecido un 25% interanual de media en los ultimos cinco anos. [INCIBE-CERT](https://www.incibe.es/incibe-cert), el CERT de referencia para empresas y ciudadanos, gestion mas de 118.000 incidentes en su ultimo informe anual.

Las empresas espanolas enfrentan amenazas especificas:

- **Ransomware dirigido.** Grupos como Lockbit y Cl0p han atacado activamente a empresas espanolas de infraestructura, sanidad y administracion publica.
- **Phishing localizado.** Campanas en espanol que suplantan a Correos, la Agencia Tributaria, bancos locales (CaixaBank, BBVA, Santander) y la Seguridad Social.
- **Ciberespionaje.** Actores estatales con interes en sectores estrategicos espanoles: defensa, energia, telecomunicaciones y diplomacia.
- **Fraude al CEO (BEC).** Especialmente dirigido a PYMES con procesos de pago poco formalizados.

Un programa de threat intelligence, incluso basico, permite a tu empresa pasar de una postura reactiva ("nos han atacado, que hacemos") a una proactiva ("sabemos que este tipo de ataque esta activo contra nuestro sector, ya hemos implementado las contramedidas").

## El ciclo de inteligencia: estructura de un programa CTI

La threat intelligence no es suscribirse a feeds y olvidarse. Es un proceso ciclico con fases bien definidas. El modelo clasico de inteligencia (usado por agencias de inteligencia y adaptado a ciberseguridad) tiene cinco fases:

### Fase 1: Requisitos de inteligencia (Planning and Direction)

Antes de recopilar nada, necesitas saber que informacion necesita tu organizacion. Los requisitos vienen de los stakeholders:

- **CISO / Responsable de seguridad.** "Necesito saber que actores de amenaza estan atacando nuestro sector en Espana y que tecnicas usan."
- **Equipo SOC.** "Necesito IOCs frescos para alimentar las reglas del SIEM y el EDR."
- **Equipo de IT.** "Necesito saber que vulnerabilidades estan siendo explotadas activamente para priorizar el parcheo."
- **Direccion general.** "Necesito entender el nivel de riesgo ciber de la empresa en terminos de negocio."

Los requisitos se formalizan como **Intelligence Requirements (IRs)**. Ejemplo:

| ID | Requisito | Stakeholder | Frecuencia |
|---|---|---|---|
| IR-01 | Actores de amenaza activos contra sector financiero en Espana | CISO | Mensual |
| IR-02 | IOCs asociados a campanas de phishing en espanol | SOC | Diaria |
| IR-03 | Vulnerabilidades criticas explotadas in-the-wild en software de nuestro stack | IT | Semanal |
| IR-04 | Tendencias de riesgo ciber para informe trimestral a comite | Direccion | Trimestral |

Sin requisitos claros, el programa de CTI se convierte en una actividad de "recopilar todo" que no aporta valor a nadie.

### Fase 2: Recoleccion (Collection)

Con los requisitos definidos, sabes que buscar. Las fuentes de recoleccion se clasifican en:

- **OSINT (Open Source Intelligence).** Fuentes publicas: feeds de IOCs, blogs de investigadores, reportes de vendors, foros de seguridad, redes sociales. Es el 80% de la inteligencia para una empresa con presupuesto cero.
- **SIGINT/TECHINT (Technical Intelligence).** Telemetria interna: logs del SIEM, alertas del EDR, sandbox de malware, honeypots. Datos que generas tu.
- **HUMINT (Human Intelligence).** Relaciones con otros CERTs, grupos de comparticion sectorial (ISACs), contactos en la comunidad de seguridad.
- **Comercial.** Feeds y plataformas de pago: Recorded Future, Mandiant, CrowdStrike Intel. Solo cuando el presupuesto lo permita.

### Fase 3: Procesamiento (Processing)

Los datos en bruto no son utiles directamente. El procesamiento incluye:

- **Normalizacion.** Convertir datos de multiples fuentes a un formato comun (STIX 2.1 es el estandar).
- **Deduplicacion.** Eliminar IOCs duplicados entre fuentes.
- **Enriquecimiento.** Anadir contexto a los IOCs: geolocalizacion de IPs, resolucion DNS historica, asociacion con malware familias, score de confianza.
- **Validacion.** Verificar que los IOCs son relevantes (no caducados, no falsos positivos conocidos).

### Fase 4: Analisis (Analysis)

El analisis transforma informacion procesada en inteligencia accionable. Aqui es donde el analista de CTI aporta valor:

- **Correlacion.** Conectar IOCs individuales en campanas coherentes. Esas 15 IPs no son 15 amenazas separadas: son la infraestructura C2 de una campana de Emotet.
- **Atribucion (cuando es posible).** Vincular actividad con actores conocidos. No siempre es posible ni necesario para una empresa.
- **Evaluacion de relevancia.** De toda la informacion disponible, que es relevante para tu organizacion especifica?
- **Recomendaciones.** El producto de inteligencia siempre debe incluir acciones recomendadas. Un informe sin recomendaciones es un paper academico, no inteligencia.

### Fase 5: Diseminacion (Dissemination)

La inteligencia que no llega al consumidor adecuado en el momento adecuado no sirve. Los productos de inteligencia tipicos son:

- **Tactical.** IOCs para el SOC (diario): IPs, dominios, hashes para reglas de deteccion.
- **Operational.** Informes de campana para el equipo de respuesta (semanal): TTPs, infraestructura, kill chain del atacante.
- **Strategic.** Briefings para direccion (trimestral): tendencias de amenaza, evaluacion de riesgo, recomendaciones de inversion.

## Fuentes de threat intelligence gratuitas para empresas espanolas

El ecosistema de fuentes gratuitas es sorprendentemente completo. Una empresa puede construir un programa CTI funcional sin gastar un euro en licencias de feeds.

### Fuentes institucionales espanolas

**CCN-CERT (Centro Criptologico Nacional).** El CERT gubernamental espanol publica:

- Alertas y avisos sobre amenazas activas contra Espana.
- La herramienta LUCIA para gestion de incidentes (disponible para administraciones publicas y operadores de servicios esenciales).
- Guias CCN-STIC con configuraciones de seguridad para sistemas.
- El portal REYES (acceso restringido) con IOCs y analisis de malware.

Si tu empresa es operador de servicios esenciales o trabaja con la administracion publica, el acceso a CCN-CERT es prioritario.

**INCIBE-CERT.** El CERT de referencia para empresas y ciudadanos. Ofrece:

- Avisos de seguridad y vulnerabilidades.
- Informes mensuales de actividad maliciosa en Espana.
- El servicio de Alerta Temprana (SAT) para empresas.
- Guias y herramientas gratuitas de ciberseguridad.

### Plataformas de comparticion de IOCs

**[AlienVault OTX](https://otx.alienvault.com/) (Open Threat Exchange).** La plataforma de threat intelligence comunitaria mas grande del mundo. Permite:

- Buscar IOCs por IP, dominio, hash o CVE.
- Suscribirse a "pulses" (colecciones de IOCs sobre una amenaza especifica).
- Crear y compartir tus propios pulses.
- Integracion via API con SIEMs y herramientas de seguridad.
- Es gratuita con registro.

**Abuse.ch.** Proyecto suizo que mantiene varios feeds de IOCs de alta calidad:

- **URLhaus.** URLs de distribucion de malware.
- **MalwareBazaar.** Muestras de malware con hashes y metadata.
- **ThreatFox.** IOCs de diversas amenazas con contexto.
- **Feodo Tracker.** Infraestructura C2 de botnets bancarias.

Todos los feeds son gratuitos, actualizados multiples veces al dia y con buena tasa de precision.

**VirusTotal.** La cuenta gratuita permite:

- Buscar hashes, IPs, dominios y URLs.
- Ver resultados de analisis multi-motor.
- Relaciones entre muestras (grafos de pivoting basico).

La cuenta gratuita tiene limitaciones de API (500 peticiones/dia), pero es suficiente para un programa CTI inicial.

### Feeds de vulnerabilidades

- **NVD (National Vulnerability Database).** Base de datos completa de CVEs con scoring CVSS.
- **CISA KEV (Known Exploited Vulnerabilities).** Lista de vulnerabilidades que CISA confirma explotadas activamente. Actualizacion frecuente. Esencial para priorizar parcheo.
- **Exploit-DB.** Base de datos de exploits publicos vinculados a CVEs.

### Fuentes de inteligencia estrategica

- **ENISA Threat Landscape.** Informe anual de la agencia europea de ciberseguridad. Panorama de amenazas europeo con datos cuantitativos.
- **Reportes de vendors.** CrowdStrike, Mandiant, Palo Alto Unit42, Cisco Talos, ESET, Kaspersky. Publican reportes gratuitos sobre campanas y actores de amenaza. Sesgo hacia sus clientes, pero son informacion valiosa.
- **Blogs de investigadores.** The DFIR Report (analisis detallados de intrusiones reales), BleepingComputer (noticias), KrebsOnSecurity (investigaciones).

## Herramientas open source para CTI

Las herramientas son el esqueleto operativo del programa. Estas cuatro cubren las necesidades basicas sin coste de licencia.

### MISP: la plataforma central

[MISP](https://www.misp-project.org/) (Malware Information Sharing Platform) es la herramienta de referencia para gestion de threat intelligence. Desarrollada originalmente por el CERT del ejercito belga (CIRCL), es usada por CERTs nacionales, empresas y organizaciones de todo el mundo.

Funcionalidades clave:

- **Gestion de eventos y atributos.** Cada amenaza se modela como un evento con atributos (IPs, dominios, hashes, emails, etc.) tipados y categorizados.
- **Taxonomias y galaxias.** Sistema de etiquetado estandarizado que incluye MITRE ATT&CK, TLP (Traffic Light Protocol), sectores afectados y tipos de amenaza.
- **Correlacion automatica.** MISP correlaciona automaticamente atributos entre eventos, revelando conexiones entre campanas aparentemente independientes.
- **Comparticion.** Diseñado para compartir inteligencia entre organizaciones de confianza. Soporta comunidades de comparticion (sharing groups) con control granular de visibilidad.
- **Integracion.** API REST completa. Modulos de exportacion a formatos STIX, CSV, IDS (Snort/Suricata), OpenIOC. Integracion nativa con SIEMs via syslog o API.
- **Feeds integrados.** Permite suscribirse a feeds externos (Abuse.ch, CIRCL, AlienVault OTX) directamente desde la interfaz.

Desplegar MISP requiere un servidor Linux (Ubuntu/Debian recomendado). La instalacion via Docker simplifica el proceso:

```bash
# Despliegue basico con Docker
git clone https://github.com/MISP/misp-docker.git
cd misp-docker
cp template.env .env
# Editar .env con la configuracion local
docker compose up -d
```

Para una empresa con un equipo de seguridad de 2-5 personas, MISP es la herramienta que mas valor aporta por hora invertida.

### OpenCTI: visualizacion y analisis avanzado

OpenCTI (Open Cyber Threat Intelligence) es una plataforma de gestion de CTI desarrollada por Filigran (empresa francesa). Complementa a MISP con:

- **Knowledge graph.** Visualiza relaciones entre actores, campanas, malware, vulnerabilidades e indicadores en un grafo interactivo.
- **Modelo de datos STIX 2.1 nativo.** Todo se almacena en formato estandar.
- **Conectores.** Mas de 100 conectores para importar datos de feeds, CERTs, vendors y otras plataformas (incluido MISP).
- **Dashboards analiticos.** Paneles para monitorizar tendencias, actores activos y actividad por sector.

OpenCTI es mas exigente en recursos que MISP (necesita Elasticsearch/OpenSearch, RabbitMQ, Redis y MinIO), pero proporciona capacidades analiticas superiores.

### TheHive: gestion de casos de respuesta

TheHive no es estrictamente una herramienta de CTI, pero se integra con el ecosistema. Es una plataforma de gestion de incidentes que conecta directamente con MISP y Cortex (motor de analisis automatizado). El flujo tipico:

1. Un IOC de MISP genera una alerta en TheHive.
2. El analista SOC escala la alerta a caso.
3. Cortex enriquece automaticamente los observables (IPs, dominios, hashes) con multiples fuentes.
4. El analista documenta la investigacion y las acciones de respuesta.

### Yeti: para empezar rapido

Si MISP y OpenCTI te parecen demasiado para empezar, Yeti es una alternativa mas ligera. Es una plataforma de CTI minimalista que permite:

- Almacenar indicadores y observables.
- Asociarlos con entidades (actores, campanas, malware).
- Buscar y pivotar entre relaciones.
- Exportar en formatos estandar.

Yeti es ideal para un equipo de 1-2 personas que quiere estructurar su inteligencia antes de invertir en plataformas mas complejas.

## Como integrar threat intelligence en tu SOC

La inteligencia que no se operacionaliza es informacion muerta. La integracion con el SOC es donde el programa CTI genera retorno real.

### Nivel 1: Feeds de IOCs en el SIEM

El primer paso es alimentar tu SIEM con IOCs de tus fuentes. Esto permite deteccion automatica cuando un IOC aparece en tus logs:

**Integracion tipica MISP a SIEM:**

```python
# Ejemplo: exportar IOCs de MISP a formato SIEM
# usando PyMISP (cliente Python oficial)

from pymisp import PyMISP

misp = PyMISP('https://misp.internal', 'API_KEY', ssl=False)

# Obtener IOCs de las ultimas 24 horas
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

Reglas practicas para la ingesta de IOCs:

- **TTL (Time to Live).** Los IOCs tienen fecha de caducidad. Una IP de C2 activa hoy puede ser reasignada a un uso legitimo en 30 dias. Configura TTL de 30 dias para IPs, 90 dias para dominios y 180 dias para hashes.
- **Nivel de confianza.** No todos los IOCs tienen la misma fiabilidad. MISP permite asignar niveles de confianza. Solo automatiza bloqueos con IOCs de confianza alta.
- **Contexto.** Un IOC sin contexto genera alertas que el analista no puede investigar eficientemente. Incluye siempre la referencia al evento/campana de origen.

### Nivel 2: Reglas de deteccion basadas en TTPs

Los IOCs son utiles pero efimeros. Los atacantes cambian de infraestructura constantemente. Las detecciones basadas en TTPs (tacticas, tecnicas y procedimientos) son mas duraderas porque detectan el comportamiento, no el indicador.

Ejemplo: en lugar de bloquear las 50 IPs de la infraestructura C2 de Emotet (que cambian cada semana), detecta el patron de comportamiento de Emotet:

- Documento Office con macro que ejecuta PowerShell.
- PowerShell descarga un payload de una URL con patron `/wp-content/` o `/wp-admin/`.
- El payload se escribe en `%APPDATA%` o `%TEMP%`.
- El proceso se comunica periodicamente (beaconing) con intervalos regulares.

Esa deteccion basada en comportamiento funciona independientemente de que IPs o dominios use el atacante esta semana.

### Nivel 3: Enriquecimiento automatico de alertas

Cuando el SOC recibe una alerta, el analista necesita contexto para decidir si es un verdadero positivo. El enriquecimiento automatico con CTI reduce drasticamente el tiempo de triaje:

1. **Alerta del SIEM.** "Conexion saliente a IP 185.220.101.42 desde servidor de contabilidad."
2. **Enriquecimiento automatico.** La IP esta en MISP como C2 de Emotet (confianza alta, reportado hace 2 dias por Abuse.ch). Asociada a tactica T1071.001 (Application Layer Protocol: Web Protocols).
3. **Decision del analista.** Con ese contexto, el analista escala inmediatamente en lugar de perder 30 minutos investigando la IP manualmente.

Herramientas como Cortex (asociado a TheHive) o los modulos de enriquecimiento de MISP automatizan este proceso.

### Nivel 4: Threat hunting proactivo

La inteligencia alimenta las hipotesis de threat hunting. El proceso:

1. El equipo de CTI publica un informe: "APT28 esta usando la tecnica T1218.011 (Signed Binary Proxy Execution: Rundll32) para evadir detecciones en campanas contra gobierno europeo."
2. El threat hunter formula la hipotesis: "Es posible que APT28 haya comprometido nuestro entorno usando rundll32 para ejecutar DLLs maliciosas."
3. El hunter busca en la telemetria historica: ejecuciones de rundll32 con argumentos inusuales, rundll32 cargando DLLs desde ubicaciones temporales, rundll32 estableciendo conexiones de red.
4. Si encuentra actividad sospechosa, escala. Si no, documenta la busqueda y la convierte en una regla de deteccion permanente.

{{< cta type="tofu" text="Riskitera integra threat intelligence con deteccion y respuesta automatizada. IA soberana que operacionaliza tu inteligencia sin que los datos salgan de tu infraestructura." label="Ver demo CTI" >}}

## Como construir tu programa de CTI desde cero: plan de 90 dias

Si empiezas sin nada, este es un roadmap realista para 90 dias con un equipo de 1-2 personas dedicando parcialmente su tiempo.

### Dias 1-30: Fundamentos

**Semana 1-2: Requisitos y fuentes.**

- Reune a los stakeholders (CISO, SOC lead, IT manager) y documenta 5-8 Intelligence Requirements.
- Registrate en AlienVault OTX, Abuse.ch y VirusTotal. Configura alertas email.
- Suscribete a las listas de CCN-CERT e INCIBE-CERT.

**Semana 3-4: Primera herramienta.**

- Despliega MISP en un servidor interno (puede ser una VM con 4 CPU, 8 GB RAM, 100 GB disco).
- Configura los feeds integrados: CIRCL OSINT Feed, Abuse.ch URLhaus y MalwareBazaar, Botvrij.eu.
- Habilita la sincronizacion automatica de feeds (cada 6 horas es suficiente para empezar).

### Dias 31-60: Integracion

**Semana 5-6: Conexion con el SIEM.**

- Configura la exportacion de IOCs desde MISP al SIEM (via API, syslog o ficheros CSV programados).
- Crea las reglas de correlacion basicas: "match" de IOCs de MISP contra logs de DNS, proxy y firewall.
- Ajusta TTL y niveles de confianza para minimizar falsos positivos.

**Semana 7-8: Primer producto de inteligencia.**

- Escribe tu primer informe semanal de CTI. Formato sugerido:
  - Resumen ejecutivo (3-5 lineas).
  - Amenazas activas relevantes para la organizacion.
  - IOCs nuevos incorporados al SIEM.
  - Recomendaciones de accion.
- Distribuye a los stakeholders definidos en los Intelligence Requirements.

### Dias 61-90: Maduracion

**Semana 9-10: Enriquecimiento y automatizacion.**

- Configura Cortex o los modulos de enriquecimiento de MISP para automatizar el contexto de IOCs.
- Implementa un workflow: alerta SIEM con match de IOC -> enriquecimiento automatico -> ticket con contexto al analista.

**Semana 11-12: Revision y ajuste.**

- Revisa los Intelligence Requirements con los stakeholders. Han cambiado las necesidades?
- Evalua la calidad de los feeds: cuales generan mas verdaderos positivos? Cuales solo ruido?
- Documenta el proceso y crea un runbook para el analista de CTI.

Al final de los 90 dias tendras: un MISP operativo con feeds automatizados, integracion basica con el SIEM, un producto de inteligencia semanal y un proceso documentado. No es un programa de CTI maduro, pero es funcional y genera valor desde el primer mes.

## Errores comunes al empezar con threat intelligence

Estos errores los cometemos casi todos al principio. Reconocerlos te ahorra meses de esfuerzo mal dirigido.

### Error 1: Confundir feeds de IOCs con threat intelligence

Suscribirse a 20 feeds de IOCs y volcarlos en el SIEM no es threat intelligence. Es datos sin procesar generando alertas. La inteligencia requiere analisis, contexto y relevancia para tu organizacion. Un analista que recibe 500 alertas diarias de "match de IOC" sin contexto abandona el programa en dos semanas.

**Solucion.** Menos feeds, mejor curados. Empieza con 3-4 fuentes de alta calidad (Abuse.ch, AlienVault OTX, CIRCL) y anade contexto a cada IOC antes de ingesta.

### Error 2: No definir requisitos de inteligencia

Sin requisitos claros, el programa CTI se convierte en "recopilar todo lo interesante". El resultado es un MISP con 500.000 atributos que nadie consulta y un analista de CTI que no sabe si esta aportando valor.

**Solucion.** Dedica la primera semana exclusivamente a definir IRs con los stakeholders. Revisalos trimestralmente.

### Error 3: No operacionalizar la inteligencia

El informe de CTI mas brillante no sirve de nada si no se traduce en acciones: reglas en el SIEM, bloqueos en el firewall, priorizacion de parcheo, formacion a usuarios. La inteligencia que se queda en un PDF compartido por email y que nadie lee es desperdicio.

**Solucion.** Cada producto de inteligencia debe incluir acciones concretas y un responsable asignado. Mide la tasa de acciones implementadas.

### Error 4: Querer cubrir todo desde el primer dia

Intentar monitorizar la dark web, analizar malware en sandbox, hacer atribucion de APTs y mantener una plataforma de comparticion con 15 organizaciones... con una persona y medio dia a la semana.

**Solucion.** El plan de 90 dias anterior es realista. Empieza con feeds basicos, un MISP y un informe semanal. Crece cuando demuestres valor.

### Error 5: No medir el impacto del programa

Si no puedes demostrar que el programa CTI aporta valor, sera el primero en perder presupuesto (o tiempo de personal). Las metricas minimas:

- Numero de IOCs que generaron verdaderos positivos en el SIEM.
- Tiempo medio de deteccion antes y despues del programa CTI.
- Numero de acciones preventivas implementadas gracias a inteligencia (parches priorizados, reglas creadas, bloqueos aplicados).
- Feedback cualitativo de los stakeholders.

## Cuando invertir en threat intelligence de pago

La pregunta no es "deberia pagar por CTI?" sino "en que momento mi programa necesita fuentes comerciales?"

### Senales de que necesitas fuentes comerciales

- **Los feeds gratuitos ya no cubren tus requisitos.** Necesitas inteligencia especifica de tu sector (financiero, energetico, sanitario) que no esta disponible en fuentes publicas.
- **Necesitas atribucion y analisis de actores.** Los feeds gratuitos proporcionan IOCs. Los servicios comerciales (Recorded Future, Mandiant, CrowdStrike) proporcionan analisis de actores, campanas y predicciones.
- **Tu equipo no tiene capacidad de analisis.** Si solo puedes consumir inteligencia ya procesada, un servicio comercial que entregue reportes listos para consumir puede tener sentido.
- **Necesitas monitorizar la dark web.** La monitorizacion de foros, mercados y canales de Telegram donde se venden credenciales o se planifican ataques requiere herramientas especializadas (y precauciones legales).
- **Compliance o regulacion lo exige.** Sectores regulados (banca, infraestructuras criticas) pueden tener requisitos de comparticion o consumo de inteligencia que las fuentes gratuitas no satisfacen documentalmente.

### Que evaluar en un proveedor comercial

Si decides invertir, evalua:

- **Relevancia geografica.** El proveedor tiene cobertura de amenazas en Espana y Europa? Un proveedor enfocado en amenazas de Asia-Pacifico no te aporta tanto.
- **Formatos de entrega.** Soporta STIX 2.1? Tiene API? Se integra con tu SIEM y tu MISP? Si los datos llegan en PDF y hay que copiar IOCs a mano, el valor cae drasticamente.
- **Frescura.** Cual es la latencia entre la deteccion de una amenaza y la publicacion del IOC o el reporte? En threat intelligence tactica, horas importan.
- **Accionabilidad.** Los productos incluyen recomendaciones concretas o solo descripciones?

### Opciones intermedias

Antes de contratar un servicio premium (que puede costar desde 15.000 EUR/ano hasta cifras de seis digitos), considera opciones intermedias:

- **ISACs sectoriales.** Los centros de comparticion sectorial (financiero, energetico, sanitario) proporcionan inteligencia relevante y especifica. En Espana, el CCN coordina algunos de estos grupos.
- **FIRST y TF-CSIRT.** Comunidades de CERTs donde se comparte inteligencia entre miembros.
- **Programas de comparticion de vendors.** Cisco Talos, Microsoft MSTIC y otros publican inteligencia de alta calidad gratuitamente.

## El modelo de madurez CTI: donde estas y donde quieres llegar

Para medir la evolucion de tu programa, usa este modelo simplificado de cinco niveles:

| Nivel | Nombre | Descripcion |
|---|---|---|
| 0 | Inexistente | No hay actividad de CTI |
| 1 | Reactivo | Se consultan fuentes ad-hoc cuando ocurre un incidente |
| 2 | Basico | Feeds de IOCs integrados en SIEM, informe periodico |
| 3 | Funcional | MISP operativo, requisitos definidos, integracion con SOC, hunting basado en CTI |
| 4 | Avanzado | Analisis propio de campanas, comparticion con comunidad, metricas de impacto |
| 5 | Optimizado | CTI integrada en todas las decisiones de seguridad, automatizacion end-to-end, prediccion |

La mayoria de empresas espanolas estan en nivel 0 o 1. Llegar a nivel 2-3 en 6 meses es un objetivo realista y suficiente para generar valor tangible.

{{< cta type="bofu" text="Solicita una demo personalizada y descubre como Riskitera integra threat intelligence, deteccion automatizada y respuesta con IA soberana, sin que tus datos salgan de Espana." label="Solicitar demo" >}}


**Articulos relacionados:**
- [Iocs En Ciberseguridad Que Son](/es/posts/2026/04/iocs-en-ciberseguridad-que-son/)
- [Threat Hunting Guia Practica](/es/posts/2026/04/threat-hunting-guia-practica/)

## Preguntas frecuentes

### Cuantas personas necesito para un programa de CTI basico?

Una persona dedicando el 50% de su tiempo puede mantener un programa de nivel 2 (feeds integrados, informe semanal). Para nivel 3 (MISP operativo, hunting basado en CTI, analisis propio), necesitas al menos una persona a tiempo completo. En muchas PYMES espanolas, el rol de CTI lo asume un analista SOC senior como funcion complementaria. Lo importante no es el numero de personas sino la constancia: 4 horas a la semana de CTI consistente aportan mas valor que 40 horas puntuales una vez al trimestre.

### Es legal monitorizar la dark web para obtener threat intelligence?

La observacion pasiva de foros y mercados dark web accesibles (sin registrarse ni interactuar) es generalmente legal en Espana. Sin embargo, hay lineas que no debes cruzar: comprar credenciales robadas (aunque sean de tu propia empresa), interactuar con actores de amenaza haciendote pasar por comprador, o acceder a sistemas cerrados sin autorizacion. La recomendacion es limitar la monitorizacion dark web a servicios especializados que operan dentro del marco legal y dejar la investigacion activa a las FCSE (Fuerzas y Cuerpos de Seguridad del Estado).

### Como priorizo entre tantas fuentes de IOCs gratuitas?

Empieza por calidad, no por cantidad. Tres fuentes bien integradas aportan mas que quince mal gestionadas. Para una empresa espanola, la combinacion recomendada es: (1) Abuse.ch (URLhaus + MalwareBazaar + ThreatFox) por su alta calidad y frescura; (2) AlienVault OTX por su amplitud y facilidad de integracion; (3) CCN-CERT/INCIBE-CERT por su relevancia geografica. Anade mas fuentes solo cuando hayas validado que las primeras generan verdaderos positivos en tu entorno y no saturan al equipo.

### Que diferencia hay entre MISP y OpenCTI? Cual deberia usar?

MISP es mejor para la gestion operativa de IOCs: recopilar, normalizar, compartir y exportar indicadores al SIEM. OpenCTI es mejor para analisis y visualizacion: grafos de relaciones, dashboards y modelado de actores de amenaza. Para empezar, MISP es la opcion recomendada porque es mas ligero, tiene mas documentacion y cubre el caso de uso mas basico (feeds a SIEM). Cuando tu programa madure al nivel 3-4 y necesites capacidades analiticas avanzadas, anade OpenCTI como capa de analisis encima de MISP (ambos se integran nativamente).

### Como justifico el tiempo invertido en CTI ante direccion?

El argumento mas efectivo son las acciones preventivas documentadas. Lleva un registro de cada vez que la inteligencia genero una accion: "El 15 de marzo, un IOC de MISP detecto una conexion a infraestructura C2 de Emotet desde un puesto de contabilidad. Se aisle el equipo en 4 minutos y se evite la propagacion." Ese tipo de ejemplos concretos, con impacto estimado (coste medio de un incidente de ransomware en Espana segun INCIBE: entre 100.000 y 2M EUR para PYMES), son mucho mas convincentes que metricas abstractas como "numero de IOCs procesados".
