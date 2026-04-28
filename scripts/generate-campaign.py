#!/usr/bin/env python3
"""Generate 36 blog posts for SEO campaign weeks 5-16."""
import os
from datetime import date, timedelta

BLOG_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "es", "posts")

# Base date: week 5 starts Monday 2026-05-05 (4 weeks after last batch)
BASE_DATE = date(2026, 5, 5)

ARTICLES = [
    # Week 5 — Compliance Deep Dive
    {
        "num": 15, "week": 5, "day": 0,
        "slug": "ens-alto-medio-bajo-diferencias",
        "title": "ENS Alto vs Medio vs Bajo: diferencias, requisitos y como elegir categoria",
        "description": "Comparativa detallada de los tres niveles del Esquema Nacional de Seguridad (ENS): criterios de categorizacion, medidas obligatorias por nivel y como elegir la categoria correcta para tu organizacion.",
        "tags": ["ENS", "Compliance", "Seguridad"],
        "categories": ["Compliance"],
        "keyword": "ENS alto medio bajo",
        "funnel": "tofu",
        "persona": "Compliance Officer",
        "h2s": [
            "Que diferencias hay entre ENS Alto, Medio y Bajo?",
            "Como se categoriza un sistema en el ENS?",
            "Que medidas de seguridad exige cada nivel?",
            "Como elegir la categoria ENS correcta para tu organizacion?",
            "Que pasa si categorizo mal mi sistema?",
            "Cuanto cuesta implementar cada nivel del ENS?",
            "Como se relacionan los niveles del ENS con ISO 27001?",
        ],
        "internal_links": ["/es/posts/2026/04/que-es-esquema-nacional-seguridad-ens/"],
    },
    {
        "num": 16, "week": 5, "day": 2,
        "slug": "diferencias-ens-iso-27001",
        "title": "Diferencias entre ENS e ISO 27001: cual necesita tu empresa",
        "description": "Analisis completo de las diferencias entre el Esquema Nacional de Seguridad y la norma ISO 27001: alcance, obligatoriedad, controles, certificacion y cuando implementar uno, otro o ambos.",
        "tags": ["ENS", "ISO 27001", "Compliance"],
        "categories": ["Compliance"],
        "keyword": "diferencias ENS ISO 27001",
        "funnel": "tofu",
        "persona": "CISO",
        "h2s": [
            "Cuales son las diferencias clave entre ENS e ISO 27001?",
            "Es obligatorio el ENS o la ISO 27001?",
            "Como se comparan los controles de ENS y los del Anexo A de ISO 27001?",
            "Puede una organizacion cumplir ambos a la vez?",
            "Que certificacion necesita mi empresa?",
            "Cuanto cuesta cada certificacion?",
            "Como aprovechar sinergias entre ENS e ISO 27001?",
        ],
        "internal_links": ["/es/posts/2026/04/que-es-esquema-nacional-seguridad-ens/", "/es/posts/2026/02/guia-iso-27001-startups/"],
    },
    {
        "num": 17, "week": 5, "day": 4,
        "slug": "requisitos-nis2-espana-checklist",
        "title": "Requisitos NIS2 para empresas espanolas: checklist completo 2026",
        "description": "Checklist completo de los requisitos de la Directiva NIS2 aplicables a empresas espanolas: medidas de gestion de riesgos, notificacion de incidentes, gobernanza y plazos de cumplimiento.",
        "tags": ["NIS2", "Compliance", "Europa"],
        "categories": ["Compliance"],
        "keyword": "requisitos NIS2 espana",
        "funnel": "mofu",
        "persona": "Compliance Officer",
        "h2s": [
            "Cuales son los requisitos de NIS2 para empresas espanolas?",
            "Que medidas de gestion de riesgos exige NIS2?",
            "Como debe ser la notificacion de incidentes bajo NIS2?",
            "Que requisitos de gobernanza establece NIS2?",
            "Que empresas estan obligadas a cumplir NIS2 en Espana?",
            "Cual es el plazo para cumplir con NIS2?",
            "Checklist de cumplimiento NIS2: los 10 puntos clave",
            "Que sanciones hay por incumplir NIS2 en Espana?",
        ],
        "internal_links": ["/es/posts/2026/04/nis2-que-es-a-quien-afecta/"],
    },
    # Week 6 — IA + Seguridad
    {
        "num": 18, "week": 6, "day": 0,
        "slug": "inteligencia-artificial-ciberseguridad-2026",
        "title": "Inteligencia artificial en ciberseguridad: estado real en 2026",
        "description": "Estado actual de la inteligencia artificial aplicada a la ciberseguridad en 2026: casos de uso reales en SOC, GRC y CTI, limitaciones, riesgos y tendencias para los proximos anos.",
        "tags": ["IA", "Ciberseguridad", "Tendencias"],
        "categories": ["SOC"],
        "keyword": "inteligencia artificial ciberseguridad",
        "funnel": "tofu",
        "persona": "CISO",
        "h2s": [
            "Como se usa la inteligencia artificial en ciberseguridad en 2026?",
            "Que casos de uso reales tiene la IA en el SOC?",
            "Como ayuda la IA al compliance y GRC?",
            "Que riesgos tiene el uso de IA en seguridad?",
            "IA generativa en ciberseguridad: oportunidad o amenaza?",
            "Que tendencias de IA en ciberseguridad veremos en 2027?",
            "Como empezar a integrar IA en tu equipo de seguridad?",
        ],
        "internal_links": ["/es/posts/2026/04/como-montar-soc-desde-cero/", "/es/posts/2026/04/analista-soc-roles-n1-n2-n3/"],
    },
    {
        "num": 19, "week": 6, "day": 2,
        "slug": "automatizar-auditorias-seguridad-ia",
        "title": "Automatizacion de auditorias con IA: del papel al triage en minutos",
        "description": "Como automatizar auditorias de seguridad informatica con inteligencia artificial: recopilacion de evidencias, analisis de gaps, generacion de informes y reduccion de costes operativos.",
        "tags": ["IA", "Auditoria", "GRC"],
        "categories": ["GRC"],
        "keyword": "automatizar auditorias seguridad",
        "funnel": "mofu",
        "persona": "CISO",
        "h2s": [
            "Por que automatizar las auditorias de seguridad?",
            "Que partes de una auditoria se pueden automatizar con IA?",
            "Como funciona la recopilacion automatica de evidencias?",
            "Como detecta la IA gaps de cumplimiento?",
            "Que ahorro supone automatizar auditorias?",
            "Que herramientas existen para automatizar auditorias?",
            "Como implementar la automatizacion paso a paso?",
        ],
        "internal_links": ["/es/posts/2026/04/auditoria-seguridad-informatica-guia/"],
    },
    {
        "num": 20, "week": 6, "day": 4,
        "slug": "agentes-ia-soc-triage-alertas",
        "title": "Agentes de IA para SOC: como automatizar el triage de alertas sin perder contexto",
        "description": "Guia practica sobre agentes de inteligencia artificial para centros de operaciones de seguridad (SOC): automatizacion del triage, reduccion de falsos positivos y escalado inteligente.",
        "tags": ["IA", "SOC", "Operaciones"],
        "categories": ["SOC"],
        "keyword": "agentes IA SOC",
        "funnel": "mofu",
        "persona": "SOC Manager",
        "h2s": [
            "Que son los agentes de IA para SOC?",
            "Como automatizan los agentes el triage de alertas?",
            "Que impacto tienen en la reduccion de falsos positivos?",
            "Como mantener el contexto humano en el triage automatizado?",
            "Que arquitectura necesita un SOC para integrar agentes IA?",
            "Cuales son los riesgos de automatizar el triage?",
            "Como empezar con agentes IA en tu SOC?",
        ],
        "internal_links": ["/es/posts/2026/04/como-montar-soc-desde-cero/", "/es/posts/2026/04/analista-soc-roles-n1-n2-n3/"],
    },
    # Week 7 — Sector Specific
    {
        "num": 21, "week": 7, "day": 0,
        "slug": "ciberseguridad-banca-dora",
        "title": "Ciberseguridad en banca: como cumplir DORA paso a paso",
        "description": "Guia practica para entidades bancarias y fintech sobre como cumplir el reglamento DORA: requisitos tecnicos, gestion de riesgos TIC, pruebas de resiliencia y plazos de implementacion.",
        "tags": ["DORA", "Banca", "Fintech", "Compliance"],
        "categories": ["Compliance"],
        "keyword": "DORA bancos",
        "funnel": "mofu",
        "persona": "CTO regulado",
        "h2s": [
            "Como afecta DORA a los bancos y entidades financieras?",
            "Cuales son los requisitos tecnicos de DORA para banca?",
            "Como implementar la gestion de riesgos TIC que exige DORA?",
            "Que pruebas de resiliencia operativa son obligatorias?",
            "Como gestionar proveedores TIC criticos bajo DORA?",
            "Cual es el calendario de implementacion para banca?",
            "Que sanciones aplican a entidades financieras que incumplan?",
        ],
        "internal_links": ["/es/posts/2026/04/dora-reglamento-ciberseguridad-financiera/"],
    },
    {
        "num": 22, "week": 7, "day": 2,
        "slug": "ciberseguridad-sector-salud-ens-rgpd",
        "title": "Seguridad en el sector salud: proteger datos clinicos bajo ENS y RGPD",
        "description": "Guia de ciberseguridad para hospitales y centros sanitarios: proteccion de datos clinicos, cumplimiento del ENS y RGPD, amenazas especificas del sector salud y buenas practicas.",
        "tags": ["Salud", "ENS", "RGPD", "Compliance"],
        "categories": ["Compliance"],
        "keyword": "ciberseguridad hospitales",
        "funnel": "mofu",
        "persona": "CISO",
        "h2s": [
            "Por que es critica la ciberseguridad en el sector salud?",
            "Que normativas de seguridad aplican a hospitales en Espana?",
            "Como proteger datos clinicos bajo RGPD?",
            "Que requisitos del ENS afectan al sector sanitario?",
            "Cuales son las amenazas mas comunes en sanidad?",
            "Como implementar un plan de seguridad en un hospital?",
            "Que coste tiene un incidente de seguridad en sanidad?",
        ],
        "internal_links": ["/es/posts/2026/04/que-es-esquema-nacional-seguridad-ens/"],
    },
    {
        "num": 23, "week": 7, "day": 4,
        "slug": "ens-administracion-publica",
        "title": "ENS en la administracion publica: requisitos, plazos y errores comunes",
        "description": "Guia practica del Esquema Nacional de Seguridad para administraciones publicas: requisitos obligatorios, plazos de cumplimiento, herramientas del CCN y errores frecuentes en la implementacion.",
        "tags": ["ENS", "Administracion Publica", "Compliance"],
        "categories": ["Compliance"],
        "keyword": "ENS administracion publica",
        "funnel": "mofu",
        "persona": "Compliance Officer",
        "h2s": [
            "Que exige el ENS a las administraciones publicas?",
            "Cuales son los plazos de cumplimiento del ENS para AA.PP.?",
            "Que herramientas proporciona el CCN para cumplir el ENS?",
            "Como categorizan los sistemas las administraciones publicas?",
            "Cuales son los errores mas comunes de las AA.PP. con el ENS?",
            "Que papel juegan los proveedores tecnologicos de la AA.PP.?",
            "Como afecta NIS2 a las administraciones publicas espanolas?",
        ],
        "internal_links": ["/es/posts/2026/04/que-es-esquema-nacional-seguridad-ens/", "/es/posts/2026/04/nis2-que-es-a-quien-afecta/"],
    },
    # Week 8 — Pillar + MOFU
    {
        "num": 24, "week": 8, "day": 0,
        "slug": "guia-compliance-ciberseguridad-2026",
        "title": "Guia completa de compliance en ciberseguridad 2026",
        "description": "Guia definitiva de compliance en ciberseguridad para empresas espanolas y europeas: ENS, NIS2, DORA, ISO 27001, RGPD, EU AI Act. Requisitos, plazos, herramientas y estrategias de cumplimiento.",
        "tags": ["Compliance", "ENS", "NIS2", "DORA", "ISO 27001", "RGPD"],
        "categories": ["Compliance"],
        "keyword": "compliance ciberseguridad",
        "funnel": "mofu",
        "persona": "CISO",
        "pillar": True,
        "h2s": [
            "Que es el compliance en ciberseguridad?",
            "Cuales son las normativas clave en Espana y Europa?",
            "Como se relacionan ENS, NIS2, DORA e ISO 27001?",
            "Que pasos seguir para implementar un programa de compliance?",
            "Como automatizar el compliance con tecnologia?",
            "Que rol juega el CISO en el compliance?",
            "Cuanto cuesta el compliance en ciberseguridad?",
            "Que pasa si no cumples: sanciones y consecuencias",
            "Tendencias en compliance para 2027",
        ],
        "internal_links": [
            "/es/posts/2026/04/que-es-esquema-nacional-seguridad-ens/",
            "/es/posts/2026/04/nis2-que-es-a-quien-afecta/",
            "/es/posts/2026/04/dora-reglamento-ciberseguridad-financiera/",
            "/es/posts/2026/02/guia-iso-27001-startups/",
        ],
    },
    {
        "num": 25, "week": 8, "day": 2,
        "slug": "como-elegir-plataforma-grc",
        "title": "Como elegir una plataforma GRC: criterios reales para empresas reguladas",
        "description": "Guia de compra para CISOs y compliance managers: criterios para elegir una plataforma GRC, funcionalidades clave, preguntas al proveedor, costes y errores al evaluar herramientas de compliance.",
        "tags": ["GRC", "Herramientas", "Compliance"],
        "categories": ["GRC"],
        "keyword": "plataforma GRC",
        "funnel": "mofu",
        "persona": "CISO",
        "h2s": [
            "Que es una plataforma GRC y para que sirve?",
            "Que funcionalidades debe tener una plataforma GRC?",
            "Cuales son los criterios clave para elegir?",
            "Que preguntas hacer al proveedor de GRC?",
            "Cuanto cuesta una plataforma GRC?",
            "On-premise vs SaaS: que modelo elegir?",
            "Cuales son los errores mas comunes al evaluar herramientas GRC?",
        ],
        "internal_links": ["/es/posts/2026/04/auditoria-seguridad-informatica-guia/", "/es/posts/2026/04/analisis-riesgos-ciberseguridad-paso-a-paso/"],
    },
    {
        "num": 26, "week": 8, "day": 4,
        "slug": "rgpd-2026-checklist-empresas",
        "title": "RGPD en 2026: checklist actualizado para empresas espanolas",
        "description": "Checklist actualizado de cumplimiento RGPD para empresas espanolas en 2026: obligaciones del responsable, derechos de los interesados, DPO, evaluaciones de impacto y sanciones recientes.",
        "tags": ["RGPD", "Compliance", "Seguridad"],
        "categories": ["Compliance"],
        "keyword": "cumplir RGPD 2026",
        "funnel": "mofu",
        "persona": "DPO",
        "h2s": [
            "Que obligaciones tiene una empresa bajo el RGPD en 2026?",
            "Cuando es obligatorio designar un DPO?",
            "Como realizar una evaluacion de impacto (EIPD)?",
            "Cuales son los derechos de los interesados?",
            "Que cambios hay en la aplicacion del RGPD en 2026?",
            "Checklist de cumplimiento RGPD: los 12 puntos clave",
            "Que sanciones por incumplimiento del RGPD ha habido en Espana?",
        ],
        "internal_links": ["/es/posts/2026/04/politicas-seguridad-informatica-como-crearlas/"],
    },
    # Week 9 — Detection Engineering
    {
        "num": 27, "week": 9, "day": 0,
        "slug": "detection-engineering-reglas-deteccion",
        "title": "Detection Engineering: como construir reglas de deteccion que realmente funcionen",
        "description": "Guia practica de detection engineering: como disenar, implementar y mantener reglas de deteccion eficaces en un SOC, reducir falsos positivos y medir la calidad de las detecciones.",
        "tags": ["SOC", "Detection Engineering", "Operaciones"],
        "categories": ["SOC"],
        "keyword": "detection engineering",
        "funnel": "mofu",
        "persona": "SOC Manager",
        "h2s": [
            "Que es detection engineering?",
            "Como se disena una regla de deteccion eficaz?",
            "Que fuentes de datos son necesarias?",
            "Como reducir falsos positivos en las detecciones?",
            "Que es el Detection Maturity Model?",
            "Como medir la calidad de las detecciones?",
            "Que herramientas se usan en detection engineering?",
        ],
        "internal_links": ["/es/posts/2026/04/como-montar-soc-desde-cero/", "/es/posts/2026/04/mitre-attack-que-es-como-usarlo/"],
    },
    {
        "num": 28, "week": 9, "day": 2,
        "slug": "reglas-sigma-guia-practica",
        "title": "Reglas Sigma: guia practica para escribir detecciones portables",
        "description": "Guia completa de reglas Sigma para SOC y SIEM: sintaxis, ejemplos practicos, conversion a SIEM, integracion con MITRE ATT&CK y mejores practicas para escribir detecciones portables.",
        "tags": ["SOC", "SIEM", "Detection Engineering"],
        "categories": ["SOC"],
        "keyword": "reglas sigma",
        "funnel": "mofu",
        "persona": "SOC Manager",
        "h2s": [
            "Que son las reglas Sigma?",
            "Como se escribe una regla Sigma?",
            "Como convertir reglas Sigma a tu SIEM?",
            "Como integrar reglas Sigma con MITRE ATT&CK?",
            "Donde encontrar reglas Sigma de la comunidad?",
            "Cuales son las mejores practicas para escribir reglas Sigma?",
            "Que limitaciones tienen las reglas Sigma?",
        ],
        "internal_links": ["/es/posts/2026/04/que-es-un-siem-para-que-sirve/", "/es/posts/2026/04/mitre-attack-que-es-como-usarlo/"],
    },
    {
        "num": 29, "week": 9, "day": 4,
        "slug": "mitre-attack-soc-mapping-detecciones",
        "title": "MITRE ATT&CK en el SOC: mapping de tecnicas a detecciones reales",
        "description": "Como mapear tecnicas MITRE ATT&CK a detecciones operativas en el SOC: cobertura de la matriz, priorizar tecnicas, crear dashboards y medir gaps de deteccion en tiempo real.",
        "tags": ["MITRE", "SOC", "Detection Engineering"],
        "categories": ["SOC"],
        "keyword": "MITRE ATT&CK SOC",
        "funnel": "mofu",
        "persona": "SOC Manager",
        "h2s": [
            "Como se mapean detecciones a MITRE ATT&CK?",
            "Que tecnicas priorizar segun tu perfil de amenaza?",
            "Como crear un dashboard de cobertura ATT&CK?",
            "Como identificar gaps de deteccion?",
            "Que fuentes de telemetria necesitas por tactica?",
            "Como automatizar el mapping de detecciones?",
            "Que metricas de cobertura ATT&CK debes medir?",
        ],
        "internal_links": ["/es/posts/2026/04/mitre-attack-que-es-como-usarlo/", "/es/posts/2026/04/como-montar-soc-desde-cero/"],
    },
    # Week 10 — GRC Avanzado
    {
        "num": 30, "week": 10, "day": 0,
        "slug": "gestion-evidencias-auditorias-seguridad",
        "title": "Gestion de evidencias en auditorias de seguridad: workflow completo",
        "description": "Workflow completo para la gestion de evidencias en auditorias de seguridad: recopilacion, clasificacion, almacenamiento, trazabilidad y presentacion ante auditores externos.",
        "tags": ["GRC", "Auditoria", "Compliance"],
        "categories": ["GRC"],
        "keyword": "gestion evidencias auditoria",
        "funnel": "mofu",
        "persona": "Compliance Officer",
        "h2s": [
            "Que son las evidencias en una auditoria de seguridad?",
            "Que tipos de evidencias existen?",
            "Como recopilar evidencias de forma eficiente?",
            "Como clasificar y almacenar evidencias?",
            "Como garantizar la trazabilidad de las evidencias?",
            "Como presentar evidencias ante un auditor externo?",
            "Como automatizar la gestion de evidencias?",
        ],
        "internal_links": ["/es/posts/2026/04/auditoria-seguridad-informatica-guia/"],
    },
    {
        "num": 31, "week": 10, "day": 2,
        "slug": "medir-riesgo-ciberseguridad-fair-magerit",
        "title": "Como medir el riesgo ciber: metodologias FAIR vs MAGERIT en la practica",
        "description": "Comparativa practica de las metodologias FAIR y MAGERIT para medir el riesgo en ciberseguridad: cuando usar cada una, ventajas, limitaciones y como combinarlas.",
        "tags": ["GRC", "Riesgos", "Metodologia"],
        "categories": ["GRC"],
        "keyword": "medir riesgo ciberseguridad",
        "funnel": "mofu",
        "persona": "CISO",
        "h2s": [
            "Como se mide el riesgo en ciberseguridad?",
            "Que es la metodologia MAGERIT?",
            "Que es la metodologia FAIR?",
            "Cuales son las diferencias entre FAIR y MAGERIT?",
            "Cuando usar MAGERIT y cuando FAIR?",
            "Se pueden combinar FAIR y MAGERIT?",
            "Que herramientas soportan cada metodologia?",
        ],
        "internal_links": ["/es/posts/2026/04/analisis-riesgos-ciberseguridad-paso-a-paso/"],
    },
    {
        "num": 32, "week": 10, "day": 4,
        "slug": "plan-director-seguridad-plantilla",
        "title": "Plan director de seguridad: plantilla y guia paso a paso",
        "description": "Guia completa para elaborar un plan director de seguridad de la informacion: estructura, contenido minimo, priorizacion de proyectos, presupuesto y plantilla descargable.",
        "tags": ["GRC", "Seguridad", "Compliance"],
        "categories": ["GRC"],
        "keyword": "plan director seguridad",
        "funnel": "mofu",
        "persona": "CISO",
        "h2s": [
            "Que es un plan director de seguridad?",
            "Que contenido debe incluir un plan director?",
            "Como se elabora un plan director paso a paso?",
            "Como priorizar proyectos de seguridad?",
            "Como estimar el presupuesto del plan director?",
            "Cual es la duracion tipica de un plan director?",
            "Que errores evitar al crear un plan director?",
        ],
        "internal_links": ["/es/posts/2026/04/analisis-riesgos-ciberseguridad-paso-a-paso/", "/es/posts/2026/04/politicas-seguridad-informatica-como-crearlas/"],
    },
    # Week 11 — SOC Avanzado
    {
        "num": 33, "week": 11, "day": 0,
        "slug": "reducir-falsos-positivos-soc",
        "title": "Como reducir falsos positivos en el SOC: tecnicas reales que funcionan",
        "description": "Tecnicas probadas para reducir falsos positivos en el SOC: tuning de reglas, enrichment automatico, whitelisting inteligente, ML para clasificacion y metricas de calidad.",
        "tags": ["SOC", "Operaciones", "Detection Engineering"],
        "categories": ["SOC"],
        "keyword": "reducir falsos positivos SOC",
        "funnel": "mofu",
        "persona": "SOC Manager",
        "h2s": [
            "Por que son un problema los falsos positivos en el SOC?",
            "Cuantos falsos positivos son normales?",
            "Como hacer tuning de reglas de deteccion?",
            "Como usar enrichment automatico para reducir ruido?",
            "Que es el whitelisting inteligente?",
            "Como aplicar machine learning para clasificar alertas?",
            "Que metricas medir para evaluar la calidad de alertas?",
        ],
        "internal_links": ["/es/posts/2026/04/como-montar-soc-desde-cero/", "/es/posts/2026/04/que-es-un-siem-para-que-sirve/"],
    },
    {
        "num": 34, "week": 11, "day": 2,
        "slug": "soar-vs-siem-diferencias",
        "title": "SOAR vs SIEM: diferencias, integracion y cuando necesitas ambos",
        "description": "Comparativa detallada entre SOAR y SIEM: diferencias funcionales, cuando necesitas cada uno, como integrarlos y mejores practicas para un SOC eficiente.",
        "tags": ["SOC", "SIEM", "SOAR", "Herramientas"],
        "categories": ["SOC"],
        "keyword": "SOAR vs SIEM",
        "funnel": "mofu",
        "persona": "SOC Manager",
        "h2s": [
            "Que diferencias hay entre SOAR y SIEM?",
            "Que hace un SOAR que no hace un SIEM?",
            "Cuando necesitas un SOAR ademas del SIEM?",
            "Como se integran SOAR y SIEM?",
            "Cuales son las principales plataformas SOAR del mercado?",
            "Cuanto cuesta implementar un SOAR?",
            "Que errores evitar al implementar SOAR?",
        ],
        "internal_links": ["/es/posts/2026/04/que-es-un-siem-para-que-sirve/", "/es/posts/2026/04/como-montar-soc-desde-cero/"],
    },
    {
        "num": 35, "week": 11, "day": 4,
        "slug": "sla-ciberseguridad-mttr-mttd",
        "title": "SLAs en ciberseguridad: como definir MTTR, MTTD y no morir en la auditoria",
        "description": "Guia practica para definir SLAs de ciberseguridad: MTTR, MTTD, MTTC, benchmarks del sector, como medirlos y como presentarlos en auditorias de seguridad.",
        "tags": ["SOC", "GRC", "Operaciones"],
        "categories": ["SOC"],
        "keyword": "SLA ciberseguridad",
        "funnel": "mofu",
        "persona": "SOC Manager",
        "h2s": [
            "Que son los SLAs en ciberseguridad?",
            "Que significan MTTR, MTTD y MTTC?",
            "Cuales son los benchmarks del sector?",
            "Como definir SLAs realistas para tu SOC?",
            "Como medir y reportar SLAs de seguridad?",
            "Como presentar SLAs en una auditoria?",
            "Que pasa cuando se incumplen los SLAs?",
        ],
        "internal_links": ["/es/posts/2026/04/como-montar-soc-desde-cero/", "/es/posts/2026/04/auditoria-seguridad-informatica-guia/"],
    },
    # Week 12 — Viral + Engagement
    {
        "num": 36, "week": 12, "day": 0,
        "slug": "salario-analista-soc-espana-2026",
        "title": "Cuanto gana un analista SOC en Espana en 2026: datos reales",
        "description": "Salarios reales de analistas SOC en Espana en 2026: rangos por nivel (N1, N2, N3), por ciudad, por sector y comparativa con Europa. Datos de ofertas y encuestas del sector.",
        "tags": ["SOC", "Carreras", "Operaciones"],
        "categories": ["SOC"],
        "keyword": "salario analista SOC Espana",
        "funnel": "tofu",
        "persona": "SOC Manager",
        "h2s": [
            "Cuanto gana un analista SOC en Espana en 2026?",
            "Cual es el salario por nivel: N1, N2 y N3?",
            "Como varian los salarios por ciudad?",
            "Que sectores pagan mejor a analistas SOC?",
            "Como se compara Espana con el resto de Europa?",
            "Que factores influyen en el salario de un analista SOC?",
            "Como negociar un mejor salario en ciberseguridad?",
        ],
        "internal_links": ["/es/posts/2026/04/analista-soc-roles-n1-n2-n3/"],
    },
    {
        "num": 37, "week": 12, "day": 2,
        "slug": "incidentes-ciberseguridad-espana-graves",
        "title": "Los 10 incidentes de ciberseguridad mas graves en Espana",
        "description": "Los 10 incidentes de ciberseguridad mas importantes en Espana: ataques a hospitales, administraciones publicas, empresas criticas. Que paso, como se resolvio y que lecciones dejo cada caso.",
        "tags": ["Ciberseguridad", "Operaciones", "SOC"],
        "categories": ["SOC"],
        "keyword": "incidentes ciberseguridad Espana",
        "funnel": "tofu",
        "persona": "CISO",
        "h2s": [
            "Cuales son los incidentes de ciberseguridad mas graves en Espana?",
            "Que lecciones dejaron estos incidentes?",
            "Que sectores han sido mas atacados en Espana?",
            "Cuanto costaron estos incidentes a las organizaciones?",
            "Que medidas habrian prevenido estos incidentes?",
            "Como ha evolucionado la ciberamenaza en Espana?",
        ],
        "internal_links": ["/es/posts/2026/04/como-montar-soc-desde-cero/", "/es/posts/2026/04/threat-hunting-guia-practica/"],
    },
    {
        "num": 38, "week": 12, "day": 4,
        "slug": "multas-rgpd-espana-coste-real",
        "title": "El coste real de no cumplir con el RGPD: multas y casos reales",
        "description": "Analisis de las multas RGPD mas importantes en Espana: importes, motivos, sectores afectados y como evitarlas. Datos de la AEPD actualizados a 2026.",
        "tags": ["RGPD", "Compliance", "Seguridad"],
        "categories": ["Compliance"],
        "keyword": "multas RGPD Espana",
        "funnel": "tofu",
        "persona": "DPO",
        "h2s": [
            "Cuanto cuestan las multas RGPD en Espana?",
            "Cuales son las multas RGPD mas altas impuestas por la AEPD?",
            "Que infracciones son las mas sancionadas?",
            "Que sectores reciben mas multas RGPD?",
            "Cual es el coste total de un incumplimiento (mas alla de la multa)?",
            "Como evitar sanciones RGPD?",
        ],
        "internal_links": ["/es/posts/2026/04/politicas-seguridad-informatica-como-crearlas/"],
    },
    # Week 13 — Segunda Pillar
    {
        "num": 39, "week": 13, "day": 0,
        "slug": "guia-montar-operar-soc-2026",
        "title": "Como montar y operar un SOC en 2026: guia definitiva",
        "description": "Guia definitiva para montar y operar un SOC en 2026: modelos organizativos, equipo, herramientas, procesos, metricas, automatizacion con IA y costes reales.",
        "tags": ["SOC", "Operaciones", "Herramientas"],
        "categories": ["SOC"],
        "keyword": "montar operar SOC",
        "funnel": "mofu",
        "persona": "SOC Manager",
        "pillar": True,
        "h2s": [
            "Que es un SOC y por que es necesario en 2026?",
            "Que modelo de SOC elegir: interno, externo o hibrido?",
            "Como disenar el equipo de un SOC?",
            "Que herramientas necesita un SOC moderno?",
            "Cuales son los procesos clave de un SOC?",
            "Como medir la eficacia de un SOC?",
            "Como integrar IA y automatizacion en el SOC?",
            "Cuanto cuesta montar y operar un SOC?",
            "Tendencias en operaciones de seguridad para 2027",
        ],
        "internal_links": [
            "/es/posts/2026/04/como-montar-soc-desde-cero/",
            "/es/posts/2026/04/analista-soc-roles-n1-n2-n3/",
            "/es/posts/2026/04/que-es-un-siem-para-que-sirve/",
        ],
    },
    {
        "num": 40, "week": 13, "day": 2,
        "slug": "respuesta-incidentes-seguridad-playbook",
        "title": "Respuesta a incidentes de seguridad: playbook completo para equipos SOC",
        "description": "Playbook completo de respuesta a incidentes para SOC: fases NIST, roles, comunicacion, contencion, erradicacion, recuperacion y lecciones aprendidas con ejemplos practicos.",
        "tags": ["SOC", "Operaciones", "Seguridad"],
        "categories": ["SOC"],
        "keyword": "respuesta incidentes seguridad",
        "funnel": "mofu",
        "persona": "SOC Manager",
        "h2s": [
            "Que es un plan de respuesta a incidentes?",
            "Cuales son las fases de respuesta a incidentes segun NIST?",
            "Que roles necesita un equipo de respuesta?",
            "Como comunicar un incidente interna y externamente?",
            "Como contener y erradicar una amenaza?",
            "Como recuperar la operacion tras un incidente?",
            "Como documentar lecciones aprendidas?",
        ],
        "internal_links": ["/es/posts/2026/04/como-montar-soc-desde-cero/", "/es/posts/2026/04/threat-hunting-guia-practica/"],
    },
    {
        "num": 41, "week": 13, "day": 4,
        "slug": "threat-intelligence-empresas-empezar",
        "title": "Threat Intelligence para empresas espanolas: como empezar sin presupuesto",
        "description": "Guia practica para que empresas espanolas comiencen con threat intelligence sin presupuesto: fuentes gratuitas, herramientas open source, integracion con el SOC y maduracion del programa.",
        "tags": ["CTI", "Threat Intelligence", "Herramientas"],
        "categories": ["CTI"],
        "keyword": "threat intelligence empresas",
        "funnel": "mofu",
        "persona": "SOC Manager",
        "h2s": [
            "Que es la threat intelligence y por que la necesita tu empresa?",
            "Que fuentes de threat intelligence gratuitas existen?",
            "Que herramientas open source se usan para CTI?",
            "Como integrar threat intelligence en tu SOC?",
            "Como madurar tu programa de CTI?",
            "Que errores evitar al empezar con threat intelligence?",
            "Cuando invertir en threat intelligence de pago?",
        ],
        "internal_links": ["/es/posts/2026/04/iocs-en-ciberseguridad-que-son/", "/es/posts/2026/04/threat-hunting-guia-practica/"],
    },
    # Week 14 — BOFU
    {
        "num": 42, "week": 14, "day": 0,
        "slug": "mejores-plataformas-grc-2026",
        "title": "Mejores plataformas GRC en 2026: comparativa real para CISOs",
        "description": "Comparativa objetiva de las mejores plataformas GRC en 2026: funcionalidades, precios, integraciones, soberania de datos y para que tipo de empresa encaja cada una.",
        "tags": ["GRC", "Herramientas", "Compliance"],
        "categories": ["GRC"],
        "keyword": "mejores plataformas GRC 2026",
        "funnel": "bofu",
        "persona": "CISO",
        "h2s": [
            "Cuales son las mejores plataformas GRC en 2026?",
            "Que funcionalidades comparar entre plataformas GRC?",
            "Como se comparan en precio?",
            "Cual es mejor para empresas europeas reguladas?",
            "Que plataformas ofrecen soberania de datos en la UE?",
            "Tabla comparativa de plataformas GRC",
            "Como elegir la plataforma GRC adecuada para tu empresa?",
        ],
        "internal_links": [],
    },
    {
        "num": 43, "week": 14, "day": 2,
        "slug": "software-compliance-espana-coste",
        "title": "Software de compliance en Espana: que necesitas y cuanto cuesta",
        "description": "Guia de compra de software de compliance para empresas espanolas: tipos de herramientas, funcionalidades clave, costes reales, modelos de licencia y criterios de seleccion.",
        "tags": ["Compliance", "Herramientas", "GRC"],
        "categories": ["GRC"],
        "keyword": "software compliance Espana",
        "funnel": "bofu",
        "persona": "Compliance Officer",
        "h2s": [
            "Que software de compliance necesita una empresa espanola?",
            "Que tipos de herramientas de compliance existen?",
            "Cuanto cuesta el software de compliance?",
            "Que funcionalidades son imprescindibles?",
            "SaaS vs on-premise: que modelo elegir en Espana?",
            "Como justificar la inversion en software de compliance?",
        ],
        "internal_links": [],
    },
    {
        "num": 44, "week": 14, "day": 4,
        "slug": "roi-plataforma-grc-calcular",
        "title": "ROI de una plataforma GRC: como calcularlo y justificar la inversion",
        "description": "Como calcular el retorno de inversion de una plataforma GRC: costes evitados, ahorro operativo, reduccion de riesgo, time-to-compliance y presentacion al comite de direccion.",
        "tags": ["GRC", "Compliance", "Herramientas"],
        "categories": ["GRC"],
        "keyword": "ROI plataforma GRC",
        "funnel": "bofu",
        "persona": "CISO",
        "h2s": [
            "Cual es el ROI tipico de una plataforma GRC?",
            "Que costes evita una plataforma GRC?",
            "Como calcular el ahorro operativo?",
            "Como cuantificar la reduccion de riesgo?",
            "Que es el time-to-compliance y como mejorarlo?",
            "Como presentar el ROI al comite de direccion?",
        ],
        "internal_links": [],
    },
    # Week 15 — Compliance avanzado
    {
        "num": 45, "week": 15, "day": 0,
        "slug": "eu-ai-act-ciberseguridad",
        "title": "EU AI Act: implicaciones reales para equipos de ciberseguridad",
        "description": "Analisis del EU AI Act desde la perspectiva de ciberseguridad: clasificacion de riesgo de sistemas IA, requisitos de seguridad, impacto en SOC y compliance, y plazos de aplicacion.",
        "tags": ["IA", "Compliance", "Europa"],
        "categories": ["Compliance"],
        "keyword": "EU AI Act ciberseguridad",
        "funnel": "mofu",
        "persona": "CISO",
        "h2s": [
            "Que es el EU AI Act y cuando entra en vigor?",
            "Como clasifica el EU AI Act los sistemas de IA por riesgo?",
            "Que requisitos de seguridad impone el EU AI Act?",
            "Como afecta el AI Act a los equipos de ciberseguridad?",
            "Que relacion tiene el AI Act con el ENS y NIS2?",
            "Como prepararse para cumplir el EU AI Act?",
        ],
        "internal_links": ["/es/posts/2026/04/nis2-que-es-a-quien-afecta/"],
    },
    {
        "num": 46, "week": 15, "day": 2,
        "slug": "guia-dora-entidades-financieras-requisitos",
        "title": "Guia completa DORA para entidades financieras: 12 requisitos tecnicos",
        "description": "Desglose tecnico de los 12 requisitos principales de DORA para entidades financieras: gestion de riesgos TIC, reporting, pruebas de resiliencia, terceros y comparticion de informacion.",
        "tags": ["DORA", "Banca", "Compliance"],
        "categories": ["Compliance"],
        "keyword": "guia DORA entidades financieras",
        "funnel": "mofu",
        "persona": "CTO regulado",
        "h2s": [
            "Cuales son los 12 requisitos tecnicos de DORA?",
            "Como implementar la gestion de riesgos TIC?",
            "Que exige DORA en materia de reporting de incidentes?",
            "Que pruebas de resiliencia operativa son obligatorias?",
            "Como gestionar el riesgo de terceros proveedores TIC?",
            "Que exige DORA sobre comparticion de informacion?",
            "Que plazos tiene cada requisito?",
        ],
        "internal_links": ["/es/posts/2026/04/dora-reglamento-ciberseguridad-financiera/"],
    },
    {
        "num": 47, "week": 15, "day": 4,
        "slug": "zero-trust-guia-practica",
        "title": "Zero Trust Architecture: guia practica mas alla del buzzword",
        "description": "Guia practica de Zero Trust para empresas: principios reales, componentes tecnicos, pasos de implementacion, errores comunes y como medir la madurez de tu arquitectura Zero Trust.",
        "tags": ["Seguridad", "Operaciones", "GRC"],
        "categories": ["GRC"],
        "keyword": "zero trust guia practica",
        "funnel": "mofu",
        "persona": "CISO",
        "h2s": [
            "Que es Zero Trust y por que importa?",
            "Cuales son los principios de Zero Trust?",
            "Que componentes tecnicos necesita una arquitectura Zero Trust?",
            "Como implementar Zero Trust paso a paso?",
            "Cuales son los errores comunes al adoptar Zero Trust?",
            "Como medir la madurez Zero Trust de tu organizacion?",
            "Cuanto cuesta implementar Zero Trust?",
        ],
        "internal_links": ["/es/posts/2026/04/politicas-seguridad-informatica-como-crearlas/"],
    },
    # Week 16 — Tercera Pillar + CTI
    {
        "num": 48, "week": 16, "day": 0,
        "slug": "guia-threat-intelligence-empresas-2026",
        "title": "Threat Intelligence: guia completa para empresas 2026",
        "description": "Guia definitiva de threat intelligence para empresas en 2026: tipos, ciclo de inteligencia, fuentes, herramientas, integracion con SOC, maduracion del programa y tendencias.",
        "tags": ["CTI", "Threat Intelligence", "Herramientas"],
        "categories": ["CTI"],
        "keyword": "threat intelligence guia",
        "funnel": "mofu",
        "persona": "SOC Manager",
        "pillar": True,
        "h2s": [
            "Que es la threat intelligence?",
            "Que tipos de threat intelligence existen?",
            "Como funciona el ciclo de inteligencia de amenazas?",
            "Que fuentes de threat intelligence usar?",
            "Que herramientas necesita un programa de CTI?",
            "Como integrar CTI con el SOC?",
            "Como madurar un programa de threat intelligence?",
            "Tendencias en CTI para 2027",
        ],
        "internal_links": [
            "/es/posts/2026/04/iocs-en-ciberseguridad-que-son/",
            "/es/posts/2026/04/mitre-attack-que-es-como-usarlo/",
            "/es/posts/2026/04/threat-hunting-guia-practica/",
        ],
    },
    {
        "num": 49, "week": 16, "day": 2,
        "slug": "feeds-cti-gratuitos-mejores",
        "title": "Feeds de CTI gratuitos: los 15 mejores y como integrarlos en tu SIEM",
        "description": "Los 15 mejores feeds de threat intelligence gratuitos en 2026: MISP, AlienVault OTX, Abuse.ch, CIRCL y mas. Como integrarlos en tu SIEM y maximizar su valor operativo.",
        "tags": ["CTI", "Threat Intelligence", "SIEM", "Herramientas"],
        "categories": ["CTI"],
        "keyword": "feeds CTI gratuitos",
        "funnel": "tofu",
        "persona": "SOC Manager",
        "h2s": [
            "Cuales son los mejores feeds de CTI gratuitos?",
            "Como evaluar la calidad de un feed CTI?",
            "Como integrar feeds CTI en tu SIEM?",
            "Como evitar sobrecarga de IOCs?",
            "Que feeds recomienda ENISA y el CCN-CERT?",
            "Cuando pasar de feeds gratuitos a pagados?",
        ],
        "internal_links": ["/es/posts/2026/04/iocs-en-ciberseguridad-que-son/", "/es/posts/2026/04/que-es-un-siem-para-que-sirve/"],
    },
    {
        "num": 50, "week": 16, "day": 4,
        "slug": "dark-web-monitoring-empresa",
        "title": "Dark Web monitoring: como vigilar tu marca sin gastar una fortuna",
        "description": "Guia practica de monitorizacion de la dark web para empresas: que buscar, herramientas accesibles, fuentes OSINT, alertas automatizadas y cuando contratar un servicio profesional.",
        "tags": ["CTI", "Threat Intelligence", "OSINT"],
        "categories": ["CTI"],
        "keyword": "dark web monitoring empresa",
        "funnel": "mofu",
        "persona": "CISO",
        "h2s": [
            "Que es la monitorizacion de la dark web?",
            "Que debe buscar una empresa en la dark web?",
            "Que herramientas accesibles existen para dark web monitoring?",
            "Como configurar alertas automatizadas?",
            "Cuales son las fuentes OSINT mas utiles?",
            "Cuando contratar un servicio profesional de dark web monitoring?",
            "Que hacer cuando encuentras datos de tu empresa en la dark web?",
        ],
        "internal_links": ["/es/posts/2026/04/iocs-en-ciberseguridad-que-son/", "/es/posts/2026/04/threat-hunting-guia-practica/"],
    },
]

CTA_MAP = {
    "CISO": {
        "tofu": ('tofu', 'Riskitera evalua tu postura de seguridad y te muestra los gaps de cumplimiento en minutos.', 'Evaluar postura'),
        "mofu": ('mofu', 'Riskitera unifica GRC, SOC y CTI en una plataforma con soberania de datos europea.', None),
        "bofu": ('bofu', 'Empieza tu PoC de 90 dias con Riskitera y automatiza el compliance desde el primer dia.', 'Iniciar PoC'),
    },
    "SOC Manager": {
        "tofu": ('tofu', 'Riskitera automatiza el triage, la correlacion y el reporting de tu SOC con IA soberana.', 'Ver demo SOC'),
        "mofu": ('mofu', 'Conecta tu SIEM, EDR y feeds CTI en una plataforma que reduce los falsos positivos un 60%.', None),
        "bofu": ('bofu', 'Solicita una demo personalizada para tu SOC y descubre como Riskitera optimiza tus operaciones.', 'Solicitar demo'),
    },
    "Compliance Officer": {
        "tofu": ('tofu', 'Riskitera mapea automaticamente controles ENS, NIS2 e ISO 27001, reduciendo el esfuerzo manual un 70%.', 'Ver como'),
        "mofu": ('mofu', 'Automatiza la recopilacion de evidencias y el seguimiento de controles con Riskitera.', None),
        "bofu": ('bofu', 'Empieza tu PoC y descubre cuanto tiempo ahorras en cada ciclo de auditoria.', 'Iniciar PoC'),
    },
    "DPO": {
        "tofu": ('tofu', 'Riskitera integra la gestion RGPD con el compliance de seguridad en una sola plataforma.', 'Explorar'),
        "mofu": ('mofu', 'Gestiona evaluaciones de impacto, registro de tratamientos y derechos ARCO desde Riskitera.', None),
        "bofu": ('bofu', 'Solicita una demo enfocada en RGPD y descubre como simplificar tu cumplimiento.', 'Solicitar demo'),
    },
    "CTO regulado": {
        "tofu": ('tofu', 'Riskitera cubre los requisitos tecnicos de DORA, ENS y NIS2 con una arquitectura soberana.', 'Ver arquitectura'),
        "mofu": ('mofu', 'Integra Riskitera con tu stack actual y cumple los requisitos regulatorios de tu sector.', None),
        "bofu": ('bofu', 'Agenda una demo tecnica para tu sector y valida la integracion con tu infraestructura.', 'Agenda demo'),
    },
}


def generate_post(article):
    """Generate a complete blog post."""
    week_offset = (article["week"] - 5) * 7 + article["day"]
    publish_date = BASE_DATE + timedelta(days=week_offset)

    # Front matter
    tags_str = ", ".join(f'"{t}"' for t in article["tags"])
    cats_str = ", ".join(f'"{c}"' for c in article["categories"])
    pillar_line = "\npillar: true" if article.get("pillar") else ""

    fm = f"""---
title: "{article['title']}"
description: "{article['description']}"
slug: "{article['slug']}"
date: {publish_date.isoformat()}
publishDate: {publish_date.isoformat()}
lastmod: {publish_date.isoformat()}
draft: false
tags: [{tags_str}]
categories: [{cats_str}]
author: "Riskitera Team"
keyword: "{article['keyword']}"
funnel: "{article['funnel']}"{pillar_line}
---"""

    # Intro paragraph (GEO: direct answer in first 100 words)
    intro = article["description"]

    # CTAs
    persona = article["persona"]
    funnel = article["funnel"]
    cta_set = CTA_MAP.get(persona, CTA_MAP["CISO"])
    cta1 = cta_set.get("tofu", cta_set.get("mofu"))
    cta2 = cta_set.get("mofu" if funnel != "mofu" else "bofu", cta_set.get("bofu"))

    cta1_shortcode = f'{{{{< cta type="{cta1[0]}" text="{cta1[1]}" label="{cta1[2]}" >}}}}'
    if cta2[2]:
        cta2_shortcode = f'{{{{< cta type="{cta2[0]}" text="{cta2[1]}" label="{cta2[2]}" >}}}}'
    else:
        cta2_shortcode = f'{{{{< cta type="{cta2[0]}" text="{cta2[1]}" >}}}}'

    # Internal links
    links_section = ""
    if article.get("internal_links"):
        links_section = "\n\n**Articulos relacionados:**\n"
        for link in article["internal_links"]:
            links_section += f"- [{link.split('/')[-2].replace('-', ' ').title()}]({link})\n"

    # Build content
    h2s = article["h2s"]
    mid = len(h2s) // 2

    sections = []
    for i, h2 in enumerate(h2s):
        sections.append(f"## {h2}\n\n<!-- TODO: contenido -->\n")
        if i == mid - 1:
            sections.append(cta1_shortcode + "\n")

    body = "\n".join(sections)

    # FAQ section
    faq = """## Preguntas frecuentes

<!-- TODO: 4-5 preguntas frecuentes con respuestas concretas -->
"""

    content = f"""{fm}

{intro}

<!--more-->

{body}

{cta2_shortcode}
{links_section}
{faq}"""

    return content


def main():
    created = 0
    for article in ARTICLES:
        slug = article["slug"]
        post_dir = os.path.join(BLOG_DIR, slug)
        os.makedirs(post_dir, exist_ok=True)

        filepath = os.path.join(post_dir, "index.md")
        if os.path.exists(filepath):
            print(f"  SKIP {slug} (already exists)")
            continue

        content = generate_post(article)
        with open(filepath, "w") as f:
            f.write(content)

        print(f"  OK   {slug} (#{article['num']}, week {article['week']})")
        created += 1

    print(f"\nCreated {created} posts")


if __name__ == "__main__":
    main()
