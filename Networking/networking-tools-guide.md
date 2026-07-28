# Linux Networking Tools - Complete Guide
*For DevOps Engineers, SysAdmins, and Interview Preparation*

---

## Table of Contents
1. [IP Command](#1-ip-command)
2. [IP Routing Commands](#2-ip-routing-commands)
3. [IP Neighbor (ARP)](#3-ip-neighbor-arp)
4. [Ping - Connectivity Testing](#4-ping---connectivity-testing)
5. [Traceroute - Path Discovery](#5-traceroute---path-discovery)
6. [Whois - Domain Information](#6-whois---domain-information)
7. [Dig - DNS Queries](#7-dig---dns-queries)
8. [Nslookup](#8-nslookup)
9. [SS - Socket Statistics](#9-ss---socket-statistics)
10. [Watch - Real-time Monitoring](#10-watch---real-time-monitoring)
11. [Nmap - Network Scanner](#11-nmap---network-scanner)
12. [SSH - Secure Shell](#12-ssh---secure-shell)
13. [SCP - Secure Copy](#13-scp---secure-copy)
14. [Rsync - Remote Sync](#14-rsync---remote-sync)
15. [Wget - Non-interactive Downloader](#15-wget---non-interactive-downloader)
16. [Curl - Transfer Data Tool](#16-curl---transfer-data-tool)
17. [Netperf - Network Performance](#17-netperf---network-performance-benchmarking)
18. [Iftop - Real-time Bandwidth](#18-iftop---real-time-bandwidth-monitoring)
19. [Btop - Modern System Monitor](#19-btop---modern-system-monitor)
20. [Ifplugstatus - Link Detection](#20-ifplugstatus---ethernet-link-detection)
21. [Ethtool - Interface Details](#21-ethtool---interface-details)
22. [Bmon - Bandwidth Monitor](#22-bmon---bandwidth-monitor)
23. [Speedtest-CLI](#23-speedtest-cli---internet-speed-test)
24. [Netplan - Network Configuration](#24-netplan---network-configuration)
25. [Nmtui - Network Manager TUI](#25-nmtui---network-manager-tui)
26. [Nmcli - NetworkManager CLI](#26-nmcli---networkmanager-cli)
27. [Additional Production Tools](#27-additional-production-tools)
28. [Legacy Commands](#legacy-commands-still-useful)
29. [Quick Reference Table](#quick-reference-table-for-interviews)
30. [Troubleshooting Workflow](#troubleshooting-workflow-for-interviews)

---

## 1. IP COMMAND
*Modern Replacement for ifconfig*

### Basic Usage
```bash
ip --help          # Show all available options
man ip             # Detailed manual
```

### Working with Network Layers

**Data Link Layer (Layer 2)**
```bash
ip link                    # Show all network interfaces
ip l                       # Short form
ip link show               # Same as above
ip link show dev eth0      # Show specific interface
ip link set eth0 up        # Bring interface UP
ip link set eth0 down      # Bring interface DOWN
```

**Network Layer (Layer 3)**
```bash
ip address show            # Show all IP addresses
ip address                 # Same as above
ip a                       # Short form
ip a show eth0             # Show specific NIC only
ip a s eth0                # Even shorter
```

### Output Formatting Options
```bash
ip -j a                    # JSON format (parseable)
ip -o a                    # One line per entry (scripting)
ip -c a                    # Color-coded output
ip -br a                   # Brief output (clean table)
ip -s link                 # Show statistics (RX/TX packets, errors)
ip -s -s link              # Detailed statistics (double -s)
```

### System Files for NICs
```bash
ls /sys/class/net/         # Lists all network interfaces
cat /sys/class/net/eth0/operstate    # Shows UP/DOWN state
cat /sys/class/net/eth0/address      # Shows MAC address
cat /sys/class/net/eth0/speed        # Shows link speed (Mbps)
```

---

## 2. IP ROUTING COMMANDS

### View Routes
```bash
ip route show              # Show routing table
ip route                   # Same as above
ip r                       # Short form
ip r | column -t           # Format as clean table
route -n                   # Legacy command (numeric IPs)
```

### Manage Routes
```bash
# Add a route
ip route add 192.168.2.0/24 via 192.168.1.1     # Via gateway
ip route add 192.168.2.0/24 dev eth0            # Via interface
ip route add default via 192.168.1.1            # Set default gateway

# Delete a route
ip route delete 192.168.2.0/24
ip route del default                             # Remove default gateway

# Get route to specific destination
ip route get 8.8.8.8                             # Shows path to Google DNS
```

---

## 3. IP NEIGHBOR (ARP)

```bash
ip neighbour                # Show ARP cache (MAC-IP mappings)
ip neigh                    # Short form
ip n                        # Shortest form
ip n show dev eth0          # Show ARP for specific interface
ip n flush dev eth0         # Clear ARP cache for interface
```

**Alternative (Legacy)**:
```bash
arp -a                      # Show ARP table
arp -n                      # Numeric format (no DNS lookup)
```

---

## 4. PING - Connectivity Testing

### Basic Usage
```bash
ping google.com             # Continuous ping (Ctrl+C to stop)
ping -c 4 8.8.8.8          # Send 4 ICMP packets only
ping -c 10 -i 0.5 8.8.8.8  # Send 10 packets, 0.5s interval
ping -s 1024 google.com    # Custom packet size (1024 bytes)
ping -W 2 8.8.8.8          # Timeout of 2 seconds
```

### Advanced Options
```bash
ping -c 100 -i 0.2 -q 8.8.8.8     # -q = quiet (summary only)
ping -f 8.8.8.8                    # Flood ping (requires root)
ping -M do -s 1472 google.com     # MTU path discovery
```

---

## 5. TRACEROUTE - Path Discovery

### Basic Usage
```bash
traceroute google.com       # Show all network hops
traceroute 8.8.8.8
traceroute -n google.com    # No DNS resolution (faster)
traceroute -I google.com    # Use ICMP instead of UDP
traceroute -T google.com    # Use TCP (bypasses some firewalls)
traceroute -m 15 google.com # Max 15 hops
```

### Understanding Output
```
1    192.168.1.1       2ms    # Hop 1 (local router)
2    10.0.0.1          5ms    # Hop 2 (ISP gateway)
3    * * *                    # Hop 3 (firewall/timeout/hidden)
```

**Note**: `* * *` means system down, firewall blocking, or hidden router

---

## 6. WHOIS - Domain Information

```bash
whois google.com            # Domain registration details
whois 8.8.8.8              # IP ownership information
whois -H google.com         # Hide legal disclaimers
whois -I google.com         # Use IANA database
```

**Returns**:
- Domain registrar
- Registration/expiration dates
- Name servers
- Registrant contact (if not privacy-protected)
- **IANA**: Internet Assigned Numbers Authority

---

## 7. DIG (Domain Information Groper) - DNS Queries

### Basic DNS Lookup
```bash
dig google.com              # A record (IPv4)
dig google.com +short       # Show IP only
dig google.com A            # Explicit A record query
dig google.com AAAA         # IPv6 address
dig google.com MX           # Mail servers
dig google.com NS           # Name servers
dig google.com TXT          # TXT records (SPF, DKIM)
dig google.com ANY          # All records (deprecated in modern DNS)
```

### Reverse DNS Lookup
```bash
dig -x 8.8.8.8              # Reverse lookup (IP to domain)
dig -x 142.250.190.46
```

### Query Specific DNS Server
```bash
dig @8.8.8.8 google.com     # Use Google DNS
dig @1.1.1.1 google.com     # Use Cloudflare DNS
dig @192.168.1.1 google.com # Use local DNS
```

### Advanced Options
```bash
dig google.com +trace       # Full DNS resolution path
dig google.com +noall +answer   # Clean output
dig google.com +stats       # Query statistics
```

---

## 8. NSLOOKUP (Name Server Lookup)

```bash
nslookup google.com         # Basic lookup
nslookup 8.8.8.8           # Reverse lookup
nslookup google.com 8.8.8.8 # Use specific DNS server
```

### Interactive Mode
```bash
nslookup
> server 8.8.8.8           # Set DNS server
> set type=MX              # Query mail servers
> google.com
> set type=NS              # Query name servers
> google.com
> exit
```

**Note**: `dig` is preferred over `nslookup` for scripting and production use.

---

## 9. SS (Socket Statistics) - Modern Netstat Replacement

### View Sockets and Ports
```bash
ss                          # All connections
ss -a                       # All sockets (listening + established)
ss -l                       # Listening sockets only
ss -t                       # TCP only
ss -u                       # UDP only
ss -n                       # Numeric (no DNS/service resolution)
ss -p                       # Show process using socket
```

### Common Combinations
```bash
ss -tulnw                   # TCP + UDP + Listening + Numeric + RAW sockets
ss -tulnp                   # Same + Process IDs
ss -plunt                   # Listening with PIDs (TCP + UDP)
ss -tun                     # Established TCP/UDP connections
ss -ant                     # All TCP with numeric ports
ss -tan state ESTABLISHED   # Only established TCP
```

### Filter by State
```bash
ss -t state established     # Established TCP connections
ss -t state listening       # Listening TCP ports
ss -t state time-wait       # TIME_WAIT connections
ss -t state close-wait      # CLOSE_WAIT connections
```

### Filter by Port
```bash
ss -tuln sport = :22        # SSH port
ss -tuln dport = :80        # HTTP port
ss -tuln '( dport = :80 or dport = :443 )'   # HTTP + HTTPS
```

### Process-Specific
```bash
ss -p | grep nginx          # All nginx connections
ss -tlnp | grep :3000       # Process listening on port 3000
```

---

## 10. WATCH - Real-time Monitoring

```bash
watch -n 2 ss -tulnp        # Update every 2 seconds
watch -n 1 'ip -s link'     # Monitor interface statistics
watch -d -n 1 'ss -tan | grep ESTABLISHED | wc -l'  # Count connections
```

**Note**: `-d` highlights differences between updates

---

## 11. NMAP - Network Scanner

### Host Discovery
```bash
nmap -sn 192.168.1.0/24     # Ping scan (no port scan)
nmap -sP 192.168.1.0/24     # Legacy ping scan
```

### Port Scanning
```bash
nmap 192.168.1.10           # Scan top 1000 ports
nmap -p 22,80,443 192.168.1.10   # Specific ports
nmap -p 1-65535 192.168.1.10     # All ports (slow)
nmap -F 192.168.1.10        # Fast scan (100 common ports)
```

### Scan Types
```bash
nmap -sS 192.168.1.10       # SYN scan (stealth, requires root)
nmap -sT 192.168.1.10       # TCP connect scan
nmap -sU 192.168.1.10       # UDP scan
nmap -sV 192.168.1.10       # Service version detection
nmap -O 192.168.1.10        # OS detection
nmap -A 192.168.1.10        # Aggressive (OS + version + scripts)
```

### Production-Safe Scanning
```bash
nmap -sS -sU -PN -p 1-65535 192.168.1.10    # Comprehensive
nmap -Pn 192.168.1.10       # Skip ping (firewall bypass)
nmap -v 192.168.1.10        # Verbose output
```

---

## 12. SSH (Secure Shell)

### Basic Connection
```bash
ssh username@192.168.1.10   # Connect to remote server
ssh username@server.com     # Using hostname
ssh -p 2222 user@host       # Custom port (default: 22)
ssh -v user@host            # Verbose (debugging)
```

### SSH Service Management
```bash
sudo systemctl status sshd  # Check SSH daemon status
sudo systemctl start sshd   # Start SSH service
sudo systemctl enable sshd  # Enable on boot
sudo systemctl restart sshd # Restart service
```

### SSH Key Generation
```bash
ssh-keygen -t rsa           # RSA algorithm (2048-bit default)
ssh-keygen -t rsa -b 4096   # RSA with 4096-bit key (more secure)
ssh-keygen -t ed25519       # Ed25519 (modern, recommended)
ssh-keygen -t ecdsa -b 521  # ECDSA algorithm
```

**Default Paths**:
- **Private key**: `/home/user/.ssh/id_rsa` (NEVER share)
- **Public key**: `/home/user/.ssh/id_rsa.pub` (safe to share)

### Copy SSH Key to Server
```bash
ssh-copy-id username@192.168.1.10   # Auto-copy public key
ssh-copy-id -i ~/.ssh/id_ed25519.pub username@host   # Specific key
```

**Manual Copy**:
```bash
cat ~/.ssh/id_rsa.pub | ssh user@host 'cat >> ~/.ssh/authorized_keys'
```

### Port Forwarding in VMs
```bash
ssh -p 2222 username@192.168.1.10   # Connect to forwarded port
ssh -L 8080:localhost:80 user@host  # Local port forwarding
ssh -R 9090:localhost:3000 user@host # Remote port forwarding
ssh -D 1080 user@host               # Dynamic (SOCKS proxy)
```

### ~/.ssh Directory Files
```bash
~/.ssh/id_rsa              # Private key (chmod 600)
~/.ssh/id_rsa.pub          # Public key (chmod 644)
~/.ssh/authorized_keys     # Trusted public keys (on server)
~/.ssh/known_hosts         # Fingerprints of known servers
~/.ssh/config              # SSH client configuration
```

**Example ~/.ssh/config**:
```bash
Host myserver
    HostName 192.168.1.10
    User admin
    Port 2222
    IdentityFile ~/.ssh/id_ed25519
```

Then connect with: `ssh myserver`

---

## 13. SCP (Secure Copy)

### Copy Files
```bash
# Local to Remote
scp file.txt user@host:/path/to/destination/
scp -P 2222 file.txt user@host:/tmp/   # Custom port

# Remote to Local
scp user@host:/path/file.txt /local/path/
scp user@host:/var/log/app.log .       # Copy to current directory
```

### Copy Directories
```bash
scp -r /local/folder user@host:/remote/path/   # Recursive
scp -rp /local/folder user@host:/remote/       # Preserve permissions
scp -C -r large_folder user@host:/backup/      # Compress during transfer
```

### Useful Options
```bash
scp -v file.txt user@host:/tmp/        # Verbose
scp -l 1024 file.txt user@host:/tmp/   # Limit bandwidth (KB/s)
scp -i ~/.ssh/custom_key file.txt user@host:/tmp/   # Custom key
```

---

## 14. RSYNC (Remote Sync)

### Basic Syntax
```bash
rsync [options] source destination
```

### Common Options
```bash
-a    # Archive mode (recursive + preserve permissions/timestamps)
-v    # Verbose
-z    # Compress during transfer
-h    # Human-readable sizes
-P    # Show progress + partial transfer resume
--progress  # Show transfer progress
--delete    # Delete files from destination not in source (DANGEROUS!)
--exclude='pattern'   # Exclude files/folders
--dry-run   # Test run (no actual transfer)
```

### Practical Examples
```bash
# Basic sync
rsync -avz /source/ user@host:/destination/

# With progress
rsync -avzP /source/ user@host:/destination/

# Resume interrupted transfer
rsync -avzP --partial /source/ user@host:/destination/

# Exclude files
rsync -avz --exclude='*.log' --exclude='node_modules/' /source/ user@host:/dest/

# Limit bandwidth
rsync -avz --bwlimit=1024 /source/ user@host:/dest/   # 1MB/s limit

# Dry run (test before actual sync)
rsync -avz --dry-run /source/ user@host:/dest/

# Mirror (delete removed files)
rsync -avz --delete /source/ user@host:/dest/    # Use with caution!

# Over custom SSH port
rsync -avz -e "ssh -p 2222" /source/ user@host:/dest/

# Using specific SSH key
rsync -avz -e "ssh -i ~/.ssh/custom_key" /source/ user@host:/dest/
```

**Important**: Trailing slash matters!
- `/source/` = copy **contents** of source
- `/source` = copy **directory itself**

---

## 15. WGET - Non-interactive Downloader

### Basic Download
```bash
wget https://example.com/file.zip       # Download file
wget -O custom_name.zip URL             # Save with custom name
wget -c https://example.com/large.zip   # Resume interrupted download
```

### Recursive Website Download
```bash
wget -r https://example.com/            # Download whole website
wget -r -np https://example.com/docs/   # -np = no parent directories
wget -r -nd https://example.com/        # -nd = no directory structure
wget -r --accept=pdf https://site.com/  # Download only PDFs
wget -r -l 3 https://example.com/       # Limit depth to 3 levels
```

### Authentication & Logging
```bash
wget --user=username --password=pass URL    # HTTP auth
wget -a download.log https://example.com/   # Log to file
wget -q https://example.com/file.zip        # Quiet mode
```

### Advanced
```bash
wget --spider URL                       # Check if file exists (no download)
wget --limit-rate=200k URL              # Limit download speed
wget -i urls.txt                        # Download from URL list
```

---

## 16. CURL - Transfer Data Tool

### Basic Usage
```bash
curl https://example.com                # Print HTML to terminal
curl -O https://example.com/file.zip    # Save file (original name)
curl -o myfile.zip https://url.com/file.zip   # Save with custom name
```

### Common Options
```bash
curl -L https://example.com             # Follow redirects
curl -s https://example.com             # Silent mode
curl -f https://example.com             # Fail fast (non-200 exits non-zero)
curl -I https://example.com             # Headers only (HEAD request)
curl -v https://example.com             # Verbose (debugging)
```

### Combined Flags (Common Pattern)
```bash
curl -fsSL https://get.docker.com | sh
# -f = fail fast
# -s = silent
# -S = show errors (even in silent mode)
# -L = follow redirects
```

### Download Files
```bash
curl -Lo /usr/local/bin/kubectl https://dl.k8s.io/release/v1.28.0/bin/linux/amd64/kubectl
# -L = follow redirects
# -o = output to file
```

### API Requests
```bash
curl -X POST https://api.example.com/data   # POST request
curl -H "Authorization: Bearer TOKEN" URL    # Custom header
curl -d '{"key":"value"}' -H "Content-Type: application/json" URL   # JSON POST
curl -X DELETE https://api.example.com/resource/123   # DELETE
```

### Testing
```bash
curl -w "\n%{http_code}\n" https://example.com   # Show HTTP status code
curl -o /dev/null -s -w "%{time_total}\n" URL    # Response time
```

---

## 17. NETPERF - Network Performance Benchmarking

### Installation
```bash
# Debian/Ubuntu
sudo apt-get install netperf

# RHEL/CentOS
sudo yum install epel-release
sudo yum install netperf
```

### Server Setup
```bash
netserver                    # Start server (default port 12865)
netserver -p 5001            # Custom port
netserver -D                 # Run as daemon
```

**Kill server**:
```bash
pkill netserver              # Must kill manually
```

### Client Testing
```bash
# Basic throughput test
netperf -H 192.168.1.100                    # Default TCP_STREAM test
netperf -H 192.168.1.100 -p 5001            # Custom server port
netperf -H 192.168.1.100 -l 60              # Run for 60 seconds
netperf -H 192.168.1.100 -t TCP_STREAM      # Explicit throughput test

# Change measurement format
netperf -H 192.168.1.100 -f M               # Megabytes
netperf -H 192.168.1.100 -f G               # Gigabytes
netperf -H 192.168.1.100 -f m               # Megabits (default)

# Change reporting interval
netperf -H 192.168.1.100 -D 5               # Report every 5 seconds

# Latency test (TCP Round-Robin)
netperf -H 192.168.1.100 -t TCP_RR -l 30    # Transactions/second
```

### Test Types
- **TCP_STREAM**: Bulk data throughput
- **TCP_RR**: Request/response latency
- **UDP_STREAM**: UDP throughput
- **TCP_CRR**: Connection rate (establish + transfer + close)

---

## 18. IFTOP - Real-time Bandwidth Monitoring

### Installation
```bash
sudo apt install iftop      # Debian/Ubuntu
sudo yum install iftop      # RHEL/CentOS
```

### Usage
```bash
sudo iftop                  # Monitor all interfaces
sudo iftop -i eth0          # Monitor specific interface
sudo iftop -n               # No DNS resolution (faster)
sudo iftop -B               # Display in bytes instead of bits
sudo iftop -P               # Show port numbers
```

### Interactive Controls
- **t**: Toggle display modes
- **p**: Pause display
- **n**: Toggle DNS resolution
- **s**: Toggle source
- **d**: Toggle destination
- **q**: Quit

**Shows**:
- Live connections with source/destination
- Data transferred per connection
- Transfer rates (2s, 10s, 40s averages)

---

## 19. BTOP - Modern System Monitor

### Installation
```bash
sudo apt install btop       # Debian/Ubuntu
sudo snap install btop      # Snap
```

### Features
- CPU usage (per core)
- Memory usage (RAM + swap)
- Disk I/O and usage
- Process list with PIDs
- **Network information per NIC** (RX/TX rates)
- Graphical terminal interface

```bash
btop                        # Run (ESC to quit)
```

---

## 20. IFPLUGSTATUS - Ethernet Link Detection

```bash
sudo apt install ifplugd    # Installation
ifplugstatus                # Check all interfaces
ifplugstatus eth0           # Specific interface
```

**Output**: Shows if Ethernet cable is **plugged in** (link beat detected)

---

## 21. ETHTOOL - Interface Details

### View Interface Info
```bash
ethtool eth0                # Complete details
ethtool eth0 | grep Speed   # Link speed
ethtool eth0 | grep Duplex  # Full/half duplex
```

**Provides**:
- Link speed (10/100/1000/10000 Mbps)
- Duplex mode (Full/Half)
- Auto-negotiation status
- Link detected (yes/no)
- Driver information
- Supported modes

---

## 22. BMON - Bandwidth Monitor

### Installation
```bash
sudo apt install bmon       # Debian/Ubuntu
```

### Usage
```bash
bmon                        # Monitor all interfaces
bmon -p eth0                # Specific interface
```

**Features**:
- Graphical CLI interface
- Live TX/RX rates
- Historical graphs
- Auto-detects all interfaces
- Color-coded display

---

## 23. SPEEDTEST-CLI - Internet Speed Test

### Installation
```bash
sudo apt install speedtest-cli     # Debian/Ubuntu
pip3 install speedtest-cli         # Via pip
```

### Usage
```bash
speedtest-cli               # Full test with details
speedtest-cli --simple      # Simplified output (ping, download, upload)
speedtest-cli --bytes       # Show in bytes instead of bits
speedtest-cli --list        # List nearby servers
speedtest-cli --server 1234 # Use specific server ID
speedtest-cli --json        # JSON output (for parsing)
```

---

## 24. NETPLAN - Network Configuration (Ubuntu 18.04+)

### Configuration Files
```bash
ls /etc/netplan/            # List config files
sudo nano /etc/netplan/01-netcfg.yaml   # Edit configuration
```

### Sample Static IP Config
```yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses: [192.168.1.100/24]
      gateway4: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 1.1.1.1]
```

### Sample DHCP Config
```yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: yes
```

### Apply Configuration
```bash
sudo netplan try            # Test (auto-reverts in 120s)
sudo netplan apply          # Apply permanently
sudo netplan --debug apply  # Debug mode
```

---

## 25. NMTUI - Network Manager TUI

```bash
nmtui                       # Launch interface
```

**Features**:
- Tab-based navigation
- Edit connections
- Activate/deactivate interfaces
- Set hostname
- User-friendly for beginners

---

## 26. NMCLI - NetworkManager CLI

### Device Management
```bash
nmcli device status         # Show all devices
nmcli dev                   # Short form
nmcli dev wifi list         # List WiFi networks
nmcli dev wifi connect SSID password PASSWORD   # Connect to WiFi
nmcli dev connect eth0      # Activate interface
nmcli dev disconnect eth0   # Deactivate interface
```

### Connection Management
```bash
nmcli connection show       # List all connections
nmcli con show              # Short form
nmcli con show "Wired connection 1"   # Details of specific connection
nmcli con up "Wired connection 1"     # Activate connection
nmcli con down "Wired connection 1"   # Deactivate connection
```

### Get IP Address Info
```bash
nmcli -p device show eth0   # Pretty format
nmcli device show eth0 | grep IP4.ADDRESS   # IP address only
```

---

## 27. ADDITIONAL PRODUCTION TOOLS

### tcpdump - Packet Capture
```bash
sudo tcpdump -i eth0                   # Capture on interface
sudo tcpdump -i eth0 port 80           # HTTP traffic only
sudo tcpdump -i eth0 -w capture.pcap   # Save to file
sudo tcpdump -i eth0 -c 100            # Capture 100 packets
sudo tcpdump -i eth0 -n                # No DNS resolution
```

### nethogs - Per-Process Bandwidth
```bash
sudo apt install nethogs
sudo nethogs eth0           # Monitor which process uses bandwidth
```

### mtr - Enhanced Traceroute
```bash
sudo apt install mtr
mtr google.com              # Continuous traceroute with stats
mtr -n google.com           # No DNS resolution
mtr --report google.com     # Generate report
```

### nc (netcat) - Network Swiss Army Knife
```bash
nc -zv 192.168.1.10 22      # Test if port is open
nc -l 1234                  # Listen on port 1234
echo "test" | nc host 1234  # Send data
nc -u host 1234             # UDP mode
```

### iperf3 - Network Performance
```bash
# Server
iperf3 -s                   # Start server

# Client
iperf3 -c 192.168.1.100     # Test to server
iperf3 -c 192.168.1.100 -t 60   # Run for 60 seconds
iperf3 -c 192.168.1.100 -u      # UDP test
iperf3 -c 192.168.1.100 -R      # Reverse (download test)
```

---

## LEGACY COMMANDS (Still Useful)

### ifconfig → Replaced by `ip a`
```bash
ifconfig                    # Show all interfaces
ifconfig eth0               # Show specific interface
ifconfig eth0 up            # Bring UP
ifconfig eth0 down          # Bring DOWN
```

### route → Replaced by `ip r`
```bash
route -n                    # Show routing table (numeric)
route add default gw 192.168.1.1   # Add default gateway
route del default           # Remove default gateway
```

### netstat → Replaced by `ss`
```bash
netstat -tuln               # Listening ports
netstat -tulnp              # With process IDs
netstat -i                  # Interface statistics
netstat -r                  # Routing table
```

### arp → Replaced by `ip n`
```bash
arp -a                      # Show ARP table
arp -n                      # Numeric format
arp -d 192.168.1.10         # Delete ARP entry
```

---

## QUICK REFERENCE TABLE FOR INTERVIEWS

| Task | Modern Command | Legacy Alternative |
|------|----------------|-------------------|
| Show IP addresses | `ip a` | `ifconfig` |
| Show routing table | `ip r` | `route -n` |
| Show ARP cache | `ip n` | `arp -a` |
| Show sockets/ports | `ss -tuln` | `netstat -tuln` |
| Bring interface UP | `ip link set eth0 up` | `ifconfig eth0 up` |
| Add route | `ip route add ... via ...` | `route add ...` |
| DNS lookup | `dig google.com` | `nslookup google.com` |
| Port scan | `nmap -sS host` | N/A |
| File transfer | `rsync -avz src/ dest/` | `scp -r src dest` |
| Network performance | `iperf3 -c host` | `netperf -H host` |

---

## TROUBLESHOOTING WORKFLOW FOR INTERVIEWS

```bash
# 1. Check interface status
ip link show

# 2. Check IP address
ip addr show

# 3. Check routing
ip route show

# 4. Test local connectivity
ping -c 4 192.168.1.1

# 5. Test external connectivity
ping -c 4 8.8.8.8

# 6. Test DNS resolution
ping -c 4 google.com

# 7. Check DNS servers
cat /etc/resolv.conf

# 8. Trace path
traceroute google.com

# 9. Check listening services
ss -tulnp

# 10. Check firewall
sudo iptables -L
```

---

## Key Interview Points

### Common Questions & Answers

**Q: What's the difference between `ip` and `ifconfig`?**
- `ip` is modern, part of iproute2 package, supports advanced features
- `ifconfig` is deprecated, part of net-tools, limited functionality
- `ip` can manage routes, neighbors, tunnels, policies

**Q: How do you check if a port is open?**
```bash
# Multiple methods:
nc -zv host 22              # Netcat
nmap -p 22 host             # Nmap
telnet host 22              # Telnet
ss -tuln | grep :22         # Check locally
```

**Q: Difference between TCP and UDP scans?**
- TCP: Connection-oriented, slower, more reliable detection
- UDP: Connectionless, faster, may miss closed ports (firewalls drop)

**Q: How to transfer files securely?**
- SCP: Simple, one-time transfers
- RSYNC: Efficient, resumable, only transfers differences
- SFTP: Interactive file management

**Q: What does `ss -tulnp` show?**
- **t**: TCP sockets
- **u**: UDP sockets
- **l**: Listening sockets
- **n**: Numeric (no DNS resolution)
- **p**: Process information

---

**This guide covers all essential networking tools used in production environments!**

*Last Updated: March 2026*
