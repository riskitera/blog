---
title: "Threat Hunting: How to Hunt Threats Before They Strike"
image: "cover.png"
description: "Practical threat hunting guide: PEAK and TaHiTI methodologies, SIEM and EDR tools, Sigma rules, MITRE ATT&CK integration, and how to build an effective threat hunting program."
slug: "threat-hunting-practical-guide"
date: 2026-04-24
lastmod: 2026-04-24
draft: false
index: true
tags: ["Threat Hunting", "CTI", "SOC"]
categories: ["CTI"]
author: "David Moya"
translationKey: "threat-hunting-guide"
---

Threat hunting is the discipline of actively searching for signs of malicious activity across an organization's systems and networks without waiting for an automated alert to flag it. In an environment where the average dwell time of an attacker inside a compromised network exceeds 200 days according to multiple industry studies, the ability to detect threats before they cause real damage has become a critical differentiator. This guide covers what threat hunting is, what methodologies exist, what tools are required, and how to build an effective program from scratch.

<!--more-->

{{< key-takeaways >}}
- Threat hunting is the proactive search for threats that have evaded automated defenses
- Key methodologies: PEAK (Splunk) and TaHiTI (Trusted Automated Hunting Intelligence)
- Requires hypotheses based on threat intelligence and environmental knowledge
- Core tools: SIEM for queries, EDR for endpoint telemetry, and Sigma rules for portable detection
- Hunting findings must be converted into new automated detection rules
{{< /key-takeaways >}}

## What Is Threat Hunting and Why Is It Necessary?

Threat hunting is an offensive security activity in which skilled analysts proactively search for threats that have evaded automated detection controls. Unlike traditional alert-based monitoring, where the system notifies the analyst when something anomalous occurs, hunting inverts the flow: it is the analyst who formulates hypotheses about possible compromises and searches for evidence to confirm or rule them out.

This activity rests on a realistic premise: no detection system is perfect. Sophisticated attackers, especially APT (Advanced Persistent Threat) groups, invest significant resources in evading firewalls, antivirus, EDR, and SIEM. Threat hunting assumes that defenses may have been bypassed and looks for the traces the adversary inevitably leaves in the environment.

The SANS Institute defines three maturity levels for threat hunting. At the initial level (HM0), the organization relies exclusively on automated alerts. At the intermediate level (HM1-HM2), indicator-based searches are conducted and hypotheses begin to be formulated. At the advanced level (HM3-HM4), hunting is systematic, intelligence-driven, and supported by custom automation. Most organizations fall between HM0 and HM1, representing a significant area for improvement.

## What Is the Difference Between Reactive Detection and Proactive Threat Hunting?

Understanding the difference between reactive detection and proactive hunting is fundamental to appreciating the importance of this discipline.

### Reactive Detection

Reactive detection relies on predefined rules, signatures, and models that generate alerts when matching activity is detected. A SIEM generates an alert when a log matches a correlation rule. An EDR blocks a file whose hash appears in its signature database. An IDS detects traffic matching a known pattern.

This approach has value and is necessary, but it has fundamental limitations: it only detects what has been previously defined as malicious. If the attacker uses techniques not covered by the rules, new tools, or modifications of known malware, reactive detection fails silently.

### Proactive Hunting

Threat hunting does not depend on prior alerts. The hunter analyzes data with a hypothesis in mind, looking for anomalies, unusual patterns, or behaviors that, while not triggering alerts, may indicate a compromise. For example, a hunter might search for processes making unusual network connections for their function, service accounts logging in interactively, or massive data transfers at unusual hours.

Proactive hunting complements reactive detection. Hunting findings are frequently translated into new detection rules that improve the organization's reactive capability, creating a virtuous cycle of continuous improvement.

## How Does Hypothesis-Based Threat Hunting Work?

The most effective approach to threat hunting is formulating structured hypotheses. This method provides clear direction, scope, and evaluation criteria for each hunting campaign.

### Formulating the Hypothesis

A hunting hypothesis must be specific, testable, and relevant to the organization. A good hypothesis follows the structure: "It is possible that [type of adversary] is using [specific technique] against [specific asset or system] to achieve [tactical objective]."

Example: "It is possible that an attacker is using technique T1053.005 (Scheduled Task/Job: Scheduled Task) to maintain persistence on our production Windows servers." This hypothesis specifies the technique, the target environment, and the adversary's purpose.

Sources for generating hypotheses include threat intelligence (reports on groups targeting the sector), the [MITRE ATT&CK](/en/posts/mitre-attack-framework-guide/) framework (techniques with detection blind spots), risk assessments (critical assets insufficiently monitored), and recent incidents at similar organizations.

### Data Collection and Analysis

Once the hypothesis is formulated, the hunter identifies the necessary data sources and executes the corresponding queries. For the hypothesis above, one would query Windows scheduled task creation logs (Event ID 4698), existing scheduled tasks on the servers, and any recent execution of schtasks.exe with unusual parameters.

The analysis combines structured queries (specific queries in the SIEM) with unstructured exploration (manual review of results looking for anomalies). The analyst's experience is decisive in this phase.

### Documentation and Closure

Regardless of the outcome, each hunting campaign must be documented: hypothesis, data sources consulted, queries executed, findings, and conclusions. If the hypothesis is confirmed, an incident response process is initiated. If it is ruled out, the collected data enriches the understanding of the environment, and the queries can be converted into permanent automated detections.

## What Threat Hunting Methodologies Exist?

Several methodological frameworks provide structure and repeatability to the hunting process.

### [PEAK](https://www.splunk.com/en_us/blog/security/peak-threat-hunting-framework.html) (Prepare, Execute, and Act with Knowledge)

Developed by SANS, the PEAK framework structures hunting into three phases. The preparation phase includes hypothesis selection, data source identification, and verification that the necessary data is available and accessible. The execution phase comprises the active search, data analysis, and documentation of findings. The action phase transforms results into actions: new detections, improvements in data visibility, hardening recommendations, or incident reports.

PEAK also distinguishes between three types of hunts: hypothesis-based (described above), model-based (using statistical or machine learning models to identify anomalies), and baseline-based (establishing normal behavior and looking for deviations).

### TaHiTI (Targeted Hunting integrating Threat Intelligence)

Developed by the Dutch FI-ISAC (Financial Institutions Information Sharing and Analysis Centre), TaHiTI is a framework specifically designed to integrate threat intelligence into the hunting process. Its main contribution is a detailed workflow that connects intelligence (threat reports, IOCs, TTPs of relevant groups) with hypothesis generation and the execution of hunting campaigns.

TaHiTI defines three main phases: initiation (intelligence gathering and hypothesis generation), hunting (search execution and results analysis), and finalization (documentation, detection creation, and feedback to the intelligence cycle).

### Sqrrl Maturity Model (now AWS)

This model defines four maturity levels for hunting: level 0 (no hunting, only reactive detection), level 1 (IOC-based hunting and ad hoc searches), level 2 (hypothesis-based hunting with defined procedures), and level 3 (automated hunting with predictive models and machine learning). It provides a clear evolutionary path for organizations at different maturity stages.

## What Tools Are Used in Threat Hunting?

The hunter needs access to rich data and tools that allow querying, analyzing, and visualizing it flexibly.

### SIEM as a Hunting Platform

The SIEM is the central tool for most hunting campaigns, as it concentrates logs from multiple sources in a centralized repository with search capabilities. Modern platforms like Elasticsearch (ELK Stack), Splunk, or Microsoft Sentinel provide powerful query languages that allow hunters to formulate complex searches over large volumes of historical data.

The key to effective SIEM-based hunting is the quality and breadth of ingested data. If relevant logs are not being collected, no query will find the evidence being sought.

### EDR (Endpoint Detection and Response)

EDR solutions provide granular visibility into endpoint activity: created processes, network connections, file system modifications, registry changes, and memory activity. For endpoint-focused hunting, EDR offers data that the SIEM typically does not collect, such as parent-child process relationships or DLL loading.

### Sigma Rules

[Sigma](https://github.com/SigmaHQ/sigma) is an open format for describing detections generically, independent of the SIEM. Sigma rules are written in YAML and can be automatically converted into queries for Splunk, Elasticsearch, Microsoft Sentinel, and other platforms. The official Sigma rules repository on GitHub contains over 3,000 rules, many of them mapped against MITRE ATT&CK techniques.

For hunting, Sigma rules provide a valuable starting point: the hunter can select rules relevant to their hypothesis, convert them to their SIEM's format, and execute them as exploratory queries.

### Specialized Tools

**Velociraptor** is an open source endpoint triage and response platform that enables running VQL (Velociraptor Query Language) queries against fleets of machines remotely and in real time. It is especially useful for hunting at scale.

**OSQuery** lets you query operating system state as if it were a SQL database. Hunters can execute queries like "SELECT * FROM processes WHERE on_disk = 0" to find processes running from memory without a file on disk.

**Jupyter Notebooks** are increasingly used for advanced hunting, combining SIEM query execution with statistical analysis and visualization in an interactive, reproducible environment.

## What Skills Does a Threat Hunter Need?

Threat hunting requires a multidisciplinary professional profile that combines deep technical knowledge with analytical capability.

### Operating System Knowledge

The hunter must understand in detail how Windows, Linux, and macOS work at the system level: processes, services, registry, file system, authentication mechanisms, and native logging. Without this knowledge, it is impossible to distinguish normal activity from suspicious activity.

### Network Analysis

The ability to analyze network traffic, understand protocols, identify C2 communications, and detect data exfiltration is essential. Tools like Wireshark and Zeek are part of the hunter's standard arsenal.

### Threat Intelligence

Understanding the threat landscape, the adversary groups relevant to the organization, and their TTPs enables formulating informed hypotheses and prioritizing hunting campaigns.

### Analytical Capability

Hunting is fundamentally an exercise in analysis. The hunter must be able to correlate data from multiple sources, identify subtle patterns, and maintain attention to detail during extended investigations. [SOC analysts with experience](/en/posts/soc-analyst-roles-n1-n2-n3/) at N2 and N3 levels tend to be the best candidates for threat hunting roles.

### Programming and Scripting

Automating queries, processing data at scale, and creating custom tools require knowledge of Python, PowerShell, or Bash. Many advanced hunters develop their own tools and scripts for recurring tasks.

{{< cta type="tofu" text="Riskitera powers your threat hunting program with AI-generated hypotheses and automated telemetry correlation." label="Explore" >}}

## How to Build a Threat Hunting Program?

Implementing a structured hunting program requires planning, resources, and organizational commitment.

### Step 1: Assess Current Maturity

Before launching a hunting program, it is necessary to assess the current maturity of security operations. Hunting requires data (complete, accessible logs), tools (a SIEM with historical search capability), and qualified personnel. If the fundamentals of monitoring and reactive detection are not established, they must be built first.

### Step 2: Define Scope and Objectives

The program should start with a realistic scope. It is better to begin with weekly hunting campaigns focused on the most critical assets than to try covering the entire environment from day one. Objectives should include both threat detection and security posture improvement (new detections, improvements in data visibility).

### Step 3: Establish the Process

Define a repeatable process that includes hypothesis generation (fed by threat intelligence and risk assessments), campaign planning (data sources, tools, duration), execution, documentation, and feedback (converting findings into automated detections and visibility improvements).

### Step 4: Allocate Resources

Hunting requires dedicated time from qualified analysts. It is difficult to conduct effective hunting if analysts are permanently absorbed by the SOC alert queue. Many organizations assign a fixed percentage of senior analyst time to hunting activities, or have a dedicated role.

### Step 5: Measure and Evolve

Without metrics, it is impossible to demonstrate the program's value and justify its continuation. Process and outcome metrics are essential for the program's evolution. Riskitera includes proactive threat hunting capabilities in its SOC platform, integrating hypothesis generation with threat intelligence and automating search execution over centralized data.

## How to Measure Threat Hunting Effectiveness?

Measuring hunting effectiveness is a frequent challenge. These are the most relevant metrics:

**Campaigns executed per period:** measures the program's cadence. A mature program executes multiple campaigns per week or month.

**Hypotheses generated versus confirmed:** the percentage of hypotheses that result in real findings indicates the quality of hypothesis generation and the intelligence driving it.

**Detections created from hunting:** each hunting campaign should produce new detection rules or improve existing ones. This metric measures hunting's contribution to continuous improvement.

**Average investigation time:** the time it takes a hunter to complete a campaign, from hypothesis formulation to results documentation.

**Critical findings:** number of real compromises, undetected malware, dangerous configurations, or security blind spots discovered through hunting.

**Data visibility improvements:** campaigns that reveal that needed data sources are not being collected, leading to improvements in logging infrastructure.

## Common Mistakes in Threat Hunting

**Confusing hunting with alert response.** Investigating SIEM alerts is not threat hunting. Hunting is proactive and does not depend on prior alerts. Many organizations believe they are doing hunting when they are actually performing advanced alert triage.

**Not documenting negative results.** A hunting campaign that finds no evidence of compromise is still valuable: it confirms that, as far as could be verified, the organization is not compromised in the investigated area. Additionally, the queries developed can be reused.

**Relying exclusively on automated tools.** Automated hunting tools have value, but they do not replace human analysis. Advanced attackers are designed to evade automated detection, and it is the hunter's judgment that makes the difference.

**Not closing the loop.** Hunting must feed reactive detection. If findings are not converted into automated detections, the organization will always depend on manual campaigns to detect the same threats.

{{< cta type="mofu" text="Take your threat hunting to the next level with a platform that connects hypotheses, detections, and compliance evidence." >}}

## Frequently Asked Questions

### What is the difference between threat hunting and penetration testing?

Penetration testing simulates an attack from outside the organization to identify exploitable vulnerabilities. Threat hunting searches for evidence that a real attacker is already inside the network. Pentesting is offensive and point-in-time; hunting is defensive and continuous. Both are complementary: pentest findings can feed hunting hypotheses and vice versa.

### Do I need a dedicated team for threat hunting?

Not necessarily. Many organizations start by assigning a percentage of their N2 or N3 SOC analysts' time to hunting activities. As the program matures and demonstrates value, a dedicated team or at least a dedicated role can be justified. The important thing is that time allocated to hunting is protected and not consumed by daily alert management.

### What data do I need to collect before starting threat hunting?

At a minimum, you need authentication logs (successful and failed logins), process creation and execution logs (Event ID 4688 on Windows or auditd on Linux), network connection logs (firewall, proxy, DNS), and access logs for critical files. The greater the visibility into the environment, the more effective hunting will be. Sysmon configurations for Windows are especially valuable.

### How often should I run hunting campaigns?

Frequency depends on available resources and program maturity. A new program can start with a biweekly or monthly campaign. A mature program executes multiple campaigns per week, with varying durations depending on hypothesis complexity. The most important thing is maintaining cadence and not letting hunting be suspended when the SOC is under pressure from other incidents.

### How do I choose the most relevant hunting hypotheses?

Hypothesis prioritization should be based on three factors: threat intelligence (which groups attack your sector and what techniques they use), risk assessment (which assets are most critical and have the least detection coverage), and known blind spots (MITRE ATT&CK techniques the organization currently cannot detect). [CCN-CERT](https://www.ccn-cert.cni.es/) guides on threats relevant to the Spanish public sector and [ENISA](https://www.enisa.europa.eu/) Threat Landscape reports are valuable resources for contextualizing hypotheses in the European sphere.
