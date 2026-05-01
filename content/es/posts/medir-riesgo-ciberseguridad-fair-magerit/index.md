---
title: "Como medir el riesgo ciber: metodologias FAIR vs MAGERIT en la practica"
description: "Comparativa practica de las metodologias FAIR y MAGERIT para medir el riesgo en ciberseguridad: cuando usar cada una, ventajas, limitaciones y como combinarlas."
slug: "medir-riesgo-ciberseguridad-fair-magerit"
date: 2026-06-11
publishDate: 2026-06-11
lastmod: 2026-06-11
draft: false
tags: ["GRC", "Riesgos", "Metodologia"]
categories: ["GRC"]
author: "David Moya"
keyword: "medir riesgo ciberseguridad"
funnel: "mofu"
---

Comparativa practica de las metodologias FAIR y MAGERIT para medir el riesgo en ciberseguridad: cuando usar cada una, ventajas, limitaciones y como combinarlas.

<!--more-->

{{< key-takeaways >}}
- MAGERIT es la metodologia de referencia para el sector publico espanol y obligatoria para el cumplimiento del ENS, con un enfoque cualitativo basado en activos, amenazas y salvaguardas
- FAIR cuantifica el riesgo en terminos monetarios, permitiendo calcular la perdida esperada anual (ALE) y facilitar la comunicacion con la direccion financiera
- Ambas metodologias no son excluyentes: un enfoque hibrido que use MAGERIT para el inventario y las amenazas, y FAIR para la cuantificacion financiera, da los mejores resultados
- La eleccion entre ambas depende del contexto regulatorio (ENS obliga MAGERIT), la madurez del equipo y el interlocutor (tecnico vs financiero)
- Las herramientas automatizadas reducen el esfuerzo de aplicacion de cualquiera de las dos metodologias en un 60-70%, eliminando el principal obstaculo: la carga manual
{{< /key-takeaways >}}

## Como se mide el riesgo en ciberseguridad?

Medir el riesgo en ciberseguridad es una de las tareas mas complejas y, paradojicamente, mas importantes de un CISO. Sin una medicion rigurosa, las decisiones de inversion en seguridad se basan en intuiciones, miedos o titulares de prensa. Con una medicion rigurosa, el CISO puede responder preguntas concretas: cuanto dinero estamos dispuestos a perder, donde tenemos las mayores exposiciones, y que inversion reduce mas riesgo por cada euro gastado.

El problema es que "medir riesgo" no significa lo mismo para todos. Para un auditor del [CCN-CERT](https://www.ccn-cert.cni.es/), medir riesgo es evaluar activos, identificar amenazas, calcular el impacto y la probabilidad, y determinar un nivel de riesgo cualitativo (Bajo, Medio, Alto, Muy Alto, Critico). Para un CFO, medir riesgo es responder: cuanto dinero podemos perder si nos atacan, y cual es la probabilidad de que eso ocurra este ano.

Ambas perspectivas son validas. Y para cada una existe una metodologia establecida:

- **[MAGERIT](https://www.ccn-cert.cni.es/herramientas-de-ciberseguridad/ear-pilar.html)** (Metodologia de Analisis y Gestion de Riesgos de los Sistemas de Informacion): desarrollada por el Consejo Superior de Administracion Electronica de Espana, es la referencia para el sector publico y organizaciones sujetas al ENS.
- **[FAIR](https://www.fairinstitute.org/)** (Factor Analysis of Information Risk): un modelo cuantitativo desarrollado por Jack Jones que descompone el riesgo en factores medibles y lo expresa en terminos monetarios.

En este articulo vamos a comparar ambas metodologias de forma practica, analizando el mismo escenario de riesgo con cada una para que puedas ver las diferencias reales, no solo las teoricas.

## Que es la metodologia MAGERIT?

MAGERIT es la metodologia oficial de analisis de riesgos de la administracion publica espanola. Su primera version se publico en 1997, y la version 3 (vigente) en 2012. Esta disenada para cumplir con los requisitos del Esquema Nacional de Seguridad (ENS) y se apoya en la herramienta [PILAR](https://www.ccn-cert.cni.es/herramientas-de-ciberseguridad/ear-pilar.html), desarrollada por el CCN-CERT.

### Estructura de MAGERIT

MAGERIT se organiza en tres libros:

1. **Libro I: Metodo.** Define el proceso completo de analisis de riesgos: identificacion de activos, valoracion, identificacion de amenazas, estimacion de impacto y riesgo.
2. **Libro II: Catalogo de elementos.** Proporciona taxonomias de activos, dimensiones de valoracion, amenazas y salvaguardas.
3. **Libro III: Guia de tecnicas.** Describe tecnicas complementarias como analisis de impacto en el negocio (BIA), arboles de ataque y analisis coste-beneficio.

### Proceso de analisis con MAGERIT

El proceso MAGERIT sigue estos pasos:

**Paso 1: Identificacion y valoracion de activos.** Se catalogan todos los activos de informacion (datos, servicios, aplicaciones, equipos, instalaciones, personal) y se valoran segun cinco dimensiones de seguridad: Disponibilidad (D), Integridad (I), Confidencialidad (C), Autenticidad (A) y Trazabilidad (T). La valoracion es cualitativa: de 0 (irrelevante) a 10 (dano muy grave).

**Paso 2: Identificacion de amenazas.** Se identifican las amenazas que pueden afectar a cada activo, utilizando el catalogo de amenazas de MAGERIT. Las amenazas se clasifican en: naturales, industriales, errores y ataques deliberados.

**Paso 3: Estimacion del impacto.** Se calcula el impacto potencial como la degradacion que la amenaza puede causar sobre el activo en cada dimension. El impacto se expresa como un porcentaje de degradacion sobre el valor del activo.

**Paso 4: Estimacion de la frecuencia.** Se estima la frecuencia con la que se espera que la amenaza se materialice. MAGERIT utiliza una escala cualitativa: despreciable, poco frecuente, normal, frecuente, muy frecuente.

**Paso 5: Calculo del riesgo.** El riesgo se calcula como la combinacion del impacto y la frecuencia. El resultado es un nivel de riesgo cualitativo que se posiciona en un mapa de calor.

**Paso 6: Evaluacion de salvaguardas.** Se identifican las salvaguardas (controles) existentes y su nivel de madurez. El riesgo residual se calcula considerando la eficacia de las salvaguardas implementadas.

### Ventajas de MAGERIT

- Alineada al 100% con el ENS y las guias CCN-STIC
- Catalogo exhaustivo de amenazas y salvaguardas adaptado al contexto espanol
- Herramienta oficial (PILAR) disponible para la administracion publica
- Proceso sistematico y repetible que facilita auditorias
- Bien documentada con ejemplos y guias en espanol

### Limitaciones de MAGERIT

- El resultado es cualitativo (Alto, Medio, Bajo), lo que dificulta la priorizacion cuando hay muchos riesgos en el mismo nivel
- No produce cifras monetarias, lo que complica la justificacion de inversiones ante la direccion
- El proceso manual es intensivo en tiempo: una organizacion mediana puede necesitar 3-6 meses para un analisis completo
- Las escalas cualitativas introducen subjetividad: lo que un analista valora como "Alto" otro lo puede valorar como "Medio"
- El catalogo de amenazas, aunque exhaustivo, no se actualiza con la frecuencia del panorama de amenazas real

## Que es la metodologia FAIR?

FAIR (Factor Analysis of Information Risk) es un modelo cuantitativo de analisis de riesgo creado por Jack Jones en 2005. A diferencia de MAGERIT, FAIR no prescribe un proceso de gestion de riesgos completo, sino que se centra en la cuantificacion: descomponer el riesgo en factores medibles y expresar el resultado en terminos monetarios (dolares o euros de perdida esperada).

FAIR se convirtio en un estandar abierto de The Open Group en 2014, y el [FAIR Institute](https://www.fairinstitute.org/) promueve su adopcion a nivel global. En 2025, FAIR-MAM (FAIR Materiality Assessment Model) amplio el framework para incluir analisis de materialidad regulatoria.

### Taxonomia de riesgo FAIR

FAIR descompone el riesgo en dos factores principales:

**LEF (Loss Event Frequency):** Con que frecuencia esperamos que un evento de perdida ocurra en un periodo determinado. Se descompone en:
- TEF (Threat Event Frequency): frecuencia con la que un agente de amenaza actua contra un activo
- Vulnerability: probabilidad de que la accion del agente de amenaza resulte en un evento de perdida

**LM (Loss Magnitude):** Cuanto perdemos cuando el evento de perdida ocurre. Se descompone en:
- Primary Loss: perdida directa (respuesta al incidente, reposicion de activos, productividad)
- Secondary Loss: perdida indirecta (multas, litigios, dano reputacional, perdida de clientes)

El resultado final es una distribucion de probabilidad de la perdida anual esperada (ALE, Annualized Loss Expectancy), tipicamente expresada como un rango (por ejemplo: "hay un 90% de probabilidad de que la perdida anual por ransomware este entre 50.000 EUR y 1.200.000 EUR, con una mediana de 320.000 EUR").

### Proceso de analisis con FAIR

**Paso 1: Definir el escenario de riesgo.** Se identifica la combinacion especifica de activo, amenaza y efecto. Ejemplo: "ransomware que cifra el ERP y paraliza la operacion durante 5 dias".

**Paso 2: Estimar la frecuencia del evento de amenaza (TEF).** Utilizando datos historicos, inteligencia de amenazas o juicio experto, se estima cuantas veces al ano un actor de amenaza intenta este tipo de ataque contra la organizacion.

**Paso 3: Estimar la vulnerabilidad.** Se evalua la probabilidad de que el intento tenga exito, considerando los controles existentes (segmentacion de red, backups, EDR, formacion).

**Paso 4: Calcular la frecuencia del evento de perdida (LEF).** LEF = TEF x Vulnerabilidad.

**Paso 5: Estimar la magnitud de la perdida.** Se desglosan los costes: respuesta al incidente, perdida de negocio, notificaciones regulatorias, multas, litigios, dano reputacional. Cada componente se estima como un rango (minimo, mas probable, maximo).

**Paso 6: Calcular el riesgo (ALE).** Utilizando simulacion de Monte Carlo, se genera una distribucion de probabilidad de la perdida anual esperada.

### Ventajas de FAIR

- Produce cifras monetarias que la direccion puede comparar directamente con otros riesgos de negocio
- Facilita la priorizacion: el riesgo de 500.000 EUR/ano es claramente mas urgente que el de 15.000 EUR/ano
- Permite calcular el ROI de inversiones en seguridad de forma cuantitativa
- Transparente: los supuestos son explicitos y cuestionables
- Escalable: se puede aplicar a riesgos individuales o a portfolios de riesgo completos
- Compatible con marcos regulatorios que exigen analisis cuantitativo (DORA, Basel)

### Limitaciones de FAIR

- Requiere datos que muchas organizaciones no tienen (frecuencia de ataques, costes historicos de incidentes)
- El juicio experto introduce incertidumbre, aunque al menos es explicita
- No cubre la gestion de riesgos completa (identificacion de activos, controles, tratamiento), solo la cuantificacion
- La simulacion de Monte Carlo puede dar falsa sensacion de precision si los inputs son de baja calidad
- No esta alineada directamente con el ENS ni con las guias CCN-STIC
- Requiere formacion especifica que no es comun en equipos de seguridad espanoles

{{< cta type="tofu" text="Riskitera evalua tu postura de seguridad y te muestra los gaps de cumplimiento en minutos." label="Evaluar postura" >}}

## Ejemplo practico: el mismo riesgo analizado con MAGERIT y con FAIR

Para que la comparativa sea tangible, vamos a analizar el mismo escenario de riesgo con ambas metodologias. El escenario es real y comun: un ataque de ransomware contra una empresa industrial mediana (400 empleados, facturacion 50M EUR).

### El escenario

**Activo:** Sistema ERP (SAP) que soporta la gestion de pedidos, produccion y facturacion.

**Amenaza:** Ransomware desplegado tras acceso inicial via phishing, con movimiento lateral y cifrado del servidor ERP y sus backups locales.

**Contexto:** La empresa tiene antivirus tradicional, backups locales (sin air-gap), segmentacion de red basica y formacion de concienciacion anual.

### Analisis con MAGERIT

Siguiendo el proceso MAGERIT:

**Activo:** ERP/SAP. Valoracion en dimensiones de seguridad:
- Disponibilidad: 9/10 (la operacion se detiene completamente sin ERP)
- Integridad: 8/10 (datos financieros y de produccion criticos)
- Confidencialidad: 7/10 (datos comerciales y financieros sensibles)

**Amenaza:** [A.24] Denegacion de servicio (aplicada como ransomware). Degradacion: 100% en Disponibilidad, 50% en Integridad.

**Impacto potencial:** Muy Alto (degradacion del 100% sobre un activo valorado en 9/10).

**Frecuencia estimada:** Normal (una vez al ano en el sector industrial segun datos de [INCIBE](https://www.incibe.es/)).

**Riesgo sin salvaguardas:** Muy Alto.

**Salvaguardas existentes:** Antivirus (madurez L2), backups locales (madurez L2, sin air-gap), segmentacion basica (madurez L1), formacion anual (madurez L1).

**Eficacia estimada de salvaguardas:** 30-40%.

**Riesgo residual:** Alto.

**Conclusion MAGERIT:** El riesgo residual es Alto. Se recomienda implementar salvaguardas adicionales: backup off-site con air-gap (prioridad critica), EDR en endpoints (prioridad alta), segmentacion de red avanzada (prioridad alta), formacion trimestral con simulaciones de phishing (prioridad media).

### Analisis con FAIR

Siguiendo el proceso FAIR:

**Escenario:** Ransomware cifra el ERP y backups locales, paralizando la operacion.

**TEF (Threat Event Frequency):** Basandonos en datos del sector industrial espanol (informe INCIBE 2025), estimamos 2-6 intentos de ransomware al ano dirigidos a la organizacion, con un valor mas probable de 3. Usamos una distribucion PERT (min: 2, mas probable: 3, max: 6).

**Vulnerabilidad:** Con los controles actuales (AV tradicional, sin EDR, backups locales vulnerables, segmentacion basica), estimamos una probabilidad de exito del 20-40% por intento, con un valor mas probable del 30%.

**LEF (Loss Event Frequency):** TEF x Vulnerabilidad = 3 x 0.30 = 0.9 eventos de perdida por ano (aproximadamente uno cada 13 meses).

**Magnitud de la perdida (desglosada):**

| Componente | Minimo | Mas probable | Maximo |
|---|---|---|---|
| Respuesta al incidente (forense, recuperacion) | 30.000 EUR | 80.000 EUR | 200.000 EUR |
| Perdida de negocio (5 dias de paralizacion, facturacion diaria ~200K) | 500.000 EUR | 800.000 EUR | 1.200.000 EUR |
| Pago de rescate (si se decide pagar) | 0 EUR | 0 EUR | 500.000 EUR |
| Notificacion regulatoria y multas (RGPD, si hay exfiltracion) | 0 EUR | 50.000 EUR | 600.000 EUR |
| Dano reputacional (perdida de clientes) | 50.000 EUR | 200.000 EUR | 800.000 EUR |
| **Total por evento** | **580.000 EUR** | **1.130.000 EUR** | **3.300.000 EUR** |

**ALE (simulacion Monte Carlo, 10.000 iteraciones):**
- Percentil 10: 180.000 EUR/ano
- Mediana: 850.000 EUR/ano
- Percentil 90: 2.100.000 EUR/ano
- Media: 950.000 EUR/ano

**Conclusion FAIR:** La perdida anual esperada por ransomware es de aproximadamente 950.000 EUR, con un rango amplio que refleja la incertidumbre. Una inversion de 150.000 EUR en controles adicionales (EDR: 40.000 EUR, backup air-gap: 30.000 EUR, segmentacion avanzada: 50.000 EUR, formacion trimestral: 30.000 EUR) reduciria la vulnerabilidad al 5-10%, bajando la ALE a 150.000-300.000 EUR. El ROI de la inversion seria del 400-500% anual.

### Comparacion de resultados

| Aspecto | MAGERIT | FAIR |
|---|---|---|
| Resultado | Riesgo residual: Alto | ALE: ~950.000 EUR/ano |
| Priorizacion | Comparable con otros riesgos "Altos" | Comparable con cualquier riesgo de negocio en EUR |
| Argumento para inversion | "El riesgo es Alto, debemos reducirlo" | "Invertir 150K nos ahorra 600-800K al ano" |
| Precision percibida | Baja (subjetiva) | Alta (pero depende de la calidad de los inputs) |
| Tiempo de analisis | 2-4 horas por escenario | 4-8 horas por escenario (primera vez) |
| Requisito regulatorio | Cumple ENS directamente | No cumple ENS, necesita complementarse |

## Cuales son las diferencias entre FAIR y MAGERIT?

Mas alla del ejemplo practico, las diferencias fundamentales entre ambas metodologias se pueden agrupar en cinco ejes.

### Enfoque: cualitativo vs cuantitativo

MAGERIT produce resultados cualitativos (escalas de color, niveles de riesgo). FAIR produce resultados cuantitativos (distribuciones de probabilidad en euros). Ningun enfoque es inherentemente superior: depende del interlocutor y del proposito. Para un informe al CCN-CERT, necesitas MAGERIT. Para un business case de inversion, necesitas FAIR.

### Alcance: gestion completa vs cuantificacion

MAGERIT cubre todo el ciclo de gestion de riesgos: desde la identificacion de activos hasta la definicion de salvaguardas. FAIR solo cubre la cuantificacion del riesgo. FAIR no te dice que activos tienes, que amenazas existen ni que controles implementar. Solo te dice cuanto cuesta el riesgo en dinero. Por eso son complementarias, no competidoras.

### Regulacion: obligatoria vs opcional

Para organizaciones sujetas al ENS, MAGERIT es la metodologia de referencia. El [CCN-CERT](https://www.ccn-cert.cni.es/) proporciona PILAR como herramienta oficial para realizar analisis MAGERIT. FAIR no tiene este respaldo regulatorio en Espana, aunque DORA (para el sector financiero) y algunas directrices de [ENISA](https://www.enisa.europa.eu/) si mencionan explicitamente el analisis cuantitativo de riesgos.

### Datos requeridos: catalogos vs estimaciones

MAGERIT se apoya en catalogos predefinidos de amenazas y salvaguardas. El analista selecciona de una lista. FAIR requiere estimaciones numericas para cada factor (frecuencia, vulnerabilidad, magnitud de perdida). Esto significa que FAIR necesita mas contexto y experiencia del analista, pero tambien produce resultados mas granulares.

### Comunicacion: tecnica vs ejecutiva

Los resultados MAGERIT hablan el lenguaje de la seguridad: niveles de riesgo, dimensiones de seguridad, salvaguardas. Los resultados FAIR hablan el lenguaje del negocio: euros, probabilidades, ROI. Un CISO que necesite defender un presupuesto ante el comite de direccion tendra mas exito con un "el ransomware nos puede costar 950K al ano y con 150K de inversion lo bajamos a 250K" que con un "tenemos 15 riesgos en nivel Alto que necesitamos reducir".

## Cuando usar MAGERIT y cuando FAIR?

### Usa MAGERIT cuando:

- Tu organizacion esta sujeta al ENS (sector publico, proveedores de la administracion)
- Necesitas cumplir requisitos de auditoria del CCN-CERT
- Es tu primer analisis de riesgos y necesitas un marco estructurado completo
- Tu equipo tiene experiencia en PILAR y en las guias CCN-STIC
- El resultado se reporta a responsables tecnicos, no a financieros

### Usa FAIR cuando:

- Necesitas justificar inversiones en seguridad con numeros ante la direccion
- Tu organizacion opera en sectores donde el riesgo se mide en terminos financieros (banca, seguros)
- Quieres priorizar entre multiples riesgos usando una metrica comun (EUR de perdida esperada)
- DORA te exige analisis cuantitativo de riesgo operacional
- Tu interlocutor es el CFO, el comite de riesgos o el consejo de administracion

### Usa ambas cuando:

- Necesitas cumplir ENS pero tambien justificar presupuestos ante la direccion
- Tu organizacion tiene madurez suficiente para mantener ambas perspectivas
- Quieres un inventario completo de activos y amenazas (MAGERIT) combinado con cuantificacion financiera de los riesgos criticos (FAIR)

## Se pueden combinar FAIR y MAGERIT?

Si, y de hecho es el enfoque que recomendamos para organizaciones con cierta madurez. El enfoque hibrido aprovecha las fortalezas de cada metodologia y mitiga sus debilidades.

### Modelo hibrido: MAGERIT como base, FAIR como capa de cuantificacion

El flujo seria el siguiente:

**Fase 1: Inventario y analisis con MAGERIT.** Usa MAGERIT para identificar todos los activos, mapear amenazas, evaluar salvaguardas y obtener un mapa de riesgos cualitativo completo. Esto cumple con el ENS y proporciona la base documental para auditorias.

**Fase 2: Seleccion de riesgos criticos.** Del mapa de riesgos MAGERIT, selecciona los 10-15 riesgos clasificados como Alto o Muy Alto. Estos son los candidatos para cuantificacion FAIR.

**Fase 3: Cuantificacion FAIR de riesgos criticos.** Para cada riesgo critico, aplica el modelo FAIR para obtener la perdida anual esperada en euros. Esto permite priorizar entre riesgos que MAGERIT clasifica en el mismo nivel.

**Fase 4: Business case con datos FAIR.** Usa los resultados cuantitativos para construir business cases de inversion. Compara el coste de las salvaguardas propuestas con la reduccion de ALE que producen.

**Fase 5: Reporting dual.** Genera dos tipos de informe: el informe MAGERIT para auditorias ENS (cualitativo, con salvaguardas y niveles de riesgo) y el informe FAIR para la direccion (cuantitativo, con ALE, ROI y priorizacion financiera).

### Ejemplo del modelo hibrido

Imaginemos una organizacion con 45 riesgos identificados en MAGERIT:
- 3 riesgos Muy Alto
- 12 riesgos Alto
- 18 riesgos Medio
- 12 riesgos Bajo

Sin FAIR, los 15 riesgos Alto/Muy Alto compiten por atencion y presupuesto. El CISO tiene que decidir por intuicion cual atacar primero. Con FAIR aplicado a esos 15 riesgos:

| Riesgo | Nivel MAGERIT | ALE (FAIR) |
|---|---|---|
| Ransomware en ERP | Muy Alto | 950.000 EUR |
| Fuga de datos de clientes | Muy Alto | 720.000 EUR |
| Compromiso de credenciales VPN | Muy Alto | 380.000 EUR |
| DDoS en portal de clientes | Alto | 85.000 EUR |
| Acceso no autorizado a backups | Alto | 340.000 EUR |

Ahora la priorizacion es clara: el ransomware y la fuga de datos son las prioridades 1 y 2, aunque los tres estaban en "Muy Alto" con MAGERIT. Y el acceso a backups (Alto) tiene mas impacto financiero que el DDoS (Alto), algo que MAGERIT sola no podia distinguir.

## Que herramientas soportan cada metodologia?

### Herramientas para MAGERIT

- **PILAR/microPILAR:** Herramienta oficial del CCN-CERT. Gratuita para la administracion publica, de pago para sector privado. Soporta MAGERIT v3 completo con catalogos actualizados. Interfaz funcional pero de otra epoca.
- **PILAR Cloud:** Version cloud de PILAR disponible en el portal del CCN. Mejora la accesibilidad pero mantiene las mismas limitaciones de UX.
- **GlobalSuite Solutions:** Plataforma espanola de GRC que integra MAGERIT con otros frameworks (ISO 27001, ENS, RGPD).
- **Riskitera:** Soporta MAGERIT de forma nativa con automatizacion de evaluacion de amenazas y salvaguardas mediante IA, ademas de integracion con el SOC para alimentar el analisis con datos reales de incidentes.

### Herramientas para FAIR

- **RiskLens:** La plataforma de referencia para FAIR. Adquirida por Safe Security en 2023. Potente pero cara y enfocada a grandes corporaciones.
- **Safe Security:** Tras absorber RiskLens, integra FAIR con scoring continuo de riesgo ciber. Pricing enterprise.
- **FAIR-U:** Herramienta gratuita del FAIR Institute para analisis FAIR basicos. Util para aprender la metodologia.
- **Hojas de calculo:** Muchas organizaciones implementan FAIR en Excel con plantillas de simulacion Monte Carlo. Funcional para analisis individuales, no escalable.
- **Riskitera:** Soporta cuantificacion FAIR integrada con los datos de MAGERIT, permitiendo el enfoque hibrido descrito anteriormente.

{{< cta type="bofu" text="Empieza tu PoC de 90 dias con Riskitera y automatiza el compliance desde el primer dia." label="Iniciar PoC" >}}

## Errores comunes al medir riesgos y como evitarlos

Independientemente de la metodologia elegida, hay errores recurrentes que invalidan el analisis de riesgos.

### Error 1: Confundir amenaza con riesgo

"El ransomware" no es un riesgo. Es una amenaza. El riesgo es "ransomware que cifra el ERP y paraliza la produccion durante 5 dias, con una perdida estimada de 800K EUR". Un riesgo siempre vincula una amenaza con un activo y un impacto. Sin ese vinculo, no se puede medir.

### Error 2: Matrices de riesgo con demasiados niveles

Las matrices 5x5 producen 25 celdas de riesgo posibles, lo que parece granular. Pero en la practica, la diferencia entre "probabilidad 3, impacto 4" y "probabilidad 4, impacto 3" es indistinguible. Las mejores practicas recomendadas por [NIST](https://www.nist.gov/cyberframework) sugieren mantener la granularidad coherente con la capacidad de discriminacion real del equipo.

### Error 3: Analisis de riesgos como proyecto puntual

Un analisis de riesgos que se hace una vez al ano es una fotografia de un momento concreto. Los riesgos cambian con cada nuevo activo, cada nueva vulnerabilidad, cada cambio regulatorio. MAGERIT y FAIR deben alimentarse con datos actualizados continuamente, no una vez al ano antes de la auditoria.

### Error 4: Ignorar el riesgo residual

Implementar controles no elimina el riesgo, lo reduce. El riesgo residual (el que queda despues de aplicar los controles) es lo que realmente importa. Muchas organizaciones evaluan el riesgo inherente, implementan controles y asumen que el problema esta resuelto sin medir el riesgo residual real.

### Error 5: No calibrar las estimaciones

Las estimaciones de frecuencia y magnitud en FAIR, y las valoraciones de activos y amenazas en MAGERIT, deben calibrarse con datos reales. Los informes anuales de [INCIBE](https://www.incibe.es/), los datos sectoriales de [ENISA](https://www.enisa.europa.eu/) y los datos de inteligencia de amenazas ([MITRE ATT&CK](https://attack.mitre.org/)) son fuentes validas para contrastar las estimaciones del equipo.

## El futuro de la medicion de riesgos: IA y automatizacion

La IA esta transformando la medicion de riesgos de tres formas concretas:

**Automatizacion del inventario de activos.** Los modelos de IA pueden escanear la infraestructura, clasificar activos automaticamente y mantener el inventario actualizado en tiempo real, eliminando el principal cuello de botella de MAGERIT.

**Calibracion de estimaciones con datos reales.** La inteligencia de amenazas procesada por IA permite calibrar las estimaciones de frecuencia (TEF en FAIR) con datos del sector, la region y el perfil de la organizacion, en lugar de depender exclusivamente del juicio experto.

**Actualizacion continua del riesgo.** En lugar de analisis puntuales, la IA permite recalcular el riesgo continuamente a medida que cambian las amenazas, los activos y los controles. Un nuevo CVE critico en un componente del ERP deberia actualizar automaticamente el riesgo de ransomware sin esperar al proximo ciclo de revision.

Estas capacidades ya existen en plataformas GRC modernas y representan la evolucion natural de ambas metodologias: MAGERIT automatizada y FAIR alimentada con datos reales.


**Articulos relacionados:**
- [Analisis Riesgos Ciberseguridad Paso A Paso](/es/posts/2026/04/analisis-riesgos-ciberseguridad-paso-a-paso/)

## Preguntas frecuentes

### MAGERIT es obligatoria para todas las empresas en Espana?

No. MAGERIT es la metodologia de referencia para organizaciones sujetas al Esquema Nacional de Seguridad (ENS), que incluye la administracion publica, sus organismos dependientes y los proveedores que manejan datos del sector publico. Las empresas privadas no sujetas al ENS pueden usar cualquier metodologia de analisis de riesgos reconocida ([ISO 27005](https://www.iso.org/standard/27001), FAIR, OCTAVE, etc.). Sin embargo, incluso para empresas privadas, MAGERIT es una opcion solida por su exhaustividad y por la disponibilidad de catalogos en espanol.

### Cuanto tiempo lleva hacer un analisis de riesgos con FAIR?

El primer analisis FAIR de un escenario especifico puede llevar 4-8 horas, incluyendo la recopilacion de datos, las estimaciones y la simulacion. Con experiencia y datos historicos, el tiempo baja a 2-4 horas por escenario. Para una organizacion que quiera cuantificar los 10-15 riesgos mas criticos, un proyecto inicial de 3-4 semanas es realista. La clave es no intentar cuantificar todos los riesgos: FAIR se aplica a los mas criticos, no a los 200 riesgos del registro.

### Puedo usar FAIR para cumplir con NIS2 o DORA?

DORA (Digital Operational Resilience Act) exige explicitamente que las entidades financieras realicen analisis cuantitativos de riesgo operacional, lo que hace de FAIR una opcion natural. NIS2 no prescribe una metodologia especifica, pero sus requisitos de gestion de riesgos son compatibles con FAIR. En ambos casos, FAIR por si sola no cubre todos los requisitos de gestion de riesgos: necesitaras complementarla con un proceso de gestion de riesgos mas amplio (como el que proporciona MAGERIT o ISO 27005).

### Que datos necesito para empezar con FAIR si no tengo historico de incidentes?

No tener datos historicos propios no es un bloqueo para empezar con FAIR. Puedes usar: informes sectoriales de [INCIBE](https://www.incibe.es/) y [ENISA](https://www.enisa.europa.eu/) para frecuencias de amenazas, el informe anual de coste de brechas de IBM/Ponemon para magnitudes de perdida, datos de [MITRE ATT&CK](https://attack.mitre.org/) para tecnicas y tacticas de atacantes, y benchmarks del FAIR Institute para calibrar estimaciones. Lo importante es documentar las fuentes y los supuestos: un analisis FAIR con datos imperfectos pero supuestos transparentes es mas util que un analisis cualitativo que oculta la incertidumbre.

### Que metodologia recomendais como punto de partida?

Si tu organizacion esta sujeta al ENS, empieza por MAGERIT (no hay alternativa regulatoria). Si no, recomendamos empezar con un enfoque pragmatico: usa ISO 27005 o MAGERIT simplificada para construir el inventario de activos y el registro de riesgos, y aplica FAIR a los 5-10 riesgos mas criticos para obtener cifras que justifiquen la inversion en seguridad. A medida que la madurez del equipo crezca, expande la cuantificacion FAIR a mas escenarios. El error mas comun es paralizarse eligiendo la metodologia "perfecta" en lugar de empezar con cualquiera de las dos.
