---
title: "Respuesta a incidentes de seguridad: playbook completo para equipos SOC"
description: "Playbook completo de respuesta a incidentes para SOC: fases NIST, roles, comunicación, contención, erradicación, recuperación y lecciones aprendidas con ejemplos prácticos."
slug: "respuesta-incidentes-seguridad-playbook"
date: 2026-07-02
publishDate: 2026-07-02
lastmod: 2026-07-02
draft: false
tags: ["SOC", "Operaciones", "Seguridad"]
categories: ["SOC"]
author: "David Moya"
keyword: "respuesta incidentes seguridad"
funnel: "mofu"
---

Playbook completo de respuesta a incidentes para SOC: fases NIST, roles, comunicación, contención, erradicación, recuperación y lecciones aprendidas con ejemplos prácticos.

<!--more-->

{{< key-takeaways >}}
- El framework NIST SP 800-61 estructura la respuesta a incidentes en 4 fases: preparación, detección y análisis, contención/erradicación/recuperación, y actividad post-incidente
- Cada tipo de incidente (ransomware, phishing, data breach, DDoS) requiere un playbook específico con criterios de detección, pasos de contención y procedimientos de recuperación propios
- Los roles del equipo de respuesta deben estar definidos antes del incidente, con un Incident Commander que coordine todas las acciones
- La documentación durante el incidente y el análisis post-mortem son tan importantes como la contención técnica
- Frameworks como MITRE ATT&CK y guías de CCN-CERT e INCIBE proporcionan taxonomías y procedimientos estandarizados para equipos SOC en España
{{< /key-takeaways >}}

## Qué es un plan de respuesta a incidentes

Un plan de respuesta a incidentes (Incident Response Plan, IRP) es el documento que define como una organización detecta, contiene, erradica y se recupera de un incidente de ciberseguridad. No es un documento teórico: es un manual operativo que el equipo SOC sigue bajo presión, cuando los sistemas están caidos y la dirección exige respuestas.

La referencia principal para construir un IRP es el [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) (Computer Security Incident Handling Guide), publicado por el National Institute of Standards and Technology. En el contexto español, el [CCN-CERT](https://www.ccn-cert.cni.es/) pública guías complementarias adaptadas al Esquema Nacional de Seguridad (ENS), y el [INCIBE](https://www.incibe.es/) ofrece recursos para el sector privado y las pymes.

### Por que necesitas un playbook, no solo un plan

Un plan de respuesta general describe el "que". Los playbooks describen el "como" para cada tipo de incidente concreto. Un SOC efectivo tiene ambos:

- **Plan general (IRP):** Roles, cadena de comunicación, criterios de escalado, umbrales de severidad.
- **Playbooks específicos:** Procedimientos paso a paso para ransomware, phishing, data breach, DDoS, compromiso de credenciales, etc.

La diferencia entre un equipo que responde en 30 minutos y uno que tarda 8 horas no suele ser técnica. Es la diferencia entre tener un playbook probado y tener que improvisar.

## Las 4 fases de respuesta a incidentes según NIST SP 800-61

El framework NIST organiza la respuesta en cuatro fases. No son secuenciales en la práctica (se solapan y se iteran), pero proporcionan la estructura necesaria para no perder el control.

### Fase 1: Preparación

La preparación ocurre antes del incidente. Es la fase más importante y la más ignorada. Incluye:

**Herramientas y capacidades:**
- SIEM configurado con reglas de detección actualizadas
- EDR/XDR desplegado en todos los endpoints
- Plataforma de ticketing para incidentes (no sirve un Excel)
- Herramientas forenses: adquisición de imagenes, análisis de memoria, PCAP
- Canales de comunicación alternativos (si el correo está comprometido, como os comunicais?)

**Documentación:**
- Inventario de activos actualizado (no puedes proteger lo que no conoces)
- Diagramas de red con segmentación real (no la teorica)
- Lista de contactos de emergencia: equipo IR, legal, CISO, comunicación, proveedores críticos
- Contratos con proveedores de IR externos (retainers) para escalado

**Entrenamiento:**
- Tabletop exercises trimestrales con escenarios realistas
- Simulacros técnicos (red team / purple team) semestrales
- Formación específica para cada rol del equipo de respuesta

**Inteligencia:**
- Feeds de threat intelligence activos (MISP, OTX, feeds sectoriales)
- Mapeo de [MITRE ATT&CK](https://attack.mitre.org/) para las técnicas más relevantes del sector
- Seguimiento de grupos APT que atacan tu sector o geografia

### Fase 2: Detección y análisis

Esta es la fase donde la mayoría de los SOC viven día a día. El objetivo es identificar qué un incidente está ocurriendo, determinar su alcance y asignarle severidad.

**Fuentes de detección:**

| Fuente | Tipo de alerta | Ejemplo |
|--------|---------------|---------|
| SIEM | Correlación de eventos | Login desde IP anomala + escalada de privilegios |
| EDR | Comportamiento en endpoint | Proceso svchost.exe ejecutando PowerShell codificado |
| IDS/IPS | Firmas y anomalías de red | Trafico C2 a dominio conocido |
| Threat Intelligence | IOCs coincidentes | Hash de fichero en feed de malware activo |
| Usuarios | Reporte manual | "Mi equipo actúa raro" o "He recibido un correo sospechoso" |
| Honeypots | Acceso a recurso trampa | Lectura de archivo canary en servidor de ficheros |

**Proceso de triage:**

1. **Verificación:** Confirmar que la alerta no es un falso positivo. Correlacionar con fuentes adicionales.
2. **Clasificación:** Asignar tipo (ransomware, phishing, intrusión, data breach, DDoS, otro).
3. **Severidad:** Usar una escala predefinida (P1-P4) basada en impacto y urgencia.
4. **Asignación:** Designar Incident Commander y equipo según la severidad.

**Escala de severidad recomendada:**

| Nivel | Descripción | Tiempo de respuesta |
|-------|-------------|---------------------|
| P1 (Crítico) | Ransomware activo, data breach confirmado, sistemas críticos caidos | Inmediato, 24/7 |
| P2 (Alto) | Compromiso de credenciales privilegiadas, malware en propagación | < 1 hora |
| P3 (Medio) | Phishing exitoso sin movimiento lateral, vulnerabilidad explotada contenida | < 4 horas |
| P4 (Bajo) | Intentos fallidos, malware detectado y bloqueado por EDR | < 24 horas |

### Fase 3: Contención, erradicación y recuperación

NIST agrupa estas tres actividades en una sola fase porque en la práctica se ejecutan de forma iterativa:

**Contención a corto plazo (primeras horas):**
- Aislar sistemas afectados de la red (no apagarlos: se pierden evidencias en memoria)
- Bloquear IOCs conocidos en firewall, proxy y EDR
- Revocar credenciales comprometidas
- Activar canales de comunicación alternativos si es necesario

**Contención a largo plazo (días):**
- Segmentar redes para limitar el movimiento lateral
- Desplegar monitorización reforzada en segmentos adyacentes
- Implementar reglas de detección específicas para el TTP observado

**Erradicación:**
- Eliminar malware de todos los sistemas afectados
- Cerrar los vectores de acceso (parchear vulnerabilidad, eliminar backdoors)
- Resetear credenciales de todos los usuarios y servicios potencialmente comprometidos
- Verificar la integridad de los sistemas antes de reconectar

**Recuperación:**
- Restaurar sistemas desde backups verificados (limpios)
- Reconectar sistemas de forma gradual, monitorizando cada paso
- Validar que los servicios operan correctamente
- Mantener monitorización intensiva durante al menos 30 días post-recuperación

### Fase 4: Actividad post-incidente

La fase que todos quieren saltarse y la que más valor genera a largo plazo.

**Post-mortem (Lessons Learned):**
- Reunión formal dentro de los 5 días laborables posteriores al cierre del incidente
- Participan todos los roles involucrados (no solo técnicos)
- Se documenta: timeline, que funciono, que fallo, acciones de mejora

**Estructura del informe post-incidente:**

1. Resumen ejecutivo (para dirección, no técnico)
2. Timeline detallado con marcas de tiempo
3. Alcance: sistemas, datos y usuarios afectados
4. Vector de ataque y TTPs mapeados a MITRE ATT&CK
5. Acciones de contención y erradicación realizadas
6. Impacto: operativo, financiero, regulatorio, reputacional
7. Causa raíz
8. Acciones de mejora con responsable y fecha límite
9. Indicadores de compromiso (IOCs) para compartir

**Compartición de información:**
- Notificación a INCIBE-CERT (sector privado) o CCN-CERT (sector público) según aplique
- Notificación a la AEPD si hay datos personales afectados (máximo 72 horas)
- Compartición de IOCs con comunidad sectorial (ISACs)

## Roles del equipo de respuesta a incidentes

Un equipo de respuesta efectivo necesita roles claros asignados antes de que ocurra el incidente. No se definen durante la crisis.

### Roles core

**Incident Commander (IC):**
- Lidera la respuesta y toma decisiones operativas
- Coordina entre equipos técnicos, comunicación y dirección
- Decide cuando escalar, cuando contener y cuando dar por cerrado el incidente
- Requisito: experiencia en gestión de crisis, no necesariamente el perfil más técnico

**Analista de triage (N1/N2):**
- Realiza el triage inicial, clasifica la alerta y recopila evidencias tempranas
- Documenta las acciones en el sistema de ticketing
- Escala al IC si confirma incidente de severidad P1/P2

**Analista forense (N3):**
- Adquiere y preserva evidencias digitales con cadena de custodia
- Analiza memoria, disco, logs y tráfico de red
- Identifica TTPs, IOCs y alcance del compromiso

**Ingeniero de infraestructura:**
- Ejecuta las acciones de contención en red y sistemas (aislamientos, bloqueos, parcheados)
- Coordina la restauración de backups
- Valida la integridad de los sistemas recuperados

### Roles de apoyo

**Comunicaciones/PR:**
- Gestiona la comunicación interna (empleados) y externa (clientes, medios, reguladores)
- Coordina con legal los mensajes públicos

**Legal:**
- Asesora sobre obligaciones regulatorias (RGPD, NIS2, ENS)
- Revisa comunicaciones públicas
- Coordina con fuerzas de seguridad si es necesario

**Dirección/CISO:**
- Autoriza decisiones de alto impacto (pagar/no pagar rescate, comunicación pública, parar producción)
- Interlocutor con el consejo de administración

### Matriz RACI simplificada

| Actividad | IC | Analista N1/N2 | Forense N3 | Infra | Legal | CISO |
|-----------|-----|----------------|------------|-------|-------|------|
| Triage inicial | I | R | C | I | - | - |
| Decisión de severidad | R | C | C | I | I | I |
| Contención técnica | A | C | C | R | I | I |
| Adquisición forense | A | I | R | C | I | - |
| Comunicación interna | R | I | I | I | C | A |
| Notificación regulatoria | I | - | C | - | R | A |
| Decisión pago rescate | C | - | C | - | C | R |
| Post-mortem | R | R | R | R | C | A |

R = Responsible, A = Accountable, C = Consulted, I = Informed

## Playbook 1: Ransomware

El ransomware es el incidente más frecuente y de mayor impacto en España, como demuestran los casos del SEPE, Hospital Clinic, Everis o Ayuntamiento de Sevilla. Este playbook detalla cada paso.

### Criterios de detección

- Alertas de EDR por cifrado masivo de ficheros
- Extensión de archivos cambiada a patrones conocidos (.locked, .encrypt, .ryuk, .lockbit)
- Notas de rescate detectadas en directorios
- Spike anómalo en operaciones de escritura en disco
- Comunicaciones salientes a dominios/IPs de C2 conocidos
- Procesos sospechosos: vssadmin.exe eliminando Shadow Copies, bcdedit.exe modificando opciones de arranque

### Acciones inmediatas (primeros 30 minutos)

1. **No apagar los equipos afectados.** La memoria RAM contiene evidencias del malware, claves de cifrado potencialmente recuperables y artefactos del proceso de infección.
2. **Aislar los sistemas afectados de la red.** Desconectar cable o deshabilitar interfaz de red (no WiFi: puede reconectar).
3. **Desconectar backups de la red** si aún no están afectados. Verificar integridad de snapshots.
4. **Bloquear IOCs** en firewall, proxy y EDR: hashes, IPs, dominios de C2.
5. **Revocar credenciales** de cuentas comprometidas o potencialmente comprometidas (empezar por cuentas privilegiadas).
6. **Activar comunicación alternativa.** Si el correo está comprometido, usar canal secundario (Signal, llamadas telefonicas, Slack externo).

### Contención

- Identificar el vector de entrada (phishing, RDP expuesto, vulnerabilidad explotada, supply chain).
- Mapear el movimiento lateral: que sistemas están comprometidos y cuales están en riesgo.
- Segmentar la red para crear zonas limpias.
- Desplegar reglas de detección específicas para el ransomware identificado.
- Verificar que los controladores de dominio (Active Directory) no están comprometidos. Si lo están, la recuperación cambia radicalmente.

### Erradicación

- Eliminar el ransomware y todos los artefactos asociados de los sistemas afectados.
- Buscar backdoors o mecanismos de persistencia (táreas programadas, servicios, claves de registro).
- Parchear la vulnerabilidad explotada como vector de entrada.
- Si Active Directory está comprometido: reconstruir desde cero o desde backup offline verificado.
- Resetear TODAS las contraseñas del dominio (no solo las comprometidas).

### Recuperación

- Restaurar desde backups verificados. Nunca restaurar sobre un sistema no limpio.
- Priorizar la restauración por criticidad de negocio.
- Reconectar sistemas de forma gradual con monitorización intensiva.
- Verificar que el cifrado no ha corrompido bases de datos o sistemas de ficheros.
- Mantener la monitorización reforzada durante al menos 30 días.

### Decisión sobre el rescate

La posición recomendada por INCIBE, CCN-CERT y Europol es **no pagar**. Las razones:

- No garantiza la recuperación de los datos
- Financia al grupo criminal para futuros ataques
- Te marca como "buen pagador" para futuros ataques
- Puede constituir financiación de terrorismo en algunos casos

Si la organización no tiene backups y los datos son críticos, la decisión final es de la dirección con asesoramiento legal. Documentar la decisión y el razonamiento.

{{< cta type="tofu" text="Riskitera automatiza el triage, la correlación y la generacion de playbooks de tu SOC con IA soberana. Reduce el tiempo de detección y respuesta desde el primer dia." label="Ver demo SOC" >}}

## Playbook 2: Phishing (compromiso de credenciales)

### Criterios de detección

- Usuario reporta correo sospechoso
- Sandbox de correo detecta enlace o adjunto malicioso
- Login desde ubicación geográfica anomala
- Acceso a aplicaciones SaaS desde IP no habitual
- Reglas de reenvio de correo creadas sin autorización
- Alertas de impossible travel (login desde Madrid y a los 10 minutos desde otro país)

### Acciones inmediatas

1. **Aislar el correo malicioso.** Buscar en todo el tenant de correo el mismo mensaje (por hash, asunto, remitente) y eliminarlo de todos los buzones.
2. **Identificar a todos los usuarios que interactuaron** con el correo (abrieron, hicieron clic, introdujeron credenciales).
3. **Forzar cambio de contraseña** para todos los usuarios afectados.
4. **Revocar tokens de sesión activos** (OAuth, cookies de sesión) para evitar que el atacante mantenga acceso.
5. **Verificar reglas de reenvio** en los buzones afectados y eliminar las no autorizadas.

### Contención

- Bloquear el dominio/URL de phishing en proxy y DNS.
- Reportar el dominio a Google Safe Browsing y PhishTank.
- Si se comprometieron credenciales: verificar si se reutilizan en otros sistemas.
- Revisar actividad del atacante en las cuentas comprometidas: correos leidos, datos accedidos, reglas creadas, ficheros descargados.

### Erradicación

- Eliminar reglas de reenvio, delegaciones y permisos no autorizados.
- Revocar aplicaciones OAuth de terceros añadidas por el atacante.
- Verificar que no hay mecanismos de persistencia (app passwords, tokens de API).
- Si el phishing incluia malware: ejecutar el playbook de malware en paralelo.

### Recuperación

- Restaurar configuraciones originales de los buzones afectados.
- Implementar MFA si no estaba activo (el 90% de los phishing exitosos se evitan con MFA).
- Enviar comunicación interna de alerta con indicadores del phishing para que otros empleados lo identifiquen.
- Realizar formación de concienciación focalizada para los usuarios afectados.

## Playbook 3: Data breach (brecha de datos)

### Criterios de detección

- DLP (Data Loss Prevention) alerta sobre exfiltración de datos sensibles
- Volumenes anómalos de datos transferidos fuera de la red
- Acceso masivo a registros de base de datos fuera de patrón habitual
- Datos de la organización detectados en foros underground o paste sites
- Notificación de un tercero (investigador, cliente, proveedor)

### Acciones inmediatas

1. **Determinar que datos están afectados.** Categorizar: datos personales (RGPD), datos financieros, propiedad intelectual, datos de clientes.
2. **Identificar el vector de exfiltración.** Via red, USB, correo, cloud storage, API expuesta.
3. **Cortar el canal de exfiltración** sin alertar al atacante (si aún está activo).
4. **Preservar logs y evidencias** del acceso a datos.
5. **Notificar a Legal** inmediatamente para evaluar obligaciones RGPD.

### Contención

- Bloquear el canal de exfiltración.
- Revocar accesos a los sistemas comprometidos.
- Implementar monitorización intensiva en las bases de datos afectadas.
- Si el vector fue una API expuesta: deshabilitarla y auditar todas las APIs públicas.
- Activar monitorización de dark web para los datos exfiltrados.

### Erradicación

- Cerrar la vulnerabilidad o vector de acceso que permitio la brecha.
- Auditar todos los accesos a los datos afectados en los últimos 90 días.
- Verificar que no hay otros canales de exfiltración activos.

### Recuperación y obligaciones legales

- **Notificación AEPD:** Máximo 72 horas desde que se tiene conocimiento de la brecha (si afecta a datos personales).
- **Notificación a afectados:** Si el riesgo para los derechos y libertades es alto, notificar a las personas afectadas sin dilación.
- **Registro interno:** Documentar la brecha en el registro de violaciones de seguridad (obligatorio RGPD, artículo 33.5).
- Evaluar si los datos exfiltrados permiten identificar personas, realizar fraude o causar otro daño.
- Ofrecer medidas de mitigación a los afectados (cambio de contraseñas, monitorización de identidad).

## Playbook 4: DDoS (denegación de servicio distribuido)

### Criterios de detección

- Spike subito en tráfico de red hacia servidores públicos
- Degradación o caida de servicios web sin causa interna identificada
- Alertas de CDN o WAF por tráfico anómalo
- Incremento masivo de conexiones desde IPs dispersas geograficamente
- Patrones de tráfico no humanos (request rate, user agents, distribución de IPs)

### Acciones inmediatas

1. **Activar mitigación en CDN/WAF.** Si usas Cloudflare, AWS Shield, Akamai o similar: activar el modo de mitigación DDoS.
2. **Identificar el tipo de ataque.** Volumetrico (saturación de ancho de banda), de protocolo (SYN flood, amplificación) o de capa de aplicación (HTTP flood).
3. **Activar rate limiting** agresivo en las IPs y patrones identificados.
4. **Comunicar internamente** que se trata de un DDoS, no de un fallo de infraestructura.

### Contención

- Coordinar con el ISP para filtrar tráfico en upstream (blackholing o scrubbing).
- Implementar geo-blocking si el tráfico malicioso viene de regiones específicas y los usuarios legitimos no.
- Escalar recursos de infraestructura si es posible (auto-scaling).
- Si el DDoS es una cortina de humo para otro ataque: verificar que no hay actividad de intrusión en paralelo.

### Erradicación

- Un DDoS no se "erradica" como un malware. Se mitiga.
- Documentar las IPs y patrones para futuros bloqueos.
- Evaluar si se trata de un ataque de extorsión (RDoS): en ese caso, tratar también como una amenaza de extorsión.
- Verificar que la infraestructura no ha sido comprometida durante el DDoS.

### Recuperación

- Desactivar gradualmente las reglas de mitigación agresivas para no bloquear tráfico legítimo.
- Verificar que todos los servicios están operativos y con rendimiento normal.
- Revisar la arquitectura de resiliencia: caching, CDN, anycast, auto-scaling.
- Considerar un servicio de mitigación DDoS dedicado si no se tenia.

## Cómo comunicar un incidente interna y externamente

La comunicación durante un incidente es tan crítica como la respuesta técnica. Una mala comunicación puede agravar el daño reputacional más que el propio incidente.

### Comunicación interna

**Primeras 2 horas:**
- Notificar a la cadena de mando: CISO, CTO, CEO.
- Informar al equipo IT/SOC con los datos necesarios para colaborar.
- No enviar correo masivo a toda la empresa hasta que se entienda el alcance.

**Primeras 24 horas:**
- Comunicación general a empleados con: que ha pasado (en términos generales), que deben hacer (no hacer), y cuando recibiran la siguiente actualización.
- Establecer cadencia de actualizaciónes (cada 4-8 horas en P1, cada 24 horas en P2).

**Durante el incidente:**
- Mantener un canal de war room (virtual o presencial) para el equipo de respuesta.
- Todas las decisiones y acciones se documentan en tiempo real en el sistema de ticketing.
- Nunca comunicar internamente lo que no se comunicaria externamente (las filtraciones son inevitables).

### Comunicación externa

**Con reguladores:**
- AEPD: 72 horas para brechas de datos personales
- CCN-CERT o INCIBE-CERT: según aplique, para incidentes significativos (NIS2)
- Cuerpos de seguridad: si hay indicios de delito

**Con clientes/usuarios:**
- Solo cuando se tenga información verificada del alcance
- Lenguaje claro, sin jerga técnica
- Incluir: que pasó, que datos se vieron afectados, que medidas se han tomado, que deben hacer ellos

**Con medios de comunicación:**
- Un único portavoz designado
- Declaraciones breves y factuales
- No especular sobre atribuciones ni costes

### Plantilla de comunicación interna (P1)

```
ASUNTO: [INCIDENTE] Situación de seguridad - Actualización [N]

Estado: [Activo/Contenido/Resuelto]
Severidad: P1
Hora de detección: [YYYY-MM-DD HH:MM UTC]

QUE HA PASADO:
[Descripción factual en 2-3 líneas]

QUE ESTAMOS HACIENDO:
[Acciones en curso]

QUE NECESITAMOS DE TI:
[Acciones que los empleados deben tomar]

PROXIMA ACTUALIZACION:
[Hora estimada]

Contacto: [Incident Commander] vía [canal]
```

## Cómo documentar lecciones aprendidas

El post-mortem es la actividad con mayor retorno de inversión en todo el proceso de respuesta. Sin embargo, la mayoría de las organizaciones lo omiten o lo hacen de forma superficial.

### Cuándo hacerlo

- Reunión formal: dentro de los 5 días laborables posteriores al cierre del incidente
- Asistentes: todos los roles involucrados en la respuesta (técnicos, comunicación, legal, dirección)
- Duración: 90-120 minutos para un P1, 60 minutos para un P2

### Qué documentar

**Timeline completo:**
- Hora de primer indicador (no de detección)
- Hora de detección
- Hora de confirmación del incidente
- Hora de inicio de contención
- Hora de contención efectiva
- Hora de erradicación
- Hora de recuperación
- Métricas clave: MTTD (Mean Time to Detect), MTTC (Mean Time to Contain), MTTR (Mean Time to Recover)

**Análisis de causa raíz:**
- Vector de ataque inicial
- Que controles fallaron y por que
- Que controles funcionaron
- TTPs mapeados a [MITRE ATT&CK](https://attack.mitre.org/) con IDs específicos (ej: T1566.001 Spearphishing Attachment, T1486 Data Encrypted for Impact)

**Acciones de mejora:**
Cada acción debe tener:
- Descripción concreta (no "mejorar la seguridad")
- Responsable asignado
- Fecha límite
- Seguimiento en la siguiente revisión

### Ejemplo de acción de mejora

```
Acción: Implementar MFA en todos los accesos VPN
Causa: El vector de entrada fue credenciales VPN comprometidas sin segundo factor
Responsable: Jefe de Infraestructura
Fecha límite: 30 días
Estado: Pendiente
Prioridad: Crítica
```

### Métricas del programa de respuesta

Para medir la madurez del programa IR a lo largo del tiempo:

| Métrica | Objetivo | Frecuencia de medición |
|---------|----------|------------------------|
| MTTD (detección) | < 24 horas | Por incidente |
| MTTC (contención) | < 4 horas desde detección | Por incidente |
| MTTR (recuperación) | < 72 horas para P1 | Por incidente |
| % incidentes con post-mortem completado | 100% para P1/P2 | Mensual |
| % acciones de mejora cerradas en plazo | > 80% | Trimestral |
| Tabletop exercises realizados | >= 4/año | Trimestral |

## Integración con frameworks: MITRE ATT&CK, CCN-CERT e INCIBE

### MITRE ATT&CK

[MITRE ATT&CK](https://attack.mitre.org/) proporciona la taxonomía común para describir las técnicas de los atacantes. Cada playbook debe mapear las TTPs observadas a la matriz ATT&CK para:

- Comunicar de forma estandarizada con otros equipos y organizaciones
- Identificar gaps en la cobertura de detección
- Priorizar reglas de detección en el SIEM basándose en técnicas reales

**Ejemplo de mapeo para un incidente de ransomware:**

| Fase | Técnica ATT&CK | ID |
|------|----------------|-----|
| Acceso inicial | Spearphishing Attachment | T1566.001 |
| Ejecución | PowerShell | T1059.001 |
| Persistencia | Scheduled Task | T1053.005 |
| Movimiento lateral | Remote Services (RDP) | T1021.001 |
| Exfiltración | Exfiltration Over C2 Channel | T1041 |
| Impacto | Data Encrypted for Impact | T1486 |

### CCN-CERT

El [CCN-CERT](https://www.ccn-cert.cni.es/) es la referencia para la Administración Pública española. Pública:

- **Guías CCN-STIC:** Procedimientos técnicos de seguridad alineados con el ENS
- **Herramienta LUCIA:** Sistema de gestión de ciberincidentes para la Administración
- **Guías de respuesta:** Procedimientos específicos para ransomware, APT y otros tipos de incidentes
- **Servicio de alerta temprana (SAT):** Monitorización del sector público

### INCIBE

[INCIBE](https://www.incibe.es/) es la referencia para el sector privado y las pymes:

- **INCIBE-CERT:** Gestión de incidentes para ciudadanos y empresas
- **Linea 017:** Teléfono de atención en ciberseguridad
- **Guías y herramientas:** Kits de concienciación, políticas de seguridad tipo, planes de respuesta
- **Informes anuales:** Balance de ciberseguridad con datos estadísticos nacionales

## Errores comunes en la respuesta a incidentes

Después de analizar decenas de incidentes reales en España (incluyendo los documentados en nuestro artículo sobre los [10 incidentes más graves en España](/es/posts/2026/06/incidentes-ciberseguridad-espana-graves/)), estos son los errores más frecuentes:

### 1. Apagar los equipos comprometidos

Error intuitivo pero crítico. Al apagar un equipo se pierde la memoria RAM, donde puede haber claves de cifrado del ransomware, procesos maliciosos en ejecución e indicadores de compromiso volatiles. La acción correcta es **aislar de la red**, no apagar.

### 2. No preservar evidencias

En la urgencia por restaurar, se formatean discos y se reinstalan sistemas sin adquirir imagenes forenses. Esto destruye la posibilidad de entender el ataque, determinar el alcance real y perseguir legalmente al atacante.

### 3. Comunicar antes de verificar

Publicar información incorrecta sobre el alcance o el tipo de incidente genera confusión y daño reputacional adicional. Es mejor decir "estamos investigando" que afirmar algo que habrá que corregir después.

### 4. No verificar los backups antes de restaurar

Restaurar un backup que contiene el malware o la vulnerabilidad que permitio el ataque original. Todos los backups deben verificarse en un entorno aislado antes de restaurar en producción.

### 5. Declarar victoria demasiado pronto

Contener la amenaza visible no significa que el atacante no tenga otros mecanismos de persistencia. El periodo de monitorización post-incidente (mínimo 30 días) es esencial para detectar reinfecciones.

### 6. No hacer post-mortem

El 60% de las organizaciones no completan un post-mortem formal tras un incidente grave. Esto garantiza que los mismos errores se repitan. El caso del Ministerio de Trabajo (atacado 3 meses después del SEPE, en el mismo ámbito ministerial) ilustra este patrón.

## Checklist rápido: preparación mínima para tu SOC

Antes de que ocurra el próximo incidente, verifica que tienes:

- [ ] Plan de respuesta general documentado y aprobado por dirección
- [ ] Playbooks específicos para ransomware, phishing, data breach y DDoS
- [ ] Roles asignados: Incident Commander, analistas, forense, infra, legal, comunicaciones
- [ ] Lista de contactos de emergencia actualizada (incluyendo fuera de horario)
- [ ] Canal de comunicación alternativo (por si el correo está comprometido)
- [ ] Backups offline verificados (probados, no solo existentes)
- [ ] Herramientas forenses preparadas (software de adquisición, jump bag)
- [ ] Contrato con proveedor IR externo (retainer) para escalado
- [ ] Al menos 2 tabletop exercises realizados en los últimos 12 meses
- [ ] Procedimiento de notificación regulatoria documentado (AEPD, INCIBE-CERT, CCN-CERT)
- [ ] Feeds de threat intelligence activos e integrados en el SIEM
- [ ] Reglas de detección mapeadas a MITRE ATT&CK para las 20 técnicas más frecuentes

{{< cta type="bofu" text="Solicita una demo personalizada para tu SOC y descubre cómo Riskitera automatiza el triage, la correlación y el reporting con IA soberana." label="Solicitar demo" >}}


**Artículos relacionados:**
- [Cómo Montar Soc Desde Cero](/es/posts/2026/04/como-montar-soc-desde-cero/)
- [Threat Hunting Guía Practica](/es/posts/2026/04/threat-hunting-guia-practica/)

## Preguntas frecuentes

### Cuánto tiempo tiene una empresa para notificar un incidente de seguridad en España?

Depende del tipo de incidente. Si hay datos personales afectados, el RGPD exige notificación a la AEPD en un máximo de 72 horas desde que se tiene conocimiento de la brecha. La Directiva NIS2 establece una alerta temprana en 24 horas y un informe completo en 72 horas para incidentes significativos. En el ámbito del ENS, el CCN-CERT debe ser notificado según la criticidad del incidente.

### Qué diferencia hay entre un plan de respuesta y un playbook?

El plan de respuesta (IRP) es el documento marco: define roles, responsabilidades, cadena de comunicación, criterios de severidad y políticas generales. Los playbooks son procedimientos operativos detallados para tipos de incidentes concretos (ransomware, phishing, DDoS). Un SOC necesita ambos: el plan dice "quien hace que y cuando escalar", el playbook dice "estos son los 15 pasos exactos para contener un ransomware".

### Es recomendable pagar el rescate en un ataque de ransomware?

La posición unanime de INCIBE, CCN-CERT, Europol y la mayoría de expertos es no pagar. No garantiza la recuperación de los datos, financia al grupo criminal y marca a la organización como objetivo futuro. Además, puede tener implicaciones legales (financiación de terrorismo). La mejor defensa contra el ransomware son backups offline verificados, segmentación de red y un plan de recuperación probado.

### Qué framework de respuesta a incidentes es mejor para una empresa española?

NIST SP 800-61 es la referencia internacional más utilizada y la base de este artículo. Para empresas españolas, se complementa con las guías CCN-STIC del CCN-CERT (obligatorias para el sector público bajo el ENS) y los recursos de INCIBE (orientados al sector privado). ISO 27035 (Gestión de incidentes de seguridad de la información) es otra opción, especialmente si la organización ya está certificada en ISO 27001.

### Cómo se mide la eficacia de un equipo de respuesta a incidentes?

Las métricas clave son: MTTD (tiempo medio de detección), MTTC (tiempo medio de contención) y MTTR (tiempo medio de recuperación). Un SOC maduro debería detectar incidentes en menos de 24 horas, contener en menos de 4 horas y recuperar servicios críticos en menos de 72 horas para incidentes P1. Además, se mide el porcentaje de post-mortems completados, las acciones de mejora cerradas en plazo y la frecuencia de simulacros.
