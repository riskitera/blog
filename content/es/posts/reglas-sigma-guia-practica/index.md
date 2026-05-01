---
title: "Reglas Sigma: guia practica para escribir detecciones portables"
description: "Guia completa de reglas Sigma para SOC y SIEM: sintaxis, ejemplos practicos, conversion a SIEM, integracion con MITRE ATT&CK y mejores practicas para escribir detecciones portables."
slug: "reglas-sigma-guia-practica"
date: 2026-06-04
publishDate: 2026-06-04
lastmod: 2026-06-04
draft: false
tags: ["SOC", "SIEM", "Detection Engineering"]
categories: ["SOC"]
author: "David Moya"
keyword: "reglas sigma"
funnel: "mofu"
---

Guia completa de reglas Sigma para SOC y SIEM: sintaxis, ejemplos practicos, conversion a SIEM, integracion con MITRE ATT&CK y mejores practicas para escribir detecciones portables.

<!--more-->

{{< key-takeaways >}}
- Sigma es el formato estandar abierto para escribir reglas de deteccion portables entre cualquier SIEM (Splunk, Elastic, Sentinel, Wazuh, etc.).
- La sintaxis YAML de Sigma permite definir detecciones con condiciones booleanas, modificadores de campo y correlacion temporal.
- El repositorio SigmaHQ contiene mas de 3.000 reglas mantenidas por la comunidad, listas para convertir y desplegar.
- sigma-cli permite convertir reglas a SPL, KQL, Lucene y otros lenguajes de consulta de SIEM con un solo comando.
- Escribir reglas Sigma propias es la forma mas eficiente de construir un programa de detection engineering portable y mantenible.
{{< /key-takeaways >}}

## Que son las reglas Sigma

[Sigma](https://github.com/SigmaHQ/sigma) es un formato generico y abierto para escribir reglas de deteccion de seguridad. Su proposito es resolver un problema fundamental: cada SIEM tiene su propio lenguaje de consulta (SPL en Splunk, KQL en Elastic/Sentinel, SQL en Graylog) y escribir detecciones directamente en el lenguaje del SIEM te ata a ese producto.

Sigma funciona como un intermediario. Escribes la regla una vez en formato YAML y luego la conviertes al lenguaje de consulta de tu SIEM. Si cambias de SIEM, no reescribes las reglas: solo cambias el backend de conversion.

El proyecto fue creado en 2017 por Florian Roth y Thomas Patzke, inspirado en lo que Snort/YARA hacen para deteccion en red y ficheros respectivamente. Si YARA es para ficheros y Snort es para paquetes de red, Sigma es para logs.

### La analogia YARA/Snort/Sigma

| Dominio | Formato estandar | Que analiza |
|---------|-------------------|-------------|
| Ficheros | YARA | Patrones en binarios y documentos |
| Trafico de red | Snort/Suricata | Paquetes de red |
| Logs | Sigma | Eventos de logs de cualquier fuente |

### Por que adoptar Sigma

1. **Portabilidad**: una regla Sigma funciona en cualquier SIEM con un backend compatible.
2. **Compartibilidad**: la comunidad comparte reglas en un formato comun. [SigmaHQ](https://github.com/SigmaHQ/sigma) tiene mas de 3.000 reglas.
3. **Versionado**: al ser YAML plano, las reglas se gestionan en Git con diff, review y CI/CD.
4. **Estandarizacion**: todos los analistas del equipo escriben detecciones en el mismo formato.
5. **Independencia de vendor**: no estas atado al SIEM que uses hoy.

## Anatomia de una regla Sigma

Cada regla Sigma es un fichero YAML con una estructura definida. Vamos a desglosar cada campo.

### Estructura basica

```yaml
title: Deteccion de Brute Force por RDP
id: a]1b2c3d4-e5f6-7890-abcd-ef1234567890
status: test
description: >
  Detecta multiples intentos fallidos de autenticacion RDP
  desde una misma IP en un periodo corto de tiempo.
references:
  - https://attack.mitre.org/techniques/T1110/001/
author: SOC Team - Riskitera
date: 2026/05/01
modified: 2026/05/15
tags:
  - attack.credential_access
  - attack.t1110.001
logsource:
  category: authentication
  product: windows
detection:
  selection:
    EventID: 4625
    LogonType: 10  # RemoteInteractive (RDP)
  timeframe: 5m
  condition: selection | count(TargetUserName) by SourceNetworkAddress > 10
falsepositives:
  - Usuarios con problemas de credenciales
  - Escaneos de vulnerabilidades autorizados
level: high
```

### Campos de metadatos

| Campo | Obligatorio | Descripcion |
|-------|-------------|-------------|
| `title` | Si | Nombre descriptivo de la regla |
| `id` | Si | UUID unico (usar `uuidgen` para generarlo) |
| `status` | Si | `experimental`, `test`, `stable`, `deprecated`, `unsupported` |
| `description` | Si | Explicacion detallada del comportamiento detectado |
| `references` | No | URLs a documentacion, blog posts, tecnicas ATT&CK |
| `author` | Si | Quien escribio la regla |
| `date` | Si | Fecha de creacion (formato YYYY/MM/DD) |
| `modified` | No | Fecha de ultima modificacion |
| `tags` | Si | Etiquetas ATT&CK y otras clasificaciones |
| `level` | Si | `informational`, `low`, `medium`, `high`, `critical` |
| `falsepositives` | Si | Escenarios conocidos de falsos positivos |

### El bloque logsource

El `logsource` define de donde vienen los logs que analiza la regla. Es lo que hace a Sigma portable: en lugar de referenciar un indice especifico de Elastic o un sourcetype de Splunk, defines la fuente de forma abstracta.

```yaml
# Logs de procesos en Windows
logsource:
  category: process_creation
  product: windows

# Logs de firewall (cualquier vendor)
logsource:
  category: firewall

# Logs de proxy web
logsource:
  category: proxy

# Sysmon especifico
logsource:
  product: windows
  service: sysmon
  category: process_creation

# Logs de Active Directory
logsource:
  product: windows
  service: security

# Logs de Linux auditd
logsource:
  product: linux
  service: auditd
```

Las categorias mas comunes:

| Categoria | Descripcion | Fuentes tipicas |
|-----------|-------------|-----------------|
| `process_creation` | Creacion de procesos | Sysmon 1, Windows 4688, EDR |
| `authentication` | Eventos de autenticacion | Windows 4624/4625, Linux auth.log |
| `firewall` | Logs de firewall | pfSense, iptables, Palo Alto |
| `proxy` | Logs de proxy web | Squid, Zscaler, BlueCoat |
| `dns_query` | Consultas DNS | Sysmon 22, Pi-hole, Zeek |
| `network_connection` | Conexiones de red | Sysmon 3, Zeek, Suricata |
| `file_event` | Operaciones con ficheros | Sysmon 11, EDR |
| `registry_event` | Cambios en registro Windows | Sysmon 12/13/14 |
| `driver_load` | Carga de drivers | Sysmon 6 |
| `image_load` | Carga de DLLs | Sysmon 7 |

### El bloque detection

El bloque `detection` es el corazon de la regla. Define las condiciones que deben cumplirse para que la regla dispare.

#### Selecciones simples

```yaml
detection:
  selection:
    EventID: 4625
    LogonType: 10
  condition: selection
```

Esto equivale a: `EventID = 4625 AND LogonType = 10`.

#### Multiples valores (OR implicito)

```yaml
detection:
  selection:
    EventID:
      - 4624
      - 4625
      - 4648
  condition: selection
```

Equivale a: `EventID IN (4624, 4625, 4648)`.

#### Multiples selecciones con operadores booleanos

```yaml
detection:
  selection_process:
    ParentImage|endswith: '\cmd.exe'
  selection_command:
    CommandLine|contains:
      - 'whoami'
      - 'net user'
      - 'net group'
  filter_legitimate:
    User|endswith: '$'  # Cuentas de maquina
  condition: selection_process and selection_command and not filter_legitimate
```

#### Modificadores de campo

Los modificadores de campo son una de las funcionalidades mas potentes de Sigma. Se aplican al nombre del campo con el operador `|`.

| Modificador | Descripcion | Ejemplo |
|-------------|-------------|---------|
| `contains` | El campo contiene el valor | `CommandLine\|contains: 'mimikatz'` |
| `startswith` | El campo empieza por | `Image\|startswith: 'C:\Temp'` |
| `endswith` | El campo termina por | `Image\|endswith: '\powershell.exe'` |
| `re` | Expresion regular | `CommandLine\|re: '.*-enc.*[A-Za-z0-9+/=]{50,}'` |
| `cidr` | Rango de red CIDR | `SourceIP\|cidr: '10.0.0.0/8'` |
| `all` | Todos los valores deben coincidir (AND) | `CommandLine\|contains\|all: ['net', 'user', '/add']` |
| `base64` | Busca valor codificado en base64 | `CommandLine\|base64: 'IEX'` |
| `base64offset` | Busca con offset de base64 | `CommandLine\|base64offset: 'IEX'` |
| `windash` | Coincide con `-` y `/` en argumentos Windows | `CommandLine\|windash\|contains: '-enc'` |

#### Condiciones de agregacion

Sigma soporta funciones de agregacion para detecciones basadas en umbrales:

```yaml
detection:
  selection:
    EventID: 4625
  timeframe: 10m
  condition: selection | count() by SourceIP > 20
```

Funciones disponibles: `count()`, `min()`, `max()`, `avg()`, `sum()`, `near`.

## Ejemplos completos de reglas Sigma

### Ejemplo 1: Deteccion de brute force SSH

```yaml
title: SSH Brute Force Attempt
id: 5c2a8e1d-9f3b-4a7c-b6d2-e8f1234abcde
status: stable
description: >
  Detecta multiples intentos fallidos de autenticacion SSH
  desde una misma IP de origen, indicativo de un ataque
  de fuerza bruta contra el servicio SSH.
references:
  - https://attack.mitre.org/techniques/T1110/001/
  - https://www.sshaudit.com/
author: SOC Team
date: 2026/04/10
modified: 2026/05/20
tags:
  - attack.credential_access
  - attack.t1110.001
  - attack.t1110.003
logsource:
  product: linux
  service: sshd
detection:
  selection:
    sshd_result: 'Failed'
  timeframe: 5m
  condition: selection | count() by src_ip > 15
falsepositives:
  - Usuarios legitimos que olvidan la contrasena
  - Conexiones automatizadas con credenciales caducadas
  - Herramientas de escaneo de compliance
level: medium
```

### Ejemplo 2: Movimiento lateral via WMI

```yaml
title: Remote WMI Command Execution
id: 7a9b3c4d-2e1f-5678-90ab-cdef12345678
status: stable
description: >
  Detecta la ejecucion remota de comandos a traves de WMI
  (Windows Management Instrumentation), tecnica comun de
  movimiento lateral usada por atacantes y herramientas
  como Impacket wmiexec.
references:
  - https://attack.mitre.org/techniques/T1047/
  - https://github.com/fortra/impacket
author: SOC Team
date: 2026/04/15
modified: 2026/05/25
tags:
  - attack.lateral_movement
  - attack.execution
  - attack.t1047
logsource:
  category: process_creation
  product: windows
detection:
  selection_parent:
    ParentImage|endswith: '\WmiPrvSE.exe'
  selection_suspicious_child:
    Image|endswith:
      - '\cmd.exe'
      - '\powershell.exe'
      - '\pwsh.exe'
      - '\mshta.exe'
      - '\wscript.exe'
      - '\cscript.exe'
      - '\rundll32.exe'
      - '\regsvr32.exe'
  filter_legitimate:
    CommandLine|contains:
      - 'Windows\CCM'       # SCCM
      - 'Windows\ccmsetup'  # SCCM setup
  condition: selection_parent and selection_suspicious_child and not filter_legitimate
falsepositives:
  - Administradores IT usando WMI para gestion remota
  - SCCM y otras herramientas de gestion de endpoints
  - Scripts de inventario y monitoreo
level: high
```

### Ejemplo 3: Persistencia via tarea programada

```yaml
title: Scheduled Task Creation for Persistence
id: 3b5c7d9e-1a2f-4e6g-8h0i-jklm12345678
status: stable
description: >
  Detecta la creacion de tareas programadas que apuntan
  a ejecutables en ubicaciones sospechosas, tecnica
  frecuente de persistencia usada por malware y atacantes.
references:
  - https://attack.mitre.org/techniques/T1053/005/
author: SOC Team
date: 2026/05/01
modified: 2026/05/28
tags:
  - attack.persistence
  - attack.execution
  - attack.t1053.005
logsource:
  product: windows
  service: security
detection:
  selection_event:
    EventID: 4698  # A scheduled task was created
  selection_suspicious_path:
    TaskContent|contains:
      - '\AppData\Local\Temp\'
      - '\AppData\Roaming\'
      - '\Users\Public\'
      - '\ProgramData\'
      - '\Windows\Temp\'
      - 'C:\Temp\'
  filter_known_tools:
    TaskContent|contains:
      - 'GoogleUpdate'
      - 'MicrosoftEdgeUpdate'
      - 'OneDrive'
  condition: selection_event and selection_suspicious_path and not filter_known_tools
falsepositives:
  - Software legitimo que instala tareas programadas en rutas de usuario
  - Herramientas de IT que usan tareas programadas para mantenimiento
level: high
```

### Ejemplo 4: Exfiltracion via DNS tunneling

```yaml
title: Possible DNS Tunneling via Long Subdomain Queries
id: 9e8d7c6b-5a4f-3210-fedc-ba9876543210
status: test
description: >
  Detecta consultas DNS con subdominios anormalmente largos,
  indicativo de DNS tunneling donde se codifican datos en
  las consultas DNS para exfiltrarlos sin pasar por controles
  de proxy o firewall.
references:
  - https://attack.mitre.org/techniques/T1048/
  - https://attack.mitre.org/techniques/T1071/004/
  - https://www.sans.org/white-papers/dns-tunneling/
author: SOC Team
date: 2026/05/10
tags:
  - attack.exfiltration
  - attack.t1048
  - attack.command_and_control
  - attack.t1071.004
logsource:
  category: dns_query
detection:
  selection:
    query|re: '^[a-zA-Z0-9]{30,}\.[a-zA-Z0-9]{10,}\.'
  filter_cdn:
    query|endswith:
      - '.amazonaws.com'
      - '.cloudfront.net'
      - '.akamaiedge.net'
      - '.googleusercontent.com'
  filter_internal:
    query|endswith:
      - '.internal.corp'
      - '.ad.company.local'
  condition: selection and not filter_cdn and not filter_internal
falsepositives:
  - Servicios cloud con subdominios largos generados automaticamente
  - Certificados de seguridad con hashes en subdominios
  - Servicios de CDN con identificadores largos
level: medium
```

## Convertir reglas Sigma a tu SIEM con sigma-cli

[sigma-cli](https://github.com/SigmaHQ/sigma-cli) es la herramienta oficial de linea de comandos para convertir reglas Sigma al lenguaje de consulta de tu SIEM. Reemplazo al antiguo `sigmac` a partir de Sigma v2.

### Instalacion

```bash
# Instalar sigma-cli via pip
pip install sigma-cli

# Instalar backends (plugins) para tu SIEM
pip install pySigma-backend-splunk
pip install pySigma-backend-elasticsearch
pip install pySigma-backend-microsoft365defender
pip install pySigma-backend-kusto     # Microsoft Sentinel

# Instalar pipelines de procesamiento
pip install pySigma-pipeline-sysmon
pip install pySigma-pipeline-windows

# Verificar instalacion
sigma version
sigma list backends
sigma list pipelines
```

### Conversion basica

```bash
# Convertir una regla a Splunk SPL
sigma convert -t splunk -p sysmon rules/brute_force_ssh.yml

# Convertir a Elastic/Lucene
sigma convert -t elasticsearch -p ecs_windows rules/wmi_lateral.yml

# Convertir a Microsoft Sentinel KQL
sigma convert -t kusto -p microsoft365defender rules/scheduled_task.yml

# Convertir un directorio completo
sigma convert -t splunk -p sysmon rules/ -o output/splunk/

# Convertir con formato de output especifico
sigma convert -t splunk -p sysmon --format savedsearches rules/
```

### Ejemplo de conversion: regla de brute force a SPL

Regla Sigma de entrada:

```yaml
title: Windows Logon Brute Force
logsource:
  product: windows
  service: security
detection:
  selection:
    EventID: 4625
  timeframe: 5m
  condition: selection | count() by SourceNetworkAddress > 10
level: high
```

Salida SPL (Splunk):

```spl
source="WinEventLog:Security" EventCode=4625
| bucket span=5m _time
| stats count by SourceNetworkAddress, _time
| where count > 10
```

### Ejemplo de conversion: regla de WMI a KQL (Elastic)

Salida KQL (Elastic):

```
process.parent.executable:*\\WmiPrvSE.exe AND
process.executable:(*\\cmd.exe OR *\\powershell.exe OR *\\pwsh.exe
  OR *\\mshta.exe OR *\\wscript.exe OR *\\cscript.exe
  OR *\\rundll32.exe OR *\\regsvr32.exe) AND
NOT process.command_line:(*Windows\\CCM* OR *Windows\\ccmsetup*)
```

### Ejemplo de conversion: regla a KQL (Microsoft Sentinel)

```kql
SecurityEvent
| where EventID == 4698
| where TaskContent has_any (
    "\\AppData\\Local\\Temp\\",
    "\\AppData\\Roaming\\",
    "\\Users\\Public\\",
    "\\ProgramData\\",
    "\\Windows\\Temp\\",
    "C:\\Temp\\"
)
| where TaskContent !has "GoogleUpdate"
    and TaskContent !has "MicrosoftEdgeUpdate"
    and TaskContent !has "OneDrive"
```

### Pipelines de procesamiento

Los pipelines de procesamiento transforman los nombres de campo genericos de Sigma a los nombres especificos de tu SIEM. Sin un pipeline adecuado, la conversion puede generar nombres de campo que tu SIEM no reconoce.

```bash
# Ver pipelines disponibles
sigma list pipelines

# Pipelines comunes:
# - sysmon: mapea campos de Sysmon
# - ecs_windows: mapea a Elastic Common Schema
# - splunk_windows: mapea a campos de Splunk para Windows
# - microsoft365defender: mapea a campos de M365 Defender

# Usar multiples pipelines
sigma convert -t elasticsearch -p ecs_windows -p sysmon rules/
```

### Crear un pipeline custom

Si tu SIEM usa nombres de campo personalizados, puedes crear un pipeline de procesamiento propio:

```yaml
# custom_pipeline.yml
name: Custom Field Mapping
priority: 50
transformations:
  - id: custom_field_mapping
    type: field_name_mapping
    mapping:
      Image: process.executable.path
      ParentImage: process.parent.executable.path
      CommandLine: process.command_line
      User: user.name
      SourceIP: source.ip
      DestinationIP: destination.ip
      DestinationPort: destination.port
```

```bash
# Usar pipeline custom
sigma convert -t elasticsearch -p custom_pipeline.yml rules/
```

{{< cta type="tofu" text="Riskitera automatiza el triage, la correlacion y el reporting de tu SOC con IA soberana. Compatible con cualquier SIEM." label="Ver demo SOC" >}}

## Integracion con MITRE ATT&CK

Una de las ventajas de Sigma es su integracion nativa con [MITRE ATT&CK](https://attack.mitre.org/). Cada regla puede (y deberia) estar etiquetada con las tacticas y tecnicas ATT&CK correspondientes.

### Convenciones de etiquetado

Las etiquetas ATT&CK en Sigma siguen un formato estandar:

```yaml
tags:
  - attack.tactica          # Nombre de la tactica en minusculas
  - attack.tXXXX            # ID de la tecnica
  - attack.tXXXX.YYY        # ID de la sub-tecnica
```

Ejemplos:

```yaml
tags:
  - attack.credential_access
  - attack.t1110             # Brute Force
  - attack.t1110.001         # Password Guessing
  - attack.t1110.003         # Password Spraying
```

### Mapear cobertura de reglas Sigma a ATT&CK

Puedes generar una matriz de cobertura automaticamente a partir de tus reglas Sigma:

```python
# sigma_coverage.py
import yaml
import glob
from collections import defaultdict

def extract_attack_tags(rules_path):
    """Extrae tags ATT&CK de todas las reglas Sigma."""
    coverage = defaultdict(list)

    for rule_file in glob.glob(f"{rules_path}/**/*.yml", recursive=True):
        with open(rule_file) as f:
            rule = yaml.safe_load(f)

        tags = rule.get("tags", [])
        title = rule.get("title", "Unknown")
        status = rule.get("status", "unknown")

        for tag in tags:
            if tag.startswith("attack.t"):
                technique_id = tag.replace("attack.", "").upper()
                coverage[technique_id].append({
                    "title": title,
                    "status": status,
                    "file": rule_file
                })

    return coverage

def print_coverage_report(coverage):
    """Imprime un resumen de cobertura."""
    print(f"\nCobertura ATT&CK: {len(coverage)} tecnicas cubiertas\n")
    for technique, rules in sorted(coverage.items()):
        stable = sum(1 for r in rules if r["status"] == "stable")
        test = sum(1 for r in rules if r["status"] == "test")
        print(f"  {technique}: {len(rules)} regla(s) "
              f"({stable} stable, {test} test)")

if __name__ == "__main__":
    coverage = extract_attack_tags("rules/")
    print_coverage_report(coverage)
```

```bash
python sigma_coverage.py

# Output:
# Cobertura ATT&CK: 47 tecnicas cubiertas
#
#   T1047: 2 regla(s) (1 stable, 1 test)
#   T1053.005: 3 regla(s) (2 stable, 1 test)
#   T1059.001: 5 regla(s) (3 stable, 2 test)
#   T1110.001: 2 regla(s) (2 stable, 0 test)
#   ...
```

### Usar SigmaHQ para cerrar gaps de cobertura

El repositorio [SigmaHQ](https://github.com/SigmaHQ/sigma) es la mayor coleccion publica de reglas Sigma. Para cerrar gaps en tu cobertura:

1. Identifica tecnicas ATT&CK sin cobertura en tu entorno.
2. Busca reglas en SigmaHQ para esas tecnicas.
3. Evalua si las fuentes de datos necesarias estan disponibles.
4. Adapta las reglas a tu entorno (exclusiones, umbrales).
5. Despliega siguiendo tu proceso de CI/CD.

```bash
# Buscar reglas de SigmaHQ para una tecnica especifica
find sigma/rules/ -name "*.yml" -exec grep -l "t1059.001" {} \;

# O usando sigma-cli
sigma list rules --tag attack.t1059.001
```

## El repositorio SigmaHQ

[SigmaHQ](https://github.com/SigmaHQ/sigma) es el repositorio oficial y centralizado de reglas Sigma mantenido por la comunidad. Es el equivalente a lo que las reglas de Snort son para la deteccion de intrusiones en red.

### Estructura del repositorio

```
sigma/
├── rules/
│   ├── windows/
│   │   ├── builtin/           # Reglas basadas en logs nativos de Windows
│   │   │   ├── security/
│   │   │   ├── system/
│   │   │   └── application/
│   │   ├── create_remote_thread/
│   │   ├── dns_query/
│   │   ├── driver_load/
│   │   ├── file/
│   │   ├── image_load/
│   │   ├── network_connection/
│   │   ├── pipe_created/
│   │   ├── process_creation/  # La categoria con mas reglas
│   │   ├── ps_script/
│   │   └── registry/
│   ├── linux/
│   │   ├── auditd/
│   │   ├── process_creation/
│   │   └── ...
│   ├── macos/
│   ├── cloud/
│   │   ├── aws/
│   │   ├── azure/
│   │   ├── gcp/
│   │   └── m365/
│   ├── network/
│   │   ├── dns/
│   │   ├── firewall/
│   │   └── proxy/
│   └── application/
│       ├── antivirus/
│       └── ...
├── rules-emerging-threats/     # Reglas para amenazas activas
├── rules-threat-hunting/       # Reglas mas amplias para hunting
├── rules-compliance/           # Reglas orientadas a compliance
└── pipelines/                  # Pipelines de procesamiento
```

### Niveles de status en SigmaHQ

Las reglas en SigmaHQ tienen un status que indica su madurez:

| Status | Descripcion | Recomendacion |
|--------|-------------|---------------|
| `stable` | Testeada y validada en multiples entornos | Desplegar directamente |
| `test` | Funcional pero necesita mas validacion | Desplegar en staging primero |
| `experimental` | Nueva, puede generar falsos positivos | Solo para hunting o lab |
| `deprecated` | Reemplazada por otra regla | No usar |
| `unsupported` | Ya no se mantiene | No usar |

### Curar reglas de SigmaHQ para tu entorno

No todas las reglas de SigmaHQ funcionan directamente en tu entorno. El proceso de curacion incluye:

1. **Filtrar por fuentes de datos disponibles**: si no tienes Sysmon desplegado, las reglas que dependen de Sysmon no te sirven (a menos que tengas un EDR equivalente).
2. **Ajustar exclusiones**: las exclusiones de SigmaHQ son genericas. Necesitas anadir las especificas de tu entorno.
3. **Calibrar niveles de severidad**: lo que es `high` en un entorno puede ser `medium` en otro segun el contexto de negocio.
4. **Validar contra logs historicos**: ejecutar la regla contra 7-30 dias de logs para entender la tasa de falsos positivos esperada.

## Escribir reglas Sigma propias

Las reglas de SigmaHQ cubren muchos escenarios comunes, pero cada organizacion tiene necesidades especificas que requieren reglas propias.

### Proceso de desarrollo

**Paso 1: Definir la hipotesis de deteccion**

Documenta que comportamiento quieres detectar, por que es malicioso y que tecnica ATT&CK mapea.

**Paso 2: Identificar la fuente de datos**

Determina que logs contienen la evidencia del comportamiento. Verifica que esos logs estan disponibles y con la calidad necesaria.

**Paso 3: Investigar el comportamiento normal**

Antes de escribir la regla, entiende como se ve la actividad normal. Ejecuta queries exploratorias contra logs historicos.

**Paso 4: Escribir la regla**

```yaml
title: Descarga de herramienta de hacking desde GitHub
id: nuevo-uuid-generado
status: test
description: >
  Detecta el uso de curl, wget o Invoke-WebRequest para
  descargar herramientas de hacking conocidas desde GitHub
  o repositorios publicos.
references:
  - https://attack.mitre.org/techniques/T1105/
author: Tu Nombre - Tu Organizacion
date: 2026/06/01
tags:
  - attack.command_and_control
  - attack.t1105
logsource:
  category: process_creation
  product: windows
detection:
  selection_tool:
    Image|endswith:
      - '\curl.exe'
      - '\wget.exe'
      - '\powershell.exe'
      - '\pwsh.exe'
  selection_url:
    CommandLine|contains:
      - 'github.com'
      - 'raw.githubusercontent.com'
  selection_hacking_tool:
    CommandLine|contains:
      - 'mimikatz'
      - 'rubeus'
      - 'SharpHound'
      - 'Certify'
      - 'Seatbelt'
      - 'winPEAS'
      - 'LaZagne'
      - 'BloodHound'
      - 'Covenant'
      - 'Sliver'
  condition: selection_tool and selection_url and selection_hacking_tool
falsepositives:
  - Red team autorizado descargando herramientas
  - Investigadores de seguridad analizando malware
level: high
```

**Paso 5: Validar la regla**

```bash
# Verificar que la sintaxis es correcta
sigma check rules/custom/download_hacking_tool.yml

# Convertir a tu SIEM para verificar la query generada
sigma convert -t splunk -p sysmon rules/custom/download_hacking_tool.yml

# Ejecutar contra logs historicos (ejemplo Splunk)
# source="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=1
# (Image="*\\curl.exe" OR Image="*\\wget.exe" OR ...)
# AND (CommandLine="*github.com*" OR CommandLine="*raw.githubusercontent.com*")
# AND (CommandLine="*mimikatz*" OR CommandLine="*rubeus*" OR ...)
```

**Paso 6: Desplegar y monitorizar**

Despliega en staging con status `test`. Monitoriza durante 1-2 semanas. Ajusta exclusiones segun los falsos positivos observados. Cuando la tasa de falsos positivos sea aceptable (< 20%), cambia a status `stable` y promueve a produccion.

### Errores comunes al escribir reglas

**1. Reglas demasiado amplias**

```yaml
# MAL: detecta cualquier ejecucion de PowerShell
detection:
  selection:
    Image|endswith: '\powershell.exe'
  condition: selection
# Resultado: miles de alertas diarias

# BIEN: detecta PowerShell con comportamiento sospechoso especifico
detection:
  selection_process:
    Image|endswith: '\powershell.exe'
  selection_suspicious:
    CommandLine|contains|all:
      - '-EncodedCommand'
      - '-WindowStyle Hidden'
  condition: selection_process and selection_suspicious
```

**2. Reglas demasiado estrechas**

```yaml
# MAL: solo detecta un hash especifico de mimikatz
detection:
  selection:
    Hashes|contains: 'SHA256=abc123...'
  condition: selection
# Resultado: solo detecta una version especifica

# BIEN: detecta el comportamiento, no el artefacto
detection:
  selection:
    TargetFilename|contains: 'mimikatz'
  selection_alt:
    CommandLine|contains:
      - 'sekurlsa::logonpasswords'
      - 'lsadump::sam'
      - 'kerberos::golden'
  condition: selection or selection_alt
```

**3. Omitir falsos positivos conocidos**

Siempre documenta escenarios de falsos positivos, incluso si no tienes exclusiones implementadas todavia. Ayuda a otros analistas a entender por que pueden ver falsos positivos y a decidir si una alerta requiere investigacion.

**4. No usar modificadores apropiados**

```yaml
# MAL: busqueda exacta que falla con variaciones de ruta
detection:
  selection:
    Image: 'C:\Windows\System32\cmd.exe'
  condition: selection

# BIEN: usar endswith para ser resiliente a variaciones
detection:
  selection:
    Image|endswith: '\cmd.exe'
  condition: selection
```

## Metodologia de testing para reglas Sigma

Testear reglas Sigma es critico para garantizar que funcionan como se espera antes de llegar a produccion.

### Testing en tres niveles

**Nivel 1: Validacion de sintaxis**

```bash
# sigma check valida la estructura YAML y los campos obligatorios
sigma check rules/custom/my_rule.yml

# Verificar que la conversion no produce errores
sigma convert -t splunk rules/custom/my_rule.yml > /dev/null
```

**Nivel 2: Testing con logs sinteticos**

Crea logs de ejemplo que representen tanto el comportamiento malicioso como el normal, y verifica que la regla produce los resultados esperados.

```yaml
# test_data/wmi_lateral_positive.json
# Debe disparar la regla
{
  "EventID": 1,
  "ParentImage": "C:\\Windows\\System32\\wbem\\WmiPrvSE.exe",
  "Image": "C:\\Windows\\System32\\cmd.exe",
  "CommandLine": "cmd.exe /c whoami",
  "User": "DOMAIN\\admin_user"
}

# test_data/wmi_lateral_negative.json
# NO debe disparar la regla (SCCM legitimo)
{
  "EventID": 1,
  "ParentImage": "C:\\Windows\\System32\\wbem\\WmiPrvSE.exe",
  "Image": "C:\\Windows\\System32\\cmd.exe",
  "CommandLine": "cmd.exe /c C:\\Windows\\CCM\\ccmsetup.exe",
  "User": "SYSTEM"
}
```

**Nivel 3: Testing con simulacion de ataque**

Usar [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) o herramientas equivalentes para ejecutar la tecnica real en un entorno de laboratorio y verificar que la regla la detecta.

```bash
# Ejecutar simulacion de WMI lateral movement
Invoke-AtomicTest T1047 -TestNumbers 1

# Esperar a que los logs se procesen (2-5 minutos)
# Ejecutar la regla convertida en el SIEM de test
# Verificar que se genero la alerta esperada
```

### Automatizar el testing en CI/CD

```yaml
# .github/workflows/sigma-ci.yml
name: Sigma Rules CI
on:
  pull_request:
    paths: ['rules/**']

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install sigma-cli
        run: |
          pip install sigma-cli
          pip install pySigma-backend-splunk
          pip install pySigma-backend-elasticsearch

      - name: Check Sigma syntax
        run: sigma check rules/

      - name: Convert to Splunk (validate)
        run: sigma convert -t splunk rules/ > /dev/null

      - name: Convert to Elastic (validate)
        run: sigma convert -t elasticsearch rules/ > /dev/null

      - name: Check mandatory fields
        run: |
          python scripts/check_mandatory_fields.py rules/
          # Verifica: title, id, status, description, author,
          # date, tags, logsource, detection, falsepositives, level

      - name: Check ATT&CK tags
        run: |
          python scripts/check_attack_tags.py rules/
          # Verifica que cada regla tiene al menos un tag ATT&CK
```

## Mejores practicas para reglas Sigma

### 1. Una regla, un comportamiento

Cada regla debe detectar un comportamiento especifico. No intentes detectar multiples tecnicas en una sola regla.

### 2. Siempre incluir un UUID

El campo `id` debe ser un UUID unico generado con `uuidgen`. Esto permite rastrear la regla a traves de sistemas y evitar duplicados.

### 3. Tags ATT&CK obligatorios

Cada regla debe tener al menos un tag de tactica y tecnica ATT&CK. Esto facilita medir la cobertura.

### 4. Documentar falsos positivos

El campo `falsepositives` no es opcional. Incluso si no conoces falsos positivos, documenta "Unknown" en lugar de omitirlo.

### 5. Usar modificadores en lugar de expresiones regulares

Los modificadores (`contains`, `startswith`, `endswith`) son mas legibles y mas faciles de convertir que las expresiones regulares. Reserva `re` para casos donde los modificadores no son suficientes.

### 6. Organizar por tactica ATT&CK

Estructura el directorio de reglas siguiendo las tacticas ATT&CK:

```
rules/
├── initial_access/
├── execution/
├── persistence/
├── privilege_escalation/
├── defense_evasion/
├── credential_access/
├── discovery/
├── lateral_movement/
├── collection/
├── exfiltration/
└── command_and_control/
```

### 7. Revisar y actualizar regularmente

Las reglas no son estaticas. Programa revisiones trimestrales para:

- Verificar que las reglas siguen siendo relevantes.
- Ajustar exclusiones segun cambios en el entorno.
- Actualizar referencias y mapeos ATT&CK.
- Eliminar reglas obsoletas (status `deprecated`).

### 8. Naming convention consistente

```
# Formato: {tactica}_{tecnica_corta}_{variante}.yml
credential_access_kerberoasting_rc4.yml
lateral_movement_psexec_service.yml
persistence_scheduled_task_temp_folder.yml
defense_evasion_process_injection_createremotethread.yml
```

## Limitaciones de Sigma

Sigma es una herramienta poderosa, pero tiene limitaciones que debes conocer:

### 1. No todos los SIEM son iguales

La conversion no siempre es perfecta. Algunos SIEM no soportan todas las funcionalidades de Sigma (especialmente agregaciones complejas y correlacion temporal). Siempre verifica la query generada.

### 2. Dependencia del backend

La calidad de la conversion depende del backend (plugin) de tu SIEM. Algunos backends estan mas maduros que otros. Splunk y Elastic tienen los backends mas completos.

### 3. Campos no estandarizados

Sigma define nombres de campo genericos, pero no todos los proveedores de logs usan los mismos nombres. Los pipelines de procesamiento mitigan esto, pero requieren mantenimiento.

### 4. Agregaciones limitadas

Las funciones de agregacion de Sigma son basicas comparadas con lo que ofrecen los lenguajes nativos de los SIEM. Para detecciones que requieren correlacion compleja, estadisticas avanzadas o machine learning, necesitaras escribir queries nativas.

### 5. No reemplaza el conocimiento del analista

Sigma facilita escribir y compartir detecciones, pero no sustituye el conocimiento de un analista experimentado que entiende el entorno, las amenazas relevantes y el contexto de negocio.

### 6. Correlacion entre fuentes de datos

Sigma opera sobre una fuente de datos a la vez. Si necesitas correlacionar eventos de multiples fuentes (por ejemplo, un login exitoso seguido de una ejecucion de proceso en otro sistema), necesitas herramientas complementarias o reglas nativas del SIEM.

{{< cta type="bofu" text="Solicita una demo personalizada para tu SOC y descubre como Riskitera integra detecciones Sigma con IA soberana para priorizar alertas." label="Solicitar demo" >}}


**Articulos relacionados:**
- [Que Es Un Siem Para Que Sirve](/es/posts/2026/04/que-es-un-siem-para-que-sirve/)
- [Mitre Attack Que Es Como Usarlo](/es/posts/2026/04/mitre-attack-que-es-como-usarlo/)

## Preguntas frecuentes

### Sigma reemplaza las reglas nativas de mi SIEM?

No. Sigma complementa las reglas nativas, no las reemplaza. Para detecciones estandar que se benefician de portabilidad (brute force, movimiento lateral, persistencia comun), Sigma es ideal. Para detecciones que requieren funcionalidades especificas de tu SIEM (machine learning, correlacion compleja entre multiples fuentes, queries de rendimiento optimizado), seguiras necesitando reglas nativas. El enfoque recomendado es usar Sigma para el 70-80% de tus detecciones y reglas nativas para el 20-30% restante.

### Cuantas reglas de SigmaHQ deberia desplegar?

No despliegues todas las 3.000+ reglas de golpe. Empieza con las reglas marcadas como `stable` que cubren las tacticas mas criticas para tu entorno (initial access, execution, persistence, credential access). Un buen punto de partida son 50-100 reglas cuidadosamente seleccionadas y validadas. Despues, expande gradualmente basandote en los gaps de cobertura ATT&CK y la threat intelligence relevante para tu sector.

### Que SIEM tiene mejor soporte para Sigma?

Splunk y Elastic Security son los SIEM con los backends de conversion mas maduros y mejor mantenidos. Microsoft Sentinel tambien tiene buen soporte via el backend Kusto. Wazuh, Graylog y QRadar tienen backends funcionales pero con algunas limitaciones en funcionalidades avanzadas. Si usas un SIEM menos comun, verifica la lista de backends disponibles en el [repositorio de pySigma](https://github.com/SigmaHQ/pySigma) antes de invertir tiempo en adoptar Sigma.

### Puedo contribuir reglas a SigmaHQ?

Si. SigmaHQ acepta contribuciones via pull request en GitHub. Tu regla debe cumplir los estandares de calidad del proyecto: campos obligatorios completos, tags ATT&CK correctos, falsos positivos documentados, y status apropiado (normalmente `test` o `experimental` para reglas nuevas). Antes de contribuir, revisa las [guias de contribucion](https://github.com/SigmaHQ/sigma/blob/master/CONTRIBUTING.md) y busca si ya existe una regla similar.

### Como integro Sigma con mi pipeline de detection-as-code?

La integracion tipica es: (1) almacena tus reglas Sigma en un repositorio Git, (2) configura un pipeline de CI que ejecute `sigma check` y `sigma convert` para validar las reglas en cada pull request, (3) cuando se aprueba y mergea el PR, un pipeline de CD convierte las reglas al formato de tu SIEM y las despliega automaticamente, (4) monitoriza las metricas de las reglas desplegadas (volumen de alertas, tasa de falsos positivos) y retroalimenta el proceso. Herramientas como GitHub Actions o GitLab CI son suficientes para montar este pipeline sin infraestructura adicional.
