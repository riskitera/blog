---
title: "What Is Spain's National Security Framework (ENS): A Complete 2026 Guide"
image: "cover.png"
description: "Everything you need to know about Spain's Esquema Nacional de Seguridad (ENS): security levels, who must comply, key measures, and steps to implement it in your organization."
slug: "spanish-national-security-framework-ens"
date: 2026-02-28
lastmod: 2026-02-28
draft: false
index: true
tags: ["ENS", "Compliance", "Spain"]
categories: ["Compliance"]
author: "David Moya"
translationKey: "ens-guide"
---

Spain's Esquema Nacional de Seguridad (ENS) is the country's mandatory cybersecurity framework for all public sector organizations and any company providing technology services to the government. With over 15,000 entities required to comply and certification audits every two years, understanding the ENS is essential for any business operating in or with Spanish public administration.

<!--more-->

{{< key-takeaways >}}
- The ENS is mandatory for Spain's public sector and its technology suppliers (Royal Decree 311/2022)
- Three security levels (low, medium, high) with 36, 58, and 73 measures respectively
- Certification must be renewed every 2 years through an accredited external audit
- CCN-CERT provides official tools (PILAR) and CCN-STIC guidelines for implementation
- The ENS aligns with ISO 27001, NIS2, and DORA, enabling cross-compliance
{{< /key-takeaways >}}

## What is the Esquema Nacional de Seguridad (ENS)?

The ENS is a Spanish regulation that defines the security policy for the use of electronic means within the public sector. Its goal is to establish the conditions needed to build trust in the use of digital services, by implementing security measures that guarantee the confidentiality, integrity, availability, authenticity, and traceability of information.

Originally published in 2010 through Royal Decree 3/2010, the ENS has evolved significantly. The current version, approved by [Royal Decree 311/2022](https://www.boe.es/eli/es/rd/2022/05/03/311), incorporates lessons learned from over a decade of enforcement and adapts the framework to today's cybersecurity threat landscape.

The National Cryptologic Centre ([CCN-CERT](https://www.ccn-cert.cni.es/)), part of Spain's National Intelligence Centre (CNI), is the body responsible for overseeing ENS compliance and publishing the technical [CCN-STIC](https://www.ccn-cert.cni.es/series-ccn-stic.html) guidelines that detail how to implement each security measure.

## How has the ENS evolved since 2010?

The first version of the ENS was created under Law 11/2007 on citizens' electronic access to public services. At the time, public sector digitization was in its early stages and the regulation aimed to establish minimum security standards.

A minor update was published in 2015 through Royal Decree 951/2015, which adjusted some technical aspects. However, the truly significant change came in May 2022 with Royal Decree 311/2022, which repealed the previous regulation and established a completely renewed framework.

The main changes introduced in ENS 2022 include:

- **Specific compliance profiles**: the CCN has defined compliance profiles that simplify ENS adoption for specific types of organizations, such as municipalities, universities, or technology providers.
- **Continuous monitoring and incident response**: the obligation to permanently monitor systems and report incidents to CCN-CERT has been strengthened.
- **Alignment with European frameworks**: the ENS now aligns with European regulations such as the eIDAS Regulation and the [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555) Directive.
- **Supply chain management**: public administrations are now required to ensure that their technology suppliers also comply with the ENS.

## What are the ENS security levels: high, medium, and low?

The ENS classifies information systems into three categories based on the impact a security incident would have on the security dimensions (confidentiality, integrity, availability, authenticity, and traceability).

### Low level

A system is classified as low level when a security incident would have a limited impact on the organization's functions, assets, or affected individuals. A typical example: an informational website for a local council that does not handle sensitive personal data.

The measures required at the low level are proportionate: a basic security policy, access control, malware protection, backups, and a basic incident response plan. A total of 36 security measures apply.

### Medium level

This level applies when an incident would have a serious impact on functions, assets, or individuals. It is the most common level across Spanish public administration. Example: an electronic processing platform that handles personal data or administrative information.

The medium level substantially increases the requirements: formal risk management, segregation of duties, intrusion detection systems, periodic audits, and specific staff training. The number of applicable measures rises to 58.

### High level

Reserved for systems whose compromise would have a very serious or catastrophic impact. Example: systems handling classified information, critical state infrastructure, or highly sensitive data.

The high level demands the most rigorous measures: strong encryption for data at rest and in transit, 24/7 continuous monitoring, business continuity plans, advanced network segmentation, and annual external audits. All 73 ENS measures apply.

According to CCN data, in 2025 47 percent of ENS certifications were at the medium level, 31 percent at the high level, and 22 percent at the low level.

## Who is required to comply with the ENS?

The scope of the ENS is broad and extends well beyond the public sector in a strict sense:

- **Central Government** (ministries, autonomous bodies, state agencies).
- **Regional and local administrations** (autonomous communities, provincial councils, municipalities).
- **Public universities**.
- **Public law entities** linked to public administrations.
- **Public sector suppliers**: any company providing technology services, managing information systems, or processing data on behalf of a public administration must comply with the ENS to the extent applicable to the service provided.
- **Private sector operators** handling classified information or providing essential services linked to the public sector.

That last point is especially relevant: if your company develops software for the government, offers cloud services to a public body, or manages the IT infrastructure of a municipality, you need to comply with the ENS.

The CCN estimates that more than 15,000 entities in Spain are subject to ENS compliance, although the number of active certifications at the end of 2025 was around 3,200, indicating that there is still significant room for improvement.

## What are the key ENS security measures?

The ENS organizes its security measures into three frameworks:

### Organizational framework

Defines security governance policies and procedures:

- **Security policy**: a document approved by senior management that establishes the commitment to security and assigns roles and responsibilities.
- **Security regulations**: a set of internal rules governing the use of information systems.
- **Security procedures**: detailed instructions for carrying out security tasks.
- **Authorization process**: a formal mechanism for authorizing new systems or significant changes.

### Operational framework

Covers day-to-day technical and procedural measures:

- **Planning**: risk analysis, security architecture, and component acquisition.
- **Access control**: identification, authentication, access mechanisms, and segregation of duties.
- **Operations**: asset inventory, configuration management, maintenance, change management, malware protection, and incident management.
- **External services**: procurement, service level agreements, and ongoing supplier monitoring.
- **Service continuity**: continuity plans, periodic testing, and crisis management.
- **System monitoring**: intrusion detection, activity logs, and security metrics.

### Protection measures

Focused on the technical protection of assets:

- Communications protection (encryption, firewalls, network segmentation).
- Information media protection.
- Application protection (secure development, security testing).
- Information protection (classification, encryption at rest, backups).
- Service protection (availability, denial-of-service protection).

## How to implement the ENS step by step

ENS implementation is a structured process that, depending on the size of the organization and the required security level, can take between 6 and 18 months. Here are the key steps:

### 1. Secure management commitment and assign roles

Without explicit support from senior management, the project will fail. You need to designate the Information Officer, the Service Officer, and the Security Officer, as required by the ENS. In organizations at the high level, these three roles must be held by different individuals.

### 2. Define the scope and categorize the system

Identify the services and information systems that fall within the ENS scope. For each one, evaluate the security dimensions and determine the category (low, medium, or high). The CCN provides the PILAR tool to facilitate this analysis.

### 3. Conduct a risk analysis

Perform a formal risk analysis following a recognized methodology. [MAGERIT](https://www.ccn-cert.cni.es/herramientas-de-ciberseguridad/ear-pilar.html) is the standard methodology in the Spanish context and is fully aligned with the ENS. Identify assets, threats, vulnerabilities, and calculate residual risk.

### 4. Statement of applicability

Document which ENS measures apply to your system, which do not, and the justification in each case. This statement is a key document for the certification audit.

### 5. Implement the measures

Deploy the technical, organizational, and operational measures corresponding to your system's category. Use the CCN's CCN-STIC guidelines, which offer detailed instructions for each measure.

### 6. Training and awareness

Train staff on their security responsibilities. The CCN offers specific ENS training resources through its Angeles platform. Training is not a one-time event but an ongoing process.

### 7. Audit and certification

Once the measures are in place, submit the system to a compliance audit. For medium and high level systems, the audit must be conducted by an accredited independent body. After passing the audit, you obtain the ENS conformity certification, which must be renewed every two years.

If your organization is looking to streamline this process, platforms like Riskitera automate much of the documentation management, measure tracking, and audit preparation, significantly reducing manual effort and implementation timelines.

{{< cta type="tofu" text="Implementing the ENS requires mapping measures to real controls. Riskitera automates this process with AI." label="See ENS demo" >}}

## How does the ENS relate to ISO 27001, NIS2, and DORA?

The ENS does not exist in isolation. It is part of an increasingly interconnected regulatory ecosystem:

- **[ISO 27001](https://www.iso.org/standard/27001)**: the ENS and ISO 27001 share many concepts and controls. An organization certified in ISO 27001 has covered much of the ground needed for the ENS, although there are specific ENS measures that ISO does not address. If you are considering implementing ISO 27001 in your organization, we recommend our [practical ISO 27001 guide for startups](/en/posts/2026/02/guia-iso-27001-startups/).
- **[NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555)**: the European NIS2 Directive affects essential and important entities across the European Union. In Spain, the ENS will serve as a vehicle for implementing some of NIS2's requirements in the public sector. In upcoming articles, we will analyze in detail [what NIS2 is and who it affects](/en/posts/2026/04/nis2-directive-guide/).
- **[DORA](https://eur-lex.europa.eu/eli/reg/2022/2554)**: the Digital Operational Resilience Act applies to the European financial sector. Financial entities subject to DORA that also work with public administration may need to comply with both frameworks. We will soon publish a comprehensive guide on [DORA and financial cybersecurity](/en/posts/2026/04/dora-regulation-financial-cybersecurity/).
- **[GDPR](https://eur-lex.europa.eu/eli/reg/2016/679)**: ENS compliance contributes to satisfying the security requirements of the General Data Protection Regulation, although it does not replace it.

## What are the benefits of ENS certification?

Beyond legal compliance, ENS certification provides tangible advantages:

- **Access to public contracts**: an increasing number of public tenders require ENS certification as a technical solvency requirement.
- **Reduced incident risk**: certified organizations report 43 percent fewer serious incidents, according to [INCIBE](https://www.incibe.es/) data from 2024.
- **Institutional trust**: certification is a clear signal of security maturity for public bodies and business partners.
- **Operational improvement**: the implementation process forces organizations to document, streamline, and optimize their security management processes.
- **Readiness for other regulations**: it eases adaptation to NIS2, DORA, and other European regulatory frameworks.

## What are the most common mistakes when implementing the ENS?

Based on industry experience, these are the most frequent mistakes:

- **Treating the ENS as a purely technical project**: the ENS requires organizational and governance measures that go beyond technology.
- **Underestimating documentation management**: documentation is a fundamental pillar of the ENS. Without formalized policies, standards, and procedures, the audit will not be passed.
- **Ignoring the supply chain**: since Royal Decree 311/2022, suppliers must comply with the ENS. Failing to verify their compliance is both a risk and a violation.
- **Not allocating sufficient resources**: implementation requires dedication. Attempting it without dedicated staff or adequate budget is a recipe for failure.
- **Incorrectly categorizing the system**: an incorrect categorization, whether too high or too low, creates problems in both the audit and day-to-day operations.

{{< cta type="mofu" text="Prepare your organization for ENS certification with a platform that manages controls, evidence, and audits." >}}

## Frequently asked questions

### Is the ENS mandatory for private companies?

The ENS is directly mandatory for the public sector. Private companies must comply when they provide technology services to public administration, manage public sector information systems, or process data on behalf of a public entity. If your company has government contracts involving the handling of information or systems, you most likely need to comply with the ENS.

### How much does ENS certification cost?

The cost varies enormously depending on the size of the organization and the security level. For an SME seeking medium-level certification, the total cost (consulting, measure implementation, and audit) typically ranges between 25,000 and 80,000 euros. For high-level certification in large organizations, the investment can exceed 200,000 euros. GRC automation tools like Riskitera can significantly reduce these costs by eliminating repetitive manual work.

### What is the difference between the ENS and ISO 27001?

ISO 27001 is a voluntary international standard focused on information security management systems. The ENS is a mandatory Spanish regulation for the public sector with specific security measures and its own classification levels. Although they share many principles, the ENS includes specific requirements (such as compliance profiles or integration with CCN-STIC guidelines) that ISO 27001 does not cover. Many organizations choose to implement both in a coordinated manner.

### How often must ENS certification be renewed?

ENS certification is valid for two years. After that period, a renewal audit is required. Additionally, continuous monitoring is mandatory, and if significant changes are made to the systems, an extraordinary audit may be needed before the two-year period expires.

### What role does CCN-CERT play in the ENS?

CCN-CERT (National Cryptologic Centre - Computer Emergency Response Team) is the reference incident response team for Spain's public sector. Within the ENS framework, CCN-CERT publishes the CCN-STIC technical guidelines, manages official tools such as PILAR (risk analysis) and INES (ENS compliance status), coordinates incident response, and maintains an updated catalog of certified security products. It is also the body to which public entities must report security incidents.
