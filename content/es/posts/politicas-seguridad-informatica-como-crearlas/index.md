---
title: "Políticas de seguridad informática: como crearlas desde cero"
image: "cover.png"
description: "Guía completa para crear políticas de seguridad informática: tipos de políticas, proceso de redacción y aprobación, comunicación a empleados, ciclo de revisión y plantillas alineadas con ENS e ISO 27001."
slug: "politicas-seguridad-informatica-como-crearlas"
date: 2026-03-20
lastmod: 2026-03-20
draft: false
tags: ["GRC", "Políticas", "Compliance"]
categories: ["GRC"]
author: "David Moya"
translationKey: "security-policies-guide"
---

Las políticas de seguridad informática son los documentos fundamentales que establecen las reglas, principios y directrices que rigen la protección de la información en una organización. Sin políticas claras, aprobadas y comunicadas, la seguridad depende de decisiones individuales inconsistentes, lo que genera brechas, incumplimientos normativos y una postura de seguridad frágil. Según datos del [CCN-CERT](https://www.ccn-cert.cni.es/), un porcentaje significativo de los incidentes de seguridad en organismos públicos españoles tiene su origen en la ausencia o el desconocimiento de políticas básicas. Esta guía explica que son las políticas de seguridad, que tipos necesita tu organización, como redactarlas, aprobarlas, comunicarlas y mantenerlas actualizadas.

<!--more-->

{{< key-takeaways >}}
- Las políticas de seguridad son requisito de ISO 27001 (cláusula 5.2) y del ENS (marco organizativo)
- Tipos principales: política general, de control de acceso, de clasificación de información, de uso aceptable y de gestión de incidentes
- El ciclo de vida incluye redacción, aprobación por la dirección, comunicación y revisión periódica
- Deben estar alineadas con el marco normativo aplicable (ENS, ISO 27001, RGPD)
- La revisión periódica (al menos anual) es tan importante como la redacción inicial
{{< /key-takeaways >}}

## ¿Qué son las políticas de seguridad informática?

Una política de seguridad informática es un documento formal que define la posición de la organización respecto a un aspecto concreto de la protección de la información. Establece que está permitido y que no, quien es responsable de que y cuales son las consecuencias de su incumplimiento.

Las políticas se sitúan en la capa más alta del marco documental de seguridad. Por debajo se encuentran los procedimientos (como implementar la política paso a paso), las instrucciones técnicas (como configurar un sistema concreto para cumplir la política) y los registros (evidencias de que la política se esta cumpliendo).

Esta jerarquía documental es fundamental para la gestión eficaz de la seguridad. Las políticas cambian con poca frecuencia porque expresan principios generales. Los procedimientos y las instrucciones técnicas cambian con más frecuencia para adaptarse a la evolución tecnológica, sin necesidad de modificar la política que los sustenta.

[ISO 27001](https://www.iso.org/standard/27001) exige una política de seguridad de la información de alto nivel como requisito del SGSI, además de políticas específicas para áreas como el control de accesos, la clasificación de la información o el uso aceptable de los recursos. El [Esquema Nacional de Seguridad (ENS)](/es/posts/que-es-esquema-nacional-seguridad-ens/) requiere una política de seguridad aprobada por el órgano competente que articule la gestión continuada de la seguridad.

## ¿Qué tipos de políticas de seguridad son esenciales?

Cada organización necesita un conjunto de políticas adaptado a su tamaño, sector y requisitos normativos. Los siguientes tipos son los más comunes y necesarios.

### Política de seguridad de la información

Es la política de nivel superior que establece el compromiso de la dirección con la seguridad de la información, los objetivos generales de seguridad, el alcance del programa de seguridad, los roles y responsabilidades de alto nivel y los principios fundamentales que guían todas las demás políticas. Es un requisito explícito de ISO 27001 (cláusula 5.2) y del [ENS](https://www.boe.es/eli/es/rd/2022/05/03/311).

Esta política debe ser breve (dos a cuatro páginas), aprobada por la alta dirección y comunicada a todo el personal. No debe contener detalles técnicos sino principios y compromisos de nivel estratégico.

### Política de uso aceptable

Define las reglas para el uso de los recursos tecnológicos de la organización: equipos informáticos, correo electrónico, acceso a internet, dispositivos móviles y cualquier otro recurso proporcionado por la empresa. Establece que usos están permitidos (uso profesional, uso personal limitado), que usos están prohibidos (descarga de software no autorizado, acceso a contenidos ilicitos, uso de servicios cloud no aprobados) y las consecuencias de su incumplimiento.

Es una de las políticas más importantes desde el punto de vista legal, ya que define las expectativas sobre el comportamiento del empleado y establece la base para acciones disciplinarias en caso de incumplimiento. Debe firmarse por todo el personal como condición de acceso a los sistemas.

### Política de control de accesos

Establece los principios para la gestión de identidades y accesos a los sistemas de información. Los principios fundamentales que suele incluir son:

**Mínimo privilegio:** cada usuario recibe únicamente los accesos estrictamente necesarios para realizar sus funciones.

**Necesidad de conocer:** el acceso a la información se concede solo a quien lo necesita para su trabajo.

**Segregación de funciones:** las funciones críticas se distribuyen entre diferentes personas para evitar fraudes o errores.

**Revisión periódica:** los accesos se revisan regularmente para detectar y revocar permisos innecesarios.

La política debe cubrir la gestión del ciclo de vida de las cuentas (alta, modificación, baja), los requisitos de autenticación (contraseñas, MFA), la gestión de cuentas privilegiadas y el acceso de terceros.

### Política de respuesta a incidentes

Define el marco para la gestión de incidentes de seguridad: como se detectan, clasifican, comunican, investigan, resuelven y documentan. Establece los roles del equipo de respuesta, los canales de comunicación, los criterios de escalado, los tiempos de respuesta objetivo y las obligaciones de notificación a reguladores ([RGPD](https://eur-lex.europa.eu/eli/reg/2016/679) exige la notificación de brechas de datos personales a la autoridad de control en un plazo máximo de 72 horas).

Esta política es crítica no solo para la operativa diaria sino para el cumplimiento normativo. [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555), [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554) y el ENS tienen requisitos específicos sobre la gestión y notificación de incidentes que la política debe reflejar.

### Política de BYOD (Bring Your Own Device)

Regula el uso de dispositivos personales (portátiles, smartphones, tablets) para acceder a recursos corporativos. Debe abordar los requisitos de seguridad mínimos para los dispositivos (cifrado, antivirus, actualizaciónes), las aplicaciones permitidas para acceso corporativo, la separación entre datos personales y corporativos, las capacidades de borrado remoto en caso de pérdida o robo y las responsabilidades del empleado.

En el contexto del trabajo híbrido, esta política es cada vez más relevante. La ausencia de normas claras sobre BYOD genera riesgos significativos de fuga de información y acceso no autorizado.

### Política de trabajo remoto

Complementaria a la de BYOD, esta política establece las condiciones de seguridad para el teletrabajo: requisitos de la conexión (VPN obligatoria, redes wifi seguras), gestión de la información fuera de la oficina (prohibición de imprimir documentos clasificados, bloqueo de pantalla), seguridad física del puesto de trabajo remoto y procedimientos de soporte técnico.

La normativa laboral española sobre teletrabajo (Ley 10/2021) exige que el acuerdo de trabajo a distancia incluya medios de protección de datos, lo que refuerza la necesidad de esta política.

### Política de contraseñas y autenticación

Establece los requisitos para la creación, uso y gestión de contraseñas. Las recomendaciones actuales, alineadas con las directrices del NIST (SP 800-63B) y el CCN, priorizan la longitud sobre la complejidad arbitraria:

Contrasenas de al menos 12 caracteres para usuarios generales y 16 para cuentas privilegiadas. Uso obligatorio de autenticación multifactor (MFA) para accesos remotos, cuentas privilegiadas y sistemas críticos. Prohibición de reutilizar contraseñas entre servicios. Uso recomendado de gestores de contraseñas corporativos. Prohibición de compartir credenciales entre empleados.

Esta política ha evolucionado significativamente en los últimos años. Las rotaciones obligatorias frecuentes (cada 30 o 90 días) ya no se recomiendan salvo tras incidentes, ya que estudios demuestran que llevan a los usuarios a crear contraseñas más debiles y predecibles.

### Política de clasificación de la información

Define los niveles de clasificación de la información (por ejemplo: pública, interna, confidencial, restringida) y los controles de seguridad aplicables a cada nivel. Para cada nivel de clasificación, la política establece como debe almacenarse, transmitirse, compartirse y destruirse la información.

El ENS define niveles de información (bajo, medio, alto) en las dimensiones de seguridad que se alinean con los esquemas de clasificación. ISO 27001 requiere un esquema de clasificación documentado como parte del Anexo A.

Sin una clasificación de información operativa, es imposible aplicar controles de seguridad proporcionales: o se protege toda la información con el mismo nivel (costoso y poco práctico) o se toman decisiones arbitrarias e inconsistentes.

## ¿Cómo redactar políticas de seguridad eficaces?

La calidad de la redacción determina la utilidad práctica de las políticas. Una política mal escrita, aunque técnicamente correcta, no será comprendida ni aplicada.

### Estructura recomendada

Cada política debe seguir una estructura coherente que facilite su lectura y consulta:

**Encabezado:** título, versión, fecha de aprobación, responsable, clasificación del documento.

**Propósito:** que objetivo persigue la política y por que es necesaria. Debe ser conciso y comprensible para cualquier empleado.

**Alcance:** a quien aplica (todo el personal, personal de TI, terceros) y a que sistemas o procesos.

**Definiciones:** términos técnicos o específicos que se utilizan en el documento.

**Principios y directrices:** el cuerpo de la política, con las reglas y requisitos formulados de forma clara e inequívoca.

**Roles y responsabilidades:** quien es responsable de que en relación con la política.

**Cumplimiento y excepciones:** consecuencias del incumplimiento y proceso para solicitar excepciones justificadas.

**Referencias:** normativas, estándares u otras políticas relacionadas.

**Historial de versiones:** registro de cambios desde la versión original.

### Principios de redacción

**Claridad.** Utilizar un lenguaje comprensible para la audiencia a la que se dirige. Si la política aplica a todo el personal, debe evitar la jerga técnica innecesaria. Si se dirige a administradores de sistemas, puede utilizar terminologia técnica apropiada.

**Precisión.** Las directrices deben ser específicas y medibles. En lugar de "las contraseñas deben ser seguras", escribir "las contraseñas deben tener un mínimo de 12 caracteres". En lugar de "los datos deben respaldarse regularmente", escribir "los datos críticos deben respaldarse diariamente con una retención mínima de 30 días".

**Brevedad.** Las políticas deben ser tan cortas como sea posible sin sacrificar la precisión. Los detalles de implementación pertenecen a los procedimientos, no a las políticas. Una política que supera las 10 páginas probablemente esta mezclando política y procedimiento.

**Viabilidad.** Toda directriz debe ser realista y ejecutable. Establecer requisitos imposibles de cumplir (por ejemplo, exigir cambio de contraseña diario) no mejora la seguridad sino que genera incumplimiento generalizado y desacredita el programa de políticas.

**Consistencia.** Las diferentes políticas deben utilizar terminologia, estructura y estilo coherentes. Las contradicciones entre políticas generan confusión y erosionan la confianza en el marco documental.

## ¿Cómo es el proceso de aprobación de políticas de seguridad?

La aprobación formal es lo que transforma un documento de trabajo en una política con autoridad y fuerza de obligado cumplimiento.

### Flujo de aprobación recomendado

1. **Borrador inicial** elaborado por el responsable de seguridad de la información o el equipo de seguridad, basándose en los requisitos normativos, las mejores prácticas y las necesidades de la organización.

2. **Revisión técnica** por los equipos de TI y operaciones para verificar la viabilidad técnica de las directrices.

3. **Revisión legal** por el departamento jurídico para asegurar la conformidad con la legislación laboral, la protección de datos y otras normativas aplicables.

4. **Revisión de recursos humanos** para validar que las directrices sobre comportamiento del personal y las consecuencias de incumplimiento son compatibles con la normativa laboral y los convenios colectivos.

5. **Aprobación por la dirección.** La política de seguridad de la información de alto nivel debe ser aprobada por la alta dirección (CEO, comité de dirección). Las políticas específicas pueden ser aprobadas por el CISO o el responsable de seguridad, según el esquema de delegación de la organización.

6. **Publicación y comunicación** a todo el personal afectado.

El ENS establece explícitamente que la política de seguridad debe ser aprobada por el órgano superior competente. ISO 27001 requiere que la política sea apropiada al propósito de la organización y aprobada por la alta dirección.

### Gestión de excepciones

Toda política debe incluir un proceso formal para gestionar excepciones. Existiran situaciones en las que un requisito de la política no pueda cumplirse por razones técnicas, operativas o económicas justificadas. El proceso de excepciones debe definir quien puede solicitar una excepción, quien la aprueba, que información debe proporcionarse (justificación, riesgo residual, medidas compensatorias, duración de la excepción) y como se documenta y revisa periódicamente.

Las excepciones sin proceso formal son una fuente frecuente de riesgo y de hallazgos en [auditorías de seguridad](/es/posts/auditoria-seguridad-informatica-guia/).

## ¿Cómo comunicar las políticas de seguridad a los empleados?

Una política aprobada pero desconocida por el personal es tan inútil como la ausencia de política. La comunicación es una fase crítica que muchas organizaciones descuidan.

### Estrategias de comunicación eficaces

**Sesiones de presentación.** Al publicar una nueva política o una actualización significativa, realizar sesiones presenciales o virtuales donde se explique su contenido, las razones de su existencia y su impacto en el trabajo diario. Estas sesiones permiten resolver dudas y recoger feedback.

**Formación integrada.** Incluir las políticas de seguridad en el programa de formación obligatoria de la organización. Las sesiones de concienciación en seguridad deben hacer referencia constante a las políticas aplicables.

**Accesibilidad.** Las políticas deben estar publicadas en un lugar accesible para todo el personal: intranet, repositorio documental corporativo o plataforma de gestión documental. El personal debe poder consultarlas en cualquier momento.

**Recordatorios periódicos.** Utilizar comunicaciones internas (newsletter, correos, carteles) para recordar periódicamente las políticas clave. Los recordatorios son especialmente importantes para políticas que afectan al comportamiento diario, como la política de uso aceptable o la de contraseñas.

**Acuse de recibo.** Para políticas críticas, solicitar que cada empleado confirme que ha leido y comprendido el documento. Este acuse de recibo, además de reforzar la comunicación, constituye una evidencia de cumplimiento valiosa para auditorías.

{{< cta type="tofu" text="Riskitera incluye plantillas de políticas de seguridad adaptadas a ENS, ISO 27001 y NIS2, listas para personalizar." label="Ver plantillas" >}}

### Adaptación al público

No todo el personal necesita conocer todas las políticas con el mismo nivel de detalle. La comunicación debe adaptarse a la audiencia: la dirección necesita comprender los principios y las implicaciones de negocio; el personal general necesita saber qué reglas le aplican directamente y cómo cumplirlas; el personal técnico necesita además los detalles que le permitan implementar y operar los controles.

## ¿Con qué frecuencia se deben revisar las políticas?

Las políticas de seguridad no son documentos estáticos. Deben revisarse y actualizarse de forma periódica y ante eventos significativos.

### Revisión periódica

Se recomienda una revisión completa de cada política al menos una vez al año. La revisión debe evaluar si la política sigue siendo relevante y adecuada, si los requisitos normativos han cambiado, si la tecnología ha evolucionado de forma que afecte a la política, si se han producido incidentes que revelen deficiencias y si el feedback del personal indica áreas de mejora.

### Actualización ante eventos

Además de la revisión periódica, las políticas deben actualizarse ante cambios significativos: nueva normativa aplicable (por ejemplo, la entrada en vigor de NIS2), cambios organizativos relevantes (fusiones, adquisiciones, reorganizaciones), incidentes de seguridad que revelen carencias en las políticas existentes, adopción de nuevas tecnologías con implicaciones de seguridad (cloud, IA, IoT) o resultados de auditorías que identifiquen no conformidades en políticas.

### Control de versiones

Cada política debe tener un sistema de control de versiones que identifique claramente la versión vigente, la fecha de aprobación, los cambios realizados respecto a la versión anterior y el historial completo de versiones. El acceso a versiones obsoletas debe restringirse o marcarse claramente para evitar que el personal consulte documentos no vigentes.

## ¿Dónde encontrar plantillas de políticas de seguridad?

Para organizaciones que crean políticas por primera vez, las plantillas proporcionan un punto de partida valioso que acelera significativamente el proceso.

### Fuentes de plantillas

**[INCIBE](https://www.incibe.es/)** pública plantillas y guías para la elaboración de políticas de seguridad orientadas a pymes, disponibles gratuitamente en su portal web.

**CCN-CERT** proporciona modelos documentales para el cumplimiento del ENS, incluyendo la política de seguridad y documentos asociados, a través de las guías CCN-STIC de la serie 800.

**ISO 27002** (versión 2022) proporciona orientación detallada para cada control del Anexo A de ISO 27001, que puede utilizarse como base para redactar políticas específicas.

**SANS Institute** ofrece plantillas de políticas de seguridad en inglés que cubren la mayoría de los tipos necesarios y que pueden adaptarse al contexto de cada organización.

Riskitera incluye plantillas de políticas de seguridad alineadas con los requisitos del ENS e ISO 27001, personalizables según el sector y el tamaño de la organización, lo que permite a las empresas disponer de un marco documental de seguridad sólido sin partir de cero.

### Adaptación de plantillas

Las plantillas son un punto de partida, no un producto final. Toda plantilla debe adaptarse al contexto específico de la organización: su sector, su tamaño, su estructura organizativa, su entorno tecnológico, sus requisitos normativos y su cultura corporativa. Una política copiada literalmente de una plantilla sin adaptación será generica, inadecuada y dificilmente aplicable.

## ¿Cuáles son los errores comunes al crear políticas de seguridad?

**Redactar políticas que nadie lee ni conoce.** La política más perfecta técnicamente es inútil si el personal no la conoce. La comunicación y la formación son tan importantes como la redacción.

**Crear políticas inviables.** Establecer requisitos que el personal no puede cumplir razonablemente genera incumplimiento generalizado y cinismo hacia el programa de seguridad. Las políticas deben ser ambiciosas pero realistas.

**No definir responsabilidades.** Cada política debe asignar responsabilidades claras. Si nadie es responsable de verificar el cumplimiento, el cumplimiento no se verificara.

**Mezclar política y procedimiento.** La política establece el que y el por que; el procedimiento establece el como. Mezclar ambos genera documentos extensos, dificiles de mantener y que requieren actualización frecuente por cambios técnicos que no afectan a los principios de la política.

**No gestionar excepciones.** La rigidez absoluta no funciona en organizaciones reales. Un proceso formal de excepciones permite la flexibilidad necesaria sin comprometer la integridad del marco normativo.

**No actualizar las políticas.** Una política de contraseñas que exige cambio cada 30 días o que prohibe el teletrabajo cuando toda la organización trabaja en remoto erosiona la credibilidad de todo el marco documental. Las políticas deben reflejar la realidad actual de la organización.

{{< cta type="mofu" text="Gestiona el ciclo de vida completo de tus políticas de seguridad: redaccion, aprobacion, difusion y revisión periodica." >}}

## Preguntas frecuentes

### ¿Cuántas políticas de seguridad necesita mi organización

No existe un número fijo. Una pyme puede funcionar con 5 a 8 políticas fundamentales: política de seguridad de la información, uso aceptable, control de accesos, gestión de incidentes, clasificación de información, contraseñas, copias de seguridad y gestión de cambios. Una organización grande o altamente regulada puede necesitar 15 a 25 políticas que cubran áreas adicionales como seguridad en el desarrollo de software, gestión de proveedores, seguridad física o continuidad de negocio. Lo importante es que cada política responda a una necesidad real y se mantenga actualizada.

### Quien debe redactar las políticas de seguridad

El responsable de seguridad de la información (CISO) o el equipo de seguridad suele liderar la redacción, pero el proceso debe involucrar a otros departamentos. TI aporta la perspectiva técnica y de viabilidad. Legal verifica la conformidad normativa. Recursos humanos válida los aspectos laborales. Los responsables de negocio confirman que las políticas no obstaculizan las operaciones. La colaboración multidisciplinar produce políticas más equilibradas y aplicables.

### Las políticas de seguridad son obligatorias por ley

Varias normativas exigen directa o indirectamente la existencia de políticas de seguridad. El ENS requiere una política de seguridad para todos los organismos públicos y empresas que trabajan con la administración. El RGPD exige medidas organizativas de protección de datos, que se materializan en políticas. ISO 27001 exige una política de seguridad como requisito para la certificación. NIS2 obliga a las entidades esenciales e importantes a adoptar políticas de seguridad. Incluso sin un requisito legal explícito, las políticas de seguridad son una práctica mínima de diligencia debida que cualquier organización debería mantener.

### ¿Cómo consigo que los empleados cumplan las políticas

El cumplimiento requiere un enfoque múltiple: comunicación clara del contenido y el propósito de cada política, formación periódica con ejemplos prácticos, apoyo de la dirección visible y consistente, controles técnicos que faciliten el cumplimiento (por ejemplo, configurar el MFA obligatorio en lugar de confiarlo a la voluntad del usuario), consecuencias proporcionadas y conocidas ante el incumplimiento y un proceso de excepciones que evite la sensación de rigidez excesiva. La cultura de seguridad se construye gradualmente y requiere consistencia y liderazgo.

### ¿Puedo utilizar políticas genéricas descargadas de internet

Las plantillas genéricas son un punto de partida aceptable, pero nunca deben utilizarse sin adaptación. Una política que no refleja la realidad de tu organización (su tecnología, sus procesos, su sector, su normativa aplicable) será poco útil y potencialmente contraproducente. El valor de una política reside en su aplicabilidad al contexto concreto. Dedica tiempo a adaptar cada plantilla, validarla con los equipos relevantes y asegurar que las directrices son viables y pertinentes para tu organización.
