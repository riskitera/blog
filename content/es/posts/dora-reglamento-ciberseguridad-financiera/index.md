---
title: "DORA: el reglamento que cambia la ciberseguridad financiera"
image: "cover.png"
description: "Guía completa sobre el Reglamento DORA: qué es, a quién afecta, los cinco pilares de resiliencia operativa digital, plazos, sanciones y cómo prepararse para."
slug: "dora-reglamento-ciberseguridad-financiera"
date: 2026-03-10
lastmod: 2026-03-10
draft: false
tags: ["DORA", "Fintech", "Compliance", "Banca"]
categories: ["Compliance"]
author: "David Moya"
translationKey: "dora-guide"
---

El Reglamento DORA (Digital Operational Resilience Act) es la normativa europea que establece un marco uniforme de resiliencia operativa digital para el sector financiero. A diferencia de las directivas, DORA es un reglamento de aplicación directa en todos los Estados miembros de la UE desde el 17 de enero de 2025, sin necesidad de transposición nacional. Afecta a más de 22.000 entidades financieras y proveedores de servicios TIC en Europa, y su incumplimiento conlleva sanciones que pueden alcanzar el 1 por ciento del volumen de negocios diario medio global.

<!--more-->

{{< key-takeaways >}}
- DORA es lex specialis respecto a NIS2 para el sector financiero europeo
- Aplica a entidades financieras y a sus proveedores críticos de servicios TIC
- Cinco pilares: gestión de riesgos TIC, notificación de incidentes, pruebas de resiliencia, gestión de terceros y compartición de información
- Sanciones: hasta 10 millones EUR o 5% de la facturación para entidades financieras
- Las entidades que ya cumplen ISO 27001 o ENS tienen parte del camino recorrido
{{< /key-takeaways >}}

## ¿Qué es el reglamento DORA y por qué existe?

[DORA](https://eur-lex.europa.eu/eli/reg/2022/2554) (Reglamento (UE) 2022/2554) fue adoptado el 14 de diciembre de 2022 y entró en aplicación el 17 de enero de 2025. Nació de una constatación clara: el sector financiero europeo depende de forma crítica de las tecnologías de la información y comunicación (TIC), pero no existía un marco armonizado que garantizara la resiliencia operativa digital de las entidades financieras frente a perturbaciones graves.

Antes de DORA, cada Estado miembro y cada regulador sectorial abordaba la ciberseguridad financiera de forma fragmentada. El Banco Central Europeo (BCE) emitía directrices para la banca, la Autoridad Europea de Valores y Mercados (ESMA) para los mercados de capitales y la Autoridad Europea de Seguros y Pensiones de Jubilación (EIOPA) para el sector asegurador. El resultado era un mosaico de requisitos dispares que dificultaba tanto el cumplimiento como la supervisión.

Según datos del BCE, los incidentes cibernéticos reportados por las entidades financieras europeas significativas aumentaron un 72 por ciento entre 2020 y 2024. El ataque a la plataforma ION Trading Technologies en enero de 2023, que afectó a la negociación de derivados en toda Europa, fue uno de los incidentes que aceleraron la adopción final de DORA.

## ¿A qué entidades financieras afecta DORA?

El ámbito de aplicación de DORA es extraordinariamente amplio dentro del sector financiero. Abarca 21 categorías de entidades:

### Entidades financieras

- **Entidades de crédito**(bancos).
-**Empresas de servicios de inversión**.
- **Sociedades de gestión de organismos de inversión colectiva**(gestoras de fondos).
-**Empresas de seguros y reaseguros**.
- **Fondos de pensiones de empleo**.
- **Entidades de dinero electrónico**.
- **Entidades de pago**.
- **Proveedores de servicios de criptoactivos**(incluidos bajo MiCA).
-**Depositarios centrales de valores**.
- **Entidades de contrapartida central**.
- **Centros de negociación**(bolsas de valores, sistemas multilaterales de negociación).
-**Registros de operaciones**.
- **Agencias de calificación crediticia**.
- **Proveedores de servicios de suministro de datos**.
- **Administradores de índices de referencia**.
- **Proveedores de servicios de financiación participativa**(crowdfunding financiero).

### Proveedores terceros de servicios TIC

Una de las novedades más significativas de DORA es la inclusión directa de los proveedores terceros de servicios TIC críticos. Esto abarca a proveedores de servicios cloud, centros de datos, empresas de software, proveedores de servicios gestionados (MSP), proveedores de seguridad gestionada (MSSP) y cualquier otro proveedor de servicios TIC que resulte crítico para las operaciones de las entidades financieras.

Los proveedores TIC críticos serán designados por las Autoridades Europeas de Supervisión (ESA) y estarán sujetos a un marco de supervisión directa por parte de un supervisor principal europeo. Esto supone un cambio radical: por primera vez, empresas tecnológicas que no son entidades financieras estarán sujetas a supervisión regulatoria directa en el contexto financiero.

### Excepciones y proporcionalidad

DORA aplica el principio de proporcionalidad: las microempresas financieras (menos de 10 empleados y menos de 2 millones de euros de facturación) tienen obligaciones simplificadas. Quedan exentas determinadas entidades menores como los intermediarios de seguros de pequeño tamaño. Sin embargo, la exención es estrecha y la inmensa mayoría de las entidades del sector financiero están obligadas.

## ¿Cuáles son los cinco pilares de DORA?

DORA se estructura en torno a cinco áreas fundamentales que, conjuntamente, definen un marco integral de resiliencia operativa digital.

### Pilar 1: Gestión de riesgos TIC

Las entidades financieras deben establecer un marco sólido e integral de gestión de riesgos TIC que incluya:

-**Gobernanza**: el órgano de dirección es directamente responsable de definir, aprobar, supervisar y asumir la responsabilidad última de la implementación del marco de gestión de riesgos TIC. Los miembros del consejo de administración deben recibir formación periódica en riesgos TIC.
- **Identificación de activos y riesgos**: inventario completo de activos de información, sistemas TIC, funciones empresariales y su interdependencia. Evaluación continua de amenazas y vulnerabilidades.
- **Protección y prevención**: implementación de políticas de seguridad, mecanismos de control de acceso, cifrado, gestión de parches y protección de redes.
- **Detección**: capacidades de monitorización continua y detección de actividades anómalas, con múltiples capas de control.
- **Respuesta y recuperación**: planes de respuesta a incidentes, planes de continuidad de negocio y procedimientos de recuperación ante desastres, con objetivos claros de tiempo de recuperación (RTO) y punto de recuperación (RPO).
- **Aprendizaje y evolución**: revisión post-incidente, incorporación de lecciones aprendidas y mejora continua del marco.

### Pilar 2: Notificación de incidentes relacionados con las TIC

DORA establece un proceso armonizado de clasificación y notificación de incidentes:

- **Clasificación**: las entidades deben clasificar los incidentes TIC según criterios definidos: número de clientes afectados, duración, extensión geográfica, impacto económico, pérdida de datos y criticidad de los servicios afectados.
- **Notificación inicial**: dentro de las 4 horas siguientes a la clasificación del incidente como grave (y no más de 24 horas después de su detección).
- **Informe intermedio**: dentro de las 72 horas, con actualizaciones sobre la gestión del incidente.
- **Informe final**: en el plazo de un mes, con el análisis de causas raíz y las medidas adoptadas.

Las notificaciones se dirigen a la autoridad competente nacional. En España, serán el Banco de España, la CNMV o la Dirección General de Seguros y Fondos de Pensiones, según el tipo de entidad.

### Pilar 3: Pruebas de resiliencia operativa digital

DORA exige un programa de pruebas riguroso y periódico:

- **Pruebas básicas**(para todas las entidades): evaluaciones de vulnerabilidades, análisis de software de código abierto, evaluaciones de seguridad de red, análisis de brechas, revisiones de seguridad física, pruebas de escenarios y pruebas de compatibilidad.
-**Pruebas avanzadas de penetración basadas en amenazas (TLPT)**: obligatorias cada tres años para las entidades que cumplan determinados criterios de tamaño y criticidad. Estas pruebas, basadas en el marco TIBER-EU, simulan ataques realistas contra los sistemas críticos de la entidad. Deben ser realizadas por auditores externos independientes y cualificados.

Las entidades deben documentar todas las pruebas, sus resultados y las acciones correctivas adoptadas.

### Pilar 4: Gestión de riesgos de terceros proveedores de servicios TIC

Este pilar aborda la dependencia crítica del sector financiero de proveedores tecnológicos:

- **Evaluación previa**: antes de contratar un proveedor TIC, la entidad debe realizar un análisis exhaustivo de riesgos, incluyendo la concentración de proveedores y los riesgos de subcontratación.
- **Requisitos contractuales**: DORA establece cláusulas mínimas obligatorias que deben incluirse en los contratos con proveedores TIC, incluyendo niveles de servicio, medidas de seguridad, obligaciones de notificación de incidentes, derechos de acceso y auditoría, estrategias de salida y planes de transición.
- **Registro de proveedores**: las entidades deben mantener un registro actualizado de todos sus proveedores TIC, clasificados por criticidad.
- **Supervisión de proveedores críticos**: los proveedores TIC designados como críticos estarán sujetos a supervisión directa por parte de las ESA, que podrán realizar inspecciones, solicitar información y emitir recomendaciones vinculantes.

### Pilar 5: Intercambio de información

DORA fomenta el intercambio voluntario de información sobre ciberamenazas entre entidades financieras:

- Las entidades pueden establecer acuerdos para compartir indicadores de compromiso (IoC), tácticas, técnicas y procedimientos (TTP) y alertas de seguridad.
- El intercambio debe respetar la normativa de protección de datos y competencia.
- Las autoridades supervisoras facilitarán y promoverán estos intercambios, reconociendo que la ciberseguridad es un desafío colectivo.

## ¿Cómo se relaciona DORA con NIS2 y otras normativas?

DORA y NIS2 se aprobaron el mismo día y fueron diseñadas para complementarse:

- **DORA es lex specialis**: para las entidades financieras, DORA prevalece sobre [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555) en los aspectos que regula. Es decir, si una entidad financiera está sujeta a DORA, debe cumplir DORA y no NIS2 para los requisitos de gestión de riesgos TIC, notificación de incidentes y pruebas de resiliencia. Para conocer en detalle los requisitos de [NIS2](/es/posts/2026/04/nis2-que-es-a-quien-afecta/), consulta nuestro artículo dedicado.
- **[ENS](https://www.boe.es/eli/es/rd/2022/05/03/311)**: las entidades financieras que operen en España y tengan relación con la Administración pública pueden necesitar cumplir tanto con DORA como con el ENS.
- **[RGPD](https://eur-lex.europa.eu/eli/reg/2016/679)**: un incidente TIC que afecte a datos personales activará obligaciones simultáneas bajo DORA y bajo el RGPD, con plazos y autoridades de notificación diferentes.
- **Directrices EBA/EIOPA/ESMA**: las directrices sectoriales preexistentes (como las Directrices EBA sobre gestión de riesgos TIC o las Directrices sobre externalización) se integran dentro del marco de DORA.
- **[ISO 27001](https://www.iso.org/standard/27001)**: si tu organización ya está certificada en ISO 27001, dispone de una base sólida para cumplir con el pilar 1 de DORA. Nuestra [guía de implementación de ISO 27001](/es/posts/2026/02/guía-iso-27001-startups/) puede ser un recurso útil para entender el marco de referencia.

{{< cta type="tofu" text="Cumplir DORA implica demostrar resiliencia operativa digital. Riskitera mapea los requisitos DORA a controles auditables automáticamente." label="Ver cómo" >}}

## ¿Cuándo entra en vigor DORA?

El calendario de DORA es el siguiente:

- **16 de enero de 2023**: entrada en vigor del Reglamento.
- **17 de enero de 2025**: fecha de aplicación. Desde esta fecha, todas las entidades incluidas en el ámbito de DORA deben cumplir con sus requisitos.
- **17 de enero de 2025 en adelante**: las Autoridades Europeas de Supervisión (ESA) publican los estándares técnicos regulatorios (RTS) y de implementación (ITS) que detallan los requisitos específicos.
- **2025-2026**: designación de los proveedores TIC terceros críticos y establecimiento del marco de supervisión directa.
- **2026**: primeras rondas de pruebas TLPT obligatorias para las entidades designadas.

En la práctica, las autoridades supervisoras nacionales han adoptado un enfoque gradual en la supervisión del cumplimiento durante el primer año de aplicación, priorizando la concienciación y la asistencia técnica. Sin embargo, las entidades que no demuestren avances significativos se exponen a medidas supervisoras.

## ¿Cómo prepararse para cumplir DORA?

### 1. Evaluación de aplicabilidad y análisis de brechas

Determina si tu organización está dentro del ámbito de DORA y, en su caso, qué requisitos específicos le aplican según su categoría y tamaño. Realiza un gap analysis detallado comparando tu postura actual con los requisitos de los cinco pilares.

### 2. Refuerzo de la gobernanza

Asegura que el órgano de dirección entiende sus responsabilidades bajo DORA. Establece comités específicos de riesgo TIC, define roles y responsabilidades claros y programa formación periódica para los consejeros.

### 3. Revisión del marco de gestión de riesgos TIC

Actualiza tu marco de gestión de riesgos para cubrir todos los aspectos del pilar 1: identificación de activos, evaluación continua de amenazas, medidas de protección, capacidades de detección y planes de respuesta y recuperación.

### 4. Implementación de procesos de notificación

Configura los mecanismos internos para clasificar incidentes según los criterios de DORA y notificarlos dentro de los plazos exigidos. Esto requiere capacidad de detección y triaje 24/7.

### 5. Programa de pruebas de resiliencia

Diseña un programa de pruebas que incluya evaluaciones de vulnerabilidades, pruebas de penetración y, si aplica, pruebas TLPT. Identifica a los proveedores externos cualificados para realizar las pruebas avanzadas.

### 6. Revisión de contratos con proveedores TIC

Audita todos los contratos existentes con proveedores TIC para verificar que incluyen las cláusulas mínimas exigidas por DORA. Renegocia los que sean necesarios y establece un registro centralizado de proveedores con su clasificación de criticidad.

### 7. Automatización y herramientas GRC

La complejidad de DORA hace que la gestión manual sea inviable para la mayoría de las entidades. Plataformas GRC como Riskitera permiten automatizar el seguimiento de controles, la gestión de evidencias, la monitorización del cumplimiento de proveedores y la generación de reportes regulatorios, reduciendo la carga operativa y el riesgo de incumplimiento.

### 8. Documentación y evidencias

DORA exige la capacidad de demostrar el cumplimiento ante las autoridades supervisoras. Mantener un repositorio centralizado de políticas, procedimientos, resultados de pruebas, registros de incidentes y evidencias de cumplimiento no es opcional: es una necesidad operativa.

## ¿Qué sanciones contempla DORA por incumplimiento?

DORA establece que los Estados miembros definan el régimen sancionador específico, pero marca unas directrices claras:

- Las sanciones deben ser efectivas, proporcionadas y disuasorias.
- Para los proveedores TIC críticos, las ESA pueden imponer multas coercitivas de hasta el 1 por ciento del volumen de negocios diario medio mundial del ejercicio anterior, por cada día de incumplimiento, durante un máximo de seis meses.
- Las autoridades nacionales pueden adoptar medidas administrativas como la publicación de resoluciones sancionadoras, la imposición de ordenes de cese y la exigencia de acciones correctivas en plazos determinados.

En España, el Banco de España y la CNMV disponen de facultades sancionadoras que se aplicarán en el contexto de DORA.

{{< cta type="mofu" text="Prepara tu entidad financiera para DORA con una plataforma que gestiona riesgos TIC, incidentes y pruebas de resiliencia." >}}

## Lo que más preguntan los equipos de seguridad

### ¿Soy una fintech con 15 empleados. Me aplica DORA?

Si tu empresa es una entidad de pago, entidad de dinero electrónico, proveedor de servicios de criptoactivos u otra categoría incluida en el artículo 2 de DORA, estás sujeta al reglamento independientemente de tu tamaño. Sin embargo, DORA aplica el principio de proporcionalidad: las microempresas financieras (menos de 10 empleados y menos de 2 millones de euros de balance) tienen un marco simplificado de gestión de riesgos. Con 15 empleados, probablemente debas cumplir con el marco completo pero de forma proporcionada a tu tamaño y complejidad operativa.

### ¿Qué diferencia hay entre DORA y NIS2 para una entidad financiera?

DORA es lex specialis respecto a NIS2 para el sector financiero. Esto significa que, para los aspectos cubiertos por DORA (gestión de riesgos TIC, notificación de incidentes, pruebas de resiliencia, gestión de terceros), las entidades financieras deben cumplir DORA y no NIS2. Sin embargo, si una entidad financiera opera en algún aspecto no cubierto por DORA, los requisitos de NIS2 podrían aplicar de forma subsidiaria.

### ¿Las pruebas TLPT son obligatorias para todas las entidades?

No. Las pruebas de penetración basadas en amenazas (TLPT) solo son obligatorias para las entidades que cumplan determinados criterios de tamaño, perfil de riesgo y criticidad sistémica. Las autoridades competentes designan a las entidades que deben someterse a estas pruebas. El resto de entidades deben realizar pruebas de resiliencia básicas (evaluaciones de vulnerabilidades, pruebas de seguridad, etc.) pero no las pruebas TLPT avanzadas.

### ¿Cuánto tiempo tengo para notificar un incidente grave bajo DORA?

El plazo comienza desde la clasificación del incidente como grave. La notificación inicial debe realizarse dentro de las 4 horas siguientes a la clasificación (y no más de 24 horas después de la detección). El informe intermedio debe enviarse dentro de las 72 horas y el informe final dentro de un mes. Estos plazos son más estrictos que los de NIS2 para la notificación inicial, lo que refleja la criticidad específica del sector financiero.

### ¿Mi empresa provee servicios cloud a bancos. Me afecta DORA directamente?

Sí. DORA incluye expresamente a los proveedores terceros de servicios TIC dentro de su ámbito. Si tus clientes son entidades financieras, estás sujeto a las obligaciones contractuales que DORA establece (cláusulas mínimas, derechos de auditoría, notificación de incidentes). Además, si las ESA te designan como proveedor TIC crítico, estarás sujeto a supervisión directa europea, con obligaciones adicionales de información, inspección y cumplimiento de recomendaciones vinculantes.
