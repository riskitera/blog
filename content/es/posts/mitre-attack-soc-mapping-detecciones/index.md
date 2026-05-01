---
title: "MITRE ATT&CK en el SOC: mapping de tecnicas a detecciones reales"
description: "Como mapear tecnicas MITRE ATT&CK a detecciones operativas en el SOC: cobertura de la matriz, priorizar tecnicas, crear dashboards y medir gaps de deteccion en tiempo real."
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

Como mapear tecnicas MITRE ATT&CK a detecciones operativas en el SOC: cobertura de la matriz, priorizar tecnicas, crear dashboards y medir gaps de deteccion en tiempo real.

<!--more-->

{{< key-takeaways >}}
- El mapping de tecnicas ATT&CK a detecciones reales permite medir objetivamente la cobertura defensiva del SOC y justificar inversiones ante direccion.
- ATT&CK Navigator genera heatmaps visuales que identifican gaps criticos en segundos, priorizando donde invertir esfuerzo en detection engineering.
- Las tecnicas T1078 (Valid Accounts), T1059 (Command and Scripting Interpreter), T1021 (Remote Services) y T1110 (Brute Force) son prioridad absoluta para SOCs en Espana por su uso frecuente en campanas APT dirigidas.
- La metodologia DeTT&CT estructura todo el proceso: desde inventariar fuentes de datos hasta puntuar la calidad de cada deteccion por tecnica.
- Las reglas Sigma permiten escribir detecciones una sola vez y desplegarlas en cualquier SIEM, acelerando el time-to-detect de semanas a horas.
{{< /key-takeaways >}}

## Por que mapear detecciones a MITRE ATT&CK cambia las reglas del juego

La mayoria de los SOC operan con un conjunto de reglas de deteccion heredadas que nadie sabe exactamente que cubren. Se anaden alertas cuando ocurre un incidente, se copian reglas de repositorios publicos y, con el tiempo, se acumula un inventario de detecciones sin estructura ni priorizacion. El resultado: falsa sensacion de seguridad.

[MITRE ATT&CK](https://attack.mitre.org/) resuelve este problema proporcionando un lenguaje comun para catalogar comportamientos adversarios. No es una lista de vulnerabilidades ni un framework de compliance. Es un catalogo de tacticas, tecnicas y procedimientos (TTPs) observados en ataques reales, organizado en una matriz que cubre desde el acceso inicial hasta la exfiltracion de datos.

Cuando mapeas tus detecciones existentes a tecnicas ATT&CK, obtienes algo que antes no tenias: **una foto objetiva de lo que detectas y lo que no**. Esa visibilidad transforma la forma de operar del SOC:

- **Priorizacion basada en evidencia.** En lugar de decidir que regla escribir a continuacion por intuicion, priorizas las tecnicas que usan los actores de amenaza relevantes para tu sector y geografia.
- **Comunicacion con direccion.** Un heatmap de ATT&CK Navigator es mucho mas convincente que una hoja de calculo con 500 reglas de correlacion. Direccion entiende rojo (gap) y verde (cubierto).
- **Medicion de progreso.** Puedes medir trimestralmente como evoluciona tu cobertura. Si en Q1 cubrias el 35% de las tecnicas de Initial Access y en Q3 llegas al 70%, tienes una metrica tangible.
- **Deteccion de redundancias.** Muchos SOC tienen 15 reglas para detectar port scanning y cero reglas para lateral movement via WMI. El mapping revela esos desequilibrios.

El mapping no es un ejercicio teorico ni un proyecto de un mes. Es un proceso continuo que se integra en el flujo de trabajo diario del equipo de detection engineering.

## Como se mapean detecciones a MITRE ATT&CK paso a paso

El proceso de mapping tiene cinco fases. Cada una genera un artefacto que alimenta la siguiente.

### Fase 1: Inventariar detecciones existentes

Antes de mapear necesitas saber que tienes. Exporta todas las reglas activas de tu SIEM (Splunk, Elastic, Sentinel, QRadar) y clasifica cada una con estos campos minimos:

- **ID de la regla** (el identificador interno del SIEM).
- **Nombre descriptivo** (que comportamiento detecta).
- **Fuente de datos** (Windows Event Log, Sysmon, firewall logs, proxy logs, EDR telemetry).
- **Logica de deteccion** (resumen de la condicion: "Proceso cmd.exe lanzado desde winword.exe").
- **Estado** (activa, deshabilitada, en pruebas).

Un SOC tipico de tamano medio tiene entre 200 y 800 reglas activas. No te preocupes por la precision del mapping en esta fase. El objetivo es tener el inventario completo.

### Fase 2: Asignar tecnicas ATT&CK

Para cada regla, identifica la tecnica o sub-tecnica ATT&CK que mejor describe el comportamiento detectado. Algunas reglas mapearan directamente a una tecnica (una regla que detecta `mimikatz` mapea a T1003.001, OS Credential Dumping: LSASS Memory). Otras seran ambiguas o cubriran multiples tecnicas.

Reglas practicas para el mapping:

- **Una regla puede mapear a varias tecnicas.** Una regla que detecta PowerShell descargando y ejecutando un script cubre T1059.001 (PowerShell) y T1105 (Ingress Tool Transfer).
- **Usa sub-tecnicas siempre que sea posible.** Mapear a T1059 (Command and Scripting Interpreter) es menos util que mapear a T1059.001 (PowerShell) o T1059.003 (Windows Command Shell).
- **No fuerces el mapping.** Si una regla detecta un comportamiento que no encaja limpiamente en ninguna tecnica, dejala sin mapear y revisala despues. Es mejor un mapping preciso que uno completo pero inexacto.

### Fase 3: Evaluar calidad de la deteccion

No todas las detecciones son iguales. Una regla que busca el string "mimikatz" en la linea de comandos es trivial de evadir. Una regla que detecta accesos sospechosos a LSASS basandose en la secuencia de API calls es mucho mas robusta. La metodologia DeTT&CT (que veremos en detalle mas adelante) propone una escala del 0 al 5:

| Puntuacion | Significado |
|---|---|
| 0 | Sin deteccion |
| 1 | Basica: busqueda de strings o hashes conocidos |
| 2 | Justa: correlacion simple de eventos |
| 3 | Buena: logica multi-evento con contexto |
| 4 | Muy buena: deteccion de comportamiento resiliente a evasion basica |
| 5 | Excelente: deteccion basada en anomalias o comportamiento que resiste tecnicas anti-forenses |

### Fase 4: Cargar en ATT&CK Navigator

[ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) es la herramienta visual oficial de MITRE para trabajar con la matriz. Permite crear capas (layers) que colorean cada tecnica segun un valor numerico. El flujo es:

1. **Crear una nueva capa** seleccionando la version de ATT&CK y la plataforma (Enterprise, Mobile, ICS).
2. **Asignar scores** a cada tecnica basandote en tu inventario. Score 0 para tecnicas sin cobertura, 1-5 segun la calidad de la deteccion.
3. **Configurar gradiente de colores.** Rojo para scores bajos, amarillo para medios, verde para altos. El resultado es un heatmap inmediato de tu postura defensiva.
4. **Exportar como JSON.** El formato JSON permite versionar las capas en Git, comparar entre trimestres y automatizar la actualizacion.

Un ejemplo practico: si tu SOC tiene 50 reglas mapeadas y cubren 35 de las 201 tecnicas de Enterprise ATT&CK v16, el heatmap mostrara un 83% de la matriz en rojo. Esa imagen vale mas que cualquier informe de 50 paginas.

### Fase 5: Iterar y mantener

El mapping no es un proyecto con fecha de fin. Cada vez que el equipo de detection engineering escribe una nueva regla, debe incluir el mapping ATT&CK como campo obligatorio. Cada vez que MITRE publica una nueva version de la matriz (normalmente dos veces al ano), hay que revisar si los IDs de tecnicas han cambiado.

## Que tecnicas priorizar segun tu perfil de amenaza

La matriz ATT&CK Enterprise v16 tiene mas de 200 tecnicas y 680 sub-tecnicas. Ninguna organizacion puede cubrir todo. La clave esta en priorizar las tecnicas que usan los actores de amenaza mas relevantes para tu contexto.

### Priorizacion por actores que atacan Espana

Los grupos APT que han dirigido campanas contra organizaciones espanolas en los ultimos anos incluyen:

- **APT28 (Fancy Bear / Sofacy).** Activo contra gobiernos europeos, defensa y think tanks. Tecnicas prioritarias: T1566.001 (Spearphishing Attachment), T1059.001 (PowerShell), T1078 (Valid Accounts), T1071.001 (Web Protocols para C2).
- **APT29 (Cozy Bear).** Enfocado en sectores gubernamentales y diplomaticos. Destaca por T1195.002 (Supply Chain Compromise via software), T1036 (Masquerading) y T1070 (Indicator Removal).
- **Grupos de ransomware (Lockbit, BlackCat/ALPHV, Cl0p).** Afectan a empresas espanolas de todos los tamanos. Tecnicas criticas: T1486 (Data Encrypted for Impact), T1021.002 (SMB/Windows Admin Shares), T1110 (Brute Force), T1078 (Valid Accounts).
- **Actores de ciberespionaje vinculados a China (APT31, Mustang Panda).** Con interes en propiedad intelectual europea. Usan T1059.005 (Visual Basic), T1547.001 (Registry Run Keys) y T1041 (Exfiltration Over C2 Channel).

La recomendacion practica: cruza los reportes de [CCN-CERT](https://www.ccn-cert.cni.es/) sobre amenazas nacionales con los perfiles de grupos en ATT&CK para obtener tu lista priorizada de tecnicas.

### Las cuatro tecnicas que todo SOC en Espana debe cubrir primero

Independientemente de tu sector, estas cuatro tecnicas aparecen en la gran mayoria de intrusiones reales reportadas en Espana:

**T1078: Valid Accounts.** El uso de credenciales legitimas robadas es la via de entrada mas comun. No genera alertas de exploit ni trafico anomalo porque el atacante "es" un usuario valido. Detecciones clave:

- Login desde geolocalizaciones imposibles (impossible travel).
- Login fuera de horario habitual del usuario.
- Primera vez que una cuenta accede a un servidor critico.
- Multiples logins desde IPs distintas en ventana corta.

**T1059: Command and Scripting Interpreter.** PowerShell, cmd, bash, Python: los interpretes de comandos son la herramienta favorita post-compromiso. Sub-tecnicas a cubrir:

- T1059.001 (PowerShell): ejecucion con `-EncodedCommand`, bypass de execution policy, descarga de scripts remotos con `IEX(New-Object Net.WebClient)`.
- T1059.003 (Windows Command Shell): `cmd.exe` lanzado como hijo de procesos inusuales (Word, Excel, Outlook).
- T1059.005 (Visual Basic): macros que invocan `Shell()` o `WScript.Shell`.

**T1021: Remote Services.** El movimiento lateral a traves de servicios remotos legitimos es la segunda fase critica de cualquier intrusion. Sub-tecnicas prioritarias:

- T1021.001 (Remote Desktop Protocol): conexiones RDP desde estaciones de trabajo a servidores no habituales.
- T1021.002 (SMB/Windows Admin Shares): acceso a `C$` o `ADMIN$` desde hosts no administrativos.
- T1021.006 (Windows Remote Management): uso de WinRM/WMI para ejecucion remota.

**T1110: Brute Force.** Los ataques de fuerza bruta contra servicios expuestos (RDP, VPN, OWA, SSH) siguen siendo efectivos porque muchas organizaciones no implementan bloqueo de cuentas o MFA. Detecciones:

- Mas de N intentos fallidos en ventana de M minutos desde una misma IP.
- Patron de password spraying: un intento por cuenta con la misma contrasena.
- Incremento anomalo de eventos 4625 (Windows) o auth failures en VPN.

## Como escribir reglas de deteccion por tecnica con Sigma

[Sigma](https://github.com/SigmaHQ/sigma) es el formato estandar para escribir reglas de deteccion independientes del SIEM. Escribes la logica una vez en YAML y luego la conviertes a la query nativa de tu plataforma (Splunk SPL, Elastic KQL, Sentinel KQL, QRadar AQL).

### Anatomia de una regla Sigma

```yaml
title: Suspicious PowerShell Download Cradle
id: 3b6ab547-1234-5678-9abc-def012345678
status: experimental
description: >
  Detecta el uso de PowerShell para descargar y ejecutar
  scripts remotos, patron comun en Initial Access y Execution.
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
  - Administradores usando scripts de despliegue legitimos
level: high
```

Los campos clave para el mapping ATT&CK son los **tags**. El prefijo `attack.` seguido de la tactica (execution) y la tecnica (t1059.001) vincula la regla directamente con la matriz.

### Ejemplo: regla para T1078 (Valid Accounts, impossible travel)

```yaml
title: Login desde geolocalizacion imposible
id: a1b2c3d4-5678-90ab-cdef-123456789abc
status: experimental
description: >
  Detecta logins exitosos desde dos ubicaciones geograficas
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

Esta regla es conceptual (la logica real de impossible travel requiere calculo de distancia y velocidad), pero ilustra como vincular una deteccion operativa con una tecnica ATT&CK especifica.

### Ejemplo: regla para T1110 (Brute Force)

```yaml
title: Password Spraying contra Active Directory
id: b2c3d4e5-6789-01ab-cdef-234567890abc
status: experimental
description: >
  Detecta intentos de password spraying: misma contrasena
  probada contra multiples cuentas en ventana corta.
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
  - Escaner de vulnerabilidades interno
level: high
```

### El ecosistema Sigma en la practica

El repositorio oficial de Sigma contiene mas de 3.000 reglas mantenidas por la comunidad, ya mapeadas a tecnicas ATT&CK. Antes de escribir una regla desde cero, busca si ya existe una en el repositorio que puedas adaptar. La herramienta `sigma-cli` convierte las reglas al formato de tu SIEM:

```bash
# Convertir regla Sigma a Splunk SPL
sigma convert -t splunk -p sysmon regla.yml

# Convertir a Elastic/Lucene
sigma convert -t elasticsearch -p ecs-windows regla.yml

# Convertir a Microsoft Sentinel KQL
sigma convert -t microsoft365defender regla.yml
```

## La metodologia DeTT&CT: estructura profesional para el mapping

DeTT&CT (Detect Tactics, Techniques & Combat Threats) es una metodologia creada por Marcus Bakker y Ruben Bouman que formaliza todo el proceso de mapping de detecciones a ATT&CK. Se compone de dos pilares:

### Pilar 1: Data Source Assessment

Antes de hablar de detecciones, DeTT&CT te obliga a responder: **que datos tienes realmente disponibles?** Porque no puedes detectar ejecucion de PowerShell si no recoges los Event IDs adecuados (4103, 4104 para Script Block Logging).

El data source assessment asigna a cada fuente de datos una puntuacion de calidad:

| Score | Calidad de datos |
|---|---|
| 0 | No recogidos |
| 1 | Recogidos pero sin parsear o normalizar |
| 2 | Parseados y normalizados |
| 3 | Parseados, normalizados y con campos enriquecidos |
| 4 | Alta calidad: cobertura completa, parseado robusto, enriquecimiento |
| 5 | Excelente: monitorizacion completa con validacion periodica de integridad |

Ejemplo: si recoges Windows Security Event Logs pero solo tienes habilitados los Event IDs por defecto (sin auditing avanzado, sin Sysmon), tu score de data source para "Process Creation" sera un 1 o 2, no un 4.

### Pilar 2: Detection Assessment

Una vez sabes que datos tienes, evaluas la calidad de las detecciones que has construido sobre esos datos. DeTT&CT usa la misma escala del 0 al 5 descrita anteriormente, pero anade dos dimensiones:

- **Detection score.** Calidad tecnica de la regla (de string matching basico a deteccion comportamental).
- **Detection applicability.** Cobertura dentro de la tecnica. Una tecnica como T1059 tiene 8 sub-tecnicas. Si solo detectas T1059.001 (PowerShell), tu applicability es parcial.

### Workflow DeTT&CT completo

1. **Crear el fichero YAML de data sources.** Lista todas tus fuentes de telemetria con su score de calidad.
2. **Crear el fichero YAML de detecciones.** Lista todas tus reglas con su score de calidad y las tecnicas mapeadas.
3. **Ejecutar las herramientas DeTT&CT.** El framework genera automaticamente las capas de ATT&CK Navigator combinando ambos ficheros.
4. **Generar el gap analysis.** La superposicion de la capa de data sources y la capa de detecciones revela donde tienes datos pero no detecciones (oportunidad rapida) y donde no tienes ni datos (requiere despliegue de nueva telemetria).

El resultado son tres capas de Navigator:

- **Capa de visibilidad (data sources).** Que tecnicas podrias detectar con los datos que ya tienes.
- **Capa de deteccion.** Que tecnicas detectas realmente con tus reglas actuales.
- **Capa de gap.** La diferencia entre ambas. Esta es la capa mas valiosa: muestra el "low hanging fruit" (tecnicas donde tienes datos pero no has escrito detecciones).

## Como crear un dashboard de cobertura ATT&CK

Un heatmap estatico en Navigator es util para reuniones trimestrales, pero el SOC necesita visibilidad en tiempo real. La solucion es construir un dashboard operativo que se actualice automaticamente.

### Arquitectura del dashboard

El dashboard necesita tres componentes:

1. **Base de datos de mapping.** Una tabla que vincula cada regla del SIEM con sus tecnicas ATT&CK. Puede ser una tabla en PostgreSQL, un Google Sheet o un fichero YAML en Git. Lo importante es que sea la fuente unica de verdad.
2. **Script de sincronizacion.** Un proceso automatico que lee las reglas activas del SIEM via API, cruza con la base de datos de mapping y calcula los scores actuales.
3. **Visualizacion.** Grafana, Kibana o cualquier herramienta de dashboarding que consuma los datos calculados.

### Metricas esenciales del dashboard

El dashboard debe responder a estas preguntas con un vistazo:

- **Cobertura por tactica.** Porcentaje de tecnicas cubiertas en cada tactica (Initial Access, Execution, Persistence, etc.). Grafico de barras horizontal.
- **Cobertura por actor.** Si tu threat profile incluye APT28 y Lockbit, muestra el porcentaje de sus tecnicas favoritas que cubres. Grafico radar.
- **Evolucion temporal.** Como ha cambiado la cobertura en los ultimos 6-12 meses. Linea temporal por tactica.
- **Top gaps.** Las 10 tecnicas con score 0 que mas actores relevantes usan. Tabla priorizada.
- **Reglas por calidad.** Distribucion de reglas por score de deteccion (1-5). Donut chart.

### Ejemplo practico con Elastic y Grafana

Si usas Elastic Security, muchas de sus reglas pre-built ya incluyen tags ATT&CK. Puedes extraerlas via API:

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

Con esa informacion, un script Python puede generar un JSON compatible con Navigator y actualizar Grafana via la API de datasources.

## Como identificar y cerrar gaps de deteccion

Identificar gaps es la mitad del trabajo. Cerrarlos requiere un proceso estructurado que no sobrecargue al equipo.

### El framework de priorizacion de gaps

No todos los gaps son iguales. Un gap en T1486 (Data Encrypted for Impact, ransomware) es critico. Un gap en T1612 (Build Image on Host, containers) puede ser irrelevante si no usas contenedores en produccion. El framework de priorizacion debe considerar:

1. **Prevalencia en actores relevantes.** Cuantos de tus threat actors priorizados usan esta tecnica? Si la usan 3 de 4, prioridad alta.
2. **Impacto potencial.** Que pasa si esta tecnica se ejecuta sin detectar? Un T1486 sin detectar significa ransomware desplegado. Un T1087 (Account Discovery) sin detectar es grave pero no catastrofico por si solo.
3. **Disponibilidad de datos.** Tienes la telemetria necesaria? Si necesitas Sysmon y no lo tienes desplegado, el gap es mas costoso de cerrar.
4. **Existencia de reglas publicas.** Hay reglas Sigma o detecciones de tu vendor que puedas adaptar? Si si, el coste de cierre es bajo.

### Proceso de cierre de un gap

Para cada gap priorizado:

1. **Verificar data sources.** Confirmar que la telemetria llega al SIEM, esta parseada y es de calidad suficiente.
2. **Buscar reglas existentes.** Revisar el repositorio Sigma, las detecciones del vendor de tu SIEM y los repositorios de la comunidad (Elastic Detection Rules, Splunk Security Content).
3. **Adaptar o escribir la regla.** Si existe una regla publica, adaptarla a tu entorno (ajustar exclusiones, umbrales, campos). Si no existe, escribirla desde cero.
4. **Testear con emulacion.** Ejecutar la tecnica en un entorno de laboratorio (Atomic Red Team, Caldera) y verificar que la regla genera la alerta esperada.
5. **Desplegar en modo monitor.** Activar la regla sin generar tickets durante 1-2 semanas para calibrar falsos positivos.
6. **Activar en produccion.** Mover la regla a produccion y actualizar el mapping en la base de datos.

### Herramientas de emulacion para validar detecciones

La emulacion de adversarios es el complemento indispensable del detection engineering. Las herramientas principales:

- **Atomic Red Team.** Coleccion de tests atomicos mapeados a tecnicas ATT&CK. Ejecutas un test y verificas si tu SIEM genera la alerta. Ideal para validacion rapida.
- **MITRE Caldera.** Plataforma de emulacion automatizada. Permite encadenar multiples tecnicas en una operacion completa (kill chain) y evaluar la deteccion end-to-end.
- **Red Canary.** Proporciona tests validados con buena documentacion de los artefactos que deberia generar cada tecnica.

## Que fuentes de telemetria necesitas por tactica

La telemetria es el combustible del detection engineering. Sin los datos adecuados, las mejores reglas no pueden funcionar. Esta tabla resume las fuentes criticas por tactica:

| Tactica | Fuentes de datos criticas |
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
| Exfiltration | DLP alerts, volumen anomalo de upload, conexiones a servicios cloud no corporativos |
| Impact | Volume Shadow Copy deletion, mass file encryption, service stops |

### La importancia de Sysmon

Si solo pudieras desplegar una herramienta adicional de telemetria, deberia ser Sysmon. Con una configuracion adecuada (la config de SwiftOnSecurity o la de Olaf Hartong son buenos puntos de partida), Sysmon proporciona:

- Creacion de procesos con linea de comandos completa y hash.
- Conexiones de red por proceso.
- Modificaciones de registro.
- Carga de DLLs.
- Acceso a procesos (critico para detectar credential dumping).
- Creacion de ficheros con hash.

Estos eventos cubren directamente mas de 80 tecnicas ATT&CK. Sin Sysmon (o un EDR equivalente), la mayoria de tecnicas de Execution, Defense Evasion y Credential Access son invisibles.

## Como automatizar el mapping de detecciones

El mapping manual es necesario al principio, pero no escala. Un SOC maduro automatiza la mayor parte del proceso.

### Automatizacion con CI/CD para reglas de deteccion

El concepto de "Detection as Code" aplica las practicas de ingenieria de software al detection engineering:

1. **Repositorio Git de reglas.** Todas las reglas Sigma viven en un repositorio con estructura de directorios por tactica ATT&CK.
2. **Validacion automatica en CI.** Cada pull request ejecuta tests: sintaxis YAML valida, tecnica ATT&CK existente, campos obligatorios presentes (tags, falsepositives, level).
3. **Conversion automatica.** El pipeline convierte las reglas Sigma al formato del SIEM de destino y las despliega via API.
4. **Actualizacion del mapping.** Al mergear una regla nueva, el pipeline actualiza automaticamente la base de datos de mapping y regenera la capa de Navigator.

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

### Integracion con threat intelligence

Cuando tu equipo de CTI publica un informe sobre un nuevo actor de amenaza, el flujo ideal es:

1. El analista CTI extrae las tecnicas ATT&CK del informe.
2. Un script cruza esas tecnicas con tu matriz de cobertura actual.
3. Se genera automaticamente un informe de gap analysis especifico para ese actor.
4. El equipo de detection engineering recibe un listado priorizado de reglas a escribir.

Este ciclo cierra el loop entre inteligencia y operaciones, que es donde la mayoria de los SOC fallan.

{{< cta type="tofu" text="Riskitera automatiza el triage, la correlacion y el reporting de tu SOC con IA soberana. Conecta tu MITRE ATT&CK mapping con detecciones operativas en minutos." label="Ver demo SOC" >}}

## Que metricas de cobertura ATT&CK debes medir

Las metricas transforman el mapping de un ejercicio academico en una herramienta de gestion. Estas son las metricas que recomendamos medir mensualmente:

### Metricas de cobertura

- **Cobertura global.** Porcentaje de tecnicas de la matriz con al menos una deteccion (score >= 1). Meta razonable: 40-60% para un SOC maduro.
- **Cobertura por tactica.** Desglose por las 14 tacticas. Las tacticas de Initial Access, Execution y Lateral Movement deberian tener mayor cobertura.
- **Cobertura ponderada por amenaza.** Porcentaje de las tecnicas de tus top 5 actores que cubres. Esta es la metrica mas relevante para el negocio.
- **Profundidad de cobertura.** Distribucion de scores (cuantas tecnicas en score 1, cuantas en 2, etc.). Mas util que el simple binario cubierto/no cubierto.

### Metricas de operacion

- **Mean Time to Detect (MTTD) por tecnica.** Cuanto tarda tu SOC en detectar cada tecnica cuando se emula. Medido con ejercicios de purple team.
- **Tasa de falsos positivos por regla.** Reglas con mas del 80% de falsos positivos son candidatas a reescritura o desactivacion.
- **Reglas desactivadas.** Porcentaje de reglas mapeadas que estan deshabilitadas. Si es alto (>20%), tienes un problema de calidad.
- **Tiempo medio de cierre de gap.** Desde que se identifica un gap hasta que la regla esta en produccion. Meta: menos de 2 semanas para gaps con datos disponibles.

### Metricas de madurez

- **Porcentaje de reglas en formato estandar (Sigma).** Mide la portabilidad de tus detecciones.
- **Porcentaje de reglas con test de emulacion.** Mide la validacion de tus detecciones.
- **Frecuencia de actualizacion del mapping.** Si se actualiza solo una vez al ano, no es util operativamente.

## Errores comunes al mapear detecciones a ATT&CK

Despues de trabajar con multiples SOC, estos son los errores que vemos con mas frecuencia:

1. **Mapear por obligacion, no por utilidad.** Si el mapping es un checkbox de compliance que nadie consulta, no aporta valor. El mapping debe alimentar decisiones operativas semanales.
2. **Inflar los scores de deteccion.** Poner score 4 a una regla que busca un hash especifico de mimikatz es autoengano. Se honesto con la calidad.
3. **Ignorar la calidad de los datos.** Una regla perfecta sobre datos incompletos o mal parseados genera mas problemas que soluciones.
4. **No incluir al equipo de threat intelligence.** El mapping sin contexto de amenaza es un ejercicio academico. El equipo de CTI aporta la priorizacion basada en actores reales.
5. **Tratar el mapping como un proyecto con fin.** Es un proceso continuo. Si se abandona despues de la foto inicial, pierde todo su valor en 6 meses.

{{< cta type="bofu" text="Solicita una demo personalizada para tu SOC y descubre como Riskitera conecta ATT&CK mapping con detecciones operativas, priorizacion por amenaza y metricas en tiempo real." label="Solicitar demo" >}}


**Articulos relacionados:**
- [Mitre Attack Que Es Como Usarlo](/es/posts/2026/04/mitre-attack-que-es-como-usarlo/)
- [Como Montar Soc Desde Cero](/es/posts/2026/04/como-montar-soc-desde-cero/)

## Preguntas frecuentes

### Cuanto tiempo se tarda en hacer el primer mapping completo de detecciones a ATT&CK?

Depende del tamano del SOC. Para un equipo con 200-500 reglas activas, el inventario y mapping inicial requiere entre 2 y 4 semanas dedicando unas 4 horas diarias. La mayor parte del tiempo se invierte en las primeras 100 reglas, porque el equipo todavia esta aprendiendo las tecnicas. Despues el ritmo se acelera. Lo importante es no intentar hacerlo perfecto a la primera: un mapping al 80% de precision que se completa en 3 semanas es mas util que uno perfecto que tarda 3 meses.

### Necesito un SIEM comercial para implementar detection engineering basada en ATT&CK?

No es imprescindible. Puedes implementar el mapping con herramientas open source. Elastic Security (con licencia basica gratuita) soporta reglas con tags ATT&CK. Wazuh incluye decoders y reglas mapeadas. Sigma te permite escribir reglas portables. Lo que si necesitas es telemetria de calidad: sin Sysmon o un EDR que recoja eventos de proceso, red y registro, el mapping sera superficial independientemente del SIEM.

### Como convenzo a direccion de que el mapping ATT&CK merece recursos dedicados?

El argumento mas efectivo es visual. Genera un heatmap de Navigator con la cobertura actual (la mayoria sera roja) y superpone las tecnicas usadas por los actores que han atacado a empresas de tu sector en Espana (datos de CCN-CERT e INCIBE). La interseccion entre "tecnicas que nos atacan" y "tecnicas que no detectamos" es el argumento de negocio. Complementa con un calculo de coste: si un incidente de ransomware cuesta de media 1.5M EUR (dato de INCIBE para PYMES), invertir 50-100 horas de equipo en cerrar los gaps criticos es trivial en comparacion.

### Con que frecuencia debo actualizar el mapping de detecciones?

El mapping debe actualizarse en tres momentos: (1) cuando se anade o modifica una regla de deteccion, como parte del proceso estandar; (2) cuando MITRE publica una nueva version de la matriz (normalmente abril y octubre), para verificar cambios en IDs de tecnicas; y (3) trimestralmente, con una revision completa de scores de deteccion que incluya tests de emulacion con Atomic Red Team o Caldera.

### Cual es la diferencia entre ATT&CK Navigator y DeTT&CT?

ATT&CK Navigator es una herramienta de visualizacion: crea capas de colores sobre la matriz ATT&CK. DeTT&CT es una metodologia y conjunto de herramientas que va mas alla: estructura la evaluacion de data sources (que telemetria tienes y con que calidad) y detecciones (que reglas tienes y como de robustas son), generando automaticamente las capas de Navigator. En resumen, Navigator es el lienzo; DeTT&CT es el proceso completo para pintarlo con datos reales.
