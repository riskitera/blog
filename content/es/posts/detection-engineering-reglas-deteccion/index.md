---
title: "Detection Engineering: como construir reglas de deteccion que realmente funcionen"
description: "Guia practica de detection engineering: como disenar, implementar y mantener reglas de deteccion eficaces en un SOC, reducir falsos positivos y medir la calidad de las detecciones."
slug: "detection-engineering-reglas-deteccion"
date: 2026-06-02
publishDate: 2026-06-02
lastmod: 2026-06-02
draft: false
tags: ["SOC", "Detection Engineering", "Operaciones"]
categories: ["SOC"]
author: "David Moya"
keyword: "detection engineering"
funnel: "mofu"
---

Guia practica de detection engineering: como disenar, implementar y mantener reglas de deteccion eficaces en un SOC, reducir falsos positivos y medir la calidad de las detecciones.

<!--more-->

{{< key-takeaways >}}
- Detection engineering aplica principios de ingenieria de software (versionado, testing, CI/CD) al ciclo de vida completo de las reglas de deteccion.
- El ciclo de vida de una deteccion tiene cinco fases: hipotesis, escritura de regla, testing, despliegue y tuning continuo.
- La matriz de cobertura MITRE ATT&CK permite identificar gaps de visibilidad y priorizar donde invertir esfuerzo.
- Atomic Red Team y DeTT&CT son herramientas clave para validar que las detecciones funcionan antes de llegar a produccion.
- Reducir falsos positivos no es opcional: un SOC saturado de ruido pierde la capacidad de detectar amenazas reales.
{{< /key-takeaways >}}

## Que es detection engineering

Detection engineering es la disciplina que aplica principios de ingenieria de software al proceso de crear, mantener y mejorar reglas de deteccion en un centro de operaciones de seguridad (SOC). No se trata solo de escribir queries en un SIEM. Se trata de tratar las detecciones como codigo: versionado, testeado, desplegado de forma controlada y medido en produccion.

El termino fue popularizado por [Jared Atkinson](https://posts.specterops.io/detection-spectrum-198a0bfb9302) y la comunidad de SpecterOps, aunque la practica existe desde que los primeros equipos de seguridad se dieron cuenta de que copiar reglas de un foro y pegarlas en el SIEM no escalaba.

En un SOC tradicional, las reglas de deteccion suelen vivir dentro del SIEM como objetos propietarios. Nadie sabe quien las creo, cuando se modificaron por ultima vez ni si siguen siendo relevantes. Detection engineering cambia eso radicalmente.

### Detection-as-Code: la filosofia central

La idea central de detection-as-code es simple: las reglas de deteccion deben vivir en un repositorio Git, igual que el codigo de cualquier aplicacion. Esto implica:

- **Versionado**: cada cambio a una regla queda registrado con autor, fecha y motivo.
- **Code review**: otro analista revisa la regla antes de que llegue a produccion.
- **Testing automatizado**: un pipeline de CI valida que la regla no tiene errores de sintaxis y que detecta lo que debe detectar.
- **Despliegue controlado**: la regla se despliega al SIEM mediante un pipeline, no a mano.
- **Rollback**: si una regla genera problemas, se revierte como cualquier otro cambio de codigo.

Una estructura tipica de repositorio detection-as-code:

```
detections/
├── rules/
│   ├── credential_access/
│   │   ├── brute_force_login.yml
│   │   └── kerberoasting.yml
│   ├── lateral_movement/
│   │   ├── psexec_usage.yml
│   │   └── wmi_remote_execution.yml
│   └── persistence/
│       ├── scheduled_task_creation.yml
│       └── registry_run_key.yml
├── tests/
│   ├── credential_access/
│   │   ├── brute_force_login_test.yml
│   │   └── kerberoasting_test.yml
│   └── ...
├── pipelines/
│   ├── deploy_splunk.yml
│   └── deploy_elastic.yml
├── docs/
│   └── runbooks/
└── .github/
    └── workflows/
        └── ci.yml
```

### Por que importa en 2026

El volumen de telemetria que genera una organizacion media ha crecido exponencialmente. Un endpoint con EDR genera decenas de miles de eventos por dia. Multiplicado por cientos o miles de endpoints, mas logs de red, cloud, identidad y aplicaciones, el resultado es un flujo de datos que ningun equipo puede revisar manualmente.

Sin detection engineering, los SOC caen en una de dos trampas: o tienen muy pocas reglas y dejan pasar amenazas reales, o tienen demasiadas reglas mal calibradas y ahogan a los analistas en falsos positivos. Ambas situaciones son peligrosas.

## El ciclo de vida de una deteccion

Cada regla de deteccion pasa por un ciclo de vida con cinco fases. Saltarse cualquiera de ellas es la receta para reglas que no funcionan o que generan mas ruido del que eliminan.

### Fase 1: Hipotesis

Todo empieza con una pregunta: "que comportamiento malicioso queremos detectar?". La hipotesis debe ser especifica y basada en inteligencia de amenazas real.

Ejemplos de hipotesis bien formuladas:

- "Un atacante que obtiene credenciales validas intentara acceder a multiples sistemas en un periodo corto de tiempo usando RDP."
- "Un atacante que establece persistencia en Windows creara una tarea programada con `schtasks.exe` apuntando a un ejecutable en una ruta no estandar."
- "Un atacante que realiza movimiento lateral usara WMI para ejecutar comandos de forma remota."

Ejemplos de hipotesis mal formuladas:

- "Detectar hackers." (demasiado vago)
- "Alertar cuando haya actividad sospechosa." (sin criterio operativo)

La hipotesis debe vincularse a una tecnica de [MITRE ATT&CK](https://attack.mitre.org/) siempre que sea posible. Esto facilita medir la cobertura y comunicar el valor de la deteccion al resto de la organizacion.

### Fase 2: Escritura de la regla

Con la hipotesis clara, el siguiente paso es escribir la regla. Esto implica definir:

1. **Fuente de datos**: que logs necesitas (Windows Security Events, Sysmon, EDR telemetry, network flow, etc.).
2. **Logica de deteccion**: las condiciones que deben cumplirse para que salte la alerta.
3. **Contexto de enriquecimiento**: que informacion adicional necesita el analista para investigar la alerta.
4. **Nivel de severidad**: como de critica es la alerta si resulta ser un verdadero positivo.
5. **Runbook asociado**: los pasos que debe seguir el analista cuando recibe la alerta.

Un ejemplo en pseudocodigo YAML:

```yaml
name: Sospecha de Kerberoasting
description: >
  Detecta solicitudes de tickets de servicio (TGS) para cuentas
  con SPN configurado, patron comun en ataques de Kerberoasting.
mitre_attack:
  tactic: Credential Access
  technique: T1558.003
  name: Kerberoasting
data_sources:
  - Windows Security Event Log (Event ID 4769)
severity: high
logic: |
  source = "WinSecurityEvent"
  AND EventID = 4769
  AND TicketEncryptionType IN ("0x17", "0x18")  # RC4 o AES
  AND ServiceName NOT LIKE "$*"                  # Excluir cuentas de maquina
  AND ServiceName NOT IN (whitelist_service_accounts)
  AND count(distinct ServiceName) > 3 within 5 minutes by SourceIP
enrichment:
  - Resolver SourceIP a hostname y usuario
  - Consultar historial de actividad del usuario
  - Verificar si las cuentas de servicio son privilegiadas
false_positive_scenarios:
  - Escaneos de vulnerabilidades programados
  - Herramientas de inventario de Active Directory
  - Cuentas de servicio de monitoreo
runbook: docs/runbooks/kerberoasting.md
```

### Fase 3: Testing

Aqui es donde muchos equipos fallan. Escribir una regla sin testearla es como escribir codigo sin ejecutarlo. El testing de detecciones tiene dos dimensiones:

**Testing positivo**: verificar que la regla detecta el comportamiento malicioso. Para esto se usan herramientas como [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) que simulan tecnicas de ataque de forma segura.

**Testing negativo**: verificar que la regla NO salta con actividad legitima. Esto requiere ejecutar la regla contra logs historicos de produccion y analizar los resultados.

```bash
# Ejecutar un test atomico para Kerberoasting
Invoke-AtomicTest T1558.003 -TestNumbers 1

# Verificar que el SIEM genero la alerta esperada
# (automatizar con script de validacion)
python validate_detection.py \
  --rule kerberoasting.yml \
  --expected-alerts 1 \
  --timeout 300
```

### Fase 4: Despliegue

El despliegue debe ser automatizado mediante un pipeline de CI/CD. El flujo tipico:

1. El analista crea un pull request con la nueva regla.
2. El pipeline de CI ejecuta validaciones: sintaxis, tests unitarios, linting.
3. Otro analista revisa el PR (code review).
4. Al aprobar el merge, el pipeline de CD despliega la regla al SIEM de staging.
5. Periodo de observacion en staging (24-72 horas).
6. Promocion a produccion.

```yaml
# .github/workflows/deploy-detections.yml
name: Deploy Detections
on:
  push:
    branches: [main]
    paths: ['rules/**']

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Lint YAML
        run: yamllint rules/
      - name: Validate Sigma syntax
        run: sigma check rules/
      - name: Run unit tests
        run: pytest tests/ -v

  deploy-staging:
    needs: validate
    runs-on: ubuntu-latest
    steps:
      - name: Convert and deploy to staging SIEM
        run: |
          sigma convert -t splunk rules/ -o output/
          python deploy.py --env staging --rules output/

  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Deploy to production SIEM
        run: python deploy.py --env production --rules output/
```

### Fase 5: Tuning continuo

Una regla desplegada no es una regla terminada. El tuning es un proceso continuo que incluye:

- **Monitorizar la tasa de falsos positivos**: si supera un umbral (por ejemplo, 80%), la regla necesita ajuste.
- **Revisar falsos negativos**: usar threat hunting y purple team exercises para descubrir que se esta escapando.
- **Actualizar exclusiones**: anadir excepciones legitimas documentadas.
- **Ajustar umbrales**: modificar conteos, ventanas temporales y condiciones segun el entorno.

```yaml
# Ejemplo de exclusion documentada
exclusions:
  - description: "Scan de Qualys programado los domingos a las 03:00"
    added_by: "analyst_jgarcia"
    added_date: "2026-03-15"
    condition: "SourceIP IN ('10.50.1.100', '10.50.1.101')"
    review_date: "2026-06-15"  # Revisar en 3 meses
```

## Cobertura MITRE ATT&CK: el mapa de tu visibilidad

La matriz de [MITRE ATT&CK](https://attack.mitre.org/) es el framework de referencia para catalogar tecnicas de adversarios. Pero su valor real para detection engineering no esta en conocer las tecnicas, sino en mapear cuales tienes cubiertas y cuales no.

### Construir una matriz de cobertura

Una matriz de cobertura es un documento que cruza las tecnicas de ATT&CK con el estado actual de tus detecciones. Para cada tecnica, se registra:

| Campo | Descripcion |
|-------|-------------|
| Tecnica ID | Identificador ATT&CK (ej. T1059.001) |
| Nombre | PowerShell Execution |
| Fuente de datos disponible | Si/No (tienes logs que cubren esta tecnica?) |
| Regla implementada | Si/No |
| Estado de la regla | Draft / Testing / Staging / Production |
| Tasa de falsos positivos | Porcentaje medido |
| Ultima revision | Fecha |

### DeTT&CT: automatizar la medicion de cobertura

[DeTT&CT](https://github.com/rabobank-cdc/DeTTECT) (Detect Tactics, Techniques & Combat Threats) es un framework open source creado por Rabobank que automatiza la creacion de matrices de cobertura. Permite:

- Definir la visibilidad de datos (que fuentes de logs tienes y con que calidad).
- Mapear las detecciones existentes a tecnicas ATT&CK.
- Generar heatmaps visuales que muestran donde tienes cobertura y donde hay gaps.
- Comparar tu cobertura contra grupos de amenazas especificos.

```yaml
# Ejemplo de fichero de visibilidad de datos para DeTT&CT
data_sources:
  - data_source_name: Process Creation
    date_registered: 2026-01-15
    date_connected: 2026-01-20
    products:
      - product_name: Sysmon
        available_for_data_analytics: true
        data_quality:
          device_completeness: 4  # 1-5
          data_field_completeness: 5
          timeliness: 4
          consistency: 5
          retention: 3
    comment: "Sysmon desplegado en todos los endpoints Windows"

  - data_source_name: Network Connection
    date_registered: 2026-02-01
    date_connected: 2026-02-10
    products:
      - product_name: Zeek
        available_for_data_analytics: true
        data_quality:
          device_completeness: 3
          data_field_completeness: 4
          timeliness: 5
          consistency: 4
          retention: 3
    comment: "Zeek en segmentos criticos, no en DMZ"
```

### Priorizar por amenaza real

No tiene sentido intentar cubrir las 200+ tecnicas de ATT&CK de golpe. La priorizacion debe basarse en:

1. **Threat intelligence**: que tecnicas usan los grupos de amenazas relevantes para tu sector (financiero, salud, infraestructura critica, etc.).
2. **Superficie de ataque**: si no tienes infraestructura cloud, no priorices tecnicas cloud.
3. **Impacto potencial**: tecnicas de exfiltracion y ransomware suelen tener prioridad sobre tecnicas de reconocimiento.
4. **Viabilidad de deteccion**: algunas tecnicas son inherentemente dificiles de detectar (ej. living-off-the-land). Empieza por las que puedes detectar con confianza.

## Testing de detecciones con Atomic Red Team

[Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) es un proyecto de Red Canary que proporciona tests atomicos mapeados a tecnicas MITRE ATT&CK. Cada test es una simulacion pequena y autocontenida de una tecnica de ataque que se puede ejecutar de forma segura en un entorno controlado.

### Por que Atomic Red Team

La alternativa a Atomic Red Team es testear detecciones de forma manual, lo cual no escala. Con Atomic Red Team:

- Cada test esta mapeado a una tecnica ATT&CK especifica.
- Los tests son reproducibles y automatizables.
- Se pueden integrar en pipelines de CI/CD.
- La comunidad mantiene cientos de tests actualizados.

### Ejecutar tests atomicos

```powershell
# Instalar el framework
Install-Module -Name invoke-atomicredteam -Scope CurrentUser

# Listar tests disponibles para una tecnica
Invoke-AtomicTest T1059.001 -ShowDetailsBrief

# Ejecutar un test especifico
Invoke-AtomicTest T1059.001 -TestNumbers 1

# Ejecutar y verificar prerequisitos
Invoke-AtomicTest T1059.001 -TestNumbers 1 -CheckPrereqs

# Limpiar artefactos despues del test
Invoke-AtomicTest T1059.001 -TestNumbers 1 -Cleanup
```

### Integrar Atomic Red Team en el pipeline de validacion

El flujo ideal es:

1. El pipeline despliega la regla de deteccion en el SIEM de staging.
2. Ejecuta el test atomico correspondiente contra un endpoint de test.
3. Espera un tiempo definido (2-5 minutos) para que el SIEM procese los logs.
4. Consulta el SIEM para verificar que se genero la alerta esperada.
5. Si la alerta no aparece, el pipeline falla y bloquea el merge.

```python
# validate_detection.py
import time
import requests

def validate_detection(rule_name, siem_url, api_key, timeout=300):
    """Valida que una deteccion genero la alerta esperada en el SIEM."""
    start_time = time.time()

    while time.time() - start_time < timeout:
        response = requests.get(
            f"{siem_url}/api/alerts",
            headers={"Authorization": f"Bearer {api_key}"},
            params={
                "rule_name": rule_name,
                "time_range": "5m",
                "status": "new"
            }
        )
        alerts = response.json().get("results", [])

        if len(alerts) > 0:
            print(f"[PASS] Regla '{rule_name}' genero {len(alerts)} alerta(s)")
            return True

        time.sleep(15)

    print(f"[FAIL] Regla '{rule_name}' no genero alertas en {timeout}s")
    return False
```

### Limitaciones de Atomic Red Team

Atomic Red Team es excelente para validaciones rapidas, pero tiene limitaciones:

- Los tests son atomicos (acciones individuales), no simulan cadenas de ataque completas.
- Algunos tests requieren privilegios elevados o infraestructura especifica.
- No cubre todas las tecnicas ATT&CK.
- No sustituye a un red team real o a ejercicios de purple team.

Para cadenas de ataque completas, complementa con herramientas como [MITRE Caldera](https://caldera.mitre.org/), [Infection Monkey](https://www.akamai.com/infectionmonkey) o ejercicios manuales de purple team.

## Como reducir falsos positivos

Los falsos positivos son el enemigo numero uno de cualquier SOC. Una regla que genera 50 alertas diarias de las cuales 49 son falsas no solo desperdicia tiempo de los analistas, sino que entrena al equipo a ignorar alertas, lo cual es exactamente lo que un atacante quiere.

### Estrategias para reducir falsos positivos

**1. Baseline del entorno**

Antes de activar una regla en produccion, ejecutala en modo "observacion" durante al menos una semana. Analiza los resultados y crea un baseline de lo que es normal en tu entorno.

```yaml
# Ejemplo: regla en modo observacion
name: Ejecucion sospechosa de PowerShell codificado
status: observation  # No genera alerta, solo log
observation_period: 7d
observation_start: 2026-05-01
logic: |
  process_name = "powershell.exe"
  AND command_line CONTAINS "-EncodedCommand"
  AND parent_process NOT IN (known_automation_tools)
```

**2. Whitelist basada en contexto**

Las exclusiones deben ser especificas y documentadas. Nunca excluyas de forma generica.

```yaml
# MAL: exclusion generica
exclusion: SourceIP = "10.0.0.0/8"  # Excluye toda la red interna

# BIEN: exclusion especifica y documentada
exclusions:
  - condition: >
      SourceIP = "10.50.1.100"
      AND DestinationPort = 445
      AND TimeOfDay BETWEEN "02:00" AND "04:00"
    reason: "Backup server accede a shares SMB en ventana nocturna"
    owner: "team_infra"
    expires: "2026-09-01"
```

**3. Correlacion temporal y por entidad**

En lugar de alertar por un solo evento, correlaciona multiples eventos en una ventana temporal agrupados por entidad (usuario, IP, hostname).

```yaml
# En lugar de alertar por cada login fallido...
# Correlacionar: 5+ fallos seguidos de un exito desde la misma IP
logic: |
  sequence by SourceIP within 10m
    [authentication where outcome = "failure"] with count >= 5
    [authentication where outcome = "success"]
severity: high
```

**4. Scoring en lugar de alertas binarias**

Asigna puntuaciones a diferentes indicadores y solo alerta cuando la puntuacion supera un umbral.

```yaml
scoring_rules:
  - condition: "encoded_powershell"
    score: 30
  - condition: "executed_from_temp_folder"
    score: 20
  - condition: "parent_process_is_office_app"
    score: 25
  - condition: "network_connection_to_external_ip"
    score: 25

alert_threshold: 70  # Solo alerta si score >= 70
```

**5. Feedback loop con analistas**

Implementa un sistema donde los analistas puedan marcar alertas como falsos positivos con un motivo estructurado. Usa esa informacion para ajustar las reglas automaticamente.

### Metricas de falsos positivos

Las metricas que debes monitorizar:

- **False Positive Rate (FPR)**: porcentaje de alertas que resultan ser falsas. Objetivo: < 20%.
- **Mean Time to Triage (MTTT)**: tiempo medio que tarda un analista en clasificar una alerta. Si sube, probablemente hay demasiado ruido.
- **Alert fatigue index**: numero de alertas por analista por turno. Mas de 50 alertas por turno de 8 horas empieza a ser problematico.

## El Detection Maturity Model

El Detection Maturity Model (DMM) es un framework para evaluar la madurez del programa de detection engineering de una organizacion. Tiene cinco niveles:

### Nivel 0: Reactivo

- Las detecciones se crean solo despues de un incidente.
- No hay proceso formal de desarrollo de reglas.
- Las reglas viven exclusivamente dentro del SIEM.
- No hay testing ni validacion.

### Nivel 1: Basico

- Existen reglas basicas (firmas, IOCs, reglas de umbral).
- Las reglas se documentan minimamente.
- El equipo empieza a usar frameworks como MITRE ATT&CK como referencia.
- El testing es manual y esporadico.

### Nivel 2: Procedural

- Las detecciones se gestionan como un proceso formal.
- Las reglas se almacenan en un repositorio centralizado.
- Existe un proceso de review antes de desplegar.
- Se mide la tasa de falsos positivos.
- Se empieza a usar Sigma u otros formatos portables.

### Nivel 3: Detection-as-Code

- Las reglas viven en Git con versionado completo.
- Pipeline de CI/CD para validacion y despliegue.
- Testing automatizado con Atomic Red Team o similar.
- Cobertura ATT&CK medida y visualizada.
- Feedback loop con analistas integrado.
- Exclusiones documentadas y con fecha de expiracion.

### Nivel 4: Proactivo y medido

- Threat hunting continuo alimenta nuevas hipotesis de deteccion.
- Metricas de calidad (FPR, MTTD, cobertura) en dashboards en tiempo real.
- Purple team exercises regulares para validar la efectividad.
- Las detecciones se priorizan segun threat intelligence del sector.
- El programa de deteccion se reporta a nivel directivo con metricas de negocio.

La mayoria de organizaciones estan entre el nivel 0 y el nivel 2. Llegar al nivel 3 requiere inversion en tooling y procesos, pero el retorno es enorme en terminos de eficacia del SOC.

## Como medir la calidad de las detecciones

No se puede mejorar lo que no se mide. Estas son las metricas clave para un programa de detection engineering:

### Metricas de eficacia

| Metrica | Descripcion | Objetivo tipico |
|---------|-------------|-----------------|
| Mean Time to Detect (MTTD) | Tiempo desde el evento malicioso hasta la alerta | < 15 minutos |
| Detection Coverage | Porcentaje de tecnicas ATT&CK cubiertas | > 60% para tacticas criticas |
| True Positive Rate | Porcentaje de alertas que son verdaderos positivos | > 80% |
| False Positive Rate | Porcentaje de alertas que son falsos positivos | < 20% |

### Metricas operativas

| Metrica | Descripcion | Objetivo tipico |
|---------|-------------|-----------------|
| Rules in production | Numero total de reglas activas | Depende del entorno |
| Rules added per month | Velocidad de desarrollo | 5-15 por mes |
| Rules tuned per month | Velocidad de mantenimiento | 10-20% del total/trimestre |
| Alert volume per analyst | Carga de trabajo | < 50 por turno de 8h |
| Stale rules | Reglas sin revision en > 6 meses | 0 |

### Metricas de proceso

| Metrica | Descripcion | Objetivo tipico |
|---------|-------------|-----------------|
| Time from hypothesis to production | Velocidad del ciclo completo | < 2 semanas |
| Code review turnaround | Tiempo de revision de PRs | < 48 horas |
| Test coverage | Porcentaje de reglas con test automatizado | > 80% |

### Dashboard de detection engineering

Un dashboard util incluye:

- Heatmap de cobertura ATT&CK (actualizado semanalmente).
- Tendencia de FPR por regla y por categoria.
- Top 10 reglas por volumen de alertas.
- Top 10 reglas por tasa de falsos positivos (candidatas a tuning).
- Velocidad de desarrollo (reglas nuevas por sprint).
- Reglas sin revision en mas de 90 dias.

## Herramientas clave para detection engineering

### Para escribir y gestionar reglas

- **[Sigma](https://github.com/SigmaHQ/sigma)**: formato portable de detecciones. Escribe una vez, convierte a cualquier SIEM.
- **[Splunk Security Content](https://github.com/splunk/security_content)**: biblioteca de detecciones pre-escritas para Splunk.
- **[Elastic Detection Rules](https://github.com/elastic/detection-rules)**: repositorio oficial de reglas para Elastic Security.

### Para testear detecciones

- **[Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)**: tests atomicos mapeados a ATT&CK.
- **[MITRE Caldera](https://caldera.mitre.org/)**: plataforma de emulacion de adversarios automatizada.
- **[Infection Monkey](https://www.akamai.com/infectionmonkey)**: herramienta de breach and attack simulation.

### Para medir cobertura

- **[DeTT&CT](https://github.com/rabobank-cdc/DeTTECT)**: framework para medir y visualizar cobertura ATT&CK.
- **[ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)**: herramienta oficial de MITRE para crear heatmaps de cobertura.

### Para automatizar el pipeline

- **GitHub Actions / GitLab CI**: para pipelines de CI/CD de detecciones.
- **sigma-cli**: herramienta de linea de comandos para convertir y validar reglas Sigma.
- **SOAR platforms**: para orquestar la respuesta automatizada cuando se activa una deteccion.

{{< cta type="tofu" text="Riskitera automatiza el triage, la correlacion y el reporting de tu SOC con IA soberana." label="Ver demo SOC" >}}

## Ejemplo practico: de hipotesis a produccion

Para aterrizar toda la teoria, veamos un ejemplo completo del ciclo de vida de una deteccion.

### Hipotesis

"Un atacante que ha comprometido credenciales de un usuario realizara movimiento lateral usando PsExec, creando un servicio temporal en el sistema remoto."

Tecnica ATT&CK: [T1021.002 - Remote Services: SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002/)

### Analisis de datos disponibles

Fuentes necesarias:
- Windows Security Event 7045 (Service Installed): registra la creacion de servicios.
- Sysmon Event 1 (Process Create): registra la ejecucion de procesos.
- Sysmon Event 17/18 (Pipe Created/Connected): PsExec usa named pipes.

### Regla en formato Sigma

```yaml
title: PsExec Service Installation
id: c3f0a541-7c25-4a64-9bc8-7e921f123456
status: production
description: >
  Detecta la instalacion del servicio PSEXESVC asociado
  a la ejecucion remota de PsExec de Sysinternals.
references:
  - https://attack.mitre.org/techniques/T1021/002/
  - https://jpcertcc.github.io/ToolAnalysisResultSheet/
author: SOC Team
date: 2026/05/15
modified: 2026/05/20
tags:
  - attack.lateral_movement
  - attack.t1021.002
logsource:
  category: driver_load
  product: windows
detection:
  selection_service:
    ServiceName|startswith: 'PSEXESVC'
  selection_pipe:
    PipeName|contains:
      - '\PSEXESVC'
  condition: selection_service or selection_pipe
falsepositives:
  - Administradores IT usando PsExec de forma legitima
  - Herramientas de despliegue que usan PsExec internamente
level: high
```

### Test con Atomic Red Team

```powershell
# Test: ejecutar PsExec contra un endpoint de test
Invoke-AtomicTest T1021.002 -TestNumbers 1

# Verificar que se genero Event ID 7045 con ServiceName PSEXESVC
Get-WinEvent -FilterHashtable @{
    LogName = 'System'
    ID = 7045
} | Where-Object { $_.Message -like '*PSEXESVC*' }
```

### Resultado

La regla se despliega en staging, se valida durante 48 horas (0 falsos positivos porque PsExec no se usa en el entorno controlado), y se promueve a produccion. Se anade una exclusion documentada para el equipo de IT que usa PsExec para despliegues de software los martes y jueves entre las 10:00 y las 12:00.

{{< cta type="bofu" text="Solicita una demo personalizada para tu SOC y descubre como Riskitera optimiza tus operaciones de deteccion con IA." label="Solicitar demo" >}}


**Articulos relacionados:**
- [Como Montar Soc Desde Cero](/es/posts/2026/04/como-montar-soc-desde-cero/)
- [Mitre Attack Que Es Como Usarlo](/es/posts/2026/04/mitre-attack-que-es-como-usarlo/)

## Preguntas frecuentes

### Que diferencia hay entre detection engineering y threat hunting?

Detection engineering se centra en crear reglas automatizadas que alertan de comportamientos maliciosos conocidos o esperados. Threat hunting es una actividad proactiva donde un analista busca manualmente evidencia de amenazas que las reglas existentes no cubren. Son disciplinas complementarias: los hallazgos del threat hunting alimentan nuevas hipotesis de deteccion, y las reglas de deteccion liberan tiempo para que los hunters se centren en lo desconocido.

### Cuanto tiempo se tarda en implementar un programa de detection engineering?

Depende del punto de partida. Un SOC que ya tiene reglas en un SIEM puede empezar a adoptar detection-as-code en 2-3 meses (migrar reglas a Git, configurar un pipeline basico de CI). Llegar a un nivel 3 de madurez (pipeline completo con testing automatizado, metricas y cobertura ATT&CK medida) suele requerir 6-12 meses de trabajo dedicado. Lo importante es empezar con un scope pequeno (por ejemplo, las 10 reglas mas criticas) e iterar.

### Se puede hacer detection engineering sin un SIEM caro?

Si. El formato Sigma permite escribir detecciones portables que se pueden convertir a cualquier SIEM, incluyendo opciones open source como Wazuh, Graylog o OpenSearch. El repositorio Git, el pipeline de CI y herramientas como Atomic Red Team y DeTT&CT son gratuitas. Lo que necesitas es un equipo con conocimiento tecnico y tiempo dedicado, no necesariamente un SIEM enterprise.

### Cuantas reglas de deteccion deberia tener un SOC?

No hay un numero magico. Mas reglas no significa mejor deteccion. Un SOC con 50 reglas bien calibradas, testeadas y mantenidas es mas efectivo que uno con 500 reglas sin mantener. Como referencia, un SOC maduro que cubre las tacticas criticas de ATT&CK (initial access, execution, persistence, credential access, lateral movement, exfiltration) suele tener entre 100 y 300 reglas activas en produccion.

### Como convencer a la direccion de invertir en detection engineering?

Los argumentos que funcionan: (1) reduccion de MTTD medible (si se detecta antes, el impacto del incidente es menor), (2) reduccion de falsos positivos (menos horas de analista desperdiciadas, lo cual se traduce en ahorro directo), (3) cobertura medible contra frameworks reconocidos como MITRE ATT&CK (los auditores y reguladores valoran esto), y (4) reduccion de riesgo de incidentes graves (el coste medio de un breach en Europa supera los 4 millones de euros segun IBM). Presenta metricas concretas, no argumentos abstractos sobre "mejorar la seguridad".
