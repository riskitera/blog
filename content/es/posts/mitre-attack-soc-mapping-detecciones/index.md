---
title: "MITRE ATT&CK en el SOC: mapping de técnicas a detecciones reales"
image: "cover.png"
description: "Cómo mapear técnicas MITRE ATT&CK a detecciones operativas en el SOC: cobertura de la matriz, priorizar técnicas, crear dashboards y medir gaps de detección en tiempo real."
slug: "mitre-attack-soc-mapping-detecciones"
date: 2026-06-06
publishDate: 2026-06-06
lastmod: 2026-06-06
draft: false
tags: ["MITRE", "SOC", "Detection Engineering"]
categories: ["SOC"]
author: "David Moya"
keyword: "MITRE ATT&CK SOC"
funnel: "mofu"
---

Cómo mapear técnicas MITRE ATT&CK a detecciones operativas en el SOC: cobertura de la matriz, priorizar técnicas, crear dashboards y medir gaps de detección en tiempo real.

<!--more-->

{{< key-takeaways >}}
- El mapping de técnicas ATT&CK a detecciones reales permite medir objetivamente la cobertura defensiva del SOC y justificar inversiones ante dirección.
- ATT&CK Navigator genera heatmaps visuales que identifican gaps críticos en segundos, priorizando donde invertir esfuerzo en detection engineering.
- Las técnicas T1078 (Valid Accounts), T1059 (Command and Scripting Interpreter), T1021 (Remote Services) y T1110 (Brute Force) son prioridad absoluta para SOCs en España por su uso frecuente en campañas APT dirigidas.
- La metodología DeTT&CT estructura todo el proceso: desde inventariar fuentes de datos hasta puntuar la calidad de cada detección por técnica.
- Las reglas Sigma permiten escribir detecciones una sola vez y desplegarlas en cualquier SIEM, acelerando el time-to-detect de semanas a horas.
{{< /key-takeaways >}}

## ¿Por qué mapear detecciones a MITRE ATT&CK cambia las reglas del juego?

La mayoría de los SOC operan con un conjunto de reglas de detección heredadas que nadie sabe exactamente qué cubren. Se añaden alertas cuando ocurre un incidente, se copian reglas de repositorios públicos y, con el tiempo, se acumula un inventario de detecciones sin estructura ni priorización. El resultado: falsa sensación de seguridad.

[MITRE ATT&CK](https://attack.mitre.org/) resuelve este problema proporcionando un lenguaje común para catalogar comportamientos adversarios. No es una lista de vulnerabilidades ni un framework de compliance. Es un catálogo de tácticas, técnicas y procedimientos (TTPs) observados en ataques reales, organizado en una matriz que cubre desde el acceso inicial hasta la exfiltración de datos.

Cuando mapeas tus detecciones existentes a técnicas ATT&CK, obtienes algo que antes no tenías: **una foto objetiva de lo que detectas y lo que no**. Esa visibilidad transforma la forma de operar del SOC:

- **Priorización basada en evidencia.** En lugar de decidir qué regla escribir a continuación por intuición, priorizas las técnicas que usan los actores de amenaza relevantes para tu sector y geografía.
- **Comunicación con dirección.** Un heatmap de ATT&CK Navigator es mucho más convincente que una hoja de cálculo con 500 reglas de correlación. Dirección entiende rojo (gap) y verde (cubierto).
- **Medición de progreso.** Puedes medir trimestralmente cómo evoluciona tu cobertura. Si en Q1 cubrías el 35% de las técnicas de Initial Access y en Q3 llegas al 70%, tienes una métrica tangible.
- **Detección de redundancias.** Muchos SOC tienen 15 reglas para detectar port scanning y cero reglas para lateral movement vía WMI. El mapping revela esos desequilibrios.

El mapping no es un ejercicio teórico ni un proyecto de un mes. Es un proceso continuo que se integra en el flujo de trabajo diario del equipo de detection engineering.

## ¿Cómo se mapean detecciones a MITRE ATT&CK paso a paso?

El proceso de mapping tiene cinco fases. Cada una genera un artefacto que alimenta la siguiente.

### Fase 1: Inventariar detecciones existentes

Antes de mapear, necesitas saber qué tienes. Exporta todas las reglas activas de tu SIEM (Splunk, Elastic, Sentinel, QRadar) y clasifica cada una con estos campos mínimos:

- **ID de la regla** (el identificador interno del SIEM).
- **Nombre descriptivo** (qué comportamiento detecta).
- **Fuente de datos** (Windows Event Log, Sysmon, firewall logs, proxy logs, EDR telemetry).
- **Lógica de detección** (resumen de la condición: "Proceso cmd.exe lanzado desde winword.exe").
- **Estado** (activa, deshabilitada, en pruebas).

Un SOC típico de tamaño medio tiene entre 200 y 800 reglas activas. No te preocupes por la precisión del mapping en esta fase. El objetivo es tener el inventario completo.

### Fase 2: Asignar técnicas ATT&CK

Para cada regla, identifica la técnica o sub-técnica ATT&CK que mejor describe el comportamiento detectado. Algunas reglas mapearán directamente a una técnica (una regla que detecta `mimikatz` mapea a T1003.001, OS Credential Dumping: LSASS Memory). Otras serán ambiguas o cubrirán múltiples técnicas.

Reglas prácticas para el mapping:

- **Una regla puede mapear a varias técnicas.** Una regla que detecta PowerShell descargando y ejecutando un script cubre T1059.001 (PowerShell) y T1105 (Ingress Tool Transfer).
- **Usa sub-técnicas siempre que sea posible.** Mapear a T1059 (Command and Scripting Interpreter) es menos útil que mapear a T1059.001 (PowerShell) o T1059.003 (Windows Command Shell).
- **No fuerces el mapping.** Si una regla detecta un comportamiento que no encaja limpiamente en ninguna técnica, déjala sin mapear y revísala después. Es mejor un mapping preciso que uno completo pero inexacto.

### Fase 3: Evaluar calidad de la detección

No todas las detecciones son iguales. Una regla que busca el string "mimikatz" en la línea de comandos es trivial de evadir. Una regla que detecta accesos sospechosos a LSASS basándose en la secuencia de API calls es mucho más robusta. La metodología DeTT&CT (que veremos en detalle más adelante) propone una escala del 0 al 5:

| Puntuación | Significado |
|---|---|
| 0 | Sin detección |
| 1 | Básica: búsqueda de strings o hashes conocidos |
| 2 | Justa: correlación simple de eventos |
| 3 | Buena: lógica multi-evento con contexto |
| 4 | Muy buena: detección de comportamiento resiliente a evasión básica |
| 5 | Excelente: detección basada en anomalías o comportamiento que resiste técnicas anti-forenses |

### Fase 4: Cargar en ATT&CK Navigator

[ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) es la herramienta visual oficial de MITRE para trabajar con la matriz. Permite crear capas (layers) que colorean cada técnica según un valor numérico. El flujo es:

1. **Crear una nueva capa** seleccionando la versión de ATT&CK y la plataforma (Enterprise, Mobile, ICS).
2. **Asignar scores** a cada técnica basándote en tu inventario. Score 0 para técnicas sin cobertura, 1-5 según la calidad de la detección.
3. **Configurar gradiente de colores.** Rojo para scores bajos, amarillo para medios, verde para altos. El resultado es un heatmap inmediato de tu postura defensiva.
4. **Exportar como JSON.** El formato JSON permite versionar las capas en Git, comparar entre trimestres y automatizar la actualización.

Un ejemplo práctico: si tu SOC tiene 50 reglas mapeadas y cubren 35 de las 201 técnicas de Enterprise ATT&CK v16, el heatmap mostrará un 83% de la matriz en rojo. Esa imagen vale más que cualquier informe de 50 páginas.

### Fase 5: Iterar y mantener

El mapping no es un proyecto con fecha de fin. Cada vez que el equipo de detection engineering escribe una nueva regla, debe incluir el mapping ATT&CK como campo obligatorio. Cada vez que MITRE publica una nueva versión de la matriz (normalmente dos veces al año), hay que revisar si los IDs de técnicas han cambiado.

## ¿Qué técnicas priorizar según tu perfil de amenaza?

La matriz ATT&CK Enterprise v16 tiene más de 200 técnicas y 680 sub-técnicas. Ninguna organización puede cubrir todo. La clave está en priorizar las técnicas que usan los actores de amenaza más relevantes para tu contexto.

### Priorización por actores que atacan España

Los grupos APT que han dirigido campañas contra organizaciones españolas en los últimos años incluyen:

- **APT28 (Fancy Bear / Sofacy).** Activo contra gobiernos europeos, defensa y think tanks. Técnicas prioritarias: T1566.001 (Spearphishing Attachment), T1059.001 (PowerShell), T1078 (Valid Accounts), T1071.001 (Web Protocols para C2).
- **APT29 (Cozy Bear).** Enfocado en sectores gubernamentales y diplomáticos. Destaca por T1195.002 (Supply Chain Compromise vía software), T1036 (Masquerading) y T1070 (Indicator Removal).
- **Grupos de ransomware (Lockbit, BlackCat/ALPHV, Cl0p).** Afectan a empresas españolas de todos los tamaños. Técnicas críticas: T1486 (Data Encrypted for Impact), T1021.002 (SMB/Windows Admin Shares), T1110 (Brute Force), T1078 (Valid Accounts).
- **Actores de ciberespionaje vinculados a China (APT31, Mustang Panda).** Con interés en propiedad intelectual europea. Usan T1059.005 (Visual Basic), T1547.001 (Registry Run Keys) y T1041 (Exfiltration Over C2 Channel).

La recomendación práctica: cruza los reportes de [CCN-CERT](https://www.ccn-cert.cni.es/) sobre amenazas nacionales con los perfiles de grupos en ATT&CK para obtener tu lista priorizada de técnicas.

### Las cuatro técnicas que todo SOC en España debe cubrir primero

Independientemente de tu sector, estas cuatro técnicas aparecen en la gran mayoría de intrusiones reales reportadas en España:

**T1078: Valid Accounts.** El uso de credenciales legítimas robadas es la vía de entrada más común. No genera alertas de exploit ni tráfico anómalo porque el atacante "es" un usuario válido. Detecciones clave:

- Login desde geolocalizaciones imposibles (impossible travel).
- Login fuera de horario habitual del usuario.
- Primera vez que una cuenta accede a un servidor crítico.
- Múltiples logins desde IPs distintas en ventana corta.

**T1059: Command and Scripting Interpreter.** PowerShell, cmd, bash, Python: los intérpretes de comandos son la herramienta favorita post-compromiso. Sub-técnicas a cubrir:

- T1059.001 (PowerShell): ejecución con `-EncodedCommand`, bypass de execution policy, descarga de scripts remotos con `IEX(New-Object Net.WebClient)`.
- T1059.003 (Windows Command Shell): `cmd.exe` lanzado como hijo de procesos inusuales (Word, Excel, Outlook).
- T1059.005 (Visual Basic): macros que invocan `Shell()` o `WScript.Shell`.

**T1021: Remote Services.** El movimiento lateral a través de servicios remotos legítimos es la segunda fase crítica de cualquier intrusión. Sub-técnicas prioritarias:

- T1021.001 (Remote Desktop Protocol): conexiones RDP desde estaciones de trabajo a servidores no habituales.
- T1021.002 (SMB/Windows Admin Shares): acceso a `C$` o `ADMIN$` desde hosts no administrativos.
- T1021.006 (Windows Remote Management): uso de WinRM/WMI para ejecución remota.

**T1110: Brute Force.** Los ataques de fuerza bruta contra servicios expuestos (RDP, VPN, OWA, SSH) siguen siendo efectivos porque muchas organizaciones no implementan bloqueo de cuentas o MFA. Detecciones:

- Más de N intentos fallidos en ventana de M minutos desde una misma IP.
- Patrón de password spraying: un intento por cuenta con la misma contraseña.
- Incremento anómalo de eventos 4625 (Windows) o auth failures en VPN.

## ¿Cómo escribir reglas de detección por técnica con Sigma?

[Sigma](https://github.com/SigmaHQ/sigma) es el formato estándar para escribir reglas de detección independientes del SIEM. Escribes la lógica una vez en YAML y luego la conviertes a la query nativa de tu plataforma (Splunk SPL, Elastic KQL, Sentinel KQL, QRadar AQL).

### Anatomía de una regla Sigma

```yaml
title: Suspicious PowerShell Download Cradle
image: "cover.png"
id: 3b6ab547-1234-5678-9abc-def012345678
status: experimental
description: >
  Detecta el uso de PowerShell para descargar y ejecutar
  scripts remotos, patrón común en Initial Access y Execution.
references:
  - https://attack.mitre.org/techniques/T1059/001/
  - https://attack.mitre.org/techniques/T1105/
author: SOC Team
date: 2026/06/01
tags:
  - attack.execution
  - attack.t1059.001
  - attack.command_and_control
  - attack.t1105
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    Image|endswith: '\powershell.exe'
    CommandLine|contains|all:
      - 'Net.WebClient'
      - 'DownloadString'
  condition: selection
falsepositives:
  - Administradores usando scripts de despliegue legítimos
level: high
```

Los campos clave para el mapping ATT&CK son los **tags**. El prefijo `attack.` seguido de la táctica (execution) y la técnica (t1059.001) vincula la regla directamente con la matriz.

### Ejemplo: regla para T1078 (Valid Accounts, impossible travel)

```yaml
title: Login desde geolocalización imposible
image: "cover.png"
id: a1b2c3d4-5678-90ab-cdef-123456789abc
status: experimental
description: >
  Detecta logins exitosos desde dos ubicaciones geográficas
  incompatibles en una ventana de tiempo corta.
tags:
  - attack.initial_access
  - attack.t1078
logsource:
  product: azure
  service: signinlogs
detection:
  selection:
    ResultType: 0
  timeframe: 60m
  condition: selection | count(Location) by UserPrincipalName > 1
  filter:
    - VPN conocida
level: high
```

Esta regla es conceptual (la lógica real de impossible travel requiere cálculo de distancia y velocidad), pero ilustra cómo vincular una detección operativa con una técnica ATT&CK específica.

### Ejemplo: regla para T1110 (Brute Force)

```yaml
title: Password Spraying contra Active Directory
image: "cover.png"
id: b2c3d4e5-6789-01ab-cdef-234567890abc
status: experimental
description: >
  Detecta intentos de password spraying: misma contraseña
  probada contra múltiples cuentas en ventana corta.
tags:
  - attack.credential_access
  - attack.t1110.003
logsource:
  product: windows
  service: security
detection:
  selection:
    EventID: 4625
    SubStatus: '0xC000006A'  # Wrong password
  timeframe: 10m
  condition: selection | count(TargetUserName) by IpAddress > 15
falsepositives:
  - Escáner de vulnerabilidades interno
level: high
```

### El ecosistema Sigma en la práctica

El repositorio oficial de Sigma contiene más de 3.000 reglas mantenidas por la comunidad, ya mapeadas a técnicas ATT&CK. Antes de escribir una regla desde cero, busca si ya existe una en el repositorio que puedas adaptar. La herramienta `sigma-cli` convierte las reglas al formato de tu SIEM:

```bash
# Convertir regla Sigma a Splunk SPL
sigma convert -t splunk -p sysmon regla.yml

# Convertir a Elastic/Lucene
sigma convert -t elasticsearch -p ecs-windows regla.yml

# Convertir a Microsoft Sentinel KQL
sigma convert -t microsoft365defender regla.yml
```

## La metodología DeTT&CT: estructura profesional para el mapping

DeTT&CT (Detect Tactics, Techniques & Combat Threats) es una metodología creada por Marcus Bakker y Ruben Bouman que formaliza todo el proceso de mapping de detecciones a ATT&CK. Se compone de dos pilares:

### Pilar 1: Data Source Assessment

Antes de hablar de detecciones, DeTT&CT te obliga a responder: **¿qué datos tienes realmente disponibles?** Porque no puedes detectar ejecución de PowerShell si no recoges los Event IDs adecuados (4103, 4104 para Script Block Logging).

El data source assessment asigna a cada fuente de datos una puntuación de calidad:

| Score | Calidad de datos |
|---|---|
| 0 | No recogidos |
| 1 | Recogidos pero sin parsear o normalizar |
| 2 | Parseados y normalizados |
| 3 | Parseados, normalizados y con campos enriquecidos |
| 4 | Alta calidad: cobertura completa, parseado robusto, enriquecimiento |
| 5 | Excelente: monitorización completa con validación periódica de integridad |

Ejemplo: si recoges Windows Security Event Logs pero solo tienes habilitados los Event IDs por defecto (sin auditing avanzado, sin Sysmon), tu score de data source para "Process Creation" será un 1 o 2, no un 4.

### Pilar 2: Detection Assessment

Una vez sabes qué datos tienes, evalúas la calidad de las detecciones que has construido sobre esos datos. DeTT&CT usa la misma escala del 0 al 5 descrita anteriormente, pero añade dos dimensiones:

- **Detection score.** Calidad técnica de la regla (de string matching básico a detección comportamental).
- **Detection applicability.** Cobertura dentro de la técnica. Una técnica como T1059 tiene 8 sub-técnicas. Si solo detectas T1059.001 (PowerShell), tu applicability es parcial.

### Workflow DeTT&CT completo

1. **Crear el fichero YAML de data sources.** Lista todas tus fuentes de telemetría con su score de calidad.
2. **Crear el fichero YAML de detecciones.** Lista todas tus reglas con su score de calidad y las técnicas mapeadas.
3. **Ejecutar las herramientas DeTT&CT.** El framework genera automáticamente las capas de ATT&CK Navigator combinando ambos ficheros.
4. **Generar el gap analysis.** La superposición de la capa de data sources y la capa de detecciones revela dónde tienes datos pero no detecciones (oportunidad rápida) y dónde no tienes ni datos (requiere despliegue de nueva telemetría).

El resultado son tres capas de Navigator:

- **Capa de visibilidad (data sources).** Qué técnicas podrías detectar con los datos que ya tienes.
- **Capa de detección.** Qué técnicas detectas realmente con tus reglas actuales.
- **Capa de gap.** La diferencia entre ambas. Esta es la capa más valiosa: muestra el "low hanging fruit" (técnicas donde tienes datos pero no has escrito detecciones).

## ¿Cómo crear un dashboard de cobertura ATT&CK?

Un heatmap estático en Navigator es útil para reuniones trimestrales, pero el SOC necesita visibilidad en tiempo real. La solución es construir un dashboard operativo que se actualice automáticamente.

### Arquitectura del dashboard

El dashboard necesita tres componentes:

1. **Base de datos de mapping.** Una tabla que vincula cada regla del SIEM con sus técnicas ATT&CK. Puede ser una tabla en PostgreSQL, un Google Sheet o un fichero YAML en Git. Lo importante es que sea la fuente única de verdad.
2. **Script de sincronización.** Un proceso automático que lee las reglas activas del SIEM vía API, cruza con la base de datos de mapping y calcula los scores actuales.
3. **Visualización.** Grafana, Kibana o cualquier herramienta de dashboarding que consuma los datos calculados.

### Métricas esenciales del dashboard

El dashboard debe responder a estas preguntas con un vistazo:

- **Cobertura por táctica.** Porcentaje de técnicas cubiertas en cada táctica (Initial Access, Execution, Persistence, etc.). Gráfico de barras horizontal.
- **Cobertura por actor.** Si tu threat profile incluye APT28 y Lockbit, muestra el porcentaje de sus técnicas favoritas que cubres. Gráfico radar.
- **Evolución temporal.** Cómo ha cambiado la cobertura en los últimos 6-12 meses. Línea temporal por táctica.
- **Top gaps.** Las 10 técnicas con score 0 que más actores relevantes usan. Tabla priorizada.
- **Reglas por calidad.** Distribución de reglas por score de detección (1-5). Donut chart.

### Ejemplo práctico con Elastic y Grafana

Si usas Elastic Security, muchas de sus reglas pre-built ya incluyen tags ATT&CK. Puedes extraerlas vía API:

```bash
# Listar reglas con sus tags ATT&CK
curl -X GET "https://elastic:9200/.kibana/_search" \
  -H "Content-Type: application/json" \
  -d '{
    "query": {
      "term": { "type": "alert" }
    },
    "_source": ["alert.name", "alert.tags", "alert.enabled"]
  }'
```

Con esa información, un script Python puede generar un JSON compatible con Navigator y actualizar Grafana vía la API de datasources.

## ¿Cómo identificar y cerrar gaps de detección?

Identificar gaps es la mitad del trabajo. Cerrarlos requiere un proceso estructurado que no sobrecargue al equipo.

### El framework de priorización de gaps

No todos los gaps son iguales. Un gap en T1486 (Data Encrypted for Impact, ransomware) es crítico. Un gap en T1612 (Build Image on Host, containers) puede ser irrelevante si no usas contenedores en producción. El framework de priorización debe considerar:

1. **Prevalencia en actores relevantes.** ¿Cuántos de tus threat actors priorizados usan esta técnica? Si la usan 3 de 4, prioridad alta.
2. **Impacto potencial.** ¿Qué pasa si esta técnica se ejecuta sin detectar? Un T1486 sin detectar significa ransomware desplegado. Un T1087 (Account Discovery) sin detectar es grave pero no catastrófico por sí solo.
3. **Disponibilidad de datos.** ¿Tienes la telemetría necesaria? Si necesitas Sysmon y no lo tienes desplegado, el gap es más costoso de cerrar.
4. **Existencia de reglas públicas.** ¿Hay reglas Sigma o detecciones de tu vendor que puedas adaptar? Si sí, el coste de cierre es bajo.

### Proceso de cierre de un gap

Para cada gap priorizado:

1. **Verificar data sources.** Confirmar que la telemetría llega al SIEM, está parseada y es de calidad suficiente.
2. **Buscar reglas existentes.** Revisar el repositorio Sigma, las detecciones del vendor de tu SIEM y los repositorios de la comunidad (Elastic Detection Rules, Splunk Security Content).
3. **Adaptar o escribir la regla.** Si existe una regla pública, adaptarla a tu entorno (ajustar exclusiones, umbrales, campos). Si no existe, escribirla desde cero.
4. **Testear con emulación.** Ejecutar la técnica en un entorno de laboratorio (Atomic Red Team, Caldera) y verificar que la regla genera la alerta esperada.
5. **Desplegar en modo monitor.** Activar la regla sin generar tickets durante 1-2 semanas para calibrar falsos positivos.
6. **Activar en producción.** Mover la regla a producción y actualizar el mapping en la base de datos.

### Herramientas de emulación para validar detecciones

La emulación de adversarios es el complemento indispensable del detection engineering. Las herramientas principales:

- **Atomic Red Team.** Colección de tests atómicos mapeados a técnicas ATT&CK. Ejecutas un test y verificas si tu SIEM genera la alerta. Ideal para validación rápida.
- **MITRE Caldera.** Plataforma de emulación automatizada. Permite encadenar múltiples técnicas en una operación completa (kill chain) y evaluar la detección end-to-end.
- **Red Canary.** Proporciona tests validados con buena documentación de los artefactos que debería generar cada técnica.

## ¿Qué fuentes de telemetría necesitas por táctica?

La telemetría es el combustible del detection engineering. Sin los datos adecuados, las mejores reglas no pueden funcionar. Esta tabla resume las fuentes críticas por táctica:

| Táctica | Fuentes de datos críticas |
|---|---|
| Initial Access | Email gateway logs, proxy/web logs, DNS logs |
| Execution | Process creation (Sysmon EID 1), PowerShell logging (EID 4103/4104), script execution |
| Persistence | Registry changes (Sysmon EID 13), scheduled tasks (EID 4698), service creation (EID 7045) |
| Privilege Escalation | Token manipulation events, UAC bypass indicators, service config changes |
| Defense Evasion | Process injection (Sysmon EID 8/10), file masquerading, timestomping |
| Credential Access | LSASS access (Sysmon EID 10), Kerberos events (EID 4768/4769), auth failures (EID 4625) |
| Discovery | LDAP queries, net.exe/nltest.exe execution, WMI queries |
| Lateral Movement | RDP connections (EID 4624 type 10), SMB access, WinRM sessions, PsExec artifacts |
| Collection | Clipboard access, screen capture, staging in temp directories |
| Command and Control | DNS anomalies, beaconing patterns en proxy logs, connections a IPs sospechosas |
| Exfiltration | DLP alerts, volumen anómalo de upload, conexiones a servicios cloud no corporativos |
| Impact | Volume Shadow Copy deletion, mass file encryption, service stops |

### La importancia de Sysmon

Si solo pudieras desplegar una herramienta adicional de telemetría, debería ser Sysmon. Con una configuración adecuada (la config de SwiftOnSecurity o la de Olaf Hartong son buenos puntos de partida), Sysmon proporciona:

- Creación de procesos con línea de comandos completa y hash.
- Conexiones de red por proceso.
- Modificaciones de registro.
- Carga de DLLs.
- Acceso a procesos (crítico para detectar credential dumping).
- Creación de ficheros con hash.

Estos eventos cubren directamente más de 80 técnicas ATT&CK. Sin Sysmon (o un EDR equivalente), la mayoría de técnicas de Execution, Defense Evasion y Credential Access son invisibles.

## ¿Cómo automatizar el mapping de detecciones?

El mapping manual es necesario al principio, pero no escala. Un SOC maduro automatiza la mayor parte del proceso.

### Automatización con CI/CD para reglas de detección

El concepto de "Detection as Code" aplica las prácticas de ingeniería de software al detection engineering:

1. **Repositorio Git de reglas.** Todas las reglas Sigma viven en un repositorio con estructura de directorios por táctica ATT&CK.
2. **Validación automática en CI.** Cada pull request ejecuta tests: sintaxis YAML válida, técnica ATT&CK existente, campos obligatorios presentes (tags, falsepositives, level).
3. **Conversión automática.** El pipeline convierte las reglas Sigma al formato del SIEM de destino y las despliega vía API.
4. **Actualización del mapping.** Al mergear una regla nueva, el pipeline actualiza automáticamente la base de datos de mapping y regenera la capa de Navigator.

```yaml
# .github/workflows/detection-pipeline.yml (ejemplo conceptual)
name: Detection Pipeline
on:
  push:
    paths:
      - 'rules/**/*.yml'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate Sigma rules
        run: sigma check rules/
      - name: Convert to SIEM format
        run: sigma convert -t splunk rules/ -o output/
      - name: Update ATT&CK mapping
        run: python scripts/update_mapping.py
      - name: Deploy to SIEM
        run: python scripts/deploy_rules.py
```

### Integración con threat intelligence

Cuando tu equipo de CTI publica un informe sobre un nuevo actor de amenaza, el flujo ideal es:

1. El analista CTI extrae las técnicas ATT&CK del informe.
2. Un script cruza esas técnicas con tu matriz de cobertura actual.
3. Se genera automáticamente un informe de gap analysis específico para ese actor.
4. El equipo de detection engineering recibe un listado priorizado de reglas a escribir.

Este ciclo cierra el loop entre inteligencia y operaciones, que es donde la mayoría de los SOC fallan.

{{< cta type="tofu" text="Riskitera automatiza el triage, la correlación y el reporting de tu SOC con IA soberana. Conecta tu MITRE ATT&CK mapping con detecciones operativas en minutos." label="Ver demo SOC" >}}

## ¿Qué métricas de cobertura ATT&CK debes medir?

Las métricas transforman el mapping de un ejercicio académico en una herramienta de gestión. Estas son las métricas que recomendamos medir mensualmente:

### Métricas de cobertura

- **Cobertura global.** Porcentaje de técnicas de la matriz con al menos una detección (score >= 1). Meta razonable: 40-60% para un SOC maduro.
- **Cobertura por táctica.** Desglose por las 14 tácticas. Las tácticas de Initial Access, Execution y Lateral Movement deberían tener mayor cobertura.
- **Cobertura ponderada por amenaza.** Porcentaje de las técnicas de tus top 5 actores que cubres. Esta es la métrica más relevante para el negocio.
- **Profundidad de cobertura.** Distribución de scores (cuántas técnicas en score 1, cuántas en 2, etc.). Más útil que el simple binario cubierto/no cubierto.

### Métricas de operación

- **Mean Time to Detect (MTTD) por técnica.** Cuánto tarda tu SOC en detectar cada técnica cuando se emula. Medido con ejercicios de purple team.
- **Tasa de falsos positivos por regla.** Reglas con más del 80% de falsos positivos son candidatas a reescritura o desactivación.
- **Reglas desactivadas.** Porcentaje de reglas mapeadas que están deshabilitadas. Si es alto (>20%), tienes un problema de calidad.
- **Tiempo medio de cierre de gap.** Desde que se identifica un gap hasta que la regla está en producción. Meta: menos de 2 semanas para gaps con datos disponibles.

### Métricas de madurez

- **Porcentaje de reglas en formato estándar (Sigma).** Mide la portabilidad de tus detecciones.
- **Porcentaje de reglas con test de emulación.** Mide la validación de tus detecciones.
- **Frecuencia de actualización del mapping.** Si se actualiza solo una vez al año, no es útil operativamente.

## Errores comunes al mapear detecciones a ATT&CK

Después de trabajar con múltiples SOC, estos son los errores que vemos con más frecuencia:

1. **Mapear por obligación, no por utilidad.** Si el mapping es un checkbox de compliance que nadie consulta, no aporta valor. El mapping debe alimentar decisiones operativas semanales.
2. **Inflar los scores de detección.** Poner score 4 a una regla que busca un hash específico de mimikatz es autoengaño. Sé honesto con la calidad.
3. **Ignorar la calidad de los datos.** Una regla perfecta sobre datos incompletos o mal parseados genera más problemas que soluciones.
4. **No incluir al equipo de threat intelligence.** El mapping sin contexto de amenaza es un ejercicio académico. El equipo de CTI aporta la priorización basada en actores reales.
5. **Tratar el mapping como un proyecto con fin.** Es un proceso continuo. Si se abandona después de la foto inicial, pierde todo su valor en 6 meses.

{{< cta type="bofu" text="Solicita una demo personalizada para tu SOC y descubre cómo Riskitera conecta ATT&CK mapping con detecciones operativas, priorización por amenaza y métricas en tiempo real." label="Solicitar demo" >}}


**Artículos relacionados:**
- [Mitre Attack Que Es Como Usarlo](/es/posts/2026/04/mitre-attack-que-es-como-usarlo/)
- [Cómo Montar Soc Desde Cero](/es/posts/2026/04/como-montar-soc-desde-cero/)

## Preguntas frecuentes

### ¿Cuánto tiempo se tarda en hacer el primer mapping completo de detecciones a ATT&CK?

Depende del tamaño del SOC. Para un equipo con 200-500 reglas activas, el inventario y mapping inicial requiere entre 2 y 4 semanas dedicando unas 4 horas diarias. La mayor parte del tiempo se invierte en las primeras 100 reglas, porque el equipo todavía está aprendiendo las técnicas. Después el ritmo se acelera. Lo importante es no intentar hacerlo perfecto a la primera: un mapping al 80% de precisión que se completa en 3 semanas es más útil que uno perfecto que tarda 3 meses.

### ¿Necesito un SIEM comercial para implementar detection engineering basada en ATT&CK?

No es imprescindible. Puedes implementar el mapping con herramientas open source. Elastic Security (con licencia básica gratuita) soporta reglas con tags ATT&CK. Wazuh incluye decoders y reglas mapeadas. Sigma te permite escribir reglas portables. Lo que sí necesitas es telemetría de calidad: sin Sysmon o un EDR que recoja eventos de proceso, red y registro, el mapping será superficial independientemente del SIEM.

### ¿Cómo convenzo a dirección de que el mapping ATT&CK merece recursos dedicados?

El argumento más efectivo es visual. Genera un heatmap de Navigator con la cobertura actual (la mayoría será roja) y superpone las técnicas usadas por los actores que han atacado a empresas de tu sector en España (datos de CCN-CERT e INCIBE). La intersección entre "técnicas que nos atacan" y "técnicas que no detectamos" es el argumento de negocio. Complementa con un cálculo de coste: si un incidente de ransomware cuesta de media 1.5M EUR (dato de INCIBE para PYMES), invertir 50-100 horas de equipo en cerrar los gaps críticos es trivial en comparación.

### ¿Con qué frecuencia debo actualizar el mapping de detecciones?

El mapping debe actualizarse en tres momentos: (1) cuando se añade o modifica una regla de detección, como parte del proceso estándar; (2) cuando MITRE publica una nueva versión de la matriz (normalmente abril y octubre), para verificar cambios en IDs de técnicas; y (3) trimestralmente, con una revisión completa de scores de detección que incluya tests de emulación con Atomic Red Team o Caldera.

### ¿Cuál es la diferencia entre ATT&CK Navigator y DeTT&CT?

ATT&CK Navigator es una herramienta de visualización: crea capas de colores sobre la matriz ATT&CK. DeTT&CT es una metodología y conjunto de herramientas que va más allá: estructura la evaluación de data sources (qué telemetría tienes y con qué calidad) y detecciones (qué reglas tienes y cómo de robustas son), generando automáticamente las capas de Navigator. En resumen, Navigator es el lienzo; DeTT&CT es el proceso completo para pintarlo con datos reales.
