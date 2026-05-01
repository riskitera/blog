---
title: "Guia completa DORA para entidades financieras: 12 requisitos tecnicos"
description: "Desglose tecnico de los 12 requisitos principales de DORA para entidades financieras: gestion de riesgos TIC, reporting, pruebas de resiliencia, terceros y comparticion de informacion."
slug: "guia-dora-entidades-financieras-requisitos"
date: 2026-07-16
publishDate: 2026-07-16
lastmod: 2026-07-16
draft: false
tags: ["DORA", "Banca", "Compliance"]
categories: ["Compliance"]
author: "David Moya"
keyword: "guia DORA entidades financieras"
funnel: "mofu"
---

Desglose tecnico de los 12 requisitos principales de DORA para entidades financieras: gestion de riesgos TIC, reporting, pruebas de resiliencia, terceros y comparticion de informacion.

<!--more-->

{{< key-takeaways >}}
- DORA establece 12 requisitos tecnicos agrupados en 5 pilares que afectan a bancos, aseguradoras, gestoras de fondos y proveedores TIC criticos en la Union Europea.
- La gestion de riesgos TIC (Articulos 6 a 16) exige un marco de gobernanza con responsabilidad directa del organo de direccion y revision anual obligatoria.
- El reporting de incidentes (Articulos 17 a 23) obliga a clasificar y notificar incidentes graves a las autoridades competentes en plazos de 4 horas, 72 horas y 1 mes.
- Las pruebas de resiliencia digital (Articulos 24 a 27) incluyen tests basicos anuales y pruebas TLPT avanzadas cada tres anios para entidades significativas.
- La gestion de riesgo de terceros (Articulos 28 a 44) impone un marco de supervision directa de la UE sobre proveedores TIC criticos, con poder sancionador.
{{< /key-takeaways >}}

## Que es DORA y por que importa a las entidades financieras

El [Reglamento (UE) 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554), conocido como DORA (Digital Operational Resilience Act), es la primera normativa europea que establece requisitos uniformes de resiliencia operativa digital para el sector financiero. Entro en vigor en enero de 2023 y su aplicacion es obligatoria desde el 17 de enero de 2025.

A diferencia de directivas anteriores que dejaban margen de transposicion a cada estado miembro, DORA es un reglamento de aplicacion directa. Esto significa que todas las entidades financieras de la UE (bancos, aseguradoras, empresas de inversion, gestoras de fondos, entidades de pago, proveedores de servicios de criptoactivos y otros 20 tipos de entidades) deben cumplir exactamente los mismos requisitos.

El contexto es claro: la dependencia del sector financiero respecto a la tecnologia ha crecido exponencialmente. Un fallo en un proveedor cloud, un ciberataque a un sistema de pagos o una interrupcion prolongada de servicios TIC puede generar un efecto cascada con impacto sistemico. DORA aborda esta realidad con un enfoque integral que va mas alla de la ciberseguridad tradicional.

### Relacion con NIS2 e ISO 27001

DORA no existe en el vacio. La [Directiva NIS2 (UE) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555) establece requisitos de ciberseguridad para sectores esenciales e importantes, incluido el financiero. Sin embargo, DORA prevalece como lex specialis para el sector financiero: cuando ambas normas cubren el mismo aspecto, se aplica DORA.

[ISO 27001](https://www.iso.org/standard/27001) sigue siendo un marco de referencia valido para la implementacion practica, pero no sustituye el cumplimiento de DORA. Muchas entidades financieras que ya tienen certificacion ISO 27001 descubren que necesitan reforzar areas especificas, como la gestion de riesgo de terceros TIC o las pruebas TLPT.

### Los 5 pilares de DORA

DORA se estructura en torno a 5 pilares fundamentales, de los que derivan los 12 requisitos tecnicos que analizamos en esta guia:

1. **Gestion de riesgos TIC** (Articulos 6 a 16)
2. **Gestion, clasificacion y notificacion de incidentes TIC** (Articulos 17 a 23)
3. **Pruebas de resiliencia operativa digital** (Articulos 24 a 27)
4. **Gestion de riesgo de terceros proveedores TIC** (Articulos 28 a 44)
5. **Acuerdos de intercambio de informacion** (Articulo 45)

Vamos a desglosar cada uno con sus requisitos tecnicos concretos.

## Pilar 1: Gestion de riesgos TIC (Articulos 6 a 16)

Este pilar es la columna vertebral de DORA. Define el marco de gobierno y los procesos que cada entidad financiera debe establecer para identificar, proteger, detectar, responder y recuperarse de riesgos relacionados con las TIC.

### Requisito 1: Marco de gobernanza TIC (Articulo 5)

El organo de direccion de la entidad financiera tiene la responsabilidad ultima y directa de la gestion de riesgos TIC. No se trata de delegar en el CISO y olvidarse. DORA exige que el consejo de administracion:

- Defina, apruebe y supervise la implementacion de la estrategia de resiliencia operativa digital.
- Establezca funciones y responsabilidades claras para todas las cuestiones relacionadas con las TIC.
- Asigne presupuesto suficiente para la formacion en resiliencia digital, tanto para empleados como para los propios miembros del organo de direccion.
- Revise y apruebe la politica de continuidad de negocio TIC al menos una vez al anio.

En la practica, esto implica que la ciberseguridad deja de ser un tema exclusivo del area tecnica. Los directivos deben demostrar conocimiento y participacion activa. Las actas del consejo deben reflejar que se han revisado los informes de riesgo TIC, los resultados de las pruebas de resiliencia y el estado de los proveedores criticos.

### Requisito 2: Marco de gestion de riesgos TIC (Articulos 6 a 9)

Toda entidad financiera debe documentar y mantener un marco de gestion de riesgos TIC solido que incluya:

- **Identificacion**: inventario completo de todos los activos TIC (hardware, software, datos, procesos), con clasificacion por criticidad y mapeo de dependencias. Cada activo debe tener un propietario asignado.
- **Proteccion y prevencion**: politicas de seguridad que cubran control de acceso, cifrado, segmentacion de redes, gestion de parches, hardening de sistemas y formacion continua del personal.
- **Deteccion**: mecanismos para identificar anomalias y actividad sospechosa en tiempo real. Esto incluye SIEM, correlacion de eventos, monitorizacion de endpoints y analisis de comportamiento.
- **Respuesta y recuperacion**: planes documentados y probados para la contencion, erradicacion y recuperacion ante incidentes TIC, con tiempos de recuperacion (RTO) y puntos de recuperacion (RPO) definidos.

Un ejemplo practico: un banco mediano necesita documentar que su sistema de banca online depende de tres proveedores cloud, dos pasarelas de pago y un proveedor de autenticacion. Debe tener mapeadas las dependencias cruzadas, de forma que si el proveedor de autenticacion cae, el plan de recuperacion contemple alternativas especificas con tiempos concretos.

### Requisito 3: Estrategia de resiliencia operativa digital (Articulo 6.8)

Mas alla del marco de gestion, DORA exige una estrategia de resiliencia que debe:

- Explicar como el marco de gestion de riesgos TIC apoya la estrategia de negocio.
- Establecer el nivel de tolerancia al riesgo TIC aprobado por el organo de direccion.
- Incluir objetivos claros de seguridad de la informacion, con KPIs medibles.
- Describir la arquitectura TIC objetivo y como la entidad planea evolucionar hacia ella.
- Definir mecanismos para detectar incidentes, responder y recuperarse de ellos.

Esta estrategia no es un documento estatico. Debe revisarse al menos anualmente o tras incidentes significativos, cambios importantes en la arquitectura TIC o resultados relevantes de pruebas de resiliencia.

### Requisito 4: Politicas de seguridad TIC (Articulos 9 a 16)

DORA detalla requisitos especificos para areas concretas de la seguridad:

- **Gestion de identidades y acceso** (Articulo 9.4b): principio de minimo privilegio, revision periodica de permisos, autenticacion multifactor para sistemas criticos.
- **Gestion de cambios TIC** (Articulo 9.4e): procedimientos formales para cambios en sistemas, con evaluacion de impacto, pruebas previas y capacidad de rollback.
- **Cifrado** (Articulo 10): politica de cifrado en transito y en reposo adaptada a la clasificacion de los datos.
- **Seguridad de redes** (Articulo 11): segmentacion adecuada, monitorizacion del trafico, proteccion perimetral y gestion de conexiones remotas.
- **Gestion de la continuidad de negocio TIC** (Articulos 11 y 12): planes de continuidad probados, sitios de recuperacion, comunicaciones de crisis y planes de comunicacion externa.
- **Aprendizaje y evolucion** (Articulo 13): las entidades deben aprender de incidentes propios y ajenos, integrando las lecciones en la mejora continua del marco.

## Pilar 2: Gestion, clasificacion y notificacion de incidentes TIC (Articulos 17 a 23)

Este pilar establece un proceso armonizado para toda la UE en la gestion de incidentes relacionados con las TIC. El objetivo es doble: asegurar que las entidades gestionan los incidentes de forma eficaz y que las autoridades supervisoras tienen visibilidad en tiempo util.

### Requisito 5: Proceso de gestion de incidentes (Articulo 17)

Las entidades financieras deben establecer un proceso de gestion de incidentes TIC que incluya:

- Indicadores de alerta temprana para la deteccion rapida de incidentes.
- Procedimientos para identificar, registrar, clasificar y notificar incidentes TIC.
- Roles y responsabilidades claros, incluida la activacion de planes de respuesta.
- Planes de comunicacion interna (incluida escalacion a alta direccion) y externa (incluidos clientes afectados).
- Procedimientos para la preservacion de evidencias forenses.
- Analisis post-incidente obligatorio para incidentes graves, con identificacion de causas raiz y acciones correctivas.

### Requisito 6: Clasificacion de incidentes (Articulo 18)

DORA establece criterios armonizados para clasificar los incidentes TIC. Los criterios principales son:

| Criterio | Descripcion |
|---|---|
| Numero de clientes afectados | Umbrales absolutos y relativos respecto a la base total |
| Duracion del incidente | Tiempo desde deteccion hasta resolucion completa |
| Extension geografica | Numero de estados miembros afectados |
| Perdidas de datos | Volumen y criticidad de los datos comprometidos |
| Criticidad de los servicios | Impacto en servicios criticos o funciones esenciales |
| Impacto economico | Costes directos e indirectos estimados |

Un incidente se clasifica como **grave** cuando supera los umbrales establecidos en al menos uno de estos criterios. Las Autoridades Europeas de Supervision (ESAs) han publicado normas tecnicas de regulacion (RTS) que detallan los umbrales concretos.

### Requisito 7: Notificacion de incidentes graves (Articulos 19 a 23)

El regimen de notificacion es uno de los aspectos mas operativos de DORA. Las entidades deben enviar tres tipos de notificaciones a su autoridad competente:

1. **Notificacion inicial**: dentro de las **4 horas** desde la clasificacion del incidente como grave (y no mas de 24 horas desde la deteccion). Debe incluir informacion basica sobre el incidente, el impacto estimado y las primeras medidas adoptadas.
2. **Notificacion intermedia**: dentro de las **72 horas** desde la notificacion inicial. Actualiza la informacion con datos mas concretos sobre el alcance, la causa raiz identificada y las acciones de remediacion en curso.
3. **Informe final**: dentro de **1 mes** desde el envio de la notificacion intermedia. Incluye el analisis completo de causas raiz, el impacto real, las medidas correctivas implementadas y las lecciones aprendidas.

Para ilustrar el impacto operativo: si una entidad detecta un ataque de ransomware a las 10:00 del lunes, debe clasificarlo antes de las 10:00 del martes, enviar la notificacion inicial antes de las 14:00 del martes (si clasifica a las 10:00), la notificacion intermedia antes del jueves, y el informe final antes de un mes despues. Estos plazos son exigentes y requieren procesos bien engrasados.

Ademas, DORA contempla la posibilidad de que las entidades notifiquen voluntariamente ciberamenazas significativas, aunque no hayan materializado un incidente. Esto alimenta el sistema de inteligencia colectiva del sector.

{{< cta type="tofu" text="Riskitera cubre los requisitos tecnicos de DORA, ENS y NIS2 con una arquitectura soberana. Automatiza la clasificacion de incidentes y genera notificaciones conformes a los plazos regulatorios." label="Ver arquitectura" >}}

## Pilar 3: Pruebas de resiliencia operativa digital (Articulos 24 a 27)

Cumplir DORA no es solo tener documentacion y politicas. Las entidades deben demostrar que sus sistemas y procesos funcionan bajo presion real. Este pilar establece un programa de pruebas obligatorio con dos niveles de exigencia.

### Requisito 8: Programa general de pruebas (Articulo 24 y 25)

Todas las entidades financieras cubiertas por DORA deben establecer un programa de pruebas de resiliencia operativa digital. Este programa debe:

- Formar parte integral del marco de gestion de riesgos TIC.
- Cubrir todos los sistemas, procesos y personal que soportan funciones criticas o importantes.
- Ejecutarse al menos **una vez al anio** para los sistemas y aplicaciones criticos.
- Ser proporcional al tamano de la entidad y a la naturaleza de sus servicios.

Las pruebas basicas que DORA contempla incluyen:

- **Evaluaciones de vulnerabilidades**: escaneos regulares de todos los sistemas TIC, con remediacion priorizada segun criticidad.
- **Pruebas de rendimiento**: verificacion de que los sistemas soportan los volumenes de operacion esperados, incluidos picos de demanda.
- **Pruebas de penetracion**: tests ofensivos que simulan ataques reales contra la infraestructura, las aplicaciones y las interfaces.
- **Pruebas de codigo fuente abierto**: revision de componentes open source utilizados, incluyendo analisis de vulnerabilidades conocidas (CVE).
- **Pruebas de compatibilidad**: verificacion de que los cambios en sistemas no afectan la interoperabilidad.
- **Pruebas de continuidad de negocio**: simulacros de recuperacion ante desastres, incluida la activacion de sitios secundarios.
- **Pruebas de escenarios**: simulacion de escenarios de amenazas realistas basados en inteligencia de amenazas actual.

### Requisito 9: Pruebas avanzadas TLPT (Articulos 26 y 27)

Las pruebas TLPT (Threat-Led Penetration Testing) son el nivel mas exigente del programa de pruebas de DORA. Estan inspiradas en el marco TIBER-EU del Banco Central Europeo, pero ahora tienen base legal vinculante.

Las TLPT son obligatorias para entidades **identificadas por las autoridades competentes** como significativas en terminos de riesgo sistemico. Los criterios incluyen tamano, cuota de mercado, interconexion con el sistema financiero y naturaleza de los servicios prestados.

Caracteristicas clave de las TLPT:

- Se ejecutan al menos cada **3 anios**.
- Deben cubrir varias o todas las funciones criticas o importantes de la entidad.
- Se realizan en el entorno de **produccion en vivo**.
- Deben ser ejecutadas por **testers externos** independientes, certificados y con experiencia demostrable.
- El equipo de inteligencia de amenazas (threat intelligence) que define los escenarios debe ser independiente del equipo de testeo (red team).
- La entidad debe involucrar a un equipo interno de defensa (blue team) que no sepa que las pruebas se estan realizando (para medir la capacidad real de deteccion).

Un aspecto importante: los proveedores TIC criticos de la entidad pueden verse incluidos en el alcance de las TLPT. Esto significa que una entidad financiera puede necesitar coordinar pruebas en vivo que afecten a la infraestructura de sus proveedores cloud, con las complejidades logisticas y contractuales que ello implica.

Al finalizar las TLPT, la entidad debe presentar a la autoridad competente un informe resumido con los hallazgos, las evidencias de remediacion y la certificacion del tester externo.

## Pilar 4: Gestion de riesgo de terceros proveedores TIC (Articulos 28 a 44)

Este pilar es probablemente el mas disruptivo de DORA. Reconoce que la resiliencia de una entidad financiera depende directamente de la resiliencia de sus proveedores tecnologicos, y establece un marco de supervision sin precedentes.

### Requisito 10: Principios generales de gestion de terceros TIC (Articulos 28 a 30)

Las entidades financieras deben gestionar el riesgo de terceros proveedores TIC como parte integral de su marco de gestion de riesgos. Esto implica:

- **Registro de proveedores**: mantener un registro actualizado de todos los acuerdos contractuales con proveedores TIC, clasificados por criticidad. Este registro debe estar disponible para las autoridades competentes.
- **Evaluacion previa a la contratacion**: antes de contratar un proveedor TIC para funciones criticas, realizar una evaluacion de riesgos que incluya capacidad tecnica, situacion financiera, concentracion de riesgo y ubicacion geografica del procesamiento de datos.
- **Estrategia de salida**: cada acuerdo con un proveedor critico debe contemplar un plan de salida viable, con periodos de transicion adecuados y sin degradacion del servicio.
- **Concentracion de riesgo**: evitar la dependencia excesiva de un unico proveedor TIC para funciones criticas. Las autoridades supervisoras evaluaran el riesgo de concentracion a nivel de mercado.

Un ejemplo concreto: si un banco utiliza AWS para su core bancario, Azure para el sistema de pagos y Google Cloud para analitica, DORA exige que documente las dependencias, los riesgos de concentracion (tres hyperscalers estadounidenses), las alternativas viables y los planes de salida para cada uno.

### Requisito 11: Clausulas contractuales obligatorias (Articulos 30 a 32)

DORA establece un listado minimo de clausulas que deben incluirse en los contratos con proveedores TIC que soporten funciones criticas o importantes:

- Descripcion clara y completa de los servicios prestados, incluidos niveles de servicio (SLA) cuantificables.
- Ubicacion del procesamiento de datos (incluidos centros de datos y paises).
- Obligacion del proveedor de asistir en caso de incidente TIC.
- Derechos de acceso, inspeccion y auditoria por parte de la entidad y de las autoridades supervisoras.
- Garantias de disponibilidad, autenticidad, integridad y confidencialidad de los datos.
- Obligacion de cooperar con las autoridades de supervision del marco de oversight.
- Clausulas de terminacion y planes de salida con periodos de transicion adecuados.
- Obligacion de notificar cualquier subcontratacion que afecte a funciones criticas.

Estas clausulas no son negociables. Si un proveedor cloud se niega a incluir derechos de auditoria o a especificar la ubicacion del procesamiento, la entidad financiera no puede contratarlo para funciones criticas. Esto ha forzado a los grandes proveedores tecnologicos a adaptar sus condiciones contractuales para el mercado financiero europeo.

### Requisito 12: Marco de supervision de proveedores TIC criticos (Articulos 31 a 44)

Esta es la innovacion mas significativa de DORA: un marco de supervision directa de la UE sobre proveedores TIC designados como criticos. Las ESAs (EBA, EIOPA y ESMA), junto con la Comision Europea, designan que proveedores son criticos basandose en:

- El caracter sistemico del proveedor para el sector financiero.
- El grado de dependencia de las entidades financieras respecto a dicho proveedor.
- La sustituibilidad del proveedor.

Para cada proveedor critico, se designa un **supervisor principal** (Lead Overseer) entre las tres ESAs. Este supervisor tiene poderes significativos:

- Solicitar informacion y documentacion completa.
- Realizar inspecciones in situ y remotas.
- Emitir recomendaciones vinculantes.
- Imponer multas coercitivas de hasta el 1% de la facturacion diaria global del proveedor en caso de incumplimiento.

Este marco es especialmente relevante para los grandes hyperscalers (AWS, Azure, Google Cloud), los proveedores SaaS financieros y las empresas de infraestructura critica (telecomunicaciones, centros de datos). Por primera vez, la UE puede supervisar directamente a proveedores tecnologicos que, aunque no sean entidades financieras, son criticos para la estabilidad del sistema financiero.

## Pilar 5: Acuerdos de intercambio de informacion (Articulo 45)

### Comparticion de informacion sobre ciberamenazas

DORA fomenta (sin obligar) el intercambio de informacion sobre ciberamenazas entre entidades financieras. El Articulo 45 establece que las entidades pueden participar en acuerdos de intercambio de informacion siempre que:

- La participacion sea voluntaria.
- Se protejan los datos personales y la informacion confidencial de negocio.
- Los acuerdos se notifiquen a las autoridades competentes.
- Se compartan indicadores de compromiso (IoC), tacticas, tecnicas y procedimientos (TTP), alertas de ciberseguridad e informacion sobre herramientas de analisis.

Aunque este pilar es voluntario, las autoridades supervisoras lo valoran positivamente. Las entidades que participan en ISACs (Information Sharing and Analysis Centers) sectoriales estan mejor posicionadas para cumplir con DORA, ya que demuestran un enfoque proactivo hacia la resiliencia.

El intercambio de informacion es especialmente valioso en el sector financiero por la naturaleza interconectada de las operaciones. Un ataque dirigido a una entidad puede ser precursor de campanas mas amplias. Compartir inteligencia de amenazas permite al sector anticiparse colectivamente.

## Plazos y calendario de cumplimiento

DORA establece un calendario claro, con la mayoria de obligaciones ya aplicables:

| Hito | Fecha |
|---|---|
| Entrada en vigor del Reglamento | 16 enero 2023 |
| Aplicacion obligatoria | 17 enero 2025 |
| Publicacion de RTS/ITS por las ESAs | A lo largo de 2024-2025 |
| Primera ronda de designacion de proveedores criticos | 2025 |
| Primera ronda de TLPT (entidades significativas) | Antes de enero 2028 |

Las entidades que aun no han completado su adaptacion deben priorizar las areas de mayor riesgo: la gestion de terceros TIC (por la complejidad contractual), el proceso de notificacion de incidentes (por los plazos estrictos) y el marco de gobernanza (por la responsabilidad directa del organo de direccion).

## Guia practica de implementacion: por donde empezar

Para las entidades que necesitan estructurar su programa de cumplimiento, esta es una hoja de ruta pragmatica:

### Fase 1: Diagnostico (semanas 1 a 4)

- Realizar un gap analysis entre la situacion actual y los 12 requisitos de DORA.
- Identificar las funciones criticas e importantes de la entidad.
- Inventariar todos los proveedores TIC y clasificarlos por criticidad.
- Evaluar la madurez del proceso de gestion de incidentes actual.

### Fase 2: Diseno del marco (semanas 5 a 12)

- Establecer la gobernanza: roles, responsabilidades, comites, lineas de reporte al organo de direccion.
- Disenar el marco de gestion de riesgos TIC alineado con los Articulos 6 a 16.
- Definir el proceso de clasificacion y notificacion de incidentes conforme a los Articulos 17 a 23.
- Revisar y actualizar todos los contratos con proveedores TIC criticos.

### Fase 3: Implementacion (semanas 13 a 24)

- Desplegar las politicas y procedimientos aprobados.
- Implementar controles tecnicos pendientes (cifrado, segmentacion, monitorizacion).
- Formar al personal, incluido el organo de direccion.
- Establecer el programa de pruebas de resiliencia.

### Fase 4: Validacion y mejora continua (semanas 25 en adelante)

- Ejecutar la primera ronda de pruebas de resiliencia.
- Realizar un simulacro de notificacion de incidentes.
- Auditar el cumplimiento del marco y documentar las evidencias.
- Planificar la preparacion para TLPT si la entidad es designada como significativa.

{{< cta type="bofu" text="Agenda una demo tecnica para tu sector y valida la integracion con tu infraestructura. Riskitera automatiza el cumplimiento de DORA con IA soberana y alojamiento 100% en la UE." label="Agenda demo" >}}

## Sanciones por incumplimiento

DORA no establece un regimen sancionador propio con cuantias fijas (a diferencia de GDPR). En su lugar, delega en las autoridades competentes nacionales la imposicion de sanciones administrativas y medidas correctivas. Sin embargo, las multas coercitivas para proveedores TIC criticos si estan definidas a nivel europeo: hasta el 1% de la facturacion diaria global media del ejercicio anterior, por cada dia de incumplimiento.

En la practica, las autoridades nacionales (como el Banco de Espana o la CNMV) pueden imponer sanciones significativas bajo sus marcos regulatorios existentes, reforzados por DORA. Ademas, el incumplimiento de DORA puede ser un agravante en procedimientos sancionadores relacionados con otros marcos (como MiFID II o Solvencia II).

**Articulos relacionados:**
- [Dora Reglamento Ciberseguridad Financiera](/es/posts/2026/04/dora-reglamento-ciberseguridad-financiera/)

## Preguntas frecuentes

### Que entidades financieras estan obligadas a cumplir DORA?

DORA se aplica a mas de 20 tipos de entidades financieras: entidades de credito, empresas de inversion, entidades de pago, entidades de dinero electronico, empresas de seguros y reaseguros, fondos de pensiones de empleo, proveedores de servicios de criptoactivos, depositarios centrales de valores, sociedades de gestion, agencias de calificacion crediticia y, de forma relevante, proveedores TIC terceros que prestan servicios a cualquiera de estos. Las microempresas tienen un regimen simplificado, pero no estan exentas.

### En que se diferencia DORA de NIS2 para el sector financiero?

NIS2 establece requisitos generales de ciberseguridad para sectores esenciales e importantes, mientras que DORA es el regimen especifico (lex specialis) para el sector financiero. Cuando ambas normas se solapan, se aplica DORA. Las diferencias principales son: DORA tiene requisitos mas detallados sobre gestion de terceros TIC, establece un marco de supervision directa sobre proveedores criticos (que NIS2 no contempla) e impone pruebas TLPT obligatorias. NIS2, por su parte, tiene un alcance sectorial mas amplio y sus propios mecanismos de notificacion de incidentes.

### Que pasa si un proveedor cloud se niega a incluir las clausulas contractuales que exige DORA?

La entidad financiera no puede utilizar ese proveedor para funciones criticas o importantes si no cumple con los requisitos contractuales del Articulo 30. En la practica, los principales proveedores cloud (AWS, Azure, Google Cloud) ya han adaptado sus condiciones contractuales para el mercado financiero europeo. Si un proveedor se niega, la entidad debe buscar alternativas o reclasificar la funcion como no critica (si esto es justificable). La autoridad supervisora puede cuestionar cualquier clasificacion que considere artificialmente baja.

### Es obligatorio realizar pruebas TLPT para todas las entidades?

No. Las pruebas TLPT solo son obligatorias para entidades que las autoridades competentes identifiquen como significativas en terminos de riesgo sistemico. Los criterios incluyen tamano, cuota de mercado, interconexion con el sistema financiero y naturaleza de los servicios. Tipicamente, esto incluye a los grandes bancos, aseguradoras sistemicas y plataformas de mercados. Las demas entidades deben realizar pruebas de resiliencia basicas (evaluaciones de vulnerabilidades, pruebas de penetracion, simulacros de continuidad), pero no TLPT.

### Cuanto tiempo lleva implementar el cumplimiento completo de DORA?

El tiempo de implementacion depende de la madurez de la entidad. Una entidad con certificacion ISO 27001 y procesos de gestion de riesgos TIC consolidados puede necesitar entre 6 y 12 meses para cubrir los gaps especificos de DORA (especialmente en gestion de terceros y preparacion para TLPT). Para entidades con menor madurez, el proceso puede extenderse a 12 o 18 meses. La clave es empezar con un gap analysis riguroso que permita priorizar las areas de mayor riesgo y mayor distancia respecto a los requisitos.
