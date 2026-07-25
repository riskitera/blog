---
title: "Feeds de CTI gratuitos: los 15 mejores y cómo integrarlos"
image: "cover.png"
description: "Los 15 mejores feeds de threat intelligence gratuitos en 2026: MISP, AlienVault OTX, Abuse.ch, CIRCL y más. Como integrarlos en tu SIEM y maximizar su valor."
slug: "feeds-cti-gratuitos-mejores"
date: 2026-07-23
publishDate: 2026-07-23
lastmod: 2026-07-23
draft: false
tags: ["CTI", "Threat Intelligence", "SIEM", "Herramientas"]
categories: ["CTI"]
author: "David Moya"
keyword: "feeds CTI gratuitos"
funnel: "tofu"
---

Los 15 mejores feeds de threat intelligence gratuitos en 2026: MISP, AlienVault OTX, Abuse.ch, CIRCL y más. Como integrarlos en tu SIEM y maximizar su valor operativo.

<!--more-->

{{< key-takeaways >}}
- Los feeds de CTI gratuitos proporcionan IOCs (indicadores de compromiso) que alimentan tu SIEM, firewall y EDR sin coste de licencia.
- Los cuatro pilares gratuitos son AlienVault OTX, el ecosistema Abuse.ch, MISP/CIRCL y el catálogo CISA KEV.
- La calidad de un feed se mide por su tasa de falsos positivos, frecuencia de actualización, contexto proporcionado y facilidad de integración.
- Integrar demasiados feeds sin filtrado genera fatiga de alertas. La clave es correlacionar, puntuar y descartar IOCs obsoletos.
- Pasar de feeds gratuitos a comerciales tiene sentido cuando necesitas atribución, contexto geopolitico o cobertura de dark web que los feeds abiertos no ofrecen.
{{< /key-takeaways >}}

## ¿Qué es un feed de CTI y por qué lo necesitas?

Un feed de Cyber Threat Intelligence (CTI) es una fuente de datos estructurados que proporciona indicadores de compromiso (IOCs), información sobre amenazas activas y contexto sobre campañas maliciosas. Los IOCs típicos incluyen hashes de malware, direcciones IP maliciosas, dominios de phishing, URLs de distribución de malware y firmas de vulnerabilidades explotadas.

La razón por la que un SOC necesita feeds de CTI es simple: sin inteligencia externa, tu capacidad de detección se limita a lo que ya conoces. Los feeds te permiten:

- **Detectar proactivamente** amenazas conocidas antes de que causen daño.
- **Enriquecer alertas** del SIEM con contexto (quién ataca, qué campaña, qué malware).
- **Priorizar respuesta** basándote en la severidad y relevancia de la amenaza.
- **Bloquear preventivamente** dominios, IPs y hashes maliciosos en tus controles perimetrales.

La buena noticia: no necesitas gastar miles de euros en feeds comerciales para empezar. Existen feeds gratuitos de alta calidad que cubren una parte significativa de las amenazas operativas.

## Los 15 mejores feeds de CTI gratuitos

### 1. AlienVault OTX (Open Threat Exchange)

[AlienVault OTX](https://otx.alienvault.com/) es la plataforma de threat intelligence colaborativa más grande del mundo, con más de 200.000 participantes que comparten "pulsos" (colecciones de IOCs asociados a una amenaza concreta).

| Característica | Detalle |
|---|---|
| **Tipo de datos** | IPs, dominios, URLs, hashes (MD5/SHA1/SHA256), CVEs, YARA rules, CIDR |
| **Formato** | API REST (JSON), STIX/TAXII, CSV, OpenIOC |
| **Frecuencia de actualización** | Continua (cada pulso es independiente) |
| **Registro** | Gratuito con cuenta |
| **Integración** | API directa, plugins para Splunk, QRadar, ELK, MISP |

**Punto fuerte**: la comunidad. Cuando surge una campaña nueva (ej. un nuevo ransomware), los pulsos aparecen en horas con IOCs verificados por múltiples analistas. La API permite filtrar por país, sector o tipo de amenaza.

**Limitación**: la calidad depende del contribuyente. Algunos pulsos contienen IOCs sin verificar o ya obsoletos. Siempre cruza con otras fuentes antes de bloquear.

**Integración SIEM**: OTX ofrece un SDK en Python (`OTXv2`) y una API REST documentada. Para Splunk existe el add-on oficial "AlienVault OTX". En ELK puedes usar Logstash con el plugin `http_poller` apuntando a la API de OTX y enriqueciendo eventos con un filtro `translate` o `elasticsearch` lookup.

### 2. Abuse.ch: URLhaus

[Abuse.ch](https://abuse.ch/) es un proyecto de investigación suizo que opera varios feeds especializados. [URLhaus](https://urlhaus.abuse.ch/) se centra en URLs utilizadas para distribuir malware.

| Característica | Detalle |
|---|---|
| **Tipo de datos** | URLs de distribución de malware, tags de campaña |
| **Formato** | CSV, JSON, API REST, STIX/TAXII |
| **Frecuencia de actualización** | Cada 5 minutos |
| **Registro** | No necesario para descargas; necesario para contribuir |
| **Volumen** | ~1.000 a 3.000 URLs activas en cualquier momento |

**Punto fuerte**: velocidad. URLhaus es consistentemente uno de los primeros feeds en publicar URLs de distribución de campañas nuevas. La comunidad de investigadores que reporta es muy activa.

**Integración SIEM**: descarga directa del CSV con `curl` o `wget` en un cron job. La mayoría de SIEMs pueden ingerir el CSV como lista de IOCs. Para Suricata o Snort, URLhaus pública reglas IDS específicas.

### 3. Abuse.ch: MalwareBazaar

[MalwareBazaar](https://bazaar.abuse.ch/) es el repositorio de muestras de malware de Abuse.ch, con más de 3 millones de muestras catalogadas.

| Característica | Detalle |
|---|---|
| **Tipo de datos** | Hashes (MD5/SHA256/SHA1), tags de familia, tlsh, imphash, ssdeep |
| **Formato** | API REST (JSON), CSV diario, STIX/TAXII |
| **Frecuencia de actualización** | Continua (cada muestra subida se pública) |
| **Registro** | No necesario para consultas; API key para uploads |

**Punto fuerte**: la profundidad de metadatos. Cada muestra incluye múltiple hashes, tags de familia de malware, resultados de sandbox y vinculación con campañas conocidas. Ideal para enriquecer alertas de EDR.

**Integración SIEM**: el dump diario de hashes se integra como feed de IOCs en cualquier SIEM. La API permite consultas de enriquecimiento en tiempo real: recibe una alerta con un hash, consulta MalwareBazaar para obtener contexto.

### 4. Abuse.ch: ThreatFox

[ThreatFox](https://threatfox.abuse.ch/) recopila IOCs asociados a familias de malware específicas, con énfasis en infraestructura de comando y control (C2).

| Característica | Detalle |
|---|---|
| **Tipo de datos** | IPs, dominios, URLs de C2, asociados a familias de malware |
| **Formato** | API REST (JSON), CSV, STIX/TAXII, MISP feed |
| **Frecuencia de actualización** | Continua |
| **Registro** | No necesario para consultas |

**Punto fuerte**: la vinculación directa entre IOC y familia de malware. Cada indicador viene etiquetado con la familia (Cobalt Strike, Emotet, QakBot, etc.), lo que facilita el triage. El formato MISP nativo permite importación directa en instancias MISP.

### 5. Abuse.ch: Feodo Tracker

[Feodo Tracker](https://feodotracker.abuse.ch/) rastrea servidores de comando y control de botnets bancarios (Dridex, Emotet, TrickBot, QakBot y sus sucesores).

| Característica | Detalle |
|---|---|
| **Tipo de datos** | IPs de C2, puertos, estado (activo/offline), familia de botnet |
| **Formato** | CSV, JSON, blocklist para firewalls |
| **Frecuencia de actualización** | Cada 5 minutos |
| **Registro** | No necesario |

**Punto fuerte**: las blocklists preparadas. Feodo Tracker pública listas en formato compatible con pfSense, iptables y Cisco ASA, listas para copiar y pegar en tu firewall. También ofrece reglas Suricata.

### 6. MISP (Malware Information Sharing Platform)

[MISP](https://www.misp-project.org/) no es un feed, sino una plataforma open source de compartición de inteligencia que agrega feeds de múltiples fuentes (incluidos todos los de Abuse.ch) y permite crear, compartir y correlacionar eventos de amenazas.

| Característica | Detalle |
|---|---|
| **Tipo de datos** | Todos (IPs, dominios, hashes, emails, YARA, Sigma, vulnerabilidades) |
| **Formato** | Formato MISP nativo (JSON), STIX 1.x/2.x, OpenIOC, CSV, texto |
| **Frecuencia de actualización** | Depende de los feeds configurados y la comunidad |
| **Registro** | Requiere instancia propia o acceso a instancia comunitaria |

**Punto fuerte**: la capacidad de correlación. MISP conecta IOCs entre sí (esta IP sirve este malware, que explota esta vulnerabilidad, en esta campaña). Los "feeds por defecto" de MISP incluyen la mayoría de las fuentes de esta lista, así que una instancia MISP bien configurada es un agregador de feeds en sí misma.

**Limitación**: requiere mantenimiento. Instalar y mantener una instancia MISP no es trivial (necesita servidor dedicado, actualizaciones, curation de feeds).

**Integración SIEM**: MISP tiene módulos de exportación directa para Splunk, QRadar, Elastic, TheHive y prácticamente cualquier plataforma que soporte STIX/TAXII. El módulo `misp-modules` permite enriquecimiento bidireccional.

### 7. CIRCL (Computer Incident Response Center Luxembourg)

[CIRCL](https://www.circl.lu/) opera varios servicios de CTI gratuitos, siendo los más relevantes su instancia MISP pública y los feeds de passive DNS/passive SSL.

| Característica | Detalle |
|---|---|
| **Tipo de datos** | Passive DNS, passive SSL, BGP ranking, feeds MISP |
| **Formato** | API REST, MISP, hashlookup |
| **Frecuencia de actualización** | Continua |
| **Registro** | Necesario para acceso completo |

**Punto fuerte**: el passive DNS. Permite resolver "que dominios apuntaron a esta IP en el pasado" o "a que IPs apunto este dominio históricamente". Fundamental para investigaciones de infraestructura C2.

### 8. PhishTank

[PhishTank](https://phishtank.org/) es una base de datos colaborativa de URLs de phishing verificadas por la comunidad, operada por Cisco Talos.

| Característica | Detalle |
|---|---|
| **Tipo de datos** | URLs de phishing, marca suplantada, estado de verificación |
| **Formato** | CSV, JSON, API REST |
| **Frecuencia de actualización** | Cada hora |
| **Registro** | Necesario para API |

**Punto fuerte**: la verificación comunitaria. Cada URL es revisada y votada por múltiples usuarios antes de marcarse como phishing confirmado. La tasa de falsos positivos es baja.

**Integración SIEM**: el dump completo se descarga como CSV y se ingesta como lista de IOCs. Para correlación en tiempo real, la API permite consultar URLs sospechosas detectadas en logs de proxy.

### 9. GreyNoise Community

[GreyNoise](https://www.greynoise.io/community) analiza el ruido de internet: escaneos masivos, crawlers y actividad de fondo que no es dirigida contra tu organización específicamente.

| Característica | Detalle |
|---|---|
| **Tipo de datos** | IPs que realizan escaneos masivos, clasificación (benigno/malicioso/desconocido) |
| **Formato** | API REST (JSON), STIX/TAXII |
| **Frecuencia de actualización** | Continua |
| **Registro** | Necesario (plan Community gratuito: 50 consultas/día) |

**Punto fuerte**: el uso inverso. En lugar de decirte "esta IP es mala", GreyNoise te dice "esta IP escanea todo internet, así que la alerta que recibiste probablemente no es un ataque dirigido". Esto reduce drásticamente los falsos positivos en tu SIEM: si una IP que dispara una alerta está en GreyNoise como "benign scanner", puedes bajar la prioridad de esa alerta.

**Limitación**: el plan Community tiene un límite de 50 consultas diarias. Para integración continua con SIEM necesitas el plan Enterprise o diseñar un cache local.

### 10. Shodan

[Shodan](https://www.shodan.io/) es el motor de búsqueda de dispositivos conectados a internet. Aunque no es un feed CTI clásico, su valor para threat intelligence es enorme.

| Característica | Detalle |
|---|---|
| **Tipo de datos** | Banners de servicios, puertos abiertos, vulnerabilidades, SSL/TLS, tecnologías |
| **Formato** | API REST (JSON), CLI |
| **Frecuencia de actualización** | Continua (escaneo global permanente) |
| **Registro** | Gratuito (limitado); plan Academic/Developer (49 USD/año) |

**Punto fuerte**: la visión externa de tu superficie de ataque. Shodan te permite buscar "qué ve un atacante de mi organización desde fuera". También puedes monitorizar IPs sospechosas para ver qué servicios exponen.

**Integración SIEM**: la API de Shodan permite enriquecer alertas con datos de la IP de origen (que puertos tiene abiertos, que servicios corre, que CVEs tiene). Esto ayuda a priorizar: una alerta de una IP que expone un servidor Cobalt Strike es más preocupante que una de un servidor web legítimo.

### 11. VirusTotal

[VirusTotal](https://www.virustotal.com/) agrega los resultados de más de 70 motores antivirus y herramientas de análisis de URLs, dominios e IPs.

| Característica | Detalle |
|---|---|
| **Tipo de datos** | Hashes, URLs, dominios, IPs, análisis de ficheros |
| **Formato** | API REST (JSON), GUI web |
| **Frecuencia de actualización** | Continua (cada análisis es público) |
| **Registro** | Gratuito (4 consultas/minuto); API premium para volumen |

**Punto fuerte**: la agregación de motores. Si 40 de 70 antivirus detectan un hash como malicioso, la confianza es alta. Útil para confirmar o descartar IOCs de otras fuentes.

**Limitación**: la API gratuita está muy limitada (4 consultas por minuto, sin búsquedas avanzadas). Para uso operativo en un SOC necesitas la licencia de VT Enterprise.

**Integración SIEM**: enriquecimiento de alertas. Cuando el SIEM detecta un hash sospechoso, una automatización (vía SOAR o script) consulta VT y añade el resultado a la alerta. En Splunk existe el add-on oficial de VirusTotal.

### 12. Emerging Threats (Proofpoint)

[Emerging Threats](https://rules.emergingthreats.net/) pública reglas de detección para Suricata y Snort, además de listas de IPs y dominios comprometidos.

| Característica | Detalle |
|---|---|
| **Tipo de datos** | Reglas IDS (Suricata/Snort), listas de IPs comprometidas, dominios C2 |
| **Formato** | Reglas Suricata/Snort, listas de texto plano |
| **Frecuencia de actualización** | Diaria (reglas OPEN); varias veces al día (PRO, de pago) |
| **Registro** | No necesario para reglas OPEN |

**Punto fuerte**: las reglas de detección listas para usar. Si tu SIEM integra Suricata o Snort como sonda IDS, las reglas de ET son el complemento perfecto. Las reglas OPEN cubren una parte significativa de las amenazas comunes.

### 13. CISA KEV (Known Exploited Vulnerabilities Catalog)

El catálogo [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) del gobierno de EE.UU. lista las vulnerabilidades que se sabe que están siendo explotadas activamente en el mundo real.

| Característica | Detalle |
|---|---|
| **Tipo de datos** | CVEs con evidencia de explotación activa, fecha de detección, fecha límite de remediación |
| **Formato** | JSON, CSV |
| **Frecuencia de actualización** | Varias veces por semana |
| **Registro** | No necesario |

**Punto fuerte**: la curaduria. A diferencia de la base de datos NVD (que lista todas las CVEs), CISA KEV solo incluye las que tienen evidencia confirmada de explotación. Si una vulnerabilidad está en KEV, parcheala ya. Es el feed de priorización de parcheado más fiable que existe.

**Integración SIEM**: cruza el feed KEV con los resultados de tu escáner de vulnerabilidades (Nessus, Qualys, OpenVAS). Las vulnerabilidades que están en KEV y en tu infraestructura son la máxima prioridad.

### 14. CCN-CERT e INCIBE-CERT (feeds españoles)

El [CCN-CERT](https://www.ccn-cert.cni.es/) y el [INCIBE-CERT](https://www.incibe.es/incibe-cert) son los equipos de respuesta nacionales de España.

| Característica | Detalle |
|---|---|
| **Tipo de datos** | Avisos de vulnerabilidades, alertas de campañas activas contra España, IOCs |
| **Formato** | Publicaciones web, correo (suscripción), API MISP (CCN, solo organismos públicos) |
| **Frecuencia de actualización** | Diaria (avisos); inmediata (alertas críticas) |
| **Registro** | SAT-INET/SAT-ICS del CCN requiere ser organismo público o infraestructura crítica. INCIBE es abierto |

**Punto fuerte**: el contexto local. Si operas en España, estos feeds son imprescindibles porque publican alertas específicas sobre campañas dirigidas al mercado español (phishing a bancos españoles, campañas contra AAPP, vulnerabilidades en software de uso común en España).

**Integración SIEM**: los avisos de INCIBE se consumen vía RSS o suscripción de correo. El CCN-CERT ofrece acceso MISP para organismos adheridos al SAT. Para empresas privadas, la suscripción a las alertas de INCIBE y la revisión manual de avisos del CCN es el mínimo.

### 15. DShield / SANS Internet Storm Center

[DShield](https://dshield.org/) es el sistema de detección distribuida del SANS Internet Storm Center (ISC). Agrega datos de firewalls y sensores distribuidos por todo el mundo.

| Característica | Detalle |
|---|---|
| **Tipo de datos** | IPs atacantes (top attackers), puertos atacados (top ports), honeypot data |
| **Formato** | API REST, feeds de texto plano, RSS |
| **Frecuencia de actualización** | Diaria |
| **Registro** | No necesario para consultas básicas |

**Punto fuerte**: la visión macro. DShield te dice "estas son las IPs que están atacando más infraestructura a nivel global ahora mismo". Útil para bloqueos preventivos y para contexto: si una IP que te ataca está en el top 10 de DShield, es un escaneo masivo, no dirigido.

**Mención adicional: Tor Exit Nodes**. La lista de nodos de salida de Tor se pública en `https://check.torproject.org/torbulkexitlist`. No es un feed CTI per se, pero correlacionar tu tráfico con nodos de salida de Tor puede revelar actividad anonimizada sospechosa. Atención: bloquear todo el tráfico de Tor tiene implicaciones de privacidad y no siempre es recomendable.

{{< cta type="tofu" text="Riskitera automatiza el triage, la correlación y el reporting de tu SOC con IA soberana." label="Ver demo SOC" >}}

## ¿Cómo evaluar la calidad de un feed CTI?

No todos los feeds son iguales. Antes de integrar un feed en tu SIEM, evalúalo contra estos criterios:

### Tasa de falsos positivos

Un feed con muchos falsos positivos genera fatiga de alertas y erosiona la confianza del equipo SOC. Mide: de cada 100 IOCs del feed, cuántos resultan ser benignos al investigarlos. Un feed con más del 5% de falsos positivos necesita filtrado adicional o descarte.

### Frecuencia de actualización

Un IOC de hace 6 meses probablemente ya no sea relevante. Los mejores feeds actualizan cada pocos minutos (Abuse.ch, GreyNoise). Los que actualizan semanalmente son útiles para contexto estratégico pero no para detección operativa.

### Contexto proporcionado

Un hash suelto es menos útil que un hash con familia de malware, campaña asociada, TTP (tácticas, técnicas y procedimientos) y kill chain phase. Los feeds que proporcionan contexto (OTX, ThreatFox, CISA KEV) permiten mejor triage que los que solo listan IOCs desnudos.

### Formato y facilidad de integración

Feeds que soportan STIX/TAXII se integran de forma estándar con cualquier TIP o SIEM moderno. Feeds en CSV o texto plano requieren parseo custom. Feeds que solo publican en web (HTML) necesitan scraping, lo que es frágil y propenso a romperse.

### Cobertura y especialización

Ningún feed cubre todo. AlienVault OTX es generalista. Abuse.ch está especializado en malware y botnets. CISA KEV solo cubre vulnerabilidades explotadas. La combinación de feeds especializados proporciona mejor cobertura que un único feed generalista.

### Tabla comparativa

| Feed | Falsos positivos | Actualización | Contexto | Formato | Especialización |
|---|---|---|---|---|---|
| AlienVault OTX | Medio | Continua | Alto | STIX, API, CSV | General |
| Abuse.ch (todos) | Bajo | 5 min | Medio-Alto | CSV, API, STIX | Malware/Botnets |
| MISP/CIRCL | Bajo | Variable | Muy alto | MISP, STIX | General (agregador) |
| PhishTank | Bajo | Horaria | Medio | CSV, API | Phishing |
| GreyNoise | Muy bajo | Continua | Alto | API, STIX | Ruido/Escaneos |
| CISA KEV | Muy bajo | Semanal | Alto | JSON, CSV | Vulnerabilidades |
| Emerging Threats | Bajo | Diaria | Medio | Reglas IDS | Detección IDS |
| DShield | Medio | Diaria | Bajo | Texto, API | IPs atacantes |

## ¿Cómo integrar feeds CTI en tu SIEM?

La integración de feeds en el SIEM sigue un patrón general independiente de la plataforma, con variaciones específicas para cada producto.

### Arquitectura general

El flujo recomendado es:

```
Feeds CTI --> TIP (MISP/OpenCTI) --> SIEM --> Alertas enriquecidas
                                  --> Firewall/WAF (blocklists)
                                  --> EDR (hashes para detección)
```

Usar una Threat Intelligence Platform (TIP) como capa intermedia tiene ventajas:

- **Normalización**: convierte todos los formatos a uno común (STIX 2.1).
- **Deduplicación**: elimina IOCs repetidos entre feeds.
- **Scoring**: asigna una puntuación de confianza a cada IOC basada en cuántas fuentes lo reportan.
- **Envejecimiento (aging)**: reduce automáticamente la relevancia de IOCs antiguos.
- **Distribución**: alimenta SIEM, firewall y EDR desde un punto central.

Si no tienes presupuesto para un TIP comercial, MISP (open source) cumple esta función perfectamente.

### Integración con Splunk

Splunk soporta feeds CTI a través de:

1. **Splunk Enterprise Security (ES)**: incluye el framework de Threat Intelligence nativo. Importa feeds en formato CSV, STIX/TAXII o vía modular inputs. Correlaciona automáticamente IOCs con eventos.
2. **Add-ons específicos**: AlienVault OTX, VirusTotal, Abuse.ch tienen add-ons en Splunkbase.
3. **Lookups manuales**: para feeds en CSV, crea un `lookup` en Splunk y usa `| lookup` en las búsquedas para correlacionar.

```spl
| inputlookup threatintel_iocs.csv
| join type=inner src_ip [search index=firewall action=allowed]
| table _time src_ip dest_ip threat_type confidence
```

### Integración con Elastic Security

En el stack ELK:

1. **Elastic Agent con integración Threat Intelligence**: soporta Abuse.ch, AlienVault OTX, MISP y otros feeds de forma nativa.
2. **Filebeat con modulo ThreatIntel**: ingesta feeds y los almacena en un índice dedicado.
3. **Indicator Match Rules**: reglas de detección que cruzan eventos de logs con IOCs almacenados.

```yaml
# Ejemplo filebeat.yml para Abuse.ch URLhaus
filebeat.modules:
  - module: threatintel
    abuseurl:
      enabled: true
      interval: 10m
```

### Integración con QRadar

IBM QRadar integra feeds CTI a través de:

1. **Pulse**: el marketplace de contenido de QRadar incluye feeds preconfigurados.
2. **Reference Sets**: importa listas de IOCs como Reference Sets y crea reglas que comparan eventos contra esas listas.
3. **STIX/TAXII**: QRadar soporta TAXII 2.0 para importación automática desde TIPs como MISP.

### Integración con Wazuh

Para entornos que usan Wazuh (open source):

1. **CDB Lists**: importa feeds como listas CDB y crea reglas de decodificación que comparan campos de logs contra esas listas.
2. **Integración con MISP**: Wazuh tiene documentación oficial para conectar con MISP vía API.
3. **VirusTotal integration**: modulo nativo de Wazuh para consultar hashes detectados por el FIM.

### Automatización con scripts

Para feeds que no tienen integración nativa, un script de ingesta es la solución:

```python
#!/usr/bin/env python3
"""Ejemplo: descarga IOCs de Abuse.ch URLhaus y los envía al SIEM."""
import requests
import json
from datetime import datetime

URLHAUS_API = "https://urlhaus-api.abuse.ch/v1/urls/recent/limit/100/"

def fetch_urlhaus_recent():
    response = requests.get(URLHAUS_API)
    data = response.json()
    iocs = []
    for entry in data.get("urls", []):
        iocs.append({
            "type": "url",
            "value": entry["url"],
            "threat_type": entry.get("threat", "malware_distribution"),
            "source": "urlhaus",
            "date_added": entry.get("date_added"),
            "tags": entry.get("tags", []),
        })
    return iocs

if __name__ == "__main__":
    iocs = fetch_urlhaus_recent()
    # Aqui: enviar a tu SIEM vía API, syslog o fichero
    print(f"[{datetime.now()}] Descargados {len(iocs)} IOCs de URLhaus")
```

Este patrón se replica para cualquier feed con API REST: descarga, parsea, normaliza, envía al SIEM.

## ¿Cómo evitar sobrecarga de IOCs?

El problema más común al integrar feeds CTI no es la falta de datos, sino el exceso. Un SOC mediano puede acabar con millones de IOCs activos, la mayoría irrelevantes o caducados, generando miles de alertas diarias que nadie investiga.

### Estrategia 1: Scoring de IOCs

Asigna una puntuación de confianza a cada IOC basada en:

- **Número de fuentes** que lo reportan (más fuentes = más confianza).
- **Edad** del IOC (IOCs de más de 30 días pierden relevancia para detección operativa).
- **Contexto** disponible (hash con familia de malware y campaña > hash suelto).
- **Relevancia sectorial** (un IOC de campaña contra banca es más relevante si operas en banca).

Solo alertas para IOCs con puntuación por encima de un umbral. El resto se almacena para enriquecimiento pero no genera alertas activas.

### Estrategia 2: Envejecimiento (aging)

Configura políticas de caducidad:

| Tipo de IOC | Vida útil operativa | Acción al expirar |
|---|---|---|
| IP de C2 | 7 a 30 días | Mover a histórico |
| Dominio de phishing | 14 a 30 días | Mover a histórico |
| Hash de malware | 90 a 180 días | Mantener pero bajar prioridad |
| CVE explotada (KEV) | Hasta que se parchee | Mantener activa |
| URL de distribución | 7 a 14 días | Eliminar |

### Estrategia 3: Whitelist de falsos positivos conocidos

Mantener una lista de IOCs que son falsos positivos recurrentes (CDNs como Cloudflare, servicios de Google, infraestructura de tu propia organización). Antes de alertar, verifica contra la whitelist.

### Estrategia 4: Correlación, no matching simple

Un match simple (la IP de la alerta está en un feed) genera demasiado ruido. La correlación avanzada combina:

- IOC match + comportamiento anómalo (la IP está en un feed Y el tráfico es a un puerto inusual).
- IOC match + contexto de activo (el hash se detecto en un servidor crítico, no en un sandbox).
- Múltiples IOC matches en ventana temporal (la misma fuente aparece en 3 feeds distintos en 24 horas).

### Estrategia 5: Revisar y podar periódicamente

Cada trimestre, revisa:

- Cuantos IOCs activos tiene cada feed.
- Cuantas alertas genera cada feed.
- Cual es la tasa de verdaderos positivos de cada feed.
- Si algun feed ha dejado de actualizarse.

Elimina feeds que no aportan valor. Menos feeds de calidad > más feeds de calidad mediocre.

## ¿Qué feeds recomienda ENISA y el CCN-CERT?

### Recomendaciones del CCN-CERT

El [CCN-CERT](https://www.ccn-cert.cni.es/) opera el Sistema de Alerta Temprana (SAT) que incluye:

- **SAT-INET**: sondas de detección en la red SARA (administraciones públicas). Genera alertas basadas en feeds propios y de partners.
- **SAT-ICS**: similar, para sistemas de control industrial.
- **LUCIA**: plataforma de gestión de incidentes con inteligencia integrada.
- **REYES**: plataforma de threat intelligence del CCN basada en MISP, accesible para organismos adheridos.

Las guías CCN-STIC 817 y 818 recomiendan explícitamente la integración de feeds CTI en los sistemas de detección, priorizando fuentes oficiales (CCN, INCIBE) y fuentes de confianza (Abuse.ch, CISA).

### Recomendaciones de ENISA

La [Agencia de la UE para la Ciberseguridad (ENISA)](https://www.enisa.europa.eu/) pública anualmente el Threat Landscape que identifica las principales amenazas. Sus recomendaciones para feeds CTI incluyen:

- Usar al menos 3 fuentes independientes para reducir el sesgo.
- Priorizar feeds con formato STIX/TAXII para interoperabilidad.
- Participar en ISACs (Information Sharing and Analysis Centers) sectoriales.
- Compartir (no solo consumir) inteligencia, contribuyendo a las plataformas.

### Feeds recomendados para el contexto español

Si operas en España, la combinación mínima recomendada es:

1. **CCN-CERT/SAT** (si eres organismo público o infraestructura crítica).
2. **INCIBE-CERT** (alertas y avisos, acceso libre).
3. **Abuse.ch** (malware y botnets, alta calidad, actualización rápida).
4. **CISA KEV** (priorización de parcheado).
5. **AlienVault OTX o MISP** (agregación y comunidad).

Con estos cinco, cubres el 80% de las necesidades operativas de un SOC.

{{< cta type="mofu" text="Conecta tu SIEM, EDR y feeds CTI en una plataforma que reduce los falsos positivos un 60%." >}}

## ¿Cuándo pasar de feeds gratuitos a pagados?

Los feeds gratuitos son excelentes para empezar y cubren la mayoría de las necesidades operativas. Pero tienen límites. Considera pasar a feeds comerciales cuando:

### Necesitas atribución

Los feeds gratuitos te dicen "esta IP es maliciosa". Los feeds comerciales (Recorded Future, Mandiant, CrowdStrike) te dicen "esta IP pertenece al grupo APT28, que opera desde Rusia y ataca al sector defensa europeo". Si necesitas atribución para tomar decisiones estratégicas o para informar a la dirección, necesitas feeds comerciales.

### Necesitas cobertura de dark web

Los feeds gratuitos cubren la superficie visible de internet. La [monitorización de foros de dark web](/es/posts/2026/04/dark-web-monitoring-empresa/), mercados de credenciales y canales de Telegram donde se venden accesos requiere feeds especializados (Flashpoint, Intel 471, Kela, DarkOwl).

### Tu volumen de consultas supera los límites gratuitos

Cuando tu SOC procesa miles de alertas diarias y necesita enriquecer cada una con datos de VirusTotal, GreyNoise y Shodan, los límites de las APIs gratuitas se quedan cortos. En ese punto, las licencias comerciales de estos mismos servicios son la evolución natural.

### Necesitas SLA y soporte

Los feeds gratuitos no tienen SLA. Si Abuse.ch se cae un martes, no hay a quien llamar. Los feeds comerciales garantizan disponibilidad, soporte técnico y, en muchos casos, un analista asignado.

### Tu sector lo exige

Algunos sectores (banca, defensa, infraestructuras críticas) requieren feeds con certificaciones específicas o acceso a inteligencia clasificada que solo proporcionan proveedores con contratos gubernamentales.

### Modelo híbrido: la mejor opción

La mayoría de los SOC maduros combinan:

- **Feeds gratuitos** para detección operativa (IOCs de malware, phishing, botnets).
- **1 o 2 feeds comerciales** para contexto estratégico (atribución, tendencias, dark web).
- **MISP/OpenCTI** como TIP para agregar, normalizar y distribuir todo.

Este modelo híbrido proporciona la mejor relación coste-efectividad sin depender exclusivamente de fuentes gratuitas.


Si quieres explorar estos feeds de forma visual y buscar IOCs en tiempo real, [MalwareIntel](https://malwareintel.es) es una plataforma gratuita de inteligencia de amenazas que agrega 13 feeds publicos (incluyendo varios de los listados aqui) con busqueda de IOCs, generador de reglas Sigma y Knowledge Graph interactivo.

**Artículos relacionados:**
- [Iocs En Ciberseguridad Que Son](/es/posts/2026/04/iocs-en-ciberseguridad-que-son/)
- [Qué Es Un Siem Para Que Sirve](/es/posts/2026/04/que-es-un-siem-para-que-sirve/)

## Preguntas frecuentes

### ¿Es legal usar feeds CTI gratuitos en una empresa privada?

Sí. Todos los feeds listados en este artículo tienen licencias que permiten su uso en organizaciones privadas, incluyendo uso comercial en la mayoría de los casos. AlienVault OTX, Abuse.ch, CISA KEV y PhishTank son explícitamente gratuitos y abiertos. MISP es software open source bajo licencia AGPL. La única restricción relevante es que algunos feeds del CCN-CERT (como SAT-INET y la plataforma REYES) están limitados a organismos públicos e infraestructuras críticas. Siempre revisa los términos de uso de cada feed, especialmente si vas a redistribuir los datos a terceros.

### ¿Cuántos feeds CTI debería usar mi SOC?

No hay un número mágico, pero la recomendación práctica es entre 5 y 8 feeds activos para un SOC mediano. Menos de 3 feeds deja puntos ciegos significativos. Más de 10 feeds sin una TIP que los gestione genera ruido inmanejable. La clave no es la cantidad sino la combinación: al menos un feed generalista (OTX o MISP), uno o dos especializados en malware (Abuse.ch), uno de vulnerabilidades explotadas (CISA KEV), uno de contexto (GreyNoise) y uno local (CCN-CERT/INCIBE si operas en España). Empieza con pocos, mide el valor que aporta cada uno y añade gradualmente.

### ¿Cómo se que un IOC de un feed gratuito no es un falso positivo?

La regla de oro es la corroboración cruzada: si un IOC aparece en dos o más feeds independientes, la probabilidad de falso positivo baja significativamente. Además, verifica el contexto: un hash reportado en MalwareBazaar con resultados de sandbox que confirman comportamiento malicioso es más fiable que un dominio suelto en un pulso de OTX sin verificación. Herramientas como VirusTotal (para hashes y URLs) y GreyNoise (para IPs) funcionan como segunda opinion. Con el tiempo, construiras una whitelist de falsos positivos recurrentes (CDNs, servicios legítimos, tu propia infraestructura) que filtra automáticamente.

### ¿Puedo integrar feeds CTI sin tener un SIEM?

Sí, aunque con menos automatización. Las opciones son: (1) usar las blocklists directamente en tu firewall o proxy (Feodo Tracker pública listas para pfSense e iptables listas para usar), (2) usar un EDR que soporte importación de IOCs (la mayoría de los EDR modernos permiten subir listas de hashes para bloqueo), (3) usar MISP como TIP standalone para almacenar, correlacionar y buscar IOCs manualmente durante investigaciones. Un SIEM potencia enormemente el valor de los feeds al automatizar la correlación, pero no es un prerrequisito absoluto para empezar a usar threat intelligence.

### ¿Con qué frecuencia debo actualizar los feeds en mi SIEM?

Depende del tipo de feed y de tu capacidad de procesamiento. Los feeds operativos de alta frecuencia (Abuse.ch, OTX) deben actualizarse al menos cada hora, idealmente cada 5 a 15 minutos. Los feeds de contexto (CISA KEV, DShield) pueden actualizarse diariamente. Las reglas IDS de Emerging Threats se actualizan una vez al día. Lo crítico es complementar la actualización con el envejecimiento: de nada sirve actualizar cada 5 minutos si nunca eliminas IOCs obsoletos. Configura un cron job para cada feed con la frecuencia adecuada y una política de aging que elimine IOCs que superan su vida útil operativa.
