# Comprehensive IP Addressing, Subnetting, CIDR & NAT Interview Guide

> 📘 **Quick Navigation**:
> * 🟢 **[Networking Basics & Introduction](networking-basics.md)** — Fundamentals, human analogies, components, network scopes, MAC history.
> * 🌐 **[Networking Protocols & Transmission](networking-protocols.md)** — Unicast/Broadcast/Multicast, HTTP/HTTPS, DNS, DHCP, BGP.
> * 🧱 **[Network Components & Architecture](networking-components-architecture.md)** — Switches, CAM tables, Routers, Topologies, Cloud VPC.
> * 🔒 **[Network Security & Firewalls](networking-security-firewalls.md)** — Stateful/Stateless firewalls, Security Groups, NACLs, VPNs.
> * 🛠️ **[Networking Tools & CLI Commands](Networking/networking-tools-guide.md)** — `ip`, `ping`, `traceroute`, `ss`, `dig`, `tcpdump`.
> * ⚡ **[Networking Interview Cheat Sheet](networking-cheatsheet.md)** — Quick reference tables, port lists, and top Q&As.

---

## 1. IPv4 vs IPv6 Quick Comparison

| Feature | IPv4 | IPv6 |
| :--- | :--- | :--- |
| **Address Length** | 32 bits (4 bytes) | 128 bits (16 bytes) |
| **Notation** | Dotted decimal (e.g., `192.168.1.1`) | Hexadecimal with colons (e.g., `2001:db8::1`) |
| **Address Space** | $\sim 4.3$ Billion ($2^{32}$) | $\sim 3.4 \times 10^{38}$ ($2^{128}$) |
| **Header Size** | Variable (20–60 bytes) | Fixed (40 bytes) for faster routing |
| **Configuration** | Manual or DHCP | SLAAC (Stateless Auto-config) or DHCPv6 |
| **NAT Requirement** | Heavily required (to conserve IPv4 space) | Not needed (every device can have a global IP) |
| **Broadcast Support** | Native Broadcast supported | Replaced entirely by **Multicast** & **Anycast** |

### IPv6 Address Scopes & Types
* **Global Unicast (`2000::/3`)**: Publicly routable on the global Internet (equivalent to IPv4 public IPs).
* **Link-Local (`fe80::/10`)**: Non-routable IP self-assigned to every IPv6 interface for single-link communication.
* **Unique Local (`fc00::/7`)**: Non-routable on the Internet; used for internal private networks (equivalent to IPv4 RFC 1918 private IPs).
* **Multicast (`ff00::/8`)**: Used to transmit packets to all nodes subscribed to a specific multicast group (replaces broadcast).
* **Loopback (`::1/128`)**: Localhost loopback interface (equivalent to IPv4 `127.0.0.1`).

---

## 2. IPv4 Classes & RFC 1918 Private Ranges

### A. Classful IPv4 Architecture (Legacy)

| Class | First Octet Range | Default Subnet Mask | Default CIDR | Purpose / Target |
| :---: | :---: | :---: | :---: | :--- |
| **A** | `1.0.0.0` to `126.255.255.255` | `255.0.0.0` | `/8` | Huge enterprises (16M hosts/net) |
| **B** | `128.0.0.0` to `191.255.255.255` | `255.255.0.0` | `/16` | Medium networks (65k hosts/net) |
| **C** | `192.0.0.0` to `223.255.255.255` | `255.255.255.0` | `/24` | Small networks (254 hosts/net) |
| **D** | `224.0.0.0` to `239.255.255.255` | N/A | N/A | Multicast Groups |
| **E** | `240.0.0.0` to `255.255.255.255` | N/A | N/A | Experimental / Research |

---

### B. RFC 1918 Private IP Ranges (Crucial for Interviews!)
Private IP addresses are **non-routable on the public Internet**. Routers automatically drop private IP packets unless NAT is used.

```
+------------------+------------------------------+---------------+-------------------+
| Private Block    | IP Range                     | Default CIDR  | Total Addresses   |
+------------------+------------------------------+---------------+-------------------+
| Class A Private  | 10.0.0.0 - 10.255.255.255    | 10.0.0.0/8    | 16,777,216        |
| Class B Private  | 172.16.0.0 - 172.31.255.255  | 172.16.0.0/12 | 1,048,576         |
| Class C Private  | 192.168.0.0 - 192.168.255.255| 192.168.0.0/16| 65,536            |
+------------------+------------------------------+---------------+-------------------+
```

---

## 3. Reserved IP Addresses in a Subnet (Standard 2 IPs vs. AWS Cloud 5 IPs)

Not all IP addresses within a subnet can be assigned to host devices. Addresses are reserved for infrastructure and networking operations.

### A. Standard IPv4 Subnet (2 Reserved IPs)
In traditional on-premise networks (RFC 950 / RFC 1812), exactly **2 IP addresses** are reserved in every subnet:
1. **Network Address (First IP, e.g., `.0`)**: Identifies the subnet block itself (all host bits set to `0`). Cannot be assigned to hosts.
2. **Broadcast Address (Last IP, e.g., `.255`)**: Used to broadcast packets to all devices on the subnet (all host bits set to `1`).
* **Standard Usable Host Formula**:
  $$\text{Usable Host Addresses} = 2^{(32 - n)} - 2$$

---

### B. Cloud / AWS VPC Subnet (5 Reserved IPs)
In cloud platforms like **AWS VPC** (e.g., in a `10.0.0.0/24` subnet block), AWS automatically reserves **5 IP addresses** in every subnet:

1. **`10.0.0.0` — Network Address**: Reserved for the subnet network ID.
2. **`10.0.0.1` — VPC Router / Default Gateway**: Reserved by AWS for the VPC local router interface. **This IP (`.1`) is assigned to and used by the Router / Default Gateway**.
3. **`10.0.0.2` — AWS DNS Server**: Reserved by AWS for DNS resolution (`AmazonProvidedDNS` / Route 53 VPC Resolver).
4. **`10.0.0.3` — Future Use**: Reserved by AWS for future internal capabilities and infrastructure management.
5. **`10.0.0.255` — Broadcast Address**: Subnet broadcast address (AWS VPC reserves this address for protocol safety).

* **AWS Cloud Usable Host Formula**:
  $$\text{AWS Usable Host Addresses} = 2^{(32 - n)} - 5$$

```
AWS Subnet Reserved IP Allocation Example (10.0.0.0/24):
+-------------+-----------------------------+------------------------------------+
| IP Address  | Reserved Role               | Component Assigned                 |
+-------------+-----------------------------+------------------------------------+
| 10.0.0.0    | Network Address             | Subnet Identification              |
| 10.0.0.1    | VPC Router / Gateway        | VPC Router Interface (ROUTER IP)   |
| 10.0.0.2    | DNS Server                  | Route 53 VPC Resolver              |
| 10.0.0.3    | Future Use                  | AWS Internal Infrastructure        |
| 10.0.0.255  | Broadcast Address           | Subnet Broadcast                   |
+-------------+-----------------------------+------------------------------------+
| 10.0.0.4 to | Usable EC2 Instance IPs     | Assignable to VMs / Containers     |
| 10.0.0.254  | (251 Usable IPs Total)      |                                    |
+-------------+-----------------------------+------------------------------------+
```

---

## 4. CIDR (Classless Inter-Domain Routing)

CIDR replaced wasteful Classful IP allocation by allowing arbitrary network prefix lengths (e.g., `/26`, `/29`).

### CIDR Master Quick Reference Cheat Table

| CIDR Prefix | Subnet Mask | Block Size | Total IPs | Std Usable (`2^H - 2`) | AWS Usable (`2^H - 5`) | Router IP | Common DevOps Use Case |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **`/32`** | `255.255.255.255` | 1 | 1 | 1 | 0 | N/A | Host firewall rule / Security Group |
| **`/30`** | `255.255.255.252` | 4 | 4 | **2** | 0 | `.1` | Point-to-Point router links / VPN tunnels |
| **`/29`** | `255.255.255.248` | 8 | 8 | **6** | **3** | `.1` | Small pool of public IPs / load balancers |
| **`/28`** | `255.255.255.240` | 16 | 16 | **14** | **11** | `.1` | Small subnet / database cluster |
| **`/27`** | `255.255.255.224` | 32 | 32 | **30** | **27** | `.1` | Container pod network / application tier |
| **`/26`** | `255.255.255.192` | 64 | 64 | **62** | **59** | `.1` | Small office branch / VPC micro-subnet |
| **`/24`** | `255.255.255.0` | 256 | 256 | **254** | **251** | `.1` | Standard office LAN / AWS VPC subnet |
| **`/20`** | `255.240.0.0` | 4,096 | 4,096 | **4,094** | **4,091** | `.1` | Large cloud VPC Availability Zone subnet |
| **`/16`** | `255.255.0.0` | 65,536 | 65,536 | **65,534** | **65,531** | `.1` | Standard Cloud VPC (e.g., AWS VPC `10.0.0.0/16`) |

---

## 5. NAT (Network Address Translation) & PAT

NAT translates private IP addresses to a public IP address before forwarding packets to the Internet.

```
[ Private Device: 192.168.1.15:52104 ]
                 |
                 v
   [ Router NAT Gateway ] ---> Map 192.168.1.15:52104 to Public IP: 203.0.113.5:10045
                 |
                 v
       [ Internet Web Server ]
```

### NAT Types Summary
1. **Static NAT (1:1)**: Maps one private IP directly to one public IP (used for hosting public servers).
2. **Dynamic NAT (M:N)**: Maps private IPs to a pool of available public IPs on a first-come, first-served basis.
3. **PAT / NAPT (Port Address Translation / NAT Overload)**: Maps multiple private IPs to a **single public IP** using unique source port numbers. *This is how home routers and cloud NAT Gateways work.*

---

## 6. Fast Mental Math Tricks for Subnetting in Interviews

### The Magic Number Rule
To find the subnet increment (block size):
$$\text{Magic Number} = 256 - \text{Interesting Octet Value}$$

* **Example**: Given subnet mask `255.255.255.224` (`/27`):
  * Interesting octet is the 4th octet (`224`).
  * Block size = $256 - 224 = 32$.
  * Subnets start at: `0`, `32`, `64`, `96`, `128`, `160`, `192`, `224`.
  * For IP `192.168.1.75`:
    * Network Address = `192.168.1.64`
    * Broadcast Address = `192.168.1.95`
    * Usable Range (Standard) = `192.168.1.65` to `192.168.1.94`

---

## 7. Top IP Addressing & Subnetting Interview Questions

### Q1: What is the difference between Public and Private IP addresses?
> **Answer**: Public IP addresses are globally unique and routable on the public Internet, assigned by IANA/ISPs. Private IP addresses (RFC 1918: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) are non-routable on the Internet and used within internal networks. NAT is required for private IP devices to access the Internet.

### Q2: Why does AWS reserve 5 IP addresses in every VPC subnet instead of 2?
> **Answer**: Standard IPv4 reserves 2 IPs (`.0` Network, `.255` Broadcast). AWS reserves 3 additional IPs for cloud infrastructure services: `.1` for the VPC Router / Default Gateway, `.2` for the AWS DNS Server (Route 53 Resolver), and `.3` for future AWS management capabilities.

### Q3: Which IP address is assigned to the Router in an AWS VPC subnet?
> **Answer**: In an AWS VPC subnet, the **`.1`** IP address (e.g., `10.0.0.1` in `10.0.0.0/24`) is reserved by AWS and assigned to the VPC local router / default gateway.

### Q4: How many usable hosts are in a `/28` subnet in standard networking vs. AWS VPC?
> **Answer**: 
> * **Standard LAN**: $2^{(32-28)} - 2 = 16 - 2 = 14$ usable hosts.
> * **AWS VPC**: $2^{(32-28)} - 5 = 16 - 5 = 11$ usable hosts.

### Q5: What is the difference between SNAT and DNAT in firewalls/NAT?
> **Answer**: 
> * **SNAT (Source NAT)** modifies the source IP address of outbound packets (used when internal hosts connect out to the Internet).
> * **DNAT (Destination NAT)** modifies the destination IP address of inbound packets (used for port forwarding to direct Internet traffic to an internal web server).

---

## Next Recommended Guides
* 🟢 **[Networking Basics & Introduction](networking-basics.md)**
* 🌐 **[Networking Protocols & Transmission](networking-protocols.md)**
* 🧱 **[Network Components & Architecture Guide](networking-components-architecture.md)**
* 🔒 **[Network Security & Firewalls Guide](networking-security-firewalls.md)**
* 🛠️ **[Networking Tools & CLI Commands Guide](Networking/networking-tools-guide.md)**
* ⚡ **[Networking Interview Cheat Sheet](networking-cheatsheet.md)**

