---
title: "Respuesta a incidentes de seguridad: playbook completo para equipos SOC"
description: "Playbook completo de respuesta a incidentes para SOC: fases NIST, roles, comunicacion, contencion, erradicacion, recuperacion y lecciones aprendidas con ejemplos practicos."
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

Playbook completo de respuesta a incidentes para SOC: fases NIST, roles, comunicacion, contencion, erradicacion, recuperacion y lecciones aprendidas con ejemplos practicos.

<!--more-->

{{< key-takeaways >}}
- El framework NIST SP 800-61 estructura la respuesta a incidentes en 4 fases: preparacion, deteccion y analisis, contencion/erradicacion/recuperacion, y actividad post-incidente
- Cada tipo de incidente (ransomware, phishing, data breach, DDoS) requiere un playbook especifico con criterios de deteccion, pasos de contencion y procedimientos de recuperacion propios
- Los roles del equipo de respuesta deben estar definidos antes del incidente, con un Incident Commander que coordine todas las acciones
- La documentacion durante el incidente y el analisis post-mortem son tan importantes como la contencion tecnica
- Frameworks como MITRE ATT&CK y guias de CCN-CERT e INCIBE proporcionan taxonomias y procedimientos estandarizados para equipos SOC en Espana
{{< /key-takeaways >}}

## Que es un plan de respuesta a incidentes

Un plan de respuesta a incidentes (Incident Response Plan, IRP) es el documento que define como una organizacion detecta, contiene, erradica y se recupera de un incidente de ciberseguridad. No es un documento teorico: es un manual operativo que el equipo SOC sigue bajo presion, cuando los sistemas estan caidos y la direccion exige respuestas.

La referencia principal para construir un IRP es el [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) (Computer Security Incident Handling Guide), publicado por el National Institute of Standards and Technology. En el contexto espanol, el [CCN-CERT](https://www.ccn-cert.cni.es/) publica guias complementarias adaptadas al Esquema Nacional de Seguridad (ENS), y el [INCIBE](https://www.incibe.es/) ofrece recursos para el sector privado y las pymes.

### Por que necesitas un playbook, no solo un plan

Un plan de respuesta general describe el "que". Los playbooks describen el "como" para cada tipo de incidente concreto. Un SOC efectivo tiene ambos:

- **Plan general (IRP):** Roles, cadena de comunicacion, criterios de escalado, umbrales de severidad.
- **Playbooks especificos:** Procedimientos paso a paso para ransomware, phishing, data breach, DDoS, compromiso de credenciales, etc.

La diferencia entre un equipo que responde en 30 minutos y uno que tarda 8 horas no suele ser tecnica. Es la diferencia entre tener un playbook probado y tener que improvisar.

## Las 4 fases de respuesta a incidentes segun NIST SP 800-61

El framework NIST organiza la respuesta en cuatro fases. No son secuenciales en la practica (se solapan y se iteran), pero proporcionan la estructura necesaria para no perder el control.

### Fase 1: Preparacion

La preparacion ocurre antes del incidente. Es la fase mas importante y la mas ignorada. Incluye:

**Herramientas y capacidades:**
- SIEM configurado con reglas de deteccion actualizadas
- EDR/XDR desplegado en todos los endpoints
- Plataforma de ticketing para incidentes (no sirve un Excel)
- Herramientas forenses: adquisicion de imagenes, analisis de memoria, PCAP
- Canales de comunicacion alternativos (si el correo esta comprometido, como os comunicais?)

**Documentacion:**
- Inventario de activos actualizado (no puedes proteger lo que no conoces)
- Diagramas de red con segmentacion real (no la teorica)
- Lista de contactos de emergencia: equipo IR, legal, CISO, comunicacion, proveedores criticos
- Contratos con proveedores de IR externos (retainers) para escalado

**Entrenamiento:**
- Tabletop exercises trimestrales con escenarios realistas
- Simulacros tecnicos (red team / purple team) semestrales
- Formacion especifica para cada rol del equipo de respuesta

**Inteligencia:**
- Feeds de threat intelligence activos (MISP, OTX, feeds sectoriales)
- Mapeo de [MITRE ATT&CK](https://attack.mitre.org/) para las tecnicas mas relevantes del sector
- Seguimiento de grupos APT que atacan tu sector o geografia

### Fase 2: Deteccion y analisis

Esta es la fase donde la mayoria de los SOC viven dia a dia. El objetivo es identificar que un incidente esta ocurriendo, determinar su alcance y asignarle severidad.

**Fuentes de deteccion:**

| Fuente | Tipo de alerta | Ejemplo |
|--------|---------------|---------|
| SIEM | Correlacion de eventos | Login desde IP anomala + escalada de privilegios |
| EDR | Comportamiento en endpoint | Proceso svchost.exe ejecutando PowerShell codificado |
| IDS/IPS | Firmas y anomalias de red | Trafico C2 a dominio conocido |
| Threat Intelligence | IOCs coincidentes | Hash de fichero en feed de malware activo |
| Usuarios | Reporte manual | "Mi equipo actua raro" o "He recibido un correo sospechoso" |
| Honeypots | Acceso a recurso trampa | Lectura de archivo canary en servidor de ficheros |

**Proceso de triage:**

1. **Verificacion:** Confirmar que la alerta no es un falso positivo. Correlacionar con fuentes adicionales.
2. **Clasificacion:** Asignar tipo (ransomware, phishing, intrusion, data breach, DDoS, otro).
3. **Severidad:** Usar una escala predefinida (P1-P4) basada en impacto y urgencia.
4. **Asignacion:** Designar Incident Commander y equipo segun la severidad.

**Escala de severidad recomendada:**

| Nivel | Descripcion | Tiempo de respuesta |
|-------|-------------|---------------------|
| P1 (Critico) | Ransomware activo, data breach confirmado, sistemas criticos caidos | Inmediato, 24/7 |
| P2 (Alto) | Compromiso de credenciales privilegiadas, malware en propagacion | < 1 hora |
| P3 (Medio) | Phishing exitoso sin movimiento lateral, vulnerabilidad explotada contenida | < 4 horas |
| P4 (Bajo) | Intentos fallidos, malware detectado y bloqueado por EDR | < 24 horas |

### Fase 3: Contencion, erradicacion y recuperacion

NIST agrupa estas tres actividades en una sola fase porque en la practica se ejecutan de forma iterativa:

**Contencion a corto plazo (primeras horas):**
- Aislar sistemas afectados de la red (no apagarlos: se pierden evidencias en memoria)
- Bloquear IOCs conocidos en firewall, proxy y EDR
- Revocar credenciales comprometidas
- Activar canales de comunicacion alternativos si es necesario

**Contencion a largo plazo (dias):**
- Segmentar redes para limitar el movimiento lateral
- Desplegar monitorizacion reforzada en segmentos adyacentes
- Implementar reglas de deteccion especificas para el TTP observado

**Erradicacion:**
- Eliminar malware de todos los sistemas afectados
- Cerrar los vectores de acceso (parchear vulnerabilidad, eliminar backdoors)
- Resetear credenciales de todos los usuarios y servicios potencialmente comprometidos
- Verificar la integridad de los sistemas antes de reconectar

**Recuperacion:**
- Restaurar sistemas desde backups verificados (limpios)
- Reconectar sistemas de forma gradual, monitorizando cada paso
- Validar que los servicios operan correctamente
- Mantener monitorizacion intensiva durante al menos 30 dias post-recuperacion

### Fase 4: Actividad post-incidente

La fase que todos quieren saltarse y la que mas valor genera a largo plazo.

**Post-mortem (Lessons Learned):**
- Reunion formal dentro de los 5 dias laborables posteriores al cierre del incidente
- Participan todos los roles involucrados (no solo tecnicos)
- Se documenta: timeline, que funciono, que fallo, acciones de mejora

**Estructura del informe post-incidente:**

1. Resumen ejecutivo (para direccion, no tecnico)
2. Timeline detallado con marcas de tiempo
3. Alcance: sistemas, datos y usuarios afectados
4. Vector de ataque y TTPs mapeados a MITRE ATT&CK
5. Acciones de contencion y erradicacion realizadas
6. Impacto: operativo, financiero, regulatorio, reputacional
7. Causa raiz
8. Acciones de mejora con responsable y fecha limite
9. Indicadores de compromiso (IOCs) para compartir

**Comparticion de informacion:**
- Notificacion a INCIBE-CERT (sector privado) o CCN-CERT (sector publico) segun aplique
- Notificacion a la AEPD si hay datos personales afectados (maximo 72 horas)
- Comparticion de IOCs con comunidad sectorial (ISACs)

## Roles del equipo de respuesta a incidentes

Un equipo de respuesta efectivo necesita roles claros asignados antes de que ocurra el incidente. No se definen durante la crisis.

### Roles core

**Incident Commander (IC):**
- Lidera la respuesta y toma decisiones operativas
- Coordina entre equipos tecnicos, comunicacion y direccion
- Decide cuando escalar, cuando contener y cuando dar por cerrado el incidente
- Requisito: experiencia en gestion de crisis, no necesariamente el perfil mas tecnico

**Analista de triage (N1/N2):**
- Realiza el triage inicial, clasifica la alerta y recopila evidencias tempranas
- Documenta las acciones en el sistema de ticketing
- Escala al IC si confirma incidente de severidad P1/P2

**Analista forense (N3):**
- Adquiere y preserva evidencias digitales con cadena de custodia
- Analiza memoria, disco, logs y trafico de red
- Identifica TTPs, IOCs y alcance del compromiso

**Ingeniero de infraestructura:**
- Ejecuta las acciones de contencion en red y sistemas (aislamientos, bloqueos, parcheados)
- Coordina la restauracion de backups
- Valida la integridad de los sistemas recuperados

### Roles de apoyo

**Comunicaciones/PR:**
- Gestiona la comunicacion interna (empleados) y externa (clientes, medios, reguladores)
- Coordina con legal los mensajes publicos

**Legal:**
- Asesora sobre obligaciones regulatorias (RGPD, NIS2, ENS)
- Revisa comunicaciones publicas
- Coordina con fuerzas de seguridad si es necesario

**Direccion/CISO:**
- Autoriza decisiones de alto impacto (pagar/no pagar rescate, comunicacion publica, parar produccion)
- Interlocutor con el consejo de administracion

### Matriz RACI simplificada

| Actividad | IC | Analista N1/N2 | Forense N3 | Infra | Legal | CISO |
|-----------|-----|----------------|------------|-------|-------|------|
| Triage inicial | I | R | C | I | - | - |
| Decision de severidad | R | C | C | I | I | I |
| Contencion tecnica | A | C | C | R | I | I |
| Adquisicion forense | A | I | R | C | I | - |
| Comunicacion interna | R | I | I | I | C | A |
| Notificacion regulatoria | I | - | C | - | R | A |
| Decision pago rescate | C | - | C | - | C | R |
| Post-mortem | R | R | R | R | C | A |

R = Responsible, A = Accountable, C = Consulted, I = Informed

## Playbook 1: Ransomware

El ransomware es el incidente mas frecuente y de mayor impacto en Espana, como demuestran los casos del SEPE, Hospital Clinic, Everis o Ayuntamiento de Sevilla. Este playbook detalla cada paso.

### Criterios de deteccion

- Alertas de EDR por cifrado masivo de ficheros
- Extension de archivos cambiada a patrones conocidos (.locked, .encrypt, .ryuk, .lockbit)
- Notas de rescate detectadas en directorios
- Spike anomalo en operaciones de escritura en disco
- Comunicaciones salientes a dominios/IPs de C2 conocidos
- Procesos sospechosos: vssadmin.exe eliminando Shadow Copies, bcdedit.exe modificando opciones de arranque

### Acciones inmediatas (primeros 30 minutos)

1. **No apagar los equipos afectados.** La memoria RAM contiene evidencias del malware, claves de cifrado potencialmente recuperables y artefactos del proceso de infeccion.
2. **Aislar los sistemas afectados de la red.** Desconectar cable o deshabilitar interfaz de red (no WiFi: puede reconectar).
3. **Desconectar backups de la red** si aun no estan afectados. Verificar integridad de snapshots.
4. **Bloquear IOCs** en firewall, proxy y EDR: hashes, IPs, dominios de C2.
5. **Revocar credenciales** de cuentas comprometidas o potencialmente comprometidas (empezar por cuentas privilegiadas).
6. **Activar comunicacion alternativa.** Si el correo esta comprometido, usar canal secundario (Signal, llamadas telefonicas, Slack externo).

### Contencion

- Identificar el vector de entrada (phishing, RDP expuesto, vulnerabilidad explotada, supply chain).
- Mapear el movimiento lateral: que sistemas estan comprometidos y cuales estan en riesgo.
- Segmentar la red para crear zonas limpias.
- Desplegar reglas de deteccion especificas para el ransomware identificado.
- Verificar que los controladores de dominio (Active Directory) no estan comprometidos. Si lo estan, la recuperacion cambia radicalmente.

### Erradicacion

- Eliminar el ransomware y todos los artefactos asociados de los sistemas afectados.
- Buscar backdoors o mecanismos de persistencia (tareas programadas, servicios, claves de registro).
- Parchear la vulnerabilidad explotada como vector de entrada.
- Si Active Directory esta comprometido: reconstruir desde cero o desde backup offline verificado.
- Resetear TODAS las contrasenas del dominio (no solo las comprometidas).

### Recuperacion

- Restaurar desde backups verificados. Nunca restaurar sobre un sistema no limpio.
- Priorizar la restauracion por criticidad de negocio.
- Reconectar sistemas de forma gradual con monitorizacion intensiva.
- Verificar que el cifrado no ha corrompido bases de datos o sistemas de ficheros.
- Mantener la monitorizacion reforzada durante al menos 30 dias.

### Decision sobre el rescate

La posicion recomendada por INCIBE, CCN-CERT y Europol es **no pagar**. Las razones:

- No garantiza la recuperacion de los datos
- Financia al grupo criminal para futuros ataques
- Te marca como "buen pagador" para futuros ataques
- Puede constituir financiacion de terrorismo en algunos casos

Si la organizacion no tiene backups y los datos son criticos, la decision final es de la direccion con asesoramiento legal. Documentar la decision y el razonamiento.

{{< cta type="tofu" text="Riskitera automatiza el triage, la correlacion y la generacion de playbooks de tu SOC con IA soberana. Reduce el tiempo de deteccion y respuesta desde el primer dia." label="Ver demo SOC" >}}

## Playbook 2: Phishing (compromiso de credenciales)

### Criterios de deteccion

- Usuario reporta correo sospechoso
- Sandbox de correo detecta enlace o adjunto malicioso
- Login desde ubicacion geografica anomala
- Acceso a aplicaciones SaaS desde IP no habitual
- Reglas de reenvio de correo creadas sin autorizacion
- Alertas de impossible travel (login desde Madrid y a los 10 minutos desde otro pais)

### Acciones inmediatas

1. **Aislar el correo malicioso.** Buscar en todo el tenant de correo el mismo mensaje (por hash, asunto, remitente) y eliminarlo de todos los buzones.
2. **Identificar a todos los usuarios que interactuaron** con el correo (abrieron, hicieron clic, introdujeron credenciales).
3. **Forzar cambio de contrasena** para todos los usuarios afectados.
4. **Revocar tokens de sesion activos** (OAuth, cookies de sesion) para evitar que el atacante mantenga acceso.
5. **Verificar reglas de reenvio** en los buzones afectados y eliminar las no autorizadas.

### Contencion

- Bloquear el dominio/URL de phishing en proxy y DNS.
- Reportar el dominio a Google Safe Browsing y PhishTank.
- Si se comprometieron credenciales: verificar si se reutilizan en otros sistemas.
- Revisar actividad del atacante en las cuentas comprometidas: correos leidos, datos accedidos, reglas creadas, ficheros descargados.

### Erradicacion

- Eliminar reglas de reenvio, delegaciones y permisos no autorizados.
- Revocar aplicaciones OAuth de terceros anadidas por el atacante.
- Verificar que no hay mecanismos de persistencia (app passwords, tokens de API).
- Si el phishing incluia malware: ejecutar el playbook de malware en paralelo.

### Recuperacion

- Restaurar configuraciones originales de los buzones afectados.
- Implementar MFA si no estaba activo (el 90% de los phishing exitosos se evitan con MFA).
- Enviar comunicacion interna de alerta con indicadores del phishing para que otros empleados lo identifiquen.
- Realizar formacion de concienciacion focalizada para los usuarios afectados.

## Playbook 3: Data breach (brecha de datos)

### Criterios de deteccion

- DLP (Data Loss Prevention) alerta sobre exfiltracion de datos sensibles
- Volumenes anomalos de datos transferidos fuera de la red
- Acceso masivo a registros de base de datos fuera de patron habitual
- Datos de la organizacion detectados en foros underground o paste sites
- Notificacion de un tercero (investigador, cliente, proveedor)

### Acciones inmediatas

1. **Determinar que datos estan afectados.** Categorizar: datos personales (RGPD), datos financieros, propiedad intelectual, datos de clientes.
2. **Identificar el vector de exfiltracion.** Via red, USB, correo, cloud storage, API expuesta.
3. **Cortar el canal de exfiltracion** sin alertar al atacante (si aun esta activo).
4. **Preservar logs y evidencias** del acceso a datos.
5. **Notificar a Legal** inmediatamente para evaluar obligaciones RGPD.

### Contencion

- Bloquear el canal de exfiltracion.
- Revocar accesos a los sistemas comprometidos.
- Implementar monitorizacion intensiva en las bases de datos afectadas.
- Si el vector fue una API expuesta: deshabilitarla y auditar todas las APIs publicas.
- Activar monitorizacion de dark web para los datos exfiltrados.

### Erradicacion

- Cerrar la vulnerabilidad o vector de acceso que permitio la brecha.
- Auditar todos los accesos a los datos afectados en los ultimos 90 dias.
- Verificar que no hay otros canales de exfiltracion activos.

### Recuperacion y obligaciones legales

- **Notificacion AEPD:** Maximo 72 horas desde que se tiene conocimiento de la brecha (si afecta a datos personales).
- **Notificacion a afectados:** Si el riesgo para los derechos y libertades es alto, notificar a las personas afectadas sin dilacion.
- **Registro interno:** Documentar la brecha en el registro de violaciones de seguridad (obligatorio RGPD, articulo 33.5).
- Evaluar si los datos exfiltrados permiten identificar personas, realizar fraude o causar otro dano.
- Ofrecer medidas de mitigacion a los afectados (cambio de contrasenas, monitorizacion de identidad).

## Playbook 4: DDoS (denegacion de servicio distribuido)

### Criterios de deteccion

- Spike subito en trafico de red hacia servidores publicos
- Degradacion o caida de servicios web sin causa interna identificada
- Alertas de CDN o WAF por trafico anomalo
- Incremento masivo de conexiones desde IPs dispersas geograficamente
- Patrones de trafico no humanos (request rate, user agents, distribucion de IPs)

### Acciones inmediatas

1. **Activar mitigacion en CDN/WAF.** Si usas Cloudflare, AWS Shield, Akamai o similar: activar el modo de mitigacion DDoS.
2. **Identificar el tipo de ataque.** Volumetrico (saturacion de ancho de banda), de protocolo (SYN flood, amplificacion) o de capa de aplicacion (HTTP flood).
3. **Activar rate limiting** agresivo en las IPs y patrones identificados.
4. **Comunicar internamente** que se trata de un DDoS, no de un fallo de infraestructura.

### Contencion

- Coordinar con el ISP para filtrar trafico en upstream (blackholing o scrubbing).
- Implementar geo-blocking si el trafico malicioso viene de regiones especificas y los usuarios legitimos no.
- Escalar recursos de infraestructura si es posible (auto-scaling).
- Si el DDoS es una cortina de humo para otro ataque: verificar que no hay actividad de intrusion en paralelo.

### Erradicacion

- Un DDoS no se "erradica" como un malware. Se mitiga.
- Documentar las IPs y patrones para futuros bloqueos.
- Evaluar si se trata de un ataque de extorsion (RDoS): en ese caso, tratar tambien como una amenaza de extorsion.
- Verificar que la infraestructura no ha sido comprometida durante el DDoS.

### Recuperacion

- Desactivar gradualmente las reglas de mitigacion agresivas para no bloquear trafico legitimo.
- Verificar que todos los servicios estan operativos y con rendimiento normal.
- Revisar la arquitectura de resiliencia: caching, CDN, anycast, auto-scaling.
- Considerar un servicio de mitigacion DDoS dedicado si no se tenia.

## Como comunicar un incidente interna y externamente

La comunicacion durante un incidente es tan critica como la respuesta tecnica. Una mala comunicacion puede agravar el dano reputacional mas que el propio incidente.

### Comunicacion interna

**Primeras 2 horas:**
- Notificar a la cadena de mando: CISO, CTO, CEO.
- Informar al equipo IT/SOC con los datos necesarios para colaborar.
- No enviar correo masivo a toda la empresa hasta que se entienda el alcance.

**Primeras 24 horas:**
- Comunicacion general a empleados con: que ha pasado (en terminos generales), que deben hacer (no hacer), y cuando recibiran la siguiente actualizacion.
- Establecer cadencia de actualizaciones (cada 4-8 horas en P1, cada 24 horas en P2).

**Durante el incidente:**
- Mantener un canal de war room (virtual o presencial) para el equipo de respuesta.
- Todas las decisiones y acciones se documentan en tiempo real en el sistema de ticketing.
- Nunca comunicar internamente lo que no se comunicaria externamente (las filtraciones son inevitables).

### Comunicacion externa

**Con reguladores:**
- AEPD: 72 horas para brechas de datos personales
- CCN-CERT o INCIBE-CERT: segun aplique, para incidentes significativos (NIS2)
- Cuerpos de seguridad: si hay indicios de delito

**Con clientes/usuarios:**
- Solo cuando se tenga informacion verificada del alcance
- Lenguaje claro, sin jerga tecnica
- Incluir: que paso, que datos se vieron afectados, que medidas se han tomado, que deben hacer ellos

**Con medios de comunicacion:**
- Un unico portavoz designado
- Declaraciones breves y factuales
- No especular sobre atribuciones ni costes

### Plantilla de comunicacion interna (P1)

```
ASUNTO: [INCIDENTE] Situacion de seguridad - Actualizacion [N]

Estado: [Activo/Contenido/Resuelto]
Severidad: P1
Hora de deteccion: [YYYY-MM-DD HH:MM UTC]

QUE HA PASADO:
[Descripcion factual en 2-3 lineas]

QUE ESTAMOS HACIENDO:
[Acciones en curso]

QUE NECESITAMOS DE TI:
[Acciones que los empleados deben tomar]

PROXIMA ACTUALIZACION:
[Hora estimada]

Contacto: [Incident Commander] via [canal]
```

## Como documentar lecciones aprendidas

El post-mortem es la actividad con mayor retorno de inversion en todo el proceso de respuesta. Sin embargo, la mayoria de las organizaciones lo omiten o lo hacen de forma superficial.

### Cuando hacerlo

- Reunion formal: dentro de los 5 dias laborables posteriores al cierre del incidente
- Asistentes: todos los roles involucrados en la respuesta (tecnicos, comunicacion, legal, direccion)
- Duracion: 90-120 minutos para un P1, 60 minutos para un P2

### Que documentar

**Timeline completo:**
- Hora de primer indicador (no de deteccion)
- Hora de deteccion
- Hora de confirmacion del incidente
- Hora de inicio de contencion
- Hora de contencion efectiva
- Hora de erradicacion
- Hora de recuperacion
- Metricas clave: MTTD (Mean Time to Detect), MTTC (Mean Time to Contain), MTTR (Mean Time to Recover)

**Analisis de causa raiz:**
- Vector de ataque inicial
- Que controles fallaron y por que
- Que controles funcionaron
- TTPs mapeados a [MITRE ATT&CK](https://attack.mitre.org/) con IDs especificos (ej: T1566.001 Spearphishing Attachment, T1486 Data Encrypted for Impact)

**Acciones de mejora:**
Cada accion debe tener:
- Descripcion concreta (no "mejorar la seguridad")
- Responsable asignado
- Fecha limite
- Seguimiento en la siguiente revision

### Ejemplo de accion de mejora

```
Accion: Implementar MFA en todos los accesos VPN
Causa: El vector de entrada fue credenciales VPN comprometidas sin segundo factor
Responsable: Jefe de Infraestructura
Fecha limite: 30 dias
Estado: Pendiente
Prioridad: Critica
```

### Metricas del programa de respuesta

Para medir la madurez del programa IR a lo largo del tiempo:

| Metrica | Objetivo | Frecuencia de medicion |
|---------|----------|------------------------|
| MTTD (deteccion) | < 24 horas | Por incidente |
| MTTC (contencion) | < 4 horas desde deteccion | Por incidente |
| MTTR (recuperacion) | < 72 horas para P1 | Por incidente |
| % incidentes con post-mortem completado | 100% para P1/P2 | Mensual |
| % acciones de mejora cerradas en plazo | > 80% | Trimestral |
| Tabletop exercises realizados | >= 4/ano | Trimestral |

## Integracion con frameworks: MITRE ATT&CK, CCN-CERT e INCIBE

### MITRE ATT&CK

[MITRE ATT&CK](https://attack.mitre.org/) proporciona la taxonomia comun para describir las tecnicas de los atacantes. Cada playbook debe mapear las TTPs observadas a la matriz ATT&CK para:

- Comunicar de forma estandarizada con otros equipos y organizaciones
- Identificar gaps en la cobertura de deteccion
- Priorizar reglas de deteccion en el SIEM basandose en tecnicas reales

**Ejemplo de mapeo para un incidente de ransomware:**

| Fase | Tecnica ATT&CK | ID |
|------|----------------|-----|
| Acceso inicial | Spearphishing Attachment | T1566.001 |
| Ejecucion | PowerShell | T1059.001 |
| Persistencia | Scheduled Task | T1053.005 |
| Movimiento lateral | Remote Services (RDP) | T1021.001 |
| Exfiltracion | Exfiltration Over C2 Channel | T1041 |
| Impacto | Data Encrypted for Impact | T1486 |

### CCN-CERT

El [CCN-CERT](https://www.ccn-cert.cni.es/) es la referencia para la Administracion Publica espanola. Publica:

- **Guias CCN-STIC:** Procedimientos tecnicos de seguridad alineados con el ENS
- **Herramienta LUCIA:** Sistema de gestion de ciberincidentes para la Administracion
- **Guias de respuesta:** Procedimientos especificos para ransomware, APT y otros tipos de incidentes
- **Servicio de alerta temprana (SAT):** Monitorizacion del sector publico

### INCIBE

[INCIBE](https://www.incibe.es/) es la referencia para el sector privado y las pymes:

- **INCIBE-CERT:** Gestion de incidentes para ciudadanos y empresas
- **Linea 017:** Telefono de atencion en ciberseguridad
- **Guias y herramientas:** Kits de concienciacion, politicas de seguridad tipo, planes de respuesta
- **Informes anuales:** Balance de ciberseguridad con datos estadisticos nacionales

## Errores comunes en la respuesta a incidentes

Despues de analizar decenas de incidentes reales en Espana (incluyendo los documentados en nuestro articulo sobre los [10 incidentes mas graves en Espana](/es/posts/2026/06/incidentes-ciberseguridad-espana-graves/)), estos son los errores mas frecuentes:

### 1. Apagar los equipos comprometidos

Error intuitivo pero critico. Al apagar un equipo se pierde la memoria RAM, donde puede haber claves de cifrado del ransomware, procesos maliciosos en ejecucion e indicadores de compromiso volatiles. La accion correcta es **aislar de la red**, no apagar.

### 2. No preservar evidencias

En la urgencia por restaurar, se formatean discos y se reinstalan sistemas sin adquirir imagenes forenses. Esto destruye la posibilidad de entender el ataque, determinar el alcance real y perseguir legalmente al atacante.

### 3. Comunicar antes de verificar

Publicar informacion incorrecta sobre el alcance o el tipo de incidente genera confusion y dano reputacional adicional. Es mejor decir "estamos investigando" que afirmar algo que habra que corregir despues.

### 4. No verificar los backups antes de restaurar

Restaurar un backup que contiene el malware o la vulnerabilidad que permitio el ataque original. Todos los backups deben verificarse en un entorno aislado antes de restaurar en produccion.

### 5. Declarar victoria demasiado pronto

Contener la amenaza visible no significa que el atacante no tenga otros mecanismos de persistencia. El periodo de monitorizacion post-incidente (minimo 30 dias) es esencial para detectar reinfecciones.

### 6. No hacer post-mortem

El 60% de las organizaciones no completan un post-mortem formal tras un incidente grave. Esto garantiza que los mismos errores se repitan. El caso del Ministerio de Trabajo (atacado 3 meses despues del SEPE, en el mismo ambito ministerial) ilustra este patron.

## Checklist rapido: preparacion minima para tu SOC

Antes de que ocurra el proximo incidente, verifica que tienes:

- [ ] Plan de respuesta general documentado y aprobado por direccion
- [ ] Playbooks especificos para ransomware, phishing, data breach y DDoS
- [ ] Roles asignados: Incident Commander, analistas, forense, infra, legal, comunicaciones
- [ ] Lista de contactos de emergencia actualizada (incluyendo fuera de horario)
- [ ] Canal de comunicacion alternativo (por si el correo esta comprometido)
- [ ] Backups offline verificados (probados, no solo existentes)
- [ ] Herramientas forenses preparadas (software de adquisicion, jump bag)
- [ ] Contrato con proveedor IR externo (retainer) para escalado
- [ ] Al menos 2 tabletop exercises realizados en los ultimos 12 meses
- [ ] Procedimiento de notificacion regulatoria documentado (AEPD, INCIBE-CERT, CCN-CERT)
- [ ] Feeds de threat intelligence activos e integrados en el SIEM
- [ ] Reglas de deteccion mapeadas a MITRE ATT&CK para las 20 tecnicas mas frecuentes

{{< cta type="bofu" text="Solicita una demo personalizada para tu SOC y descubre como Riskitera automatiza el triage, la correlacion y el reporting con IA soberana." label="Solicitar demo" >}}


**Articulos relacionados:**
- [Como Montar Soc Desde Cero](/es/posts/2026/04/como-montar-soc-desde-cero/)
- [Threat Hunting Guia Practica](/es/posts/2026/04/threat-hunting-guia-practica/)

## Preguntas frecuentes

### Cuanto tiempo tiene una empresa para notificar un incidente de seguridad en Espana?

Depende del tipo de incidente. Si hay datos personales afectados, el RGPD exige notificacion a la AEPD en un maximo de 72 horas desde que se tiene conocimiento de la brecha. La Directiva NIS2 establece una alerta temprana en 24 horas y un informe completo en 72 horas para incidentes significativos. En el ambito del ENS, el CCN-CERT debe ser notificado segun la criticidad del incidente.

### Que diferencia hay entre un plan de respuesta y un playbook?

El plan de respuesta (IRP) es el documento marco: define roles, responsabilidades, cadena de comunicacion, criterios de severidad y politicas generales. Los playbooks son procedimientos operativos detallados para tipos de incidentes concretos (ransomware, phishing, DDoS). Un SOC necesita ambos: el plan dice "quien hace que y cuando escalar", el playbook dice "estos son los 15 pasos exactos para contener un ransomware".

### Es recomendable pagar el rescate en un ataque de ransomware?

La posicion unanime de INCIBE, CCN-CERT, Europol y la mayoria de expertos es no pagar. No garantiza la recuperacion de los datos, financia al grupo criminal y marca a la organizacion como objetivo futuro. Ademas, puede tener implicaciones legales (financiacion de terrorismo). La mejor defensa contra el ransomware son backups offline verificados, segmentacion de red y un plan de recuperacion probado.

### Que framework de respuesta a incidentes es mejor para una empresa espanola?

NIST SP 800-61 es la referencia internacional mas utilizada y la base de este articulo. Para empresas espanolas, se complementa con las guias CCN-STIC del CCN-CERT (obligatorias para el sector publico bajo el ENS) y los recursos de INCIBE (orientados al sector privado). ISO 27035 (Gestion de incidentes de seguridad de la informacion) es otra opcion, especialmente si la organizacion ya esta certificada en ISO 27001.

### Como se mide la eficacia de un equipo de respuesta a incidentes?

Las metricas clave son: MTTD (tiempo medio de deteccion), MTTC (tiempo medio de contencion) y MTTR (tiempo medio de recuperacion). Un SOC maduro deberia detectar incidentes en menos de 24 horas, contener en menos de 4 horas y recuperar servicios criticos en menos de 72 horas para incidentes P1. Ademas, se mide el porcentaje de post-mortems completados, las acciones de mejora cerradas en plazo y la frecuencia de simulacros.
