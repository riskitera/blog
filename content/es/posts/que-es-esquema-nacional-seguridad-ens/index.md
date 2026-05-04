---
title: "Que es el Esquema Nacional de Seguridad (ENS): guía completa 2026"
image: "cover.png"
description: "Todo lo que necesitas saber sobre el Esquema Nacional de Seguridad (ENS): niveles de seguridad, quien debe cumplirlo, medidas clave y pasos para implementarlo en tu organización."
slug: "que-es-esquema-nacional-seguridad-ens"
date: 2026-02-28
lastmod: 2026-02-28
draft: false
tags: ["ENS", "Compliance", "Seguridad"]
categories: ["Compliance"]
author: "David Moya"
translationKey: "ens-guide"
---

El Esquema Nacional de Seguridad (ENS) es el marco normativo que establece los principios y requisitos mínimos de seguridad de la información para el sector público español y para cualquier entidad que preste servicios o gestione soluciones tecnológicas para la Administración. Regulado por el [Real Decreto 311/2022](https://www.boe.es/eli/es/rd/2022/05/03/311), su cumplimiento no es opcional: es una obligación legal que afecta a miles de organizaciones en España.

<!--more-->

{{< key-takeaways >}}
- El ENS es obligatorio para el sector público español y sus proveedores tecnológicos (RD 311/2022)
- Tres niveles de seguridad (bajo, medio, alto) con 36, 58 y 73 medidas respectivamente
- La certificación se renueva cada 2 años mediante auditoría externa acreditada
- El CCN-CERT proporciona herramientas oficiales (PILAR) y guías CCN-STIC para la implementación
- El ENS se alinea con ISO 27001, NIS2 y DORA, facilitando el cumplimiento cruzado
{{< /key-takeaways >}}

## Qué es el Esquema Nacional de Seguridad (ENS)?

El ENS es una normativa española que define la política de seguridad en la utilización de medios electrónicos en el ámbito del sector público. Su objetivo es crear las condiciones necesarias de confianza en el uso de los medios electrónicos, estableciendo medidas de seguridad para garantizar la confidencialidad, integridad, disponibilidad, autenticidad y trazabilidad de la información.

Publicado originalmente en 2010 mediante el Real Decreto 3/2010, el ENS ha evolucionado significativamente. La versión vigente, aprobada por el Real Decreto 311/2022, incorpora lecciones aprendidas de más de una decada de aplicación y adapta el marco a las amenazas actuales del panorama de ciberseguridad.

El Centro Criptologico Nacional ([CCN-CERT](https://www.ccn-cert.cni.es/)), adscrito al Centro Nacional de Inteligencia (CNI), es el organismo encargado de velar por el cumplimiento del ENS y de publicar las guías técnicas [CCN-STIC](https://www.ccn-cert.cni.es/series-ccn-stic.html) que detallan como implementar cada medida de seguridad.

## Cómo ha evolucionado el ENS desde 2010?

La primera versión del ENS nacio al amparo de la Ley 11/2007 de acceso electrónico de los ciudadanos a los servicios públicos. En aquel momento, la digitalización del sector público estaba en sus inicios y la normativa buscaba establecer unas bases mínimas de seguridad.

En 2015 se público una actualización menor mediante el Real Decreto 951/2015, que ajusto algunos aspectos técnicos. Sin embargo, el cambio verdaderamente significativo llego en mayo de 2022 con el Real Decreto 311/2022, que derogo la normativa anterior y estableció un marco completamente renovado.

Las principales novedades del ENS 2022 incluyen:

- **Perfiles de cumplimiento específicos**: el CCN ha definido perfiles de cumplimiento que simplifican la adopción del ENS para tipos concretos de organizaciones, como ayuntamientos, universidades o proveedores tecnológicos.
- **Vigilancia continúa y respuesta a incidentes**: se refuerza la obligación de monitorizar los sistemas de forma permanente y de notificar incidentes al CCN-CERT.
- **Interconexion con marcos europeos**: se alinea el ENS con normativas europeas como el Reglamento eIDAS y la Directiva [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555).
- **Gestión de la cadena de suministro**: se exige a las Administraciones que sus proveedores tecnológicos también cumplan con el ENS.

## Cuáles son los niveles de seguridad del ENS: alto, medio y bajo?

El ENS clasifica los sistemas de información en tres categorías en función del impacto que tendría un incidente de seguridad sobre las dimensiones de seguridad (confidencialidad, integridad, disponibilidad, autenticidad y trazabilidad).

### Nivel bajo

Un sistema se clasifica como nivel bajo cuando un incidente de seguridad tendría un impacto limitado sobre las funciones de la organización, los activos o los individuos afectados. Ejemplo típico: un portal web informativo de un ayuntamiento que no gestiona datos personales sensibles.

Las medidas exigidas en nivel bajo son proporcionadas: política de seguridad básica, control de acceso, protección frente a malware, copias de seguridad y un plan de respuesta a incidentes elemental. Son 36 medidas de seguridad aplicables.

### Nivel medio

Se aplica cuando el impacto de un incidente sería grave para las funciones, los activos o los individuos. Es el nivel más común en la Administración pública. Ejemplo: una plataforma de tramitación electrónica que gestiona datos personales o información administrativa.

El nivel medio incrementa sustancialmente las exigencias: gestión formal de riesgos, segregación de funciones, sistemas de detección de intrusiones, auditorías periódicas y formación específica del personal. El número de medidas aplicables asciende a 58.

### Nivel alto

Se reserva para sistemas cuyo compromiso tendría un impacto muy grave o catastrófico. Ejemplo: sistemas que gestionan información clasificada, infraestructuras críticas del Estado o datos especialmente sensibles.

El nivel alto exige las medidas más rigurosas: cifrado robusto de datos en reposo y tránsito, monitorización continua 24/7, planes de continuidad de negocio, segmentación avanzada de redes, y auditorías externas anuales. Se aplican las 73 medidas del ENS.

Según datos del CCN, en 2025 el 47 por ciento de las certificaciones ENS correspondieron al nivel medio, el 31 por ciento al nivel alto y el 22 por ciento al nivel bajo.

## Quien está obligado a cumplir el ENS?

El ámbito de aplicación del ENS es amplio y no se limita al sector público en sentido estricto:

- **Administración General del Estado** (ministerios, organismos autónomos, agencias estatales).
- **Administraciones autonomicas y locales** (comunidades autónomas, diputaciones, ayuntamientos).
- **Universidades públicas**.
- **Entidades de derecho público** vinculadas a las Administraciones.
- **Proveedores del sector público**: cualquier empresa que preste servicios tecnológicos, gestione sistemas de información o trate datos en nombre de una Administración pública debe cumplir el ENS en la medida que corresponda al servicio prestado.
- **Operadores del sector privado** que gestionen información clasificada o presten servicios esenciales vinculados al sector público.

Este último punto es especialmente relevante: si tu empresa desarrolla software para la Administración, ofrece servicios cloud a un organismo público o gestiona la infraestructura TIC de un ayuntamiento, necesitas cumplir con el ENS.

El CCN estima que más de 15.000 entidades en España están sujetas al cumplimiento del ENS, aunque el número de certificaciones activas a finales de 2025 rondaba las 3.200, lo que indica que todavia existe un margen significativo de mejora.

## Cuáles son las medidas de seguridad clave del ENS?

El ENS organiza sus medidas de seguridad en tres marcos:

### Marco organizativo

Define las políticas y procedimientos de gobernanza de la seguridad:

- **Política de seguridad**: documento aprobado por la dirección que establece el compromiso con la seguridad y asigna roles y responsabilidades.
- **Normativa de seguridad**: conjunto de normas internas que regulan el uso de los sistemas de información.
- **Procedimientos de seguridad**: instrucciones detalladas para la ejecución de tareas de seguridad.
- **Proceso de autorización**: mecanismo formal para autorizar nuevos sistemas o cambios significativos.

### Marco operacional

Abarca las medidas técnicas y procedimentales del día a día:

- **Planificación**: análisis de riesgos, arquitectura de seguridad y adquisición de componentes.
- **Control de acceso**: identificación, autenticación, mecanismo de acceso y segregación de funciones.
- **Explotación**: inventario de activos, gestión de configuración, mantenimiento, gestión de cambios, protección frente a código danino y gestión de incidentes.
- **Servicios externos**: contratación, acuerdos de nivel de servicio y seguimiento continuo de proveedores.
- **Continuidad del servicio**: planes de continuidad, pruebas periódicas y gestión de crisis.
- **Monitorización del sistema**: detección de intrusiones, registros de actividad y métricas de seguridad.

### Medidas de protección

Se centran en la protección técnica de los activos:

- Protección de las comunicaciones (cifrado, cortafuegos, segmentación de redes).
- Protección de los soportes de información.
- Protección de las aplicaciones informáticas (desarrollo seguro, pruebas de seguridad).
- Protección de la información (clasificación, cifrado en reposo, copias de seguridad).
- Protección de los servicios (disponibilidad, protección frente a denegación de servicio).

## Cómo se implementa el ENS paso a paso?

La implementación del ENS es un proceso estructurado que, dependiendo del tamaño de la organización y del nivel de seguridad requerido, puede llevar entre 6 y 18 meses. Estos son los pasos fundamentales:

### 1. Compromiso de la dirección y designación de roles

Sin el apoyo explícito de la alta dirección, el proyecto fracasara. Es necesario designar al Responsable de la Información, al Responsable del Servicio y al Responsable de la Seguridad, tal como exige el ENS. En organizaciones con nivel alto, estas tres figuras deben ser personas distintas.

### 2. Determinación del alcance y categorization del sistema

Identifica los servicios y sistemas de información que entran en el ámbito del ENS. Para cada uno, evalúa las dimensiones de seguridad y determina la categoría (baja, media o alta). El CCN proporciona la herramienta PILAR para facilitar este análisis.

### 3. Análisis de riesgos

Realiza un análisis de riesgos formal siguiendo una metodología reconocida. [MAGERIT](https://www.ccn-cert.cni.es/herramientas-de-ciberseguridad/ear-pilar.html) es la metodología de referencia en el contexto español y esta plenamente alineada con el ENS. Identifica activos, amenazas, vulnerabilidades y calcula el riesgo residual.

### 4. Declaración de aplicabilidad

Documenta que medidas del ENS son aplicables a tu sistema, cuales no lo son y la justificación en cada caso. Esta declaración es un documento clave para la auditoría de certificación.

### 5. Implementación de medidas

Despliega las medidas técnicas, organizativas y operacionales que correspondan según la categoría del sistema. Apoyate en las guías CCN-STIC del CCN, que ofrecen instrucciones detalladas para cada medida.

### 6. Formación y concienciación

Forma al personal en sus responsabilidades de seguridad. El CCN ofrece a través de su plataforma Angeles recursos formativos específicos para el ENS. La formación no es un evento puntual, sino un proceso continuo.

### 7. Auditoría y certificación

Una vez implementadas las medidas, somete el sistema a una auditoría de cumplimiento. Para sistemas de nivel medio y alto, la auditoría debe ser realizada por una entidad independiente acreditada. Tras superar la auditoría, se obtiene la certificación de conformidad con el ENS, que debe renovarse cada dos años.

Si tu organización busca optimizar este proceso, plataformas como Riskitera automatizan gran parte de la gestión documental, el seguimiento de medidas y la preparación para la auditoría, reduciendo significativamente el esfuerzo manual y los plazos de implementación.

{{< cta type="tofu" text="Implementar el ENS requiere mapear medidas a controles reales. Riskitera automatiza este proceso con IA." label="Ver demo ENS" >}}

## Cómo se relaciona el ENS con ISO 27001, NIS2 y DORA?

El ENS no existe de forma aislada. Forma parte de un ecosistema normativo cada vez más interconectado:

- **[ISO 27001](https://www.iso.org/standard/27001)**: el ENS y la ISO 27001 comparten muchos conceptos y controles. Una organización certificada en ISO 27001 tiene gran parte del camino recorrido para el ENS, aunque hay medidas específicas del ENS que la ISO no cubre. Si estas valorando implementar ISO 27001 en tu organización, te recomendamos nuestra [guía práctica de ISO 27001 para startups](/es/posts/2026/02/guia-iso-27001-startups/).
- **[NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555)**: la Directiva europea NIS2 afecta a entidades esenciales e importantes en toda la Union Europea. En España, el ENS actuara como vehículo para implementar parte de los requisitos de NIS2 en el sector público. En próximos artículos analizaremos en detalle [qué es la NIS2 y a quien afecta](/es/posts/2026/04/nis2-que-es-a-quien-afecta/).
- **[DORA](https://eur-lex.europa.eu/eli/reg/2022/2554)**: el Reglamento de Resiliencia Operativa Digital afecta al sector financiero europeo. Las entidades financieras sujetas a DORA que también trabajan con la Administración pública podrían necesitar cumplir con ambos marcos. Publicaremos proximamente una guía completa sobre [DORA y la ciberseguridad financiera](/es/posts/2026/04/dora-reglamento-ciberseguridad-financiera/).
- **[RGPD](https://eur-lex.europa.eu/eli/reg/2016/679)**: el cumplimiento del ENS contribuye a satisfacer los requisitos de seguridad del Reglamento General de Protección de Datos, aunque no lo sustituye.

## Qué beneficios aporta la certificación ENS?

Más allá del cumplimiento legal, la certificación ENS aporta ventajas tangibles:

- **Acceso a contratos públicos**: cada vez más licitaciones exigen la certificación ENS como requisito de solvencia técnica.
- **Reducción del riesgo de incidentes**: las organizaciones certificadas reportan un 43 por ciento menos de incidentes graves, según datos de [INCIBE](https://www.incibe.es/) correspondientes a 2024.
- **Confianza institucional**: la certificación es una señal clara de madurez en seguridad ante organismos públicos y socios comerciales.
- **Mejora operativa**: el proceso de implementación obliga a documentar, racionalizar y optimizar los procesos de gestión de la seguridad.
- **Preparación para otras normativas**: facilita la adaptación a NIS2, DORA y otros marcos regulatorios europeos.

## Cuáles son los errores más comunes al implementar el ENS?

Basandonos en la experiencia del sector, estos son los errores más frecuentes:

- **Tratar el ENS como un proyecto exclusivamente tecnologico**: el ENS exige medidas organizativas y de gobernanza que van más allá de la tecnología.
- **Subestimar la gestión documental**: la documentación es un pilar fundamental del ENS. Sin políticas, normas y procedimientos formalizados, la auditoría no se supera.
- **Ignorar la cadena de suministro**: desde el RD 311/2022, los proveedores deben cumplir con el ENS. No verificar su cumplimiento es un riesgo y un incumplimiento.
- **No asignar recursos suficientes**: la implementación requiere dedicación. Intentar hacerlo sin personal dedicado ni presupuesto adecuado es una receta para el fracaso.
- **Categorizar incorrectamente el sistema**: una categorización erronea, ya sea por exceso o por defecto, genera problemas en la auditoría y en la operación.

{{< cta type="mofu" text="Prepara tu organización para la certificación ENS con una plataforma que gestiona controles, evidencias y auditorías." >}}

## Preguntas frecuentes

### Es obligatorio el ENS para las empresas privadas?

El ENS es directamente obligatorio para el sector público. Las empresas privadas deben cumplirlo cuando prestan servicios tecnológicos a la Administración, gestionan sistemas de información del sector público o tratan datos en nombre de una entidad pública. Si tu empresa tiene contratos con la Administración que implican el manejo de información o sistemas, muy probablemente necesitas cumplir con el ENS.

### Cuánto cuesta obtener la certificación ENS?

El coste varía enormemente según el tamaño de la organización y el nivel de seguridad. Para una pyme que busca la certificación en nivel medio, el coste total (consultoría, implementación de medidas y auditoría) suele oscilar entre 25.000 y 80.000 euros. Para nivel alto en organizaciones grandes, la inversión puede superar los 200.000 euros. Las herramientas de automatización GRC como Riskitera pueden reducir estos costes significativamente al eliminar trabajo manual repetitivo.

### Cuál es la diferencia entre el ENS y la ISO 27001?

La ISO 27001 es un estándar internacional voluntario centrado en sistemas de gestión de seguridad de la información. El ENS es una normativa española obligatoria para el sector público con medidas de seguridad específicas y niveles de clasificación propios. Aunque comparten muchos principios, el ENS incluye requisitos concretos (como los perfiles de cumplimiento o la integración con las guías CCN-STIC) que la ISO 27001 no contempla. Muchas organizaciones optan por implementar ambos de forma coordinada.

### Cada cuanto hay que renovar la certificación ENS?

La certificación ENS tiene una validez de dos años. Al cabo de ese periodo, es necesario someterse a una nueva auditoría de renovación. Además, se requiere una vigilancia continua y, en caso de cambios significativos en los sistemas, puede ser necesaria una auditoría extraordinaria antes de que expire el plazo de dos años.

### Qué papel juega el CCN-CERT en el ENS?

El CCN-CERT (Centro Criptologico Nacional - Computer Emergency Response Team) es el equipo de respuesta a incidentes de seguridad de referencia para el sector público español. En el marco del ENS, el CCN-CERT pública las guías técnicas CCN-STIC, gestiona las herramientas oficiales como PILAR (análisis de riesgos) e INES (estado de cumplimiento del ENS), coordina la respuesta a incidentes y mantiene actualizado el catálogo de productos de seguridad certificados. Además, es el organismo ante el que las entidades públicas deben notificar los incidentes de seguridad.
