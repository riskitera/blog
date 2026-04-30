---
title: "How to Conduct a Cybersecurity Risk Analysis Step by Step"
image: "cover.png"
description: "Step-by-step guide to cybersecurity risk analysis: MAGERIT, FAIR, ISO 27005, and NIST RMF methodologies, asset inventory, threat assessment, risk calculation, and treatment strategies."
slug: "cybersecurity-risk-analysis-step-by-step"
date: 2026-03-15
lastmod: 2026-03-15
draft: false
index: true
tags: ["GRC", "Risk Management", "Methodology"]
categories: ["GRC"]
author: "David Moya"
translationKey: "risk-analysis-guide"
---

Risk analysis is the cornerstone process that enables organizations to identify, evaluate, and prioritize threats targeting their information assets. Without a rigorous risk analysis, security decisions are driven by gut feeling, which inevitably leads to disproportionate investment in low-risk areas and insufficient protection where it actually matters. According to the [ENISA](https://www.enisa.europa.eu/) Threat Landscape Report, over 60 percent of European SMEs that suffered a major cyberattack had not conducted a formal risk analysis beforehand. This guide walks through the complete process, the available methodologies, and the mistakes worth avoiding.

<!--more-->

{{< key-takeaways >}}
- Risk analysis is mandated by ENS, GDPR, NIS2, DORA, and ISO 27001
- Key methodologies: MAGERIT (reference in Spain), FAIR (quantitative), ISO 27005, and NIST RMF
- Process in 7 steps: scope, asset inventory, threats, vulnerabilities, calculation, prioritization, and treatment
- It should be reviewed at least annually and updated whenever significant changes occur
- The CCN's PILAR tool facilitates analysis following the MAGERIT methodology
{{< /key-takeaways >}}

## Why is risk analysis essential in cybersecurity?

Risk analysis in cybersecurity is not an academic exercise or a bureaucratic requirement: it is the foundation on which an organization's entire security strategy is built. Its benefits are concrete and measurable.

First, it enables rational resource allocation. Security budgets are always limited, and risk analysis identifies where each euro or dollar invested delivers the greatest risk reduction. Without this insight, organizations tend to invest in trendy technologies rather than addressing real risks.

Second, it is a regulatory requirement. Regulations such as Spain's National Security Framework (ENS), the [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679), the [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555) Directive, [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554), and the [ISO 27001](/en/posts/iso-27001-startup-guide/) standard all require risk analysis as a core requirement. Article 32 of the GDPR explicitly states that security measures must be proportionate to the risk, which presupposes that a formal assessment has been carried out.

Third, it facilitates communication with senior management. A well-crafted risk register translates technical threats into business impact terms (financial loss, service disruption, reputational damage), enabling business leaders to make informed decisions.

Finally, it provides a framework for continuous improvement. Risk analysis is not a static document but a cyclical process that is updated in response to changes in the threat landscape, technology infrastructure, or business requirements.

## What risk analysis methodologies exist?

Several internationally recognized methodologies are available. The right choice depends on the regulatory context, the industry, and the organization's maturity level.

### MAGERIT

MAGERIT (Methodology for the Analysis and Management of IT Risk) is the official methodology of the Spanish government, developed by the Superior Council of Electronic Administration and maintained by the [CCN](https://www.ccn-cert.cni.es/). It is the reference methodology for compliance with the [National Security Framework (ENS)](/en/posts/what-is-national-security-framework-ens/) and is widely used across the Spanish public sector and by companies working with government agencies.

MAGERIT is structured in three books: the method (which describes the process), the element catalog (which provides standardized inventories of assets, threats, and safeguards), and the techniques guide (which details complementary techniques such as impact analysis or attack trees).

Its approach is qualitative-quantitative, allowing assets and risks to be valued on both numerical scales and categorical ratings. The CCN provides the [PILAR](https://www.ccn-cert.cni.es/herramientas-de-ciberseguridad/ear-pilar.html) tool as official support for conducting MAGERIT analyses, significantly streamlining the process.

### [FAIR](https://www.fairinstitute.org/) (Factor Analysis of Information Risk)

FAIR is the only standardized quantitative model (by The Open Group) for measuring risk in financial terms. Unlike qualitative methodologies that classify risks as "high," "medium," or "low," FAIR calculates expected loss in monetary units using probability distributions.

The model breaks risk down into factors such as threat event frequency, the probability that an event results in loss, primary loss magnitude, and secondary loss magnitude (regulatory, reputational). This decomposition pinpoints which factors contribute most to overall risk.

FAIR is particularly useful for communicating risks to the CFO and for prioritizing investments based on risk-reduction return. However, it requires historical data that may not always be available, especially in less mature organizations.

### [ISO 27005](https://www.iso.org/standard/80585.html)

ISO 27005 is the international standard that provides guidelines for information security risk management within the context of an ISO 27001-based management system. It does not prescribe a specific methodology; instead, it establishes a process framework: context establishment, risk identification, risk analysis, risk evaluation, risk treatment, and communication.

Its main advantage is direct alignment with ISO 27001, which simplifies the certification journey. It is flexible enough to adapt to organizations of any size and sector, supporting both qualitative and quantitative approaches.

### NIST Risk Management Framework (RMF)

The NIST RMF, described in Special Publication [SP 800-37](https://csrc.nist.gov/pubs/sp/800/37/r2/final), defines a seven-step risk management process: prepare, categorize, select controls, implement controls, assess controls, authorize, and monitor. Complemented by the [SP 800-30](https://csrc.nist.gov/pubs/sp/800/30/r1/final) guide for risk assessment, it provides a comprehensive and detailed framework.

Although it originates in the United States, the NIST RMF is widely used internationally thanks to the quality of its documentation and the free availability of all its publications. ENISA references it as one of the benchmark frameworks in its risk management guidelines.

## How to conduct a risk analysis step by step

Regardless of the chosen methodology, the risk analysis process follows a common logical sequence.

### Step 1: Define scope and context

Before starting the analysis, it is essential to clearly define what will be analyzed. The scope may encompass the entire organization, a department, a specific information system, or a business process.

Defining the context includes identifying applicable legal and regulatory requirements (ENS, GDPR, NIS2, ISO 27001), understanding business objectives and management's risk tolerance, identifying stakeholders and their expectations, and delineating the technological and organizational boundaries of the analysis.

A common mistake is defining a scope that is too broad for the available resources. A thorough analysis of a narrow scope is preferable to a superficial analysis of the entire organization.

### Step 2: Asset inventory

Assets are elements that hold value for the organization and therefore need protection. The inventory must be exhaustive within the defined scope and should include:

**Information assets:** customer databases, intellectual property, financial documentation, employee records, strategic plans.

**Technology assets:** servers, workstations, network devices, applications, cloud services, mobile devices.

**Supporting assets:** physical facilities, power supply, HVAC systems, communications links.

**Human assets:** key personnel, undocumented specialized knowledge.

Each asset should be valued based on its importance to the organization, considering the dimensions of confidentiality, integrity, and availability. A database server holding customer information will have a high confidentiality rating, while a public-facing web server will prioritize availability.

MAGERIT provides a comprehensive catalog of asset types that facilitates this process. The CCN's PILAR tool enables asset inventory management following this classification.

### Step 3: Threat identification

For each asset or group of assets, the threats that could cause a security incident are identified. Threats are generally classified as:

**Natural threats:** floods, earthquakes, wildfires, lightning storms.

**Industrial threats:** power failures, HVAC failures, water leaks, hardware failures.

**Unintentional human threats:** configuration errors, accidental data deletion, sending information to the wrong recipient.

**Intentional human threats:** external attacks (ransomware, phishing, DDoS, APT), insider threats (disgruntled employees, industrial espionage), social engineering attacks.

The MAGERIT threat catalogs and the ENISA threat taxonomy provide comprehensive lists that help ensure no relevant threats are overlooked. Periodic reports from [INCIBE](https://www.incibe.es/) on incidents in Spain and the ENISA Threat Landscape offer up-to-date data on the prevalence of each threat type.

### Step 4: Vulnerability identification

Vulnerabilities are weaknesses in assets or their security controls that could be exploited by the identified threats. Vulnerability identification is performed through:

**Technical analysis:** vulnerability scanning, penetration testing, configuration reviews, source code analysis.

**Organizational analysis:** security policy reviews, access management process assessments, backup and recovery procedure verification.

**Human factor analysis:** security awareness evaluation, training program reviews, simulated phishing tests.

Each vulnerability is rated in terms of ease of exploitation and the degree of exposure of the affected asset.

### Step 5: Risk calculation

Risk is calculated by combining the probability that a threat will exploit a vulnerability with the impact it would have on the organization. The basic formula is:

**Risk = Probability x Impact**

In qualitative approaches, both probability and impact are expressed on categorical scales (very low, low, medium, high, very high) and combined using predefined risk matrices. In quantitative approaches such as FAIR, both factors are expressed as numerical values (annual frequency and estimated monetary loss).

Probability is estimated by considering the historical frequency of the threat, the motivation and capability of potential attackers, the ease of exploiting vulnerabilities, and the effectiveness of existing controls.

Impact is assessed across multiple dimensions: direct financial impact (recovery costs, revenue loss), regulatory impact (penalties, fines), reputational impact (loss of customer trust), operational impact (service interruption), and legal impact (litigation, liabilities).

### Step 6: Evaluation and prioritization

Once the risk for each scenario has been calculated, it is evaluated against the risk acceptance criteria defined by the organization. Risks that exceed the acceptance threshold require treatment; those that fall below it can be formally accepted.

Prioritization ranks risks from highest to lowest, enabling resources to be allocated to the most critical risks first. A visual representation using heat maps facilitates communicating results to senior management.

### Step 7: Risk treatment

For each risk that exceeds the acceptance threshold, a treatment strategy is selected:

**Mitigate:** implement security controls that reduce probability or impact. This is the most common option. Examples: deploying an EDR solution, implementing MFA, performing encrypted backups.

**Transfer:** shift the risk to a third party, typically through cyber insurance or outsourcing the service to a specialized provider with defined SLAs.

**Avoid:** eliminate the activity or asset that generates the risk. For example, ceasing to store data that is not necessary for the business.

**Accept:** formally acknowledge the risk without taking additional measures. This is only appropriate for risks that fall within the tolerance defined by management. Acceptance must be documented with the explicit approval of an authorized person.

For each mitigation measure, an implementation plan is defined with assigned owners, deadlines, required resources, and effectiveness metrics.

{{< cta type="tofu" text="Riskitera automates risk analysis with AI, mapping threats to ENS and ISO 27001 controls." label="See how it works" >}}

## What tools are used for risk analysis?

### PILAR

Developed by the CCN, PILAR is the reference tool for MAGERIT analysis. It supports the entire risk analysis process, from asset inventory to report generation, including the official threat and safeguard catalogs. A simplified version (microPILAR) is available for smaller organizations.

### Commercial tools

Platforms such as Archer (RSA), ServiceNow GRC, and OneTrust provide comprehensive risk management modules with automated workflows, real-time dashboards, and integration with other GRC functions. Riskitera automates the risk analysis process with artificial intelligence, facilitating asset identification, threat assessment, and the generation of treatment plans aligned with applicable regulatory requirements.

### Spreadsheets

While not ideal for complex analyses, spreadsheets remain a valid tool for small organizations conducting their first risk analysis. What matters most is that the tool does not become an obstacle to starting the process.

## How to build a risk register

The risk register is the central document that consolidates the results of the analysis. Each entry in the register should include:

- Unique risk identifier
- Risk scenario description
- Affected assets
- Associated threat and vulnerability
- Probability and impact rating
- Inherent risk level (before controls)
- Existing controls and their effectiveness
- Residual risk level (after controls)
- Selected treatment strategy
- Risk owner
- Treatment plan status
- Date of last review

The risk register should be reviewed at least quarterly and updated whenever there is a significant change in the threat environment, infrastructure, or business requirements.

## What are common mistakes in risk analysis?

**Performing the analysis only once.** Risk analysis is a continuous process, not a one-off project. Risks constantly evolve, and an analysis from two years ago may be completely outdated.

**Overvaluing technology risks and undervaluing organizational ones.** Many organizations focus on technical vulnerabilities and neglect risks such as lack of staff awareness, absence of incident response procedures, or dependency on critical suppliers without contractual controls.

**Not involving business stakeholders.** Risk analysis is not the sole responsibility of the IT or security department. Business leaders should participate in asset valuation and risk tolerance definition, as they best understand the real impact of an incident on operations.

**Using ambiguous rating scales.** Qualitative scales must be clearly defined with objective criteria. If "high probability" means different things to different assessors, the results will be inconsistent and unreliable.

**Ignoring residual risk.** After implementing controls, residual risk always remains and must be evaluated against the acceptance threshold. Assuming that controls eliminate risk entirely is a dangerous mistake.

## How to conduct an effective risk analysis

Start with the critical assets. Do not try to analyze everything at once. Identify the 10 or 20 most critical assets and begin with those. A deep analysis of essential assets delivers more value than a superficial analysis of the entire inventory.

Use multiple information sources. Do not rely solely on interviews: supplement with technical scans, historical incident reviews, industry reports, and statistics from bodies such as INCIBE and ENISA.

Document your assumptions. Every probability and impact rating involves assumptions. Documenting them allows you to review and update the analysis as new information becomes available.

Link risks to business objectives. Risks that directly threaten the organization's strategic objectives should receive the highest attention, regardless of their technical nature.

Automate where possible. Technology asset inventory, vulnerability scanning, and control monitoring can all be automated to keep the analysis continuously up to date.

{{< cta type="mofu" text="Simplify your next risk analysis with a platform that integrates MAGERIT, FAIR, and automated risk register management." >}}

## Frequently asked questions

### How often should I update the risk analysis

The risk analysis should be fully reviewed at least annually. In addition, it must be updated whenever significant changes occur: onboarding of new systems or services, changes in applicable regulations, relevant security incidents (your own or within your industry), major organizational changes, or audit findings. Both ISO 27001 and the ENS require periodic review of the risk analysis as a compliance requirement.

### Which methodology is best for an SME

For a Spanish SME, MAGERIT with the microPILAR tool is a solid option that facilitates ENS compliance where applicable. ISO 27005 is suitable if the organization aims for ISO 27001 certification. For SMEs that want a practical approach without excessive formality, the [NIST CSF](https://www.nist.gov/cyberframework) framework includes an accessible risk assessment function. The important thing is not choosing the perfect methodology but starting the process with the one that best fits available resources.

### Do I need an external consultant to conduct the risk analysis

It is not strictly necessary, but it is advisable for organizations conducting the analysis for the first time or lacking staff with risk management experience. An external consultant brings an independent perspective, knowledge of best practices, and cross-sector experience. In any case, the organization's internal knowledge is irreplaceable: the consultant facilitates the process, but business and IT leaders must actively participate.

### How do I integrate risk analysis with regulatory compliance

Risk analysis is the central axis that connects all regulatory requirements. The security measures required by the ENS, ISO 27001, NIS2, or GDPR must be proportionate to the identified risk. A well-executed risk analysis justifies the measures implemented, identifies compliance gaps, and prioritizes corrective actions. It is recommended to map risks against the requirements of each applicable regulation to ensure complete coverage.

### What should I do if management does not support the risk analysis process

The key is to communicate value in business terms, not technical ones. Present concrete data: the average cost of a data breach in your sector, applicable regulatory penalties, examples of incidents at comparable organizations, and the cost of inaction versus the cost of performing the analysis. Reports from INCIBE and ENISA provide statistics that can be used for this purpose. If the organization is subject to regulations that require risk analysis, the regulatory argument is an additional and unavoidable one.
