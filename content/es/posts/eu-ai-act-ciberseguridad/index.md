---
title: "EU AI Act: implicaciones reales para equipos de ciberseguridad"
description: "Analisis del EU AI Act desde la perspectiva de ciberseguridad: clasificacion de riesgo de sistemas IA, requisitos de seguridad, impacto en SOC y compliance, y plazos de aplicacion."
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

Analisis del EU AI Act desde la perspectiva de ciberseguridad: clasificacion de riesgo de sistemas IA, requisitos de seguridad, impacto en SOC y compliance, y plazos de aplicacion.

<!--more-->

{{< key-takeaways >}}
- El [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689) clasifica los sistemas de IA en cuatro niveles de riesgo, y los equipos de ciberseguridad operan principalmente en las categorias de alto riesgo y riesgo limitado.
- Los sistemas de IA usados en SOC para deteccion de amenazas, triage automatizado y evaluacion de riesgos estan sujetos a requisitos especificos de transparencia, supervision humana y documentacion tecnica.
- Los plazos de aplicacion son escalonados: prohibiciones desde febrero 2025, obligaciones GPAI desde agosto 2025 y cumplimiento completo en agosto 2026.
- Los CISOs necesitan un inventario exhaustivo de todos los sistemas de IA desplegados en sus operaciones de seguridad para evaluar su nivel de riesgo regulatorio.
- La interseccion con ENS, NIS2 y DORA crea un ecosistema normativo complejo que exige una estrategia de compliance integrada.
{{< /key-takeaways >}}

## Que es el EU AI Act y por que importa a los equipos de ciberseguridad

El [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689), conocido como EU AI Act, es la primera legislacion integral sobre inteligencia artificial a nivel mundial. Aprobado en marzo de 2024 y publicado en el Diario Oficial de la UE en julio de 2024, este reglamento establece un marco juridico armonizado para el desarrollo, comercializacion y uso de sistemas de IA en la Union Europea.

Para los equipos de ciberseguridad, el EU AI Act no es "otra normativa mas" que gestionar desde compliance. Es una regulacion que afecta directamente a las herramientas que usan a diario. Desde los motores de deteccion de amenazas basados en machine learning hasta los sistemas de triage automatizado en el SOC, pasando por las plataformas de evaluacion de riesgos con IA, practicamente todo el stack de seguridad moderno incorpora algun componente de inteligencia artificial.

La cuestion central es que el AI Act no regula la IA en abstracto. Regula usos concretos. Y muchos de esos usos concretos son exactamente los que implementan los departamentos de seguridad de la informacion en organizaciones de todos los tamanos.

### El contexto regulatorio europeo

El EU AI Act no surge en el vacio. Forma parte de una estrategia europea mas amplia de regulacion digital que incluye el RGPD (proteccion de datos), el Digital Services Act (servicios digitales), el Digital Markets Act (competencia digital), NIS2 (ciberseguridad de infraestructuras criticas) y DORA (resiliencia operativa digital del sector financiero).

Esta convergencia regulatoria significa que los equipos de ciberseguridad no pueden analizar el AI Act de forma aislada. Necesitan entender como interactua con el resto del ecosistema normativo, especialmente cuando operan en sectores regulados como banca, energia, salud o telecomunicaciones.

## Como clasifica el EU AI Act los sistemas de IA por riesgo

El nucleo del EU AI Act es su sistema de clasificacion basado en riesgo. No todos los sistemas de IA reciben el mismo tratamiento regulatorio. El reglamento establece cuatro categorias con obligaciones progresivas.

### Riesgo inaceptable (prohibido)

Son sistemas de IA cuyo uso esta directamente prohibido en la UE por considerarse incompatible con los derechos fundamentales. Incluyen:

- **Sistemas de puntuacion social** (social scoring) por parte de autoridades publicas o en su nombre.
- **Manipulacion subliminal** de personas mediante tecnicas que explotan vulnerabilidades (edad, discapacidad, situacion economica).
- **Identificacion biometrica remota en tiempo real** en espacios publicos con fines de aplicacion de la ley (con excepciones tasadas).
- **Categorizacion biometrica** basada en caracteristicas sensibles (raza, orientacion sexual, creencias politicas).
- **Scraping no dirigido de imagenes faciales** de internet o camaras de videovigilancia para crear bases de datos de reconocimiento facial.
- **Reconocimiento de emociones** en el lugar de trabajo y en centros educativos.

Para ciberseguridad, la implicacion directa es que cualquier herramienta de seguridad fisica o de vigilancia que use reconocimiento facial en tiempo real necesita una revision legal inmediata. Tambien afecta a los sistemas de behavioral analytics que puedan inferir estados emocionales de empleados.

### Riesgo alto

Esta es la categoria mas relevante para los equipos de ciberseguridad. Un sistema de IA se considera de alto riesgo cuando se utiliza en alguna de las areas listadas en el Anexo III del reglamento, que incluye:

- **Infraestructuras criticas**: sistemas de IA usados en la gestion y operacion de infraestructuras criticas digitales, incluyendo el suministro de agua, gas, calefaccion y electricidad.
- **Acceso a servicios esenciales**: sistemas que determinan el acceso a servicios publicos y privados esenciales.
- **Aplicacion de la ley**: sistemas usados para evaluar riesgos de reincidencia, poligrafos, evaluacion de pruebas.
- **Gestion de migracion, asilo y control de fronteras**.
- **Administracion de justicia y procesos democraticos**.

En la practica, muchos sistemas de seguridad operan en o para infraestructuras criticas. Un SIEM con capacidades de IA que monitoriza una red electrica, un sistema de deteccion de intrusiones con machine learning en un hospital, o una plataforma de gestion de vulnerabilidades con priorizacion automatizada en un banco: todos podrian caer en la categoria de alto riesgo dependiendo del contexto de uso.

### Riesgo limitado

Los sistemas de riesgo limitado tienen obligaciones de transparencia. Esto significa que los usuarios deben ser informados de que estan interactuando con un sistema de IA. Los casos mas comunes incluyen:

- **Chatbots**: cualquier sistema conversacional basado en IA debe informar al usuario de que esta interactuando con una maquina.
- **Deep fakes**: contenido generado o manipulado por IA debe etiquetarse como tal.
- **Sistemas de reconocimiento de emociones o categorizacion biometrica** (los que no estan prohibidos).

En ciberseguridad, esto afecta a los chatbots de soporte de seguridad, a los asistentes virtuales para gestion de incidentes y a cualquier interfaz conversacional que use IA para interactuar con usuarios o analistas.

### Riesgo minimo

La gran mayoria de sistemas de IA quedan en esta categoria y no tienen obligaciones especificas bajo el AI Act. Incluyen filtros de spam, sistemas de recomendacion de contenido, herramientas de busqueda basicas y otros usos cotidianos que no plantean riesgos significativos para los derechos fundamentales.

Algunos componentes del stack de seguridad podrian clasificarse aqui: filtros antispam basicos, clasificadores de correo, o herramientas de productividad con IA integrada.

## Requisitos de seguridad para sistemas de IA de alto riesgo

Los sistemas clasificados como alto riesgo deben cumplir un conjunto exhaustivo de requisitos antes de poder comercializarse o desplegarse en la UE. Estos requisitos tienen implicaciones directas para los equipos de ciberseguridad, tanto como usuarios de estos sistemas como responsables de garantizar su seguridad.

### Gestion de riesgos continua

El articulo 9 del AI Act exige un sistema de gestion de riesgos que se mantenga durante todo el ciclo de vida del sistema de IA. No es un analisis puntual: es un proceso iterativo que incluye identificacion, estimacion, evaluacion y tratamiento de riesgos. Para los equipos de seguridad, esto se traduce en:

- Documentar los riesgos de cada sistema de IA desplegado en el SOC o en herramientas GRC.
- Evaluar periodicamente si el perfil de riesgo ha cambiado (por actualizaciones del modelo, cambios en los datos de entrenamiento, nuevos vectores de ataque).
- Implementar medidas de mitigacion proporcionales al nivel de riesgo identificado.

### Gobernanza de datos

El articulo 10 establece requisitos estrictos sobre los datos usados para entrenar, validar y testear sistemas de IA de alto riesgo. Los datasets deben ser relevantes, representativos, libres de errores y completos. Deben documentarse las practicas de gobernanza de datos, incluyendo el proposito de la recopilacion, los procesos de preparacion y las medidas para detectar sesgos.

En un contexto SOC, esto significa que los modelos de deteccion de amenazas deben entrenarse con datasets que representen adecuadamente el panorama de amenazas actual. Un modelo entrenado solo con amenazas de 2023 no cumple el requisito de representatividad en 2026.

### Documentacion tecnica

Antes de comercializar un sistema de IA de alto riesgo, el proveedor debe elaborar documentacion tecnica detallada (articulo 11) que demuestre el cumplimiento de todos los requisitos. Esta documentacion debe incluir:

- Descripcion general del sistema y su proposito.
- Descripcion detallada de los elementos del sistema y su proceso de desarrollo.
- Informacion sobre los datos de entrenamiento, validacion y prueba.
- Metricas de rendimiento y limitaciones conocidas.
- Descripcion de las medidas de supervision humana.

### Registro automatico de actividad (logging)

El articulo 12 requiere que los sistemas de IA de alto riesgo incluyan capacidades de logging que permitan la trazabilidad de su funcionamiento. Los registros deben permitir identificar situaciones de riesgo, facilitar la monitorizacion post-despliegue y asistir en investigaciones de conformidad.

Para equipos de ciberseguridad, este requisito es natural: el logging exhaustivo ya es una practica estandar. La diferencia es que ahora el logging de los propios sistemas de IA de seguridad tiene un marco legal que define que debe registrarse y durante cuanto tiempo.

### Transparencia e informacion

Los usuarios de sistemas de IA de alto riesgo deben recibir informacion suficiente para interpretar los resultados del sistema y usarlo de forma apropiada (articulo 13). Esto incluye informacion sobre el nivel de precision, robustez y ciberseguridad del sistema.

### Supervision humana

El articulo 14 establece que los sistemas de IA de alto riesgo deben disenarse para permitir una supervision humana efectiva. Esto no significa simplemente que un humano pueda pulsar un boton de apagado. Implica que:

- Las personas encargadas de supervisar el sistema deben poder comprender sus capacidades y limitaciones.
- Deben poder interpretar correctamente los resultados del sistema.
- Deben poder decidir no usar el sistema o ignorar sus resultados.
- Deben poder intervenir o detener el sistema en cualquier momento.

En un SOC, esto tiene implicaciones directas sobre el grado de automatizacion permisible. Un sistema que automatiza completamente la respuesta a incidentes sin ninguna supervision humana en decisiones de alto riesgo (por ejemplo, aislar un servidor de produccion critico) podria no cumplir este requisito.

### Precision, robustez y ciberseguridad

El articulo 15 es el que mas directamente concierne a los profesionales de ciberseguridad. Exige que los sistemas de IA de alto riesgo alcancen niveles apropiados de:

- **Precision**: el sistema debe funcionar segun lo previsto. Las metricas de rendimiento deben documentarse y comunicarse.
- **Robustez**: el sistema debe ser resiliente frente a errores, fallos, inconsistencias y situaciones inesperadas. Debe incluir medidas de redundancia y mecanismos fail-safe.
- **Ciberseguridad**: el sistema debe protegerse frente a ataques que intenten manipular su comportamiento. Esto incluye proteccion contra data poisoning, adversarial examples, model extraction y otros ataques especificos a sistemas de IA.

## Como afecta el AI Act a los equipos de ciberseguridad en la practica

Vamos a lo concreto. Estos son los escenarios practicos donde el AI Act impacta directamente en las operaciones de seguridad.

### IA en el SOC: deteccion y triage

Los SOC modernos utilizan IA de multiples formas:

- **Deteccion de anomalias** en trafico de red mediante modelos de machine learning.
- **Correlacion automatizada de eventos** en plataformas SIEM con capacidades de IA.
- **Triage automatizado** de alertas mediante clasificadores que priorizan por severidad.
- **Analisis de comportamiento de usuarios** (UEBA) para detectar amenazas internas.

La clasificacion de riesgo de estos sistemas depende del contexto. Si el SOC protege infraestructura critica (energia, transporte, salud, finanzas), los sistemas de IA utilizados probablemente se clasifiquen como alto riesgo. Si protege una empresa de comercio electronico, podrian quedar en riesgo limitado o minimo.

La recomendacion practica es asumir el peor caso y prepararse para cumplir los requisitos de alto riesgo. El coste de estar preparado es significativamente menor que el de una sancion por incumplimiento.

### IA en GRC: evaluacion de riesgos y compliance

Las plataformas GRC modernas incorporan IA para:

- **Evaluacion automatizada de riesgos** basada en datos historicos y contexto sectorial.
- **Mapeo automatico de controles** entre diferentes frameworks (ENS, NIS2, ISO 27001, DORA).
- **Priorizacion de hallazgos** de auditorias mediante scoring automatizado.
- **Generacion de informes** de compliance con lenguaje natural.

Cuando estos sistemas toman decisiones o generan recomendaciones que influyen directamente en la postura de seguridad de una organizacion regulada, pueden clasificarse como alto riesgo. Un sistema de IA que recomienda no aplicar un parche critico porque su analisis de riesgos automatizado lo considera bajo riesgo esta tomando una decision con implicaciones de seguridad significativas.

### IA en CTI: inteligencia de amenazas

Los equipos de Cyber Threat Intelligence usan IA para:

- **Clasificacion automatica de indicadores de compromiso** (IoCs).
- **Analisis de malware** mediante modelos de machine learning.
- **Correlacion de campanas de amenazas** usando procesamiento de lenguaje natural.
- **Prediccion de tendencias de amenazas** basada en datos historicos.

Estos sistemas generalmente se clasifican como riesgo limitado o minimo, salvo que operen en el contexto de infraestructuras criticas o aplicacion de la ley.

### Impacto en proveedores de herramientas de seguridad

Si tu organizacion desarrolla herramientas de seguridad con IA (SIEM, SOAR, EDR, XDR con capacidades de machine learning), el AI Act te afecta como proveedor. Debes:

- Clasificar el riesgo de cada producto.
- Cumplir los requisitos aplicables a tu categoria de riesgo.
- Proporcionar documentacion tecnica a tus clientes.
- Implementar sistemas de gestion de calidad.
- Someterte a evaluaciones de conformidad cuando sea necesario.

{{< cta type="tofu" text="Riskitera evalua tu postura de seguridad y te muestra los gaps de cumplimiento del AI Act, ENS y NIS2 en minutos." label="Evaluar postura" >}}

## Timeline del EU AI Act: fechas clave para equipos de seguridad

El AI Act sigue un calendario de aplicacion escalonado. Estas son las fechas que todo CISO y responsable de seguridad debe tener marcadas.

### Febrero 2025: prohibiciones activas

Desde el 2 de febrero de 2025, las practicas de IA prohibidas (riesgo inaceptable) ya son de obligado cumplimiento. Si tu organizacion utiliza algun sistema de IA que cae en esta categoria, debe haberse retirado antes de esta fecha. Revisa especialmente:

- Sistemas de videovigilancia con reconocimiento facial en tiempo real (excepto los supuestos tasados).
- Herramientas de analisis de comportamiento que puedan inferir emociones en el ambito laboral.
- Cualquier forma de puntuacion social aplicada a empleados o clientes.

### Agosto 2025: obligaciones GPAI

Desde el 2 de agosto de 2025, se aplican las obligaciones para modelos de IA de proposito general (GPAI, General Purpose AI). Esto afecta a los proveedores de modelos fundacionales como GPT, Claude, Gemini, Llama, Mistral y similares. Para los equipos de seguridad, las implicaciones son:

- Los proveedores de modelos GPAI deben proporcionar documentacion tecnica y resumen del contenido usado para entrenar el modelo.
- Los modelos GPAI con riesgo sistemico (aquellos entrenados con mas de 10^25 FLOPs) tienen obligaciones adicionales de evaluacion y mitigacion de riesgos.
- Si usas modelos GPAI como parte de tu stack de seguridad (por ejemplo, LLMs para analisis de logs o generacion de informes), debes verificar que tu proveedor cumple estas obligaciones.

### Agosto 2026: cumplimiento completo

El 2 de agosto de 2026 es la fecha de aplicacion completa del AI Act. A partir de esta fecha, todos los requisitos para sistemas de IA de alto riesgo estan en vigor. Esto significa:

- Los sistemas de IA de alto riesgo que se comercialicen o desplieguen deben cumplir todos los requisitos del reglamento.
- Los proveedores deben tener implementados sus sistemas de gestion de calidad.
- Las evaluaciones de conformidad deben estar completadas.
- La documentacion tecnica debe estar disponible.

### Agosto 2027: obligaciones adicionales para ciertos sistemas de alto riesgo

Los sistemas de IA de alto riesgo que son componentes de seguridad de productos ya regulados (por ejemplo, dispositivos medicos, vehiculos, aviacion) tienen hasta el 2 de agosto de 2027 para cumplir.

## Relacion del AI Act con ENS, NIS2 y DORA

El AI Act no opera en solitario. Para organizaciones en Espana y la UE, la interseccion con otras normativas de seguridad crea un panorama regulatorio complejo pero coherente.

### AI Act y ENS (Esquema Nacional de Seguridad)

El [ENS](https://ens.ccn.cni.es/) establece los principios basicos y requisitos minimos de seguridad para los sistemas de informacion del sector publico espanol y sus proveedores. Cuando una administracion publica o su cadena de suministro despliega sistemas de IA, el AI Act se superpone al ENS:

- **Gestion de riesgos**: ambos requieren analisis de riesgos, pero el AI Act anade requisitos especificos para riesgos derivados de la IA (sesgos, robustez, ataques adversariales).
- **Trazabilidad**: el ENS ya exige logging extenso, lo que facilita el cumplimiento del articulo 12 del AI Act.
- **Supervision**: el ENS categoriza los sistemas por nivel de seguridad (bajo, medio, alto), lo que puede complementar la clasificacion de riesgo del AI Act.

### AI Act y NIS2

La [Directiva NIS2](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive) establece obligaciones de ciberseguridad para entidades esenciales e importantes. Su interseccion con el AI Act es particularmente relevante porque:

- Muchas entidades cubiertas por NIS2 (energia, transporte, salud, infraestructuras digitales) son exactamente los sectores donde el AI Act clasifica sistemas como alto riesgo.
- NIS2 exige gestion de riesgos de seguridad de la cadena de suministro, lo que incluye evaluar los riesgos de los sistemas de IA proporcionados por terceros.
- Los requisitos de notificacion de incidentes de NIS2 se aplican tambien a incidentes que involucren sistemas de IA.

### AI Act y DORA

El [Reglamento DORA](https://www.digital-operational-resilience-act.com/) se centra en la resiliencia operativa digital del sector financiero. Para bancos, aseguradoras y gestoras de activos que usan IA:

- DORA exige pruebas de resiliencia operativa que ahora deben incluir los sistemas de IA criticos.
- Los acuerdos con proveedores de servicios TIC (incluidos proveedores de IA) deben cumplir requisitos especificos de DORA.
- La gestion de riesgos de terceros bajo DORA debe considerar los riesgos especificos de los sistemas de IA utilizados.

## Checklist del CISO para el EU AI Act

Esta es una guia practica para que los CISOs y responsables de seguridad preparen su organizacion.

### Fase 1: inventario y clasificacion (hacer ahora)

1. **Inventariar todos los sistemas de IA** en uso en la organizacion. No solo los que el equipo de seguridad utiliza, sino todos los que la organizacion ha desplegado. Incluir:
   - Herramientas de seguridad con componentes de IA (SIEM, SOAR, EDR, XDR, UEBA).
   - Sistemas de GRC con capacidades de IA.
   - Chatbots y asistentes virtuales.
   - Herramientas de productividad con IA integrada (Copilot, asistentes de codigo).
   - Modelos de IA desarrollados internamente.

2. **Clasificar cada sistema** segun las categorias de riesgo del AI Act. Documentar la justificacion de cada clasificacion.

3. **Identificar proveedores** de sistemas de IA y verificar su postura de cumplimiento del AI Act.

### Fase 2: gap analysis (Q3 2026)

4. **Evaluar el cumplimiento actual** de cada sistema de alto riesgo contra los requisitos del AI Act.
5. **Documentar gaps** y crear un plan de remediacion priorizado.
6. **Revisar contratos con proveedores** para incluir clausulas de cumplimiento del AI Act.
7. **Evaluar la capacidad interna** de supervision humana de los sistemas de IA.

### Fase 3: implementacion (Q4 2026)

8. **Implementar controles** para los gaps identificados.
9. **Establecer procesos de gobernanza** de IA que integren los requisitos del AI Act con los frameworks existentes (ENS, NIS2, ISO 27001).
10. **Formar al equipo** en los requisitos del AI Act y en las responsabilidades especificas de cada rol.
11. **Implementar o mejorar el logging** de los sistemas de IA para cumplir el articulo 12.

### Fase 4: monitorizacion continua (permanente)

12. **Establecer un proceso de monitorizacion post-despliegue** para todos los sistemas de IA de alto riesgo.
13. **Integrar la gestion de riesgos de IA** en el ciclo de gestion de riesgos corporativo.
14. **Auditar periodicamente** el cumplimiento de los requisitos del AI Act.
15. **Mantener actualizada la documentacion tecnica** ante cambios en los sistemas de IA.

## Impacto en herramientas de seguridad con IA

El mercado de herramientas de ciberseguridad esta en plena transformacion por el AI Act. Estos son los cambios concretos que ya se estan produciendo.

### SIEM con IA

Los principales proveedores de SIEM (Splunk, Microsoft Sentinel, Elastic Security, QRadar) estan actualizando sus productos para cumplir los requisitos del AI Act. Los cambios incluyen:

- Mayor transparencia en los modelos de deteccion: los proveedores deben explicar como funcionan sus algoritmos de correlacion y deteccion de anomalias.
- Mejoras en el logging de decisiones de la IA: cada alerta generada por un modelo de IA debe incluir informacion sobre la confianza del modelo y los factores que contribuyeron a la decision.
- Opciones de supervision humana mejoradas: interfaces que permiten a los analistas entender, cuestionar y anular las decisiones de la IA.

### EDR/XDR con IA

Las plataformas de deteccion y respuesta (CrowdStrike Falcon, SentinelOne, Microsoft Defender) utilizan extensivamente IA para deteccion de malware, analisis de comportamiento y respuesta automatizada. El AI Act les exige:

- Documentar los datasets de entrenamiento de sus modelos de deteccion.
- Proporcionar metricas de precision (falsos positivos, falsos negativos) verificables.
- Garantizar que las acciones de respuesta automatizada cuentan con mecanismos de supervision humana adecuados.

### SOAR con IA

Las plataformas de orquestacion y respuesta automatizada (Palo Alto XSOAR, Splunk SOAR, Swimlane) que incorporan decision-making basado en IA deben:

- Permitir que los playbooks automatizados incluyan puntos de decision humana en acciones de alto impacto.
- Documentar la logica de decision de los componentes de IA.
- Proporcionar trazabilidad completa de cada accion ejecutada por la IA.

## Sanciones por incumplimiento

El regimen sancionador del AI Act es significativo y proporcional a la gravedad de la infraccion:

- **Practicas prohibidas**: hasta 35 millones de euros o el 7% de la facturacion anual global (lo que sea mayor).
- **Incumplimiento de requisitos de alto riesgo**: hasta 15 millones de euros o el 3% de la facturacion anual global.
- **Informacion incorrecta**: hasta 7,5 millones de euros o el 1,5% de la facturacion anual global.

Para PYMEs y startups, las multas se calculan sobre la base del porcentaje de facturacion, lo que proporciona cierta proporcionalidad. No obstante, incluso una sancion del 3% puede ser existencial para una empresa pequena.

Las autoridades nacionales de supervision (en Espana, la [AEPD](https://www.aepd.es/) tiene un papel coordinador junto con la futura Agencia Espanola de Supervision de la IA) tendran potestad para:

- Realizar inspecciones.
- Exigir acceso a la documentacion tecnica.
- Ordenar la retirada de sistemas de IA no conformes del mercado.
- Imponer sanciones economicas.

{{< cta type="bofu" text="Empieza tu PoC de 90 dias con Riskitera y automatiza el compliance del AI Act, ENS y NIS2 desde el primer dia." label="Iniciar PoC" >}}

## Recomendaciones practicas para equipos de ciberseguridad

### Para organizaciones que usan IA en seguridad

1. **No esperes a agosto de 2026**. El inventario y la clasificacion de sistemas de IA deben empezar ya. El esfuerzo de documentacion y adaptacion es significativo.

2. **Integra el AI Act en tu marco de compliance existente**. Si ya cumples ENS Alto o ISO 27001, tienes una base solida. Los controles de gestion de riesgos, logging, documentacion y supervision humana ya estan parcialmente cubiertos.

3. **Exige informacion a tus proveedores**. Pregunta a tus proveedores de herramientas de seguridad como estan adaptando sus productos al AI Act. Pide documentacion tecnica, metricas de rendimiento y hojas de ruta de cumplimiento.

4. **Forma a tus analistas SOC**. Los analistas que supervisan sistemas de IA deben entender las capacidades y limitaciones de estos sistemas. La supervision humana efectiva requiere conocimiento tecnico.

5. **Revisa tus playbooks de respuesta automatizada**. Identifica donde la IA toma decisiones criticas sin supervision humana y anade checkpoints de validacion humana donde sea necesario.

### Para proveedores de herramientas de seguridad

1. **Clasificad vuestros productos**. Determinad en que categoria de riesgo cae cada producto segun el contexto de uso.

2. **Documentad todo**. La documentacion tecnica exigida por el AI Act debe ser exhaustiva: arquitectura, datos de entrenamiento, metricas de rendimiento, limitaciones conocidas, medidas de seguridad.

3. **Implementad explainability**. Los clientes necesitan entender por que la IA toma cada decision. Esto no significa que los modelos deban ser interpretables (glass box), pero si que cada resultado debe acompanarse de informacion contextual suficiente.

4. **Preparad las evaluaciones de conformidad**. Para sistemas de alto riesgo, necesitareis someteros a evaluaciones de conformidad por organismos notificados.

## Recursos y organismos de referencia

Para mantenerse actualizado sobre el EU AI Act y su aplicacion en ciberseguridad:

- **[ENISA](https://www.enisa.europa.eu/)**: la Agencia de la UE para la Ciberseguridad publica guias y analisis sobre la interseccion entre IA y ciberseguridad.
- **[AI Office de la Comision Europea](https://digital-strategy.ec.europa.eu/en/policies/ai-office)**: responsable de supervisar los modelos GPAI y coordinar la aplicacion del AI Act.
- **[CCN-CERT](https://www.ccn-cert.cni.es/)**: en el ambito espanol, el Centro Criptologico Nacional publica guias de seguridad que iran incorporando los requisitos del AI Act.
- **[INCIBE](https://www.incibe.es/)**: el Instituto Nacional de Ciberseguridad ofrece recursos y formacion sobre seguridad, incluyendo aspectos relacionados con IA.
- **Texto completo del reglamento**: [EUR-Lex 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689).


**Articulos relacionados:**
- [Nis2 Que Es A Quien Afecta](/es/posts/2026/04/nis2-que-es-a-quien-afecta/)

## Preguntas frecuentes

### El EU AI Act obliga a dejar de usar IA en el SOC?

No. El AI Act no prohibe el uso de IA en operaciones de seguridad. Lo que hace es establecer requisitos segun el nivel de riesgo del sistema. Los equipos SOC pueden seguir usando herramientas de deteccion, triage y respuesta basadas en IA, pero deben garantizar que cumplen los requisitos de transparencia, supervision humana, logging y documentacion aplicables a su categoria de riesgo. En la mayoria de los casos, esto supone mejorar practicas ya existentes, no eliminar herramientas.

### Que pasa si mi proveedor de SIEM o EDR no cumple el AI Act?

Si despliegas un sistema de IA que no cumple el AI Act, la responsabilidad recae tanto en el proveedor (como desarrollador del sistema) como en tu organizacion (como deployer o usuario). El reglamento establece obligaciones diferenciadas para proveedores y usuarios. Como usuario, debes verificar que tus proveedores cumplen, exigir la documentacion tecnica necesaria y mantener registros de tu diligencia debida. Si un proveedor no demuestra cumplimiento antes de agosto de 2026, deberias evaluar alternativas.

### Como clasifico la IA de mi SOC: alto riesgo o riesgo limitado?

La clasificacion depende del contexto de uso, no de la tecnologia en si. Un mismo sistema de deteccion de anomalias puede ser de alto riesgo si protege una infraestructura critica (hospital, central electrica, red de transporte) y de riesgo limitado si protege una empresa de comercio electronico. La clave esta en revisar el Anexo III del reglamento e identificar si el uso de tu sistema entra en alguna de las categorias listadas. Ante la duda, clasifica como alto riesgo: cumplir requisitos superiores nunca es un problema regulatorio.

### El AI Act afecta a los modelos de IA open source que uso en mi SOC?

Si. El AI Act se aplica independientemente de si el modelo es propietario u open source. Si despliegas un modelo open source (por ejemplo, un modelo de deteccion de malware basado en un modelo fundacional abierto), eres responsable de cumplir los requisitos aplicables como deployer. Los proveedores de modelos GPAI open source tienen ciertas exenciones (no necesitan proporcionar documentacion tecnica tan exhaustiva si el modelo se distribuye con licencia libre), pero estas exenciones no se extienden a los usuarios que despliegan el modelo en contextos de alto riesgo.

### Cuanto cuesta adaptarse al EU AI Act para un equipo de seguridad tipico?

El coste depende enormemente del tamano de la organizacion, del numero de sistemas de IA en uso y del nivel de madurez actual en gobernanza de IA. Para una organizacion mediana (500-2000 empleados) con un SOC que utiliza 3-5 herramientas con componentes de IA, la estimacion realista incluye: inventario y clasificacion (2-4 semanas de trabajo de consultoria), gap analysis (4-8 semanas), implementacion de controles adicionales (variable, pero tipicamente 3-6 meses), y formacion del equipo (1-2 semanas). En terminos economicos, el rango tipico es de 50.000 a 200.000 euros para el proyecto inicial de adaptacion, mas un coste recurrente de mantenimiento del 10-15% anual.
