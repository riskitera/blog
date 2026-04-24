---
title: "Politicas de seguridad informatica: como crearlas desde cero"
image: "cover.png"
description: "Guia completa para crear politicas de seguridad informatica: tipos de politicas, proceso de redaccion y aprobacion, comunicacion a empleados, ciclo de revision y plantillas alineadas con ENS e ISO 27001."
slug: "politicas-seguridad-informatica-como-crearlas"
date: 2026-04-06
lastmod: 2026-04-06
draft: false
tags: ["GRC", "Politicas", "Compliance"]
categories: ["GRC"]
author: "Riskitera Team"
translationKey: "security-policies-guide"
---

Las politicas de seguridad informatica son los documentos fundamentales que establecen las reglas, principios y directrices que rigen la proteccion de la informacion en una organizacion. Sin politicas claras, aprobadas y comunicadas, la seguridad depende de decisiones individuales inconsistentes, lo que genera brechas, incumplimientos normativos y una postura de seguridad fragil. Segun datos del CCN-CERT, un porcentaje significativo de los incidentes de seguridad en organismos publicos espanoles tiene su origen en la ausencia o el desconocimiento de politicas basicas. Esta guia explica que son las politicas de seguridad, que tipos necesita tu organizacion, como redactarlas, aprobarlas, comunicarlas y mantenerlas actualizadas.

<!--more-->

## Que son las politicas de seguridad informatica

Una politica de seguridad informatica es un documento formal que define la posicion de la organizacion respecto a un aspecto concreto de la proteccion de la informacion. Establece que esta permitido y que no, quien es responsable de que y cuales son las consecuencias de su incumplimiento.

Las politicas se situan en la capa mas alta del marco documental de seguridad. Por debajo se encuentran los procedimientos (como implementar la politica paso a paso), las instrucciones tecnicas (como configurar un sistema concreto para cumplir la politica) y los registros (evidencias de que la politica se esta cumpliendo).

Esta jerarquia documental es fundamental para la gestion eficaz de la seguridad. Las politicas cambian con poca frecuencia porque expresan principios generales. Los procedimientos y las instrucciones tecnicas cambian con mas frecuencia para adaptarse a la evolucion tecnologica, sin necesidad de modificar la politica que los sustenta.

ISO 27001 exige una politica de seguridad de la informacion de alto nivel como requisito del SGSI, ademas de politicas especificas para areas como el control de accesos, la clasificacion de la informacion o el uso aceptable de los recursos. El [Esquema Nacional de Seguridad (ENS)](/es/posts/que-es-esquema-nacional-seguridad-ens/) requiere una politica de seguridad aprobada por el organo competente que articule la gestion continuada de la seguridad.

## Tipos de politicas de seguridad esenciales

Cada organizacion necesita un conjunto de politicas adaptado a su tamano, sector y requisitos normativos. Los siguientes tipos son los mas comunes y necesarios.

### Politica de seguridad de la informacion

Es la politica de nivel superior que establece el compromiso de la direccion con la seguridad de la informacion, los objetivos generales de seguridad, el alcance del programa de seguridad, los roles y responsabilidades de alto nivel y los principios fundamentales que guian todas las demas politicas. Es un requisito explicito de ISO 27001 (clausula 5.2) y del ENS.

Esta politica debe ser breve (dos a cuatro paginas), aprobada por la alta direccion y comunicada a todo el personal. No debe contener detalles tecnicos sino principios y compromisos de nivel estrategico.

### Politica de uso aceptable

Define las reglas para el uso de los recursos tecnologicos de la organizacion: equipos informaticos, correo electronico, acceso a internet, dispositivos moviles y cualquier otro recurso proporcionado por la empresa. Establece que usos estan permitidos (uso profesional, uso personal limitado), que usos estan prohibidos (descarga de software no autorizado, acceso a contenidos ilicitos, uso de servicios cloud no aprobados) y las consecuencias de su incumplimiento.

Es una de las politicas mas importantes desde el punto de vista legal, ya que define las expectativas sobre el comportamiento del empleado y establece la base para acciones disciplinarias en caso de incumplimiento. Debe firmarse por todo el personal como condicion de acceso a los sistemas.

### Politica de control de accesos

Establece los principios para la gestion de identidades y accesos a los sistemas de informacion. Los principios fundamentales que suele incluir son:

**Minimo privilegio:** cada usuario recibe unicamente los accesos estrictamente necesarios para realizar sus funciones.

**Necesidad de conocer:** el acceso a la informacion se concede solo a quien lo necesita para su trabajo.

**Segregacion de funciones:** las funciones criticas se distribuyen entre diferentes personas para evitar fraudes o errores.

**Revision periodica:** los accesos se revisan regularmente para detectar y revocar permisos innecesarios.

La politica debe cubrir la gestion del ciclo de vida de las cuentas (alta, modificacion, baja), los requisitos de autenticacion (contrasenas, MFA), la gestion de cuentas privilegiadas y el acceso de terceros.

### Politica de respuesta a incidentes

Define el marco para la gestion de incidentes de seguridad: como se detectan, clasifican, comunican, investigan, resuelven y documentan. Establece los roles del equipo de respuesta, los canales de comunicacion, los criterios de escalado, los tiempos de respuesta objetivo y las obligaciones de notificacion a reguladores (RGPD exige la notificacion de brechas de datos personales a la autoridad de control en un plazo maximo de 72 horas).

Esta politica es critica no solo para la operativa diaria sino para el cumplimiento normativo. NIS2, DORA y el ENS tienen requisitos especificos sobre la gestion y notificacion de incidentes que la politica debe reflejar.

### Politica de BYOD (Bring Your Own Device)

Regula el uso de dispositivos personales (portatiles, smartphones, tablets) para acceder a recursos corporativos. Debe abordar los requisitos de seguridad minimos para los dispositivos (cifrado, antivirus, actualizaciones), las aplicaciones permitidas para acceso corporativo, la separacion entre datos personales y corporativos, las capacidades de borrado remoto en caso de perdida o robo y las responsabilidades del empleado.

En el contexto del trabajo hibrido, esta politica es cada vez mas relevante. La ausencia de normas claras sobre BYOD genera riesgos significativos de fuga de informacion y acceso no autorizado.

### Politica de trabajo remoto

Complementaria a la de BYOD, esta politica establece las condiciones de seguridad para el teletrabajo: requisitos de la conexion (VPN obligatoria, redes wifi seguras), gestion de la informacion fuera de la oficina (prohibicion de imprimir documentos clasificados, bloqueo de pantalla), seguridad fisica del puesto de trabajo remoto y procedimientos de soporte tecnico.

La normativa laboral espanola sobre teletrabajo (Ley 10/2021) exige que el acuerdo de trabajo a distancia incluya medios de proteccion de datos, lo que refuerza la necesidad de esta politica.

### Politica de contrasenas y autenticacion

Establece los requisitos para la creacion, uso y gestion de contrasenas. Las recomendaciones actuales, alineadas con las directrices del NIST (SP 800-63B) y el CCN, priorizan la longitud sobre la complejidad arbitraria:

Contrasenas de al menos 12 caracteres para usuarios generales y 16 para cuentas privilegiadas. Uso obligatorio de autenticacion multifactor (MFA) para accesos remotos, cuentas privilegiadas y sistemas criticos. Prohibicion de reutilizar contrasenas entre servicios. Uso recomendado de gestores de contrasenas corporativos. Prohibicion de compartir credenciales entre empleados.

Esta politica ha evolucionado significativamente en los ultimos anos. Las rotaciones obligatorias frecuentes (cada 30 o 90 dias) ya no se recomiendan salvo tras incidentes, ya que estudios demuestran que llevan a los usuarios a crear contrasenas mas debiles y predecibles.

### Politica de clasificacion de la informacion

Define los niveles de clasificacion de la informacion (por ejemplo: publica, interna, confidencial, restringida) y los controles de seguridad aplicables a cada nivel. Para cada nivel de clasificacion, la politica establece como debe almacenarse, transmitirse, compartirse y destruirse la informacion.

El ENS define niveles de informacion (bajo, medio, alto) en las dimensiones de seguridad que se alinean con los esquemas de clasificacion. ISO 27001 requiere un esquema de clasificacion documentado como parte del Anexo A.

Sin una clasificacion de informacion operativa, es imposible aplicar controles de seguridad proporcionales: o se protege toda la informacion con el mismo nivel (costoso y poco practico) o se toman decisiones arbitrarias e inconsistentes.

## Como redactar politicas de seguridad eficaces

La calidad de la redaccion determina la utilidad practica de las politicas. Una politica mal escrita, aunque tecnicamente correcta, no sera comprendida ni aplicada.

### Estructura recomendada

Cada politica debe seguir una estructura coherente que facilite su lectura y consulta:

**Encabezado:** titulo, version, fecha de aprobacion, responsable, clasificacion del documento.

**Proposito:** que objetivo persigue la politica y por que es necesaria. Debe ser conciso y comprensible para cualquier empleado.

**Alcance:** a quien aplica (todo el personal, personal de TI, terceros) y a que sistemas o procesos.

**Definiciones:** terminos tecnicos o especificos que se utilizan en el documento.

**Principios y directrices:** el cuerpo de la politica, con las reglas y requisitos formulados de forma clara e inequivoca.

**Roles y responsabilidades:** quien es responsable de que en relacion con la politica.

**Cumplimiento y excepciones:** consecuencias del incumplimiento y proceso para solicitar excepciones justificadas.

**Referencias:** normativas, estandares u otras politicas relacionadas.

**Historial de versiones:** registro de cambios desde la version original.

### Principios de redaccion

**Claridad.** Utilizar un lenguaje comprensible para la audiencia a la que se dirige. Si la politica aplica a todo el personal, debe evitar la jerga tecnica innecesaria. Si se dirige a administradores de sistemas, puede utilizar terminologia tecnica apropiada.

**Precision.** Las directrices deben ser especificas y medibles. En lugar de "las contrasenas deben ser seguras", escribir "las contrasenas deben tener un minimo de 12 caracteres". En lugar de "los datos deben respaldarse regularmente", escribir "los datos criticos deben respaldarse diariamente con una retencion minima de 30 dias".

**Brevedad.** Las politicas deben ser tan cortas como sea posible sin sacrificar la precision. Los detalles de implementacion pertenecen a los procedimientos, no a las politicas. Una politica que supera las 10 paginas probablemente esta mezclando politica y procedimiento.

**Viabilidad.** Toda directriz debe ser realista y ejecutable. Establecer requisitos imposibles de cumplir (por ejemplo, exigir cambio de contrasena diario) no mejora la seguridad sino que genera incumplimiento generalizado y desacredita el programa de politicas.

**Consistencia.** Las diferentes politicas deben utilizar terminologia, estructura y estilo coherentes. Las contradicciones entre politicas generan confusion y erosionan la confianza en el marco documental.

## Proceso de aprobacion

La aprobacion formal es lo que transforma un documento de trabajo en una politica con autoridad y fuerza de obligado cumplimiento.

### Flujo de aprobacion recomendado

1. **Borrador inicial** elaborado por el responsable de seguridad de la informacion o el equipo de seguridad, basandose en los requisitos normativos, las mejores practicas y las necesidades de la organizacion.

2. **Revision tecnica** por los equipos de TI y operaciones para verificar la viabilidad tecnica de las directrices.

3. **Revision legal** por el departamento juridico para asegurar la conformidad con la legislacion laboral, la proteccion de datos y otras normativas aplicables.

4. **Revision de recursos humanos** para validar que las directrices sobre comportamiento del personal y las consecuencias de incumplimiento son compatibles con la normativa laboral y los convenios colectivos.

5. **Aprobacion por la direccion.** La politica de seguridad de la informacion de alto nivel debe ser aprobada por la alta direccion (CEO, comite de direccion). Las politicas especificas pueden ser aprobadas por el CISO o el responsable de seguridad, segun el esquema de delegacion de la organizacion.

6. **Publicacion y comunicacion** a todo el personal afectado.

El ENS establece explicitamente que la politica de seguridad debe ser aprobada por el organo superior competente. ISO 27001 requiere que la politica sea apropiada al proposito de la organizacion y aprobada por la alta direccion.

### Gestion de excepciones

Toda politica debe incluir un proceso formal para gestionar excepciones. Existiran situaciones en las que un requisito de la politica no pueda cumplirse por razones tecnicas, operativas o economicas justificadas. El proceso de excepciones debe definir quien puede solicitar una excepcion, quien la aprueba, que informacion debe proporcionarse (justificacion, riesgo residual, medidas compensatorias, duracion de la excepcion) y como se documenta y revisa periodicamente.

Las excepciones sin proceso formal son una fuente frecuente de riesgo y de hallazgos en [auditorias de seguridad](/es/posts/auditoria-seguridad-informatica-guia/).

## Comunicacion a los empleados

Una politica aprobada pero desconocida por el personal es tan inutil como la ausencia de politica. La comunicacion es una fase critica que muchas organizaciones descuidan.

### Estrategias de comunicacion eficaces

**Sesiones de presentacion.** Al publicar una nueva politica o una actualizacion significativa, realizar sesiones presenciales o virtuales donde se explique su contenido, las razones de su existencia y su impacto en el trabajo diario. Estas sesiones permiten resolver dudas y recoger feedback.

**Formacion integrada.** Incluir las politicas de seguridad en el programa de formacion obligatoria de la organizacion. Las sesiones de concienciacion en seguridad deben hacer referencia constante a las politicas aplicables.

**Accesibilidad.** Las politicas deben estar publicadas en un lugar accesible para todo el personal: intranet, repositorio documental corporativo o plataforma de gestion documental. El personal debe poder consultarlas en cualquier momento.

**Recordatorios periodicos.** Utilizar comunicaciones internas (newsletter, correos, carteles) para recordar periodicamente las politicas clave. Los recordatorios son especialmente importantes para politicas que afectan al comportamiento diario, como la politica de uso aceptable o la de contrasenas.

**Acuse de recibo.** Para politicas criticas, solicitar que cada empleado confirme que ha leido y comprendido el documento. Este acuse de recibo, ademas de reforzar la comunicacion, constituye una evidencia de cumplimiento valiosa para auditorias.

### Adaptacion al publico

No todo el personal necesita conocer todas las politicas con el mismo nivel de detalle. La comunicacion debe adaptarse a la audiencia: la direccion necesita comprender los principios y las implicaciones de negocio; el personal general necesita saber que reglas le aplican directamente y como cumplirlas; el personal tecnico necesita ademas los detalles que le permitan implementar y operar los controles.

## Ciclo de revision y actualizacion

Las politicas de seguridad no son documentos estaticos. Deben revisarse y actualizarse de forma periodica y ante eventos significativos.

### Revision periodica

Se recomienda una revision completa de cada politica al menos una vez al ano. La revision debe evaluar si la politica sigue siendo relevante y adecuada, si los requisitos normativos han cambiado, si la tecnologia ha evolucionado de forma que afecte a la politica, si se han producido incidentes que revelen deficiencias y si el feedback del personal indica areas de mejora.

### Actualizacion ante eventos

Ademas de la revision periodica, las politicas deben actualizarse ante cambios significativos: nueva normativa aplicable (por ejemplo, la entrada en vigor de NIS2), cambios organizativos relevantes (fusiones, adquisiciones, reorganizaciones), incidentes de seguridad que revelen carencias en las politicas existentes, adopcion de nuevas tecnologias con implicaciones de seguridad (cloud, IA, IoT) o resultados de auditorias que identifiquen no conformidades en politicas.

### Control de versiones

Cada politica debe tener un sistema de control de versiones que identifique claramente la version vigente, la fecha de aprobacion, los cambios realizados respecto a la version anterior y el historial completo de versiones. El acceso a versiones obsoletas debe restringirse o marcarse claramente para evitar que el personal consulte documentos no vigentes.

## Plantillas y recursos

Para organizaciones que crean politicas por primera vez, las plantillas proporcionan un punto de partida valioso que acelera significativamente el proceso.

### Fuentes de plantillas

**INCIBE** publica plantillas y guias para la elaboracion de politicas de seguridad orientadas a pymes, disponibles gratuitamente en su portal web.

**CCN-CERT** proporciona modelos documentales para el cumplimiento del ENS, incluyendo la politica de seguridad y documentos asociados, a traves de las guias CCN-STIC de la serie 800.

**ISO 27002** (version 2022) proporciona orientacion detallada para cada control del Anexo A de ISO 27001, que puede utilizarse como base para redactar politicas especificas.

**SANS Institute** ofrece plantillas de politicas de seguridad en ingles que cubren la mayoria de los tipos necesarios y que pueden adaptarse al contexto de cada organizacion.

Riskitera incluye plantillas de politicas de seguridad alineadas con los requisitos del ENS e ISO 27001, personalizables segun el sector y el tamano de la organizacion, lo que permite a las empresas disponer de un marco documental de seguridad solido sin partir de cero.

### Adaptacion de plantillas

Las plantillas son un punto de partida, no un producto final. Toda plantilla debe adaptarse al contexto especifico de la organizacion: su sector, su tamano, su estructura organizativa, su entorno tecnologico, sus requisitos normativos y su cultura corporativa. Una politica copiada literalmente de una plantilla sin adaptacion sera generica, inadecuada y dificilmente aplicable.

## Errores comunes al crear politicas de seguridad

**Redactar politicas que nadie lee ni conoce.** La politica mas perfecta tecnicamente es inutil si el personal no la conoce. La comunicacion y la formacion son tan importantes como la redaccion.

**Crear politicas inviables.** Establecer requisitos que el personal no puede cumplir razonablemente genera incumplimiento generalizado y cinismo hacia el programa de seguridad. Las politicas deben ser ambiciosas pero realistas.

**No definir responsabilidades.** Cada politica debe asignar responsabilidades claras. Si nadie es responsable de verificar el cumplimiento, el cumplimiento no se verificara.

**Mezclar politica y procedimiento.** La politica establece el que y el por que; el procedimiento establece el como. Mezclar ambos genera documentos extensos, dificiles de mantener y que requieren actualizacion frecuente por cambios tecnicos que no afectan a los principios de la politica.

**No gestionar excepciones.** La rigidez absoluta no funciona en organizaciones reales. Un proceso formal de excepciones permite la flexibilidad necesaria sin comprometer la integridad del marco normativo.

**No actualizar las politicas.** Una politica de contrasenas que exige cambio cada 30 dias o que prohibe el teletrabajo cuando toda la organizacion trabaja en remoto erosiona la credibilidad de todo el marco documental. Las politicas deben reflejar la realidad actual de la organizacion.

## Preguntas frecuentes

### Cuantas politicas de seguridad necesita mi organizacion

No existe un numero fijo. Una pyme puede funcionar con 5 a 8 politicas fundamentales: politica de seguridad de la informacion, uso aceptable, control de accesos, gestion de incidentes, clasificacion de informacion, contrasenas, copias de seguridad y gestion de cambios. Una organizacion grande o altamente regulada puede necesitar 15 a 25 politicas que cubran areas adicionales como seguridad en el desarrollo de software, gestion de proveedores, seguridad fisica o continuidad de negocio. Lo importante es que cada politica responda a una necesidad real y se mantenga actualizada.

### Quien debe redactar las politicas de seguridad

El responsable de seguridad de la informacion (CISO) o el equipo de seguridad suele liderar la redaccion, pero el proceso debe involucrar a otros departamentos. TI aporta la perspectiva tecnica y de viabilidad. Legal verifica la conformidad normativa. Recursos humanos valida los aspectos laborales. Los responsables de negocio confirman que las politicas no obstaculizan las operaciones. La colaboracion multidisciplinar produce politicas mas equilibradas y aplicables.

### Las politicas de seguridad son obligatorias por ley

Varias normativas exigen directa o indirectamente la existencia de politicas de seguridad. El ENS requiere una politica de seguridad para todos los organismos publicos y empresas que trabajan con la administracion. El RGPD exige medidas organizativas de proteccion de datos, que se materializan en politicas. ISO 27001 exige una politica de seguridad como requisito para la certificacion. NIS2 obliga a las entidades esenciales e importantes a adoptar politicas de seguridad. Incluso sin un requisito legal explicito, las politicas de seguridad son una practica minima de diligencia debida que cualquier organizacion deberia mantener.

### Como consigo que los empleados cumplan las politicas

El cumplimiento requiere un enfoque multiple: comunicacion clara del contenido y el proposito de cada politica, formacion periodica con ejemplos practicos, apoyo de la direccion visible y consistente, controles tecnicos que faciliten el cumplimiento (por ejemplo, configurar el MFA obligatorio en lugar de confiarlo a la voluntad del usuario), consecuencias proporcionadas y conocidas ante el incumplimiento y un proceso de excepciones que evite la sensacion de rigidez excesiva. La cultura de seguridad se construye gradualmente y requiere consistencia y liderazgo.

### Puedo utilizar politicas genericas descargadas de internet

Las plantillas genericas son un punto de partida aceptable, pero nunca deben utilizarse sin adaptacion. Una politica que no refleja la realidad de tu organizacion (su tecnologia, sus procesos, su sector, su normativa aplicable) sera poco util y potencialmente contraproducente. El valor de una politica reside en su aplicabilidad al contexto concreto. Dedica tiempo a adaptar cada plantilla, validarla con los equipos relevantes y asegurar que las directrices son viables y pertinentes para tu organizacion.
