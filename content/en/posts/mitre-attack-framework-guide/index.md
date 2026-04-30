---
title: "MITRE ATT&CK: What It Is and How to Use It in Your Organization"
image: "cover.png"
description: "Complete guide to the MITRE ATT&CK framework: Enterprise, Mobile, and ICS matrices, tactics and techniques, SOC integration, threat hunting, and tools like ATT&CK Navigator."
slug: "mitre-attack-framework-guide"
date: 2026-04-14
lastmod: 2026-04-14
draft: false
index: true
tags: ["MITRE", "CTI", "Framework"]
categories: ["CTI"]
author: "David Moya"
translationKey: "mitre-attack-guide"
---

[MITRE ATT&CK](https://attack.mitre.org/) has become the global standard for understanding, classifying, and communicating the tactics and techniques used by adversaries in real-world cyberattacks. Maintained by MITRE Corporation, this open knowledge base documents the behavior of over 140 threat groups and catalogs hundreds of techniques observed in actual incidents. For any organization aiming for a mature security posture, learning and applying MITRE ATT&CK is not optional: it is an operational necessity.

<!--more-->

{{< key-takeaways >}}
- MITRE ATT&CK catalogs tactics, techniques, and procedures (TTPs) from real-world adversaries
- Three main matrices: Enterprise (the most widely used), Mobile, and ICS
- ATT&CK Navigator lets you visualize your organization's detection coverage
- Essential for threat hunting, control assessment, and communicating with leadership
- Direct integration with SIEM, EDR, and threat intelligence platforms
{{< /key-takeaways >}}

## What Is MITRE ATT&CK and What Is It For?

MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) is a structured knowledge base that describes attacker behavior throughout the entire lifecycle of an intrusion. Unlike other frameworks focused on defensive controls or risk management, ATT&CK adopts the adversary's perspective: it documents what attackers do, how they do it, and with what tools.

The project started in 2013 as an internal MITRE initiative to document the tactics, techniques, and procedures (TTPs) used by advanced persistent threat (APT) groups against Windows systems. Since then, it has grown exponentially and now covers enterprise environments, mobile devices, and industrial control systems.

The current version of ATT&CK (v15, released in 2024) includes 14 tactics, over 200 techniques, and more than 400 sub-techniques in the Enterprise matrix. Each technique is documented with detailed descriptions, examples of procedures used by real groups, data sources for detection, and recommended mitigations.

The framework is free, open, and maintained by a dedicated team at MITRE with contributions from the global cybersecurity community. Organizations such as [ENISA](https://www.enisa.europa.eu/), [CCN-CERT](https://www.ccn-cert.cni.es/), and CISA reference it in their guides and publications, reinforcing its position as the de facto industry standard.

## What Are the MITRE ATT&CK Matrices?

MITRE ATT&CK is organized into three main matrices, each tailored to a different technology environment.

### ATT&CK for Enterprise

[This is the most extensive and widely used matrix](https://attack.mitre.org/matrices/enterprise/). It covers Windows, macOS, Linux, cloud environments (AWS, Azure, GCP, SaaS), networks, and containers. It organizes adversary behavior into 14 tactics that represent the attacker's objectives at each phase of the intrusion:

1. **Reconnaissance**: the adversary gathers information about the target before the attack.
2. **Resource Development**: the adversary prepares infrastructure and tools.
3. **Initial Access**: the adversary gains an entry point into the network.
4. **Execution**: the adversary runs malicious code.
5. **Persistence**: the adversary maintains their presence after reboots or credential changes.
6. **Privilege Escalation**: the adversary obtains elevated permissions.
7. **Defense Evasion**: the adversary avoids being detected.
8. **Credential Access**: the adversary steals usernames and passwords.
9. **Discovery**: the adversary explores the environment to understand its composition.
10. **Lateral Movement**: the adversary moves between systems.
11. **Collection**: the adversary gathers data of interest.
12. **Command and Control**: the adversary communicates with compromised systems.
13. **Exfiltration**: the adversary extracts data from the network.
14. **Impact**: the adversary manipulates, disrupts, or destroys systems and data.

### ATT&CK for Mobile

[This matrix](https://attack.mitre.org/matrices/mobile/) covers Android and iOS devices, documenting specific techniques such as exploiting excessive application permissions, intercepting communications, or accessing device data. With the growing adoption of mobile work, this matrix gains relevance every year.

### ATT&CK for ICS

Focused on [industrial control systems (ICS/SCADA)](https://attack.mitre.org/matrices/ics/), this matrix documents techniques used against critical infrastructure such as power grids, water treatment plants, or manufacturing facilities. It includes specific tactics such as inhibiting response functions or manipulating physical processes. ENISA has highlighted the importance of protecting these environments in its annual reports, and ATT&CK for ICS provides the common vocabulary to do so.

## How Are Tactics, Techniques, and Sub-Techniques Organized?

Understanding the ATT&CK hierarchy is essential for using it correctly.

### Tactics: The "Why"

Tactics represent the adversary's tactical objective: why they perform a given action. For example, the "Persistence" tactic indicates that the attacker's goal is to maintain access to the system even after a reboot. Tactics are relatively stable and do not change frequently.

### Techniques: The "How"

Techniques describe how the adversary achieves a tactical objective. Within the "Persistence" tactic, for example, you will find techniques such as "Boot or Logon Autostart Execution" (the adversary configures programs to run automatically at system startup) or "Create Account" (the adversary creates accounts to maintain access).

### Sub-Techniques: The "How" in Detail

Sub-techniques provide an additional level of granularity. The technique "Boot or Logon Autostart Execution" breaks down into sub-techniques such as "Registry Run Keys / Startup Folder," "Authentication Package," or "Kernel Modules and Extensions." This level of detail enables more precise detection mappings.

### Procedures: The "Who and When"

Procedures are specific implementations of techniques by particular threat groups. For example, the APT29 group (associated with Russian actors) uses the "Registry Run Keys" sub-technique in a particular way, documented in ATT&CK with references to public intelligence reports.

## How Is MITRE ATT&CK Applied in the SOC?

The practical application of ATT&CK in a [security operations center](/en/posts/how-to-build-soc-from-scratch/) transforms its detection, response, and communication capabilities.

### Detection Mapping

The most immediate use of ATT&CK in the SOC is to assess which techniques the organization can detect and which represent blind spots. The process involves taking each existing detection rule in the SIEM, EDR, or other tools and mapping it to the corresponding ATT&CK technique or sub-technique. The result is a visual coverage map that reveals which tactics are well covered and where critical gaps exist.

This exercise often reveals that many organizations have good coverage for tactics like Initial Access and Execution but show significant weaknesses in Defense Evasion and Lateral Movement, which are precisely the phases where advanced attackers invest the most effort.

### Investment Prioritization

Once blind spots have been identified, ATT&CK enables prioritizing where to invest detection resources. If the organization belongs to the financial sector, it can check which threat groups target that sector, review their preferred techniques in ATT&CK, and prioritize coverage for those specific techniques. This threat intelligence-driven approach is significantly more effective than trying to cover all techniques equally.

### Standardized Communication

ATT&CK provides a common vocabulary that facilitates communication between technical teams, security managers, and leadership. Instead of describing an incident with vague terminology, analysts can report: "The adversary used T1566.001 (Spearphishing Attachment) for initial access, followed by T1059.001 (PowerShell) for execution and T1053.005 (Scheduled Task) for persistence." This precision improves report quality and investigation traceability.

### Tool Evaluation

ATT&CK is increasingly used to evaluate the effectiveness of security products. MITRE Engenuity's ATT&CK Evaluations subject EDR and endpoint security solutions to attack simulations based on the TTPs of real groups, publishing results transparently. These evaluations allow organizations to compare products using objective data.

## How to Use ATT&CK for Threat Hunting?

The ATT&CK framework is an essential tool for structuring threat hunting programs, transforming the search for threats from an ad hoc activity into a systematic, measurable process.

### Hypothesis Generation

ATT&CK enables the creation of structured hunting hypotheses. A hunter can formulate hypotheses like: "It is possible that an adversary is using T1055 (Process Injection) to execute malicious code within legitimate processes and evade our defenses." This hypothesis defines exactly what to look for, where to look, and what data sources are needed.

### Systematic Coverage

Using ATT&CK as a guide, the hunting team can plan campaigns that systematically cover the most relevant techniques for the organization. Instead of relying on individual intuition, the framework provides a structure that ensures no critical areas are overlooked.

### Linking with IOCs

Threat hunting findings frequently generate new [IOCs](/en/posts/iocs-in-cybersecurity-explained/) that enrich the organization's threat intelligence. These IOCs, mapped against the ATT&CK techniques they evidence, feed the continuous cycle of detection improvement.

{{< cta type="tofu" text="Riskitera automatically maps your detections to MITRE ATT&CK, visualizing coverage gaps in real time." label="See coverage" >}}

## What Tools Exist for Working with ATT&CK?

The ecosystem of tools around ATT&CK is broad and constantly growing.

### ATT&CK Navigator

This is [MITRE's official tool](https://mitre-attack.github.io/attack-navigator/) for visualizing coverage across the ATT&CK matrix. It allows you to create "layers" that represent existing detections, techniques used by a specific threat group, or the results of a red team exercise. Overlaying layers visually reveals coverage gaps. It is a free web tool, also available as a local application.

### MITRE ATT&CK Workbench

Allows organizations to create and maintain customized versions of ATT&CK, adding proprietary techniques, internal notes, or sector-specific adaptations. It is especially useful for organizations that want to extend the framework with their own knowledge.

### Atomic Red Team

Developed by Red Canary, this is a library of atomic tests that implement ATT&CK techniques in a safe, controlled manner. Each test is mapped to a specific technique and can be run to validate whether existing defenses detect it.

### Sigma and ATT&CK-Based Detection

[Sigma rules](https://github.com/SigmaHQ/sigma), an open format for writing generic SIEM detections, include ATT&CK tags that link each rule to the techniques it detects. This enables building detection coverage mapped directly against the framework.

### Caldera

Developed by MITRE, Caldera is an automated adversary emulation platform that executes attack chains based on ATT&CK TTP profiles. It allows simulating the behavior of specific threat groups to evaluate detection and response capabilities.

## How to Integrate ATT&CK with Your SIEM?

The integration between ATT&CK and the SIEM is one of the most powerful applications of the framework.

### Rule Tagging

Each correlation rule in the SIEM should be tagged with the ATT&CK technique or sub-technique it detects. This makes it possible to generate real-time coverage dashboards and automatically measure what percentage of the matrix is covered by active detections.

### Contextual Correlation

When a SIEM alert is mapped against ATT&CK, the analyst immediately gains additional context: which groups use that technique, which other techniques typically accompany it, what additional data sources could confirm it, and what mitigations are applicable. This context significantly accelerates triage and investigation.

### Continuous Measurement

With tagged rules, it is possible to generate continuous detection coverage metrics: percentage of techniques covered per tactic, coverage trend over time, techniques with the highest alert volume, and techniques detected but with no real alerts (possible areas of over-detection). Riskitera automatically maps security controls against MITRE ATT&CK techniques, providing instant visibility into detection coverage and the organization's blind spots.

## What Are the Common Mistakes When Implementing ATT&CK?

**Trying to cover the entire matrix at once.** ATT&CK is extensive, and attempting to detect all techniques simultaneously is unfeasible for most organizations. It is better to prioritize the most relevant techniques based on the threat profile and progress gradually.

**Confusing theoretical coverage with real detection.** Having a SIEM rule mapped to a technique does not guarantee it works. Detections must be validated periodically with tests like Atomic Red Team or red team exercises.

**Ignoring data sources.** Each technique in ATT&CK documents the data sources needed for its detection. If the organization does not collect those data sources, detection is impossible regardless of the rules configured.

**Using ATT&CK only for compliance.** The true value of ATT&CK lies in its daily operational application, not in generating coverage reports for audits. Coverage must translate into real detection and response capability.

## Official Resources and Training

MITRE offers numerous free resources for learning and applying ATT&CK:

The official page (attack.mitre.org) provides full access to the knowledge base with interactive search and navigation. The MITRE ATT&CK blog regularly publishes articles on updates, use cases, and best practices. MITRE Engenuity's ATT&CK Training courses offer structured education. CTI Blueprints provide templates for creating ATT&CK-based intelligence reports.

In the European context, CCN-CERT has published CCN-STIC guides that reference ATT&CK for threat detection in Spanish public organizations, and ENISA includes references to the framework in its annual threat report (ENISA Threat Landscape).

{{< cta type="mofu" text="Integrate MITRE ATT&CK into your SOC with a platform that connects tactics, detections, and compliance controls." >}}

## Frequently Asked Questions

### Is MITRE ATT&CK a mandatory standard?

No. MITRE ATT&CK is an open, free knowledge base, not a regulatory standard. However, its adoption is widely recommended by organizations such as ENISA, CCN-CERT, CISA, and NIST. Many organizations integrate it as part of their security programs, and ATT&CK-based product evaluations have become a common selection criterion.

### What is the difference between MITRE ATT&CK and the Cyber Kill Chain?

The Lockheed Martin Cyber Kill Chain describes the phases of an attack in a linear, high-level manner (7 phases). MITRE ATT&CK is significantly more granular, with 14 tactics and hundreds of techniques and sub-techniques. Additionally, ATT&CK does not assume a linear flow: attackers can jump between tactics and repeat phases. Both frameworks are complementary, but ATT&CK offers far greater operational utility.

### Do I need a large team to implement ATT&CK?

Not necessarily. A small organization can start by selecting the 20 to 30 techniques most relevant to its threat profile and evaluating its detection coverage against them. As the team grows and matures, coverage expands. The key is to start with a realistic scope and progress incrementally.

### How often is MITRE ATT&CK updated?

MITRE publishes major ATT&CK updates approximately twice a year, incorporating new techniques, sub-techniques, threat groups, and software documented by the community. Between major updates, minor corrections and additions are made. It is advisable to review the changelogs of each version to identify new techniques that may be relevant.

### How can I start implementing ATT&CK tomorrow?

The first practical step is to download ATT&CK Navigator and create a layer that represents the organization's current detections. This provides an immediate snapshot of coverage and blind spots. From there, prioritize techniques to cover based on the threat profile and write or acquire the corresponding detections. It is an iterative process that improves with each cycle.
