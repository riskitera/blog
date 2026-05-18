---
title: "Cómo medir el riesgo ciber: metodologías FAIR vs MAGERIT en la práctica"
description: "Comparativa práctica de las metodologías FAIR y MAGERIT para medir el riesgo en ciberseguridad: cuándo usar cada una, ventajas, limitaciones y cómo combinarlas."
slug: "medir-riesgo-ciberseguridad-fair-magerit"
date: 2026-06-11
publishDate: 2026-06-11
lastmod: 2026-06-11
draft: false
tags: ["GRC", "Riesgos", "Metodología"]
categories: ["GRC"]
author: "David Moya"
keyword: "medir riesgo ciberseguridad"
funnel: "mofu"
---

Comparativa práctica de las metodologías FAIR y MAGERIT para medir el riesgo en ciberseguridad: cuándo usar cada una, ventajas, limitaciones y cómo combinarlas.

<!--more-->

{{< key-takeaways >}}
- MAGERIT es la metodología de referencia para el sector público español y obligatoria para el cumplimiento del ENS, con un enfoque cualitativo basado en activos, amenazas y salvaguardas
- FAIR cuantifica el riesgo en términos monetarios, permitiendo calcular la pérdida esperada anual (ALE) y facilitar la comunicación con la dirección financiera
- Ambas metodologías no son excluyentes: un enfoque híbrido que use MAGERIT para el inventario y las amenazas, y FAIR para la cuantificación financiera, da los mejores resultados
- La elección entre ambas depende del contexto regulatorio (ENS obliga MAGERIT), la madurez del equipo y el interlocutor (técnico vs financiero)
- Las herramientas automatizadas reducen el esfuerzo de aplicación de cualquiera de las dos metodologías en un 60-70%, eliminando el principal obstáculo: la carga manual
{{< /key-takeaways >}}

## ¿Cómo se mide el riesgo en ciberseguridad?

Medir el riesgo en ciberseguridad es una de las tareas más complejas y, paradójicamente, más importantes de un CISO. Sin una medición rigurosa, las decisiones de inversión en seguridad se basan en intuiciones, miedos o titulares de prensa. Con una medición rigurosa, el CISO puede responder preguntas concretas: cuánto dinero estamos dispuestos a perder, dónde tenemos las mayores exposiciones, y qué inversión reduce más riesgo por cada euro gastado.

El problema es que "medir riesgo" no significa lo mismo para todos. Para un auditor del [CCN-CERT](https://www.ccn-cert.cni.es/), medir riesgo es evaluar activos, identificar amenazas, calcular el impacto y la probabilidad, y determinar un nivel de riesgo cualitativo (Bajo, Medio, Alto, Muy Alto, Crítico). Para un CFO, medir riesgo es responder: cuánto dinero podemos perder si nos atacan, y cuál es la probabilidad de que eso ocurra este año.

Ambas perspectivas son válidas. Y para cada una existe una metodología establecida:

- **[MAGERIT](https://www.ccn-cert.cni.es/herramientas-de-ciberseguridad/ear-pilar.html)** (Metodología de Análisis y Gestión de Riesgos de los Sistemas de Información): desarrollada por el Consejo Superior de Administración Electrónica de España, es la referencia para el sector público y organizaciones sujetas al ENS.
- **[FAIR](https://www.fairinstitute.org/)** (Factor Analysis of Information Risk): un modelo cuantitativo desarrollado por Jack Jones que descompone el riesgo en factores medibles y lo expresa en términos monetarios.

En este artículo vamos a comparar ambas metodologías de forma práctica, analizando el mismo escenario de riesgo con cada una para que puedas ver las diferencias reales, no solo las teóricas.

## ¿Qué es la metodología MAGERIT?

MAGERIT es la metodología oficial de análisis de riesgos de la administración pública española. Su primera versión se publicó en 1997, y la versión 3 (vigente) en 2012. Está diseñada para cumplir con los requisitos del Esquema Nacional de Seguridad (ENS) y se apoya en la herramienta [PILAR](https://www.ccn-cert.cni.es/herramientas-de-ciberseguridad/ear-pilar.html), desarrollada por el CCN-CERT.

### Estructura de MAGERIT

MAGERIT se organiza en tres libros:

1. **Libro I: Método.** Define el proceso completo de análisis de riesgos: identificación de activos, valoración, identificación de amenazas, estimación de impacto y riesgo.
2. **Libro II: Catálogo de elementos.** Proporciona taxonomías de activos, dimensiones de valoración, amenazas y salvaguardas.
3. **Libro III: Guía de técnicas.** Describe técnicas complementarias como análisis de impacto en el negocio (BIA), árboles de ataque y análisis coste-beneficio.

### Proceso de análisis con MAGERIT

El proceso MAGERIT sigue estos pasos:

**Paso 1: Identificación y valoración de activos.** Se catalogan todos los activos de información (datos, servicios, aplicaciones, equipos, instalaciones, personal) y se valoran según cinco dimensiones de seguridad: Disponibilidad (D), Integridad (I), Confidencialidad (C), Autenticidad (A) y Trazabilidad (T). La valoración es cualitativa: de 0 (irrelevante) a 10 (daño muy grave).

**Paso 2: Identificación de amenazas.** Se identifican las amenazas que pueden afectar a cada activo, utilizando el catálogo de amenazas de MAGERIT. Las amenazas se clasifican en: naturales, industriales, errores y ataques deliberados.

**Paso 3: Estimación del impacto.** Se calcula el impacto potencial como la degradación que la amenaza puede causar sobre el activo en cada dimensión. El impacto se expresa como un porcentaje de degradación sobre el valor del activo.

**Paso 4: Estimación de la frecuencia.** Se estima la frecuencia con la que se espera que la amenaza se materialice. MAGERIT utiliza una escala cualitativa: despreciable, poco frecuente, normal, frecuente, muy frecuente.

**Paso 5: Cálculo del riesgo.** El riesgo se calcula como la combinación del impacto y la frecuencia. El resultado es un nivel de riesgo cualitativo que se posiciona en un mapa de calor.

**Paso 6: Evaluación de salvaguardas.** Se identifican las salvaguardas (controles) existentes y su nivel de madurez. El riesgo residual se calcula considerando la eficacia de las salvaguardas implementadas.

### Ventajas de MAGERIT

- Alineada al 100% con el ENS y las guías CCN-STIC
- Catálogo exhaustivo de amenazas y salvaguardas adaptado al contexto español
- Herramienta oficial (PILAR) disponible para la administración pública
- Proceso sistemático y repetible que facilita auditorías
- Bien documentada con ejemplos y guías en español

### Limitaciones de MAGERIT

- El resultado es cualitativo (Alto, Medio, Bajo), lo que dificulta la priorización cuando hay muchos riesgos en el mismo nivel
- No produce cifras monetarias, lo que complica la justificación de inversiones ante la dirección
- El proceso manual es intensivo en tiempo: una organización mediana puede necesitar 3-6 meses para un análisis completo
- Las escalas cualitativas introducen subjetividad: lo que un analista valora como "Alto" otro lo puede valorar como "Medio"
- El catálogo de amenazas, aunque exhaustivo, no se actualiza con la frecuencia del panorama de amenazas real

## ¿Qué es la metodología FAIR?

FAIR (Factor Analysis of Information Risk) es un modelo cuantitativo de análisis de riesgo creado por Jack Jones en 2005. A diferencia de MAGERIT, FAIR no prescribe un proceso de gestión de riesgos completo, sino que se centra en la cuantificación: descomponer el riesgo en factores medibles y expresar el resultado en términos monetarios (dólares o euros de pérdida esperada).

FAIR se convirtió en un estándar abierto de The Open Group en 2014, y el [FAIR Institute](https://www.fairinstitute.org/) promueve su adopción a nivel global. En 2025, FAIR-MAM (FAIR Materiality Assessment Model) amplió el framework para incluir análisis de materialidad regulatoria.

### Taxonomía de riesgo FAIR

FAIR descompone el riesgo en dos factores principales:

**LEF (Loss Event Frequency):** ¿Con qué frecuencia esperamos que un evento de pérdida ocurra en un periodo determinado. Se descompone en:
- TEF (Threat Event Frequency): frecuencia con la que un agente de amenaza actúa contra un activo
- Vulnerability: probabilidad de que la acción del agente de amenaza resulte en un evento de pérdida

**LM (Loss Magnitude):** Cuánto perdemos cuando el evento de pérdida ocurre. Se descompone en:
- Primary Loss: pérdida directa (respuesta al incidente, reposición de activos, productividad)
- Secondary Loss: pérdida indirecta (multas, litigios, daño reputacional, pérdida de clientes)

El resultado final es una distribución de probabilidad de la pérdida anual esperada (ALE, Annualized Loss Expectancy), típicamente expresada como un rango (por ejemplo: "hay un 90% de probabilidad de que la pérdida anual por ransomware esté entre 50.000 EUR y 1.200.000 EUR, con una mediana de 320.000 EUR").

### Proceso de análisis con FAIR

**Paso 1: Definir el escenario de riesgo.** Se identifica la combinación específica de activo, amenaza y efecto. Ejemplo: "ransomware que cifra el ERP y paraliza la operación durante 5 días".

**Paso 2: Estimar la frecuencia del evento de amenaza (TEF).** Utilizando datos históricos, inteligencia de amenazas o juicio experto, se estima cuántas veces al año un actor de amenaza intenta este tipo de ataque contra la organización.

**Paso 3: Estimar la vulnerabilidad.** Se evalúa la probabilidad de que el intento tenga éxito, considerando los controles existentes (segmentación de red, backups, EDR, formación).

**Paso 4: Calcular la frecuencia del evento de pérdida (LEF).** LEF = TEF x Vulnerabilidad.

**Paso 5: Estimar la magnitud de la perdida.** Se desglosan los costes: respuesta al incidente, pérdida de negocio, notificaciones regulatorias, multas, litigios, daño reputacional. Cada componente se estima como un rango (mínimo, más probable, máximo).

**Paso 6: Calcular el riesgo (ALE).** Utilizando simulación de Monte Carlo, se genera una distribución de probabilidad de la pérdida anual esperada.

### Ventajas de FAIR

- Produce cifras monetarias que la dirección puede comparar directamente con otros riesgos de negocio
- Facilita la priorización: el riesgo de 500.000 EUR/año es claramente más urgente que el de 15.000 EUR/año
- Permite calcular el ROI de inversiones en seguridad de forma cuantitativa
- Transparente: los supuestos son explícitos y cuestionables
- Escalable: se puede aplicar a riesgos individuales o a portfolios de riesgo completos
- Compatible con marcos regulatorios que exigen análisis cuantitativo (DORA, Basel)

### Limitaciones de FAIR

- Requiere datos que muchas organizaciones no tienen (frecuencia de ataques, costes históricos de incidentes)
- El juicio experto introduce incertidumbre, aunque al menos es explícita
- No cubre la gestión de riesgos completa (identificación de activos, controles, tratamiento), solo la cuantificación
- La simulación de Monte Carlo puede dar falsa sensación de precisión si los inputs son de baja calidad
- No está alineada directamente con el ENS ni con las guías CCN-STIC
- Requiere formación específica que no es común en equipos de seguridad españoles

{{< cta type="tofu" text="Riskitera evalua tu postura de seguridad y te muestra los gaps de cumplimiento en minutos." label="Evaluar postura" >}}

## Ejemplo práctico: el mismo riesgo analizado con MAGERIT y con FAIR

Para que la comparativa sea tangible, vamos a analizar el mismo escenario de riesgo con ambas metodologías. El escenario es real y común: un ataque de ransomware contra una empresa industrial mediana (400 empleados, facturación 50M EUR).

### El escenario

**Activo:** Sistema ERP (SAP) que soporta la gestión de pedidos, producción y facturación.

**Amenaza:** Ransomware desplegado tras acceso inicial vía phishing, con movimiento lateral y cifrado del servidor ERP y sus backups locales.

**Contexto:** La empresa tiene antivirus tradicional, backups locales (sin air-gap), segmentación de red básica y formación de concienciación anual.

### Análisis con MAGERIT

Siguiendo el proceso MAGERIT:

**Activo:** ERP/SAP. Valoración en dimensiones de seguridad:
- Disponibilidad: 9/10 (la operación se detiene completamente sin ERP)
- Integridad: 8/10 (datos financieros y de producción críticos)
- Confidencialidad: 7/10 (datos comerciales y financieros sensibles)

**Amenaza:** [A.24] Denegación de servicio (aplicada como ransomware). Degradación: 100% en Disponibilidad, 50% en Integridad.

**Impacto potencial:** Muy Alto (degradación del 100% sobre un activo valorado en 9/10).

**Frecuencia estimada:** Normal (una vez al año en el sector industrial según datos de [INCIBE](https://www.incibe.es/)).

**Riesgo sin salvaguardas:** Muy Alto.

**Salvaguardas existentes:** Antivirus (madurez L2), backups locales (madurez L2, sin air-gap), segmentación básica (madurez L1), formación anual (madurez L1).

**Eficacia estimada de salvaguardas:** 30-40%.

**Riesgo residual:** Alto.

**Conclusión MAGERIT:** El riesgo residual es Alto. Se recomienda implementar salvaguardas adicionales: backup off-site con air-gap (prioridad crítica), EDR en endpoints (prioridad alta), segmentación de red avanzada (prioridad alta), formación trimestral con simulaciones de phishing (prioridad media).

### Análisis con FAIR

Siguiendo el proceso FAIR:

**Escenario:** Ransomware cifra el ERP y backups locales, paralizando la operación.

**TEF (Threat Event Frequency):** Basándonos en datos del sector industrial español (informe INCIBE 2025), estimamos 2-6 intentos de ransomware al año dirigidos a la organización, con un valor más probable de 3. Usamos una distribución PERT (min: 2, más probable: 3, max: 6).

**Vulnerabilidad:** Con los controles actuales (AV tradicional, sin EDR, backups locales vulnerables, segmentación básica), estimamos una probabilidad de éxito del 20-40% por intento, con un valor más probable del 30%.

**LEF (Loss Event Frequency):** TEF x Vulnerabilidad = 3 x 0.30 = 0.9 eventos de pérdida por año (aproximadamente uno cada 13 meses).

**Magnitud de la pérdida (desglosada):**

| Componente | Mínimo | Más probable | Máximo |
|---|---|---|---|
| Respuesta al incidente (forense, recuperación) | 30.000 EUR | 80.000 EUR | 200.000 EUR |
| Perdida de negocio (5 días de paralización, facturación diaria ~200K) | 500.000 EUR | 800.000 EUR | 1.200.000 EUR |
| Pago de rescate (si se decide pagar) | 0 EUR | 0 EUR | 500.000 EUR |
| Notificación regulatoria y multas (RGPD, si hay exfiltración) | 0 EUR | 50.000 EUR | 600.000 EUR |
| Dano reputacional (pérdida de clientes) | 50.000 EUR | 200.000 EUR | 800.000 EUR |
| **Total por evento** | **580.000 EUR** | **1.130.000 EUR** | **3.300.000 EUR** |

**ALE (simulación Monte Carlo, 10.000 iteraciones):**
- Percentil 10: 180.000 EUR/año
- Mediana: 850.000 EUR/año
- Percentil 90: 2.100.000 EUR/año
- Media: 950.000 EUR/año

**Conclusión FAIR:** La pérdida anual esperada por ransomware es de aproximadamente 950.000 EUR, con un rango amplio que refleja la incertidumbre. Una inversión de 150.000 EUR en controles adicionales (EDR: 40.000 EUR, backup air-gap: 30.000 EUR, segmentación avanzada: 50.000 EUR, formación trimestral: 30.000 EUR) reduciría la vulnerabilidad al 5-10%, bajando la ALE a 150.000-300.000 EUR. El ROI de la inversión sería del 400-500% anual.

### Comparación de resultados

| Aspecto | MAGERIT | FAIR |
|---|---|---|
| Resultado | Riesgo residual: Alto | ALE: ~950.000 EUR/año |
| Priorización | Comparable con otros riesgos "Altos" | Comparable con cualquier riesgo de negocio en EUR |
| Argumento para inversión | "El riesgo es Alto, debemos reducirlo" | "Invertir 150K nos ahorra 600-800K al año" |
| Precisión percibida | Baja (subjetiva) | Alta (pero depende de la calidad de los inputs) |
| Tiempo de análisis | 2-4 horas por escenario | 4-8 horas por escenario (primera vez) |
| Requisito regulatorio | Cumple ENS directamente | No cumple ENS, necesita complementarse |

## ¿Cuáles son las diferencias entre FAIR y MAGERIT?

Más allá del ejemplo práctico, las diferencias fundamentales entre ambas metodologías se pueden agrupar en cinco ejes.

### Enfoque: cualitativo vs cuantitativo

MAGERIT produce resultados cualitativos (escalas de color, niveles de riesgo). FAIR produce resultados cuantitativos (distribuciones de probabilidad en euros). Ningún enfoque es inherentemente superior: depende del interlocutor y del propósito. Para un informe al CCN-CERT, necesitas MAGERIT. Para un business case de inversión, necesitas FAIR.

### Alcance: gestión completa vs cuantificación

MAGERIT cubre todo el ciclo de gestión de riesgos: desde la identificación de activos hasta la definición de salvaguardas. FAIR solo cubre la cuantificación del riesgo. FAIR no te dice qué activos tienes, qué amenazas existen ni qué controles implementar. Solo te dice cuánto cuesta el riesgo en dinero. Por eso son complementarias, no competidoras.

### Regulación: obligatoria vs opcional

Para organizaciones sujetas al ENS, MAGERIT es la metodología de referencia. El [CCN-CERT](https://www.ccn-cert.cni.es/) proporciona PILAR como herramienta oficial para realizar análisis MAGERIT. FAIR no tiene este respaldo regulatorio en España, aunque DORA (para el sector financiero) y algunas directrices de [ENISA](https://www.enisa.europa.eu/) sí mencionan explícitamente el análisis cuantitativo de riesgos.

### Datos requeridos: catálogos vs estimaciones

MAGERIT se apoya en catálogos predefinidos de amenazas y salvaguardas. El analista selecciona de una lista. FAIR requiere estimaciones numéricas para cada factor (frecuencia, vulnerabilidad, magnitud de pérdida). Esto significa que FAIR necesita más contexto y experiencia del analista, pero también produce resultados más granulares.

### Comunicación: técnica vs ejecutiva

Los resultados MAGERIT hablan el lenguaje de la seguridad: niveles de riesgo, dimensiones de seguridad, salvaguardas. Los resultados FAIR hablan el lenguaje del negocio: euros, probabilidades, ROI. Un CISO que necesite defender un presupuesto ante el comité de dirección tendrá más éxito con un "el ransomware nos puede costar 950K al año y con 150K de inversión lo bajamos a 250K" que con un "tenemos 15 riesgos en nivel Alto que necesitamos reducir".

## ¿Cuándo usar MAGERIT y cuándo FAIR?

### Usa MAGERIT cuando:

- Tu organización está sujeta al ENS (sector público, proveedores de la administración)
- Necesitas cumplir requisitos de auditoría del CCN-CERT
- Es tu primer análisis de riesgos y necesitas un marco estructurado completo
- Tu equipo tiene experiencia en PILAR y en las guías CCN-STIC
- El resultado se reporta a responsables técnicos, no a financieros

### Usa FAIR cuando:

- Necesitas justificar inversiones en seguridad con números ante la dirección
- Tu organización opera en sectores donde el riesgo se mide en términos financieros (banca, seguros)
- Quieres priorizar entre múltiples riesgos usando una métrica común (EUR de pérdida esperada)
- DORA te exige análisis cuantitativo de riesgo operacional
- Tu interlocutor es el CFO, el comité de riesgos o el consejo de administración

### Usa ambas cuando:

- Necesitas cumplir ENS pero también justificar presupuestos ante la dirección
- Tu organización tiene madurez suficiente para mantener ambas perspectivas
- Quieres un inventario completo de activos y amenazas (MAGERIT) combinado con cuantificación financiera de los riesgos críticos (FAIR)

## ¿Se pueden combinar FAIR y MAGERIT?

Sí, y de hecho es el enfoque que recomendamos para organizaciones con cierta madurez. El enfoque híbrido aprovecha las fortalezas de cada metodología y mitiga sus debilidades.

### Modelo híbrido: MAGERIT como base, FAIR como capa de cuantificación

El flujo sería el siguiente:

**Fase 1: Inventario y análisis con MAGERIT.** Usa MAGERIT para identificar todos los activos, mapear amenazas, evaluar salvaguardas y obtener un mapa de riesgos cualitativo completo. Esto cumple con el ENS y proporciona la base documental para auditorías.

**Fase 2: Selección de riesgos críticos.** Del mapa de riesgos MAGERIT, selecciona los 10-15 riesgos clasificados como Alto o Muy Alto. Estos son los candidatos para cuantificación FAIR.

**Fase 3: Cuantificación FAIR de riesgos críticos.** Para cada riesgo crítico, aplica el modelo FAIR para obtener la pérdida anual esperada en euros. Esto permite priorizar entre riesgos que MAGERIT clasifica en el mismo nivel.

**Fase 4: Business case con datos FAIR.** Usa los resultados cuantitativos para construir business cases de inversión. Compara el coste de las salvaguardas propuestas con la reducción de ALE que producen.

**Fase 5: Reporting dual.** Genera dos tipos de informe: el informe MAGERIT para auditorías ENS (cualitativo, con salvaguardas y niveles de riesgo) y el informe FAIR para la dirección (cuantitativo, con ALE, ROI y priorización financiera).

### Ejemplo del modelo híbrido

Imaginemos una organización con 45 riesgos identificados en MAGERIT:
- 3 riesgos Muy Alto
- 12 riesgos Alto
- 18 riesgos Medio
- 12 riesgos Bajo

Sin FAIR, los 15 riesgos Alto/Muy Alto compiten por atención y presupuesto. El CISO tiene que decidir por intuición cuál atacar primero. Con FAIR aplicado a esos 15 riesgos:

| Riesgo | Nivel MAGERIT | ALE (FAIR) |
|---|---|---|
| Ransomware en ERP | Muy Alto | 950.000 EUR |
| Fuga de datos de clientes | Muy Alto | 720.000 EUR |
| Compromiso de credenciales VPN | Muy Alto | 380.000 EUR |
| DDoS en portal de clientes | Alto | 85.000 EUR |
| Acceso no autorizado a backups | Alto | 340.000 EUR |

Ahora la priorización es clara: el ransomware y la fuga de datos son las prioridades 1 y 2, aunque los tres estaban en "Muy Alto" con MAGERIT. Y el acceso a backups (Alto) tiene más impacto financiero que el DDoS (Alto), algo que MAGERIT sola no podía distinguir.

## ¿Qué herramientas soportan cada metodología?

### Herramientas para MAGERIT

- **PILAR/microPILAR:** Herramienta oficial del CCN-CERT. Gratuita para la administración pública, de pago para sector privado. Soporta MAGERIT v3 completo con catálogos actualizados. Interfaz funcional pero de otra época.
- **PILAR Cloud:** Versión cloud de PILAR disponible en el portal del CCN. Mejora la accesibilidad pero mantiene las mismas limitaciones de UX.
- **GlobalSuite Solutions:** Plataforma española de GRC que integra MAGERIT con otros frameworks (ISO 27001, ENS, RGPD).
- **Riskitera:** Soporta MAGERIT de forma nativa con automatización de evaluación de amenazas y salvaguardas mediante IA, además de integración con el SOC para alimentar el análisis con datos reales de incidentes.

### Herramientas para FAIR

- **RiskLens:** La plataforma de referencia para FAIR. Adquirida por Safe Security en 2023. Potente pero cara y enfocada a grandes corporaciones.
- **Safe Security:** Tras absorber RiskLens, integra FAIR con scoring continuo de riesgo ciber. Pricing enterprise.
- **FAIR-U:** Herramienta gratuita del FAIR Institute para análisis FAIR básicos. Útil para aprender la metodología.
- **Hojas de calculo:** Muchas organizaciones implementan FAIR en Excel con plantillas de simulación Monte Carlo. Funcional para análisis individuales, no escalable.
- **Riskitera:** Soporta cuantificación FAIR integrada con los datos de MAGERIT, permitiendo el enfoque híbrido descrito anteriormente.

{{< cta type="bofu" text="Empieza tu PoC de 90 días con Riskitera y automatiza el compliance desde el primer dia." label="Iniciar PoC" >}}

## Errores comunes al medir riesgos y cómo evitarlos

Independientemente de la metodología elegida, hay errores recurrentes que invalidan el análisis de riesgos.

### Error 1: Confundir amenaza con riesgo

"El ransomware" no es un riesgo. Es una amenaza. El riesgo es "ransomware que cifra el ERP y paraliza la producción durante 5 días, con una pérdida estimada de 800K EUR". Un riesgo siempre vincula una amenaza con un activo y un impacto. Sin ese vínculo, no se puede medir.

### Error 2: Matrices de riesgo con demasiados niveles

Las matrices 5x5 producen 25 celdas de riesgo posibles, lo que parece granular. Pero en la práctica, la diferencia entre "probabilidad 3, impacto 4" y "probabilidad 4, impacto 3" es indistinguible. Las mejores prácticas recomendadas por [NIST](https://www.nist.gov/cyberframework) sugieren mantener la granularidad coherente con la capacidad de discriminación real del equipo.

### Error 3: Análisis de riesgos como proyecto puntual

Un análisis de riesgos que se hace una vez al año es una fotografía de un momento concreto. Los riesgos cambian con cada nuevo activo, cada nueva vulnerabilidad, cada cambio regulatorio. MAGERIT y FAIR deben alimentarse con datos actualizados continuamente, no una vez al año antes de la auditoría.

### Error 4: Ignorar el riesgo residual

Implementar controles no elimina el riesgo, lo reduce. El riesgo residual (el que queda después de aplicar los controles) es lo que realmente importa. Muchas organizaciones evalúan el riesgo inherente, implementan controles y asumen que el problema está resuelto sin medir el riesgo residual real.

### Error 5: No calibrar las estimaciones

Las estimaciones de frecuencia y magnitud en FAIR, y las valoraciones de activos y amenazas en MAGERIT, deben calibrarse con datos reales. Los informes anuales de [INCIBE](https://www.incibe.es/), los datos sectoriales de [ENISA](https://www.enisa.europa.eu/) y los datos de inteligencia de amenazas ([MITRE ATT&CK](https://attack.mitre.org/)) son fuentes válidas para contrastar las estimaciones del equipo.

## El futuro de la medición de riesgos: IA y automatización

La IA está transformando la medición de riesgos de tres formas concretas:

**Automatización del inventario de activos.** Los modelos de IA pueden escanear la infraestructura, clasificar activos automáticamente y mantener el inventario actualizado en tiempo real, eliminando el principal cuello de botella de MAGERIT.

**Calibración de estimaciones con datos reales.** La inteligencia de amenazas procesada por IA permite calibrar las estimaciones de frecuencia (TEF en FAIR) con datos del sector, la región y el perfil de la organización, en lugar de depender exclusivamente del juicio experto.

**Actualización continua del riesgo.** En lugar de análisis puntuales, la IA permite recalcular el riesgo continuamente a medida que cambian las amenazas, los activos y los controles. Un nuevo CVE crítico en un componente del ERP debería actualizar automáticamente el riesgo de ransomware sin esperar al próximo ciclo de revisión.

Estas capacidades ya existen en plataformas GRC modernas y representan la evolución natural de ambas metodologías: MAGERIT automatizada y FAIR alimentada con datos reales.


**Artículos relacionados:**
- [Análisis Riesgos Ciberseguridad Paso A Paso](/es/posts/2026/04/análisis-riesgos-ciberseguridad-paso-a-paso/)

## Preguntas frecuentes

### ¿MAGERIT es obligatoria para todas las empresas en España?

No. MAGERIT es la metodología de referencia para organizaciones sujetas al Esquema Nacional de Seguridad (ENS), que incluye la administración pública, sus organismos dependientes y los proveedores que manejan datos del sector público. Las empresas privadas no sujetas al ENS pueden usar cualquier metodología de análisis de riesgos reconocida ([ISO 27005](https://www.iso.org/standard/27001), FAIR, OCTAVE, etc.). Sin embargo, incluso para empresas privadas, MAGERIT es una opción sólida por su exhaustividad y por la disponibilidad de catálogos en español.

### ¿Cuánto tiempo lleva hacer un análisis de riesgos con FAIR?

El primer análisis FAIR de un escenario específico puede llevar 4-8 horas, incluyendo la recopilación de datos, las estimaciones y la simulación. Con experiencia y datos históricos, el tiempo baja a 2-4 horas por escenario. Para una organización que quiera cuantificar los 10-15 riesgos más críticos, un proyecto inicial de 3-4 semanas es realista. La clave es no intentar cuantificar todos los riesgos: FAIR se aplica a los más críticos, no a los 200 riesgos del registro.

### ¿Puedo usar FAIR para cumplir con NIS2 o DORA?

DORA (Digital Operational Resilience Act) exige explícitamente que las entidades financieras realicen análisis cuantitativos de riesgo operacional, lo que hace de FAIR una opción natural. NIS2 no prescribe una metodología específica, pero sus requisitos de gestión de riesgos son compatibles con FAIR. En ambos casos, FAIR por sí sola no cubre todos los requisitos de gestión de riesgos: necesitarás complementarla con un proceso de gestión de riesgos más amplio (como el que proporciona MAGERIT o ISO 27005).

### ¿Qué datos necesito para empezar con FAIR si no tengo histórico de incidentes?

No tener datos históricos propios no es un bloqueo para empezar con FAIR. Puedes usar: informes sectoriales de [INCIBE](https://www.incibe.es/) y [ENISA](https://www.enisa.europa.eu/) para frecuencias de amenazas, el informe anual de coste de brechas de IBM/Ponemon para magnitudes de pérdida, datos de [MITRE ATT&CK](https://attack.mitre.org/) para técnicas y tácticas de atacantes, y benchmarks del FAIR Institute para calibrar estimaciones. Lo importante es documentar las fuentes y los supuestos: un análisis FAIR con datos imperfectos pero supuestos transparentes es más útil que un análisis cualitativo que oculta la incertidumbre.

### ¿Qué metodología recomendáis como punto de partida?

Si tu organización está sujeta al ENS, empieza por MAGERIT (no hay alternativa regulatoria). Si no, recomendamos empezar con un enfoque pragmático: usa ISO 27005 o MAGERIT simplificada para construir el inventario de activos y el registro de riesgos, y aplica FAIR a los 5-10 riesgos más críticos para obtener cifras que justifiquen la inversión en seguridad. A medida que la madurez del equipo crezca, expande la cuantificación FAIR a más escenarios. El error más común es paralizarse eligiendo la metodología "perfecta" en lugar de empezar con cualquiera de las dos.
