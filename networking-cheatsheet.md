# DevOps & SysAdmin Networking Interview Cheat Sheet

> ⚡ **Master Quick Reference Guide**: Use this single page for last-minute interview prep, quick port lookups, command syntax, and elevator-pitch answers.

---

## 📌 Master Networking Documentation Index

| Guide | Description | Key Focus Topics |
| :--- | :--- | :--- |
| 🟢 **[Networking Basics & Intro](networking-basics.md)** | Core concepts & introduction | 4 Pillars matrix, Human vs Network analogy, Scopes (LAN/MAN/WAN), MAC evolution (Token Ring vs CSMA/CD). |
| 🌐 **[Networking Protocols](networking-protocols.md)** | Application, routing & management protocols | Unicast/Broadcast/Multicast, HTTP/HTTPS, DNS, DHCP, SNMP, BGP (Autonomous Systems), OSPF, SSH. |
| 🧱 **[Network Components & Architecture](networking-components-architecture.md)** | Hardware, topologies & cloud networks | Hub vs Switch vs Router matrix, CAM tables, Port Mirroring, Promiscuous Mode, Topologies, AWS VPC topology. |
| 🔒 **[Network Security & Firewalls](networking-security-firewalls.md)** | Network security, firewalls & VPNs | Stateful vs Stateless firewalls, AWS SGs vs NACLs, WAF (Layer 7), IPsec/WireGuard VPNs, Zero Trust. |
| 🔢 **[IP Addressing & Subnetting](networking-ip-addressing.md)** | Addressing, subnets, reserved IPs & NAT | IPv4 vs IPv6, 5 Cloud Reserved IPs (AWS VPC), Router IP assignment (`.1`), CIDR magic numbers, NAT/PAT. |
| 🧱 **[OSI & TCP/IP Models](networking-osi-tcpip.md)** | Architecture & traffic flow | 7 OSI layers, Encapsulation/Decapsulation, Browser URL packet flow, TCP vs UDP, TCP 3-Way handshake & Flags. |
| 🛠️ **[Networking Tools Guide](Networking/networking-tools-guide.md)** | CLI tools & troubleshooting | `ip`, `ping`, `traceroute`, `dig`, `ss`, `netstat`, `nmap`, `tcpdump`, `curl`, `ethtool`. |

---

## 1. Top 25 Must-Know Port Numbers

```
+------+----------+-------------------------------------------------------+
| Port | Protocol | Service / Description                                 |
+------+----------+-------------------------------------------------------+
| 20/21| FTP      | File Transfer Protocol (Data/Control)                 |
| 22   | SSH / SFTP| Secure Shell / Secure File Transfer                   |
| 23   | Telnet   | Unencrypted text terminal (Insecure)                  |
| 25   | SMTP     | Simple Mail Transfer Protocol (Server-to-Server)      |
| 49   | TACACS+  | Cisco Terminal Access Controller (AAA Device Admin)   |
| 53   | DNS      | Domain Name System (UDP for queries, TCP for transfer)|
| 67/68| DHCP     | Dynamic Host Configuration Protocol (Server/Client)   |
| 80   | HTTP     | Hypertext Transfer Protocol                           |
| 123  | NTP      | Network Time Protocol (System clock sync)             |
| 143  | IMAP     | Internet Message Access Protocol (Plaintext)          |
| 161/2| SNMP     | Simple Network Management Protocol (Poll/Traps)       |
| 179  | BGP      | Border Gateway Protocol (Inter-AS Routing)            |
| 389  | LDAP     | Lightweight Directory Access Protocol                 |
| 443  | HTTPS    | HTTP Secure over TLS/SSL                              |
| 465  | SMTPS    | Secure SMTP over TLS                                  |
| 500  | IPsec    | Internet Key Exchange (IKE for VPNs)                  |
| 587  | SMTP     | Mail Submission (with STARTTLS)                       |
| 636  | LDAPS    | Secure LDAP over TLS                                  |
| 993  | IMAPS    | Secure IMAP over TLS                                  |
| 995  | POP3S    | Secure POP3 over TLS                                  |
| 1433 | MSSQL    | Microsoft SQL Server Database                         |
| 1812 | RADIUS   | Remote Authentication Dial-In (AuthN / AuthZ)         |
| 1813 | RADIUS-Ac| RADIUS Accounting Traffic                             |
| 3306 | MySQL    | MySQL / MariaDB Database                              |
| 3389 | RDP      | Remote Desktop Protocol (Windows)                     |
| 5432 | PostgreSQL| PostgreSQL Database                                  |
| 6379 | Redis    | Redis In-Memory Data Store                            |
| 8080 | HTTP-Alt | Alternate HTTP / Tomcat / Jenkins / Proxy             |
| 8443 | HTTPS-Alt| Alternate HTTPS / Kubernetes API Server               |
| 9090 | Prometheus| Prometheus Monitoring Server Metrics                  |
+------+----------+-------------------------------------------------------+
```

---

## 2. HTTP Response Status Codes Quick Table

| Code Range | Category | Key Status Codes to Memorize |
| :---: | :--- | :--- |
| **`1xx`** | Informational | `100` Continue, `101` Switching Protocols (WebSockets) |
| **`2xx`** | Success | `200` OK, `201` Created, `204` No Content |
| **`3xx`** | Redirection | `301` Moved Permanently, `302` Found (Temp Redirect), `304` Not Modified (Cached) |
| **`4xx`** | Client Error | `400` Bad Request, `401` Unauthorized, `403` Forbidden, `404` Not Found, `408` Request Timeout, `429` Too Many Requests |
| **`5xx`** | Server Error | `500` Internal Server Error, `502` Bad Gateway, `503` Service Unavailable, `504` Gateway Timeout |

---

## 3. Subnetting & CIDR Quick Cheat Sheet

$$\text{Standard Usable Hosts} = 2^{(32 - \text{CIDR})} - 2 \quad \vert \quad \text{AWS Cloud Usable Hosts} = 2^{(32 - \text{CIDR})} - 5$$

```
+------+-------------------+------------+----------------+----------------+-----------+---------------------------------------+
| CIDR | Subnet Mask       | Block Size | Std Usable     | AWS Usable     | Router IP | Primary Use Case                      |
+------+-------------------+------------+----------------+----------------+-----------+---------------------------------------+
| /32  | 255.255.255.255   | 1          | 1              | 0              | N/A       | Single host IP / Firewall rule        |
| /30  | 255.255.255.252   | 4          | 2              | 0              | .1        | Point-to-point router link / VPN      |
| /28  | 255.255.255.240   | 16         | 14             | 11             | .1        | Database cluster subnet               |
| /26  | 255.255.255.192   | 64         | 62             | 59             | .1        | Small application subnet              |
| /24  | 255.255.255.0     | 256        | 254            | 251            | .1        | Standard office / AWS VPC subnet      |
| /16  | 255.255.0.0       | 65,536     | 65,534         | 65,531         | .1        | Cloud VPC CIDR (e.g. AWS 10.0.0.0/16) |
+------+-------------------+------------+----------------+----------------+-----------+---------------------------------------+
```

---

## 4. Top Linux CLI Commands Quick Reference

```bash
# IP & Interface Configuration
ip addr show                        # View all IP addresses (modern ifconfig)
ip link set eth0 up/down            # Enable or disable an interface
ip route show                       # Display kernel routing table

# Diagnostic & Connectivity
ping -c 4 8.8.8.8                   # Send ICMP echo requests
traceroute google.com               # Trace hop-by-hop packet path (ICMP/UDP)
mtr google.com                      # Real-time traceroute + ping stats combined

# Socket & Port Monitoring
ss -tulpn                           # List all listening TCP/UDP ports with PIDs
netstat -tulpn                      # Legacy listening ports command
lsof -i :8080                       # Find which process is listening on port 8080

# DNS Inspection
dig +short A google.com             # Quick DNS A-record lookup
dig @8.8.8.8 google.com MX          # Query specific DNS server for MX records
nslookup google.com                 # Quick DNS lookup tool

# Packet Analysis & Security
tcpdump -i eth0 port 80 -n          # Capture raw HTTP packets on eth0 without DNS resolution
nmap -sV -p 1-1000 192.168.1.1      # Scan open ports and detect service versions
curl -Iv https://example.com        # Inspect HTTP response headers and SSL handshake details
```

---

## 5. Rapid-Fire Interview Questions & Answers

### Q1: What happens if two devices on a LAN have the same IP address?
> **Answer**: An IP address conflict occurs. Operating systems trigger Gratuitous ARP warnings. Packets destined for that IP are intermittently routed to both devices based on which ARP response reached the switch MAC table last, causing dropped connections and unstable network behavior.

### Q2: What is the difference between `502 Bad Gateway` and `504 Gateway Timeout`?
> **Answer**: 
> * **502 Bad Gateway**: The gateway/reverse proxy (e.g., NGINX) received an *invalid response* or connection refused from the upstream application server.
> * **504 Gateway Timeout**: The gateway/reverse proxy did not receive a response from the upstream application server within the configured timeout window.

### Q3: What is the difference between a Forward Proxy and a Reverse Proxy?
> **Answer**: 
> * **Forward Proxy**: Sits in front of **clients** to evaluate outbound traffic (used for client anonymity, content filtering, corporate security).
> * **Reverse Proxy**: Sits in front of **backend servers** to manage incoming traffic (used for load balancing, SSL termination, caching, routing).

### Q4: How does `traceroute` work under the hood?
> **Answer**: `traceroute` sends packets (UDP or ICMP) with incrementally increasing **TTL (Time to Live)** values starting at TTL=1. Each router along the path decrements TTL by 1. When TTL reaches 0, the router drops the packet and sends back an `ICMP Time Exceeded` message, revealing that router's IP address.

### Q5: What is the difference between Stateful and Stateless Firewalls?
> **Answer**: 
> * **Stateful Firewall**: Tracks active connection states (TCP 3-way handshake, state tables). Automatically allows return traffic for established outbound connections (e.g., AWS Security Groups).
> * **Stateless Firewall**: Evaluates each packet individually against rules without connection tracking. Return traffic must be explicitly allowed in rule tables (e.g., AWS Network ACLs).

---

## 6. Wireless Security & Architecture Quick Matrix

### A. Wi-Fi Encryption Protocols At-A-Glance

| Generation | Cipher & Mode | Key Exchange | Vulnerability Profile | Status |
| :--- | :--- | :--- | :--- | :--- |
| **WEP** (1997) | RC4 + CRC-32 | Static Key / Shared | 24-bit IV reuse collisions; cracked in < 60s via `aircrack-ng`. | ❌ **Broken** |
| **WPA** (2003) | RC4 + TKIP | 4-Way EAPOL (PSK) | Emergency WEP hardware fix; Michael MIC collision attacks. | ⚠️ **Deprecated** |
| **WPA2** (2004) | AES-128 + CCMP | 4-Way EAPOL (PSK) | Susceptible to offline dictionary attacks if 4-way handshake captured. | 🟢 **Baseline** |
| **WPA3** (2018) | AES-GCM / GCMP-256 | **SAE** (Dragonfly) | Zero-knowledge proof immune to dictionary attacks; **Perfect Forward Secrecy**. | 💎 **Recommended** |

---

### B. Core Architecture Decisions

* **Personal (PSK) vs. Enterprise (802.1X)**:
  * **Personal**: Single shared key for all clients. Zero individual accountability; impossible to revoke one employee without updating all endpoints.
  * **Enterprise**: IEEE 802.1X Port-Based Network Access Control. Client (*Supplicant*) connects to WAP (*Authenticator*) which verifies individual credentials/certificates against a central **RADIUS** (*Authentication Server*) querying LDAP/Active Directory. Dynamic per-session keys; instant account revocation.
* **Extender vs. Hardwired AP vs. Wireless Mesh**:
  * **Extender / Repeater**: Single-radio half-duplex relay cuts usable throughput by 50%; fragments SSIDs (`Office_EXT`).
  * **Hardwired AP**: Full Gigabit wire speed; requires Cat6 cabling; sticky client roaming without WLC.
  * **Wireless Mesh**: Single unified SSID; 802.11r/k/v fast seamless roaming; **dedicated backhaul radio** preserves 100% of client communication bandwidth!
* **Hidden SSIDs Myth**: Hiding beacon broadcasts provides **no real security**. Clients broadcast the hidden SSID in plaintext Probe Requests, and deauthentication attacks force re-association frames that reveal the SSID in Wireshark within seconds.

---

### C. Essential Linux Wireless Troubleshooting Commands

```bash
# Scan and list surrounding Wi-Fi networks with signal strength and security type
nmcli dev wifi list

# Associate and authenticate with a WPA2/WPA3 network
nmcli dev wifi connect "Company-5G" password "SuperSecretKey2026!"

# Display wireless interface link quality, Tx-Power, bit rate, and ESSID
iwconfig wlan0

# Low-level 802.11 kernel radio scan for nearby AP beacons and frequencies
sudo iw dev wlan0 scan | grep -E "SSID|signal|freq"

# Interactive ncurses wireless link quality, signal level, and noise monitor
sudo wavemon

# Launch background WPA/WPA2/WPA3 IEEE 802.1X enterprise authentication supplicant
sudo wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf
```

---

## Complete Guide Cross-References
* 🟢 **[Networking Basics & Introduction](networking-basics.md)**
* 🌐 **[Networking Protocols & Transmission](networking-protocols.md)**
* 🧱 **[Network Components & Architecture Guide](networking-components-architecture.md)**
* 🔒 **[Network Security & Firewalls Guide](networking-security-firewalls.md)**
* 🔢 **[IP Addressing & Subnetting Guide](networking-ip-addressing.md)**
* 🧱 **[OSI & TCP/IP Models & Packet Flow Guide](networking-osi-tcpip.md)**
* 🛠️ **[Networking Tools & CLI Commands Guide](Networking/networking-tools-guide.md)**

