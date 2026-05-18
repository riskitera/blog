---
title: "SLAs en ciberseguridad: cómo definir MTTR, MTTD y no morir en la auditoría"
description: "Guía práctica para definir SLAs de ciberseguridad: MTTR, MTTD, MTTC, benchmarks del sector, cómo medirlos y cómo presentarlos en auditorías de seguridad."
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

Guía práctica para definir SLAs de ciberseguridad: MTTR, MTTD, MTTC, benchmarks del sector, cómo medirlos y cómo presentarlos en auditorías de seguridad.

<!--more-->

{{< key-takeaways >}}
- MTTR, MTTD y MTTC son las tres métricas fundamentales que cualquier SOC debe medir para demostrar eficacia operativa.
- Los benchmarks del sector sitúan el MTTD medio en 204 días y el MTTR en 73 días, cifras que cualquier organización seria debería mejorar significativamente.
- Los SLAs contractuales con MSSPs deben incluir penalizaciones concretas y mecanismos de verificación independiente.
- El ENS y la directiva NIS2 exigen tiempos de notificación y respuesta que condicionan directamente los SLAs internos.
- La automatización del triage y la correlación de alertas puede reducir el MTTD en un 60-80% respecto a procesos manuales.
{{< /key-takeaways >}}

## ¿Qué son los SLAs en ciberseguridad?

Un SLA (Service Level Agreement) en ciberseguridad es un compromiso formal, medible y contractualmente vinculante, que define los niveles mínimos de servicio que un equipo de seguridad (interno o externo) debe cumplir. No se trata de un documento decorativo para la carpeta de compliance: es la columna vertebral operativa de cualquier SOC que pretenda funcionar de forma profesional.

En el contexto de un centro de operaciones de seguridad, los SLAs definen aspectos como el tiempo máximo para detectar una amenaza, el tiempo máximo para contenerla, la frecuencia de reporting, la disponibilidad del servicio (24x7 o en franjas horarias) y los procedimientos de escalado. Son, en esencia, la traducción cuantitativa de lo que la organización espera de su capacidad defensiva.

La importancia de los SLAs va mucho más allá de la relación con un proveedor MSSP. Incluso cuando el SOC es 100% interno, definir SLAs claros permite tres cosas fundamentales:

1. **Medir la mejora continua.** Sin métricas base, es imposible saber si las inversiones en herramientas, personal o procesos están dando resultado.
2. **Rendir cuentas ante la dirección.** Un CISO que presenta métricas concretas (tiempo medio de detección reducido un 40% en seis meses) tiene mucho más impacto que uno que habla de "mejora general".
3. **Cumplir con marcos regulatorios.** Tanto el [Esquema Nacional de Seguridad (ENS)](https://www.boe.es/eli/es/rd/2022/05/03/311) como la [Directiva NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555) establecen requisitos de notificación y respuesta que solo se pueden garantizar con SLAs bien definidos.

En España, el contexto regulatorio hace que los SLAs de ciberseguridad no sean opcionales para la administración pública ni para operadores de servicios esenciales. Son un requisito legal.

## ¿Qué significan MTTR, MTTD y MTTC?

Las tres métricas fundamentales que vertebran los SLAs de cualquier SOC son MTTD, MTTC y MTTR. Vamos a desgranarlas una por una, porque confundirlas (algo habitual) puede llevar a SLAs que no reflejan la realidad operativa.

### MTTD: Mean Time To Detect

El MTTD mide el tiempo medio que transcurre desde que una amenaza o incidente se produce hasta que el SOC lo detecta. Es, probablemente, la métrica más crítica porque lo que no se detecta no se puede contener.

**¿Qué incluye el MTTD?**
- Tiempo desde el compromiso inicial hasta que una regla de correlación, un analista o un feed de threat intelligence genera una alerta.
- Incluye el tiempo de ingestion de logs, procesamiento por el SIEM y generación de la alerta.

**¿Qué NO incluye?**
- El tiempo de validación (eso es parte del triage).
- El tiempo de respuesta (eso es MTTR).

**Ejemplo práctico:** Un atacante compromete credenciales de un empleado el lunes a las 09:00. El SIEM detecta un patrón anómalo de acceso el miércoles a las 15:00. El MTTD es de 54 horas.

### MTTC: Mean Time To Contain

El MTTC mide el tiempo desde que se confirma un incidente hasta que se contiene su propagación. Es la métrica que más directamente impacta en la reducción de daño.

**¿Qué incluye el MTTC?**
- Aislamiento del sistema comprometido.
- Bloqueo de cuentas afectadas.
- Aplicación de reglas de firewall de emergencia.
- Desactivación de servicios comprometidos.

**Ejemplo práctico:** Se confirma un ransomware a las 10:00. A las 10:45 se han aislado los tres servidores afectados y bloqueado la cuenta comprometida. MTTC: 45 minutos.

### MTTR: Mean Time To Respond (o Recover)

El MTTR tiene dos acepciones comunes: Mean Time To Respond y Mean Time To Recover. En ciberseguridad, la distinción importa:

- **MTTR (Respond):** Tiempo desde la detección hasta que se inicia la primera acción de respuesta. Cubre la fase de triage y escalado.
- **MTTR (Recover):** Tiempo desde la detección hasta la restauración completa del servicio afectado. Es un superset que incluye contención, erradicación y recuperación.

En SLAs contractuales, es crítico especificar cuál de las dos acepciones se está usando. Un MTTR de 4 horas para "respond" es agresivo pero alcanzable. Un MTTR de 4 horas para "recover" es, en la mayoría de escenarios, irrealista.

### Otras métricas complementarias

Además de las tres principales, un SOC maduro debería medir:

| Métrica | Definición | Benchmark |
|---------|-----------|-----------|
| MTTA (Acknowledge) | Tiempo hasta que un analista acepta la alerta | < 15 min (críticos) |
| MTTI (Investigate) | Tiempo de investigación completa | 1-4 horas |
| False Positive Rate | % de alertas que resultan ser falsos positivos | < 30% (objetivo) |
| Alert Volume | Número de alertas por día/semana | Variable por sector |
| Escalation Rate | % de alertas escaladas a N2/N3 | 10-20% |

## ¿Cuáles son los benchmarks del sector?

Los benchmarks de la industria son útiles como punto de partida, pero hay que interpretarlos con cuidado. Los números que publican IBM, Mandiant o Ponemon representan medias globales que incluyen desde grandes bancos con SOC 24x7 hasta pymes sin equipo de seguridad dedicado.

### Datos clave del IBM Cost of a Data Breach Report 2024

- **MTTD medio global:** 204 días.
- **MTTR medio global:** 73 días.
- **Ciclo completo (detección + respuesta):** 277 días de media.
- **Organizaciones con IA y automatización:** MTTD de 154 días (50 días menos) y ahorro medio de 1,76 millones de USD por brecha.

### Benchmarks por sector

| Sector | MTTD medio | MTTR medio | Notas |
|--------|-----------|-----------|-------|
| Financiero | 168 días | 51 días | Regulación DORA impulsa mejora |
| Sanitario | 231 días | 92 días | Mayor coste por brecha (10,93M USD) |
| Administración pública | 233 días | 93 días | ENS obliga a mejorar |
| Retail | 203 días | 69 días | Alto volumen de transacciones |
| Tecnología | 179 días | 63 días | Mejor postura general |

### Benchmarks objetivo para un SOC profesional

Los benchmarks globales son útiles para el contexto, pero un SOC que aspire a operar profesionalmente debería apuntar a objetivos mucho más agresivos:

| Severidad | MTTD objetivo | MTTA objetivo | MTTC objetivo | MTTR objetivo |
|-----------|--------------|--------------|--------------|--------------|
| Crítica (P1) | < 1 hora | < 15 min | < 4 horas | < 24 horas |
| Alta (P2) | < 4 horas | < 30 min | < 8 horas | < 48 horas |
| Media (P3) | < 24 horas | < 2 horas | < 24 horas | < 5 días |
| Baja (P4) | < 72 horas | < 8 horas | < 48 horas | < 10 días |

Estos objetivos son alcanzables con un equipo bien dimensionado, herramientas modernas (SIEM + SOAR + threat intelligence) y procesos de triage automatizados. Para un SOC que empieza, puede ser razonable definir un roadmap de 12-18 meses para llegar a estos números.

{{< cta type="tofu" text="Riskitera automatiza el triage, la correlación y el reporting de tu SOC con IA soberana." label="Ver demo SOC" >}}

## ¿Cómo definir SLAs realistas para tu SOC?

Definir SLAs que sean a la vez ambiciosos y alcanzables requiere un enfoque metódico. No se trata de copiar los números de un benchmark y pegarlos en un contrato: se trata de entender la realidad operativa de tu organización y construir desde ahí.

### Paso 1: Establecer la línea base

Antes de definir objetivos, hay que medir dónde estás. Durante 30-60 días, registra:

- Tiempo real de detección para cada incidente.
- Tiempo de respuesta por nivel de severidad.
- Volumen de alertas y tasa de falsos positivos.
- Ratio de escalado N1 a N2 y N2 a N3.

Si no tienes histórico, no inventes números. Es mejor arrancar con SLAs conservadores y ajustar que prometer tiempos que no puedes cumplir.

### Paso 2: Clasificar por severidad y tipo de activo

No todos los incidentes merecen el mismo SLA. Un intento de phishing genérico no requiere la misma urgencia que un movimiento lateral detectado en el directorio activo. La clasificación debería considerar:

- **Severidad del incidente:** Crítica, alta, media, baja (alineada con la taxonomía de [INCIBE](https://www.incibe.es/) o tu framework de referencia).
- **Tipo de activo afectado:** Sistemas críticos de negocio, datos regulados (PII, financieros), sistemas de soporte, entornos de desarrollo.
- **Impacto potencial:** Pérdida de datos, interrupción de servicio, impacto regulatorio, daño reputacional.

### Paso 3: Alinear con requisitos regulatorios

En España y la Unión Europea, los SLAs internos deben ser compatibles con las obligaciones legales:

- **ENS (nivel alto):** Notificación al [CCN-CERT](https://www.ccn-cert.cni.es/) en menos de 24 horas para incidentes de nivel alto o crítico. Esto implica que el MTTD + MTTA debe ser inferior a 20 horas para dejar margen.
- **NIS2:** Alerta temprana en 24 horas, notificación completa en 72 horas, informe final en un mes. Aplica a operadores esenciales e importantes.
- **[DORA](https://eur-lex.europa.eu/eli/reg/2022/2554):** Para entidades financieras, notificación inicial de incidentes TIC graves en 4 horas. Un SLA de MTTD de 8 horas sería incompatible con este requisito.

### Paso 4: Definir la estructura del SLA

Un SLA de ciberseguridad bien estructurado debería incluir como mínimo:

1. **Alcance del servicio:** Qué sistemas y redes están cubiertos.
2. **Horario de cobertura:** 24x7, 8x5, horas extendidas.
3. **Tiempos de respuesta por severidad:** Tabla con MTTD, MTTA, MTTC, MTTR para cada nivel.
4. **Procedimientos de escalado:** Quién escala, cuándo y a quién.
5. **Mecanismos de medición:** Cómo se calculan las métricas, qué herramientas se usan, quién audita.
6. **Penalizaciones por incumplimiento:** Créditos, descuentos o cláusulas de salida.
7. **Exclusiones:** Qué situaciones no están cubiertas (fuerza mayor, cambios no notificados, etc.).
8. **Proceso de revisión:** Frecuencia de revisión y ajuste de los SLAs (trimestral recomendado).

### Paso 5: Negociar con el MSSP (si aplica)

Si contratas un proveedor de servicios de seguridad gestionados, ten en cuenta estas recomendaciones:

- **Exige métricas verificables.** No aceptes un SLA que se mida con las herramientas del propio proveedor sin capacidad de auditoría independiente.
- **Define claramente el inicio del cronometro.** El MTTR empieza cuando se detecta, no cuando el cliente notifica.
- **Incluye cláusulas de mejora continua.** Los SLAs del primer año deben ser más laxos que los del tercero.
- **Negocia créditos reales.** Un 5% de descuento en la factura mensual por incumplimiento no es una penalización seria si el incumplimiento generó un incidente de 500.000 euros.

## ¿Cómo medir y reportar SLAs de seguridad?

Medir SLAs no es simplemente hacer un cálculo de tiempo. Requiere infraestructura, procesos y disciplina.

### Infraestructura de medición

Para medir SLAs de forma fiable necesitas:

1. **Ticketing con timestamps automáticos.** Cada cambio de estado de un incidente debe generar un timestamp automático. Herramientas como ServiceNow, Jira Service Management o TheHive lo soportan de forma nativa.

2. **SIEM con capacidad de reporting.** Tu SIEM debe poder exportar los tiempos de detección de cada alerta, correlacionados con el ticket del incidente correspondiente. Si usas [Wazuh, Splunk o Elastic](/es/posts/2026/04/que-es-un-siem-para-que-sirve/), todos ofrecen esta funcionalidad.

3. **Dashboard de métricas en tiempo real.** Un panel centralizado que muestre las métricas clave actualizadas en tiempo real o near-real-time. Grafana con fuentes de datos del SIEM y el ticketing es una opción excelente.

4. **Log de evidencias para auditoría.** Cada incidente debe tener un trail de auditoría completo: quién detectó, cuándo escaló, qué acciones se tomaron y en qué tiempos.

### Cálculo correcto de las métricas

El cálculo de MTTD y MTTR parece trivial, pero tiene trampas:

**MTTD = Suma de tiempos de detección / Número de incidentes detectados**

La trampa: los incidentes que nunca se detectan no entran en el cálculo. Un SOC con un MTTD excelente pero que solo detecta el 40% de los incidentes tiene un problema mucho más grave que uno con un MTTD mediocre pero que detecta el 90%.

Por eso, el MTTD siempre debe acompañarse de la tasa de detección (Detection Rate), idealmente validada con ejercicios de red team o purple team periódicos.

**MTTR = Suma de tiempos de respuesta / Número de incidentes resueltos**

La trampa: definir "resuelto". Un incidente de ransomware puede considerarse "contenido" (servidores aislados) en 2 horas pero "resuelto" (sistemas restaurados y operativos) en 5 días. El SLA debe especificar qué hito marca el final del MTTR.

### Frecuencia de reporting

La frecuencia del reporting de SLAs depende de la audiencia:

| Audiencia | Frecuencia | Contenido |
|-----------|-----------|-----------|
| Equipo SOC | Diario | Dashboard operativo, alertas abiertas, SLAs en riesgo |
| CISO / Security Management | Semanal | Métricas agregadas, tendencias, incumplimientos |
| Dirección / Comité de seguridad | Mensual | Resumen ejecutivo, comparativa con benchmarks, ROI |
| Auditores | Bajo demanda | Evidencias completas, trazabilidad, historial de mejora |

### Automatización del reporting

El reporting manual es insostenible y propenso a errores. Las organizaciones maduras automatizan:

- **Generación automática de dashboards** con datos en tiempo real del SIEM y el ticketing.
- **Alertas proactivas** cuando un SLA está en riesgo de incumplimiento (por ejemplo, un P1 que lleva 3 horas sin contenerse cuando el SLA es de 4 horas).
- **Informes mensuales automatizados** que se generan y distribuyen sin intervención manual.

## ¿Cómo presentar SLAs en una auditoría?

Las auditorías de seguridad (ya sean internas, de terceros o regulatorias bajo el ENS) examinan los SLAs desde tres angulos: definición, medición y cumplimiento.

### Lo que el auditor busca

1. **Formalización.** Que los SLAs estén documentados, aprobados por la dirección y comunicados a todos los implicados. Un SLA verbal no existe para un auditor.

2. **Coherencia con el marco regulatorio.** Si operas bajo el ENS nivel alto, tus SLAs de notificación deben ser compatibles con los plazos del CCN-CERT. Si aplica NIS2, los plazos de 24/72 horas deben estar reflejados.

3. **Evidencia de medición.** No basta con tener un documento que diga "MTTR < 4 horas". El auditor pedirá evidencia de que mides esa métrica, cómo la mides y cuáles son los resultados reales.

4. **Historial de cumplimiento.** Un SLA que se incumple sistemáticamente sin plan de mejora es peor que no tener SLA. El auditor espera ver un porcentaje de cumplimiento (idealmente > 95%) y acciones correctivas cuando se incumple.

5. **Plan de mejora continua.** Los SLAs deben revisarse periódicamente y ajustarse en función de los resultados. Un auditor mira con buenos ojos un histórico que muestre mejora progresiva.

### Estructura recomendada para la presentación

Cuando te sientes con un auditor, presenta los SLAs con esta estructura:

1. **Contexto organizativo.** Tamaño del equipo, herramientas, cobertura horaria, tipos de activos protegidos.
2. **Definición de los SLAs.** Tabla clara con métricas, objetivos por severidad y alcance.
3. **Metodología de medición.** Herramientas, automatizaciones, fuentes de datos.
4. **Resultados del periodo.** Métricas reales vs. objetivos, porcentaje de cumplimiento, tendencias.
5. **Incumplimientos y acciones correctivas.** No escondas los fallos: presenta qué pasó, por qué y qué se hizo para evitar que se repita.
6. **Plan de mejora.** Objetivos para el próximo periodo, inversiones previstas, cambios de proceso planificados.

### Errores frecuentes en auditoría

- **Presentar métricas sin contexto.** Un MTTR de 2 horas impresiona hasta que el auditor descubre que solo cuentas los incidentes P1 y excluyes los P2-P4.
- **No tener evidencia.** Decir "medimos el MTTD con el SIEM" sin poder mostrar un dashboard o un informe generado automáticamente.
- **SLAs desactualizados.** Presentar SLAs definidos hace tres años que no reflejan la realidad actual del SOC.
- **Confundir métricas.** Presentar el MTTR como tiempo de respuesta cuando en realidad mides tiempo de recuperación (o viceversa).

## ¿Qué pasa cuando se incumplen los SLAs?

El incumplimiento de SLAs tiene consecuencias en tres dimensiones: contractual, operativa y regulatoria.

### Consecuencias contractuales (con MSSPs)

Los contratos con proveedores de seguridad gestionados suelen incluir:

- **Service Credits.** Descuentos en la facturación proporcionales al incumplimiento. Tipicamente entre el 5% y el 25% de la factura mensual.
- **Clausulas de terminación anticipada.** Incumplimientos reiterados (por ejemplo, más de 3 meses consecutivos) pueden dar derecho a rescindir el contrato sin penalización.
- **Obligaciones de remediación.** El proveedor puede estar obligado a presentar un plan de mejora con plazos concretos y a absorber los costes de la remediación.

### Consecuencias operativas

Un SLA incumplido es un síntoma. Las causas raíz típicas son:

- **Subdimensionamiento del equipo.** Pocos analistas para el volumen de alertas.
- **Herramientas inadecuadas.** SIEM sin reglas de correlación actualizadas, SOAR sin playbooks maduros.
- **Procesos deficientes.** Falta de runbooks, escalado confuso, handoff entre turnos deficiente.
- **Fatiga de alertas.** Demasiados falsos positivos generan que los analistas ignoren o depriorizan alertas legítimas.

La acción correctiva no debería ser simplemente "relajar el SLA" sino diagnosticar y atacar la causa raíz. Si el equipo N1 tiene un MTTA de 45 minutos cuando el SLA es de 15, quizás la solución no es subir el SLA a 45 sino automatizar el triage para que el analista reciba alertas pre-priorizadas y enriquecidas.

### Consecuencias regulatorias

En el contexto del ENS y NIS2, el incumplimiento de los plazos de notificación puede acarrear:

- **ENS:** Observaciones en auditorías de conformidad, planes de adecuación obligatorios y, en casos graves, suspensión de la certificación.
- **NIS2:** Multas de hasta 10 millones de euros o el 2% de la facturación global (lo que sea mayor) para entidades esenciales. Para entidades importantes, hasta 7 millones o el 1,4% de la facturación.
- **DORA:** Para entidades financieras, las sanciones pueden incluir multas significativas y requerimientos de las autoridades supervisoras.

El marco de referencia [NIST SP 800-61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) proporciona directrices detalladas sobre gestión de incidentes que pueden servir como base para diseñar procesos que cumplan con todos estos requisitos regulatorios.

## Automatización de SLAs: el factor diferencial

La diferencia entre un SOC que cumple sus SLAs de forma consistente y uno que lucha cada día para no incumplirlos suele estar en el nivel de automatización.

### ¿Qué automatizar para mejorar el MTTD?

- **Ingestion y normalización de logs.** Cuanto más rápido lleguen los logs al SIEM y se normalicen, antes se puede detectar. Pipelines de ingestion optimizados con parsers pre-configurados para las fuentes más críticas.
- **Reglas de correlación continuamente actualizadas.** Reglas SIGMA actualizadas semanalmente con feeds de threat intelligence.
- **Detección basada en comportamiento (UEBA).** Complementar la detección basada en firmas con análisis de comportamiento que detecte anomalías sin necesidad de reglas específicas.

### ¿Qué automatizar para mejorar el MTTR?

- **Triage automático.** Enriquecer cada alerta automáticamente con contexto (reputación de IP, hash del fichero, historial del usuario) antes de que llegue al analista.
- **Playbooks de respuesta.** Automatizar las acciones de contención inmediata para escenarios conocidos: bloqueo de IP, aislamiento de host, desactivación de cuenta.
- **Orquestación de herramientas.** Conectar SIEM, EDR, firewall, ticketing y CMDB para que las acciones de respuesta se ejecuten de forma coordinada sin intervenciones manuales.

La automatización no sustituye al analista humano. Lo que hace es eliminar la fricción operativa para que el analista pueda dedicar su tiempo a lo que realmente importa: investigar amenazas complejas y tomar decisiones críticas. Para profundizar en la relación entre SIEM, SOAR y automatización, puedes leer nuestro artículo sobre [SOAR vs SIEM](/es/posts/2026/06/soar-vs-siem-diferencias/).

{{< cta type="bofu" text="Solicita una demo personalizada para tu SOC y descubre cómo Riskitera optimiza tus operaciones." label="Solicitar demo" >}}


**Artículos relacionados:**
- [Cómo Montar Soc Desde Cero](/es/posts/2026/04/como-montar-soc-desde-cero/)
- [Auditoría Seguridad Informatica Guia](/es/posts/2026/04/auditoria-seguridad-informatica-guia/)

## Preguntas frecuentes

### ¿Cuál es la diferencia entre MTTR y MTTC?

El MTTC (Mean Time To Contain) mide el tiempo desde la confirmación de un incidente hasta que se contiene su propagación (aislamiento de sistemas, bloqueo de cuentas). El MTTR (Mean Time To Respond/Recover) es más amplio y abarca desde la detección hasta la restauración completa del servicio afectado. Un incidente puede estar contenido en 30 minutos pero no completamente resuelto hasta 3 días después. En los SLAs es fundamental especificar cuál de las dos métricas se está utilizando para evitar malentendidos, especialmente en contratos con proveedores MSSP.

### ¿Qué SLAs de ciberseguridad exige el ENS?

El ENS no define SLAs específicos como "MTTD < X horas". Lo que establece son obligaciones de notificación (al CCN-CERT en menos de 24 horas para incidentes de nivel alto o crítico) y requisitos de capacidad de respuesta proporcionales al nivel de seguridad (básico, medio, alto). Estas obligaciones se traducen indirectamente en SLAs internos: si tienes que notificar en 24 horas, tu MTTD + tiempo de validación debe ser inferior a ese plazo. Para entidades bajo NIS2, los plazos son aún más estrictos con alertas tempranas en 24 horas y notificación completa en 72 horas.

### ¿Cómo reduzco el MTTD de mi SOC sin contratar más analistas?

La forma más efectiva de reducir el MTTD sin aumentar plantilla es invertir en automatización: reglas de correlación afinadas en el SIEM para reducir falsos positivos, feeds de threat intelligence automatizados que actualicen IOCs en tiempo real, y detección basada en comportamiento (UEBA) que identifique anomalías sin depender de firmas. La reducción de falsos positivos es clave porque permite que los analistas existentes se centren en las alertas que realmente importan. Organizaciones que implementan estas medidas reportan reducciones del MTTD del 40-60%.

### ¿Qué penalizaciones debo incluir en el contrato con mi MSSP?

Las penalizaciones deben ser proporcionales al impacto del incumplimiento. Un esquema típico incluye: service credits del 10-25% de la factura mensual por incumplimiento sostenido de SLAs críticos, derecho a auditoría independiente de las métricas del proveedor, obligación de presentar plan de mejora en 30 días tras un incumplimiento, y cláusula de terminación anticipada sin penalización tras 3 meses consecutivos de incumplimiento. Evita penalizaciones puramente simbolicas (como un 2% de descuento) que no incentivan realmente al proveedor a mejorar.

### ¿Con qué frecuencia debo revisar los SLAs de mi SOC?

La revisión formal debería ser trimestral como mínimo, con una revisión anual más profunda. En la revisión trimestral se analizan las métricas de cumplimiento, se identifican tendencias y se ajustan los objetivos si es necesario. En la revisión anual se reevalúa la estructura completa de los SLAs en función de cambios en la organización (nuevos sistemas, cambios regulatorios, lecciones aprendidas de incidentes). Además, cualquier incidente significativo debería disparar una revisión ad hoc de los SLAs afectados para determinar si los objetivos eran realistas y si los procesos son adecuados.