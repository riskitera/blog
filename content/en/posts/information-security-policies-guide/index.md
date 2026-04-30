---
title: "Information Security Policies: How to Create Them from Scratch"
image: "cover.png"
description: "Complete guide to creating information security policies: types of policies, drafting and approval process, employee communication, review cycle, and templates aligned with ENS and ISO 27001."
slug: "information-security-policies-guide"
date: 2026-03-20
lastmod: 2026-03-20
draft: false
index: true
tags: ["GRC", "Policies", "Compliance"]
categories: ["GRC"]
author: "David Moya"
translationKey: "security-policies-guide"
---

Information security policies are the foundational documents that establish the rules, principles, and guidelines governing information protection within an organization. Without clear, approved, and communicated policies, security depends on inconsistent individual decisions, which leads to breaches, regulatory non-compliance, and a fragile security posture. According to the [CCN-CERT](https://www.ccn-cert.cni.es/), a significant percentage of security incidents in Spanish public bodies originate from the absence or ignorance of basic policies. This guide explains what security policies are, what types your organization needs, and how to draft, approve, communicate, and maintain them.

<!--more-->

{{< key-takeaways >}}
- Security policies are required by ISO 27001 (clause 5.2) and the ENS (organizational framework)
- Key types: general policy, access control, information classification, acceptable use, and incident management
- The lifecycle includes drafting, management approval, communication, and periodic review
- They must be aligned with the applicable regulatory framework (ENS, ISO 27001, GDPR)
- Periodic review (at least annually) is as important as the initial drafting
{{< /key-takeaways >}}

## What are information security policies?

An information security policy is a formal document that defines the organization's stance on a specific aspect of information protection. It establishes what is permitted and what is not, who is responsible for what, and what the consequences of non-compliance are.

Policies sit at the top layer of the security documentation framework. Below them are procedures (how to implement the policy step by step), technical instructions (how to configure a specific system to comply with the policy), and records (evidence that the policy is being followed).

This document hierarchy is fundamental to effective security management. Policies change infrequently because they express general principles. Procedures and technical instructions change more often to adapt to technological evolution, without requiring modifications to the policy they support.

[ISO 27001](https://www.iso.org/standard/27001) requires a high-level information security policy as an ISMS requirement, along with specific policies for areas such as access control, information classification, or acceptable use of resources. The [National Security Framework (ENS)](/en/posts/what-is-national-security-framework-ens/) requires a security policy approved by the competent governing body that underpins the continuous management of security.

## What types of security policies are essential?

Every organization needs a set of policies tailored to its size, industry, and regulatory requirements. The following types are the most common and necessary.

### Information security policy

This is the top-level policy that establishes management's commitment to information security, the general security objectives, the scope of the security program, high-level roles and responsibilities, and the fundamental principles guiding all other policies. It is an explicit requirement of ISO 27001 (clause 5.2) and the [ENS](https://www.boe.es/eli/es/rd/2022/05/03/311).

This policy should be brief (two to four pages), approved by senior management, and communicated to all staff. It should not contain technical details but rather principles and strategic-level commitments.

### Acceptable use policy

Defines the rules for using the organization's technology resources: computer equipment, email, internet access, mobile devices, and any other company-provided resource. It establishes which uses are permitted (professional use, limited personal use), which uses are prohibited (downloading unauthorized software, accessing illicit content, using unapproved cloud services), and the consequences of non-compliance.

This is one of the most important policies from a legal standpoint, as it defines expectations about employee behavior and provides the basis for disciplinary action in case of violation. It should be signed by all staff as a condition for system access.

### Access control policy

Establishes the principles for identity and access management across information systems. The fundamental principles it typically includes are:

**Least privilege:** each user receives only the access strictly necessary to perform their duties.

**Need to know:** access to information is granted only to those who need it for their work.

**Segregation of duties:** critical functions are distributed among different people to prevent fraud or errors.

**Periodic review:** access rights are regularly reviewed to detect and revoke unnecessary permissions.

The policy should cover account lifecycle management (creation, modification, deactivation), authentication requirements (passwords, MFA), privileged account management, and third-party access.

### Incident response policy

Defines the framework for managing security incidents: how they are detected, classified, communicated, investigated, resolved, and documented. It establishes the roles of the response team, communication channels, escalation criteria, target response times, and obligations for notifying regulators (the [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679) requires notification of personal data breaches to the supervisory authority within a maximum of 72 hours).

This policy is critical not only for daily operations but also for regulatory compliance. [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555), [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554), and the ENS all have specific requirements regarding incident management and notification that the policy must reflect.

### BYOD policy (Bring Your Own Device)

Regulates the use of personal devices (laptops, smartphones, tablets) to access corporate resources. It should address minimum security requirements for devices (encryption, antivirus, updates), permitted applications for corporate access, separation between personal and corporate data, remote wipe capabilities in case of loss or theft, and employee responsibilities.

In the context of hybrid work, this policy is increasingly relevant. The absence of clear BYOD rules creates significant risks of information leakage and unauthorized access.

### Remote work policy

Complementary to the BYOD policy, this one establishes security conditions for telecommuting: connection requirements (mandatory VPN, secure Wi-Fi networks), information handling outside the office (prohibition on printing classified documents, screen lock), physical security of the remote workspace, and technical support procedures.

Spanish labor legislation on remote work (Law 10/2021) requires that remote work agreements include data protection measures, reinforcing the need for this policy.

### Password and authentication policy

Establishes requirements for the creation, use, and management of passwords. Current recommendations, aligned with NIST guidelines (SP 800-63B) and the CCN, prioritize length over arbitrary complexity:

Passwords of at least 12 characters for regular users and 16 for privileged accounts. Mandatory multifactor authentication (MFA) for remote access, privileged accounts, and critical systems. Prohibition on reusing passwords across services. Recommended use of corporate password managers. Prohibition on sharing credentials between employees.

This policy has evolved significantly in recent years. Frequent mandatory rotations (every 30 or 90 days) are no longer recommended except after incidents, as studies show they lead users to create weaker and more predictable passwords.

### Information classification policy

Defines the information classification levels (for example: public, internal, confidential, restricted) and the security controls applicable to each level. For each classification level, the policy establishes how information should be stored, transmitted, shared, and destroyed.

The ENS defines information levels (low, medium, high) across security dimensions that align with classification schemes. ISO 27001 requires a documented classification scheme as part of Annex A.

Without an operational information classification system, it is impossible to apply proportionate security controls: either all information is protected at the same level (costly and impractical) or arbitrary and inconsistent decisions are made.

## How to draft effective security policies

The quality of the writing determines the practical usefulness of the policies. A poorly written policy, even if technically correct, will not be understood or applied.

### Recommended structure

Each policy should follow a consistent structure that facilitates reading and reference:

**Header:** title, version, approval date, owner, document classification.

**Purpose:** what objective the policy pursues and why it is necessary. It should be concise and understandable to any employee.

**Scope:** who it applies to (all staff, IT staff, third parties) and to which systems or processes.

**Definitions:** technical or specific terms used in the document.

**Principles and guidelines:** the body of the policy, with rules and requirements stated clearly and unambiguously.

**Roles and responsibilities:** who is responsible for what in relation to the policy.

**Compliance and exceptions:** consequences of non-compliance and the process for requesting justified exceptions.

**References:** regulations, standards, or other related policies.

**Version history:** record of changes since the original version.

### Writing principles

**Clarity.** Use language that is understandable to the target audience. If the policy applies to all staff, avoid unnecessary technical jargon. If it is aimed at system administrators, appropriate technical terminology is acceptable.

**Precision.** Guidelines must be specific and measurable. Instead of "passwords should be secure," write "passwords must be at least 12 characters long." Instead of "data should be backed up regularly," write "critical data must be backed up daily with a minimum retention of 30 days."

**Brevity.** Policies should be as short as possible without sacrificing precision. Implementation details belong in procedures, not policies. A policy exceeding 10 pages is likely mixing policy and procedure.

**Feasibility.** Every guideline must be realistic and enforceable. Setting impossible requirements (for example, requiring daily password changes) does not improve security; it generates widespread non-compliance and discredits the policy program.

**Consistency.** Different policies should use coherent terminology, structure, and style. Contradictions between policies create confusion and erode trust in the documentation framework.

## What is the security policy approval process?

Formal approval is what transforms a working document into a policy with authority and binding force.

### Recommended approval workflow

1. **Initial draft** prepared by the information security officer or the security team, based on regulatory requirements, best practices, and organizational needs.

2. **Technical review** by IT and operations teams to verify the technical feasibility of the guidelines.

3. **Legal review** by the legal department to ensure compliance with labor law, data protection regulations, and other applicable legislation.

4. **Human resources review** to validate that guidelines about staff conduct and consequences of non-compliance are compatible with labor regulations and collective agreements.

5. **Management approval.** The high-level information security policy must be approved by senior management (CEO, executive committee). Specific policies may be approved by the CISO or the security officer, depending on the organization's delegation scheme.

6. **Publication and communication** to all affected personnel.

The ENS explicitly states that the security policy must be approved by the competent senior body. ISO 27001 requires that the policy be appropriate to the organization's purpose and approved by top management.

### Exception management

Every policy should include a formal process for managing exceptions. There will be situations where a policy requirement cannot be met for justified technical, operational, or economic reasons. The exception process must define who can request an exception, who approves it, what information must be provided (justification, residual risk, compensating measures, duration of the exception), and how it is documented and periodically reviewed.

Exceptions without a formal process are a frequent source of risk and of findings in [security audits](/en/posts/security-audit-practical-guide/).

## How to communicate security policies to employees

An approved policy that is unknown to staff is as useless as having no policy at all. Communication is a critical phase that many organizations neglect.

### Effective communication strategies

**Presentation sessions.** When publishing a new policy or a significant update, hold in-person or virtual sessions to explain its content, the reasons for its existence, and its impact on daily work. These sessions allow questions to be addressed and feedback to be collected.

**Integrated training.** Include security policies in the organization's mandatory training program. Security awareness sessions should constantly reference applicable policies.

**Accessibility.** Policies must be published in a location accessible to all staff: intranet, corporate document repository, or document management platform. Staff should be able to consult them at any time.

**Periodic reminders.** Use internal communications (newsletters, emails, posters) to periodically remind staff of key policies. Reminders are especially important for policies that affect daily behavior, such as the acceptable use or password policies.

**Acknowledgment of receipt.** For critical policies, require each employee to confirm they have read and understood the document. This acknowledgment, in addition to reinforcing communication, provides valuable compliance evidence for audits.

{{< cta type="tofu" text="Riskitera includes security policy templates adapted to ENS, ISO 27001, and NIS2, ready to customize." label="View templates" >}}

### Audience adaptation

Not all staff need to know every policy in the same level of detail. Communication should be adapted to the audience: management needs to understand the principles and business implications; general staff needs to know which rules apply to them directly and how to comply; technical staff additionally needs the details that enable them to implement and operate the controls.

## How often should policies be reviewed?

Security policies are not static documents. They must be reviewed and updated periodically and in response to significant events.

### Periodic review

A complete review of each policy at least once a year is recommended. The review should assess whether the policy remains relevant and adequate, whether regulatory requirements have changed, whether technology has evolved in ways that affect the policy, whether incidents have revealed deficiencies, and whether staff feedback indicates areas for improvement.

### Event-driven updates

In addition to periodic reviews, policies should be updated following significant changes: new applicable regulations (for example, NIS2 coming into force), major organizational changes (mergers, acquisitions, reorganizations), security incidents that reveal gaps in existing policies, adoption of new technologies with security implications (cloud, AI, IoT), or audit results identifying non-conformities in policies.

### Version control

Each policy must have a version control system that clearly identifies the current version, the approval date, the changes made from the previous version, and the complete version history. Access to obsolete versions should be restricted or clearly marked to prevent staff from consulting outdated documents.

## Where to find security policy templates

For organizations creating policies for the first time, templates provide a valuable starting point that significantly accelerates the process.

### Template sources

**[INCIBE](https://www.incibe.es/)** publishes templates and guides for developing security policies aimed at SMEs, available free of charge on its website.

**CCN-CERT** provides document models for ENS compliance, including the security policy and associated documents, through the CCN-STIC 800 series guides.

**ISO 27002** (2022 version) provides detailed guidance for each Annex A control of ISO 27001, which can be used as a basis for drafting specific policies.

**SANS Institute** offers security policy templates in English covering most required types, which can be adapted to each organization's context.

Riskitera includes security policy templates aligned with ENS and ISO 27001 requirements, customizable by sector and organization size, enabling companies to have a solid security documentation framework without starting from scratch.

### Adapting templates

Templates are a starting point, not a finished product. Every template must be adapted to the organization's specific context: its sector, size, organizational structure, technology environment, regulatory requirements, and corporate culture. A template copied verbatim without adaptation will be generic, inadequate, and difficult to apply.

## What are common mistakes when creating security policies?

**Drafting policies that no one reads or knows about.** The most technically perfect policy is useless if staff are unaware of it. Communication and training are as important as the drafting itself.

**Creating unfeasible policies.** Setting requirements that staff cannot reasonably comply with generates widespread non-compliance and cynicism toward the security program. Policies should be ambitious but realistic.

**Not defining responsibilities.** Each policy must assign clear responsibilities. If no one is responsible for verifying compliance, compliance will not be verified.

**Mixing policy and procedure.** The policy establishes the what and the why; the procedure establishes the how. Mixing both produces lengthy documents that are difficult to maintain and require frequent updates due to technical changes that do not affect the policy's principles.

**Not managing exceptions.** Absolute rigidity does not work in real organizations. A formal exception process allows the necessary flexibility without compromising the integrity of the normative framework.

**Not updating policies.** A password policy that requires changes every 30 days or a policy prohibiting remote work when the entire organization works remotely erodes the credibility of the entire documentation framework. Policies must reflect the organization's current reality.

{{< cta type="mofu" text="Manage the complete lifecycle of your security policies: drafting, approval, distribution, and periodic review." >}}

## Frequently asked questions

### How many security policies does my organization need

There is no fixed number. An SME can function with 5 to 8 core policies: information security policy, acceptable use, access control, incident management, information classification, passwords, backups, and change management. A large or highly regulated organization may need 15 to 25 policies covering additional areas such as software development security, vendor management, physical security, or business continuity. What matters is that each policy addresses a real need and is kept up to date.

### Who should draft the security policies

The Chief Information Security Officer (CISO) or the security team typically leads the drafting, but the process should involve other departments. IT provides the technical and feasibility perspective. Legal verifies regulatory compliance. Human resources validates labor aspects. Business leaders confirm that the policies do not obstruct operations. Cross-functional collaboration produces more balanced and applicable policies.

### Are security policies legally required

Several regulations directly or indirectly require security policies. The ENS requires a security policy for all public bodies and companies working with government agencies. The GDPR requires organizational data protection measures, which materialize as policies. ISO 27001 requires a security policy as a certification requirement. NIS2 obliges essential and important entities to adopt security policies. Even without an explicit legal requirement, security policies represent a minimum standard of due diligence that any organization should maintain.

### How do I get employees to comply with policies

Compliance requires a multi-pronged approach: clear communication of each policy's content and purpose, periodic training with practical examples, visible and consistent management support, technical controls that facilitate compliance (for example, enforcing mandatory MFA rather than relying on user willingness), proportionate and known consequences for non-compliance, and an exception process that avoids the perception of excessive rigidity. Security culture is built gradually and requires consistency and leadership.

### Can I use generic policies downloaded from the internet

Generic templates are an acceptable starting point, but they should never be used without adaptation. A policy that does not reflect your organization's reality (its technology, processes, sector, applicable regulations) will be of little use and potentially counterproductive. The value of a policy lies in its applicability to the specific context. Take the time to adapt each template, validate it with the relevant teams, and ensure the guidelines are feasible and pertinent to your organization.
