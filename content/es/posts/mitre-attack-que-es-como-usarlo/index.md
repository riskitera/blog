---
title: "MITRE ATT&CK: qué es y cómo aplicarlo en tu organización"
image: "cover.png"
description: "Guía completa sobre el framework MITRE ATT&CK: matrices Enterprise, Mobile e ICS, tácticas y técnicas, integración con el SOC, threat hunting y herramientas."
slug: "mitre-attack-que-es-como-usarlo"
date: 2026-04-14
lastmod: 2026-04-14
draft: false
tags: ["MITRE", "CTI", "Framework"]
categories: ["CTI"]
author: "David Moya"
translationKey: "mitre-attack-guide"
---

[MITRE ATT&CK](https://attack.mitre.org/) se ha consolidado como el marco de referencia global para comprender, clasificar y comunicar las tácticas y técnicas empleadas por los adversarios en ciberataques reales. Desarrollado y mantenido por MITRE Corporation, este framework de conocimiento abierto documenta el comportamiento de más de 140 grupos de amenazas y cataloga cientos de técnicas observadas en incidentes reales. Para cualquier organización que aspire a una postura de seguridad madura, conocer y aplicar MITRE ATT&CK no es opcional: es una necesidad operativa.

<!--more-->

{{< key-takeaways >}}
- MITRE ATT&CK cataloga tácticas, técnicas y procedimientos (TTPs) de adversarios reales
- Tres matrices principales: Enterprise (la más usada), Mobile e ICS
- ATT&CK Navigator permite visualizar la cobertura de detección de tu organización
- Fundamental para threat hunting, evaluación de controles y comunicación con la dirección
- Integración directa con SIEM, EDR y plataformas de threat intelligence
{{< /key-takeaways >}}

## ¿Qué es MITRE ATT&CK y para qué sirve?

MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) es una base de conocimiento estructurada que describe el comportamiento de los atacantes a lo largo de todo el ciclo de vida de una intrusión. A diferencia de otros frameworks que se centran en controles defensivos o en la gestión de riesgos, ATT&CK adopta la perspectiva del adversario: documenta qué hacen los atacantes, cómo lo hacen y con qué herramientas.

El proyecto comenzó en 2013 como una iniciativa interna de MITRE para documentar las tácticas, técnicas y procedimientos (TTPs) utilizados por grupos de amenazas avanzadas (APT) contra sistemas Windows. Desde entonces ha crecido exponencialmente y en la actualidad cubre entornos empresariales, dispositivos móviles y sistemas de control industrial.

La versión actual de ATT&CK (v15, publicada en 2024) incluye 14 tácticas, más de 200 técnicas y más de 400 subtécnicas en la matriz Enterprise. Cada técnica está documentada con descripciones detalladas, ejemplos de procedimientos utilizados por grupos reales, fuentes de datos para su detección y mitigaciones recomendadas.

El framework es gratuito, abierto y mantenido por un equipo dedicado en MITRE con aportaciones de la comunidad global de ciberseguridad. Organizaciones como [ENISA](https://www.enisa.europa.eu/), el [CCN-CERT](https://www.ccn-cert.cni.es/) y CISA lo referencian en sus guías y publicaciones, lo que refuerza su posición como estándar de facto en la industria.

## Las tres matrices ATT&CK: Enterprise, Mobile e ICS

MITRE ATT&CK se organiza en tres matrices principales, cada una adaptada a un entorno tecnológico diferente.

### ATT&CK for Enterprise

[Es la matriz más extensa y utilizada](https://attack.mitre.org/matrices/enterprise/). Cubre las plataformas Windows, macOS, Linux, entornos cloud (AWS, Azure, GCP, SaaS), redes y contenedores. Organiza el comportamiento adversario en 14 tácticas que representan los objetivos del atacante en cada fase de la intrusión:

1. **Reconnaissance** (Reconocimiento): el adversario recopila información sobre la víctima antes del ataque.
2. **Resource Development** (Desarrollo de recursos): el adversario prepara infraestructura y herramientas.
3. **Initial Access** (Acceso inicial): el adversario obtiene un punto de entrada en la red.
4. **Execution** (Ejecución): el adversario ejecuta código malicioso.
5. **Persistence** (Persistencia): el adversario mantiene su presencia tras reinicios o cambios de credenciales.
6. **Privilege Escalation** (Escalada de privilegios): el adversario obtiene permisos elevados.
7. **Defense Evasión** (Evasión de defensas): el adversario evita ser detectado.
8. **Credential Access** (Acceso a credenciales): el adversario roba nombres de usuario y contraseñas.
9. **Discovery** (Descubrimiento): el adversario explora el entorno para entender su composición.
10. **Lateral Movement** (Movimiento lateral): el adversario se desplaza entre sistemas.
11. **Collection** (Recopilación): el adversario recopila datos de interés.
12. **Command and Control** (Comando y control): el adversario se comunica con los sistemas comprometidos.
13. **Exfiltration** (Exfiltración): el adversario extrae datos fuera de la red.
14. **Impact** (Impacto): el adversario manipula, interrumpe o destruye sistemas y datos.

### ATT&CK for Mobile

[Esta matriz](https://attack.mitre.org/matrices/mobile/) cubre dispositivos Android e iOS, documentando técnicas específicas como la explotación de permisos excesivos en aplicaciones, la interceptación de comunicaciones o el acceso a datos del dispositivo. Con la creciente adopción del trabajo móvil, esta matriz gana relevancia cada año.

### ATT&CK for ICS

Orientada a [sistemas de control industrial (ICS/SCADA)](https://attack.mitre.org/matrices/ics/), esta matriz documenta técnicas utilizadas contra infraestructuras críticas como redes eléctricas, plantas de tratamiento de agua o instalaciones de fabricación. Incluye tácticas específicas como la inhibición de funciones de respuesta o la manipulación de procesos físicos. ENISA ha destacado en sus informes anuales la importancia de proteger estos entornos, y ATT&CK for ICS proporciona el vocabulario común para hacerlo.

## ¿Cómo se organizan las tácticas, técnicas y subtécnicas?

Comprender la jerarquía de ATT&CK es esencial para utilizarlo correctamente.

### Tácticas: el "por qué"

Las tácticas representan el objetivo táctico del adversario: por qué realiza una acción determinada. Por ejemplo, la táctica "Persistence" indica que el objetivo del atacante es mantener su acceso al sistema incluso después de un reinicio. Las tácticas son relativamente estables y no cambian con frecuencia.

### Técnicas: el "cómo"

Las técnicas describen cómo el adversario logra un objetivo táctico. Dentro de la táctica "Persistence", por ejemplo, se encuentran técnicas como "Boot or Logon Autostart Execution" (el adversario configura programas para ejecutarse automáticamente al iniciar el sistema) o "Create Account" (el adversario crea cuentas para mantener el acceso).

### Subtécnicas: el "cómo" con detalle

Las subtécnicas proporcionan un nivel adicional de granularidad. La técnica "Boot or Logon Autostart Execution" se descompone en subtécnicas como "Registry Run Keys / Startup Folder", "Authentication Package" o "Kernel Modules and Extensions". Este nivel de detalle permite mapeos de detección más precisos.

### Procedimientos: el "quién y cuándo"

Los procedimientos son implementaciones específicas de técnicas por parte de grupos de amenaza concretos. Por ejemplo, el grupo APT29 (asociado a actores rusos) utiliza la subtécnica "Registry Run Keys" de una manera particular, documentada en ATT&CK con referencias a informes públicos de inteligencia.

## ¿Cómo se aplica MITRE ATT&CK en el SOC?

La aplicación práctica de ATT&CK en un [centro de operaciones de seguridad](/es/posts/como-montar-soc-desde-cero/) transforma su capacidad de detección, respuesta y comunicación.

### Mapeo de detecciones

El uso más inmediato de ATT&CK en el SOC es [evaluar qué técnicas puede detectar la organización](/es/posts/2026/04/mitre-attack-soc-mapping-detecciones/) y cuáles representan puntos ciegos. El proceso consiste en tomar cada regla de detección existente en el SIEM, EDR u otras herramientas y asignarle la técnica o subtécnica de ATT&CK correspondiente. El resultado es un mapa visual de cobertura que revela qué tácticas están bien cubiertas y dónde hay brechas críticas.

Este ejercicio suele revelar que muchas organizaciones tienen buena cobertura en tácticas como Initial Access y Execution, pero presentan debilidades significativas en Defense Evasión y Lateral Movement, que son precisamente las fases donde los atacantes avanzados invierten más esfuerzo.

### Priorización de inversiones

Una vez identificados los puntos ciegos, ATT&CK permite priorizar dónde invertir recursos de detección. Si la organización pertenece al sector financiero, puede consultar qué grupos de amenaza atacan ese sector, revisar sus técnicas preferidas en ATT&CK y priorizar la cobertura de esas técnicas específicas. Este enfoque basado en inteligencia de amenazas es significativamente más eficaz que intentar cubrir todas las técnicas por igual.

### Comunicación estandarizada

ATT&CK proporciona un vocabulario común que facilita la comunicación entre equipos técnicos, responsables de seguridad y dirección. En lugar de describir un incidente con terminología vaga, los analistas pueden reportar: "El adversario utilizó T1566.001 (Spearphishing Attachment) para obtener acceso inicial, seguido de T1059.001 (PowerShell) para ejecución y T1053.005 (Scheduled Task) para persistencia". Esta precisión mejora la calidad de los informes y la trazabilidad de las investigaciones.

### Evaluación de herramientas

ATT&CK se utiliza cada vez más para evaluar la eficacia de productos de seguridad. Las evaluaciones ATT&CK de MITRE Engenuity someten a soluciones EDR y de seguridad endpoint a simulaciones de ataques basadas en las TTPs de grupos reales, publicando los resultados de forma transparente. Estas evaluaciones permiten a las organizaciones comparar productos con datos objetivos.

## ¿Cómo usar ATT&CK para threat hunting?

El framework ATT&CK es una herramienta esencial para estructurar programas de threat hunting, transformando la búsqueda de amenazas de una actividad ad hoc a un proceso sistemático y medible.

### Generación de hipótesis

ATT&CK permite generar hipótesis de caza estructuradas. Un hunter puede formular hipótesis como: "Es posible que un adversario esté utilizando T1055 (Process Injection) para ejecutar código malicioso dentro de procesos legítimos y evadir nuestras defensas". Esta hipótesis define exactamente qué buscar, dónde buscar y qué fuentes de datos son necesarias.

### Cobertura sistemática

Utilizando ATT&CK como guía, el equipo de hunting puede planificar campañas que cubran sistemáticamente las técnicas más relevantes para la organización. En lugar de depender de la intuición individual, el framework proporciona una estructura que garantiza que no se omiten áreas críticas.

### Vinculación con IOCs

Los hallazgos del threat hunting frecuentemente generan nuevos [IOCs](/es/posts/iocs-en-ciberseguridad-que-son/) que enriquecen la inteligencia de amenazas de la organización. Estos IOCs, mapeados contra las técnicas de ATT&CK que evidencian, alimentan el ciclo continuo de mejora de la detección.

{{< cta type="tofu" text="Riskitera mapea tus detecciones a MITRE ATT&CK automáticamente, visualizando gaps de cobertura en tiempo real." label="Ver cobertura" >}}

## Herramientas para ATT&CK: Navigator, TRAM, DeTT&CT y CAR

El ecosistema de herramientas alrededor de ATT&CK es amplio y en constante crecimiento.

### ATT&CK Navigator

Es la [herramienta oficial de MITRE](https://mitre-attack.github.io/attack-navigator/) para visualizar la cobertura sobre la matriz ATT&CK. Permite crear "capas" (layers) que representan las detecciones existentes, las técnicas utilizadas por un grupo de amenaza específico o los resultados de un ejercicio de red team. La superposición de capas revela visualmente las brechas de cobertura. Es una herramienta web gratuita, disponible también como aplicación local.

### MITRE ATT&CK Workbench

Permite a las organizaciones crear y mantener versiones personalizadas de ATT&CK, añadiendo técnicas propias, notas internas o adaptaciones específicas del sector. Es especialmente útil para organizaciones que quieren extender el framework con conocimiento propio.

### Atomic Red Team

Desarrollado por Red Canary, es una biblioteca de pruebas atomicas que implementan técnicas de ATT&CK de forma segura y controlada. Cada prueba está mapeada a una técnica específica y puede ejecutarse para validar si las defensas existentes la detectan.

### Sigma y detección basada en ATT&CK

Las [reglas Sigma](https://github.com/SigmaHQ/sigma), un formato abierto para escribir detecciones genéricas de SIEM, incluyen etiquetas ATT&CK que vinculan cada regla con las técnicas que detecta. Esto permite construir una cobertura de detección mapeada directamente contra el framework.

### Caldera

Desarrollado por MITRE, Caldera es una plataforma de emulación de adversarios automatizada que ejecuta cadenas de ataque basadas en perfiles de TTPs de ATT&CK. Permite simular el comportamiento de grupos de amenaza específicos para evaluar la capacidad de detección y respuesta.

## ¿Cómo integrar ATT&CK con el SIEM?

La integración entre ATT&CK y el SIEM es una de las aplicaciones más potentes del framework.

### Etiquetado de reglas

Cada regla de correlación en el SIEM debe etiquetarse con la técnica o subtécnica de ATT&CK que detecta. Esto permite generar dashboards de cobertura en tiempo real y medir automáticamente qué porcentaje de la matriz está cubierto por las detecciones activas.

### Correlación contextual

Cuando una alerta del SIEM se mapea contra ATT&CK, el analista obtiene inmediatamente contexto adicional: qué grupos utilizan esa técnica, qué otras técnicas suelen acompañarla, qué fuentes de datos adicionales podrían confirmarlo y qué mitigaciones son aplicables. Este contexto acelera significativamente el triaje y la investigación.

### Medición continua

Con las reglas etiquetadas, es posible generar métricas continuas de cobertura de detección: porcentaje de técnicas cubiertas por tactica, tendencia temporal de cobertura, técnicas con mayor volumen de alertas y técnicas detectadas pero sin alertas reales (posibles áreas de sobredetección). Riskitera mapea automáticamente los controles de seguridad contra las técnicas de MITRE ATT&CK, proporcionando visibilidad instantánea sobre la cobertura de detección y los puntos ciegos de la organización.

## Trampas habituales al adoptar ATT&CK en el SOC

**Intentar cubrir toda la matriz a la vez.** ATT&CK es extenso y pretender detectar todas las técnicas simultáneamente es inviable para la mayoría de organizaciones. Es mejor priorizar las técnicas más relevantes según el perfil de amenaza y avanzar gradualmente.

**Confundir cobertura teórica con detección real.** Tener una regla de SIEM mapeada a una técnica no garantiza que funcione. Las detecciones deben validarse periódicamente con pruebas como Atomic Red Team o ejercicios de red team.

**Ignorar las fuentes de datos.** Cada técnica en ATT&CK documenta las fuentes de datos necesarias para su detección. Si la organización no recoge esas fuentes de datos, la detección es imposible independientemente de las reglas configuradas.

**Usar ATT&CK solo para compliance.** El verdadero valor de ATT&CK está en su aplicación operativa diaria, no en generar informes de cobertura para auditorías. La cobertura debe traducirse en capacidad real de detección y respuesta.

## Recursos oficiales y formación

MITRE ofrece numerosos recursos gratuitos para aprender y aplicar ATT&CK:

La página oficial (attack.mitre.org) proporciona acceso completo a la base de conocimiento, con búsqueda y navegación interactiva. El blog de MITRE ATT&CK publica regularmente artículos sobre actualizaciones, casos de uso y mejores prácticas. Los cursos ATT&CK Training de MITRE Engenuity ofrecen formación estructurada. Los CTI Blueprints proporcionan plantillas para crear informes de inteligencia basados en ATT&CK.

En el ámbito europeo, el CCN-CERT ha publicado guías CCN-STIC que referencian ATT&CK para la detección de amenazas en organismos públicos españoles, y ENISA incluye referencias al framework en su informe anual de amenazas (ENISA Threat Landscape).

{{< cta type="mofu" text="Integra MITRE ATT&CK en tu SOC con una plataforma que conecta tácticas, detecciones y controles de compliance." >}}

## Preguntas frecuentes

### MITRE ATT&CK es un estándar de obligado cumplimiento

No. MITRE ATT&CK es una base de conocimiento abierta y gratuita, no un estándar regulatorio. Sin embargo, su adopción esta ampliamente recomendada por organismos como ENISA, el CCN-CERT, CISA y NIST. Muchas organizaciones lo integran como parte de sus programas de seguridad, y las evaluaciones de productos basadas en ATT&CK se han convertido en un criterio de selección habitual.

### ¿Qué diferencia hay entre MITRE ATT&CK y el Cyber Kill Chain?

El Cyber Kill Chain de Lockheed Martin describe las fases de un ataque de forma lineal y a alto nivel (7 fases). MITRE ATT&CK es significativamente más granular, con 14 tácticas y cientos de técnicas y subtécnicas. Además, ATT&CK no asume un flujo lineal: los atacantes pueden saltar entre tácticas y repetir fases. Ambos marcos son complementarios, pero ATT&CK ofrece mucha mayor utilidad operativa.

### ¿Necesito un equipo grande para implementar ATT&CK?

No necesariamente. Una organización pequeña puede comenzar seleccionando las 20-30 técnicas más relevantes para su perfil de amenaza y evaluar su cobertura de detección sobre ellas. A medida que el equipo crece y madura, se amplía la cobertura. La clave es empezar con un alcance realista y avanzar de forma incremental.

### ¿Con qué frecuencia se actualiza MITRE ATT&CK?

MITRE publica actualizaciones mayores de ATT&CK aproximadamente dos veces al año, incorporando nuevas técnicas, subtécnicas, grupos de amenaza y software documentado por la comunidad. Entre actualizaciones mayores, se realizan correcciones y adiciones menores. Es recomendable revisar los changelogs de cada versión para identificar técnicas nuevas que puedan ser relevantes.

### ¿Cómo puedo empezar a implementar ATT&CK mañana?

El primer paso práctico es descargar ATT&CK Navigator y crear una capa que represente las detecciones actuales de la organización. Esto proporciona una radiografía inmediata de la cobertura y los puntos ciegos. A partir de ahí, se priorizan las técnicas a cubrir según el perfil de amenaza y se escriben o adquieren las detecciones correspondientes. Es un proceso iterativo que mejora con cada ciclo.
