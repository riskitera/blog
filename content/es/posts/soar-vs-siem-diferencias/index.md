---
title: "SOAR vs SIEM: diferencias, integracion y cuando necesitas ambos"
description: "Comparativa detallada entre SOAR y SIEM: diferencias funcionales, cuando necesitas cada uno, como integrarlos y mejores practicas para un SOC eficiente."
slug: "soar-vs-siem-diferencias"
date: 2026-06-18
publishDate: 2026-06-18
lastmod: 2026-06-18
draft: false
tags: ["SOC", "SIEM", "SOAR", "Herramientas"]
categories: ["SOC"]
author: "David Moya"
keyword: "SOAR vs SIEM"
funnel: "mofu"
---

Comparativa detallada entre SOAR y SIEM: diferencias funcionales, cuando necesitas cada uno, como integrarlos y mejores practicas para un SOC eficiente.

<!--more-->

{{< key-takeaways >}}
- SIEM recopila, correlaciona y analiza logs de seguridad para detectar amenazas. SOAR automatiza la respuesta, la orquestacion y la gestion de casos tras la deteccion.
- Un SIEM sin SOAR genera alertas que los analistas deben investigar manualmente. Un SOAR sin SIEM carece de la fuente de deteccion primaria para alimentar sus playbooks.
- La integracion SIEM + SOAR reduce el tiempo medio de respuesta (MTTR) de horas a minutos, automatizando el triage de alertas de bajo riesgo y enriqueciendo las de alto riesgo.
- El mercado ofrece opciones desde soluciones enterprise (Splunk SOAR, Cortex XSOAR) hasta alternativas open source (Shuffle, Tines Community) para equipos con presupuesto limitado.
- Antes de comprar un SOAR, valida que tu SOC tiene playbooks documentados, fuentes de datos integradas en el SIEM y al menos un analista capaz de mantener las automatizaciones.
{{< /key-takeaways >}}

## Que es un SIEM y que problema resuelve

Un SIEM (Security Information and Event Management) es la herramienta central de visibilidad de un SOC. Segun la definicion de [Gartner](https://www.gartner.com/), un SIEM combina dos capacidades que originalmente eran productos separados: la gestion de informacion de seguridad (SIM) y la gestion de eventos de seguridad (SEM).

En terminos practicos, un SIEM hace tres cosas fundamentales:

**Recopilacion centralizada de logs.** Ingesta datos de decenas o cientos de fuentes: firewalls, endpoints, servidores, aplicaciones, servicios cloud, proxies, sistemas de autenticacion, bases de datos. Todo se normaliza en un formato comun para poder correlacionar eventos entre fuentes diferentes.

**Correlacion y deteccion.** Aplica reglas de correlacion, modelos estadicos y (cada vez mas) modelos de machine learning para identificar patrones sospechosos. Por ejemplo: un inicio de sesion desde una IP en un pais inusual, seguido de un acceso a un recurso sensible, seguido de una transferencia de datos superior al umbral normal. Ninguno de estos eventos por separado seria una alerta, pero la secuencia si.

**Almacenamiento y busqueda.** Retiene logs durante semanas, meses o anios (segun la politica de retencion), permitiendo investigaciones forenses retrospectivas. Cuando un analista necesita reconstruir la secuencia de un ataque que empezo hace tres meses, el SIEM es donde busca.

Los SIEM mas extendidos en el mercado incluyen Splunk Enterprise Security, Microsoft Sentinel, IBM QRadar, Elastic Security, Google Chronicle (SecOps) y LogRhythm. Cada uno tiene fortalezas distintas en escala, coste, facilidad de uso o integraciones nativas.

### Las limitaciones reales de un SIEM

A pesar de su importancia, un SIEM tiene limitaciones que cualquier equipo SOC conoce de primera mano:

- **Fatiga de alertas**: un SIEM mal tunado puede generar miles de alertas diarias, de las cuales un porcentaje significativo son falsos positivos. Los analistas acaban ignorando alertas o priorizando mal.
- **Accion manual**: el SIEM detecta, pero no actua. Cuando genera una alerta, un analista humano debe investigar, decidir y ejecutar la respuesta. Esto introduce latencia.
- **Complejidad de reglas**: mantener las reglas de correlacion actualizadas requiere conocimiento del panorama de amenazas y de la infraestructura. Las reglas obsoletas generan ruido, y las que faltan dejan puntos ciegos.
- **Coste de ingesta**: el modelo de precios de muchos SIEM se basa en volumen de datos ingeridos (GB/dia). A medida que la infraestructura crece, los costes pueden dispararse, forzando decisiones incomodas sobre que logs incluir.

Estas limitaciones son exactamente las que un SOAR viene a resolver.

## Que es un SOAR y que problema resuelve

SOAR (Security Orchestration, Automation and Response) es una categoria de herramientas que automatiza y orquesta los flujos de trabajo de respuesta a incidentes de seguridad. El termino fue acunado por Gartner en 2017, aunque las capacidades subyacentes existian antes bajo otros nombres.

Un SOAR tiene tres componentes principales:

**Orquestacion (Orchestration).** Conecta herramientas de seguridad dispares y coordina acciones entre ellas. Un SOAR puede, en una sola ejecucion de playbook, consultar el SIEM, enriquecer una IP en un servicio de reputacion, bloquear la IP en el firewall, crear un ticket en el sistema de gestion y enviar una notificacion al canal de Slack del equipo. Sin el SOAR, un analista haria esto manualmente, alternando entre 5 o 6 consolas diferentes.

**Automatizacion (Automation).** Ejecuta tareas repetitivas sin intervencion humana. El ejemplo clasico: una alerta de phishing llega al SIEM, el SOAR automaticamente extrae los indicadores (URLs, hashes de adjuntos, remitente), los consulta contra bases de reputacion ([MITRE ATT&CK](https://attack.mitre.org/), VirusTotal, AbuseIPDB), y si el veredicto es malicioso, bloquea el remitente, elimina el correo de todos los buzones afectados y documenta el caso. Todo en menos de un minuto.

**Respuesta (Response).** Gestiona el ciclo de vida completo de los incidentes: creacion del caso, asignacion al analista adecuado, seguimiento de las tareas de remediacion, generacion de metricas (MTTD, MTTR, tasa de falsos positivos) y creacion de informes para la direccion.

## Tabla comparativa: SIEM vs SOAR

| Aspecto | SIEM | SOAR |
|---|---|---|
| **Funcion principal** | Deteccion de amenazas | Respuesta a amenazas |
| **Entrada de datos** | Logs, eventos, flujos de red | Alertas del SIEM, tickets, IoCs |
| **Salida principal** | Alertas correlacionadas | Acciones automatizadas, casos cerrados |
| **Correlacion** | Si (motor de reglas, ML) | Limitada (depende del SIEM) |
| **Automatizacion** | Basica (alertas, dashboards) | Avanzada (playbooks completos) |
| **Integraciones** | Fuentes de datos (agentes, APIs) | Herramientas de accion (firewalls, EDR, ticketing) |
| **Almacenamiento** | Largo plazo (logs historicos) | Corto plazo (casos activos) |
| **Tiempo de valor** | Semanas a meses (tuning) | Dias a semanas (playbooks) |
| **Modelo de coste** | Volumen de datos (GB/dia) | Numero de acciones/analistas |
| **Curva de aprendizaje** | Alta (queries, reglas) | Media (visual, low-code) |
| **Ejemplo de uso** | Detectar login anomalo | Bloquear cuenta + notificar + documentar |

La conclusion de esta tabla es simple: SIEM y SOAR no son competidores. Son complementarios. El SIEM es los ojos del SOC. El SOAR es las manos.

## Que hace un SOAR que no hace un SIEM

Para entender cuando necesitas un SOAR, es util desglosar las capacidades exclusivas que aporta:

### Playbooks automatizados

Un playbook es una secuencia de acciones predefinidas que se ejecuta automaticamente (o con aprobacion humana en pasos criticos) cuando se cumple un disparador. Ejemplos reales:

**Playbook de phishing:**
1. Alerta de phishing llega del SIEM o de la bandeja de abuso.
2. Extraer URLs, IPs, hashes de adjuntos, remitente.
3. Consultar reputacion en VirusTotal, URLhaus, AbuseIPDB.
4. Si es malicioso: bloquear remitente en el gateway de correo, eliminar correo de buzones afectados, aislar endpoints que hayan hecho clic.
5. Crear caso con toda la evidencia adjunta.
6. Notificar al equipo y al usuario afectado.
7. Generar informe de cierre.

**Playbook de endpoint comprometido:**
1. Alerta de EDR indica comportamiento sospechoso en un endpoint.
2. Aislar el endpoint de la red (via API del EDR).
3. Capturar snapshot de memoria y procesos activos.
4. Consultar hashes de procesos sospechosos contra threat intelligence.
5. Si se confirma compromiso: escalar a N2, iniciar procedimiento forense.
6. Si es falso positivo: restaurar conectividad, documentar y cerrar.

**Playbook de fuerza bruta:**
1. El SIEM detecta multiples intentos fallidos de autenticacion desde una IP.
2. Consultar la IP en listas de reputacion.
3. Si la IP es conocida como maliciosa: bloquear en firewall, notificar.
4. Si la IP es interna: verificar si la cuenta esta comprometida, forzar cambio de contrasena.
5. Documentar y cerrar.

Estos playbooks no son teoria. Son flujos que los SOC maduros ejecutan decenas de veces al dia, y sin automatizacion cada uno consume entre 20 y 45 minutos de trabajo de analista.

### Orquestacion multi-herramienta

Un SOC tipico utiliza entre 10 y 50 herramientas de seguridad. El SOAR actua como el conector central que permite a estas herramientas trabajar juntas sin que el analista tenga que saltar entre consolas. Las integraciones tipicas incluyen:

- SIEM (Splunk, Sentinel, QRadar)
- EDR (CrowdStrike, SentinelOne, Microsoft Defender)
- Firewall/NGFW (Palo Alto, Fortinet, Check Point)
- Ticketing (ServiceNow, Jira)
- Threat Intelligence (MITRE, VirusTotal, OTX, MISP)
- Email security (Proofpoint, Mimecast)
- Cloud (AWS Security Hub, Azure Defender, GCP SCC)
- Comunicaciones (Slack, Teams, PagerDuty)

### Gestion de casos e investigacion

El SOAR proporciona un espacio centralizado donde cada incidente tiene su timeline de eventos, evidencias adjuntas, acciones realizadas (automaticas y manuales), analistas asignados y estado actual. Esto es critico para:

- Auditorias de cumplimiento (DORA, NIS2, ISO 27001).
- Traspaso entre turnos de analistas.
- Post-mortem de incidentes.
- Metricas de rendimiento del SOC.

### Metricas y reporting automatizado

Un SOAR bien configurado genera automaticamente metricas que un SIEM por si solo no puede calcular:

- **MTTD** (Mean Time to Detect): tiempo desde que ocurre el evento hasta que se genera la alerta.
- **MTTR** (Mean Time to Respond): tiempo desde la alerta hasta la remediacion completa.
- **Tasa de automatizacion**: porcentaje de alertas gestionadas sin intervencion humana.
- **Alertas por analista**: carga de trabajo por persona.
- **Falsos positivos**: porcentaje de alertas que resultan benignas despues de investigacion.

{{< cta type="tofu" text="Riskitera automatiza el triage, la correlacion y el reporting de tu SOC con IA soberana. Reduce tu MTTR sin enviar datos a terceros." label="Ver demo SOC" >}}

## Cuando necesitas un SOAR ademas del SIEM

No todos los SOC necesitan un SOAR. Hay senales claras de que ha llegado el momento:

### Senales de que necesitas un SOAR

1. **Tu equipo no puede gestionar el volumen de alertas.** Si los analistas procesan menos del 50% de las alertas generadas por el SIEM, las alertas pendientes se acumulan y los tiempos de respuesta crecen semana a semana, necesitas automatizar.

2. **Las tareas repetitivas consumen mas del 60% del tiempo de los analistas.** Enriquecer IoCs, crear tickets, notificar a stakeholders, documentar acciones. Si tus analistas N1 pasan la mayor parte del dia en tareas que no requieren juicio experto, un SOAR libera su tiempo para investigaciones reales.

3. **El MTTR supera los 30 minutos para alertas de riesgo medio.** Un SOAR bien configurado puede reducir el MTTR de alertas rutinarias de 30 minutos a menos de 2 minutos.

4. **Tienes requisitos regulatorios de documentacion y trazabilidad.** Marcos como DORA, NIS2 o ISO 27001 exigen evidencias de que los incidentes se gestionan de forma estructurada, con tiempos de respuesta medibles y acciones documentadas.

5. **Operas un SOC 24/7 con rotacion de turnos.** La consistencia en la respuesta es critica. Un playbook automatizado aplica la misma logica a las 3 de la manana que a las 10 de la manana, independientemente de quien este de turno.

### Cuando NO necesitas un SOAR (todavia)

- Tu equipo SOC tiene menos de 3 personas y el volumen de alertas es manejable.
- No tienes playbooks de respuesta documentados (primero documenta, luego automatiza).
- Tu SIEM no esta bien tunado y genera mas ruido que senales (arregla el SIEM primero).
- No tienes integraciones API con tus herramientas de seguridad (el SOAR necesita APIs para actuar).

## Como se integran SOAR y SIEM

La integracion entre SIEM y SOAR sigue patrones bien establecidos. Estos son los mas comunes:

### Patron 1: SIEM como fuente primaria de alertas

El flujo mas basico y mas comun:

```
[Fuentes de logs] → [SIEM] → [Alertas correlacionadas] → [SOAR] → [Acciones automatizadas]
```

El SIEM ingesta logs, aplica reglas de correlacion y genera alertas. El SOAR recibe estas alertas via API, webhook o syslog, y ejecuta el playbook correspondiente. Este patron funciona bien cuando el SIEM es la fuente principal de deteccion.

### Patron 2: SOAR como agregador multi-fuente

En SOCs maduros, el SOAR recibe alertas de multiples fuentes, no solo del SIEM:

```
[SIEM]           ─┐
[EDR]            ─┤
[Email gateway]  ─┼→ [SOAR] → [Deduplicacion + Correlacion + Playbook]
[Cloud alerts]   ─┤
[Threat intel]   ─┘
```

En este patron, el SOAR deduplica alertas (la misma IP puede generar alertas en el SIEM, el EDR y el firewall simultaneamente), las correlaciona como parte del mismo incidente y ejecuta un playbook unificado. Esto evita que tres analistas investiguen el mismo evento por separado.

### Patron 3: Retroalimentacion bidireccional

El patron mas avanzado incluye un bucle de feedback:

```
[SIEM] ←→ [SOAR]
  ↑           ↓
  └── [Threat Intel actualizada, reglas refinadas] ──┘
```

El SOAR, tras resolver un incidente, puede actualizar las reglas del SIEM (aniadir una IP a una watchlist, ajustar un umbral de correlacion), enriquecer las fuentes de threat intelligence (agregar nuevos IoCs validados) o modificar la prioridad de futuras alertas similares. Este bucle de mejora continua es lo que diferencia un SOC reactivo de uno proactivo.

### Ejemplo de integracion practica

Un banco mediano con Splunk Enterprise Security como SIEM y Splunk SOAR decide automatizar el proceso de phishing:

1. **Configuracion en Splunk ES**: regla de correlacion que detecta correos con adjuntos ejecutables o URLs sospechosas reportados por usuarios.
2. **Conector SOAR**: webhook que envia la alerta a Splunk SOAR cuando la regla se dispara.
3. **Playbook en SOAR**: extrae IoCs, consulta VirusTotal y URLhaus, verifica si otros usuarios recibieron el mismo correo, y decide:
   - Si malicioso: elimina correo de todos los buzones (via API de Exchange/M365), bloquea URLs en el proxy (via API de Zscaler), crea caso y notifica.
   - Si sospechoso: escala a analista N2 con toda la informacion pre-enriquecida.
   - Si benigno: cierra automaticamente y documenta.
4. **Feedback**: los IoCs confirmados se anaden a la watchlist de Splunk ES para deteccion futura.

Resultado: lo que antes consumia 35 minutos por alerta ahora se resuelve en 90 segundos para los casos automaticos, y en 10 minutos para los escalados (porque el analista recibe toda la informacion ya enriquecida).

## Principales plataformas SOAR del mercado

### Soluciones enterprise

**Splunk SOAR (antes Phantom)**
Probablemente el SOAR mas maduro del mercado. Mas de 300 integraciones nativas, editor visual de playbooks, fuerte en automatizacion y con la ventaja de integracion nativa con Splunk ES. Adquisicion por Cisco en 2024 amplia el ecosistema. Punto debil: precio elevado y curva de aprendizaje para playbooks complejos.

**Cortex XSOAR (Palo Alto Networks)**
Originalmente Demisto, adquirido por Palo Alto en 2019. Destaca por su marketplace de integraciones y content packs, su motor de machine learning para clasificacion de alertas y la integracion con el ecosistema Palo Alto (NGFW, Prisma, Cortex XDR). Incluye un modulo de threat intelligence integrado (TIM). Punto debil: funcionalidad completa requiere el ecosistema Palo Alto.

**Microsoft Sentinel + Logic Apps**
Microsoft ha integrado capacidades SOAR directamente en Sentinel mediante Logic Apps y reglas de automatizacion. No es un SOAR independiente, sino capacidades de automatizacion integradas en el SIEM. Ventaja: coste nulo adicional si ya usas Sentinel. Punto debil: menos flexible que un SOAR dedicado para orquestacion multi-vendor.

**IBM QRadar SOAR (antes Resilient)**
Fuerte en gestion de casos y cumplimiento regulatorio (incluye plantillas para GDPR, DORA, NIS2). Buena integracion con QRadar SIEM. Punto debil: interfaz menos moderna que competidores y menor comunidad de integraciones.

### Alternativas open source y low-cost

**Shuffle**
SOAR open source con editor visual de workflows, mas de 1000 integraciones via OpenAPI y despliegue on-premise o cloud. Ideal para equipos que quieren control total y tienen capacidad de gestion. Licencia gratuita para uso basico, con planes de pago para funcionalidades avanzadas.

**Tines**
Plataforma de automatizacion no-code con enfoque en seguridad. Ofrece un tier Community Edition gratuito con funcionalidad completa (limitado en volumen). Destaca por su simplicidad: los playbooks se construyen arrastrando "stories" (acciones) y conectandolas visualmente. Ideal para equipos pequenos que necesitan resultados rapidos.

**TheHive + Cortex**
Combinacion open source donde TheHive gestiona los casos y Cortex ejecuta los analyzers y responders (automatizaciones). Muy popular en CERTs y SOCs europeos. Punto debil: requiere mas esfuerzo de mantenimiento que las soluciones comerciales.

**n8n (con enfoque seguridad)**
Aunque n8n es una plataforma de automatizacion generica, su modelo self-hosted, su motor de workflows visuales y sus integraciones con APIs de seguridad lo convierten en una opcion viable para equipos que necesitan automatizacion SOC sin el coste de un SOAR enterprise. Especialmente util cuando ya se utiliza n8n para otras automatizaciones operativas.

## Build vs buy: cuando construir tus propios playbooks

La decision entre comprar un SOAR comercial o construir automatizaciones con herramientas genericas depende de varios factores:

### Cuando comprar un SOAR comercial

- Tu SOC tiene mas de 10 analistas y gestiona mas de 500 alertas diarias.
- Necesitas integraciones out-of-the-box con docenas de herramientas de seguridad.
- Tienes requisitos de cumplimiento que exigen un audit trail robusto (DORA, NIS2).
- El presupuesto lo permite (entre 50.000 y 300.000 EUR anuales segun la solucion y el tamano).

### Cuando construir con herramientas genericas

- Tu SOC tiene menos de 10 analistas y el volumen de alertas es moderado.
- Tienes ingenieros de seguridad capaces de desarrollar y mantener playbooks.
- Tus necesidades de automatizacion son especificas y no justifican el coste de una plataforma completa.
- Prefieres un enfoque incremental: automatizar un playbook, medir resultados, iterar.

### Ejemplo de playbook "build" con Python

Para equipos que deciden construir, un playbook de enriquecimiento de IoCs puede ser sorprendentemente simple:

```python
import requests
from datetime import datetime

def enrich_ioc(ioc_value: str, ioc_type: str) -> dict:
    """Enriquece un IoC consultando multiples fuentes."""
    results = {"ioc": ioc_value, "type": ioc_type, "timestamp": datetime.utcnow().isoformat()}

    if ioc_type == "ip":
        # AbuseIPDB
        resp = requests.get(
            "https://api.abuseipdb.com/api/v2/check",
            headers={"Key": ABUSEIPDB_KEY, "Accept": "application/json"},
            params={"ipAddress": ioc_value, "maxAgeInDays": 90}
        )
        results["abuseipdb_score"] = resp.json()["data"]["abuseConfidenceScore"]

        # VirusTotal
        resp = requests.get(
            f"https://www.virustotal.com/api/v3/ip_addresses/{ioc_value}",
            headers={"x-apikey": VT_KEY}
        )
        stats = resp.json()["data"]["attributes"]["last_analysis_stats"]
        results["vt_malicious"] = stats.get("malicious", 0)

    elif ioc_type == "hash":
        resp = requests.get(
            f"https://www.virustotal.com/api/v3/files/{ioc_value}",
            headers={"x-apikey": VT_KEY}
        )
        stats = resp.json()["data"]["attributes"]["last_analysis_stats"]
        results["vt_malicious"] = stats.get("malicious", 0)

    return results
```

Este script, conectado a un webhook del SIEM y combinado con un par de acciones de remediacion (bloqueo en firewall via API, creacion de ticket en Jira), cubre el 80% de lo que un SOAR basico ofrece para ese caso de uso especifico.

## Que errores evitar al implementar SOAR

La implementacion de un SOAR es un proyecto que puede salir muy bien o muy mal. Estos son los errores mas comunes:

### Error 1: Automatizar sin documentar

Si no tienes playbooks de respuesta documentados antes de implementar el SOAR, vas a automatizar el caos. Primero documenta como gestionas cada tipo de alerta manualmente (phishing, malware, fuerza bruta, acceso no autorizado). Luego identifica que pasos son automatizables. Solo entonces configura el SOAR.

### Error 2: Intentar automatizar todo desde el dia uno

Empieza con 3 a 5 playbooks de alto volumen y bajo riesgo (enriquecimiento de IoCs, cierre automatico de falsos positivos conocidos, notificaciones). Mide los resultados durante un mes. Luego expande gradualmente. La tentacion de automatizar 50 playbooks en paralelo lleva al agotamiento del equipo y a playbooks mal probados que generan mas problemas que los que resuelven.

### Error 3: No incluir puntos de decision humana

No todo debe ser full-auto. Las acciones de alto impacto (aislar un servidor de produccion, bloquear una cuenta de un directivo, reportar un incidente al regulador) deben incluir un checkpoint donde un analista humano aprueba o rechaza antes de ejecutar. La automatizacion sin supervision en acciones criticas es una receta para el desastre.

### Error 4: No medir el antes y el despues

Sin metricas de referencia (MTTR antes del SOAR, tiempo por alerta, porcentaje de alertas procesadas), no puedes demostrar el ROI de la implementacion. Mide durante al menos un mes antes de desplegar el SOAR, y compara con los mismos KPIs despues.

### Error 5: Ignorar el mantenimiento continuo

Los playbooks no son "configurar y olvidar". Las APIs cambian, las herramientas se actualizan, las amenazas evolucionan. Asigna al menos un 20% del tiempo de un ingeniero de seguridad al mantenimiento y evolucion de los playbooks. Un playbook roto es peor que no tener playbook, porque da una falsa sensacion de seguridad.

### Error 6: No alinear con el framework MITRE ATT&CK

Cada playbook deberia mapear a una o mas tacticas y tecnicas de MITRE ATT&CK. Esto permite identificar gaps en la cobertura de deteccion y respuesta, priorizar playbooks por riesgo real y comunicar el valor al negocio en un lenguaje comun.

## Cuanto cuesta implementar un SOAR

El coste total de propiedad (TCO) de un SOAR incluye mucho mas que la licencia del software:

| Componente | Rango de coste anual |
|---|---|
| Licencia SOAR enterprise | 50.000 a 300.000 EUR |
| SOAR open source (infra + soporte) | 10.000 a 50.000 EUR |
| Integracion inicial (servicios profesionales) | 20.000 a 80.000 EUR (una vez) |
| Desarrollo de playbooks (interno o externo) | 15.000 a 60.000 EUR |
| Mantenimiento anual (20% de un FTE) | 15.000 a 30.000 EUR |
| Formacion del equipo | 5.000 a 15.000 EUR |

Para un SOC mediano (5 a 15 analistas, 200 a 1000 alertas diarias), el coste total del primer anio oscila entre 80.000 y 200.000 EUR con una solucion enterprise, y entre 30.000 y 80.000 EUR con una solucion open source.

El ROI tipico se calcula en tiempo de analista recuperado. Si un SOAR automatiza 200 alertas diarias que antes consumian 20 minutos cada una, son 66 horas de analista al dia. A un coste medio de 35 EUR/hora, son 2.310 EUR diarios, o mas de 840.000 EUR anuales. Incluso con numeros mas conservadores, el ROI es habitualmente positivo en el primer anio.

{{< cta type="bofu" text="Solicita una demo personalizada para tu SOC y descubre como Riskitera optimiza tus operaciones con automatizacion soberana y cumplimiento DORA integrado." label="Solicitar demo" >}}


**Articulos relacionados:**
- [Que Es Un Siem Para Que Sirve](/es/posts/2026/04/que-es-un-siem-para-que-sirve/)
- [Como Montar Soc Desde Cero](/es/posts/2026/04/como-montar-soc-desde-cero/)

## Preguntas frecuentes

### Puede un SOAR reemplazar completamente a un SIEM?

No. Un SOAR no recopila ni almacena logs, no ejecuta correlacion de eventos a gran escala ni proporciona capacidad forense retrospectiva. El SOAR necesita una fuente de deteccion (normalmente un SIEM) que le alimente con alertas. Son herramientas complementarias: el SIEM detecta, el SOAR responde. Intentar usar un SOAR sin SIEM es como tener un equipo de bomberos sin sistema de alarma contra incendios.

### Necesito un SOAR si mi SIEM ya tiene automatizacion basica?

Depende del nivel de automatizacion que necesites. Muchos SIEM modernos (como Microsoft Sentinel con Logic Apps o Splunk con Adaptive Response) incluyen capacidades basicas de automatizacion. Para SOCs pequenos con necesidades simples (notificaciones, enriquecimiento basico), esto puede ser suficiente. Cuando necesitas orquestacion multi-herramienta compleja, playbooks con logica condicional avanzada, gestion de casos completa o integraciones con decenas de herramientas externas, un SOAR dedicado aporta un valor significativamente mayor.

### Cuanto tiempo tarda en ser productivo un SOAR despues de la implementacion?

El tiempo hasta el primer valor depende del enfoque. Un playbook simple (enriquecimiento automatico de IoCs) puede estar operativo en 1 a 2 semanas. Tres a cinco playbooks de produccion con integraciones reales suelen estar listos en 4 a 8 semanas. Un programa de automatizacion maduro con 15 o mas playbooks, metricas completas y bucles de feedback lleva entre 3 y 6 meses. La clave es empezar con victorias rapidas que demuestren valor al equipo y a la direccion, y expandir gradualmente.

### Es viable un SOAR open source para un SOC en produccion?

Si, con matices. Herramientas como Shuffle, TheHive + Cortex o incluso n8n con integraciones de seguridad pueden cubrir las necesidades de un SOC de tamano pequeno a mediano. Las ventajas son el control total, la ausencia de costes de licencia y la flexibilidad de personalizacion. Los inconvenientes son la mayor carga de mantenimiento, la necesidad de ingenieros con habilidades de desarrollo, y la ausencia de soporte comercial (aunque Shuffle y Tines ofrecen planes de pago con soporte). Para SOCs con requisitos regulatorios estrictos (banca, seguros), el audit trail y las certificaciones de un SOAR enterprise pueden ser un factor decisivo.

### Como se relaciona la implementacion de un SOAR con el cumplimiento de DORA?

DORA (Reglamento UE 2022/2554) exige que las entidades financieras tengan procesos de gestion de incidentes TIC con plazos estrictos de notificacion (4 horas para la notificacion inicial, 72 horas para la intermedia). Un SOAR facilita el cumplimiento al automatizar la clasificacion de incidentes, generar las notificaciones en el formato requerido por las autoridades, documentar automaticamente la timeline de acciones y calcular los tiempos de respuesta. No es un requisito explicito de DORA tener un SOAR, pero en la practica es muy dificil cumplir los plazos de notificacion de forma consistente sin algun nivel de automatizacion.
