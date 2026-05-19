---
title: "Dark Web monitoring: cómo vigilar tu marca sin gastar una fortuna"
image: "cover.png"
description: "Guía práctica de monitorización de la dark web para empresas: qué buscar, herramientas accesibles, fuentes OSINT, alertas automatizadas y cuándo contratar un servicio profesional."
slug: "dark-web-monitoring-empresa"
date: 2026-07-25
publishDate: 2026-07-25
lastmod: 2026-07-25
draft: false
tags: ["CTI", "Threat Intelligence", "OSINT"]
categories: ["CTI"]
author: "David Moya"
keyword: "dark web monitoring empresa"
funnel: "mofu"
---

Guía práctica de monitorización de la dark web para empresas: qué buscar, herramientas accesibles, fuentes OSINT, alertas automatizadas y cuándo contratar un servicio profesional.

<!--more-->

{{< key-takeaways >}}
- La dark web es un ecosistema donde se comercian credenciales robadas, datos corporativos filtrados y accesos iniciales a redes empresariales. Monitorizar estos espacios no es opcional para empresas con activos digitales relevantes.
- Existen herramientas gratuitas (Have I Been Pwned, IntelX, Dehashed) que permiten arrancar un programa básico de vigilancia sin inversión inicial.
- Las plataformas profesionales (Recorded Future, Flashpoint, SpiderFoot) ofrecen cobertura automatizada de foros, mercados y canales de Telegram donde se negocian datos corporativos.
- En España, acceder a la dark web es legal siempre que no se participe en actividades ilícitas. El marco normativo (RGPD, LSSI, NIS2) exige protección proactiva de datos.
- Integrar las alertas de dark web monitoring en el flujo de trabajo del SOC es imprescindible para que la inteligencia se traduzca en acciones concretas y tiempos de respuesta medibles.
{{< /key-takeaways >}}

## ¿Qué es la monitorización de la dark web y por qué importa en 2026?

La dark web es la porción de internet que no está indexada por buscadores convencionales y requiere software específico (normalmente [Tor](https://www.torproject.org/)) para acceder. Dentro de este ecosistema operan foros de hacking, mercados de datos robados, servicios de malware-as-a-service y canales de comunicación cifrada donde actores maliciosos negocian accesos corporativos.

El dark web monitoring consiste en vigilar de forma sistemática estos espacios para detectar menciones a tu organización, tus dominios, tus empleados o tus activos digitales antes de que un incidente se materialice. No se trata de navegar por la dark web de forma artesanal. Se trata de implementar procesos y herramientas que automaticen la detección y generen alertas accionables.

Según el informe [Data Breach Investigations Report de Verizon](https://www.verizon.com/business/resources/reports/dbir/), el 86% de las brechas involucran credenciales robadas. Muchas de esas credenciales aparecen en la dark web semanas o meses antes de que se utilicen en un ataque. Esa ventana temporal es exactamente lo que el monitoring te permite aprovechar.

En 2026 el panorama se ha intensificado. Los initial access brokers (IABs) venden accesos VPN y RDP corporativos en subastas con precios que van desde 500 hasta 50.000 euros dependiendo del tamaño y sector de la víctima. Los infostealers como Lumma, Raccoon y RedLine extraen cookies de sesión, credenciales almacenadas en navegadores y tokens de autenticación de forma masiva. El volumen de datos filtrados crece cada trimestre.

### El coste de no monitorizar

Para una pyme española, el coste medio de una brecha de datos ronda los 100.000 euros entre respuesta al incidente, notificación AEPD, daño reputacional y posibles sanciones. Para una empresa mediana con datos regulados (salud, financiero, infraestructuras críticas), la cifra se multiplica. El dark web monitoring funciona como un sistema de alerta temprana que reduce el tiempo de detección de días o semanas a horas.

## Credenciales, datos filtrados y menciones: qué monitorizar en la dark web

No basta con "vigilar la dark web" de forma genérica. Necesitas definir qué activos monitorizar y qué tipo de amenazas son relevantes para tu organización. Estos son los cinco vectores principales.

### 1. Filtraciones de credenciales

Es el caso de uso más común y el que ofrece resultados más inmediatos. Debes buscar:

- **Credenciales corporativas filtradas:** combinaciones de email/contraseña de tus dominios que aparecen en dumps o combolists. Un solo par de credenciales válidas puede ser la puerta de entrada a tu red.
- **Credenciales de servicios SaaS:** cuentas de empleados en plataformas como Slack, Jira, GitHub, Office 365. Los actores maliciosos saben que muchas organizaciones no implementan MFA en todas sus herramientas.
- **Cookies de sesión y tokens:** los infostealers modernos no solo roban contraseñas. Extraen cookies de sesión activas que permiten bypass completo de MFA. Si un token de sesión de tu VPN corporativa aparece en un log de infostealer, tienes un problema crítico.
- **Credenciales de acceso remoto:** VPN, RDP, Citrix, SSH. Los IABs las venden como paquetes de "acceso inicial" en foros especializados.

### 2. Data dumps y bases de datos filtradas

Más allá de credenciales individuales, debes vigilar la aparición de:

- Bases de datos de clientes con información personal (PII)
- Documentos internos, contratos, información financiera
- Código fuente de aplicaciones propietarias
- Backups de servidores o bases de datos completas
- Datos de tarjetas de pago si operas en ecommerce

Los actores de ransomware practican la doble extorsión: cifran los datos y además los publican (o amenazan con publicarlos) en sus sitios de leaks. Monitorizar estos sitios es parte fundamental del dark web monitoring.

### 3. Menciones de marca y dominio

Tu organización puede aparecer mencionada en la dark web en contextos como:

- Discusiones sobre vulnerabilidades en tus sistemas
- Planificación de ataques dirigidos (targeted attacks)
- Listados de empresas vulnerables a un CVE específico
- Ofertas de venta de accesos a tu infraestructura
- Reclamaciones de ataques por parte de grupos de ransomware

### 4. Targeting de ejecutivos y empleados clave

Los ataques de spear phishing y business email compromise (BEC) frecuentemente comienzan con reconocimiento en la dark web. Debes vigilar:

- Datos personales de ejecutivos C-level (CEO, CFO, CTO)
- Información utilizada para ataques de ingeniería social (teléfonos, direcciones, rutinas)
- Cuentas personales de correo de empleados que reutilizan contraseñas corporativas
- Perfiles en foros o redes sociales que puedan vincular a empleados con la organización

### 5. Domain typosquatting y phishing infrastructure

Los atacantes registran dominios similares al tuyo para campañas de phishing. Debes monitorizar:

- Dominios con errores tipográficos de tu marca (ej. riskltera.com, riskitera.net)
- Certificados SSL emitidos para dominios similares al tuyo (Certificate Transparency logs)
- Paginas de phishing que imitan tu portal de login o tu web corporativa
- Kits de phishing a la venta que incluyan plantillas de tu organización

## Herramientas gratuitas para empezar hoy mismo

No necesitas un presupuesto de seis cifras para iniciar un programa básico de dark web monitoring. Estas herramientas permiten cubrir los vectores principales sin coste.

### Have I Been Pwned (HIBP)

[Have I Been Pwned](https://haveibeenpwned.com/) es la referencia para verificar si direcciones de correo han aparecido en brechas de datos conocidas. Su funcionalidad clave para empresas es la **Domain Search**, que permite monitorizar todas las direcciones de un dominio corporativo.

**¿Cómo usarla:**

1. Registra tu dominio en HIBP verificando propiedad vía DNS TXT record o email
2. Activa las notificaciones para recibir alertas cuando aparezcan nuevas brechas
3. Revisa el listado inicial de brechas que afectan a cuentas de tu dominio
4. Para cada brecha, identifica qué datos se expusieron (contraseñas, hashes, datos personales)

**Limitaciones:** HIBP solo cubre brechas que se hacen públicas y que Troy Hunt incorpora a la base de datos. No cubre datos vendidos en privado ni filtraciones recientes que aún no se hayan difundido ampliamente.

**Consejo práctico:** configura HIBP como tu primera línea de defensa. Es gratuita, fiable y requiere minutos de setup. Combinarla con rotación forzada de credenciales ante cada alerta convierte una herramienta sencilla en un control efectivo.

### IntelX (Intelligence X)

[IntelX](https://intelx.io/) es un motor de búsqueda que indexa contenido de la dark web, data leaks, dominios, emails, URLs y otros indicadores. Su tier gratuito permite realizar búsquedas limitadas con resultados parciales.

**¿Cómo usarla:**

1. Busca tu dominio corporativo para ver qué datos aparecen indexados
2. Busca direcciones de email de ejecutivos y empleados críticos
3. Revisa los resultados por tipo de fuente (paste sites, leaks, dark web)
4. Documenta hallazgos y prioriza por criticidad

**Tier gratuito vs de pago:** la versión gratuita muestra resultados truncados y limita el número de búsquedas diarias. Para un uso operativo serio necesitarás el plan profesional, pero la versión gratuita es suficiente para evaluaciones puntuales y para decidir si la herramienta aporta valor a tu organización.

### Dehashed

[Dehashed](https://www.dehashed.com/) permite buscar en bases de datos filtradas por email, nombre de usuario, IP, teléfono o nombre. Su tier gratuito ofrece búsquedas básicas con resultados limitados.

**¿Cómo usarla:**

1. Busca tu dominio para ver cuántas credenciales filtradas existen
2. Busca nombres de empleados clave para detectar reutilización de credenciales
3. Cruza resultados con tu directorio activo para identificar cuentas activas comprometidas
4. Prioriza el reseteo de credenciales que aún estén en uso

**Importante:** Dehashed contiene datos sensibles. Usala exclusivamente para proteger tu propia organización y documenta el propósito legítimo de cada consulta.

### Herramientas complementarias gratuitas

- **[Shodan](https://www.shodan.io/):** busca dispositivos y servicios expuestos de tu organización. No es dark web en sentido estricto, pero complementa la superficie de ataque.
- **[crt.sh](https://crt.sh/):** consulta Certificate Transparency logs para detectar dominios similares al tuyo con certificados SSL emitidos recientemente.
- **[PhishTank](https://phishtank.org/):** base de datos colaborativa de URLs de phishing. Busca si hay campañas activas que usen tu marca.
- **Google Alerts:** configura alertas para variaciones de tu nombre de dominio y marca. Sencillo pero efectivo para detectar typosquatting en la surface web.

## Plataformas profesionales de dark web monitoring

Cuando el volumen de activos a monitorizar crece o la organización opera en un sector regulado, las herramientas gratuitas se quedan cortas. Estas son las principales plataformas profesionales.

### Recorded Future

[Recorded Future](https://www.recordedfuture.com/) es una de las plataformas de threat intelligence más completas del mercado. Su módulo de dark web monitoring cubre:

- Indexación automatizada de foros, mercados y canales de Telegram
- Detección de credenciales filtradas con contexto (fuente, fecha, tipo de brecha)
- Alertas en tiempo real sobre menciones de marca y dominio
- Integración nativa con SIEMs (Splunk, QRadar, Sentinel)
- Análisis de actores de amenaza con perfiles enriquecidos

**Ideal para:** empresas medianas y grandes con SOC interno o MSSP contratado. El coste es significativo (decenas de miles de euros anuales), pero la cobertura y la integración justifican la inversión en sectores como banca, salud o infraestructuras críticas.

### Flashpoint

[Flashpoint](https://flashpoint.io/) se especializa en inteligencia sobre actores de amenaza y análisis de la dark web en profundidad. Sus fortalezas:

- Cobertura de foros cerrados y comunidades de habla rusa, china y árabe
- Análisis de intenciones y capacidades de actores de amenaza
- Detección de campañas de fraude y venta de datos
- Reporting adaptado a audiencias ejecutivas y técnicas
- Contextualización geopolítica de amenazas

**Ideal para:** organizaciones con programas de CTI maduros que necesitan inteligencia contextualizada, no solo alertas. Flashpoint es particularmente fuerte en el análisis de amenazas procedentes de actores estatales y grupos de crimen organizado.

### SpiderFoot

[SpiderFoot](https://www.spiderfoot.net/) es una plataforma de OSINT con una versión open source (SpiderFoot HX) y una versión cloud. Su enfoque es la automatización del reconocimiento:

- Más de 200 módulos de recopilación de datos
- Correlación automática entre fuentes (dark web, DNS, redes sociales, brechas)
- Visualización gráfica de relaciones entre entidades
- Versión open source desplegable en tu propia infraestructura

**Ideal para:** equipos técnicos que quieren control total sobre sus herramientas y prefieren self-hosting. La versión open source es gratuita y potente, aunque requiere mantenimiento y conocimiento técnico para sacarle partido.

### Comparativa rápida

| Criterio | Recorded Future | Flashpoint | SpiderFoot |
|---|---|---|---|
| Cobertura dark web | Muy alta | Alta (foros cerrados) | Media-alta |
| Facilidad de uso | Alta | Media | Baja (técnica) |
| Integración SIEM | Nativa | Nativa | Via API |
| Coste anual aprox. | 50k-150k EUR | 40k-120k EUR | Gratis (OSS) / 5k-20k EUR (cloud) |
| Self-hosting | No | No | Si (versión OSS) |
| Ideal para | SOC con SIEM | CTI team maduro | Equipos técnicos |

## Consideraciones legales en España

Uno de los temas que más dudas genera es la legalidad de acceder a la dark web con propósitos de monitoring. La respuesta corta: es legal, con matices importantes.

### Marco normativo aplicable

**Acceso a la dark web:** en España no existe ninguna ley que prohiba acceder a la red Tor ni navegar por la dark web. Lo que es ilegal son las actividades que puedas realizar allí (comprar datos robados, contratar servicios de hacking, adquirir malware).

**[RGPD](https://www.aepd.es/reglamento/reglamento.html) y protección de datos:** si durante el monitoring encuentras datos personales de terceros (empleados de otras empresas, clientes), debes tratarlos conforme al RGPD. Esto incluye minimización de datos, propósito legítimo documentado y eliminación cuando ya no sean necesarios.

**[LSSI-CE](https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758):** la Ley de Servicios de la Sociedad de la Información establece obligaciones sobre comunicaciones electrónicas. Si detectas phishing que suplanta tu marca, tienes legitimidad para actuar (takedown requests).

**[NIS2](https://www.enisa.europa.eu/):** la Directiva NIS2, aplicable desde octubre de 2024, exige a entidades esenciales e importantes medidas de gestión de riesgos de ciberseguridad. El dark web monitoring es una práctica razonable dentro de esas medidas. [ENISA](https://www.enisa.europa.eu/) recomienda explícitamente la monitorización de amenazas como parte de la postura de seguridad.

**[INCIBE](https://www.incibe.es/)** (Instituto Nacional de Ciberseguridad) proporciona guías y recursos para empresas españolas sobre cómo gestionar incidentes y implementar medidas de ciberseguridad, incluyendo la monitorización de amenazas.

### Buenas prácticas legales

1. **Documenta el propósito:** mantén un registro escrito de por qué monitorizas la dark web, qué activos vigilas y quién autoriza las búsquedas.
2. **No interactues con actores maliciosos:** observa, documenta, pero no compres datos, no participes en foros simulando ser un ciberdelincuente, no contactes vendedores.
3. **Notifica hallazgos relevantes:** si encuentras datos de otras organizaciones, valora notificarlas. Si encuentras evidencia de delitos graves, considera comunicarlo a las FCSE (Fuerzas y Cuerpos de Seguridad del Estado) o al INCIBE-CERT.
4. **Consulta con asesoria jurídica:** si operas en sectores regulados (banca, salud, infraestructuras críticas), involucra al departamento legal antes de iniciar un programa de monitoring.

## Integración del dark web monitoring con el flujo SOC

La información de la dark web solo tiene valor si se integra en los procesos operativos de seguridad. Detectar una filtración y no actuar es peor que no haberla detectado, porque genera una falsa sensación de seguridad.

### Flujo de trabajo recomendado

**Fase 1: Recopilación (Collection)**

- Configura las herramientas elegidas (gratuitas o profesionales) con los activos a monitorizar
- Define frecuencia de escaneo: credenciales (diaria), menciones de marca (diaria), data dumps (continúa si la herramienta lo permite)
- Centraliza las alertas en un canal único (email, Slack, SIEM)

**Fase 2: Triaje (Triage)**

- Clasifica cada alerta por criticidad:
  - **Crítica:** credenciales activas de cuentas con privilegios, accesos VPN/RDP a la venta, datos de clientes filtrados
  - **Alta:** credenciales de empleados en brechas recientes, menciones de vulnerabilidades específicas
  - **Media:** credenciales antiguas (más de 6 meses), menciones genéricas de la marca
  - **Baja:** datos ya conocidos de brechas históricas, falsos positivos
- Asigna propietario para cada alerta crítica y alta

**Fase 3: Respuesta (Response)**

- **Credenciales filtradas:** forzar reseteo inmediato, revocar sesiones activas, verificar accesos no autorizados en logs
- **Datos corporativos:** evaluar alcance, activar protocolo de brecha de datos, notificar a AEPD si aplica RGPD
- **Dominios typosquatting:** solicitar takedown al registrador, bloquear en proxy/firewall, alertar a empleados
- **Accesos a la venta:** investigar si el acceso es real, parchear vector de entrada, monitorizar actividad sospechosa

**Fase 4: Feedback (Lessons Learned)**

- Documenta cada incidente y la respuesta aplicada
- Actualiza la lista de activos monitorizados con nuevos dominios, cuentas o ejecutivos
- Ajusta umbrales de alerta para reducir falsos positivos
- Reporta métricas al CISO/DPO: alertas recibidas, tiempo medio de respuesta, credenciales comprometidas neutralizadas

{{< cta type="tofu" text="Riskitera integra dark web monitoring con tu SOC y automatiza el triage de alertas con IA soberana. Sin datos saliendo de Europa." label="Ver cómo funciona" >}}

### Métricas clave para medir la efectividad

| Métrica | Objetivo recomendado |
|---|---|
| Tiempo de detección (filtración a alerta) | < 24 horas |
| Tiempo de respuesta (alerta a acción) | < 4 horas (críticas), < 24h (altas) |
| Credenciales comprometidas reseteadas | 100% en < 48h |
| Falsos positivos | < 20% del total de alertas |
| Dominios typosquatting detectados/bloqueados | Ratio > 90% |

## ¿Cómo configurar alertas automatizadas paso a paso?

Un sistema de alertas bien configurado es la diferencia entre un programa reactivo y uno proactivo. Aquí tienes un plan de implementación progresivo.

### Nivel 1: Alertas básicas (semana 1)

1. **Registra tu dominio en Have I Been Pwned.** Verifica propiedad y activa notificaciones por email.
2. **Configura Google Alerts** para tu nombre de dominio, nombre de empresa y variaciones comunes con errores tipográficos.
3. **Revisa crt.sh semanalmente** buscando certificados nuevos emitidos para dominios similares al tuyo.
4. **Crea una búsqueda guardada en IntelX** (tier gratuito) para tu dominio principal.

### Nivel 2: Alertas intermedias (semana 2-4)

1. **Automatiza consultas con scripts:** crea un script en Python que consulte las APIs gratuitas de HIBP y crt.sh, y envie resultados a un canal de Slack o email.
2. **Integra con tu SIEM:** si usas Splunk, QRadar o Sentinel, configura feeds de threat intelligence que incluyan IoCs de la dark web.
3. **Monitoriza paste sites:** configura alertas en servicios como Pastebin o GitHub para detectar datos de tu organización publicados en texto plano.

### Nivel 3: Alertas avanzadas (mes 2-3)

1. **Despliega SpiderFoot en tu infraestructura** para escaneos automatizados y profundos.
2. **Contrata una plataforma profesional** si el volumen de alertas o la criticidad de tus activos lo justifica.
3. **Integra con playbooks de respuesta automática:** ante una alerta crítica (credenciales con privilegios), ejecuta automáticamente el reseteo de contraseña y la revocación de sesiones vía tu IdP (Okta, Azure AD, Google Workspace).

### Ejemplo de script básico de alertas

```python
import requests
import json
from datetime import datetime

# Consulta HIBP para un dominio (requiere API key)
def check_hibp_domain(domain, api_key):
    url = f"https://haveibeenpwned.com/api/v3/breaches"
    headers = {"hibp-api-key": api_key}
    response = requests.get(url, headers=headers)
    breaches = response.json()
    # Filtrar brechas que afectan a cuentas del dominio
    relevant = [b for b in breaches if domain in str(b.get("Domain", ""))]
    return relevant

# Consulta crt.sh para certificados nuevos
def check_crtsh(domain):
    url = f"https://crt.sh/?q=%25{domain}%25&output=json"
    response = requests.get(url)
    certs = response.json()
    # Filtrar últimos 7 días
    recent = [c for c in certs if "2026" in c.get("entry_timestamp", "")]
    return recent

# Enviar alerta a Slack
def send_slack_alert(webhook_url, message):
    payload = {"text": message}
    requests.post(webhook_url, json=payload)
```

Este es un ejemplo simplificado. En un entorno productivo necesitarás manejo de errores, rate limiting, almacenamiento de resultados previos para evitar alertas duplicadas, y autenticación adecuada.

## Fuentes OSINT más útiles para dark web monitoring

Más allá de las herramientas ya mencionadas, estas fuentes OSINT complementan un programa de monitoring completo.

### Feeds de indicadores de compromiso (IoCs)

- **[Abuse.ch](https://abuse.ch/):** feeds gratuitos de malware (MalwareBazaar), URLs maliciosas (URLhaus) y botnets (Feodo Tracker). Imprescindible para correlacionar actividad de la dark web con infraestructura de ataque.
- **[AlienVault OTX](https://otx.alienvault.com/):** plataforma colaborativa de threat intelligence con pulsos que incluyen IoCs de la dark web.
- **[MISP Feeds](https://www.misp-project.org/):** la plataforma MISP ofrece feeds compartidos por comunidades de seguridad que incluyen datos de la dark web.

### Monitores de ransomware

- **Ransomwatch:** proyecto que monitoriza sitios de leaks de grupos de ransomware. Permite detectar si tu organización aparece como víctima antes de que los datos se publiquen completamente.
- **DarkFeed de DarkTracer:** feed de actividad de ransomware en la dark web.

### Canales de Telegram

Muchos actores de amenaza han migrado de foros tradicionales a canales de Telegram para la venta de credenciales, accesos y datos. Monitorizar estos canales requiere precaución legal y operativa, pero es una fuente de inteligencia cada vez más relevante.

### Foros y mercados

Los foros como BreachForums (y sus sucesores) y los mercados de la dark web son las fuentes primarias. Acceder directamente requiere experiencia, precauciones operativas (Tails OS, VPN sobre Tor, identidades separadas) y conlleva riesgos. Para la mayoría de empresas, es preferible usar plataformas que indexen estos foros automáticamente.

## ¿Cuándo contratar un servicio profesional de dark web monitoring?

No todas las empresas necesitan una plataforma profesional desde el primer día. Usa esta guía para decidir.

### Puedes empezar con herramientas gratuitas si:

- Tu organización tiene menos de 200 empleados
- No operas en un sector regulado (banca, salud, infraestructuras críticas)
- Tu superficie de ataque digital es limitada (pocos dominios, pocas aplicaciones públicas)
- Tienes personal técnico capaz de gestionar alertas manualmente
- Tu presupuesto de seguridad es limitado y necesitas demostrar valor antes de invertir

### Necesitas un servicio profesional si:

- Operas en un sector regulado donde NIS2 o DORA exigen medidas de monitoring
- Has sufrido una brecha y necesitas visibilidad inmediata de tus datos en la dark web
- Tu organización tiene más de 500 empleados y múltiples dominios
- Tu SOC necesita integración automatizada con el SIEM para reducir tiempos de respuesta
- Los ejecutivos C-level son objetivos potenciales (sector financiero, defensa, tecnología)
- Necesitas reporting ejecutivo periódico para el consejo de administración o el comité de riesgos

### Modelo híbrido (recomendado)

La mejor estrategia para la mayoría de empresas medianas es un modelo híbrido:

1. **Herramientas gratuitas** para monitoring continuo básico (HIBP, crt.sh, Google Alerts)
2. **SpiderFoot OSS** para reconocimiento periódico automatizado (semanal o quincenal)
3. **Plataforma profesional** para los activos más críticos (cuentas de ejecutivos, dominios principales, datos de clientes)

Este enfoque permite cubrir la superficie de ataque sin sobredimensionar la inversión.

## Protocolo de respuesta ante filtraciones detectadas en dark web

Encontrar datos de tu organización en la dark web no es cuestión de si, sino de cuándo. Lo importante es tener un protocolo claro de respuesta.

### Protocolo de respuesta inmediata

**Paso 1: Verificación (primeros 30 minutos)**

- Confirma que los datos son reales y pertenecen a tu organización
- Determina la antiguedad de la filtración (reciente vs histórica)
- Evalúa la sensibilidad de los datos expuestos
- Identifica la fuente probable (brecha en tercero, ataque directo, insider)

**Paso 2: Contención (primeras 4 horas)**

- Reseta credenciales comprometidas y revoca sesiones activas
- Bloquea accesos desde IPs sospechosas identificadas en la filtración
- Activa monitoreo reforzado en los sistemas afectados
- Si hay dominios typosquatting, añade los a las listas de bloqueo

**Paso 3: Investigación (primeras 24-72 horas)**

- Analiza los logs para determinar si las credenciales filtradas ya se utilizaron
- Busca movimientos laterales o accesos no autorizados
- Evalua si la filtración afecta a datos de clientes (obligación RGPD)
- Documenta la cadena de custodia si los datos podrían ser evidencia

**Paso 4: Notificación (si aplica)**

- **AEPD:** si hay datos personales afectados, notificación en las primeras 72 horas según RGPD
- **INCIBE-CERT:** si eres operador de servicios esenciales o infraestructura crítica
- **Clientes afectados:** si sus datos personales están comprometidos, notificación obligatoria
- **Aseguradora cyber:** si tienes póliza de ciberseguro, notifica para activar cobertura

**Paso 5: Remediación y mejora (semana siguiente)**

- Implementa controles para evitar que se repita (MFA universal, políticas de contraseñas más estrictas)
- Actualiza tu programa de monitoring con los nuevos indicadores descubiertos
- Realiza un post-mortem documentado
- Reporta al comité de dirección con lecciones aprendidas y recomendaciones

{{< cta type="bofu" text="Riskitera automatiza el protocolo de respuesta ante filtraciones en la dark web. Empieza tu PoC de 90 dias." label="Iniciar PoC" >}}

## Errores comunes en dark web monitoring

Después de trabajar con múltiples organizaciones en programas de CTI, estos son los errores que vemos con más frecuencia:

1. **Monitorizar sin plan de respuesta.** De nada sirve detectar una filtración si nadie sabe qué hacer con la alerta. Define el playbook antes de activar las herramientas.
2. **Centrarse solo en credenciales.** Las credenciales son importantes, pero ignorar menciones de marca, planificación de ataques o infraestructura de phishing deja ángulos muertos críticos.
3. **No actualizar los activos monitorizados.** Las empresas adquieren dominios, lanzan productos, contratan empleados. Si la lista de activos no se actualiza trimestralmente, el monitoring se queda obsoleto.
4. **Confundir acceso con actividad ilegal.** Acceder a la dark web para monitoring es legal. Participar en transacciones o simular ser un actor malicioso cruza la línea. Forma a tu equipo.
5. **No medir resultados.** Si no mides tiempo de detección, tiempo de respuesta y credenciales neutralizadas, no puedes demostrar el valor del programa ni justificar presupuesto.


**Artículos relacionados:**
- [Iocs En Ciberseguridad Que Son](/es/posts/2026/04/iocs-en-ciberseguridad-que-son/)
- [Threat Hunting Guía Practica](/es/posts/2026/04/threat-hunting-guia-practica/)

## Preguntas frecuentes

### ¿Es legal acceder a la dark web en España?

Sí. Acceder a la dark web mediante Tor u otras redes anónimas es completamente legal en España. Lo que está prohibido son las actividades ilícitas que puedas realizar allí: comprar datos robados, contratar servicios de hacking, adquirir malware o participar en mercados ilegales. Para dark web monitoring con fines defensivos, documenta el propósito legítimo y evita cualquier interacción con actores maliciosos.

### ¿Cuánto cuesta implementar dark web monitoring en una pyme?

Puedes empezar a coste cero con herramientas gratuitas (Have I Been Pwned, IntelX free tier, crt.sh, Google Alerts). Un programa básico pero efectivo se puede montar en menos de una semana con estas herramientas. Si necesitas una plataforma profesional, los costes arrancan en 5.000 euros anuales (SpiderFoot cloud) y pueden superar los 100.000 euros para soluciones enterprise como Recorded Future o Flashpoint. La recomendación es empezar gratis, demostrar valor, y escalar la inversión conforme la organización lo necesite.

### ¿Qué hago si encuentro credenciales de mi empresa en la dark web?

Lo primero es verificar que son reales y determinar su antiguedad. Si son credenciales activas, fuerza el reseteo inmediato y revoca todas las sesiones activas de las cuentas afectadas. Verifica en los logs si ya se han utilizado para accesos no autorizados. Si los datos incluyen información personal de clientes, evalúa la obligación de notificar a la AEPD en las primeras 72 horas. Documenta todo el proceso de respuesta para el post-mortem.

### ¿Con qué frecuencia debo revisar las alertas de dark web monitoring?

Las alertas críticas (credenciales activas, accesos a la venta, datos de clientes) deben revisarse en tiempo real o con un SLA máximo de 4 horas. Las alertas de prioridad media y baja pueden revisarse diariamente. La lista de activos monitorizados debe actualizarse al menos cada trimestre. El reporting ejecutivo debe ser mensual o trimestral dependiendo del nivel de madurez del programa y las exigencias regulatorias.

### ¿Puedo hacer dark web monitoring sin un SOC dedicado?

Sí, especialmente en la fase inicial. Un equipo de IT con formación básica en ciberseguridad puede gestionar un programa de monitoring con herramientas gratuitas. La clave es tener un playbook de respuesta claro para cada tipo de alerta. Conforme el volumen de alertas crece o si operas en sectores regulados, necesitarás un SOC (interno o externalizado como servicio MSSP) para mantener tiempos de respuesta aceptables.
