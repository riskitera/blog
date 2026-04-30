---
title: "How to Build a SOC from Scratch: A Practical Guide for Businesses"
image: "cover.png"
description: "Complete guide to building a Security Operations Center (SOC): types, team roles, required tools, processes, costs, and common mistakes to avoid."
slug: "how-to-build-soc-from-scratch"
date: 2026-04-04
lastmod: 2026-04-04
draft: false
index: true
tags: ["SOC", "Operations", "SIEM"]
categories: ["SOC"]
author: "David Moya"
translationKey: "soc-guide"
---

A Security Operations Center (SOC) is the backbone of an organization's threat detection and response capability. It brings together the people, processes, and technology needed to monitor, analyze, and respond to cybersecurity incidents around the clock, 365 days a year. Building a SOC from scratch is a complex undertaking, but with the right planning, any mid-sized or large company can do it effectively.

<!--more-->

{{< key-takeaways >}}
- Three models: in-house SOC (EUR 700K-1.5M/year), outsourced (EUR 96K-300K/year), or hybrid (EUR 250K-500K/year)
- Minimum 24/7 team: 5-6 Tier 1 analysts, 2-3 Tier 2, 1-2 Tier 3, plus SOC Manager and detection engineer
- Essential technology stack: SIEM + EDR + SOAR + threat intelligence platform
- Key metrics: MTTD, MTTR, false positive rate, and MITRE ATT&CK coverage
- Most common mistake: starting with technology instead of processes and use cases
{{< /key-takeaways >}}

## What Is a SOC and Why Does Your Business Need One?

A SOC (Security Operations Center) is a centralized function that employs people, processes, and technology to continuously monitor and improve an organization's security posture, while preventing, detecting, analyzing, and responding to cybersecurity incidents.

According to a report by [INCIBE](https://www.incibe.es/) on the state of enterprise cybersecurity in Spain (2025), the average time to detect a security incident in companies without a SOC is 197 days, compared to an average of 38 days in companies with an operational SOC. This difference is critical: every day a threat remains undetected in your systems exponentially increases the potential damage.

The main reasons for having a SOC are:

- **Early threat detection**: continuous monitoring allows you to identify suspicious activity before it becomes a serious incident.
- **Rapid incident response**: a dedicated team can contain a threat in minutes or hours, rather than days or weeks.
- **Regulatory compliance**: regulations such as [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555), [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554), the [ENS](https://www.boe.es/eli/es/rd/2022/05/03/311), and [ISO 27001](https://www.iso.org/standard/27001) require monitoring and incident response capabilities that, in practice, demand a SOC.
- **Global visibility**: the SOC provides a unified view of the security status across the entire organization.
- **Reduced incident costs**: according to IBM, the average cost of a data breach in Europe was EUR 4.3 million in 2025. Organizations with a SOC reduced that cost by 40 percent on average.

## What Types of SOC Exist: In-House, Outsourced, or Hybrid?

Before designing your SOC, the first strategic decision is choosing the operating model.

### In-House SOC

The organization builds and operates its own SOC with its own staff, technology, and infrastructure.

**Advantages:**
- Full control over processes and data.
- Deep knowledge of the environment and business context.
- Maximum customization capability.
- Direct alignment with organizational objectives.

**Disadvantages:**
- High cost: infrastructure, licenses, salaries for a 24/7 team.
- Difficulty recruiting and retaining specialized talent in a high-demand market.
- Long setup time (12-18 months for a mature SOC).
- Risk of team burnout if not properly sized.

### Outsourced SOC (MSSP/MDR)

The organization contracts an external managed security service provider (MSSP) or managed detection and response (MDR) provider to operate the SOC.

**Advantages:**
- Operational from day one.
- Predictable cost, generally lower than an in-house SOC.
- Access to specialized talent and global threat intelligence.
- Immediate scalability.

**Disadvantages:**
- Less control over processes and prioritization.
- Dependency on a third party for a critical function.
- Potential lack of business context.
- Limitations in detection rule customization.

### Hybrid SOC

Combines a small internal team with support from an external provider. This is the most widely adopted model among mid-sized companies in Spain.

**Advantages:**
- Balance between control and cost.
- The internal team provides business context; the provider delivers 24/7 coverage and advanced capabilities.
- Flexibility to scale as needed.
- Knowledge transfer between the internal team and the provider.

**Disadvantages:**
- Requires good coordination between internal and external teams.
- Clear definition of roles, responsibilities, and escalation paths is essential.
- Managing two distinct operational cultures.

According to INCIBE data, in 2025, 34 percent of mid-sized and large Spanish companies with a SOC operated a hybrid model, 41 percent fully outsourced, and 25 percent maintained a purely in-house SOC.

## What Roles Does a SOC Team Need?

A SOC team is organized into three tiers with differentiated functions, skills, and responsibilities. For a deep dive into each professional profile, we recommend our article on [SOC analysts: Tier 1, Tier 2, and Tier 3 roles explained in detail](/en/posts/2026/04/soc-analyst-roles-tiers-explained/).

### Tier 1 (N1): Triage Analyst

Tier 1 analysts are the first line of defense. Their primary function is to monitor alerts generated by security tools, perform initial triage, and escalate alerts that require further investigation.

**Responsibilities:**
- Continuous monitoring of alerts from SIEM, EDR, IDS/IPS, and other sources.
- Initial triage and classification of alerts (true positive, false positive, requires escalation).
- Basic documentation of each alert in the ticketing system.
- Execution of predefined playbooks for routine incidents.
- Escalation to Tier 2 for alerts requiring investigation.

**Typical profile:** 1-2 years of IT or cybersecurity experience. Basic knowledge of networking, operating systems, and SIEM tools. Ability to work in shifts.

A 24/7 SOC needs a minimum of 5-6 Tier 1 analysts to cover all three shifts with vacation and sick leave coverage.

### Tier 2 (N2): Incident Analyst

Tier 2 analysts investigate alerts escalated by Tier 1 in depth, determine the scope and severity of incidents, and coordinate the response.

**Responsibilities:**
- Deep investigation of escalated alerts.
- Event correlation from multiple sources to determine incident scope.
- Basic malware analysis and preliminary forensics.
- Incident response coordination.
- Development and improvement of detection rules and playbooks.
- Incident report generation.

**Typical profile:** 3-5 years of cybersecurity experience. Advanced knowledge of threat analysis, digital forensics, and incident response. Experience with SIEM, EDR, and SOAR tools.

A mature SOC needs at least 2-3 Tier 2 analysts.

### Tier 3 (N3): Senior Analyst / Threat Hunter

Tier 3 analysts are the most experienced profiles in the SOC. They focus on proactive threat hunting, advanced malware analysis, and continuous improvement of detection capabilities.

**Responsibilities:**
- Proactive threat hunting: searching for threats that have evaded automated detection mechanisms.
- Advanced malware analysis (reverse engineering).
- Advanced digital forensics.
- Applied threat intelligence development.
- Detection architecture design and rule optimization.
- Technical advisory on complex incidents.
- Mentoring Tier 1 and Tier 2 analysts.

**Typical profile:** 5+ years of cybersecurity experience. Specialization in forensics, malware analysis, or threat intelligence. Advanced certifications (GCFA, GREM, OSCP).

A typical SOC has 1-2 Tier 3 analysts.

### Other Key Roles

- **SOC Manager**: responsible for overall SOC operations, team management, metrics and KPI definition, and executive reporting.
- **Detection Engineer**: develops and maintains correlation rules, use cases, and the SIEM infrastructure.
- **Automation Engineer (SOAR)**: develops automated playbooks and manages the SOAR platform.

## What Tools Does a SOC Need?

Technology is one of the three pillars of a SOC, alongside people and processes.

### SIEM (Security Information and Event Management)

The SIEM is the central tool of the SOC. It collects logs from across the infrastructure, normalizes them, correlates them, and generates alerts. For a detailed guide on [what a SIEM is and how it works](/en/posts/2026/04/what-is-siem-why-you-need-it/), see our dedicated article.

Main options on the market:
- **[Splunk](https://www.splunk.com/) Enterprise Security**: market leader, powerful but costly.
- **[Microsoft Sentinel](https://azure.microsoft.com/products/microsoft-sentinel)**: cloud-native solution, ideal for Microsoft/Azure environments.
- **IBM QRadar**: robust, with strong out-of-the-box correlation capabilities.
- **[Elastic Security](https://www.elastic.co/security)**: built on Elasticsearch, with an open source option.
- **Google Chronicle (SecOps)**: cloud-first approach with massive-scale analytics capabilities.

### EDR (Endpoint Detection and Response)

Provides visibility and response capability at the endpoint level (servers, workstations, mobile devices):
- CrowdStrike Falcon.
- Microsoft Defender for Endpoint.
- SentinelOne.
- Carbon Black (VMware).

### SOAR (Security Orchestration, Automation and Response)

Automates incident response through predefined playbooks and orchestrates security tools:
- Palo Alto XSOAR (formerly Demisto).
- Splunk SOAR (formerly Phantom).
- IBM QRadar SOAR.
- Shuffle (open source).
- Tines.

### Other Tools

- **NDR (Network Detection and Response)**: Darktrace, Vectra AI, ExtraHop.
- **Threat Intelligence Platform**: MISP (open source), Anomali, Recorded Future.
- **Ticketing System**: ServiceNow, Jira Service Management, TheHive.
- **Forensic Tools**: Velociraptor, Autopsy, Volatility.
- **Vulnerability Management**: Qualys, Tenable, Rapid7.

{{< cta type="tofu" text="Building a SOC requires the right tools. Riskitera integrates SIEM, correlation, and AI-powered triage in a single platform." label="Learn more" >}}

## What Are the Core Processes of a SOC?

Technology without well-defined processes is useless. These are the essential processes:

### Alert Management

Define a clear workflow from alert generation to closure:
1. Alert reception and logging.
2. Initial triage (Tier 1): severity classification and action determination.
3. Investigation (Tier 2): detailed analysis if warranted.
4. Response: execution of containment and remediation actions.
5. Closure: final documentation and lessons learned.

### Incident Response

Based on recognized frameworks such as [NIST SP 800-61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) or [CCN-CERT](https://www.ccn-cert.cni.es/) guidelines:
1. Preparation.
2. Detection and analysis.
3. Containment.
4. Eradication.
5. Recovery.
6. Lessons learned.

### Threat Hunting

A proactive threat search process:
1. Hypothesis formulation based on threat intelligence.
2. Relevant data collection.
3. Investigation and analysis.
4. Findings documentation.
5. Converting findings into new detection rules.

### Use Case Management

Use cases are the detection rules that feed the SIEM:
1. Identification of relevant threats (based on [MITRE ATT&CK](https://attack.mitre.org/)).
2. Detection logic design.
3. Implementation in the SIEM.
4. Testing and validation.
5. Ongoing operation and tuning.

### Metrics and KPIs

Measure SOC effectiveness with key metrics:
- **MTTD (Mean Time to Detect)**: average time from when an incident occurs until it is detected.
- **MTTR (Mean Time to Respond)**: average time from detection to containment.
- **False positive rate**: percentage of alerts that turn out to be false positives.
- **Alert volume per analyst**: workload indicator.
- **MITRE ATT&CK coverage**: percentage of framework techniques covered by detection rules.

## How Much Does It Cost to Build and Operate a SOC?

SOC costs vary enormously depending on the model, size, and desired maturity level. These are indicative references for the Spanish market in 2026:

### In-House SOC

- **Personnel** (minimum team for 24/7: 8-10 people): between EUR 450,000 and 700,000 per year in salaries and associated costs.
- **Technology** (SIEM, EDR, SOAR, infrastructure): between EUR 150,000 and 500,000 per year in licenses, depending on data volume and chosen tools.
- **Physical infrastructure**: between EUR 50,000 and 200,000 initial investment (operations room, monitors, servers).
- **Training and certifications**: between EUR 30,000 and 60,000 per year.
- **Estimated first-year total cost**: between EUR 700,000 and 1,500,000.
- **Annual recurring cost**: between EUR 650,000 and 1,200,000.

### Outsourced SOC (MSSP/MDR)

- **Typical cost for a mid-sized company**: between EUR 8,000 and 25,000 per month (EUR 96,000 to 300,000 per year), depending on service scope, number of data sources, and contracted SLAs.

### Hybrid SOC

- **Small internal team** (3-4 people): between EUR 180,000 and 320,000 per year.
- **Complementary MSSP service**: between EUR 5,000 and 15,000 per month.
- **Estimated total cost**: between EUR 250,000 and 500,000 per year.

Riskitera offers 24/7 managed SOC services with a flexible model that adapts to each organization's needs, combining experienced analysts with advanced detection and response technology.

## What Are the Most Common Mistakes When Building a SOC?

These are the mistakes we see most frequently in organizations trying to build a SOC:

### Starting with Technology Instead of Processes

Many companies invest in expensive tools before defining what they want to detect, how they will respond, and who will operate the SOC. Technology should serve the processes, not the other way around.

### Underestimating Staffing Needs

A 24/7 SOC requires more staff than it may seem. Having only two or three analysts to cover night shifts, weekends, holidays, and sick leave is a recipe for burnout and turnover.

### Not Defining Use Cases Before Deploying the SIEM

Connecting all log sources to the SIEM without having defined what you want to detect generates an unsustainable volume of alerts, most of them irrelevant. It is better to start with 20-30 well-tuned use cases and grow gradually.

### Ignoring Alert Fatigue

If analysts receive hundreds of daily alerts, most of them false positives, they will stop paying attention. Continuous tuning of detection rules and automation through SOAR are essential.

### Not Measuring Effectiveness

Without clear metrics (MTTD, MTTR, false positive rate), it is impossible to know if the SOC is working or if it is simply a passive monitoring center.

### Forgetting Continuous Training

The threat landscape changes constantly. A SOC team that does not continuously train will become obsolete in months. Allocate budget and time for certifications, red team exercises, and participation in security communities.

{{< cta type="mofu" text="Planning your SOC? Request a free assessment and discover how Riskitera reduces deployment time." >}}

## Frequently Asked Questions

### What Company Size Justifies a SOC?

There is no single threshold. As a general reference, companies with more than 200-300 employees, operating in regulated sectors or handling sensitive data, tend to benefit from a SOC, even in an outsourced or hybrid model. The decision depends more on the risk profile than on size: a fintech with 50 employees processing millions of transactions may need a SOC before an industrial company with 500 employees and low digital exposure.

### How Long Does It Take to Build a SOC from Scratch?

For an in-house SOC with basic operational capability (8x5 coverage, initial use cases, trained team), 6 to 9 months. To achieve a mature SOC with 24/7 coverage, proactive threat hunting, and advanced automation, 18 to 24 months. An outsourced SOC can be operational in 4-8 weeks.

### Can I Build a SOC Using Only Open Source Tools?

Technically yes. Elastic Security as SIEM, [Wazuh](https://wazuh.com/) as EDR, Shuffle as SOAR, MISP as a threat intelligence platform, and TheHive as a ticketing system form a functional stack. Licensing costs will be minimal, but you will need experienced staff to deploy, configure, maintain, and operate these tools, which may cost more in qualified personnel.

### What Certifications Should the SOC Team Have?

The most valued certifications for SOC teams are: [CompTIA Security+](https://www.comptia.org/certifications/security) and CySA+ for Tier 1, GCIH and ECIH for Tier 2, and GCFA, GREM, or OSCP for Tier 3. For the SOC Manager, CISM or [CISSP](https://www.isc2.org/certifications/cissp). Vendor-specific certifications (Splunk Certified Power User, Microsoft SC-200) are also very useful for engineering roles.

### How Do You Measure SOC ROI?

SOC ROI is measured by comparing SOC costs against costs avoided through incidents prevented. Key metrics are: reduction in detection time (MTTD), reduction in response time (MTTR), number of incidents contained before causing damage, reduction in average incident cost, and savings from avoided regulatory penalties. According to the Ponemon Institute, organizations with a mature SOC reduce the average data breach cost by 40 to 50 percent.
