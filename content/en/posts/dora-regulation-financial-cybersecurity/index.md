---
title: "DORA: The Regulation Reshaping Financial Cybersecurity in Europe"
image: "cover.png"
description: "A complete guide to the DORA Regulation: what it is, who it affects, the five pillars of digital operational resilience, deadlines, penalties, and how to prepare for compliance."
slug: "dora-regulation-financial-cybersecurity"
date: 2026-03-10
lastmod: 2026-03-10
draft: false
index: true
tags: ["DORA", "Fintech", "Compliance"]
categories: ["Compliance"]
author: "David Moya"
translationKey: "dora-guide"
---

The Digital Operational Resilience Act (DORA) is the EU regulation that sets a uniform framework for digital operational resilience across the financial sector. Directly applicable in all Member States since January 17, 2025, it affects over 22,000 financial entities and ICT service providers in Europe. Non-compliance can result in penalties reaching 1 percent of average daily global turnover, per day.

<!--more-->

{{< key-takeaways >}}
- DORA is lex specialis with respect to NIS2 for the European financial sector
- It applies to financial entities and their critical ICT service providers
- Five pillars: ICT risk management, incident reporting, resilience testing, third-party management, and information sharing
- Penalties: up to EUR 10 million or 5% of turnover for financial entities
- Organizations already compliant with ISO 27001 or ENS have a head start
{{< /key-takeaways >}}

## What is DORA and why does it exist?

[DORA](https://eur-lex.europa.eu/eli/reg/2022/2554) (Regulation (EU) 2022/2554) was adopted on December 14, 2022, and became applicable on January 17, 2025. It was born from a clear observation: the European financial sector depends critically on information and communication technologies (ICT), yet there was no harmonized framework ensuring the digital operational resilience of financial entities against severe disruptions.

Before DORA, each Member State and sectoral regulator addressed financial cybersecurity in a fragmented manner. The European Central Bank (ECB) issued guidelines for banking, the European Securities and Markets Authority (ESMA) for capital markets, and the European Insurance and Occupational Pensions Authority (EIOPA) for the insurance sector. The result was a patchwork of disparate requirements that made both compliance and supervision difficult.

According to ECB data, cyber incidents reported by significant European financial entities increased by 72 percent between 2020 and 2024. The attack on the ION Trading Technologies platform in January 2023, which disrupted derivatives trading across Europe, was one of the incidents that accelerated DORA's final adoption.

## Which financial entities does DORA affect?

DORA's scope within the financial sector is extraordinarily broad. It covers 21 categories of entities:

### Financial entities

- **Credit institutions** (banks).
- **Investment firms**.
- **Management companies of collective investment undertakings** (fund managers).
- **Insurance and reinsurance undertakings**.
- **Institutions for occupational retirement provision**.
- **Electronic money institutions**.
- **Payment institutions**.
- **Crypto-asset service providers** (covered under MiCA).
- **Central securities depositories**.
- **Central counterparties**.
- **Trading venues** (stock exchanges, multilateral trading facilities).
- **Trade repositories**.
- **Credit rating agencies**.
- **Data reporting service providers**.
- **Benchmark administrators**.
- **Crowdfunding service providers**.

### Third-party ICT service providers

One of DORA's most significant innovations is the direct inclusion of critical third-party ICT service providers. This covers cloud service providers, data centers, software companies, managed service providers (MSPs), managed security service providers (MSSPs), and any other ICT service provider deemed critical to the operations of financial entities.

Critical ICT providers will be designated by the European Supervisory Authorities (ESAs) and will be subject to a direct supervision framework by a lead European overseer. This represents a radical shift: for the first time, technology companies that are not financial entities will be subject to direct regulatory supervision in a financial context.

### Exemptions and proportionality

DORA applies the principle of proportionality: financial microenterprises (fewer than 10 employees and less than 2 million euros in turnover) have simplified obligations. Certain minor entities such as small insurance intermediaries are exempt. However, the exemption is narrow and the vast majority of financial sector entities are obligated.

## What are the five pillars of DORA?

DORA is structured around five core areas that together define a comprehensive digital operational resilience framework.

### Pillar 1: ICT risk management

Financial entities must establish a robust and comprehensive ICT risk management framework that includes:

- **Governance**: the management body is directly responsible for defining, approving, overseeing, and bearing ultimate accountability for the implementation of the ICT risk management framework. Board members must receive regular ICT risk training.
- **Asset and risk identification**: a complete inventory of information assets, ICT systems, business functions, and their interdependencies. Continuous assessment of threats and vulnerabilities.
- **Protection and prevention**: implementation of security policies, access control mechanisms, encryption, patch management, and network protection.
- **Detection**: continuous monitoring and anomalous activity detection capabilities, with multiple layers of control.
- **Response and recovery**: incident response plans, business continuity plans, and disaster recovery procedures, with clear recovery time objectives (RTO) and recovery point objectives (RPO).
- **Learning and evolution**: post-incident review, incorporation of lessons learned, and continuous improvement of the framework.

### Pillar 2: ICT-related incident reporting

DORA establishes a harmonized incident classification and reporting process:

- **Classification**: entities must classify ICT incidents according to defined criteria: number of affected clients, duration, geographic extent, economic impact, data loss, and criticality of affected services.
- **Initial notification**: within 4 hours of classifying the incident as major (and no later than 24 hours after detection).
- **Intermediate report**: within 72 hours, with updates on incident management.
- **Final report**: within one month, with a root cause analysis and measures taken.

Notifications are directed to the relevant national competent authority. In Spain, this will be the Bank of Spain, the CNMV, or the Directorate General for Insurance and Pension Funds, depending on the type of entity.

### Pillar 3: Digital operational resilience testing

DORA requires a rigorous and periodic testing program:

- **Basic testing** (for all entities): vulnerability assessments, open-source software analysis, network security evaluations, gap analyses, physical security reviews, scenario testing, and compatibility testing.
- **Advanced threat-led penetration testing (TLPT)**: mandatory every three years for entities meeting certain size and criticality criteria. These tests, based on the TIBER-EU framework, simulate realistic attacks against the entity's critical systems. They must be carried out by qualified independent external auditors.

Entities must document all tests, their results, and the corrective actions taken.

### Pillar 4: ICT third-party risk management

This pillar addresses the financial sector's critical dependency on technology providers:

- **Pre-engagement assessment**: before contracting an ICT provider, the entity must conduct a thorough risk analysis, including provider concentration and subcontracting risks.
- **Contractual requirements**: DORA establishes mandatory minimum clauses that must be included in contracts with ICT providers, covering service levels, security measures, incident notification obligations, access and audit rights, exit strategies, and transition plans.
- **Provider register**: entities must maintain an up-to-date register of all their ICT providers, classified by criticality.
- **Critical provider oversight**: ICT providers designated as critical will be subject to direct supervision by the ESAs, which may conduct inspections, request information, and issue binding recommendations.

### Pillar 5: Information sharing

DORA encourages voluntary sharing of cyber threat information among financial entities:

- Entities may establish arrangements to share indicators of compromise (IoCs), tactics, techniques, and procedures (TTPs), and security alerts.
- Sharing must comply with data protection and competition regulations.
- Supervisory authorities will facilitate and promote these exchanges, recognizing that cybersecurity is a collective challenge.

## How does DORA relate to NIS2 and other regulations?

DORA and NIS2 were adopted on the same day and were designed to complement each other:

- **DORA is lex specialis**: for financial entities, DORA takes precedence over [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555) in the areas it regulates. This means that if a financial entity is subject to DORA, it must comply with DORA rather than NIS2 for ICT risk management, incident reporting, and resilience testing requirements. For a detailed look at [NIS2 requirements](/en/posts/2026/04/nis2-directive-guide/), see our dedicated article.
- **[ENS](https://www.boe.es/eli/es/rd/2022/05/03/311)**: financial entities operating in Spain that have a relationship with public administration may need to comply with both DORA and the ENS.
- **[GDPR](https://eur-lex.europa.eu/eli/reg/2016/679)**: an ICT incident affecting personal data will trigger simultaneous obligations under both DORA and the GDPR, with different notification deadlines and authorities.
- **EBA/EIOPA/ESMA guidelines**: pre-existing sectoral guidelines (such as the EBA Guidelines on ICT risk management or the Guidelines on outsourcing) are integrated within the DORA framework.
- **[ISO 27001](https://www.iso.org/standard/27001)**: if your organization is already ISO 27001 certified, you have a solid foundation for complying with DORA's Pillar 1. Our [ISO 27001 implementation guide](/en/posts/2026/02/guia-iso-27001-startups/) can be a useful resource for understanding the reference framework.

{{< cta type="tofu" text="DORA compliance means demonstrating digital operational resilience. Riskitera maps DORA requirements to auditable controls automatically." label="See how" >}}

## When does DORA take effect?

DORA's timeline is as follows:

- **January 16, 2023**: the Regulation entered into force.
- **January 17, 2025**: date of application. From this date, all entities within DORA's scope must comply with its requirements.
- **January 17, 2025 onward**: the European Supervisory Authorities (ESAs) publish Regulatory Technical Standards (RTS) and Implementing Technical Standards (ITS) detailing specific requirements.
- **2025-2026**: designation of critical third-party ICT providers and establishment of the direct supervision framework.
- **2026**: first rounds of mandatory TLPT testing for designated entities.

In practice, national supervisory authorities have adopted a gradual approach to compliance supervision during the first year of application, prioritizing awareness and technical assistance. However, entities that fail to demonstrate significant progress face supervisory measures.

## How to prepare for DORA compliance

### 1. Applicability assessment and gap analysis

Determine whether your organization falls within DORA's scope and, if so, which specific requirements apply based on its category and size. Conduct a detailed gap analysis comparing your current posture with the requirements of the five pillars.

### 2. Strengthen governance

Ensure the management body understands its responsibilities under DORA. Establish dedicated ICT risk committees, define clear roles and responsibilities, and schedule regular training for board members.

### 3. Review the ICT risk management framework

Update your risk management framework to cover all aspects of Pillar 1: asset identification, continuous threat assessment, protection measures, detection capabilities, and response and recovery plans.

### 4. Implement notification processes

Set up internal mechanisms to classify incidents according to DORA criteria and report them within the required deadlines. This requires 24/7 detection and triage capability.

### 5. Resilience testing program

Design a testing program that includes vulnerability assessments, penetration testing, and, where applicable, TLPT exercises. Identify qualified external providers for advanced testing.

### 6. Review contracts with ICT providers

Audit all existing contracts with ICT providers to verify they include the mandatory minimum clauses required by DORA. Renegotiate where necessary and establish a centralized provider register with criticality classifications.

### 7. Automation and GRC tools

DORA's complexity makes manual management unfeasible for most entities. GRC platforms like Riskitera allow you to automate control tracking, evidence management, supplier compliance monitoring, and regulatory report generation, reducing operational burden and the risk of non-compliance.

### 8. Documentation and evidence

DORA requires the ability to demonstrate compliance to supervisory authorities. Maintaining a centralized repository of policies, procedures, test results, incident records, and compliance evidence is not optional: it is an operational necessity.

## What penalties does DORA impose for non-compliance?

DORA establishes that Member States shall define the specific penalty regime, but sets clear guidelines:

- Penalties must be effective, proportionate, and dissuasive.
- For critical ICT providers, the ESAs may impose periodic penalty payments of up to 1 percent of average daily global turnover from the previous financial year, per day of non-compliance, for a maximum of six months.
- National authorities may adopt administrative measures such as publishing penalty decisions, issuing cease-and-desist orders, and requiring corrective actions within specified deadlines.

In Spain, the Bank of Spain and the CNMV have sanctioning powers that will be applied within the DORA context.

{{< cta type="mofu" text="Prepare your financial entity for DORA with a platform that manages ICT risks, incidents, and resilience testing." >}}

## Frequently asked questions

### I'm a fintech with 15 employees. Does DORA apply to me?

If your company is a payment institution, electronic money institution, crypto-asset service provider, or another category included in Article 2 of DORA, you are subject to the regulation regardless of your size. However, DORA applies the principle of proportionality: financial microenterprises (fewer than 10 employees and less than 2 million euros in balance sheet total) have a simplified risk management framework. With 15 employees, you will likely need to comply with the full framework, but proportionately to your size and operational complexity.

### What is the difference between DORA and NIS2 for a financial entity?

DORA is lex specialis with respect to NIS2 for the financial sector. This means that, for the aspects covered by DORA (ICT risk management, incident reporting, resilience testing, third-party management), financial entities must comply with DORA rather than NIS2. However, if a financial entity operates in an area not covered by DORA, NIS2 requirements may apply on a subsidiary basis.

### Are TLPT tests mandatory for all entities?

No. Threat-led penetration testing (TLPT) is only mandatory for entities that meet certain criteria regarding size, risk profile, and systemic criticality. The competent authorities designate which entities must undergo these tests. All other entities must perform basic resilience testing (vulnerability assessments, security tests, etc.) but not the advanced TLPT exercises.

### How much time do I have to report a major incident under DORA?

The clock starts from the moment the incident is classified as major. The initial notification must be submitted within 4 hours of classification (and no later than 24 hours after detection). The intermediate report must be sent within 72 hours, and the final report within one month. These deadlines are stricter than NIS2's for initial notification, reflecting the specific criticality of the financial sector.

### My company provides cloud services to banks. Does DORA directly affect me?

Yes. DORA explicitly includes third-party ICT service providers within its scope. If your clients are financial entities, you are subject to the contractual obligations that DORA establishes (mandatory minimum clauses, audit rights, incident notification). Furthermore, if the ESAs designate you as a critical ICT provider, you will be subject to direct European supervision, with additional obligations regarding information provision, inspections, and compliance with binding recommendations.
