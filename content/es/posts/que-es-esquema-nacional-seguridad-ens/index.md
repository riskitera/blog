---
title: "Que es el Esquema Nacional de Seguridad (ENS): guia completa 2026"
description: "Todo lo que necesitas saber sobre el Esquema Nacional de Seguridad (ENS): niveles de seguridad, quien debe cumplirlo, medidas clave y pasos para implementarlo en tu organizacion."
slug: "que-es-esquema-nacional-seguridad-ens"
date: 2026-04-05
lastmod: 2026-04-05
draft: false
tags: ["ENS", "Compliance", "Seguridad"]
categories: ["Compliance"]
author: "Riskitera Team"
translationKey: "ens-guide"
---

El Esquema Nacional de Seguridad (ENS) es el marco normativo que establece los principios y requisitos minimos de seguridad de la informacion para el sector publico espanol y para cualquier entidad que preste servicios o gestione soluciones tecnologicas para la Administracion. Regulado por el Real Decreto 311/2022, su cumplimiento no es opcional: es una obligacion legal que afecta a miles de organizaciones en Espana.

<!--more-->

## Que es el Esquema Nacional de Seguridad

El ENS es una normativa espanola que define la politica de seguridad en la utilizacion de medios electronicos en el ambito del sector publico. Su objetivo es crear las condiciones necesarias de confianza en el uso de los medios electronicos, estableciendo medidas de seguridad para garantizar la confidencialidad, integridad, disponibilidad, autenticidad y trazabilidad de la informacion.

Publicado originalmente en 2010 mediante el Real Decreto 3/2010, el ENS ha evolucionado significativamente. La version vigente, aprobada por el Real Decreto 311/2022, incorpora lecciones aprendidas de mas de una decada de aplicacion y adapta el marco a las amenazas actuales del panorama de ciberseguridad.

El Centro Criptologico Nacional (CCN), adscrito al Centro Nacional de Inteligencia (CNI), es el organismo encargado de velar por el cumplimiento del ENS y de publicar las guias tecnicas CCN-STIC que detallan como implementar cada medida de seguridad.

## Historia y evolucion del ENS

La primera version del ENS nacio al amparo de la Ley 11/2007 de acceso electronico de los ciudadanos a los servicios publicos. En aquel momento, la digitalizacion del sector publico estaba en sus inicios y la normativa buscaba establecer unas bases minimas de seguridad.

En 2015 se publico una actualizacion menor mediante el Real Decreto 951/2015, que ajusto algunos aspectos tecnicos. Sin embargo, el cambio verdaderamente significativo llego en mayo de 2022 con el Real Decreto 311/2022, que derogo la normativa anterior y establecio un marco completamente renovado.

Las principales novedades del ENS 2022 incluyen:

- **Perfiles de cumplimiento especificos**: el CCN ha definido perfiles de cumplimiento que simplifican la adopcion del ENS para tipos concretos de organizaciones, como ayuntamientos, universidades o proveedores tecnologicos.
- **Vigilancia continua y respuesta a incidentes**: se refuerza la obligacion de monitorizar los sistemas de forma permanente y de notificar incidentes al CCN-CERT.
- **Interconexion con marcos europeos**: se alinea el ENS con normativas europeas como el Reglamento eIDAS y la Directiva NIS2.
- **Gestion de la cadena de suministro**: se exige a las Administraciones que sus proveedores tecnologicos tambien cumplan con el ENS.

## Niveles de seguridad: alto, medio y bajo

El ENS clasifica los sistemas de informacion en tres categorias en funcion del impacto que tendria un incidente de seguridad sobre las dimensiones de seguridad (confidencialidad, integridad, disponibilidad, autenticidad y trazabilidad).

### Nivel bajo

Un sistema se clasifica como nivel bajo cuando un incidente de seguridad tendria un impacto limitado sobre las funciones de la organizacion, los activos o los individuos afectados. Ejemplo tipico: un portal web informativo de un ayuntamiento que no gestiona datos personales sensibles.

Las medidas exigidas en nivel bajo son proporcionadas: politica de seguridad basica, control de acceso, proteccion frente a malware, copias de seguridad y un plan de respuesta a incidentes elemental. Son 36 medidas de seguridad aplicables.

### Nivel medio

Se aplica cuando el impacto de un incidente seria grave para las funciones, los activos o los individuos. Es el nivel mas comun en la Administracion publica. Ejemplo: una plataforma de tramitacion electronica que gestiona datos personales o informacion administrativa.

El nivel medio incrementa sustancialmente las exigencias: gestion formal de riesgos, segregacion de funciones, sistemas de deteccion de intrusiones, auditorias periodicas y formacion especifica del personal. El numero de medidas aplicables asciende a 58.

### Nivel alto

Se reserva para sistemas cuyo compromiso tendria un impacto muy grave o catastrofico. Ejemplo: sistemas que gestionan informacion clasificada, infraestructuras criticas del Estado o datos especialmente sensibles.

El nivel alto exige las medidas mas rigurosas: cifrado robusto de datos en reposo y transito, monitorizacion continua 24/7, planes de continuidad de negocio, segmentacion avanzada de redes, y auditorias externas anuales. Se aplican las 73 medidas del ENS.

Segun datos del CCN, en 2025 el 47 por ciento de las certificaciones ENS correspondieron al nivel medio, el 31 por ciento al nivel alto y el 22 por ciento al nivel bajo.

## Quien debe cumplir el ENS

El ambito de aplicacion del ENS es amplio y no se limita al sector publico en sentido estricto:

- **Administracion General del Estado** (ministerios, organismos autonomos, agencias estatales).
- **Administraciones autonomicas y locales** (comunidades autonomas, diputaciones, ayuntamientos).
- **Universidades publicas**.
- **Entidades de derecho publico** vinculadas a las Administraciones.
- **Proveedores del sector publico**: cualquier empresa que preste servicios tecnologicos, gestione sistemas de informacion o trate datos en nombre de una Administracion publica debe cumplir el ENS en la medida que corresponda al servicio prestado.
- **Operadores del sector privado** que gestionen informacion clasificada o presten servicios esenciales vinculados al sector publico.

Este ultimo punto es especialmente relevante: si tu empresa desarrolla software para la Administracion, ofrece servicios cloud a un organismo publico o gestiona la infraestructura TIC de un ayuntamiento, necesitas cumplir con el ENS.

El CCN estima que mas de 15.000 entidades en Espana estan sujetas al cumplimiento del ENS, aunque el numero de certificaciones activas a finales de 2025 rondaba las 3.200, lo que indica que todavia existe un margen significativo de mejora.

## Medidas de seguridad clave

El ENS organiza sus medidas de seguridad en tres marcos:

### Marco organizativo

Define las politicas y procedimientos de gobernanza de la seguridad:

- **Politica de seguridad**: documento aprobado por la direccion que establece el compromiso con la seguridad y asigna roles y responsabilidades.
- **Normativa de seguridad**: conjunto de normas internas que regulan el uso de los sistemas de informacion.
- **Procedimientos de seguridad**: instrucciones detalladas para la ejecucion de tareas de seguridad.
- **Proceso de autorizacion**: mecanismo formal para autorizar nuevos sistemas o cambios significativos.

### Marco operacional

Abarca las medidas tecnicas y procedimentales del dia a dia:

- **Planificacion**: analisis de riesgos, arquitectura de seguridad y adquisicion de componentes.
- **Control de acceso**: identificacion, autenticacion, mecanismo de acceso y segregacion de funciones.
- **Explotacion**: inventario de activos, gestion de configuracion, mantenimiento, gestion de cambios, proteccion frente a codigo danino y gestion de incidentes.
- **Servicios externos**: contratacion, acuerdos de nivel de servicio y seguimiento continuo de proveedores.
- **Continuidad del servicio**: planes de continuidad, pruebas periodicas y gestion de crisis.
- **Monitorizacion del sistema**: deteccion de intrusiones, registros de actividad y metricas de seguridad.

### Medidas de proteccion

Se centran en la proteccion tecnica de los activos:

- Proteccion de las comunicaciones (cifrado, cortafuegos, segmentacion de redes).
- Proteccion de los soportes de informacion.
- Proteccion de las aplicaciones informaticas (desarrollo seguro, pruebas de seguridad).
- Proteccion de la informacion (clasificacion, cifrado en reposo, copias de seguridad).
- Proteccion de los servicios (disponibilidad, proteccion frente a denegacion de servicio).

## Pasos para implementar el ENS

La implementacion del ENS es un proceso estructurado que, dependiendo del tamano de la organizacion y del nivel de seguridad requerido, puede llevar entre 6 y 18 meses. Estos son los pasos fundamentales:

### 1. Compromiso de la direccion y designacion de roles

Sin el apoyo explicito de la alta direccion, el proyecto fracasara. Es necesario designar al Responsable de la Informacion, al Responsable del Servicio y al Responsable de la Seguridad, tal como exige el ENS. En organizaciones con nivel alto, estas tres figuras deben ser personas distintas.

### 2. Determinacion del alcance y categorization del sistema

Identifica los servicios y sistemas de informacion que entran en el ambito del ENS. Para cada uno, evalua las dimensiones de seguridad y determina la categoria (baja, media o alta). El CCN proporciona la herramienta PILAR para facilitar este analisis.

### 3. Analisis de riesgos

Realiza un analisis de riesgos formal siguiendo una metodologia reconocida. MAGERIT es la metodologia de referencia en el contexto espanol y esta plenamente alineada con el ENS. Identifica activos, amenazas, vulnerabilidades y calcula el riesgo residual.

### 4. Declaracion de aplicabilidad

Documenta que medidas del ENS son aplicables a tu sistema, cuales no lo son y la justificacion en cada caso. Esta declaracion es un documento clave para la auditoria de certificacion.

### 5. Implementacion de medidas

Despliega las medidas tecnicas, organizativas y operacionales que correspondan segun la categoria del sistema. Apoyate en las guias CCN-STIC del CCN, que ofrecen instrucciones detalladas para cada medida.

### 6. Formacion y concienciacion

Forma al personal en sus responsabilidades de seguridad. El CCN ofrece a traves de su plataforma Angeles recursos formativos especificos para el ENS. La formacion no es un evento puntual, sino un proceso continuo.

### 7. Auditoria y certificacion

Una vez implementadas las medidas, somete el sistema a una auditoria de cumplimiento. Para sistemas de nivel medio y alto, la auditoria debe ser realizada por una entidad independiente acreditada. Tras superar la auditoria, se obtiene la certificacion de conformidad con el ENS, que debe renovarse cada dos anos.

Si tu organizacion busca optimizar este proceso, plataformas como Riskitera automatizan gran parte de la gestion documental, el seguimiento de medidas y la preparacion para la auditoria, reduciendo significativamente el esfuerzo manual y los plazos de implementacion.

## Relacion del ENS con otros marcos y normativas

El ENS no existe de forma aislada. Forma parte de un ecosistema normativo cada vez mas interconectado:

- **ISO 27001**: el ENS y la ISO 27001 comparten muchos conceptos y controles. Una organizacion certificada en ISO 27001 tiene gran parte del camino recorrido para el ENS, aunque hay medidas especificas del ENS que la ISO no cubre. Si estas valorando implementar ISO 27001 en tu organizacion, te recomendamos nuestra [guia practica de ISO 27001 para startups](/es/posts/2026/02/guia-iso-27001-startups/).
- **NIS2**: la Directiva europea NIS2 afecta a entidades esenciales e importantes en toda la Union Europea. En Espana, el ENS actuara como vehiculo para implementar parte de los requisitos de NIS2 en el sector publico. En proximos articulos analizaremos en detalle [que es la NIS2 y a quien afecta](/es/posts/2026/04/nis2-que-es-a-quien-afecta/).
- **DORA**: el Reglamento de Resiliencia Operativa Digital afecta al sector financiero europeo. Las entidades financieras sujetas a DORA que tambien trabajan con la Administracion publica podrian necesitar cumplir con ambos marcos. Publicaremos proximamente una guia completa sobre [DORA y la ciberseguridad financiera](/es/posts/2026/04/dora-reglamento-ciberseguridad-financiera/).
- **RGPD**: el cumplimiento del ENS contribuye a satisfacer los requisitos de seguridad del Reglamento General de Proteccion de Datos, aunque no lo sustituye.

## Beneficios de la certificacion ENS

Mas alla del cumplimiento legal, la certificacion ENS aporta ventajas tangibles:

- **Acceso a contratos publicos**: cada vez mas licitaciones exigen la certificacion ENS como requisito de solvencia tecnica.
- **Reduccion del riesgo de incidentes**: las organizaciones certificadas reportan un 43 por ciento menos de incidentes graves, segun datos de INCIBE correspondientes a 2024.
- **Confianza institucional**: la certificacion es una senal clara de madurez en seguridad ante organismos publicos y socios comerciales.
- **Mejora operativa**: el proceso de implementacion obliga a documentar, racionalizar y optimizar los procesos de gestion de la seguridad.
- **Preparacion para otras normativas**: facilita la adaptacion a NIS2, DORA y otros marcos regulatorios europeos.

## Errores comunes en la implementacion del ENS

Basandonos en la experiencia del sector, estos son los errores mas frecuentes:

- **Tratar el ENS como un proyecto exclusivamente tecnologico**: el ENS exige medidas organizativas y de gobernanza que van mas alla de la tecnologia.
- **Subestimar la gestion documental**: la documentacion es un pilar fundamental del ENS. Sin politicas, normas y procedimientos formalizados, la auditoria no se supera.
- **Ignorar la cadena de suministro**: desde el RD 311/2022, los proveedores deben cumplir con el ENS. No verificar su cumplimiento es un riesgo y un incumplimiento.
- **No asignar recursos suficientes**: la implementacion requiere dedicacion. Intentar hacerlo sin personal dedicado ni presupuesto adecuado es una receta para el fracaso.
- **Categorizar incorrectamente el sistema**: una categorizacion erronea, ya sea por exceso o por defecto, genera problemas en la auditoria y en la operacion.

## Preguntas frecuentes

### Es obligatorio el ENS para las empresas privadas?

El ENS es directamente obligatorio para el sector publico. Las empresas privadas deben cumplirlo cuando prestan servicios tecnologicos a la Administracion, gestionan sistemas de informacion del sector publico o tratan datos en nombre de una entidad publica. Si tu empresa tiene contratos con la Administracion que implican el manejo de informacion o sistemas, muy probablemente necesitas cumplir con el ENS.

### Cuanto cuesta obtener la certificacion ENS?

El coste varia enormemente segun el tamano de la organizacion y el nivel de seguridad. Para una pyme que busca la certificacion en nivel medio, el coste total (consultoria, implementacion de medidas y auditoria) suele oscilar entre 25.000 y 80.000 euros. Para nivel alto en organizaciones grandes, la inversion puede superar los 200.000 euros. Las herramientas de automatizacion GRC como Riskitera pueden reducir estos costes significativamente al eliminar trabajo manual repetitivo.

### Cual es la diferencia entre el ENS y la ISO 27001?

La ISO 27001 es un estandar internacional voluntario centrado en sistemas de gestion de seguridad de la informacion. El ENS es una normativa espanola obligatoria para el sector publico con medidas de seguridad especificas y niveles de clasificacion propios. Aunque comparten muchos principios, el ENS incluye requisitos concretos (como los perfiles de cumplimiento o la integracion con las guias CCN-STIC) que la ISO 27001 no contempla. Muchas organizaciones optan por implementar ambos de forma coordinada.

### Cada cuanto hay que renovar la certificacion ENS?

La certificacion ENS tiene una validez de dos anos. Al cabo de ese periodo, es necesario someterse a una nueva auditoria de renovacion. Ademas, se requiere una vigilancia continua y, en caso de cambios significativos en los sistemas, puede ser necesaria una auditoria extraordinaria antes de que expire el plazo de dos anos.

### Que papel juega el CCN-CERT en el ENS?

El CCN-CERT (Centro Criptologico Nacional - Computer Emergency Response Team) es el equipo de respuesta a incidentes de seguridad de referencia para el sector publico espanol. En el marco del ENS, el CCN-CERT publica las guias tecnicas CCN-STIC, gestiona las herramientas oficiales como PILAR (analisis de riesgos) e INES (estado de cumplimiento del ENS), coordina la respuesta a incidentes y mantiene actualizado el catalogo de productos de seguridad certificados. Ademas, es el organismo ante el que las entidades publicas deben notificar los incidentes de seguridad.
