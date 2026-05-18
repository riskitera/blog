---
title: "EU AI Act: implicaciones reales para equipos de ciberseguridad"
description: "Análisis del EU AI Act desde la perspectiva de ciberseguridad: clasificación de riesgo de sistemas IA, requisitos de seguridad, impacto en SOC y compliance, y plazos de aplicación."
slug: "eu-ai-act-ciberseguridad"
date: 2026-07-14
publishDate: 2026-07-14
lastmod: 2026-07-14
draft: false
tags: ["IA", "Compliance", "Europa"]
categories: ["Compliance"]
author: "David Moya"
keyword: "EU AI Act ciberseguridad"
funnel: "mofu"
---

Análisis del EU AI Act desde la perspectiva de ciberseguridad: clasificación de riesgo de sistemas IA, requisitos de seguridad, impacto en SOC y compliance, y plazos de aplicación.

<!--more-->

{{< key-takeaways >}}
- El [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689) clasifica los sistemas de IA en cuatro niveles de riesgo, y los equipos de ciberseguridad operan principalmente en las categorías de alto riesgo y riesgo limitado.
- Los sistemas de IA usados en SOC para detección de amenazas, triage automatizado y evaluación de riesgos están sujetos a requisitos específicos de transparencia, supervisión humana y documentación técnica.
- Los plazos de aplicación son escalonados: prohibiciones desde febrero 2025, obligaciones GPAI desde agosto 2025 y cumplimiento completo en agosto 2026.
- Los CISOs necesitan un inventario exhaustivo de todos los sistemas de IA desplegados en sus operaciones de seguridad para evaluar su nivel de riesgo regulatorio.
- La intersección con ENS, NIS2 y DORA crea un ecosistema normativo complejo que exige una estrategia de compliance integrada.
{{< /key-takeaways >}}

## ¿Qué es el EU AI Act y por que importa a los equipos de ciberseguridad

El [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689), conocido como EU AI Act, es la primera legislación integral sobre inteligencia artificial a nivel mundial. Aprobado en marzo de 2024 y publicado en el Diario Oficial de la UE en julio de 2024, este reglamento establece un marco jurídico armonizado para el desarrollo, comercialización y uso de sistemas de IA en la Unión Europea.

Para los equipos de ciberseguridad, el EU AI Act no es "otra normativa más" que gestionar desde compliance. Es una regulación que afecta directamente a las herramientas que usan a diario. Desde los motores de detección de amenazas basados en machine learning hasta los sistemas de triage automatizado en el SOC, pasando por las plataformas de evaluación de riesgos con IA, practicamente todo el stack de seguridad moderno incorpora algun componente de inteligencia artificial.

La cuestion central es que el AI Act no regula la IA en abstracto. Regula usos concretos. Y muchos de esos usos concretos son exactamente los que implementan los departamentos de seguridad de la información en organizaciones de todos los tamaños.

### El contexto regulatorio europeo

El EU AI Act no surge en el vacio. Forma parte de una estrategia europea más amplia de regulación digital que incluye el RGPD (protección de datos), el Digital Services Act (servicios digitales), el Digital Markets Act (competencia digital), NIS2 (ciberseguridad de infraestructuras críticas) y DORA (resiliencia operativa digital del sector financiero).

Esta convergencia regulatoria significa que los equipos de ciberseguridad no pueden analizar el AI Act de forma aislada. Necesitan entender cómo interactua con el resto del ecosistema normativo, especialmente cuando operan en sectores regulados como banca, energía, salud o telecomunicaciones.

## ¿Cómo clasifica el EU AI Act los sistemas de IA por riesgo

El núcleo del EU AI Act es su sistema de clasificación basado en riesgo. No todos los sistemas de IA reciben el mismo tratamiento regulatorio. El reglamento establece cuatro categorías con obligaciones progresivas.

### Riesgo inaceptable (prohibido)

Son sistemas de IA cuyo uso esta directamente prohibido en la UE por considerarse incompatible con los derechos fundamentales. Incluyen:

- **Sistemas de puntuación social** (social scoring) por parte de autoridades públicas o en su nombre.
- **Manipulación subliminal** de personas mediante técnicas que explotan vulnerabilidades (edad, discapacidad, situación económica).
- **Identificación biométrica remota en tiempo real** en espacios públicos con fines de aplicación de la ley (con excepciones tasadas).
- **Categorización biométrica** basada en caracteristicas sensibles (raza, orientación sexual, creencias políticas).
- **Scraping no dirigido de imagenes faciales** de internet o cámaras de videovigilancia para crear bases de datos de reconocimiento facial.
- **Reconocimiento de emociones** en el lugar de trabajo y en centros educativos.

Para ciberseguridad, la implicación directa es que cualquier herramienta de seguridad física o de vigilancia que use reconocimiento facial en tiempo real necesita una revisión legal inmediata. También afecta a los sistemas de behavioral analytics que puedan inferir estados emocionales de empleados.

### Riesgo alto

Esta es la categoría más relevante para los equipos de ciberseguridad. Un sistema de IA se considera de alto riesgo cuando se utiliza en alguna de las áreas listadas en el Anexo III del reglamento, que incluye:

- **Infraestructuras críticas**: sistemas de IA usados en la gestión y operación de infraestructuras críticas digitales, incluyendo el suministro de agua, gas, calefacción y electricidad.
- **Acceso a servicios esenciales**: sistemas que determinan el acceso a servicios públicos y privados esenciales.
- **Aplicación de la ley**: sistemas usados para evaluar riesgos de reincidencia, poligrafos, evaluación de pruebas.
- **Gestión de migración, asilo y control de fronteras**.
- **Administración de justicia y procesos democraticos**.

En la práctica, muchos sistemas de seguridad operan en o para infraestructuras críticas. Un SIEM con capacidades de IA que monitoriza una red eléctrica, un sistema de detección de intrusiones con machine learning en un hospital, o una plataforma de gestión de vulnerabilidades con priorización automatizada en un banco: todos podrían caer en la categoría de alto riesgo dependiendo del contexto de uso.

### Riesgo limitado

Los sistemas de riesgo limitado tienen obligaciones de transparencia. Esto significa que los usuarios deben ser informados de que están interactuando con un sistema de IA. Los casos más comunes incluyen:

- **Chatbots**: cualquier sistema conversacional basado en IA debe informar al usuario de que está interactuando con una máquina.
- **Deep fakes**: contenido generado o manipulado por IA debe etiquetarse como tal.
- **Sistemas de reconocimiento de emociones o categorización biométrica** (los que no están prohibidos).

En ciberseguridad, esto afecta a los chatbots de soporte de seguridad, a los asistentes virtuales para gestión de incidentes y a cualquier interfaz conversacional que use IA para interactuar con usuarios o analistas.

### Riesgo mínimo

La gran mayoría de sistemas de IA quedan en esta categoría y no tienen obligaciones específicas bajo el AI Act. Incluyen filtros de spam, sistemas de recomendación de contenido, herramientas de búsqueda básicas y otros usos cotidianos que no plantean riesgos significativos para los derechos fundamentales.

Algunos componentes del stack de seguridad podrían clasificarse aquí: filtros antispam básicos, clasificadores de correo, o herramientas de productividad con IA integrada.

## Requisitos de seguridad para sistemas de IA de alto riesgo

Los sistemas clasificados como alto riesgo deben cumplir un conjunto exhaustivo de requisitos antes de poder comercializarse o desplegarse en la UE. Estos requisitos tienen implicaciones directas para los equipos de ciberseguridad, tanto como usuarios de estos sistemas como responsables de garantizar su seguridad.

### Gestión de riesgos continúa

El artículo 9 del AI Act exige un sistema de gestión de riesgos que se mantenga durante todo el ciclo de vida del sistema de IA. No es un análisis puntual: es un proceso iterativo que incluye identificación, estimación, evaluación y tratamiento de riesgos. Para los equipos de seguridad, esto se traduce en:

- Documentar los riesgos de cada sistema de IA desplegado en el SOC o en herramientas GRC.
- Evaluar periódicamente si el perfil de riesgo ha cambiado (por actualizaciónes del modelo, cambios en los datos de entrenamiento, nuevos vectores de ataque).
- Implementar medidas de mitigación proporcionales al nivel de riesgo identificado.

### Gobernanza de datos

El artículo 10 establece requisitos estrictos sobre los datos usados para entrenar, validar y testear sistemas de IA de alto riesgo. Los datasets deben ser relevantes, representativos, libres de errores y completos. Deben documentarse las prácticas de gobernanza de datos, incluyendo el propósito de la recopilación, los procesos de preparación y las medidas para detectar sesgos.

En un contexto SOC, esto significa que los modelos de detección de amenazas deben entrenarse con datasets que representen adecuadamente el panorama de amenazas actual. Un modelo entrenado solo con amenazas de 2023 no cumple el requisito de representatividad en 2026.

### Documentación técnica

Antes de comercializar un sistema de IA de alto riesgo, el proveedor debe elaborar documentación técnica detallada (artículo 11) que demuestre el cumplimiento de todos los requisitos. Esta documentación debe incluir:

- Descripción general del sistema y su propósito.
- Descripción detallada de los elementos del sistema y su proceso de desarrollo.
- Información sobre los datos de entrenamiento, validación y prueba.
- Métricas de rendimiento y limitaciones conocidas.
- Descripción de las medidas de supervisión humana.

### Registro automático de actividad (logging)

El artículo 12 requiere que los sistemas de IA de alto riesgo incluyan capacidades de logging que permitan la trazabilidad de su funcionamiento. Los registros deben permitir identificar situaciones de riesgo, facilitar la monitorización post-despliegue y asistir en investigaciones de conformidad.

Para equipos de ciberseguridad, este requisito es natural: el logging exhaustivo ya es una práctica estándar. La diferencia es que ahora el logging de los propios sistemas de IA de seguridad tiene un marco legal que define que debe registrarse y durante cuanto tiempo.

### Transparencia e información

Los usuarios de sistemas de IA de alto riesgo deben recibir información suficiente para interpretar los resultados del sistema y usarlo de forma apropiada (artículo 13). Esto incluye información sobre el nivel de precisión, robustez y ciberseguridad del sistema.

### Supervisión humana

El artículo 14 establece que los sistemas de IA de alto riesgo deben disenarse para permitir una supervisión humana efectiva. Esto no significa simplemente que un humano pueda pulsar un boton de apagado. Implica que:

- Las personas encargadas de supervisar el sistema deben poder comprender sus capacidades y limitaciones.
- Deben poder interpretar correctamente los resultados del sistema.
- Deben poder decidir no usar el sistema o ignorar sus resultados.
- Deben poder intervenir o detener el sistema en cualquier momento.

En un SOC, esto tiene implicaciones directas sobre el grado de automatización permisible. Un sistema que automatiza completamente la respuesta a incidentes sin ninguna supervisión humana en decisiones de alto riesgo (por ejemplo, aislar un servidor de producción crítico) podría no cumplir este requisito.

### Precisión, robustez y ciberseguridad

El artículo 15 es el que más directamente concierne a los profesionales de ciberseguridad. Exige que los sistemas de IA de alto riesgo alcancen niveles apropiados de:

- **Precisión**: el sistema debe funcionar según lo previsto. Las métricas de rendimiento deben documentarse y comunicarse.
- **Robustez**: el sistema debe ser resiliente frente a errores, fallos, inconsistencias y situaciones inesperadas. Debe incluir medidas de redundancia y mecanismos fail-safe.
- **Ciberseguridad**: el sistema debe protegerse frente a ataques que intenten manipular su comportamiento. Esto incluye protección contra data poisoning, adversarial examples, model extraction y otros ataques específicos a sistemas de IA.

## ¿Cómo afecta el AI Act a los equipos de ciberseguridad en la práctica

Vamos a lo concreto. Estos son los escenarios prácticos donde el AI Act impacta directamente en las operaciones de seguridad.

### IA en el SOC: detección y triage

Los SOC modernos utilizan IA de múltiples formas:

- **Detección de anomalías** en tráfico de red mediante modelos de machine learning.
- **Correlación automatizada de eventos** en plataformas SIEM con capacidades de IA.
- **Triage automatizado** de alertas mediante clasificadores que priorizan por severidad.
- **Análisis de comportamiento de usuarios** (UEBA) para detectar amenazas internas.

La clasificación de riesgo de estos sistemas depende del contexto. Si el SOC protege infraestructura crítica (energía, transporte, salud, finanzas), los sistemas de IA utilizados probablemente se clasifiquen como alto riesgo. Si protege una empresa de comercio electrónico, podrían quedar en riesgo limitado o mínimo.

La recomendación práctica es asumir el peor caso y prepararse para cumplir los requisitos de alto riesgo. El coste de estar preparado es significativamente menor que el de una sanción por incumplimiento.

### IA en GRC: evaluación de riesgos y compliance

Las plataformas GRC modernas incorporan IA para:

- **Evaluación automatizada de riesgos** basada en datos históricos y contexto sectorial.
- **Mapeo automático de controles** entre diferentes frameworks (ENS, NIS2, ISO 27001, DORA).
- **Priorización de hallazgos** de auditorías mediante scoring automatizado.
- **Generación de informes** de compliance con lenguaje natural.

Cuando estos sistemas toman decisiones o generan recomendaciones que influyen directamente en la postura de seguridad de una organización regulada, pueden clasificarse como alto riesgo. Un sistema de IA que recomienda no aplicar un parche crítico porque su análisis de riesgos automatizado lo considera bajo riesgo esta tomando una decisión con implicaciones de seguridad significativas.

### IA en CTI: inteligencia de amenazas

Los equipos de Cyber Threat Intelligence usan IA para:

- **Clasificación automática de indicadores de compromiso** (IoCs).
- **Análisis de malware** mediante modelos de machine learning.
- **Correlación de campañas de amenazas** usando procesamiento de lenguaje natural.
- **Predicción de tendencias de amenazas** basada en datos históricos.

Estos sistemas generalmente se clasifican como riesgo limitado o mínimo, salvo que operen en el contexto de infraestructuras críticas o aplicación de la ley.

### Impacto en proveedores de herramientas de seguridad

Si tu organización desarrolla herramientas de seguridad con IA (SIEM, SOAR, EDR, XDR con capacidades de machine learning), el AI Act te afecta como proveedor. Debes:

- Clasificar el riesgo de cada producto.
- Cumplir los requisitos aplicables a tu categoría de riesgo.
- Proporcionar documentación técnica a tus clientes.
- Implementar sistemas de gestión de calidad.
- Someterte a evaluaciones de conformidad cuando sea necesario.

{{< cta type="tofu" text="Riskitera evalua tu postura de seguridad y te muestra los gaps de cumplimiento del AI Act, ENS y NIS2 en minutos." label="Evaluar postura" >}}

## Timeline del EU AI Act: fechas clave para equipos de seguridad

El AI Act sigue un calendario de aplicación escalonado. Estas son las fechas que todo CISO y responsable de seguridad debe tener marcadas.

### Febrero 2025: prohibiciones activas

Desde el 2 de febrero de 2025, las prácticas de IA prohibidas (riesgo inaceptable) ya son de obligado cumplimiento. Si tu organización utiliza algun sistema de IA que cae en esta categoría, debe haberse retirado antes de esta fecha. Revisa especialmente:

- Sistemas de videovigilancia con reconocimiento facial en tiempo real (excepto los supuestos tasados).
- Herramientas de análisis de comportamiento que puedan inferir emociones en el ámbito laboral.
- Cualquier forma de puntuación social aplicada a empleados o clientes.

### Agosto 2025: obligaciones GPAI

Desde el 2 de agosto de 2025, se aplican las obligaciones para modelos de IA de propósito general (GPAI, General Purpose AI). Esto afecta a los proveedores de modelos fundacionales como GPT, Claude, Gemini, Llama, Mistral y similares. Para los equipos de seguridad, las implicaciones son:

- Los proveedores de modelos GPAI deben proporcionar documentación técnica y resumen del contenido usado para entrenar el modelo.
- Los modelos GPAI con riesgo sistemico (aquellos entrenados con más de 10^25 FLOPs) tienen obligaciones adicionales de evaluación y mitigación de riesgos.
- Si usas modelos GPAI como parte de tu stack de seguridad (por ejemplo, LLMs para análisis de logs o generación de informes), debes verificar que tu proveedor cumple estas obligaciones.

### Agosto 2026: cumplimiento completo

El 2 de agosto de 2026 es la fecha de aplicación completa del AI Act. A partir de esta fecha, todos los requisitos para sistemas de IA de alto riesgo están en vigor. Esto significa:

- Los sistemas de IA de alto riesgo que se comercialicen o desplieguen deben cumplir todos los requisitos del reglamento.
- Los proveedores deben tener implementados sus sistemas de gestión de calidad.
- Las evaluaciones de conformidad deben estar completadas.
- La documentación técnica debe estar disponible.

### Agosto 2027: obligaciones adicionales para ciertos sistemas de alto riesgo

Los sistemas de IA de alto riesgo que son componentes de seguridad de productos ya regulados (por ejemplo, dispositivos médicos, vehículos, aviación) tienen hasta el 2 de agosto de 2027 para cumplir.

## Relación del AI Act con ENS, NIS2 y DORA

El AI Act no opera en solitario. Para organizaciones en España y la UE, la intersección con otras normativas de seguridad crea un panorama regulatorio complejo pero coherente.

### AI Act y ENS (Esquema Nacional de Seguridad)

El [ENS](https://ens.ccn.cni.es/) establece los principios básicos y requisitos mínimos de seguridad para los sistemas de información del sector público español y sus proveedores. Cuando una administración pública o su cadena de suministro despliega sistemas de IA, el AI Act se superpone al ENS:

- **Gestión de riesgos**: ambos requieren análisis de riesgos, pero el AI Act añade requisitos específicos para riesgos derivados de la IA (sesgos, robustez, ataques adversariales).
- **Trazabilidad**: el ENS ya exige logging extenso, lo que facilita el cumplimiento del artículo 12 del AI Act.
- **Supervisión**: el ENS categoriza los sistemas por nivel de seguridad (bajo, medio, alto), lo que puede complementar la clasificación de riesgo del AI Act.

### AI Act y NIS2

La [Directiva NIS2](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive) establece obligaciones de ciberseguridad para entidades esenciales e importantes. Su intersección con el AI Act es particularmente relevante porque:

- Muchas entidades cubiertas por NIS2 (energía, transporte, salud, infraestructuras digitales) son exactamente los sectores donde el AI Act clasifica sistemas como alto riesgo.
- NIS2 exige gestión de riesgos de seguridad de la cadena de suministro, lo que incluye evaluar los riesgos de los sistemas de IA proporcionados por terceros.
- Los requisitos de notificación de incidentes de NIS2 se aplican también a incidentes que involucren sistemas de IA.

### AI Act y DORA

El [Reglamento DORA](https://www.digital-operational-resilience-act.com/) se centra en la resiliencia operativa digital del sector financiero. Para bancos, aseguradoras y gestoras de activos que usan IA:

- DORA exige pruebas de resiliencia operativa que ahora deben incluir los sistemas de IA críticos.
- Los acuerdos con proveedores de servicios TIC (incluidos proveedores de IA) deben cumplir requisitos específicos de DORA.
- La gestión de riesgos de terceros bajo DORA debe considerar los riesgos específicos de los sistemas de IA utilizados.

## Checklist del CISO para el EU AI Act

Esta es una guía práctica para que los CISOs y responsables de seguridad preparen su organización.

### Fase 1: inventario y clasificación (hacer ahora)

1. **Inventariar todos los sistemas de IA** en uso en la organización. No solo los que el equipo de seguridad utiliza, sino todos los que la organización ha desplegado. Incluir:
   - Herramientas de seguridad con componentes de IA (SIEM, SOAR, EDR, XDR, UEBA).
   - Sistemas de GRC con capacidades de IA.
   - Chatbots y asistentes virtuales.
   - Herramientas de productividad con IA integrada (Copilot, asistentes de código).
   - Modelos de IA desarrollados internamente.

2. **Clasificar cada sistema** según las categorías de riesgo del AI Act. Documentar la justificación de cada clasificación.

3. **Identificar proveedores** de sistemas de IA y verificar su postura de cumplimiento del AI Act.

### Fase 2: gap analysis (Q3 2026)

4. **Evaluar el cumplimiento actual** de cada sistema de alto riesgo contra los requisitos del AI Act.
5. **Documentar gaps** y crear un plan de remediación priorizado.
6. **Revisar contratos con proveedores** para incluir cláusulas de cumplimiento del AI Act.
7. **Evaluar la capacidad interna** de supervisión humana de los sistemas de IA.

### Fase 3: implementación (Q4 2026)

8. **Implementar controles** para los gaps identificados.
9. **Establecer procesos de gobernanza** de IA que integren los requisitos del AI Act con los frameworks existentes (ENS, NIS2, ISO 27001).
10. **Formar al equipo** en los requisitos del AI Act y en las responsabilidades específicas de cada rol.
11. **Implementar o mejorar el logging** de los sistemas de IA para cumplir el artículo 12.

### Fase 4: monitorización continua (permanente)

12. **Establecer un proceso de monitorización post-despliegue** para todos los sistemas de IA de alto riesgo.
13. **Integrar la gestión de riesgos de IA** en el ciclo de gestión de riesgos corporativo.
14. **Auditar periódicamente** el cumplimiento de los requisitos del AI Act.
15. **Mantener actualizada la documentación técnica** ante cambios en los sistemas de IA.

## Impacto en herramientas de seguridad con IA

El mercado de herramientas de ciberseguridad está en plena transformación por el AI Act. Estos son los cambios concretos que ya se están produciendo.

### SIEM con IA

Los principales proveedores de SIEM (Splunk, Microsoft Sentinel, Elastic Security, QRadar) están actualizando sus productos para cumplir los requisitos del AI Act. Los cambios incluyen:

- Mayor transparencia en los modelos de detección: los proveedores deben explicar cómo funcionan sus algoritmos de correlación y detección de anomalías.
- Mejoras en el logging de decisiones de la IA: cada alerta generada por un modelo de IA debe incluir información sobre la confianza del modelo y los factores que contribuyeron a la decisión.
- Opciones de supervisión humana mejoradas: interfaces que permiten a los analistas entender, cuestionar y anular las decisiones de la IA.

### EDR/XDR con IA

Las plataformas de detección y respuesta (CrowdStrike Falcon, SentinelOne, Microsoft Defender) utilizan extensivamente IA para detección de malware, análisis de comportamiento y respuesta automatizada. El AI Act les exige:

- Documentar los datasets de entrenamiento de sus modelos de detección.
- Proporcionar métricas de precisión (falsos positivos, falsos negativos) verificables.
- Garantizar que las acciones de respuesta automatizada cuentan con mecanismos de supervisión humana adecuados.

### SOAR con IA

Las plataformas de orquestación y respuesta automatizada (Palo Alto XSOAR, Splunk SOAR, Swimlane) que incorporan decisión-making basado en IA deben:

- Permitir que los playbooks automatizados incluyan puntos de decisión humana en acciones de alto impacto.
- Documentar la lógica de decisión de los componentes de IA.
- Proporcionar trazabilidad completa de cada acción ejecutada por la IA.

## Sanciones por incumplimiento

El régimen sancionador del AI Act es significativo y proporcional a la gravedad de la infracción:

- **Prácticas prohibidas**: hasta 35 millones de euros o el 7% de la facturación anual global (lo que sea mayor).
- **Incumplimiento de requisitos de alto riesgo**: hasta 15 millones de euros o el 3% de la facturación anual global.
- **Información incorrecta**: hasta 7,5 millones de euros o el 1,5% de la facturación anual global.

Para PYMEs y startups, las multas se calculan sobre la base del porcentaje de facturación, lo que proporciona cierta proporcionalidad. No obstante, incluso una sanción del 3% puede ser existencial para una empresa pequeña.

Las autoridades nacionales de supervisión (en España, la [AEPD](https://www.aepd.es/) tiene un papel coordinador junto con la futura Agencia Española de Supervisión de la IA) tendrán potestad para:

- Realizar inspecciones.
- Exigir acceso a la documentación técnica.
- Ordenar la retirada de sistemas de IA no conformes del mercado.
- Imponer sanciones económicas.

{{< cta type="bofu" text="Empieza tu PoC de 90 días con Riskitera y automatiza el compliance del AI Act, ENS y NIS2 desde el primer dia." label="Iniciar PoC" >}}

## Recomendaciones prácticas para equipos de ciberseguridad

### Para organizaciones que usan IA en seguridad

1. **No esperes a agosto de 2026**. El inventario y la clasificación de sistemas de IA deben empezar ya. El esfuerzo de documentación y adaptación es significativo.

2. **Integra el AI Act en tu marco de compliance existente**. Si ya cumples ENS Alto o ISO 27001, tienes una base sólida. Los controles de gestión de riesgos, logging, documentación y supervisión humana ya están parcialmente cubiertos.

3. **Exige información a tus proveedores**. Pregunta a tus proveedores de herramientas de seguridad como están adaptando sus productos al AI Act. Pide documentación técnica, métricas de rendimiento y hojas de ruta de cumplimiento.

4. **Forma a tus analistas SOC**. Los analistas que supervisan sistemas de IA deben entender las capacidades y limitaciones de estos sistemas. La supervisión humana efectiva requiere conocimiento técnico.

5. **Revisa tus playbooks de respuesta automatizada**. Identifica donde la IA toma decisiones críticas sin supervisión humana y añade checkpoints de validación humana donde sea necesario.

### Para proveedores de herramientas de seguridad

1. **Clasificad vuestros productos**. Determinad en que categoría de riesgo cae cada producto según el contexto de uso.

2. **Documentad todo**. La documentación técnica exigida por el AI Act debe ser exhaustiva: arquitectura, datos de entrenamiento, métricas de rendimiento, limitaciones conocidas, medidas de seguridad.

3. **Implementad explainability**. Los clientes necesitan entender por que la IA toma cada decisión. Esto no significa que los modelos deban ser interpretables (glass box), pero si que cada resultado debe acompañarse de información contextual suficiente.

4. **Preparad las evaluaciones de conformidad**. Para sistemas de alto riesgo, necesitareis someteros a evaluaciones de conformidad por organismos notificados.

## Recursos y organismos de referencia

Para mantenerse actualizado sobre el EU AI Act y su aplicación en ciberseguridad:

- **[ENISA](https://www.enisa.europa.eu/)**: la Agencia de la UE para la Ciberseguridad pública guías y análisis sobre la intersección entre IA y ciberseguridad.
- **[AI Office de la Comisión Europea](https://digital-strategy.ec.europa.eu/en/policies/ai-office)**: responsable de supervisar los modelos GPAI y coordinar la aplicación del AI Act.
- **[CCN-CERT](https://www.ccn-cert.cni.es/)**: en el ámbito español, el Centro Criptológico Nacional pública guías de seguridad que iran incorporando los requisitos del AI Act.
- **[INCIBE](https://www.incibe.es/)**: el Instituto Nacional de Ciberseguridad ofrece recursos y formación sobre seguridad, incluyendo aspectos relacionados con IA.
- **Texto completo del reglamento**: [EUR-Lex 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689).


**Artículos relacionados:**
- [Nis2 Que Es A Quien Afecta](/es/posts/2026/04/nis2-que-es-a-quien-afecta/)

## Preguntas frecuentes

### ¿El EU AI Act obliga a dejar de usar IA en el SOC?

No. El AI Act no prohibe el uso de IA en operaciones de seguridad. Lo que hace es establecer requisitos según el nivel de riesgo del sistema. Los equipos SOC pueden seguir usando herramientas de detección, triage y respuesta basadas en IA, pero deben garantizar que cumplen los requisitos de transparencia, supervisión humana, logging y documentación aplicables a su categoría de riesgo. En la mayoría de los casos, esto supone mejorar prácticas ya existentes, no eliminar herramientas.

### ¿Qué pasa si mi proveedor de SIEM o EDR no cumple el AI Act?

Si despliegas un sistema de IA que no cumple el AI Act, la responsabilidad recae tanto en el proveedor (como desarrollador del sistema) como en tu organización (como deployer o usuario). El reglamento establece obligaciones diferenciadas para proveedores y usuarios. Como usuario, debes verificar que tus proveedores cumplen, exigir la documentación técnica necesaria y mantener registros de tu diligencia debida. Si un proveedor no demuestra cumplimiento antes de agosto de 2026, deberías evaluar alternativas.

### ¿Cómo clasifico la IA de mi SOC: alto riesgo o riesgo limitado?

La clasificación depende del contexto de uso, no de la tecnología en si. Un mismo sistema de detección de anomalías puede ser de alto riesgo si protege una infraestructura crítica (hospital, central eléctrica, red de transporte) y de riesgo limitado si protege una empresa de comercio electrónico. La clave está en revisar el Anexo III del reglamento e identificar si el uso de tu sistema entra en alguna de las categorías listadas. Ante la duda, clasifica como alto riesgo: cumplir requisitos superiores nunca es un problema regulatorio.

### ¿El AI Act afecta a los modelos de IA open source que uso en mi SOC?

Sí. El AI Act se aplica independientemente de si el modelo es propietario u open source. Si despliegas un modelo open source (por ejemplo, un modelo de detección de malware basado en un modelo fundacional abierto), eres responsable de cumplir los requisitos aplicables como deployer. Los proveedores de modelos GPAI open source tienen ciertas exenciones (no necesitan proporcionar documentación técnica tan exhaustiva si el modelo se distribuye con licencia libre), pero estas exenciones no se extienden a los usuarios que despliegan el modelo en contextos de alto riesgo.

### ¿Cuánto cuesta adaptarse al EU AI Act para un equipo de seguridad típico?

El coste depende enormemente del tamaño de la organización, del número de sistemas de IA en uso y del nivel de madurez actual en gobernanza de IA. Para una organización mediana (500-2000 empleados) con un SOC que utiliza 3-5 herramientas con componentes de IA, la estimación realista incluye: inventario y clasificación (2-4 semanas de trabajo de consultoría), gap analysis (4-8 semanas), implementación de controles adicionales (variable, pero típicamente 3-6 meses), y formación del equipo (1-2 semanas). En términos económicos, el rango típico es de 50.000 a 200.000 euros para el proyecto inicial de adaptación, más un coste recurrente de mantenimiento del 10-15% anual.
