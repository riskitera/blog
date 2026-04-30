---
title: "ENS en la administracion publica: requisitos, plazos y errores comunes"
description: "Guia practica del Esquema Nacional de Seguridad para administraciones publicas: requisitos obligatorios, plazos de cumplimiento, herramientas del CCN y errores frecuentes en la implementacion."
slug: "ens-administracion-publica"
date: 2026-05-23
publishDate: 2026-05-23
lastmod: 2026-05-23
draft: false
tags: ["ENS", "Administracion Publica", "Compliance"]
categories: ["Compliance"]
author: "David Moya"
keyword: "ENS administracion publica"
funnel: "mofu"
---

Guia practica del Esquema Nacional de Seguridad para administraciones publicas: requisitos obligatorios, plazos de cumplimiento, herramientas del CCN y errores frecuentes en la implementacion.

<!--more-->

## Que exige el ENS a las administraciones publicas?

El Esquema Nacional de Seguridad (RD 311/2022) es obligatorio para todo el sector publico espanol: Administracion General del Estado (AGE), comunidades autonomas, entidades locales (ayuntamientos, diputaciones), universidades publicas y cualquier entidad de derecho publico. Tambien aplica a las empresas privadas que prestan servicios o manejan informacion del sector publico.

El ENS establece un marco comun de seguridad que incluye:

**Principios basicos.** Seguridad como proceso integral, gestion de riesgos, prevencion, deteccion, respuesta y conservacion, lineas de defensa, vigilancia continua y reevaluacion periodica. Estos principios no son declarativos: el CCN los evalua en las auditorias.

**Requisitos minimos.** 15 requisitos minimos que toda administracion publica debe cumplir: organizacion e implantacion del proceso de seguridad, analisis y gestion de riesgos, gestion de personal, profesionalidad, autorizacion y control de accesos, proteccion de las instalaciones, adquisicion de productos de seguridad, seguridad por defecto, integridad y actualizacion del sistema, proteccion de la informacion almacenada y en transito, prevencion ante otros sistemas interconectados, registro de actividad, incidentes de seguridad, continuidad de la actividad y mejora continua.

**73 medidas de seguridad.** Organizadas en tres marcos (organizativo, operacional y de proteccion), con niveles de exigencia que dependen de la categoria del sistema (basica, media o alta). Cada medida tiene requisitos concretos: que implementar, como documentarlo y como auditarlo.

**Conformidad.** Las administraciones publicas deben obtener la Declaracion de Conformidad (categoria basica) o la Certificacion de Conformidad (categorias media y alta) emitida por un organismo acreditado. El proceso de certificacion incluye auditoria documental, auditoria tecnica y revision por el CCN.

## Cuales son los plazos de cumplimiento del ENS para AA.PP.?

El ENS original (RD 3/2010) lleva vigente desde 2010. La actualizacion de 2022 (RD 311/2022) entro en vigor en mayo de 2022 con un periodo de adecuacion de 24 meses que finalizo en mayo de 2024.

**Estado actual (2026).** Todas las administraciones publicas deberian estar adecuadas al ENS 2022. En la practica, el grado de cumplimiento es desigual:

- **AGE:** nivel de cumplimiento alto. Los ministerios y organismos de la AGE llevan anos trabajando con el CCN y la mayoria tienen certificacion o estan en proceso avanzado.
- **Comunidades autonomas:** nivel medio-alto. Las CCAA grandes (Madrid, Cataluna, Andalucia, Pais Vasco) tienen programas de seguridad maduros. Las mas pequenas presentan gaps significativos por falta de recursos.
- **Entidades locales:** nivel bajo-medio. Los ayuntamientos grandes (Madrid, Barcelona, Valencia, Sevilla) tienen equipos de seguridad y programas de adecuacion. Los ayuntamientos medianos y pequenos (que son la mayoria: hay mas de 8.000 municipios en Espana) carecen de personal especializado y presupuesto. Segun el CCN, menos del 30% de los ayuntamientos de menos de 50.000 habitantes tienen un nivel de cumplimiento ENS aceptable.

**Plazos de certificacion.** No hay un plazo unico de certificacion impuesto, pero el CCN presiona activamente a traves del sistema INES (Informe Nacional del Estado de Seguridad) para que todas las entidades publicas reporten su estado y avancen hacia la conformidad. La renovacion de la certificacion es cada 2 anos.

## Que herramientas proporciona el CCN para cumplir el ENS?

El CCN-CERT pone a disposicion de las administraciones publicas un ecosistema completo de herramientas gratuitas:

**PILAR.** Herramienta de analisis y gestion de riesgos basada en la metodologia MAGERIT. Permite inventariar activos, identificar amenazas, evaluar riesgos y seleccionar salvaguardas. Es la herramienta de referencia para el analisis de riesgos ENS. Disponible en version desktop y web.

**CLARA.** Herramienta de auditoria de cumplimiento que verifica automaticamente la configuracion de seguridad de sistemas Windows y Linux contra los requisitos del ENS. Genera informes de conformidad y no conformidad que alimentan el proceso de certificacion.

**INES (Informe Nacional del Estado de Seguridad).** Plataforma web donde las administraciones publicas reportan su nivel de cumplimiento del ENS. Permite al CCN tener una vision agregada del estado de seguridad del sector publico y priorizar acciones.

**LUCIA.** Sistema de gestion de ciberincidentes que permite a las entidades reportar, gestionar y escalar incidentes de seguridad. Conecta con el CCN-CERT para incidentes que requieran soporte o coordinacion.

**REYES (Red de Excelencia y Seguridad).** Plataforma de inteligencia de amenazas que proporciona informacion sobre IOCs, campanas de malware activas y vulnerabilidades relevantes para el sector publico espanol.

**microCLAUDE.** Sonda de deteccion de amenazas que el CCN despliega en las redes de las administraciones publicas para detectar trafico malicioso, conexiones a C2 y exfiltracion de datos.

**Guias CCN-STIC (serie 800).** Mas de 200 guias tecnicas con instrucciones detalladas para securizar sistemas operativos, aplicaciones, redes y servicios cloud. Son el complemento practico de las medidas del ENS.

**ANA (Analisis de Red Automatizado).** Herramienta de analisis de vulnerabilidades de red que el CCN ofrece como servicio a las administraciones publicas.

{{< cta type="tofu" text="Riskitera mapea automaticamente controles ENS, NIS2 e ISO 27001, reduciendo el esfuerzo manual un 70%." label="Ver como" >}}

## Como categorizan los sistemas las administraciones publicas?

La categorizacion es el primer paso del proceso ENS y determina el nivel de exigencia de seguridad aplicable. Se basa en valorar el impacto que tendria un incidente de seguridad sobre cinco dimensiones:

**Las cinco dimensiones de seguridad:**
1. **Disponibilidad (D):** que un servicio o informacion este accesible cuando se necesita
2. **Autenticidad (A):** que la identidad de quien accede o envia informacion sea verificable
3. **Integridad (I):** que la informacion no sea alterada de forma no autorizada
4. **Confidencialidad (C):** que la informacion solo sea accesible a quien esta autorizado
5. **Trazabilidad (T):** que las acciones sobre la informacion sean registradas y atribuibles

**Niveles de impacto.** Para cada dimension se asigna un nivel: BAJO (perjuicio limitado), MEDIO (perjuicio grave) o ALTO (perjuicio muy grave o irreparable).

**Determinacion de la categoria.** La categoria del sistema es la mayor de todas las valoraciones:
- **Categoria BASICA:** todas las dimensiones en BAJO
- **Categoria MEDIA:** al menos una dimension en MEDIO, ninguna en ALTO
- **Categoria ALTA:** al menos una dimension en ALTO

**Ejemplos practicos en AA.PP.:**
- Portal web informativo de un ayuntamiento sin datos personales: categoria BASICA
- Sede electronica con tramitacion de expedientes: categoria MEDIA (integridad y autenticidad MEDIA como minimo)
- Sistema de gestion de padron municipal: categoria MEDIA o ALTA (confidencialidad MEDIA/ALTA por datos personales a gran escala)
- Historia clinica electronica en hospital publico: categoria ALTA (confidencialidad ALTA por datos de salud)
- Sistemas de emergencias 112: categoria ALTA (disponibilidad ALTA por impacto en vidas humanas)
- Plataforma de contratacion publica: categoria MEDIA o ALTA (integridad y confidencialidad de ofertas)

La categorizacion debe documentarse, justificarse y revisarse cuando cambien las circunstancias del sistema (nuevos datos tratados, nuevos servicios, cambios normativos).

## Cuales son los errores mas comunes de las AA.PP. con el ENS?

Tras mas de 15 anos de vigencia del ENS, los errores se repiten. Estos son los mas frecuentes segun los informes del CCN y la experiencia de auditores:

**1. Tratar el ENS como un proyecto puntual, no como un proceso.** Muchas entidades abordan el ENS como un proyecto con fecha de fin: contratan una consultora, obtienen la certificacion y vuelven a la operativa habitual. El ENS exige mejora continua, monitorizacion permanente y reevaluacion periodica. Sin mantenimiento, el cumplimiento se degrada en meses.

**2. Categorizacion demasiado baja.** Algunos organismos infravaloran el impacto de sus sistemas para reducir el numero de controles exigibles. Categorizar como BASICA un sistema que maneja datos personales a gran escala o que soporta un servicio publico esencial es un error que los auditores detectan y que expone a la entidad.

**3. Analisis de riesgos superficial.** Rellenar PILAR como un formulario burocratico sin reflexion real sobre amenazas y vulnerabilidades. Un analisis de riesgos valido requiere conocimiento de la infraestructura, participacion de los responsables de los sistemas y actualizacion periodica.

**4. Falta de segregacion de funciones.** El responsable de seguridad, el responsable del sistema y el responsable de la informacion deben ser personas diferentes (o al menos, roles diferenciados). En entidades pequenas es comun que una sola persona asuma todos los roles, lo que elimina los controles cruzados.

**5. Planes de continuidad no probados.** Tener un plan de continuidad documentado pero nunca probado es casi peor que no tenerlo: genera una falsa sensacion de seguridad. El ENS exige pruebas periodicas de los planes de continuidad y recuperacion.

**6. Gestion de proveedores inexistente.** Las AA.PP. externalizan servicios TIC (hosting, desarrollo, soporte) sin exigir cumplimiento ENS al proveedor ni auditar su postura de seguridad. Si el proveedor maneja informacion del sector publico, debe cumplir el ENS.

**7. Formacion y concienciacion insuficiente.** El ENS exige formacion del personal en seguridad de la informacion. En la practica, muchas entidades no realizan formacion periodica o la limitan a un curso online anual que nadie completa.

**8. Registros de actividad incompletos.** El ENS exige registrar la actividad de los usuarios en los sistemas para poder investigar incidentes. Muchas entidades no configuran los logs adecuadamente, no los retienen el tiempo necesario o no los revisan nunca.

## Que papel juegan los proveedores tecnologicos de la AA.PP.?

Los proveedores de servicios TIC de la administracion publica tienen un papel critico en el cumplimiento del ENS, y sus obligaciones han aumentado con la actualizacion de 2022.

**Obligacion de cumplimiento.** Cualquier proveedor que maneje informacion del sector publico o preste servicios que soporten sistemas afectados por el ENS debe cumplir las medidas de seguridad correspondientes a la categoria del sistema. Esto aplica a: empresas de hosting y cloud, desarrolladoras de software, consultoras, integradores de sistemas, proveedores de servicios gestionados (MSP/MSSP) y empresas de outsourcing de IT.

**Certificacion de proveedores.** El ENS 2022 refuerza la exigencia de que los proveedores acrediten su conformidad. Los pliegos de contratacion publica deben incluir requisitos de seguridad alineados con el ENS, y la certificacion ENS del proveedor se valora en la adjudicacion.

**Productos cualificados.** El CCN mantiene el Catalogo de Productos de Seguridad de las Tecnologias de la Informacion y la Comunicacion (CPSTIC) con productos y servicios evaluados y cualificados para su uso en sistemas ENS. Las administraciones publicas deben priorizar estos productos cuando sea posible.

**Servicios cloud.** Los servicios cloud utilizados por la AA.PP. deben cumplir las condiciones del ENS para servicios en la nube (guia CCN-STIC-823). Los grandes proveedores cloud (AWS, Azure, Google Cloud) tienen certificacion ENS para determinados servicios, pero la responsabilidad de la configuracion segura recae en la entidad publica.

**Responsabilidad compartida.** El proveedor es responsable de la seguridad "del" servicio (infraestructura, plataforma) y la administracion publica es responsable de la seguridad "en" el servicio (configuracion, datos, accesos). Esta distincion es fuente frecuente de gaps de seguridad.

**Auditorias a proveedores.** Las administraciones publicas tienen derecho a auditar a sus proveedores TIC en materia de seguridad. En la practica, pocas lo ejercen por falta de recursos. DORA (para sector financiero) y NIS2 estan elevando este estandar y es previsible que el ENS lo refuerce en futuras revisiones.

## Como afecta NIS2 a las administraciones publicas espanolas?

La Directiva NIS2 (2022/2555) incluye a las administraciones publicas como entidades esenciales, lo que supone un nuevo nivel de exigencia que se suma al ENS.

**Ambito de aplicacion.** NIS2 aplica a las entidades de la administracion publica a nivel central y regional (AGE y comunidades autonomas). Los Estados miembros pueden decidir si incluir a las entidades locales (ayuntamientos, diputaciones). La transposicion espanola (en tramite) determinara el alcance exacto para las entidades locales.

**Requisitos adicionales a los del ENS.** Aunque el ENS ya cubre muchos de los requisitos de NIS2, la directiva introduce elementos nuevos:

- **Gobernanza:** NIS2 exige que el organo de direccion apruebe las medidas de gestion de riesgos, supervise su implementacion y reciba formacion en ciberseguridad. Esto implica que los equipos de gobierno (alcaldes, consejeros, secretarios generales) deben tener un papel activo, no solo firmar documentos.
- **Notificacion de incidentes:** NIS2 establece plazos mas exigentes que el ENS: alerta temprana en 24 horas, notificacion completa en 72 horas e informe final en un mes. El destinatario es el CSIRT de referencia (CCN-CERT para AA.PP.).
- **Seguridad en la cadena de suministro:** NIS2 exige evaluar los riesgos de ciberseguridad de los proveedores y de la cadena de suministro TIC, con medidas especificas para mitigarlos.
- **Sanciones:** NIS2 introduce sanciones para entidades esenciales de hasta 10 millones de euros o el 2% del volumen de negocio global. Para las administraciones publicas, las sanciones pueden traducirse en responsabilidad personal de los directivos.

**Convergencia ENS-NIS2.** El CCN esta trabajando en alinear el ENS con los requisitos de NIS2 para evitar duplicidades. La expectativa es que una administracion publica que cumpla el ENS en su categoria correspondiente cumpla tambien los requisitos de NIS2, con complementos menores en gobernanza y notificacion.

**Plazo de transposicion.** El plazo de transposicion de NIS2 era octubre de 2024. Espana (como la mayoria de Estados miembros) no cumplio el plazo. La transposicion esta en tramite parlamentario y se espera su aprobacion durante 2026.


{{< cta type="bofu" text="Empieza tu PoC y descubre cuanto tiempo ahorras en cada ciclo de auditoria." label="Iniciar PoC" >}}


**Articulos relacionados:**
- [Que Es Esquema Nacional Seguridad Ens](/es/posts/2026/04/que-es-esquema-nacional-seguridad-ens/)
- [Nis2 Que Es A Quien Afecta](/es/posts/2026/04/nis2-que-es-a-quien-afecta/)

## Preguntas frecuentes

**Un ayuntamiento pequeno tiene que cumplir el ENS?**
Si. El ENS es obligatorio para todas las administraciones publicas, independientemente de su tamano. Un ayuntamiento de 500 habitantes esta sujeto al ENS igual que un ministerio. La diferencia esta en la categorizacion: los sistemas de un ayuntamiento pequeno seran probablemente de categoria BASICA, lo que reduce el numero de controles exigibles. El CCN ofrece herramientas gratuitas y guias simplificadas para entidades locales pequenas.

**Cuanto cuesta la certificacion ENS?**
El coste depende de la categoria y la complejidad. Para un ayuntamiento mediano con sistemas de categoria MEDIA, la auditoria de certificacion cuesta entre 15.000 y 40.000 euros. Para un organismo de la AGE con multiples sistemas de categoria ALTA, puede superar los 100.000 euros. A esto hay que sumar el coste de adecuacion previo (consultoria, herramientas, personal), que es significativamente mayor que la auditoria en si.

**Que pasa si una administracion publica no cumple el ENS?**
No hay un regimen sancionador explicito en el propio ENS como el del RGPD. Sin embargo, el incumplimiento puede tener consecuencias: requerimientos del CCN, informes negativos en INES que afectan a la reputacion institucional, responsabilidad patrimonial de la administracion en caso de brecha de seguridad, y responsabilidad personal de los funcionarios que no adoptaron las medidas exigidas. Con NIS2, las consecuencias se endurecen significativamente.

**Se puede cumplir ENS e ISO 27001 al mismo tiempo?**
Si, y es recomendable. El ENS y la ISO 27001 comparten muchos controles (gestion de riesgos, control de accesos, continuidad, auditorias). El CCN ha publicado la guia CCN-STIC-825 que mapea los controles del ENS con los de ISO 27001:2022. Una entidad que se certifique en ambos marcos puede optimizar el proceso evitando duplicar esfuerzos. Riskitera mapea automaticamente controles entre ambos marcos.

**Como afecta la Ley 40/2015 a la seguridad de las AA.PP.?**
La Ley 40/2015 de Regimen Juridico del Sector Publico establece en su articulo 156 que el ENS tiene por objeto establecer la politica de seguridad en la utilizacion de medios electronicos y que sera de aplicacion a todo el sector publico. Esto da cobertura legal plena al ENS y vincula su cumplimiento con la obligacion legal de las administraciones de garantizar la seguridad de los servicios electronicos que prestan a los ciudadanos.
