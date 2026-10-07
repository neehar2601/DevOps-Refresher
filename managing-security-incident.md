# Managing Security Incidents: Incident Response, Computer Crimes & Forensics Guide

> 📘 **Quick Navigation**:
> * 🛡️ **[Security Hub Overview](Security/security_index.html)** — Interactive browser portal with CIA triad, IAM, Zero Trust, and live attack simulators.
> * 🌐 **[Network Security & Firewalls Guide](networking-security-firewalls.md)** — Stateful vs. Stateless firewalls, NACLs vs. Security Groups, VPN architectures.
> * ☸️ **[Kubernetes Security & PKI](kubernetes-security.md)** — Cluster CA, client authentication, mTLS, RBAC, and Admission Controllers.
> * ⚡ **[DevOps & Networking Cheat Sheet](networking-cheatsheet.md)** — Comprehensive CLI reference and interview quick guide.

---

## 1. Executive Overview & Foundational Concepts

In modern enterprise infrastructure, security breaches are an operational reality rather than a statistical anomaly. Organizations must transition from an assumption of impenetrable defense to an **assumed breach** mindset.

```
+---------------------------------------------------------------------------------------------------+
|                                     THE SECURITY CONTINUUM                                        |
|                                                                                                   |
|    [ Event ]                      [ Alert ]                   [ Incident ]             [ Breach ] |
|  Any observable           System flags an anomaly      Specific risk event      Confirmed theft   |
|  occurrence in a       (e.g., 5 failed SSH attempts)   occurring; threatens     or exfiltration of|
|  system or network                                     confidentiality,         sensitive data    |
|                                                        integrity, or            to unauthorized   |
|                                                        availability             third parties     |
+---------------------------------------------------------------------------------------------------+
```

### A. What is a Security Incident?
* **Definition**: A **security incident** is a specific instance of a risk event occurring, whether it immediately causes measurable damage or not.
* **Scope**: It represents an unauthorized, unexpected, or adverse event that threatens the **Confidentiality, Integrity, or Availability (CIA Triad)** of an organization's computing systems, networks, or digital assets.
* **Examples**:
  * An employee falls for a phishing email and enters credentials on an attacker's portal.
  * A distributed denial-of-service (DDoS) flood degrades web server responsiveness.
  * An unauthorized consumer Wi-Fi access point (Rogue AP) is plugged into an office Ethernet wall jack.
  * Malware or ransomware executes on an internal endpoint, even if contained by endpoint detection (EDR).

### B. What is Security Incident Management?
* **Definition**: **Security Incident Management** is the formal framework of policies, procedures, tools, and practices that govern how an organization detects, analyzes, prioritizes, contains, and remediates an incident in progress.
* **Primary Objectives**:
  1. **Contain the Incident**: Prevent lateral movement and stop active exfiltration.
  2. **Minimize Damage**: Reduce financial loss, business interruption, reputational damage, and operational fallout.
  3. **Restore Operations**: Return compromised workloads to a known, verified secure state without reintroducing vulnerabilities.
  4. **Log & Report**: Document all actions taken, preserve digital evidence for potential legal proceedings, and fulfill regulatory compliance mandates.

### C. Understanding Computer Crimes
* **Definition**: A **computer crime** (cybercrime) is any criminal act that involves using a computer or network infrastructure as a **source (instrument)**, a **target (victim)**, or both, rather than directly targeting an individual in physical space.
* **Categorization & Real-World Examples**:
  * **Unauthorized Access**: Infiltrating corporate networks, databases, or cloud accounts without legal authorization (e.g., violations of the *Computer Fraud and Abuse Act / CFAA* in the US).
  * **Intellectual Property & Data Theft**: Exfiltrating proprietary source code, trade secrets, customer PII, credit card records, or classified government intelligence.
  * **Malicious Code Propagation**: Developing, deploying, or renting ransomware, wiper malware, trojans, rootkits, or botnets.
  * **Financial Fraud & Extortion**: Business Email Compromise (BEC), CEO fraud, unauthorized wire transfers, and double-extortion ransomware campaigns.
  * **Network Disruption & Sabotage**: Bombarding infrastructure with DDoS attacks or wiping industrial control systems (SCADA).
  * **Social Engineering as Cybercrime**: Phishing, spear-phishing, whaling, vishing, and smishing schemes designed to execute fraudulent financial transactions or identity theft.

---

## 2. The Incident Response Policy (IRP)

An **Incident Response Policy (IRP)** is a high-level governance policy approved by executive management and board leadership that establishes the mandatory operational framework an organization must follow when a security incident or suspected breach occurs.

```mermaid
graph TD
    IRP[Incident Response Policy - IRP] --> Prep[1. Preparation & Threat Intelligence]
    IRP --> Auth[2. Declaration Authority - Who Declares?]
    IRP --> Triage[3. Identification & Triage Methodology]
    IRP --> Resp[4. Escalation Paths & SLA Matrices]
    IRP --> Legal[5. Legal, Regulatory & PR Mandates]

    Auth --> Declared{Incident Declared?}
    Declared -->|Yes| Mobilize[Mobilize CSIRT & Execute Runbook]
    Declared -->|No| SOC[Log as Security Event / Routine Ticket]
```

### Key Elements Mandated by an IRP:

#### 1. Preparation Measures
* Requires ongoing research into known, emerging, and likely threat vectors (Threat Intelligence feeds, MITRE ATT&CK mappings, CVE vulnerabilities).
* Mandates the creation and periodic rehearsal of specialized **Incident Response Playbooks** (e.g., Ransomware Playbook, Cloud Credential Leak Playbook, Compromised Laptop Playbook).
* Enforces tabletop exercises (TTX) and simulated adversary drills (Red Team vs. Blue Team) at least annually.

#### 2. Authority to Declare an Incident
* **The Problem**: If any employee could declare an incident, false alarms would trigger costly business shutdowns. Conversely, if no one has the authority, incidents are swept under the rug.
* **The Policy Mandate**: The IRP explicitly specifies **WHO** has the legal and administrative authority to declare an official security incident:
  * Typically designated to the **Chief Information Security Officer (CISO)**, **Incident Commander**, or the **Lead CSIRT Incident Handler**.
  * Defines formal criteria that differentiate a routine *Security Event* (handled by Tier 1 SOC analysts) from an *Official Security Incident* (mobilizing the full incident task force).

#### 3. Incident Identification & Triage Methodology
* Specifies the objective criteria used to evaluate reported anomalies.
* Dictates how the incident team will investigate, categorize, and assign severity ratings.
* Mandates clear communication paths so employees know how to immediately report suspicious indicators (e.g., dedicated emergency phone line, `#security-incident` Slack channel, or automated ticketing integration).

### Severity Classification Matrix

| Severity Level | Business Impact | Example Scenario | Initial Response SLA | Escalation Target |
| :--- | :--- | :--- | :--- | :--- |
| **P1 - Critical** | Catastrophic business disruption; critical core systems down; mass data exfiltration. | Ransomware spreading across production Kubernetes cluster; active Active Directory domain takeover. | **Immediate (< 15 mins)** | Executive Leadership, Board, Legal Counsel, External DFIR Firm |
| **P2 - High** | Significant impact on sensitive operations; localized compromise of production services. | Compromised AWS IAM Administrator key; unauthorized database query dumping customer PII. | **< 30 minutes** | CISO, Security Director, Cloud Infrastructure Leads |
| **P3 - Medium** | Limited impact; single endpoint infected; no confirmed lateral movement. | Single workstation infected with adware or non-propagating trojan; brute-force attempt against test environment. | **< 2 hours** | SOC Tier 2 Analysts, Endpoint Engineering |
| **P4 - Low** | Negligible impact; informational security events or benign policy violations. | Single employee clicking an educational phishing simulation link; port scan deflected by edge firewall. | **< 8 hours / Next Business Day** | SOC Tier 1 Analyst, User Security Awareness Team |

---

## 3. The Incident Response Task Force (CSIRT / CIRT)

An organization creates a designated **Computer Security Incident Response Team (CSIRT)** or **Cyber Incident Response Team (CIRT)** specifically empowered to manage all aspects of incident response across the enterprise.

```
+------------------------------------------------------------------------------------+
|                      INCIDENT RESPONSE TASK FORCE STRUCTURE                        |
|                                                                                    |
|                           [ Incident Commander (IC) ]                              |
|                    Single point of tactical and operational authority              |
|                                         |                                          |
|         +-------------------------------+-------------------------------+          |
|         |                               |                               |          |
|         v                               v                               v          |
|  [ Technical Leads ]           [ Business Advisors ]          [ Communications ]   |
|  - Lead SOC Analyst             - Corporate Legal Counsel       - PR / Media Team  |
|  - DFIR Specialist              - Human Resources (HR)          - Internal Comms   |
|  - Cloud / DevOps Engineer      - Compliance / Privacy          - Customer Support |
|  - Network Engineer             - Risk Management               - Executive Liaison|
+------------------------------------------------------------------------------------+
```

### Core Roles & Responsibilities:

* **Incident Commander (IC)**:
  * Holds ultimate tactical command over response operations.
  * Directs technical teams, approves containment actions (e.g., severing internet uplinks or shutting down production databases), and coordinates cross-departmental operations.
* **Digital Forensics & Incident Response (DFIR) Specialists**:
  * Execute forensic evidence acquisition (memory dumps, disk images, network packet captures).
  * Reverse-engineer malware artifacts, trace attackers' command-and-control (C2) channels, and reconstruct the timeline of compromise.
* **DevOps / Cloud Infrastructure Engineers**:
  * Implement technical containment in cloud environments: isolating EC2 instances, modifying Security Groups, revoking IAM credentials, and rotating Kubernetes secrets.
* **Corporate Legal Counsel**:
  * Assesses legal exposure, attorney-client privilege protection for investigation findings, regulatory notification duties, and potential liability.
* **Public Relations & Communications**:
  * Controls external messaging to customers, news media, and partners to prevent panic, misstatements, or premature disclosures that could alert the adversary.
* **Human Resources (HR)**:
  * Directly involved in cases involving insider threats, rogue employees, credential sabotage, or acceptable-use policy violations.

---

## 4. The 6-Phase Incident Response Lifecycle (NIST SP 800-61 & SANS)

Industry-standard incident response frameworks follow a structured, iterative lifecycle (NIST SP 800-61 Rev. 2 and SANS PICERL):

```mermaid
flowchart LR
    P1[1. Preparation] --> P2[2. Identification]
    P2 --> P3[3. Containment]
    P3 --> P4[4. Eradication]
    P4 --> P5[5. Recovery]
    P5 --> P6[6. Lessons Learned]
    P6 -.->|Continuous Feedback Loop| P1
```

---

### Phase 1: Preparation
*The most critical phase; executed BEFORE an incident occurs.*

* **Infrastructure Hardening**: Deploy central log aggregation (SIEM), Endpoint Detection & Response (EDR), and Network Traffic Analysis (NTA).
* **Forensic Toolkits ("Jump Bags")**: Pre-stage clean forensic workstations, write-blockers, imaging software (`dd`, `FTK Imager`), and memory capture tools (`LiME`, `DumpIt`, `WinPmem`).
* **Out-of-Band (OOB) Communications**: Establish dedicated communication channels (e.g., encrypted Signal groups or external conference bridges) in case primary email or Slack is monitored or compromised by the adversary.
* **Access & Credentials**: Secure break-glass administrative accounts with hardware-backed MFA (FIDO2 keys) stored in physical vaults.

---

### Phase 2: Identification & Detection
*Discovering the incident, scoping its extent, and validating legitimacy.*

* **Signals & Detection Vectors**:
  * Automated EDR alerts (e.g., suspicious PowerShell execution, unauthorized LSASS memory dump).
  * SIEM correlation rules (e.g., root login from an unexpected geographical location).
  * Network IDS/IPS alerts (e.g., beaconing traffic matching known C2 server IP addresses).
  * User reports (e.g., employee reporting desktop wallpaper changed to a ransom note).
* **Triage & Validation**:
  * Distinguish between **False Positives** and verified incidents.
  * Identify **Indicators of Compromise (IoCs)**: File hashes (SHA-256), malicious domain names, attacker IP addresses.
  * Identify **Indicators of Attack (IoAs)**: Behavioral patterns such as living-off-the-land binaries (LOLBins), privilege escalation, or unauthorized access attempts.
* **Scoping**:
  * Determine all affected systems, user accounts, network segments, and data repositories.

---

### Phase 3: Containment
*Stopping the bleeding and preventing the adversary from moving laterally.*

Containment is split into two strategic stages:

```
[ Compromised Endpoint ]
         |
         +---> Short-Term Containment: Network Isolation (Quarantine VLAN / SG)
         |     * Preserves RAM state; severs attacker's C2 connection.
         |
         +---> Forensic Snapshotting: Live Memory Dump + Disk Bit-Stream Image
         |
         +---> Long-Term Containment: Firewall blocks, credential revokes, clean patching
```

#### A. Short-Term Containment (Immediate Isolation)
* **Crucial Rule**: **DO NOT immediately power off or reboot a compromised machine!** Rebooting wipes volatile RAM, destroying active network socket tables, running malware payloads, encryption keys, and injector processes.
* **Techniques**:
  * Isolate the endpoint from the network via EDR soft-isolation or by moving the switch port to an unrouted Quarantine VLAN.
  * In cloud environments (AWS/Azure), detach default security groups and attach an empty `Quarantine-SG` that blocks all inbound and outbound traffic except from the forensic jump host.

#### B. Long-Term Containment
* Apply temporary firewall blocks against attacker C2 IP addresses and domains.
* Invalidate compromised user sessions and rotate active API tokens and passwords.
* Isolate sensitive database segments to prevent lateral movement.

---

### Phase 4: Eradication
*Completely removing the attacker's presence from the environment.*

* **Root Cause Identification**: Determine the exact initial access vector (e.g., unpatched CVE-2023-38606 in web server, stolen VPN credentials, phishing payload).
* **Malware & Artifact Removal**: Delete malware binaries, scheduled tasks, hidden cron jobs, rogue user accounts, and persistence hooks.
* **Vulnerability Remediation**: Patch the underlying software vulnerability or reconfigure misconfigured access control lists (ACLs).
* **Credential Reset**: Force a global password reset for all compromised identity tiers, including Active Directory Kerberos Ticket Granting Service accounts (`KRBTGT`) in case Golden Ticket attacks were staged.

---

### Phase 5: Recovery & Restoration
*Safely restoring systems to normal production operations.*

* **Rebuild from Trusted Sources**:
  * Re-image endpoints and redeploy servers using clean, automated Infrastructure-as-Code (Terraform / Ansible) and validated golden AMI images.
  * Do **not** restore unvetted system backups that may already contain the attacker's dormant backdoors.
* **Validation & Testing**:
  * Validate system integrity, test database connectivity, and confirm services operate correctly before opening to general users.
* **Enhanced Monitoring**:
  * Place restored systems under hyper-care telemetry monitoring for 30–90 days to verify the adversary does not attempt re-entry.

---

### Phase 6: Lessons Learned (Post-Incident Review)
*Institutionalizing knowledge to prevent recurrence.*

* **Post-Mortem Meeting**: Conducted within 1–2 weeks following incident closure. Involves all technical leads, business stakeholders, and executives.
* **Blameless Culture**: Focus on systemic process failures, architectural vulnerabilities, and detection gaps rather than assigning individual human blame.
* **Deliverable: Root Cause Analysis (RCA) Document**:
  * Detailed chronological timeline of the incident.
  * Total business impact (cost, downtime, compromised records).
  * What worked well in the response process vs. what failed or took too long.
  * Action items with assigned owners and deadlines (e.g., enforce MFA across legacy portals, implement egress traffic filtering).

---

## 5. Digital Forensics & Evidence Handling

When an incident involves potential computer crimes or regulatory investigations, all technical evidence must be handled with rigorous forensic discipline to remain legally admissible in a court of law.

```
+-----------------------------------------------------------------------------------------+
|                              ORDER OF VOLATILITY (RFC 3227)                             |
|                                                                                         |
|  HIGHEST VOLATILITY  1. CPU Registers & Cache (Nanoseconds)                             |
|          |           2. Routing Tables, ARP Cache, Process Table, Kernel Memory         |
|          |           3. System Memory (RAM) (Lost on power loss)                        |
|          |           4. Temporary File Systems & Swap Space                             |
|          |           5. Non-Volatile Storage (Hard Drives, SSDs)                        |
|          v           6. Remote Logging Data (SIEM, Syslog)                              |
|  LOWEST VOLATILITY   7. Physical Media, Backup Tapes & Optical Disks                    |
+-----------------------------------------------------------------------------------------+
```

### A. The Order of Volatility (RFC 3227)
Digital evidence degrades and disappears at different rates. Forensic examiners must acquire evidence in strict order from **most volatile** to **least volatile**:

1. **CPU Registers and Cache**: Disappears in nanoseconds; impossible to preserve without specialized hardware probes.
2. **Routing Table, ARP Table, Process Table, Kernel Memory**: Disappears immediately upon network disconnection or shutdown.
3. **System Memory (RAM)**: Holds encryption keys, unencrypted passwords, running malware code, and active socket connections.
4. **Temporary File Systems**: `/tmp`, Windows paging files (`pagefile.sys`), and swap space.
5. **Disk / Non-Volatile Storage**: Hard drives, SSDs, and storage arrays (persists through power cycles).
6. **Remote Logging Data**: Syslog servers, AWS CloudTrail, and SIEM logs.
7. **Physical Backups & Archival Media**: Backup tapes, optical discs, offline cold storage.

### B. Chain of Custody & Evidence Integrity

```mermaid
sequenceDiagram
    participant Analyst as Forensic Investigator
    participant Evidence as Disk / Memory Image
    participant Hash as Cryptographic Hash (SHA-256)
    participant Locker as Secure Evidence Locker
    participant Court as Court / Legal Proceeding

    Analyst->>Evidence: Bit-Stream Acquisition (dd / write-blocker)
    Analyst->>Hash: Generate Initial SHA-256 Hash
    Analyst->>Locker: Store Primary Image in Vault with Chain of Custody Form
    Note over Analyst,Locker: Form logs: Date, Time, Serial, Collector, Reason
    Analyst->>Evidence: Work ONLY on Forensic Copy (Never the Original)
    Analyst->>Court: Present Evidence + Matching SHA-256 Hash to Prove Zero Tampering
```

* **Bit-Stream Disk Image**: A bit-for-bit physical clone of the entire storage media, including unallocated space, slack space, and deleted file fragments (using tools like `dc3dd` or hardware write-blockers).
* **Cryptographic Hashing**:
  * An algorithm (`SHA-256` or `SHA-3`) is calculated across the raw evidence immediately upon collection.
  * When evidence is presented in court, the hash is re-calculated. If even 1 single bit has changed, the hash differs and the evidence is deemed contaminated.
* **Chain of Custody Documentation**:
  * A tamper-evident log sheet detailing:
    * Exact timestamp and location of seizure.
    * Identifying serial numbers, MAC addresses, and model names.
    * Full name, title, and signature of the seizing investigator.
    * Purpose of transfer whenever evidence moves from secure storage to analysis.

### C. Legal Coordination & Breach Disclosure Laws

| Regulation / Body | Required Reporting Window | Trigger Conditions | Penalties / Consequences |
| :--- | :--- | :--- | :--- |
| **GDPR (EU)** | **Within 72 Hours** | Breach involving personal data of EU residents resulting in risk to rights and freedoms. | Up to €20M or 4% of global annual turnover. |
| **SEC Form 8-K (US)** | **Within 4 Business Days** | Material cybersecurity incident impacting publicly traded companies. | SEC enforcement actions, shareholder lawsuits. |
| **HIPAA (US)** | **Within 60 Calendar Days** (or 24h if > 500 records) | Unauthorized acquisition or disclosure of Protected Health Information (PHI). | Substantial civil monetary penalties per violation. |
| **Law Enforcement (FBI / CISA)** | **As soon as practical** | Critical infrastructure disruption, state-sponsored intrusion, major ransomware extortion. | Access to federal threat intelligence and mutual legal assistance treaties (MLAT). |

---

## 6. Cloud & DevOps Incident Response Playbooks

In modern cloud-native environments, incident response relies heavily on programmatic API automation and Infrastructure-as-Code.

### Playbook A: Compromised Cloud IAM Access Key

When an engineer accidentally commits an active AWS Access Key to a public GitHub repository:

```bash
# STEP 1: Immediately Deactivate the Compromised Key
aws iam update-access-key \
    --user-name dev-deployer \
    --access-key-id AKIAIOSFODNN7EXAMPLE \
    --status Inactive

# STEP 2: Attach an Explicit Deny-All Inline Policy to Stop Active Sessions
cat << 'EOF' > /tmp/deny-policy.json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
EOF

aws iam put-user-policy \
    --user-name dev-deployer \
    --policy-name EmergencyQuarantine \
    --policy-document file:///tmp/deny-policy.json

# STEP 3: Revoke Temporary STS Sessions
aws iam put-user-permissions-boundary \
    --user-name dev-deployer \
    --permissions-boundary-arn arn:aws:iam::aws:policy/AdministratorAccess # (Or specific containment boundary)

# STEP 4: Query CloudTrail for Unauthorized Actions in the Last 24 Hours
aws cloudtrail lookup-events \
    --lookup-attributes AttributeKey=AccessKeyId,AttributeValue=AKIAIOSFODNN7EXAMPLE \
    --start-time $(date -u -d '24 hours ago' +%s) \
    --output json | jq '.Events[] | {EventTime, EventName, SourceIPAddress: .SourceIPAddress, Resources}'
```

---

### Playbook B: Compromised Kubernetes Pod Containment

When a containerized workload in a Kubernetes cluster is compromised by a web shell:

```mermaid
graph LR
    Pod[Compromised Pod: payment-service-xyz] -->|Label Quarantine| Isolation[NetworkPolicy: Deny All Ingress & Egress]
    Isolation --> Dump[Capture Memory & Core Dump]
    Dump --> Cordon[Cordon & Drain Node]
    Cordon --> Terminate[Delete Pod & Spin Clean Replica]
```

```yaml
# Step 1: Apply Emergency Quarantine NetworkPolicy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: quarantine-isolated-pod
  namespace: production
spec:
  podSelector:
    matchLabels:
      quarantine: "true"
  policyTypes:
  - Ingress
  - Egress
  # Empty ingress and egress blocks all network traffic to and from the pod
```

```bash
# Step 2: Label the suspect pod to trigger immediate network isolation
kubectl label pod payment-service-789abc-xyz quarantine=true -n production --overwrite

# Step 3: Capture container filesystem snapshot
kubectl exec payment-service-789abc-xyz -n production -- tar -czf - /tmp /var/log > /forensics/pod_evidence.tar.gz

# Step 4: Cordon the underlying Kubernetes node to prevent scheduling new workloads
kubectl cordon node-worker-pool-04

# Step 5: Terminate the compromised pod
kubectl delete pod payment-service-789abc-xyz -n production --grace-period=0 --force
```

---

## 7. Linux System Administrator Incident Triage Cheat Sheet

When responding to a live Linux system suspected of compromise, execute these non-destructive triage commands in order:

### 1. Network Activity & Socket Connections
```bash
# List all active listening ports and established connections with Process IDs
ss -tulpen
ss -antp | grep -E 'ESTAB|LISTEN'

# Identify processes communicating with foreign IP addresses
lsof -i -P -n | grep ESTABLISHED
```

### 2. Process Analysis & Inspection
```bash
# Tree view of all running processes with full arguments
ps auxf

# Inspect executable path and deleted binary hooks for a suspect PID
ls -la /proc/<PID>/exe
cat /proc/<PID>/cmdline | tr '\0' ' ' ; echo
ls -la /proc/<PID>/cwd
```

### 3. User Logins & Account Persistence
```bash
# Check currently logged in users
w
who -u

# Check recent login history and failed attempts
last -n 20
lastb -n 20 # Requires root; shows failed login attempts

# Check for unauthorized accounts with UID 0 (root privileges)
awk -F: '($3 == "0") {print $1}' /etc/passwd

# Check for unauthorized SSH keys
cat /root/.ssh/authorized_keys
cat /home/*/.ssh/authorized_keys
```

### 4. Scheduled Tasks & Persistence Hooks
```bash
# Check system and user crontabs
crontab -l
ls -la /etc/cron* /etc/crontab /var/spool/cron/crontabs

# Check systemd timers (modern persistence mechanism)
systemctl list-timers --all
```

### 5. File Integrity & Suspicious Directories
```bash
# Search for files modified in the last 24 hours in sensitive locations
find /etc /bin /sbin /usr/bin /tmp /var/tmp -mtime -1 -type f 2>/dev/null

# Identify hidden files in temporary staging directories
ls -la /tmp /var/tmp /dev/shm
```

---

## 8. Summary & Key Certification / Exam Review

| Key Term / Question | Correct Answer / Takeaway |
| :--- | :--- |
| **Security Incident vs. Event** | An **event** is any observable change on a system (login, file open). An **incident** is an adverse event that threatens the CIA triad. |
| **Incident Response Policy (IRP)** | Defines actions post-breach, mandates preparation, and specifies **who determines and declares** an incident. |
| **CIRT / CSIRT** | Multidisciplinary task force created to manage incident analysis, response, reporting, and documentation under governance guidelines. |
| **Computer Crime** | Criminal act using a computer as the source or target rather than an individual (e.g., unauthorized access, malware propagation, classified data theft). |
| **Rebooting a compromised system?** | **NO!** Violates RFC 3227 Order of Volatility; wipes system RAM, destroying active connections, keys, and injected code. |
| **Order of Volatility (Top 3)** | 1. CPU Cache/Registers $\rightarrow$ 2. Routing/Process Tables $\rightarrow$ 3. RAM. |
| **Bit-Stream Disk Image** | Bit-for-bit physical copy of disk including unallocated space; validated via cryptographic SHA-256 hash. |
| **Chain of Custody** | Continuous, tamper-evident log accounting for who possessed the digital evidence, when, and for what purpose. |
| **NIST 6-Phase Lifecycle** | **P**reparation $\rightarrow$ **I**dentification $\rightarrow$ **C**ontainment $\rightarrow$ **E**radication $\rightarrow$ **R**ecovery $\rightarrow$ **L**essons Learned. |
