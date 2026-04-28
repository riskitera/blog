#!/usr/bin/env python3
"""Generate local SEO posts for Spanish regions and provincial capitals."""
import os
from datetime import date, timedelta

BLOG_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "es", "posts")

# Phase 1 starts after campaign (week 17)
BASE_DATE = date(2026, 7, 27)

# --- DATA ---

CCAA = [
    {"name": "Andalucia", "slug": "andalucia", "capital": "Sevilla", "provinces": 8, "ayuntamientos": 786, "population": "8.5 millones", "sector_key": "turismo, agroalimentaria, energia renovable", "cert": "AndaluciaCERT", "ens_entities": "mas de 1.200 organismos publicos"},
    {"name": "Aragon", "slug": "aragon", "capital": "Zaragoza", "provinces": 3, "ayuntamientos": 731, "population": "1.3 millones", "sector_key": "logistica, industria, agroalimentaria", "cert": "CSIRT.es", "ens_entities": "mas de 400 organismos publicos"},
    {"name": "Asturias", "slug": "asturias", "capital": "Oviedo", "provinces": 1, "ayuntamientos": 78, "population": "1 millon", "sector_key": "industria, energia, sanidad publica", "cert": "CSIRT.es", "ens_entities": "mas de 150 organismos publicos"},
    {"name": "Islas Baleares", "slug": "islas-baleares", "capital": "Palma de Mallorca", "provinces": 1, "ayuntamientos": 67, "population": "1.2 millones", "sector_key": "turismo, transporte, sanidad", "cert": "CSIRT.es", "ens_entities": "mas de 100 organismos publicos"},
    {"name": "Canarias", "slug": "canarias", "capital": "Las Palmas / Santa Cruz de Tenerife", "provinces": 2, "ayuntamientos": 88, "population": "2.2 millones", "sector_key": "turismo, energia, portuaria", "cert": "CSIRT.es", "ens_entities": "mas de 200 organismos publicos"},
    {"name": "Cantabria", "slug": "cantabria", "capital": "Santander", "provinces": 1, "ayuntamientos": 102, "population": "580.000", "sector_key": "industria, sanidad, educacion", "cert": "CSIRT.es", "ens_entities": "mas de 120 organismos publicos"},
    {"name": "Castilla-La Mancha", "slug": "castilla-la-mancha", "capital": "Toledo", "provinces": 5, "ayuntamientos": 919, "population": "2.1 millones", "sector_key": "energia renovable, agroalimentaria, administracion", "cert": "CSIRT.es", "ens_entities": "mas de 950 organismos publicos"},
    {"name": "Castilla y Leon", "slug": "castilla-y-leon", "capital": "Valladolid", "provinces": 9, "ayuntamientos": 2248, "population": "2.4 millones", "sector_key": "agroalimentaria, industria, educacion", "cert": "CSIRT.es", "ens_entities": "mas de 2.300 organismos publicos"},
    {"name": "Cataluna", "slug": "cataluna", "capital": "Barcelona", "provinces": 4, "ayuntamientos": 947, "population": "7.8 millones", "sector_key": "industria, biotecnologia, servicios financieros, turismo", "cert": "CESICAT", "ens_entities": "mas de 1.000 organismos publicos"},
    {"name": "Comunidad Valenciana", "slug": "comunidad-valenciana", "capital": "Valencia", "provinces": 3, "ayuntamientos": 542, "population": "5.1 millones", "sector_key": "turismo, ceramica, agroalimentaria, portuaria", "cert": "CSIRT-CV", "ens_entities": "mas de 600 organismos publicos"},
    {"name": "Extremadura", "slug": "extremadura", "capital": "Merida", "provinces": 2, "ayuntamientos": 388, "population": "1.1 millones", "sector_key": "agroalimentaria, energia, administracion publica", "cert": "CSIRT.es", "ens_entities": "mas de 400 organismos publicos"},
    {"name": "Galicia", "slug": "galicia", "capital": "Santiago de Compostela", "provinces": 4, "ayuntamientos": 313, "population": "2.7 millones", "sector_key": "pesca, automocion, textil, sanidad", "cert": "CSIRT.gal", "ens_entities": "mas de 350 organismos publicos"},
    {"name": "Comunidad de Madrid", "slug": "comunidad-de-madrid", "capital": "Madrid", "provinces": 1, "ayuntamientos": 179, "population": "6.8 millones", "sector_key": "servicios financieros, tecnologia, administracion central, sanidad", "cert": "Madrid CSIRT", "ens_entities": "mas de 500 organismos publicos"},
    {"name": "Region de Murcia", "slug": "region-de-murcia", "capital": "Murcia", "provinces": 1, "ayuntamientos": 45, "population": "1.5 millones", "sector_key": "agroalimentaria, turismo, logistica", "cert": "CSIRT.es", "ens_entities": "mas de 100 organismos publicos"},
    {"name": "Navarra", "slug": "navarra", "capital": "Pamplona", "provinces": 1, "ayuntamientos": 272, "population": "660.000", "sector_key": "industria, energia renovable, automocion", "cert": "Navarra CSIRT", "ens_entities": "mas de 300 organismos publicos"},
    {"name": "Pais Vasco", "slug": "pais-vasco", "capital": "Vitoria-Gasteiz", "provinces": 3, "ayuntamientos": 251, "population": "2.2 millones", "sector_key": "industria, energia, servicios financieros, tecnologia", "cert": "Basque Cybersecurity Centre", "ens_entities": "mas de 300 organismos publicos"},
    {"name": "La Rioja", "slug": "la-rioja", "capital": "Logrono", "provinces": 1, "ayuntamientos": 174, "population": "320.000", "sector_key": "agroalimentaria, vitivinicola, turismo", "cert": "CSIRT.es", "ens_entities": "mas de 180 organismos publicos"},
    {"name": "Ceuta", "slug": "ceuta", "capital": "Ceuta", "provinces": 0, "ayuntamientos": 1, "population": "84.000", "sector_key": "administracion, logistica fronteriza, seguridad", "cert": "CSIRT.es", "ens_entities": "organismos de la ciudad autonoma"},
    {"name": "Melilla", "slug": "melilla", "capital": "Melilla", "provinces": 0, "ayuntamientos": 1, "population": "87.000", "sector_key": "administracion, logistica fronteriza, comercio", "cert": "CSIRT.es", "ens_entities": "organismos de la ciudad autonoma"},
]

CAPITALS = [
    {"name": "Madrid", "slug": "madrid", "ccaa": "Comunidad de Madrid", "population": "3.3 millones", "sector": "financiero, tecnologia, administracion central"},
    {"name": "Barcelona", "slug": "barcelona", "ccaa": "Cataluna", "population": "1.6 millones", "sector": "industria, biotecnologia, turismo, tecnologia"},
    {"name": "Valencia", "slug": "valencia", "ccaa": "Comunidad Valenciana", "population": "800.000", "sector": "portuaria, turismo, agroalimentaria"},
    {"name": "Sevilla", "slug": "sevilla", "ccaa": "Andalucia", "population": "690.000", "sector": "turismo, aeronautica, administracion autonomica"},
    {"name": "Zaragoza", "slug": "zaragoza", "ccaa": "Aragon", "population": "680.000", "sector": "logistica, automocion, industria"},
    {"name": "Malaga", "slug": "malaga", "ccaa": "Andalucia", "population": "580.000", "sector": "tecnologia, turismo, ciberseguridad"},
    {"name": "Murcia", "slug": "murcia", "ccaa": "Region de Murcia", "population": "460.000", "sector": "agroalimentaria, logistica"},
    {"name": "Palma de Mallorca", "slug": "palma-de-mallorca", "ccaa": "Islas Baleares", "population": "420.000", "sector": "turismo, transporte, sanidad"},
    {"name": "Las Palmas de Gran Canaria", "slug": "las-palmas", "ccaa": "Canarias", "population": "380.000", "sector": "turismo, portuaria, energia"},
    {"name": "Bilbao", "slug": "bilbao", "ccaa": "Pais Vasco", "population": "350.000", "sector": "industria, financiero, tecnologia"},
    {"name": "Alicante", "slug": "alicante", "ccaa": "Comunidad Valenciana", "population": "340.000", "sector": "turismo, calzado, tecnologia"},
    {"name": "Cordoba", "slug": "cordoba", "ccaa": "Andalucia", "population": "325.000", "sector": "agroalimentaria, turismo, joyeria"},
    {"name": "Valladolid", "slug": "valladolid", "ccaa": "Castilla y Leon", "population": "300.000", "sector": "automocion, administracion autonomica"},
    {"name": "Vigo", "slug": "vigo", "ccaa": "Galicia", "population": "295.000", "sector": "automocion, pesca, naval"},
    {"name": "Gijon", "slug": "gijon", "ccaa": "Asturias", "population": "270.000", "sector": "industria, portuaria, tecnologia"},
    {"name": "Vitoria-Gasteiz", "slug": "vitoria-gasteiz", "ccaa": "Pais Vasco", "population": "255.000", "sector": "industria, administracion autonomica"},
    {"name": "A Coruna", "slug": "a-coruna", "ccaa": "Galicia", "population": "245.000", "sector": "textil, portuaria, tecnologia"},
    {"name": "Granada", "slug": "granada", "ccaa": "Andalucia", "population": "230.000", "sector": "turismo, universidad, tecnologia"},
    {"name": "Oviedo", "slug": "oviedo", "ccaa": "Asturias", "population": "220.000", "sector": "administracion, sanidad, educacion"},
    {"name": "Santa Cruz de Tenerife", "slug": "santa-cruz-tenerife", "ccaa": "Canarias", "population": "210.000", "sector": "turismo, portuaria, administracion"},
    {"name": "Pamplona", "slug": "pamplona", "ccaa": "Navarra", "population": "205.000", "sector": "industria, automocion, energia renovable"},
    {"name": "Santander", "slug": "santander", "ccaa": "Cantabria", "population": "175.000", "sector": "financiero, turismo, educacion"},
    {"name": "Almeria", "slug": "almeria", "ccaa": "Andalucia", "population": "200.000", "sector": "agroalimentaria, portuaria, energia solar"},
    {"name": "San Sebastian", "slug": "san-sebastian", "ccaa": "Pais Vasco", "population": "190.000", "sector": "tecnologia, turismo, industria"},
    {"name": "Burgos", "slug": "burgos", "ccaa": "Castilla y Leon", "population": "180.000", "sector": "industria, agroalimentaria"},
    {"name": "Salamanca", "slug": "salamanca", "ccaa": "Castilla y Leon", "population": "145.000", "sector": "educacion, turismo, administracion"},
    {"name": "Logrono", "slug": "logrono", "ccaa": "La Rioja", "population": "150.000", "sector": "vitivinicola, agroalimentaria"},
    {"name": "Huelva", "slug": "huelva", "ccaa": "Andalucia", "population": "145.000", "sector": "quimica, agroalimentaria, portuaria"},
    {"name": "Tarragona", "slug": "tarragona", "ccaa": "Cataluna", "population": "135.000", "sector": "petroquimica, turismo, portuaria"},
    {"name": "Lleida", "slug": "lleida", "ccaa": "Cataluna", "population": "140.000", "sector": "agroalimentaria, energia"},
    {"name": "Jaen", "slug": "jaen", "ccaa": "Andalucia", "population": "112.000", "sector": "olivar, agroalimentaria"},
    {"name": "Ourense", "slug": "ourense", "ccaa": "Galicia", "population": "105.000", "sector": "termal, agroalimentaria"},
    {"name": "Girona", "slug": "girona", "ccaa": "Cataluna", "population": "103.000", "sector": "turismo, agroalimentaria"},
    {"name": "Lugo", "slug": "lugo", "ccaa": "Galicia", "population": "98.000", "sector": "agroalimentaria, madera"},
    {"name": "Cadiz", "slug": "cadiz", "ccaa": "Andalucia", "population": "116.000", "sector": "naval, turismo, aeronautica"},
    {"name": "Leon", "slug": "leon", "ccaa": "Castilla y Leon", "population": "125.000", "sector": "energia, mineria, turismo"},
    {"name": "Badajoz", "slug": "badajoz", "ccaa": "Extremadura", "population": "150.000", "sector": "agroalimentaria, energia, administracion"},
    {"name": "Caceres", "slug": "caceres", "ccaa": "Extremadura", "population": "96.000", "sector": "turismo, administracion"},
    {"name": "Albacete", "slug": "albacete", "ccaa": "Castilla-La Mancha", "population": "174.000", "sector": "agroalimentaria, cuchilleria, energia"},
    {"name": "Ciudad Real", "slug": "ciudad-real", "ccaa": "Castilla-La Mancha", "population": "75.000", "sector": "vitivinicola, energia renovable"},
    {"name": "Cuenca", "slug": "cuenca", "ccaa": "Castilla-La Mancha", "population": "55.000", "sector": "turismo, madera"},
    {"name": "Guadalajara", "slug": "guadalajara", "ccaa": "Castilla-La Mancha", "population": "87.000", "sector": "logistica, industria"},
    {"name": "Toledo", "slug": "toledo", "ccaa": "Castilla-La Mancha", "population": "85.000", "sector": "turismo, administracion autonomica"},
    {"name": "Palencia", "slug": "palencia", "ccaa": "Castilla y Leon", "population": "78.000", "sector": "automocion, agroalimentaria"},
    {"name": "Zamora", "slug": "zamora", "ccaa": "Castilla y Leon", "population": "62.000", "sector": "agroalimentaria, energia"},
    {"name": "Segovia", "slug": "segovia", "ccaa": "Castilla y Leon", "population": "52.000", "sector": "turismo, agroalimentaria"},
    {"name": "Avila", "slug": "avila", "ccaa": "Castilla y Leon", "population": "57.000", "sector": "turismo, agroalimentaria"},
    {"name": "Soria", "slug": "soria", "ccaa": "Castilla y Leon", "population": "39.000", "sector": "agroalimentaria, madera"},
    {"name": "Teruel", "slug": "teruel", "ccaa": "Aragon", "population": "36.000", "sector": "turismo, mineria, agroalimentaria"},
    {"name": "Huesca", "slug": "huesca", "ccaa": "Aragon", "population": "53.000", "sector": "turismo, agroalimentaria, energia"},
]


def generate_ccaa_post(ccaa, index):
    """Generate a CCAA-level local SEO post."""
    pub_date = BASE_DATE + timedelta(days=index * 2)
    slug = f"ciberseguridad-administracion-publica-{ccaa['slug']}"

    content = f"""---
title: "Ciberseguridad para la administracion publica en {ccaa['name']}: ENS, NIS2 y cumplimiento obligatorio"
description: "Guia de ciberseguridad para ayuntamientos y organismos publicos de {ccaa['name']}: requisitos ENS, NIS2, plazos, herramientas del CCN y como cumplir la normativa de seguridad obligatoria."
slug: "{slug}"
date: {pub_date.isoformat()}
publishDate: {pub_date.isoformat()}
lastmod: {pub_date.isoformat()}
draft: false
tags: ["ENS", "Administracion Publica", "NIS2", "{ccaa['name']}"]
categories: ["Compliance"]
author: "Riskitera Team"
keyword: "ciberseguridad administracion publica {ccaa['name']}"
funnel: "mofu"
geo_target: "{ccaa['name']}"
---

La administracion publica de {ccaa['name']} gestiona {ccaa['ens_entities']} que deben cumplir el Esquema Nacional de Seguridad (ENS). Con una poblacion de {ccaa['population']} de habitantes y sectores criticos como {ccaa['sector_key']}, la ciberseguridad no es opcional: es una obligacion legal recogida en el Real Decreto 311/2022. En esta guia detallamos los requisitos, plazos y pasos concretos para que los organismos publicos de {ccaa['name']} cumplan con el ENS y se preparen para NIS2.

<!--more-->

## Que obligaciones de ciberseguridad tiene la administracion publica en {ccaa['name']}?

Todos los organismos publicos de {ccaa['name']}, incluyendo el Gobierno autonomico, los {ccaa['ayuntamientos']} ayuntamientos, las diputaciones provinciales, las entidades de derecho publico y las empresas publicas que gestionen sistemas de informacion, estan obligados a cumplir el ENS. Esto incluye tanto los sistemas que gestionan datos de ciudadanos como los que soportan servicios publicos digitales.

El Real Decreto 311/2022 establece que todas las administraciones publicas deben categorizar sus sistemas, implementar las medidas de seguridad correspondientes y someterse a auditorias periodicas. Para los organismos de {ccaa['name']}, esto implica adaptar sus infraestructuras tecnologicas a los requisitos del ENS segun el nivel de seguridad (alto, medio o bajo) que corresponda a cada sistema.

## Que nivel ENS necesitan los ayuntamientos de {ccaa['name']}?

La mayoria de los ayuntamientos de {ccaa['name']} necesitan al menos un nivel ENS medio para sus sistemas principales (padron, sede electronica, gestion tributaria). Los ayuntamientos de mayor tamano o los que gestionan datos sensibles (servicios sociales, policia local) pueden requerir nivel ENS alto.

La categorizacion depende del impacto que un incidente de seguridad tendria sobre los servicios publicos y los ciudadanos. El CCN proporciona la herramienta PILAR para realizar esta categorizacion de forma sistematica.

## Como afecta NIS2 a los organismos publicos de {ccaa['name']}?

La Directiva NIS2, que Espana esta transponiendo a su legislacion nacional, amplia las obligaciones de ciberseguridad a las administraciones publicas. Los organismos de {ccaa['name']} que gestionen servicios esenciales (sanidad, transporte, agua, energia) estaran directamente afectados.

NIS2 exige gestion de riesgos, notificacion de incidentes en menos de 24 horas y gobernanza de la ciberseguridad a nivel de direccion. Esto complementa y refuerza las obligaciones del ENS.

## Que recursos tiene {ccaa['name']} para la ciberseguridad publica?

{ccaa['name']} cuenta con {ccaa['cert']} como referencia para la gestion de incidentes de seguridad. Ademas, el CCN-CERT proporciona a todos los organismos publicos espanoles acceso a herramientas como PILAR (analisis de riesgos), INES (estado de cumplimiento del ENS), LUCIA (gestion de ciberincidentes) y microCLAUDIA (proteccion de endpoints).

Estas herramientas son gratuitas para la administracion publica y permiten a los organismos de {ccaa['name']} avanzar en el cumplimiento del ENS sin necesidad de grandes inversiones en software.

## Cuales son los principales riesgos de ciberseguridad en {ccaa['name']}?

Los sectores de {ccaa['sector_key']} que caracterizan la economia de {ccaa['name']} presentan riesgos especificos. Los ataques de ransomware a ayuntamientos espanoles han crecido un 35% entre 2024 y 2025 segun datos del CCN-CERT. Los organismos publicos de {ccaa['name']} son objetivo por la cantidad de datos personales que gestionan y, en muchos casos, por la falta de recursos dedicados a ciberseguridad.

Los incidentes mas frecuentes en administraciones publicas incluyen: phishing dirigido a empleados publicos, ransomware contra servidores de gestion, y exfiltracion de datos del padron o servicios sociales.

## Como empezar a cumplir el ENS en un ayuntamiento de {ccaa['name']}?

1. **Inventariar los sistemas de informacion** que gestiona el ayuntamiento
2. **Categorizar cada sistema** segun el impacto de un incidente (usar PILAR)
3. **Realizar un analisis de riesgos** sobre los sistemas categorizados
4. **Implementar las medidas de seguridad** correspondientes al nivel asignado
5. **Aprobar la politica de seguridad** por el pleno del ayuntamiento
6. **Designar un responsable de seguridad** con formacion adecuada
7. **Realizar la auditoria** de cumplimiento (bienal para nivel medio y alto)
8. **Reportar el estado de cumplimiento** a traves de la plataforma INES del CCN

{{{{< cta type="mofu" text="Riskitera automatiza el cumplimiento ENS para administraciones publicas: categorizacion, analisis de riesgos, seguimiento de controles y generacion de informes para auditoria." label="Ver demo para AA.PP." >}}}}

## Preguntas frecuentes

### Es obligatorio el ENS para todos los ayuntamientos de {ccaa['name']}?

Si. El ENS es obligatorio para todas las administraciones publicas espanolas, independientemente de su tamano. Esto incluye a los {ccaa['ayuntamientos']} ayuntamientos de {ccaa['name']}, asi como a sus organismos autonomos y empresas publicas que gestionen sistemas de informacion.

### Cuanto cuesta cumplir el ENS en un ayuntamiento?

El coste depende del tamano del ayuntamiento y del nivel de seguridad requerido. Para un ayuntamiento mediano de {ccaa['name']}, el coste total (consultoria, implementacion y auditoria) oscila entre 15.000 y 50.000 euros para nivel medio. Las herramientas del CCN (PILAR, INES, LUCIA) son gratuitas para la administracion publica, lo que reduce significativamente el coste.

### Que plazo tienen los ayuntamientos para cumplir NIS2?

La transposicion de NIS2 a la legislacion espanola se espera completada en 2026. Los organismos publicos que gestionen servicios esenciales tendran un periodo de adaptacion, pero la recomendacion del CCN es comenzar la preparacion de forma inmediata, ya que muchos de los requisitos de NIS2 coinciden con los del ENS.

**Articulos relacionados:**
- [Que es el Esquema Nacional de Seguridad (ENS)](/es/posts/2026/04/que-es-esquema-nacional-seguridad-ens/)
- [NIS2: que es, a quien afecta y plazos](/es/posts/2026/04/nis2-que-es-a-quien-afecta/)
- [ENS en la administracion publica](/es/posts/2026/05/ens-administracion-publica/)
"""
    return slug, content


def generate_capital_post(capital, index):
    """Generate a capital city local SEO post."""
    pub_date = BASE_DATE + timedelta(days=38 + index)  # Start after CCAA posts
    slug = f"ciberseguridad-ayuntamiento-{capital['slug']}"

    content = f"""---
title: "Ciberseguridad para el Ayuntamiento de {capital['name']}: cumplir ENS y NIS2"
description: "Guia de cumplimiento ENS y NIS2 para el Ayuntamiento de {capital['name']} y organismos publicos de la ciudad: requisitos, plazos, herramientas CCN y pasos para la certificacion."
slug: "{slug}"
date: {pub_date.isoformat()}
publishDate: {pub_date.isoformat()}
lastmod: {pub_date.isoformat()}
draft: false
tags: ["ENS", "Administracion Publica", "NIS2", "{capital['name']}"]
categories: ["Compliance"]
author: "Riskitera Team"
keyword: "ciberseguridad ayuntamiento {capital['name']}"
funnel: "mofu"
geo_target: "{capital['name']}"
---

El Ayuntamiento de {capital['name']}, con una poblacion de {capital['population']} de habitantes, esta obligado a cumplir el Esquema Nacional de Seguridad (ENS) en todos sus sistemas de informacion. Como capital de {capital['ccaa']}, gestiona servicios publicos digitales criticos para los ciudadanos: padron municipal, sede electronica, gestion tributaria, servicios sociales y policia local. El cumplimiento del ENS y la preparacion para NIS2 no son opcionales: son obligaciones legales que afectan a la continuidad de estos servicios.

<!--more-->

## Que requisitos de ciberseguridad debe cumplir el Ayuntamiento de {capital['name']}?

El Ayuntamiento de {capital['name']} debe cumplir el ENS (Real Decreto 311/2022) en todos los sistemas que soporten servicios publicos electronicos. Dada la poblacion de {capital['population']} y los sectores economicos de la ciudad ({capital['sector']}), la mayoria de sus sistemas criticos requeriran nivel ENS medio o alto.

Ademas, con la transposicion de NIS2, los servicios esenciales del municipio (abastecimiento de agua, transporte publico, gestion de residuos) quedaran sujetos a requisitos adicionales de gestion de riesgos y notificacion de incidentes.

## Que nivel ENS necesita el Ayuntamiento de {capital['name']}?

Los sistemas criticos del Ayuntamiento de {capital['name']} (padron, sede electronica, gestion tributaria, policia local) requieren como minimo nivel ENS medio. Los sistemas que gestionen datos especialmente sensibles (servicios sociales, datos de menores, policia local) deben categorizarse como nivel alto.

La categorizacion debe realizarse sistema por sistema, evaluando el impacto de un incidente de seguridad sobre la confidencialidad, integridad, disponibilidad, autenticidad y trazabilidad de la informacion.

## Como puede el Ayuntamiento de {capital['name']} empezar a cumplir el ENS?

1. **Designar un responsable de seguridad** con dedicacion y formacion
2. **Inventariar todos los sistemas** de informacion municipales
3. **Categorizar cada sistema** con la herramienta PILAR del CCN
4. **Realizar el analisis de riesgos** segun la metodologia MAGERIT
5. **Implementar las medidas de seguridad** exigidas por el nivel asignado
6. **Aprobar la politica de seguridad municipal** por el pleno
7. **Someterse a auditoria** de cumplimiento ENS
8. **Mantener el cumplimiento continuo** con revisiones periodicas

## Que herramientas gratuitas del CCN puede usar el Ayuntamiento de {capital['name']}?

El CCN-CERT pone a disposicion de todas las administraciones publicas herramientas gratuitas: PILAR para el analisis de riesgos, INES para reportar el estado de cumplimiento del ENS, LUCIA para la gestion de ciberincidentes, microCLAUDIA para la proteccion de endpoints y REYES para la gestion de ciberinteligencia.

## Que impacto tiene un ciberataque en un ayuntamiento como {capital['name']}?

Un ciberataque al Ayuntamiento de {capital['name']} afectaria directamente a {capital['population']} de ciudadanos. Los servicios de padron, gestion tributaria, sede electronica y servicios sociales quedarian interrumpidos. Segun el CCN-CERT, el tiempo medio de recuperacion de un ayuntamiento espanol tras un ataque de ransomware es de 23 dias, con un coste directo que puede superar los 200.000 euros.

{{{{< cta type="mofu" text="Riskitera ayuda a ayuntamientos a cumplir el ENS de forma continua: categorizacion automatica, seguimiento de controles y preparacion para auditoria." label="Ver demo para ayuntamientos" >}}}}

## Preguntas frecuentes

### Cuanto cuesta al Ayuntamiento de {capital['name']} cumplir el ENS?

El coste depende del numero de sistemas y del nivel de seguridad requerido. Para un ayuntamiento del tamano de {capital['name']}, el presupuesto total (consultoria, implementacion y auditoria) oscila entre 30.000 y 100.000 euros para nivel medio-alto. Las herramientas del CCN son gratuitas.

### Puede el Ayuntamiento de {capital['name']} externalizar el cumplimiento del ENS?

Si. Muchos ayuntamientos trabajan con empresas especializadas en ciberseguridad que ayudan en la implementacion y el mantenimiento del ENS. Lo que no puede externalizarse es la responsabilidad: el responsable de seguridad del ayuntamiento sigue siendo el ultimo responsable del cumplimiento.

### Como afecta NIS2 al Ayuntamiento de {capital['name']}?

NIS2 amplia las obligaciones de ciberseguridad a los servicios municipales esenciales. El Ayuntamiento de {capital['name']} debera notificar incidentes significativos en menos de 24 horas, implementar gestion de riesgos a nivel de direccion y garantizar la seguridad de su cadena de suministro TIC.

**Articulos relacionados:**
- [Que es el ENS](/es/posts/2026/04/que-es-esquema-nacional-seguridad-ens/)
- [NIS2: que es y a quien afecta](/es/posts/2026/04/nis2-que-es-a-quien-afecta/)
- [Ciberseguridad en {capital['ccaa']}](/es/posts/ciberseguridad-administracion-publica-{capital['ccaa'].lower().replace(' ', '-').replace('í', 'i').replace('ó', 'o').replace('á', 'a').replace('ú', 'u').replace('ñ', 'n')}/)
"""
    return slug, content


def main():
    created = 0

    # Phase 1: CCAA
    print("=== FASE 1: Comunidades Autonomas ===")
    for i, ccaa in enumerate(CCAA):
        slug, content = generate_ccaa_post(ccaa, i)
        post_dir = os.path.join(BLOG_DIR, slug)
        os.makedirs(post_dir, exist_ok=True)
        filepath = os.path.join(post_dir, "index.md")
        if os.path.exists(filepath):
            print(f"  SKIP {slug}")
            continue
        with open(filepath, "w") as f:
            f.write(content)
        print(f"  OK   {slug}")
        created += 1

    # Phase 2: Capitals
    print("\n=== FASE 2: Capitales de provincia ===")
    for i, capital in enumerate(CAPITALS):
        slug, content = generate_capital_post(capital, i)
        post_dir = os.path.join(BLOG_DIR, slug)
        os.makedirs(post_dir, exist_ok=True)
        filepath = os.path.join(post_dir, "index.md")
        if os.path.exists(filepath):
            print(f"  SKIP {slug}")
            continue
        with open(filepath, "w") as f:
            f.write(content)
        print(f"  OK   {slug}")
        created += 1

    print(f"\nCreated {created} local SEO posts")


if __name__ == "__main__":
    main()
