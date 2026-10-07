# Comprehensive Network Components, Devices & Architecture Guide

> 📘 **Quick Navigation**:
> * 🟢 **[Networking Basics & Introduction](networking-basics.md)** — Core concepts, human analogies, network scopes, MAC history.
> * 🌐 **[Networking Protocols & Transmission](networking-protocols.md)** — Unicast/Broadcast/Multicast, HTTP/HTTPS, DNS, DHCP, BGP.
> * 🔢 **[IP Addressing, Subnetting & NAT](networking-ip-addressing.md)** — IPv4/IPv6, CIDR notation, 5 Cloud Reserved IPs, NAT/PAT.
> * 🔒 **[Network Security & Firewalls](networking-security-firewalls.md)** — Stateful/Stateless firewalls, Security Groups, NACLs, VPNs.
> * 🛠️ **[Networking Tools & CLI Commands](Networking/networking-tools-guide.md)** — `ip`, `ping`, `traceroute`, `ss`, `dig`, `tcpdump`.
> * ⚡ **[Networking Interview Cheat Sheet](networking-cheatsheet.md)** — Master single-page quick reference.

---

## 1. Network Component Comparison Matrix

Network devices operate at specific layers of the OSI model, with varying levels of intelligence, packet inspection capabilities, and boundary isolation:

| Device | Primary OSI Layer | Forwarding Identifier | Intelligence Level | Collision Domains | Broadcast Domains | Core Function |
| :--- | :---: | :--- | :--- | :---: | :---: | :--- |
| **Hub** | **Layer 1** (Physical) | None (Electrical Repeater) | Zero (Dummy multiport repeater) | 1 (All ports shared) | 1 (All ports shared) | Re-amplifies electrical signals and broadcasts to all connected ports indiscriminately. |
| **Bridge** | **Layer 2** (Data Link) | MAC Address | Software-based filtering (2 ports) | 2 (Separated by port) | 1 (Shared) | Interconnects two network segments, filtering frame traffic based on MAC addresses. |
| **Unmanaged Switch** | **Layer 2** (Data Link) | MAC Address (`CAM Table`) | Hardware-based ASIC filtering | $N$ (Every port isolated) | 1 (Shared) | Plug-and-play local network interconnect. Forwards frames directly to target ports using hardware MAC tables. |
| **Managed Switch** | **Layer 2 / Layer 3** | MAC & IP Addresses | Firmware / OS programmable | $N$ (Every port isolated) | Isolated per VLAN | Advanced switch supporting VLANs, Quality of Service (QoS), Port Mirroring, SNMP, and Spanning Tree Protocol (STP). |
| **Layer 3 Switch** | **Layer 3** (Network) | MAC & IP Addresses | Hardware ASIC routing | $N$ (Every port isolated) | Isolated per VLAN/Subnet | Combines ultra-fast hardware switching with inter-VLAN IP routing capability at wire speed. |
| **Router** | **Layer 3** (Network) | IP Address (`Routing Table`) | Software/Hardware IP Routing Engine | $N$ (Every port isolated) | $N$ (Separates broadcast domains) | Interconnects distinct IP networks/subnets. Evaluates IP headers to forward packets across subnets and WANs. |
| **Firewall** | **Layer 4 – 7** | IP, Port, Protocol, App State | Deep Packet Inspection (DPI) | $N$ (Every port isolated) | $N$ (Separates broadcast domains) | Enforces security boundaries by filtering inbound/outbound traffic based on connection states and security policies. |

---

## 2. Switches & Layer 2 Mechanics

### A. How a Switch Works: The CAM Table (Content Addressable Memory)
A switch connects multiple devices on a Local Area Network (LAN). Unlike a hub, a switch sends frames **only to the intended target port** by building a **CAM Table** (MAC Address Table):

```
Switch CAM Table (MAC Address Table):
+-------------------+--------------+------------+
| MAC Address       | Switch Port  | VLAN ID    |
+-------------------+--------------+------------+
| aa:bb:cc:11:22:33 | Port 1       | VLAN 10    |
| aa:bb:cc:44:55:66 | Port 2       | VLAN 10    |
| aa:bb:cc:77:88:99 | Port 3       | VLAN 20    |
+-------------------+--------------+------------+
```

1. **Learning Process**: When Host A (Port 1) sends a frame to Host B (Port 2), the switch inspects the **Source MAC Address** (`aa:bb:cc:11:22:33`) and records it against **Port 1** in its CAM table with a timestamp.
2. **Flooding Process**: If the **Destination MAC Address** is not yet in the CAM table (an *Unknown Unicast* frame), the switch floods the frame out to **all ports except the receiving port**.
3. **Filtering & Forwarding**: Once Host B replies, the switch learns Host B's MAC on **Port 2**. Subsequent frames between Host A and Host B are forwarded **directly between Port 1 and Port 2** without flooding other ports.
4. **Aging**: Entries in the CAM table expire (typically after 300 seconds of inactivity) to account for disconnected or moved devices.

---

### B. Network Interface Duplex Modes
Network Interface Cards (NICs) and switch ports communicate using duplex modes:

* **Half-Duplex**:
  * Data can travel in **both directions, but only one direction at a time** (like a walkie-talkie).
  * Susceptible to collisions if two devices transmit simultaneously.
  * Uses **CSMA/CD** (Carrier Sense Multiple Access with Collision Detection).
  * Example: Legacy hubs and legacy coaxial/10BASE-T Ethernet links.
* **Full-Duplex**:
  * Data travels in **both directions simultaneously** over separate physical transmit (Tx) and receive (Rx) wire pairs.
  * Completely **collision-free**. CSMA/CD is disabled.
  * Example: Modern Gigabit/10G Ethernet switches and full-duplex NIC connections.

---

### C. Port Mirroring & Promiscuous Mode (Network Sniffing)

Normally, a switch sends frames directly to the target port, and a device's NIC ignores any frames not addressed to its own MAC address (or broadcast). To inspect network traffic using packet analyzers like **Wireshark** or `tcpdump`:

1. **Port Mirroring (SPAN - Switched Port Analyzer)**:
   * A feature on managed switches that copies all traffic from one or more source ports (or VLANs) and sends it out to a designated **monitoring port**.
   * Essential for network monitoring, intrusion detection systems (IDS), and troubleshooting.

2. **Promiscuous Mode**:
   * A software/driver state placed on a Network Interface Card (NIC).
   * Tells the NIC to **disable hardware MAC address filtering** and pass **ALL captured frames** up to the operating system protocol stack regardless of destination MAC.
   * Required by packet sniffers (`tcpdump`, Wireshark) when receiving mirrored traffic.

---

## 3. Routers & Layer 3 Routing Architecture

### A. What Defines a Router?
Technically, **any device connected to two or more distinct networks that forwards IP packets between them is a router**. A router evaluates Layer 3 destination IP addresses against its **Routing Table** to determine the optimal next-hop path.

```
                  [ Router ]
                 /          \
                /            \
    Subnet A (10.0.1.0/24)   Subnet B (10.0.2.0/24)
    Broadcast Domain A       Broadcast Domain B
```

### B. Core Router Functions
1. **Separating Broadcast Domains**: Routers **do not forward Layer 2/3 broadcasts** (`FF:FF:FF:FF:FF:FF` or `255.255.255.255`). Broadcasts stay contained within their local subnet.
2. **Default Gateway**: Functions as the default exit point for nodes attempting to send traffic outside their local subnet.
3. **Routing Table Maintenance**: Stores routing entries (static routes or dynamic protocols like BGP/OSPF) mapping IP prefix ranges to target interface gateways.

---

## 4. Network Topologies

Network topology describes how devices are physically or logically arranged and interconnected:

```
Star Topology:              Mesh Topology:                  Leaf-Spine Architecture:
     [Host]                     [Node A] --- [Node B]             [Spine 1]  [Spine 2]
       \                           |    \   /   |                    |    \  /    |
  [Host]-[Switch]-[Host]           |     \ /    |                    |     \/     |
       /                           |      X     |                    |     /\     |
     [Host]                     [Node C] --- [Node D]             [Leaf 1]   [Leaf 2]
```

### A. Classic Topologies
* **Star Topology**:
  * All nodes connect directly to a central device (switch or hub).
  * *Pros*: Single link failure does not affect other devices; easy to troubleshoot and scale.
  * *Cons*: Central switch is a Single Point of Failure (SPOF).
  * *Usage*: Universal standard for modern LANs and office networks.
* **Mesh Topology (Full vs Partial)**:
  * Devices are redundantly interconnected to multiple other nodes.
  * *Full Mesh Formula*: $\text{Links} = \frac{N(N-1)}{2}$
  * *Pros*: Extreme high availability, fault tolerance, and multi-path routing.
  * *Cons*: High cabling cost and complex configuration.
  * *Usage*: Datacenter core backbones, WAN routers, and high-availability cloud regions.
* **Bus Topology (Legacy)**:
  * Single central coaxial cable (trunk) shared by all nodes with T-connectors and terminators.
  * *Cons*: A single cable break drops the entire network; high collisions.
* **Ring Topology (Legacy)**:
  * Nodes connected in a closed circular loop (e.g., IBM Token Ring, FDDI).

---

### B. Modern Datacenter Topology: Leaf-Spine Architecture
Modern cloud datacenters (AWS, Azure, Google Cloud) replaced traditional 3-tier architectures (Access-Aggregation-Core) with **Leaf-Spine Architecture**:

* **Leaf Switches (Top-of-Rack - ToR)**: Connect directly to servers, storage units, and Kubernetes nodes.
* **Spine Switches**: Form the high-speed backbone core. **Every Leaf switch connects to EVERY Spine switch**.
* **Key Advantages**:
  * **Consistent Low Latency**: Every server in the datacenter is exactly 3 hops away from any other server (`Leaf 1` $\rightarrow$ `Spine` $\rightarrow$ `Leaf 2`).
  * **High East-West Bandwidth**: Perfect for containerized microservices and distributed database clusters where servers communicate heavily with each other.
  * **Predictable Scale**: Add a spine switch to scale bandwidth; add a leaf switch to scale server density.

---

## 5. Cloud Virtual Network Architecture (AWS VPC Model)

In cloud engineering and DevOps, physical infrastructure is virtualized into **Software-Defined Networks (SDN)** like AWS Virtual Private Clouds (VPC):

```
+-----------------------------------------------------------------------------------+
| AWS Cloud Region (VPC: 10.0.0.0/16)                                               |
|  +-------------------------------------+   +-----------------------------------+  |
|  | Public Subnet (10.0.1.0/24)           |   | Private Subnet (10.0.10.0/24)     |  |
|  |  [ Internet Gateway ]               |   |  [ App Server / DB Node ]         |  |
|  |  [ NAT Gateway (10.0.1.50) ] <--------+---|--- Outbound Traffic               |  |
|  |  [ Web Server / Load Balancer ]     |   |                                   |  |
|  +-------------------------------------+   +-----------------------------------+  |
+-----------------------------------------------------------------------------------+
```

### Core Cloud Network Components
1. **VPC (Virtual Private Cloud)**: Logically isolated virtual network block defined by an RFC 1918 CIDR prefix (e.g., `10.0.0.0/16`).
2. **Public Subnet**: A subnet whose routing table routes outbound internet traffic directly to an **Internet Gateway (IGW)**.
3. **Private Subnet**: A subnet whose routing table has no direct route to the Internet Gateway. Outbound internet access is routed via a **NAT Gateway** located in a public subnet.
4. **Internet Gateway (IGW)**: Horizontally scaled, highly available VPC component that enables bidirectional communication between instances in public subnets and the Internet.
5. **NAT Gateway**: Managed cloud service that translates private IP addresses to a public IP for outbound internet connections while blocking incoming internet-initiated connections.
6. **VPC Peering & Transit Gateway**:
   * **VPC Peering**: Direct 1:1 network connection between two VPCs allowing private IP communication.
   * **Transit Gateway (TGW)**: Centralized cloud hub interconnecting hundreds of VPCs and on-premise networks in a hub-and-spoke topology.

---

## 6. Wireless Networking & Hardware Architecture

Wireless networks transmit data packets across unguided radio frequency (RF) spectrums instead of physical cables. Modern IT and enterprise environments rely on rigorous RF architecture to deliver high-throughput, low-latency connectivity to mobile client fleets.

### A. RF Transmission & The IEEE 802.11 Standards Family

```
+------------------+-------------------+--------------------+---------------------------------------------------+
| 802.11 Standard  | Frequency Bands   | Maximum Data Rate  | Core Architectural Mechanism                      |
+------------------+-------------------+--------------------+---------------------------------------------------+
| 802.11b (1999)   | 2.4 GHz           | 11 Mbps            | DSSS; 3 non-overlapping channels (1, 6, 11).      |
| 802.11a (1999)   | 5 GHz             | 54 Mbps            | OFDM; uncrowded 5 GHz band; short range.          |
| 802.11g (2003)   | 2.4 GHz           | 54 Mbps            | OFDM in 2.4 GHz; backwards-compatible with b.     |
| 802.11n (Wi-Fi 4)| 2.4 & 5 GHz       | 600 Mbps           | MIMO (Multiple-Input Multiple-Output); 40 MHz.    |
| 802.11ac (Wi-Fi 5)| 5 GHz            | 3.46 Gbps          | MU-MIMO; 80/160 MHz channel bonding; 256-QAM.     |
| 802.11ax (Wi-Fi 6)| 2.4, 5 & 6 GHz   | 9.6 Gbps           | OFDMA (Orthogonal Frequency Division Multiple     |
|                  |                   |                    | Access); Target Wake Time (TWT); 1024-QAM.        |
| 802.11be (Wi-Fi 7)| 2.4, 5 & 6 GHz   | 46 Gbps            | 320 MHz channels; 4096-QAM; Multi-Link (MLO).     |
+------------------+-------------------+--------------------+---------------------------------------------------+
```

* **Frequency Compatibility Rule**: Devices broadcasting on different physical frequencies (e.g. 5 GHz vs 2.4 GHz) cannot communicate directly over RF without dual-band access points.
* **Environmental Attenuation & Obstacles**:
  * **Physical Barriers**: Reinforced concrete walls, bricks, steel beams, and elevator shafts severely attenuate 5 GHz and 6 GHz waves.
  * **Electromagnetic Interference (EMI)**: Microwave ovens (2.45 GHz), fluorescent lighting ballasts, and electric motors introduce noise into the RF floor.
  * **High Device Density**: Crowded offices with hundreds of smartphones and laptops cause high contention. Wi-Fi 6 OFDMA divides channels into sub-carriers (Resource Units) to handle dense device concurrency.

---

### B. Wireless Operating Modes: Infrastructure vs. Ad-Hoc

1. **Infrastructure Mode (BSS / ESS)**:
   * Clients connect to a centralized **Wireless Access Point (WAP)** that bridges RF frames to the wired 802.3 Ethernet switch backbone.
   * **SOHO Wireless Multifunction Router**: Integrates a WAP, Layer-3 Router, 4-Port Switch, DHCP Server, NAT gateway, and Stateful Firewall into a single physical chassis.
2. **Ad-Hoc Mode (IBSS / Peer-to-Peer)**:
   * Direct device-to-device communication with **no central access point**.
   * **IoT Bootstrapping**: Used by smart home devices (video doorbells, smart plugs) during initial unboxing. The device generates a temporary ad-hoc Wi-Fi network so a mobile phone can pass the home network SSID and WPA password.
   * **⚠️ Critical Security Warning**: Ad-hoc networks are **never encrypted**. They must only be used for momentary bootstrapping and never maintained for standard operations.

---

### C. SSID Architecture & The Myth of Hidden SSIDs
* **Service Set Identifier (SSID)**: The 32-character network name that identifies the Basic Service Set. Clients must match the SSID to initiate association.
* **Association Handshake**: Clients do not simply "join"—they transmit 802.11 Probe Requests, negotiate Open/802.11i Authentication, and exchange Association Request/Response frames.
* **Hidden SSIDs (Security Through Obscurity)**:
  * Turning off SSID beacon broadcasts **provides zero real security**.
  * Client devices actively transmit the hidden SSID in plaintext Probe Requests whenever searching for the network.
  * Attackers send an 802.11 Deauthentication frame; when the client re-associates, Wireshark exposes the SSID instantly.
  * Hidden SSIDs create connection delays, roaming failures, and high battery drain without stopping attackers.

---

### D. Signal Attenuation, Pre-Deployment Site Surveys & Heat Maps
* **Attenuation**: The reduction in signal strength (measured in **dBm**) over distance and material penetration.
* **Site Survey**: A physical and RF audit conducted prior to deployment to calculate the exact number and placement of access points.
* **RF Heat Map Calibration Levels**:
  * **$-30\text{ to } -55\text{ dBm}$ (Optimal)**: Direct proximity to AP; maximum data rates, negligible latency.
  * **$-56\text{ to } -67\text{ dBm}$ (Enterprise Target)**: Industry standard target for enterprise voice and data roaming.
  * **$-68\text{ to } -75\text{ dBm}$ (Edge Threshold)**: Usable web access; ideal target at building perimeter to prevent external bleed.
  * **$< -80\text{ dBm}$ (Dead Zone)**: Severe packet loss, frame retries, and dropped connections.

---

### E. Coverage Extension: Repeaters vs. Hardwired APs vs. Wireless Mesh

```
1. Extender / Repeater:   [AP] - - - (RF Half-Duplex) - - - [Repeater] - - - (RF) - - - [Client]
                          * Cuts throughput by 50%; often uses separate fragmented SSID (e.g. Office_EXT).

2. Hardwired APs:         [AP 1] <==== (Cat6 1Gbps Cable) ====> [Switch] <==== (Cat6) ====> [AP 2]
                          * Full wire speed; requires cabling; sticky-client roaming without WLC.

3. Wireless Mesh Fabric:  [Root Mesh Node] - - - (Dedicated Backhaul Radio) - - - [Mesh Node 2]
                                 |                                                       |
                          (Client Band)                                           (Client Band)
                                 v                                                       v
                            [Client A]                                              [Client B]
                          * Single unified SSID; 802.11r/k/v fast seamless roaming; dedicated backhaul radio!
```

* **Wireless Mesh Architecture**: Multiple intelligent AP nodes collaborate to form a self-healing fabric. A dedicated, reserved backhaul channel (separate 5 GHz or 6 GHz radio) is used exclusively for node-to-node relay, preventing the 50% bandwidth penalty of single-radio repeaters.

---

### F. Physical RF Containment, Transmit Power & Antennas
* **Transmit Power Tuning (Tx / EIRP)**: Reducing AP transmit power so signals attenuate below $-75\text{ dBm}$ at exterior building walls. Prevents parking lot wardriving attacks and maintains compliance with regulatory transmission limits.
* **Antenna Radiation Types**:
  * **Omnidirectional (Dipole)**: 360-degree spherical doughnut radiation pattern for open office floor plans.
  * **Directional (Yagi / Patch / Parabolic)**: Narrow high-gain beam for point-to-point building links and long corridors without leaking RF energy through lateral building walls.

---

## Next Recommended Guides
* 🟢 **[Networking Basics & Introduction](networking-basics.md)**
* 🌐 **[Networking Protocols & Transmission](networking-protocols.md)**
* 🔢 **[IP Addressing, Subnetting & NAT Guide](networking-ip-addressing.md)**
* 🔒 **[Network Security & Firewalls Guide](networking-security-firewalls.md)**
* 🛠️ **[Networking Tools & CLI Commands Guide](Networking/networking-tools-guide.md)**
* ⚡ **[Networking Interview Cheat Sheet](networking-cheatsheet.md)**
