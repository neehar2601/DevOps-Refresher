# Comprehensive Network Security, Firewalls & VPNs Guide

> 📘 **Quick Navigation**:
> * 🟢 **[Networking Basics & Introduction](networking-basics.md)** — Core concepts, human analogies, network scopes.
> * 🌐 **[Networking Protocols & Transmission](networking-protocols.md)** — Unicast/Broadcast/Multicast, HTTP/HTTPS, DNS, DHCP, BGP.
> * 🧱 **[Network Components & Architecture](networking-components-architecture.md)** — Switches, CAM tables, Routers, Topologies, Cloud VPC.
> * 🔢 **[IP Addressing, Subnetting & NAT](networking-ip-addressing.md)** — IPv4/IPv6, CIDR notation, 5 Cloud Reserved IPs, NAT/PAT.
> * 🛠️ **[Networking Tools & CLI Commands](Networking/networking-tools-guide.md)** — `ip`, `ping`, `traceroute`, `ss`, `dig`, `tcpdump`.
> * ⚡ **[Networking Interview Cheat Sheet](networking-cheatsheet.md)** — Master single-page quick reference.

---

## 1. Stateful vs. Stateless Firewalls

Firewalls inspect and filter incoming and outgoing network traffic based on established security rules. The fundamental classification of firewalls lies in how they handle **connection state tracking**:

```
Stateless Firewall:   [Packet] ---> [Check Rules (IP / Port / Protocol)] ---> Allow or Drop (Ignores connection history)
Stateful Firewall:    [Packet] ---> [Check Connection State Table] --------> Fast-Track if ESTABLISHED
                                           | (New Connection)
                                           v
                                    [Check Rule Table] --------------> Allow & Record in State Table
```

### A. Detailed Comparison Matrix

| Feature | Stateless Firewall | Stateful Firewall |
| :--- | :--- | :--- |
| **Connection Tracking** | None. Evaluates each packet in complete isolation. | Tracks active connection states in a **State Table** (TCP 3-way handshake, sequence numbers). |
| **Return Traffic** | **Must explicitly write rules for BOTH inbound and outbound directions**. | **Automatic**. If outbound traffic is allowed, return response traffic is automatically allowed. |
| **Performance Impact** | Ultra-high processing speed (low CPU/memory usage). | Requires RAM to maintain connection state tables. |
| **Security Level** | Lower (vulnerable to IP spoofing and ACK scanning). | High (prevents unauthorized inbound connection attempts). |
| **Inspection Layers** | Layers 3 & 4 (IP, Port, Protocol). | Layers 3, 4, and partial Layer 5. |
| **Cloud Analogy** | **AWS Network ACL (NACL)** | **AWS Security Group (SG)** |

---

### B. Cloud Implementation: AWS Security Groups vs. AWS Network ACLs

In cloud infrastructure (AWS VPC), stateful and stateless firewalls are deployed in tandem:

```
+-------------------------------------------------------------------------------+
| AWS VPC                                                                       |
|   [ Internet ]                                                                |
|        |                                                                      |
|        v                                                                      |
|   +-----------------------------------------------------------------------+   |
|   | Subnet Boundary: Network ACL (Stateless)                              |   |
|   |  - Evaluates Inbound Rules (e.g. Allow 443 from 0.0.0.0/0)           |   |
|   |  - Evaluates Outbound Rules (e.g. Allow Ephemeral Ports 1024-65535)   |   |
|   +-----------------------------------------------------------------------+   |
|        |                                                                      |
|        v                                                                      |
|   +-----------------------------------------------------------------------+   |
|   | Instance Boundary: Security Group (Stateful)                          |   |
|   |  - Inbound Rule: Allow TCP 443 from 0.0.0.0/0                        |   |
|   |  - Return traffic automatically permitted                             |   |
|   |  [ EC2 Instance / Application Pod ]                                   |   |
|   +-----------------------------------------------------------------------+   |
+-------------------------------------------------------------------------------+
```

---

## 2. Web Application Firewalls (WAF) & Layer 7 Security

Standard stateful/stateless firewalls operate at Layers 3 and 4 (filtering by IP address and port number). However, modern attacks occur at **Layer 7 (Application Layer)** inside valid HTTP/HTTPS payloads on standard ports (`80`/`443`).

```
Layer 3/4 Firewall:   Inspects IP: 192.168.1.50 -> Port: 443  (Allowed)
Layer 7 WAF:           Inspects HTTP Payload: GET /user?id=1 OR 1=1 -- (BLOCKED: SQL Injection detected!)
```

### Key Features of a WAF (Layer 7 Firewall)
1. **OWASP Top 10 Protection**: Detects and blocks SQL Injection (SQLi), Cross-Site Scripting (XSS), Remote Code Execution (RCE), and Cross-Site Request Forgery (CSRF).
2. **HTTP Payload Inspection**: Inspects HTTP headers, cookies, URL query parameters, and request body payload strings.
3. **Rate Limiting & DDoS Mitigation**: Restricts request rates per client IP address to prevent brute-force attacks and Layer 7 HTTP flood attacks.
4. **Virtual Patching**: Allows security teams to write custom WAF rules to block newly disclosed zero-day vulnerabilities instantly before developers update backend application code.

---

## 3. Virtual Private Networks (VPNs) & Tunneling Protocols

A **Virtual Private Network (VPN)** establishes an encrypted, secure tunnel over an untrusted public network (like the Internet), allowing remote users or branch offices to safely access private internal networks.

```
[ Remote Worker / Client ] === Encrypted IPsec / WireGuard Tunnel ===> [ Corporate VPN Gateway ] ---> [ Private Internal LAN ]
(Public IP: 203.0.113.10)              (Over Public Internet)            (Public IP: 198.51.100.5)        (Private IP: 10.0.0.0/16)
```

### A. Core VPN Architectures
* **Remote Access VPN**: Connects individual user endpoints (laptops, mobile devices) to a private enterprise network using VPN client software.
* **Site-to-Site VPN**: Interconnects two entire static networks (e.g., connecting a physical corporate datacenter to an AWS Cloud VPC).

---

### B. Standard VPN & Tunneling Protocols

| Protocol | OSI Layer | Encryption / Security | Pros & Cons | Primary Use Case |
| :--- | :---: | :--- | :--- | :--- |
| **IPsec** (IP Security) | **Layer 3** | High (AES-256, IKEv2, AH/ESP) | *Pros*: Enterprise standard, highly secure. *Cons*: Complex setup. | Site-to-Site VPNs, Cloud-to-On-Prem connectivity. |
| **WireGuard** | **Layer 3** | High (ChaCha20, Poly1305, Noise Framework) | *Pros*: Modern, ultra-lightweight (~4,000 lines of code), extremely fast. | Modern Remote Access VPNs, Mesh networking (Tailscale/Netmaker). |
| **OpenVPN** | **Layer 4 / TLS** | High (OpenSSL, AES, RSA) | *Pros*: Runs over standard UDP/TCP ports (bypasses firewalls). *Cons*: Slower performance. | Remote User Access VPNs. |
| **GRE** (Generic Routing Encapsulation) | **Layer 3** | **None** (Plaintext encapsulation) | *Pros*: Encapsulates routing protocols (multicast/OSPF). *Cons*: No security/encryption by default. | Router-to-router tunnel encapsulation (often combined with IPsec). |

---

## 4. Zero Trust Architecture & Modern Network Access

Traditional perimeter security relies on the *"Castle and Moat"* model (once inside the internal network, everything is trusted). **Zero Trust Architecture (ZTA)** operates under the core principle: **"Never Trust, Always Verify."**

### Core Pillars of Zero Trust Networking
1. **Micro-Segmentation**: Dividing network workloads into granular isolated segments (e.g., isolating database pods so web servers can only talk to specific database ports).
2. **mTLS (Mutual TLS Authentication)**: Both the client and server present and validate X.509 digital certificates to establish encrypted, identity-authenticated communication (extensively used in Service Meshes like Istio/Linkerd).
3. **Identity-Aware Proxies (IAP)**: Replaces traditional client VPNs by authenticating user identity, device health, and context at the application layer before granting access to internal applications (e.g., Google BeyondCorp, Cloudflare Access).

---


## 5. Identity, Authentication & Access Control (IAM)

Controlling network and system access requires robust identity governance, multi-factor verification, and structured authorization models.

### A. Identity, Claims & The 50% Rule
* **Subject vs. Object**: A **Subject** is an active entity requesting access (user, service account, API client). An **Object** is the passive target resource (file, database, endpoint).
* **Identity Uniqueness**: An identity is a symbolic representation of the subject. It must be strictly **unique** across the directory (e.g. `employee2345`).
* **The 50% Rule**: Predictable usernames (e.g. `sfarrell` and deducing `cfarrell` for family/team members) give attackers 50% of the credentials needed for account takeover.
* **Claim vs. Authentication**: A **Claim** is an unverified assertion of identity (*"sfarrell, open up!"*). **Authentication (AuthN)** is the mathematical verification of that claim via credentials.

### B. The 5 Authentication Factors & Multi-Factor Authentication (MFA)
1. **Something You Know**: Password, passphrase, security questions, PIN.
2. **Something You Have**: Smart cards with chips, Common Access Cards (CAC), RSA SecurID fobs, SMS/OTP codes (verifies device possession), digital certificates.
3. **Something You Are**: Biometrics (Fingerprint, Face geometry, Iris pattern, Retina blood vessels).
4. **Somewhere You Are**: Geolocation, IP address boundaries, impossible travel detection.
5. **Something You Do**: Behavioral biometrics (Gait analysis on CCTV, typing cadence, signature dynamics).

> 💡 **MFA Security Rule**: Requiring 20 items from the *same factor* (e.g., password + security questions + PIN) is **still single-factor**. True MFA mandates items from $\\ge 2$ different categories (e.g., Bank card [have] + PIN [know]). MFA is superior to biometrics alone because biometric templates stored in software databases can be breached, whereas multi-factor attacks require two completely distinct physical attack vectors.

### C. Account Governance & The Detective Rule
* **Accountability**: Every event must trace back to a specific individual. Shared accounts shatter accountability (*"If 4 admins share a password, the detective cannot prove who altered the database"*).
* **Multiple Accounts for Privileged Users**: Administrators must use a standard user account for email/browsing and elevate only via `sudo` or `runas` with a separate admin account.
* **Generic & Service Accounts**: Disable generic names (`Administrator`, `Guest`). Service accounts must use automated rotation (Group Managed Service Accounts - gMSA) instead of static non-expiring passwords.

### D. Single Sign-On (SSO), Kerberos & Federation
* **LDAP (Port 389, plaintext)** vs. **LDAPS (Port 636, encrypted with TLS)**.
* **Kerberos**: Built on symmetric cryptography, the **Key Distribution Center (KDC)**, Ticket Granting Tickets (TGT), and Service Tickets. Enforces $\\le 5$ minute clock skew to prevent replay attacks.
* **Federation**: Identity Provider (IdP) authenticates subjects; Service Provider (SP) trusts the IdP without seeing passwords. Protocols: **SAML** (XML authN/authZ), **OpenID** (authN), **OAuth 2.0** (authZ).

### E. The 5 Access Control Models & Implicit Deny
* **Implicit Deny**: If an Access Control List (ACL) has no rule explicitly allowing access, access is **DENIED** (*"If mom didn't say yes, the answer is no"*).
* **Least Privilege**: Grant users the minimum access required to execute their role; audit regularly to eliminate **privilege creep**.
* **The 5 Access Control Models**:
  1. **MAC (Mandatory Access Control)**: Labels and clearances (Top Secret); enforced by OS; zero human discretion.
  2. **DAC (Discretionary Access Control)**: Data owner decides permissions on the ACL.
  3. **RBAC (Role-Based Access Control)**: Permissions assigned to job roles via user groups (e.g., Developers, Marketing).
  4. **RuBAC (Rule-Based Access Control)**: Sequentially evaluated rules (first match wins; firewalls).
  5. **ABAC (Attribute-Based Access Control)**: Dynamic attributes (user department, location, device health) for conditional Zero Trust access.

---

## 6. Wireless Network Security, Encryption & AAA Protocols

Because radio frequency (RF) networks broadcast over unguided open air, anyone within transmission range can intercept frames. Securing wireless infrastructure requires rigorous Layer-2 cryptography, robust authentication, and physical RF confinement.

### A. Open Wi-Fi, Hotspots & Captive Portals
* **Open Networks (Zero Encryption)**: Public Wi-Fi hotspots in coffee shops or airports transmit Layer-2 frames in plaintext. Any adjacent user running `airodump-ng` or Wireshark can inspect unencrypted HTTP traffic, DNS queries, and session tokens.
* **Captive Portals**: Web gateways that intercept initial HTTP/DNS requests and redirect the client to a splash page before granting route authorization.
  * **Function**: Enforces user acceptance of an **Acceptable Use Policy (AUP)** / Terms of Service (TOS) to protect the network provider from legal liability for guest misconduct.
  * **Security Limitation**: A captive portal *does not encrypt RF traffic*. It only controls gateway routing.
* **Mandatory Defense**: Always tunnel client traffic through an encrypted **VPN (WireGuard, IPsec, OpenVPN)** when utilizing untrusted open Wi-Fi.

---

### B. Evolution of 802.11 Encryption Protocols: WEP to WPA3

```
+---------------+------------------------+--------------------------+-------------------------------------+
| Standard      | Cipher & Integrity     | Handshake / Auth         | Security Status & Vulnerabilities   |
+---------------+------------------------+--------------------------+-------------------------------------+
| WEP (1997)    | RC4 + CRC-32           | Open / Shared Key        | CRITICALLY BROKEN: 24-bit IV reuse  |
|               | (40/104-bit static)    | (Challenge-Response)     | cracked in < 60s via aircrack-ng.   |
+---------------+------------------------+--------------------------+-------------------------------------+
| WPA (2003)    | RC4 with TKIP          | 4-Way EAPOL Handshake    | DEPRECATED: Interim WEP hardware fix|
|               | + Michael MIC (64-bit) | (Pre-Shared Key)         | TKIP & Michael collision attacks.   |
+---------------+------------------------+--------------------------+-------------------------------------+
| WPA2 (2004)   | AES + CCMP             | 4-Way EAPOL Handshake    | INDUSTRY BASELINE: Robust AES-128.  |
| (802.11i)     | (128-bit Block Cipher) | (Pre-Shared Key / 802.1X)| Susceptible to offline dictionary   |
|               |                        |                          | brute force if 4-way handshake snft.|
+---------------+------------------------+--------------------------+-------------------------------------+
| WPA3 (2018)   | AES-GCM (128-bit) or   | SAE (Dragonfly Handshake)| MAXIMUM SECURITY: Immune to offline |
|               | GCMP-256 (192-bit)     | + Perfect Forward        | dictionary attacks; forward secrecy |
|               | + BIP-GMAC-256         |   Secrecy (PFS)          | protects past sessions.             |
+---------------+------------------------+--------------------------+-------------------------------------+
```

* **WEP Flaw**: Reused a short 24-bit Initialization Vector (IV) in plaintext. In high-traffic networks, IV collisions occur rapidly, enabling attackers to mathematically reconstruct the master key.
* **WPA2 (AES-CCMP)**: Replaced RC4 with the **Advanced Encryption Standard (AES)** in **CCMP** (Counter Mode Cipher Block Chaining Message Authentication Code Protocol). Guarantees both data confidentiality and message integrity.
* **WPA3 Innovations**:
  * **SAE (Simultaneous Authentication of Equals)**: Replaces vulnerable PSK handshakes with a zero-knowledge proof (Dragonfly). Even if a user configures a weak password, attackers cannot execute offline dictionary attacks.
  * **Perfect Forward Secrecy (PFS)**: Generates a unique ephemeral key per session. Compromising a future key cannot decrypt previously recorded network traffic.

---

### C. Wi-Fi Authentication Modes: Personal (PSK) vs. Enterprise (802.1X)

1. **WPA-Personal (WPA-PSK)**:
   * Uses a single **Pre-Shared Key (passphrase)** shared across all endpoints.
   * **Limitation**: Zero individual accountability. If an employee departs or a passphrase is leaked, the key must be manually changed across *every connected device*.
2. **WPA-Enterprise (IEEE 802.1X PNAC)**:
   * Employs **Port-Based Network Access Control (PNAC)** combined with a central AAA server.
   * **The 3 Entities**:
     * **Supplicant**: Client software requesting wireless network access.
     * **Authenticator**: Wireless Access Point (WAP) gating network traffic.
     * **Authentication Server**: Central RADIUS server backed by an enterprise directory (Active Directory / LDAP).
   * **Advantage**: Every user authenticates with individual credentials or an X.509 client certificate. The RADIUS server provisions unique per-session dynamic keys (PMK/PTK). Terminating a user in Active Directory immediately revokes their Wi-Fi access.

---

### D. Centralized AAA Framework: RADIUS vs. TACACS+

**AAA** defines the core triad of enterprise identity governance:
* **Authentication**: Proving the identity of the user or machine (*"Who are you?"*).
* **Authorization**: Determining permissions, assigned VLANs, and firewall ACLs (*"What can you access?"*).
* **Accounting**: Auditing session duration, login timestamps, and byte counts (*"What did you do?"*).

| Parameter | RADIUS (Remote Authentication Dial-In) | TACACS+ (Terminal Access Controller) |
| :--- | :--- | :--- |
| **Origin / RFC** | Open IETF Standard (RFC 2865 / 2866) | Cisco Proprietary (RFC 8907) |
| **Transport & Port** | **UDP Ports 1812** (AuthN/AuthZ) & **1813** (Acct) | **TCP Port 49** (Connection-oriented) |
| **Architecture** | Combines Authentication & Authorization | **Separates AuthN, AuthZ, and Accounting** |
| **Packet Encryption**| Encrypts *only the password field* (headers plaintext) | Encrypts the **entire payload body** |
| **Primary Domain** | **Wi-Fi 802.1X, VPNs**, 802.1X Ethernet switches | **Router/Switch Network Device Administration** |

---

### E. Physical RF Containment & Transmit Power Tuning

* **Transmit Power (Tx / EIRP) Containment**:
  * Unchecked high-power Wi-Fi broadcasts penetrate exterior walls, bleeding signals into parking lots and public roadways.
  * **Threat Vector**: Wardriving adversaries sit in parked cars outside corporate buildings, capturing 802.11 handshakes without entering physical security perimeters.
  * **Remediation**: Tune AP Equivalent Isotropically Radiated Power (EIRP) so signal levels drop below $-75\text{ dBm}$ at exterior building walls, containing the RF perimeter.
* **Antenna Engineering**:
  * **Omnidirectional (Dipole)**: Distributes RF energy in a uniform 360-degree doughnut pattern; ideal for indoor central ceilings.
  * **Directional (Yagi / Patch / Parabolic)**: Concentrates RF energy into a focused, narrow beam; ideal for point-to-point building links and long corridors without leaking energy through lateral walls.

---

## Next Recommended Guides
* 🟢 **[Networking Basics & Introduction](networking-basics.md)**
* 🌐 **[Networking Protocols & Transmission](networking-protocols.md)**
* 🧱 **[Network Components & Architecture Guide](networking-components-architecture.md)**
* 🔢 **[IP Addressing, Subnetting & NAT Guide](networking-ip-addressing.md)**
* 🛠️ **[Networking Tools & CLI Commands Guide](Networking/networking-tools-guide.md)**
* ⚡ **[Networking Interview Cheat Sheet](networking-cheatsheet.md)**
