---
title: "SLAs en ciberseguridad: como definir MTTR, MTTD y no morir en la auditoria"
description: "Guia practica para definir SLAs de ciberseguridad: MTTR, MTTD, MTTC, benchmarks del sector, como medirlos y como presentarlos en auditorias de seguridad."
slug: "sla-ciberseguridad-mttr-mttd"
date: 2026-06-20
publishDate: 2026-06-20
lastmod: 2026-06-20
draft: false
tags: ["SOC", "GRC", "Operaciones"]
categories: ["SOC"]
author: "David Moya"
keyword: "SLA ciberseguridad"
funnel: "mofu"
---

Guia practica para definir SLAs de ciberseguridad: MTTR, MTTD, MTTC, benchmarks del sector, como medirlos y como presentarlos en auditorias de seguridad.

<!--more-->

{{< key-takeaways >}}
- MTTR, MTTD y MTTC son las tres metricas fundamentales que cualquier SOC debe medir para demostrar eficacia operativa.
- Los benchmarks del sector situan el MTTD medio en 204 dias y el MTTR en 73 dias, cifras que cualquier organizacion seria deberia mejorar significativamente.
- Los SLAs contractuales con MSSPs deben incluir penalizaciones concretas y mecanismos de verificacion independiente.
- El ENS y la directiva NIS2 exigen tiempos de notificacion y respuesta que condicionan directamente los SLAs internos.
- La automatizacion del triage y la correlacion de alertas puede reducir el MTTD en un 60-80% respecto a procesos manuales.
{{< /key-takeaways >}}

## Que son los SLAs en ciberseguridad?

Un SLA (Service Level Agreement) en ciberseguridad es un compromiso formal, medible y contractualmente vinculante, que define los niveles minimos de servicio que un equipo de seguridad (interno o externo) debe cumplir. No se trata de un documento decorativo para la carpeta de compliance: es la columna vertebral operativa de cualquier SOC que pretenda funcionar de forma profesional.

En el contexto de un centro de operaciones de seguridad, los SLAs definen aspectos como el tiempo maximo para detectar una amenaza, el tiempo maximo para contenerla, la frecuencia de reporting, la disponibilidad del servicio (24x7 o en franjas horarias) y los procedimientos de escalado. Son, en esencia, la traduccion cuantitativa de lo que la organizacion espera de su capacidad defensiva.

La importancia de los SLAs va mucho mas alla de la relacion con un proveedor MSSP. Incluso cuando el SOC es 100% interno, definir SLAs claros permite tres cosas fundamentales:

1. **Medir la mejora continua.** Sin metricas base, es imposible saber si las inversiones en herramientas, personal o procesos estan dando resultado.
2. **Rendir cuentas ante la direccion.** Un CISO que presenta metricas concretas (tiempo medio de deteccion reducido un 40% en seis meses) tiene mucho mas impacto que uno que habla de "mejora general".
3. **Cumplir con marcos regulatorios.** Tanto el [Esquema Nacional de Seguridad (ENS)](https://www.boe.es/eli/es/rd/2022/05/03/311) como la [Directiva NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555) establecen requisitos de notificacion y respuesta que solo se pueden garantizar con SLAs bien definidos.

En Espana, el contexto regulatorio hace que los SLAs de ciberseguridad no sean opcionales para la administracion publica ni para operadores de servicios esenciales. Son un requisito legal.

## Que significan MTTR, MTTD y MTTC?

Las tres metricas fundamentales que vertebran los SLAs de cualquier SOC son MTTD, MTTC y MTTR. Vamos a desgranarlas una por una, porque confundirlas (algo habitual) puede llevar a SLAs que no reflejan la realidad operativa.

### MTTD: Mean Time To Detect

El MTTD mide el tiempo medio que transcurre desde que una amenaza o incidente se produce hasta que el SOC lo detecta. Es, probablemente, la metrica mas critica porque lo que no se detecta no se puede contener.

**Que incluye el MTTD:**
- Tiempo desde el compromiso inicial hasta que una regla de correlacion, un analista o un feed de threat intelligence genera una alerta.
- Incluye el tiempo de ingestion de logs, procesamiento por el SIEM y generacion de la alerta.

**Que NO incluye:**
- El tiempo de validacion (eso es parte del triage).
- El tiempo de respuesta (eso es MTTR).

**Ejemplo practico:** Un atacante compromete credenciales de un empleado el lunes a las 09:00. El SIEM detecta un patron anomalo de acceso el miercoles a las 15:00. El MTTD es de 54 horas.

### MTTC: Mean Time To Contain

El MTTC mide el tiempo desde que se confirma un incidente hasta que se contiene su propagacion. Es la metrica que mas directamente impacta en la reduccion de dano.

**Que incluye el MTTC:**
- Aislamiento del sistema comprometido.
- Bloqueo de cuentas afectadas.
- Aplicacion de reglas de firewall de emergencia.
- Desactivacion de servicios comprometidos.

**Ejemplo practico:** Se confirma un ransomware a las 10:00. A las 10:45 se han aislado los tres servidores afectados y bloqueado la cuenta comprometida. MTTC: 45 minutos.

### MTTR: Mean Time To Respond (o Recover)

El MTTR tiene dos acepciones comunes: Mean Time To Respond y Mean Time To Recover. En ciberseguridad, la distincion importa:

- **MTTR (Respond):** Tiempo desde la deteccion hasta que se inicia la primera accion de respuesta. Cubre la fase de triage y escalado.
- **MTTR (Recover):** Tiempo desde la deteccion hasta la restauracion completa del servicio afectado. Es un superset que incluye contencion, erradicacion y recuperacion.

En SLAs contractuales, es critico especificar cual de las dos acepciones se esta usando. Un MTTR de 4 horas para "respond" es agresivo pero alcanzable. Un MTTR de 4 horas para "recover" es, en la mayoria de escenarios, irrealista.

### Otras metricas complementarias

Ademas de las tres principales, un SOC maduro deberia medir:

| Metrica | Definicion | Benchmark |
|---------|-----------|-----------|
| MTTA (Acknowledge) | Tiempo hasta que un analista acepta la alerta | < 15 min (criticos) |
| MTTI (Investigate) | Tiempo de investigacion completa | 1-4 horas |
| False Positive Rate | % de alertas que resultan ser falsos positivos | < 30% (objetivo) |
| Alert Volume | Numero de alertas por dia/semana | Variable por sector |
| Escalation Rate | % de alertas escaladas a N2/N3 | 10-20% |

## Cuales son los benchmarks del sector?

Los benchmarks de la industria son utiles como punto de partida, pero hay que interpretarlos con cuidado. Los numeros que publican IBM, Mandiant o Ponemon representan medias globales que incluyen desde grandes bancos con SOC 24x7 hasta pymes sin equipo de seguridad dedicado.

### Datos clave del IBM Cost of a Data Breach Report 2024

- **MTTD medio global:** 204 dias.
- **MTTR medio global:** 73 dias.
- **Ciclo completo (deteccion + respuesta):** 277 dias de media.
- **Organizaciones con IA y automatizacion:** MTTD de 154 dias (50 dias menos) y ahorro medio de 1,76 millones de USD por brecha.

### Benchmarks por sector

| Sector | MTTD medio | MTTR medio | Notas |
|--------|-----------|-----------|-------|
| Financiero | 168 dias | 51 dias | Regulacion DORA impulsa mejora |
| Sanitario | 231 dias | 92 dias | Mayor coste por brecha (10,93M USD) |
| Administracion publica | 233 dias | 93 dias | ENS obliga a mejorar |
| Retail | 203 dias | 69 dias | Alto volumen de transacciones |
| Tecnologia | 179 dias | 63 dias | Mejor postura general |

### Benchmarks objetivo para un SOC profesional

Los benchmarks globales son utiles para el contexto, pero un SOC que aspire a operar profesionalmente deberia apuntar a objetivos mucho mas agresivos:

| Severidad | MTTD objetivo | MTTA objetivo | MTTC objetivo | MTTR objetivo |
|-----------|--------------|--------------|--------------|--------------|
| Critica (P1) | < 1 hora | < 15 min | < 4 horas | < 24 horas |
| Alta (P2) | < 4 horas | < 30 min | < 8 horas | < 48 horas |
| Media (P3) | < 24 horas | < 2 horas | < 24 horas | < 5 dias |
| Baja (P4) | < 72 horas | < 8 horas | < 48 horas | < 10 dias |

Estos objetivos son alcanzables con un equipo bien dimensionado, herramientas modernas (SIEM + SOAR + threat intelligence) y procesos de triage automatizados. Para un SOC que empieza, puede ser razonable definir un roadmap de 12-18 meses para llegar a estos numeros.

{{< cta type="tofu" text="Riskitera automatiza el triage, la correlacion y el reporting de tu SOC con IA soberana." label="Ver demo SOC" >}}

## Como definir SLAs realistas para tu SOC?

Definir SLAs que sean a la vez ambiciosos y alcanzables requiere un enfoque metodico. No se trata de copiar los numeros de un benchmark y pegarlos en un contrato: se trata de entender la realidad operativa de tu organizacion y construir desde ahi.

### Paso 1: Establecer la linea base

Antes de definir objetivos, hay que medir donde estas. Durante 30-60 dias, registra:

- Tiempo real de deteccion para cada incidente.
- Tiempo de respuesta por nivel de severidad.
- Volumen de alertas y tasa de falsos positivos.
- Ratio de escalado N1 a N2 y N2 a N3.

Si no tienes historico, no inventes numeros. Es mejor arrancar con SLAs conservadores y ajustar que prometer tiempos que no puedes cumplir.

### Paso 2: Clasificar por severidad y tipo de activo

No todos los incidentes merecen el mismo SLA. Un intento de phishing generico no requiere la misma urgencia que un movimiento lateral detectado en el directorio activo. La clasificacion deberia considerar:

- **Severidad del incidente:** Critica, alta, media, baja (alineada con la taxonomia de [INCIBE](https://www.incibe.es/) o tu framework de referencia).
- **Tipo de activo afectado:** Sistemas criticos de negocio, datos regulados (PII, financieros), sistemas de soporte, entornos de desarrollo.
- **Impacto potencial:** Perdida de datos, interrupcion de servicio, impacto regulatorio, dano reputacional.

### Paso 3: Alinear con requisitos regulatorios

En Espana y la Union Europea, los SLAs internos deben ser compatibles con las obligaciones legales:

- **ENS (nivel alto):** Notificacion al [CCN-CERT](https://www.ccn-cert.cni.es/) en menos de 24 horas para incidentes de nivel alto o critico. Esto implica que el MTTD + MTTA debe ser inferior a 20 horas para dejar margen.
- **NIS2:** Alerta temprana en 24 horas, notificacion completa en 72 horas, informe final en un mes. Aplica a operadores esenciales e importantes.
- **[DORA](https://eur-lex.europa.eu/eli/reg/2022/2554):** Para entidades financieras, notificacion inicial de incidentes TIC graves en 4 horas. Un SLA de MTTD de 8 horas seria incompatible con este requisito.

### Paso 4: Definir la estructura del SLA

Un SLA de ciberseguridad bien estructurado deberia incluir como minimo:

1. **Alcance del servicio:** Que sistemas y redes estan cubiertos.
2. **Horario de cobertura:** 24x7, 8x5, horas extendidas.
3. **Tiempos de respuesta por severidad:** Tabla con MTTD, MTTA, MTTC, MTTR para cada nivel.
4. **Procedimientos de escalado:** Quien escala, cuando y a quien.
5. **Mecanismos de medicion:** Como se calculan las metricas, que herramientas se usan, quien audita.
6. **Penalizaciones por incumplimiento:** Creditos, descuentos o clausulas de salida.
7. **Exclusiones:** Que situaciones no estan cubiertas (fuerza mayor, cambios no notificados, etc.).
8. **Proceso de revision:** Frecuencia de revision y ajuste de los SLAs (trimestral recomendado).

### Paso 5: Negociar con el MSSP (si aplica)

Si contratas un proveedor de servicios de seguridad gestionados, ten en cuenta estas recomendaciones:

- **Exige metricas verificables.** No aceptes un SLA que se mida con las herramientas del propio proveedor sin capacidad de auditoria independiente.
- **Define claramente el inicio del cronometro.** El MTTR empieza cuando se detecta, no cuando el cliente notifica.
- **Incluye clausulas de mejora continua.** Los SLAs del primer ano deben ser mas laxos que los del tercero.
- **Negocia creditos reales.** Un 5% de descuento en la factura mensual por incumplimiento no es una penalizacion seria si el incumplimiento genero un incidente de 500.000 euros.

## Como medir y reportar SLAs de seguridad?

Medir SLAs no es simplemente hacer un calculo de tiempo. Requiere infraestructura, procesos y disciplina.

### Infraestructura de medicion

Para medir SLAs de forma fiable necesitas:

1. **Ticketing con timestamps automaticos.** Cada cambio de estado de un incidente debe generar un timestamp automatico. Herramientas como ServiceNow, Jira Service Management o TheHive lo soportan de forma nativa.

2. **SIEM con capacidad de reporting.** Tu SIEM debe poder exportar los tiempos de deteccion de cada alerta, correlacionados con el ticket del incidente correspondiente. Si usas [Wazuh, Splunk o Elastic](/es/posts/2026/04/que-es-un-siem-para-que-sirve/), todos ofrecen esta funcionalidad.

3. **Dashboard de metricas en tiempo real.** Un panel centralizado que muestre las metricas clave actualizadas en tiempo real o near-real-time. Grafana con fuentes de datos del SIEM y el ticketing es una opcion excelente.

4. **Log de evidencias para auditoria.** Cada incidente debe tener un trail de auditoria completo: quien detecto, cuando escalo, que acciones se tomaron y en que tiempos.

### Calculo correcto de las metricas

El calculo de MTTD y MTTR parece trivial, pero tiene trampas:

**MTTD = Suma de tiempos de deteccion / Numero de incidentes detectados**

La trampa: los incidentes que nunca se detectan no entran en el calculo. Un SOC con un MTTD excelente pero que solo detecta el 40% de los incidentes tiene un problema mucho mas grave que uno con un MTTD mediocre pero que detecta el 90%.

Por eso, el MTTD siempre debe acompanarse de la tasa de deteccion (Detection Rate), idealmente validada con ejercicios de red team o purple team periodicos.

**MTTR = Suma de tiempos de respuesta / Numero de incidentes resueltos**

La trampa: definir "resuelto". Un incidente de ransomware puede considerarse "contenido" (servidores aislados) en 2 horas pero "resuelto" (sistemas restaurados y operativos) en 5 dias. El SLA debe especificar que hito marca el final del MTTR.

### Frecuencia de reporting

La frecuencia del reporting de SLAs depende de la audiencia:

| Audiencia | Frecuencia | Contenido |
|-----------|-----------|-----------|
| Equipo SOC | Diario | Dashboard operativo, alertas abiertas, SLAs en riesgo |
| CISO / Security Management | Semanal | Metricas agregadas, tendencias, incumplimientos |
| Direccion / Comite de seguridad | Mensual | Resumen ejecutivo, comparativa con benchmarks, ROI |
| Auditores | Bajo demanda | Evidencias completas, trazabilidad, historial de mejora |

### Automatizacion del reporting

El reporting manual es insostenible y propenso a errores. Las organizaciones maduras automatizan:

- **Generacion automatica de dashboards** con datos en tiempo real del SIEM y el ticketing.
- **Alertas proactivas** cuando un SLA esta en riesgo de incumplimiento (por ejemplo, un P1 que lleva 3 horas sin contenerse cuando el SLA es de 4 horas).
- **Informes mensuales automatizados** que se generan y distribuyen sin intervencion manual.

## Como presentar SLAs en una auditoria?

Las auditorias de seguridad (ya sean internas, de terceros o regulatorias bajo el ENS) examinan los SLAs desde tres angulos: definicion, medicion y cumplimiento.

### Lo que el auditor busca

1. **Formalizacion.** Que los SLAs esten documentados, aprobados por la direccion y comunicados a todos los implicados. Un SLA verbal no existe para un auditor.

2. **Coherencia con el marco regulatorio.** Si operas bajo el ENS nivel alto, tus SLAs de notificacion deben ser compatibles con los plazos del CCN-CERT. Si aplica NIS2, los plazos de 24/72 horas deben estar reflejados.

3. **Evidencia de medicion.** No basta con tener un documento que diga "MTTR < 4 horas". El auditor pedira evidencia de que mides esa metrica, como la mides y cuales son los resultados reales.

4. **Historial de cumplimiento.** Un SLA que se incumple sistematicamente sin plan de mejora es peor que no tener SLA. El auditor espera ver un porcentaje de cumplimiento (idealmente > 95%) y acciones correctivas cuando se incumple.

5. **Plan de mejora continua.** Los SLAs deben revisarse periodicamente y ajustarse en funcion de los resultados. Un auditor mira con buenos ojos un historico que muestre mejora progresiva.

### Estructura recomendada para la presentacion

Cuando te sientes con un auditor, presenta los SLAs con esta estructura:

1. **Contexto organizativo.** Tamano del equipo, herramientas, cobertura horaria, tipos de activos protegidos.
2. **Definicion de los SLAs.** Tabla clara con metricas, objetivos por severidad y alcance.
3. **Metodologia de medicion.** Herramientas, automatizaciones, fuentes de datos.
4. **Resultados del periodo.** Metricas reales vs. objetivos, porcentaje de cumplimiento, tendencias.
5. **Incumplimientos y acciones correctivas.** No escondas los fallos: presenta que paso, por que y que se hizo para evitar que se repita.
6. **Plan de mejora.** Objetivos para el proximo periodo, inversiones previstas, cambios de proceso planificados.

### Errores frecuentes en auditoria

- **Presentar metricas sin contexto.** Un MTTR de 2 horas impresiona hasta que el auditor descubre que solo cuentas los incidentes P1 y excluyes los P2-P4.
- **No tener evidencia.** Decir "medimos el MTTD con el SIEM" sin poder mostrar un dashboard o un informe generado automaticamente.
- **SLAs desactualizados.** Presentar SLAs definidos hace tres anos que no reflejan la realidad actual del SOC.
- **Confundir metricas.** Presentar el MTTR como tiempo de respuesta cuando en realidad mides tiempo de recuperacion (o viceversa).

## Que pasa cuando se incumplen los SLAs?

El incumplimiento de SLAs tiene consecuencias en tres dimensiones: contractual, operativa y regulatoria.

### Consecuencias contractuales (con MSSPs)

Los contratos con proveedores de seguridad gestionados suelen incluir:

- **Service Credits.** Descuentos en la facturacion proporcionales al incumplimiento. Tipicamente entre el 5% y el 25% de la factura mensual.
- **Clausulas de terminacion anticipada.** Incumplimientos reiterados (por ejemplo, mas de 3 meses consecutivos) pueden dar derecho a rescindir el contrato sin penalizacion.
- **Obligaciones de remediacion.** El proveedor puede estar obligado a presentar un plan de mejora con plazos concretos y a absorber los costes de la remediacion.

### Consecuencias operativas

Un SLA incumplido es un sintoma. Las causas raiz tipicas son:

- **Subdimensionamiento del equipo.** Pocos analistas para el volumen de alertas.
- **Herramientas inadecuadas.** SIEM sin reglas de correlacion actualizadas, SOAR sin playbooks maduros.
- **Procesos deficientes.** Falta de runbooks, escalado confuso, handoff entre turnos deficiente.
- **Fatiga de alertas.** Demasiados falsos positivos generan que los analistas ignoren o depriorizan alertas legitimas.

La accion correctiva no deberia ser simplemente "relajar el SLA" sino diagnosticar y atacar la causa raiz. Si el equipo N1 tiene un MTTA de 45 minutos cuando el SLA es de 15, quizas la solucion no es subir el SLA a 45 sino automatizar el triage para que el analista reciba alertas pre-priorizadas y enriquecidas.

### Consecuencias regulatorias

En el contexto del ENS y NIS2, el incumplimiento de los plazos de notificacion puede acarrear:

- **ENS:** Observaciones en auditorias de conformidad, planes de adecuacion obligatorios y, en casos graves, suspension de la certificacion.
- **NIS2:** Multas de hasta 10 millones de euros o el 2% de la facturacion global (lo que sea mayor) para entidades esenciales. Para entidades importantes, hasta 7 millones o el 1,4% de la facturacion.
- **DORA:** Para entidades financieras, las sanciones pueden incluir multas significativas y requerimientos de las autoridades supervisoras.

El marco de referencia [NIST SP 800-61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) proporciona directrices detalladas sobre gestion de incidentes que pueden servir como base para disenar procesos que cumplan con todos estos requisitos regulatorios.

## Automatizacion de SLAs: el factor diferencial

La diferencia entre un SOC que cumple sus SLAs de forma consistente y uno que lucha cada dia para no incumplirlos suele estar en el nivel de automatizacion.

### Que automatizar para mejorar el MTTD

- **Ingestion y normalizacion de logs.** Cuanto mas rapido lleguen los logs al SIEM y se normalicen, antes se puede detectar. Pipelines de ingestion optimizados con parsers pre-configurados para las fuentes mas criticas.
- **Reglas de correlacion continuamente actualizadas.** Reglas SIGMA actualizadas semanalmente con feeds de threat intelligence.
- **Deteccion basada en comportamiento (UEBA).** Complementar la deteccion basada en firmas con analisis de comportamiento que detecte anomalias sin necesidad de reglas especificas.

### Que automatizar para mejorar el MTTR

- **Triage automatico.** Enriquecer cada alerta automaticamente con contexto (reputacion de IP, hash del fichero, historial del usuario) antes de que llegue al analista.
- **Playbooks de respuesta.** Automatizar las acciones de contencion inmediata para escenarios conocidos: bloqueo de IP, aislamiento de host, desactivacion de cuenta.
- **Orquestacion de herramientas.** Conectar SIEM, EDR, firewall, ticketing y CMDB para que las acciones de respuesta se ejecuten de forma coordinada sin intervenciones manuales.

La automatizacion no sustituye al analista humano. Lo que hace es eliminar la friccion operativa para que el analista pueda dedicar su tiempo a lo que realmente importa: investigar amenazas complejas y tomar decisiones criticas. Para profundizar en la relacion entre SIEM, SOAR y automatizacion, puedes leer nuestro articulo sobre [SOAR vs SIEM](/es/posts/2026/06/soar-vs-siem-diferencias/).

{{< cta type="bofu" text="Solicita una demo personalizada para tu SOC y descubre como Riskitera optimiza tus operaciones." label="Solicitar demo" >}}


**Articulos relacionados:**
- [Como Montar Soc Desde Cero](/es/posts/2026/04/como-montar-soc-desde-cero/)
- [Auditoria Seguridad Informatica Guia](/es/posts/2026/04/auditoria-seguridad-informatica-guia/)

## Preguntas frecuentes

### Cual es la diferencia entre MTTR y MTTC?

El MTTC (Mean Time To Contain) mide el tiempo desde la confirmacion de un incidente hasta que se contiene su propagacion (aislamiento de sistemas, bloqueo de cuentas). El MTTR (Mean Time To Respond/Recover) es mas amplio y abarca desde la deteccion hasta la restauracion completa del servicio afectado. Un incidente puede estar contenido en 30 minutos pero no completamente resuelto hasta 3 dias despues. En los SLAs es fundamental especificar cual de las dos metricas se esta utilizando para evitar malentendidos, especialmente en contratos con proveedores MSSP.

### Que SLAs de ciberseguridad exige el ENS?

El ENS no define SLAs especificos como "MTTD < X horas". Lo que establece son obligaciones de notificacion (al CCN-CERT en menos de 24 horas para incidentes de nivel alto o critico) y requisitos de capacidad de respuesta proporcionales al nivel de seguridad (basico, medio, alto). Estas obligaciones se traducen indirectamente en SLAs internos: si tienes que notificar en 24 horas, tu MTTD + tiempo de validacion debe ser inferior a ese plazo. Para entidades bajo NIS2, los plazos son aun mas estrictos con alertas tempranas en 24 horas y notificacion completa en 72 horas.

### Como reduzco el MTTD de mi SOC sin contratar mas analistas?

La forma mas efectiva de reducir el MTTD sin aumentar plantilla es invertir en automatizacion: reglas de correlacion afinadas en el SIEM para reducir falsos positivos, feeds de threat intelligence automatizados que actualicen IOCs en tiempo real, y deteccion basada en comportamiento (UEBA) que identifique anomalias sin depender de firmas. La reduccion de falsos positivos es clave porque permite que los analistas existentes se centren en las alertas que realmente importan. Organizaciones que implementan estas medidas reportan reducciones del MTTD del 40-60%.

### Que penalizaciones debo incluir en el contrato con mi MSSP?

Las penalizaciones deben ser proporcionales al impacto del incumplimiento. Un esquema tipico incluye: service credits del 10-25% de la factura mensual por incumplimiento sostenido de SLAs criticos, derecho a auditoria independiente de las metricas del proveedor, obligacion de presentar plan de mejora en 30 dias tras un incumplimiento, y clausula de terminacion anticipada sin penalizacion tras 3 meses consecutivos de incumplimiento. Evita penalizaciones puramente simbolicas (como un 2% de descuento) que no incentivan realmente al proveedor a mejorar.

### Con que frecuencia debo revisar los SLAs de mi SOC?

La revision formal deberia ser trimestral como minimo, con una revision anual mas profunda. En la revision trimestral se analizan las metricas de cumplimiento, se identifican tendencias y se ajustan los objetivos si es necesario. En la revision anual se reevalua la estructura completa de los SLAs en funcion de cambios en la organizacion (nuevos sistemas, cambios regulatorios, lecciones aprendidas de incidentes). Ademas, cualquier incidente significativo deberia disparar una revision ad hoc de los SLAs afectados para determinar si los objetivos eran realistas y si los procesos son adecuados.