---
title: "MITRE ATT&CK: que es y como aplicarlo en tu organizacion"
image: "cover.png"
description: "Guia completa sobre el framework MITRE ATT&CK: matrices Enterprise, Mobile e ICS, tacticas y tecnicas, integracion con el SOC, threat hunting y herramientas como ATT&CK Navigator."
slug: "mitre-attack-que-es-como-usarlo"
date: 2026-04-14
lastmod: 2026-04-14
draft: false
tags: ["MITRE", "CTI", "Framework"]
categories: ["CTI"]
author: "David Moya"
translationKey: "mitre-attack-guide"
---

[MITRE ATT&CK](https://attack.mitre.org/) se ha consolidado como el marco de referencia global para comprender, clasificar y comunicar las tacticas y tecnicas empleadas por los adversarios en ciberataques reales. Desarrollado y mantenido por MITRE Corporation, este framework de conocimiento abierto documenta el comportamiento de mas de 140 grupos de amenazas y cataloga cientos de tecnicas observadas en incidentes reales. Para cualquier organizacion que aspire a una postura de seguridad madura, conocer y aplicar MITRE ATT&CK no es opcional: es una necesidad operativa.

<!--more-->

{{< key-takeaways >}}
- MITRE ATT&CK cataloga tacticas, tecnicas y procedimientos (TTPs) de adversarios reales
- Tres matrices principales: Enterprise (la mas usada), Mobile e ICS
- ATT&CK Navigator permite visualizar la cobertura de deteccion de tu organizacion
- Fundamental para threat hunting, evaluacion de controles y comunicacion con la direccion
- Integracion directa con SIEM, EDR y plataformas de threat intelligence
{{< /key-takeaways >}}

## Que es MITRE ATT&CK y para que sirve?

MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) es una base de conocimiento estructurada que describe el comportamiento de los atacantes a lo largo de todo el ciclo de vida de una intrusion. A diferencia de otros frameworks que se centran en controles defensivos o en la gestion de riesgos, ATT&CK adopta la perspectiva del adversario: documenta que hacen los atacantes, como lo hacen y con que herramientas.

El proyecto comenzo en 2013 como una iniciativa interna de MITRE para documentar las tacticas, tecnicas y procedimientos (TTPs) utilizados por grupos de amenazas avanzadas (APT) contra sistemas Windows. Desde entonces ha crecido exponencialmente y en la actualidad cubre entornos empresariales, dispositivos moviles y sistemas de control industrial.

La version actual de ATT&CK (v15, publicada en 2024) incluye 14 tacticas, mas de 200 tecnicas y mas de 400 subtecnicas en la matriz Enterprise. Cada tecnica esta documentada con descripciones detalladas, ejemplos de procedimientos utilizados por grupos reales, fuentes de datos para su deteccion y mitigaciones recomendadas.

El framework es gratuito, abierto y mantenido por un equipo dedicado en MITRE con aportaciones de la comunidad global de ciberseguridad. Organizaciones como [ENISA](https://www.enisa.europa.eu/), el [CCN-CERT](https://www.ccn-cert.cni.es/) y CISA lo referencian en sus guias y publicaciones, lo que refuerza su posicion como estandar de facto en la industria.

## Cuales son las matrices de MITRE ATT&CK?

MITRE ATT&CK se organiza en tres matrices principales, cada una adaptada a un entorno tecnologico diferente.

### ATT&CK for Enterprise

[Es la matriz mas extensa y utilizada](https://attack.mitre.org/matrices/enterprise/). Cubre las plataformas Windows, macOS, Linux, entornos cloud (AWS, Azure, GCP, SaaS), redes y contenedores. Organiza el comportamiento adversario en 14 tacticas que representan los objetivos del atacante en cada fase de la intrusion:

1. **Reconnaissance** (Reconocimiento): el adversario recopila informacion sobre la victima antes del ataque.
2. **Resource Development** (Desarrollo de recursos): el adversario prepara infraestructura y herramientas.
3. **Initial Access** (Acceso inicial): el adversario obtiene un punto de entrada en la red.
4. **Execution** (Ejecucion): el adversario ejecuta codigo malicioso.
5. **Persistence** (Persistencia): el adversario mantiene su presencia tras reinicios o cambios de credenciales.
6. **Privilege Escalation** (Escalada de privilegios): el adversario obtiene permisos elevados.
7. **Defense Evasion** (Evasion de defensas): el adversario evita ser detectado.
8. **Credential Access** (Acceso a credenciales): el adversario roba nombres de usuario y contrasenas.
9. **Discovery** (Descubrimiento): el adversario explora el entorno para entender su composicion.
10. **Lateral Movement** (Movimiento lateral): el adversario se desplaza entre sistemas.
11. **Collection** (Recopilacion): el adversario recopila datos de interes.
12. **Command and Control** (Comando y control): el adversario se comunica con los sistemas comprometidos.
13. **Exfiltration** (Exfiltracion): el adversario extrae datos fuera de la red.
14. **Impact** (Impacto): el adversario manipula, interrumpe o destruye sistemas y datos.

### ATT&CK for Mobile

[Esta matriz](https://attack.mitre.org/matrices/mobile/) cubre dispositivos Android e iOS, documentando tecnicas especificas como la explotacion de permisos excesivos en aplicaciones, la interceptacion de comunicaciones o el acceso a datos del dispositivo. Con la creciente adopcion del trabajo movil, esta matriz gana relevancia cada ano.

### ATT&CK for ICS

Orientada a [sistemas de control industrial (ICS/SCADA)](https://attack.mitre.org/matrices/ics/), esta matriz documenta tecnicas utilizadas contra infraestructuras criticas como redes electricas, plantas de tratamiento de agua o instalaciones de fabricacion. Incluye tacticas especificas como la inhibicion de funciones de respuesta o la manipulacion de procesos fisicos. ENISA ha destacado en sus informes anuales la importancia de proteger estos entornos, y ATT&CK for ICS proporciona el vocabulario comun para hacerlo.

## Como se organizan las tacticas, tecnicas y subtecnicas?

Comprender la jerarquia de ATT&CK es esencial para utilizarlo correctamente.

### Tacticas: el "por que"

Las tacticas representan el objetivo tactico del adversario: por que realiza una accion determinada. Por ejemplo, la tactica "Persistence" indica que el objetivo del atacante es mantener su acceso al sistema incluso despues de un reinicio. Las tacticas son relativamente estables y no cambian con frecuencia.

### Tecnicas: el "como"

Las tecnicas describen como el adversario logra un objetivo tactico. Dentro de la tactica "Persistence", por ejemplo, se encuentran tecnicas como "Boot or Logon Autostart Execution" (el adversario configura programas para ejecutarse automaticamente al iniciar el sistema) o "Create Account" (el adversario crea cuentas para mantener el acceso).

### Subtecnicas: el "como" con detalle

Las subtecnicas proporcionan un nivel adicional de granularidad. La tecnica "Boot or Logon Autostart Execution" se descompone en subtecnicas como "Registry Run Keys / Startup Folder", "Authentication Package" o "Kernel Modules and Extensions". Este nivel de detalle permite mapeos de deteccion mas precisos.

### Procedimientos: el "quien y cuando"

Los procedimientos son implementaciones especificas de tecnicas por parte de grupos de amenaza concretos. Por ejemplo, el grupo APT29 (asociado a actores rusos) utiliza la subtecnica "Registry Run Keys" de una manera particular, documentada en ATT&CK con referencias a informes publicos de inteligencia.

## Como se aplica MITRE ATT&CK en el SOC?

La aplicacion practica de ATT&CK en un [centro de operaciones de seguridad](/es/posts/como-montar-soc-desde-cero/) transforma su capacidad de deteccion, respuesta y comunicacion.

### Mapeo de detecciones

El uso mas inmediato de ATT&CK en el SOC es evaluar que tecnicas puede detectar la organizacion y cuales representan puntos ciegos. El proceso consiste en tomar cada regla de deteccion existente en el SIEM, EDR u otras herramientas y asignarle la tecnica o subtecnica de ATT&CK correspondiente. El resultado es un mapa visual de cobertura que revela que tacticas estan bien cubiertas y donde hay brechas criticas.

Este ejercicio suele revelar que muchas organizaciones tienen buena cobertura en tacticas como Initial Access y Execution, pero presentan debilidades significativas en Defense Evasion y Lateral Movement, que son precisamente las fases donde los atacantes avanzados invierten mas esfuerzo.

### Priorizacion de inversiones

Una vez identificados los puntos ciegos, ATT&CK permite priorizar donde invertir recursos de deteccion. Si la organizacion pertenece al sector financiero, puede consultar que grupos de amenaza atacan ese sector, revisar sus tecnicas preferidas en ATT&CK y priorizar la cobertura de esas tecnicas especificas. Este enfoque basado en inteligencia de amenazas es significativamente mas eficaz que intentar cubrir todas las tecnicas por igual.

### Comunicacion estandarizada

ATT&CK proporciona un vocabulario comun que facilita la comunicacion entre equipos tecnicos, responsables de seguridad y direccion. En lugar de describir un incidente con terminologia vaga, los analistas pueden reportar: "El adversario utilizo T1566.001 (Spearphishing Attachment) para obtener acceso inicial, seguido de T1059.001 (PowerShell) para ejecucion y T1053.005 (Scheduled Task) para persistencia". Esta precision mejora la calidad de los informes y la trazabilidad de las investigaciones.

### Evaluacion de herramientas

ATT&CK se utiliza cada vez mas para evaluar la eficacia de productos de seguridad. Las evaluaciones ATT&CK de MITRE Engenuity someten a soluciones EDR y de seguridad endpoint a simulaciones de ataques basadas en las TTPs de grupos reales, publicando los resultados de forma transparente. Estas evaluaciones permiten a las organizaciones comparar productos con datos objetivos.

## Como usar ATT&CK para threat hunting?

El framework ATT&CK es una herramienta esencial para estructurar programas de threat hunting, transformando la busqueda de amenazas de una actividad ad hoc a un proceso sistematico y medible.

### Generacion de hipotesis

ATT&CK permite generar hipotesis de caza estructuradas. Un hunter puede formular hipotesis como: "Es posible que un adversario este utilizando T1055 (Process Injection) para ejecutar codigo malicioso dentro de procesos legitimos y evadir nuestras defensas". Esta hipotesis define exactamente que buscar, donde buscar y que fuentes de datos son necesarias.

### Cobertura sistematica

Utilizando ATT&CK como guia, el equipo de hunting puede planificar campanas que cubran sistematicamente las tecnicas mas relevantes para la organizacion. En lugar de depender de la intuicion individual, el framework proporciona una estructura que garantiza que no se omiten areas criticas.

### Vinculacion con IOCs

Los hallazgos del threat hunting frecuentemente generan nuevos [IOCs](/es/posts/iocs-en-ciberseguridad-que-son/) que enriquecen la inteligencia de amenazas de la organizacion. Estos IOCs, mapeados contra las tecnicas de ATT&CK que evidencian, alimentan el ciclo continuo de mejora de la deteccion.

{{< cta type="tofu" text="Riskitera mapea tus detecciones a MITRE ATT&CK automaticamente, visualizando gaps de cobertura en tiempo real." label="Ver cobertura" >}}

## Que herramientas existen para trabajar con ATT&CK?

El ecosistema de herramientas alrededor de ATT&CK es amplio y en constante crecimiento.

### ATT&CK Navigator

Es la [herramienta oficial de MITRE](https://mitre-attack.github.io/attack-navigator/) para visualizar la cobertura sobre la matriz ATT&CK. Permite crear "capas" (layers) que representan las detecciones existentes, las tecnicas utilizadas por un grupo de amenaza especifico o los resultados de un ejercicio de red team. La superposicion de capas revela visualmente las brechas de cobertura. Es una herramienta web gratuita, disponible tambien como aplicacion local.

### MITRE ATT&CK Workbench

Permite a las organizaciones crear y mantener versiones personalizadas de ATT&CK, anadiendo tecnicas propias, notas internas o adaptaciones especificas del sector. Es especialmente util para organizaciones que quieren extender el framework con conocimiento propio.

### Atomic Red Team

Desarrollado por Red Canary, es una biblioteca de pruebas atomicas que implementan tecnicas de ATT&CK de forma segura y controlada. Cada prueba esta mapeada a una tecnica especifica y puede ejecutarse para validar si las defensas existentes la detectan.

### Sigma y deteccion basada en ATT&CK

Las [reglas Sigma](https://github.com/SigmaHQ/sigma), un formato abierto para escribir detecciones genericas de SIEM, incluyen etiquetas ATT&CK que vinculan cada regla con las tecnicas que detecta. Esto permite construir una cobertura de deteccion mapeada directamente contra el framework.

### Caldera

Desarrollado por MITRE, Caldera es una plataforma de emulacion de adversarios automatizada que ejecuta cadenas de ataque basadas en perfiles de TTPs de ATT&CK. Permite simular el comportamiento de grupos de amenaza especificos para evaluar la capacidad de deteccion y respuesta.

## Como integrar ATT&CK con el SIEM?

La integracion entre ATT&CK y el SIEM es una de las aplicaciones mas potentes del framework.

### Etiquetado de reglas

Cada regla de correlacion en el SIEM debe etiquetarse con la tecnica o subtecnica de ATT&CK que detecta. Esto permite generar dashboards de cobertura en tiempo real y medir automaticamente que porcentaje de la matriz esta cubierto por las detecciones activas.

### Correlacion contextual

Cuando una alerta del SIEM se mapea contra ATT&CK, el analista obtiene inmediatamente contexto adicional: que grupos utilizan esa tecnica, que otras tecnicas suelen acompanarla, que fuentes de datos adicionales podrian confirmarlo y que mitigaciones son aplicables. Este contexto acelera significativamente el triaje y la investigacion.

### Medicion continua

Con las reglas etiquetadas, es posible generar metricas continuas de cobertura de deteccion: porcentaje de tecnicas cubiertas por tactica, tendencia temporal de cobertura, tecnicas con mayor volumen de alertas y tecnicas detectadas pero sin alertas reales (posibles areas de sobredeteccion). Riskitera mapea automaticamente los controles de seguridad contra las tecnicas de MITRE ATT&CK, proporcionando visibilidad instantanea sobre la cobertura de deteccion y los puntos ciegos de la organizacion.

## Cuales son los errores comunes al implementar ATT&CK?

**Intentar cubrir toda la matriz a la vez.** ATT&CK es extenso y pretender detectar todas las tecnicas simultaneamente es inviable para la mayoria de organizaciones. Es mejor priorizar las tecnicas mas relevantes segun el perfil de amenaza y avanzar gradualmente.

**Confundir cobertura teorica con deteccion real.** Tener una regla de SIEM mapeada a una tecnica no garantiza que funcione. Las detecciones deben validarse periodicamente con pruebas como Atomic Red Team o ejercicios de red team.

**Ignorar las fuentes de datos.** Cada tecnica en ATT&CK documenta las fuentes de datos necesarias para su deteccion. Si la organizacion no recoge esas fuentes de datos, la deteccion es imposible independientemente de las reglas configuradas.

**Usar ATT&CK solo para compliance.** El verdadero valor de ATT&CK esta en su aplicacion operativa diaria, no en generar informes de cobertura para auditorias. La cobertura debe traducirse en capacidad real de deteccion y respuesta.

## Recursos oficiales y formacion

MITRE ofrece numerosos recursos gratuitos para aprender y aplicar ATT&CK:

La pagina oficial (attack.mitre.org) proporciona acceso completo a la base de conocimiento, con busqueda y navegacion interactiva. El blog de MITRE ATT&CK publica regularmente articulos sobre actualizaciones, casos de uso y mejores practicas. Los cursos ATT&CK Training de MITRE Engenuity ofrecen formacion estructurada. Los CTI Blueprints proporcionan plantillas para crear informes de inteligencia basados en ATT&CK.

En el ambito europeo, el CCN-CERT ha publicado guias CCN-STIC que referencian ATT&CK para la deteccion de amenazas en organismos publicos espanoles, y ENISA incluye referencias al framework en su informe anual de amenazas (ENISA Threat Landscape).

{{< cta type="mofu" text="Integra MITRE ATT&CK en tu SOC con una plataforma que conecta tacticas, detecciones y controles de compliance." >}}

## Preguntas frecuentes

### MITRE ATT&CK es un estandar de obligado cumplimiento

No. MITRE ATT&CK es una base de conocimiento abierta y gratuita, no un estandar regulatorio. Sin embargo, su adopcion esta ampliamente recomendada por organismos como ENISA, el CCN-CERT, CISA y NIST. Muchas organizaciones lo integran como parte de sus programas de seguridad, y las evaluaciones de productos basadas en ATT&CK se han convertido en un criterio de seleccion habitual.

### Que diferencia hay entre MITRE ATT&CK y el Cyber Kill Chain

El Cyber Kill Chain de Lockheed Martin describe las fases de un ataque de forma lineal y a alto nivel (7 fases). MITRE ATT&CK es significativamente mas granular, con 14 tacticas y cientos de tecnicas y subtecnicas. Ademas, ATT&CK no asume un flujo lineal: los atacantes pueden saltar entre tacticas y repetir fases. Ambos marcos son complementarios, pero ATT&CK ofrece mucha mayor utilidad operativa.

### Necesito un equipo grande para implementar ATT&CK

No necesariamente. Una organizacion pequena puede comenzar seleccionando las 20-30 tecnicas mas relevantes para su perfil de amenaza y evaluar su cobertura de deteccion sobre ellas. A medida que el equipo crece y madura, se amplia la cobertura. La clave es empezar con un alcance realista y avanzar de forma incremental.

### Con que frecuencia se actualiza MITRE ATT&CK

MITRE publica actualizaciones mayores de ATT&CK aproximadamente dos veces al ano, incorporando nuevas tecnicas, subtecnicas, grupos de amenaza y software documentado por la comunidad. Entre actualizaciones mayores, se realizan correcciones y adiciones menores. Es recomendable revisar los changelogs de cada version para identificar tecnicas nuevas que puedan ser relevantes.

### Como puedo empezar a implementar ATT&CK manana

El primer paso practico es descargar ATT&CK Navigator y crear una capa que represente las detecciones actuales de la organizacion. Esto proporciona una radiografia inmediata de la cobertura y los puntos ciegos. A partir de ahi, se priorizan las tecnicas a cubrir segun el perfil de amenaza y se escriben o adquieren las detecciones correspondientes. Es un proceso iterativo que mejora con cada ciclo.
