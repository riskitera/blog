---
title: "ENS en la administración pública: requisitos, plazos y errores comunes"
description: "Guía práctica del Esquema Nacional de Seguridad para administraciones públicas: requisitos obligatorios, plazos de cumplimiento, herramientas del CCN y errores frecuentes en la implementación."
slug: "ens-administracion-publica"
date: 2026-05-23
publishDate: 2026-05-23
lastmod: 2026-05-23
draft: false
tags: ["ENS", "Administración Pública", "Compliance"]
categories: ["Compliance"]
author: "David Moya"
keyword: "ENS administracion publica"
funnel: "mofu"
---

Guía práctica del Esquema Nacional de Seguridad para administraciones públicas: requisitos obligatorios, plazos de cumplimiento, herramientas del CCN y errores frecuentes en la implementación.

<!--more-->

## Qué exige el ENS a las administraciones públicas?

El Esquema Nacional de Seguridad (RD 311/2022) es obligatorio para todo el sector público español: Administración General del Estado (AGE), comunidades autónomas, entidades locales (ayuntamientos, diputaciones), universidades públicas y cualquier entidad de derecho público. También aplica a las empresas privadas que prestan servicios o manejan información del sector público.

El ENS establece un marco común de seguridad que incluye:

**Principios básicos.** Seguridad como proceso integral, gestión de riesgos, prevención, detección, respuesta y conservación, líneas de defensa, vigilancia continua y reevaluación periódica. Estos principios no son declarativos: el CCN los evalúa en las auditorías.

**Requisitos mínimos.** 15 requisitos mínimos que toda administración pública debe cumplir: organización e implantación del proceso de seguridad, análisis y gestión de riesgos, gestión de personal, profesionalidad, autorización y control de accesos, protección de las instalaciones, adquisición de productos de seguridad, seguridad por defecto, integridad y actualización del sistema, protección de la información almacenada y en tránsito, prevención ante otros sistemas interconectados, registro de actividad, incidentes de seguridad, continuidad de la actividad y mejora continua.

**73 medidas de seguridad.** Organizadas en tres marcos (organizativo, operacional y de protección), con niveles de exigencia que dependen de la categoría del sistema (básica, media o alta). Cada medida tiene requisitos concretos: que implementar, como documentarlo y como auditarlo.

**Conformidad.** Las administraciones públicas deben obtener la Declaración de Conformidad (categoría básica) o la Certificación de Conformidad (categorías media y alta) emitida por un organismo acreditado. El proceso de certificación incluye auditoría documental, auditoría técnica y revisión por el CCN.

## Cuáles son los plazos de cumplimiento del ENS para AA.PP.?

El ENS original (RD 3/2010) lleva vigente desde 2010. La actualización de 2022 (RD 311/2022) entró en vigor en mayo de 2022 con un periodo de adecuación de 24 meses que finalizó en mayo de 2024.

**Estado actual (2026).** Todas las administraciones públicas deberían estar adecuadas al ENS 2022. En la práctica, el grado de cumplimiento es desigual:

- **AGE:** nivel de cumplimiento alto. Los ministerios y organismos de la AGE llevan años trabajando con el CCN y la mayoría tienen certificación o están en proceso avanzado.
- **Comunidades autónomas:** nivel medio-alto. Las CCAA grandes (Madrid, Cataluña, Andalucía, País Vasco) tienen programas de seguridad maduros. Las más pequeñas presentan gaps significativos por falta de recursos.
- **Entidades locales:** nivel bajo-medio. Los ayuntamientos grandes (Madrid, Barcelona, Valencia, Sevilla) tienen equipos de seguridad y programas de adecuación. Los ayuntamientos medianos y pequeños (que son la mayoría: hay más de 8.000 municipios en España) carecen de personal especializado y presupuesto. Según el CCN, menos del 30% de los ayuntamientos de menos de 50.000 habitantes tienen un nivel de cumplimiento ENS aceptable.

**Plazos de certificación.** No hay un plazo único de certificación impuesto, pero el CCN presiona activamente a través del sistema INES (Informe Nacional del Estado de Seguridad) para que todas las entidades públicas reporten su estado y avancen hacia la conformidad. La renovación de la certificación es cada 2 años.

## Qué herramientas proporciona el CCN para cumplir el ENS?

El CCN-CERT pone a disposición de las administraciones públicas un ecosistema completo de herramientas gratuitas:

**PILAR.** Herramienta de análisis y gestión de riesgos basada en la metodología MAGERIT. Permite inventariar activos, identificar amenazas, evaluar riesgos y seleccionar salvaguardas. Es la herramienta de referencia para el análisis de riesgos ENS. Disponible en versión desktop y web.

**CLARA.** Herramienta de auditoría de cumplimiento que verifica automáticamente la configuración de seguridad de sistemas Windows y Linux contra los requisitos del ENS. Genera informes de conformidad y no conformidad que alimentan el proceso de certificación.

**INES (Informe Nacional del Estado de Seguridad).** Plataforma web donde las administraciones públicas reportan su nivel de cumplimiento del ENS. Permite al CCN tener una visión agregada del estado de seguridad del sector público y priorizar acciones.

**LUCIA.** Sistema de gestión de ciberincidentes que permite a las entidades reportar, gestionar y escalar incidentes de seguridad. Conecta con el CCN-CERT para incidentes que requieran soporte o coordinación.

**REYES (Red de Excelencia y Seguridad).** Plataforma de inteligencia de amenazas que proporciona información sobre IOCs, campañas de malware activas y vulnerabilidades relevantes para el sector público español.

**microCLAUDE.** Sonda de detección de amenazas que el CCN despliega en las redes de las administraciones públicas para detectar tráfico malicioso, conexiones a C2 y exfiltración de datos.

**Guías CCN-STIC (serie 800).** Más de 200 guías técnicas con instrucciones detalladas para securizar sistemas operativos, aplicaciones, redes y servicios cloud. Son el complemento práctico de las medidas del ENS.

**ANA (Análisis de Red Automatizado).** Herramienta de análisis de vulnerabilidades de red que el CCN ofrece como servicio a las administraciones públicas.

{{< cta type="tofu" text="Riskitera mapea automaticamente controles ENS, NIS2 e ISO 27001, reduciendo el esfuerzo manual un 70%." label="Ver cómo" >}}

## Cómo categorizan los sistemas las administraciones públicas?

La categorización es el primer paso del proceso ENS y determina el nivel de exigencia de seguridad aplicable. Se basa en valorar el impacto que tendría un incidente de seguridad sobre cinco dimensiones:

**Las cinco dimensiones de seguridad:**
1. **Disponibilidad (D):** que un servicio o información esté accesible cuando se necesita
2. **Autenticidad (A):** que la identidad de quien accede o envía información sea verificable
3. **Integridad (I):** que la información no sea alterada de forma no autorizada
4. **Confidencialidad (C):** que la información solo sea accesible a quien está autorizado
5. **Trazabilidad (T):** que las acciones sobre la información sean registradas y atribuibles

**Niveles de impacto.** Para cada dimensión se asigna un nivel: BAJO (perjuicio limitado), MEDIO (perjuicio grave) o ALTO (perjuicio muy grave o irreparable).

**Determinación de la categoría.** La categoría del sistema es la mayor de todas las valoraciones:
- **Categoría BASICA:** todas las dimensiones en BAJO
- **Categoría MEDIA:** al menos una dimensión en MEDIO, ninguna en ALTO
- **Categoría ALTA:** al menos una dimensión en ALTO

**Ejemplos prácticos en AA.PP.:**
- Portal web informativo de un ayuntamiento sin datos personales: categoría BASICA
- Sede electrónica con tramitación de expedientes: categoría MEDIA (integridad y autenticidad MEDIA como mínimo)
- Sistema de gestión de padrón municipal: categoría MEDIA o ALTA (confidencialidad MEDIA/ALTA por datos personales a gran escala)
- Historia clinica electrónica en hospital público: categoría ALTA (confidencialidad ALTA por datos de salud)
- Sistemas de emergencias 112: categoría ALTA (disponibilidad ALTA por impacto en vidas humanas)
- Plataforma de contratación pública: categoría MEDIA o ALTA (integridad y confidencialidad de ofertas)

La categorización debe documentarse, justificarse y revisarse cuando cambien las circunstancias del sistema (nuevos datos tratados, nuevos servicios, cambios normativos).

## Cuáles son los errores más comunes de las AA.PP. con el ENS?

Tras más de 15 años de vigencia del ENS, los errores se repiten. Estos son los más frecuentes según los informes del CCN y la experiencia de auditores:

**1. Tratar el ENS como un proyecto puntual, no como un proceso.** Muchas entidades abordan el ENS como un proyecto con fecha de fin: contratan una consultora, obtienen la certificación y vuelven a la operativa habitual. El ENS exige mejora continua, monitorización permanente y reevaluación periódica. Sin mantenimiento, el cumplimiento se degrada en meses.

**2. Categorización demasiado baja.** Algunos organismos infravaloran el impacto de sus sistemas para reducir el número de controles exigibles. Categorizar como BASICA un sistema que maneja datos personales a gran escala o que soporta un servicio público esencial es un error que los auditores detectan y que expone a la entidad.

**3. Análisis de riesgos superficial.** Rellenar PILAR como un formulario burocrático sin reflexión real sobre amenazas y vulnerabilidades. Un análisis de riesgos válido requiere conocimiento de la infraestructura, participación de los responsables de los sistemas y actualización periódica.

**4. Falta de segregación de funciones.** El responsable de seguridad, el responsable del sistema y el responsable de la información deben ser personas diferentes (o al menos, roles diferenciados). En entidades pequeñas es común que una sola persona asuma todos los roles, lo que elimina los controles cruzados.

**5. Planes de continuidad no probados.** Tener un plan de continuidad documentado pero nunca probado es casi peor que no tenerlo: genera una falsa sensación de seguridad. El ENS exige pruebas periódicas de los planes de continuidad y recuperación.

**6. Gestión de proveedores inexistente.** Las AA.PP. externalizan servicios TIC (hosting, desarrollo, soporte) sin exigir cumplimiento ENS al proveedor ni auditar su postura de seguridad. Si el proveedor maneja información del sector público, debe cumplir el ENS.

**7. Formación y concienciación insuficiente.** El ENS exige formación del personal en seguridad de la información. En la práctica, muchas entidades no realizan formación periódica o la limitan a un curso online anual que nadie completa.

**8. Registros de actividad incompletos.** El ENS exige registrar la actividad de los usuarios en los sistemas para poder investigar incidentes. Muchas entidades no configuran los logs adecuadamente, no los retienen el tiempo necesario o no los revisan nunca.

## Qué papel juegan los proveedores tecnológicos de la AA.PP.?

Los proveedores de servicios TIC de la administración pública tienen un papel crítico en el cumplimiento del ENS, y sus obligaciones han aumentado con la actualización de 2022.

**Obligación de cumplimiento.** Cualquier proveedor que maneje información del sector público o preste servicios que soporten sistemas afectados por el ENS debe cumplir las medidas de seguridad correspondientes a la categoría del sistema. Esto aplica a: empresas de hosting y cloud, desarrolladoras de software, consultoras, integradores de sistemas, proveedores de servicios gestionados (MSP/MSSP) y empresas de outsourcing de IT.

**Certificación de proveedores.** El ENS 2022 refuerza la exigencia de que los proveedores acrediten su conformidad. Los pliegos de contratación pública deben incluir requisitos de seguridad alineados con el ENS, y la certificación ENS del proveedor se valora en la adjudicación.

**Productos cualificados.** El CCN mantiene el Catálogo de Productos de Seguridad de las Tecnologías de la Información y la Comunicación (CPSTIC) con productos y servicios evaluados y cualificados para su uso en sistemas ENS. Las administraciones públicas deben priorizar estos productos cuando sea posible.

**Servicios cloud.** Los servicios cloud utilizados por la AA.PP. deben cumplir las condiciones del ENS para servicios en la nube (guía CCN-STIC-823). Los grandes proveedores cloud (AWS, Azure, Google Cloud) tienen certificación ENS para determinados servicios, pero la responsabilidad de la configuración segura recae en la entidad pública.

**Responsabilidad compartida.** El proveedor es responsable de la seguridad "del" servicio (infraestructura, plataforma) y la administración pública es responsable de la seguridad "en" el servicio (configuración, datos, accesos). Esta distinción es fuente frecuente de gaps de seguridad.

**Auditorias a proveedores.** Las administraciones públicas tienen derecho a auditar a sus proveedores TIC en materia de seguridad. En la práctica, pocas lo ejercen por falta de recursos. DORA (para sector financiero) y NIS2 están elevando este estándar y es previsible que el ENS lo refuerce en futuras revisiones.

## Cómo afecta NIS2 a las administraciones públicas españolas?

La Directiva NIS2 (2022/2555) incluye a las administraciones públicas como entidades esenciales, lo que supone un nuevo nivel de exigencia que se suma al ENS.

**Ambito de aplicación.** NIS2 aplica a las entidades de la administración pública a nivel central y regional (AGE y comunidades autónomas). Los Estados miembros pueden decidir si incluir a las entidades locales (ayuntamientos, diputaciones). La transposición española (en trámite) determinará el alcance exacto para las entidades locales.

**Requisitos adicionales a los del ENS.** Aunque el ENS ya cubre muchos de los requisitos de NIS2, la directiva introduce elementos nuevos:

- **Gobernanza:** NIS2 exige que el órgano de dirección apruebe las medidas de gestión de riesgos, supervise su implementación y reciba formación en ciberseguridad. Esto implica que los equipos de gobierno (alcaldes, consejeros, secretarios generales) deben tener un papel activo, no solo firmar documentos.
- **Notificación de incidentes:** NIS2 establece plazos más exigentes que el ENS: alerta temprana en 24 horas, notificación completa en 72 horas e informe final en un mes. El destinatario es el CSIRT de referencia (CCN-CERT para AA.PP.).
- **Seguridad en la cadena de suministro:** NIS2 exige evaluar los riesgos de ciberseguridad de los proveedores y de la cadena de suministro TIC, con medidas específicas para mitigarlos.
- **Sanciones:** NIS2 introduce sanciones para entidades esenciales de hasta 10 millones de euros o el 2% del volumen de negocio global. Para las administraciones públicas, las sanciones pueden traducirse en responsabilidad personal de los directivos.

**Convergencia ENS-NIS2.** El CCN está trabajando en alinear el ENS con los requisitos de NIS2 para evitar duplicidades. La expectativa es que una administración pública que cumpla el ENS en su categoría correspondiente cumpla también los requisitos de NIS2, con complementos menores en gobernanza y notificación.

**Plazo de transposición.** El plazo de transposición de NIS2 era octubre de 2024. España (como la mayoría de Estados miembros) no cumplió el plazo. La transposición está en trámite parlamentario y se espera su aprobación durante 2026.


{{< cta type="bofu" text="Empieza tu PoC y descubre cuanto tiempo ahorras en cada ciclo de auditoría." label="Iniciar PoC" >}}


**Artículos relacionados:**
- [Qué Es Esquema Nacional Seguridad Ens](/es/posts/2026/04/que-es-esquema-nacional-seguridad-ens/)
- [Nis2 Que Es A Quien Afecta](/es/posts/2026/04/nis2-que-es-a-quien-afecta/)

## Preguntas frecuentes

**Un ayuntamiento pequeño tiene que cumplir el ENS?**
Sí. El ENS es obligatorio para todas las administraciones públicas, independientemente de su tamaño. Un ayuntamiento de 500 habitantes está sujeto al ENS igual que un ministerio. La diferencia está en la categorización: los sistemas de un ayuntamiento pequeño serán probablemente de categoría BASICA, lo que reduce el número de controles exigibles. El CCN ofrece herramientas gratuitas y guías simplificadas para entidades locales pequeñas.

**Cuanto cuesta la certificación ENS?**
El coste depende de la categoría y la complejidad. Para un ayuntamiento mediano con sistemas de categoría MEDIA, la auditoría de certificación cuesta entre 15.000 y 40.000 euros. Para un organismo de la AGE con múltiples sistemas de categoría ALTA, puede superar los 100.000 euros. A esto hay que sumar el coste de adecuación previo (consultoría, herramientas, personal), que es significativamente mayor que la auditoría en si.

**Que pasa si una administración pública no cumple el ENS?**
No hay un régimen sancionador explícito en el propio ENS como el del RGPD. Sin embargo, el incumplimiento puede tener consecuencias: requerimientos del CCN, informes negativos en INES que afectan a la reputación institucional, responsabilidad patrimonial de la administración en caso de brecha de seguridad, y responsabilidad personal de los funcionarios que no adoptaron las medidas exigidas. Con NIS2, las consecuencias se endurecen significativamente.

**Se puede cumplir ENS e ISO 27001 al mismo tiempo?**
Sí, y es recomendable. El ENS y la ISO 27001 comparten muchos controles (gestión de riesgos, control de accesos, continuidad, auditorías). El CCN ha publicado la guía CCN-STIC-825 que mapea los controles del ENS con los de ISO 27001:2022. Una entidad que se certifique en ambos marcos puede optimizar el proceso evitando duplicar esfuerzos. Riskitera mapea automáticamente controles entre ambos marcos.

**Como afecta la Ley 40/2015 a la seguridad de las AA.PP.?**
La Ley 40/2015 de Régimen Jurídico del Sector Público establece en su artículo 156 que el ENS tiene por objeto establecer la política de seguridad en la utilización de medios electrónicos y que será de aplicación a todo el sector público. Esto da cobertura legal plena al ENS y vincula su cumplimiento con la obligación legal de las administraciones de garantizar la seguridad de los servicios electrónicos que prestan a los ciudadanos.
