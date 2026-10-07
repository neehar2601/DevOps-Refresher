import re

with open("Network_Security_Guide.html", "r") as f:
    content = f.read()

new_tabs = """
    },
    firewalls_dmz_nat: {
        title: "Firewalls, DMZ & Gateways",
        icon: "shield",
        intro: "Securing the network perimeter using Firewalls, Demilitarized Zones (DMZ), and Network Address Translation.",
        sections: [
            {
                title: "1. Network Firewalls",
                content: `
                    <p class="text-slate-300 mb-6">Firewalls monitor and control incoming and outgoing network traffic based on predetermined security rules. They establish a barrier between a trusted network and an untrusted network.</p>
                    <div class="grid md:grid-cols-2 gap-6 mb-8">
                        <div class="bg-slate-900/40 p-6 rounded-xl border border-slate-700">
                            <h4 class="text-amber-400 font-bold mb-2">Stateful vs Stateless</h4>
                            <ul class="text-sm text-slate-400 space-y-2">
                                <li><strong>Stateless:</strong> Examines each packet individually based purely on source/destination IPs and ports (e.g., standard Router ACLs). Fast but less secure.</li>
                                <li><strong>Stateful:</strong> Tracks the operating state and characteristics of network connections. It remembers if a packet is part of an established connection.</li>
                            </ul>
                        </div>
                        <div class="bg-slate-900/40 p-6 rounded-xl border border-slate-700">
                            <h4 class="text-emerald-400 font-bold mb-2">Advanced Firewalls</h4>
                            <ul class="text-sm text-slate-400 space-y-2">
                                <li><strong>NGFW (Next-Gen):</strong> Adds Application-layer (Layer 7) awareness, Deep Packet Inspection (DPI), and Intrusion Prevention Systems (IPS).</li>
                                <li><strong>WAF (Web App Firewall):</strong> Specifically protects web applications by filtering HTTP/HTTPS traffic from exploits like SQL injection and XSS.</li>
                            </ul>
                        </div>
                    </div>
                `
            },
            {
                title: "2. The Demilitarized Zone (DMZ)",
                content: `
                    <p class="text-slate-300 mb-6">A <strong>DMZ</strong> (Demilitarized Zone) is a physical or logical subnetwork that contains and exposes an organization's external-facing services to an untrusted network (the Internet). The purpose of a DMZ is to add an additional layer of security to an organization's Local Area Network (LAN): an external attacker only has direct access to equipment in the DMZ, rather than the entire internal network.</p>
                    
                    <div class="bg-slate-950 p-6 rounded-xl border border-slate-800 font-mono text-[10px] sm:text-xs overflow-hidden relative min-h-[300px]">
                        
                        <!-- Internet -->
                        <div class="absolute left-4 top-1/2 -translate-y-1/2 flex flex-col items-center z-10">
                            <i data-lucide="globe" class="w-8 h-8 text-slate-400 mb-2"></i>
                            <div class="text-slate-400 font-bold">Internet</div>
                        </div>

                        <!-- Traffic Line In -->
                        <div class="absolute left-16 top-1/2 -translate-y-1/2 w-16 h-1 bg-red-500/50"></div>

                        <!-- External Firewall -->
                        <div class="absolute left-32 top-1/2 -translate-y-1/2 flex flex-col items-center z-10">
                            <div class="w-8 h-24 bg-red-900/80 border-2 border-red-500 rounded flex items-center justify-center mb-2 shadow-[0_0_15px_rgba(239,68,68,0.4)]">
                                <i data-lucide="flame" class="w-5 h-5 text-red-400"></i>
                            </div>
                            <div class="text-red-400 font-bold text-center">External<br>Firewall</div>
                        </div>

                        <!-- Traffic Line DMZ -->
                        <div class="absolute left-40 top-1/2 -translate-y-1/2 w-24 h-1 bg-amber-500/50"></div>

                        <!-- DMZ Subnet -->
                        <div class="absolute left-64 top-1/4 bottom-1/4 w-32 bg-amber-900/20 border-2 border-amber-500/50 border-dashed rounded-xl flex flex-col items-center justify-center z-0">
                            <div class="absolute -top-6 text-amber-400 font-bold tracking-widest uppercase">DMZ</div>
                            
                            <div class="flex flex-col gap-4 z-10">
                                <div class="bg-slate-800 px-3 py-2 rounded border border-slate-600 flex items-center gap-2">
                                    <i data-lucide="server" class="w-4 h-4 text-amber-300"></i> Web Srv
                                </div>
                                <div class="bg-slate-800 px-3 py-2 rounded border border-slate-600 flex items-center gap-2">
                                    <i data-lucide="mail" class="w-4 h-4 text-amber-300"></i> Mail Srv
                                </div>
                            </div>
                        </div>

                        <!-- Traffic Line Internal -->
                        <div class="absolute left-[24rem] top-1/2 -translate-y-1/2 w-24 h-1 bg-emerald-500/50"></div>

                        <!-- Internal Firewall -->
                        <div class="absolute left-[30rem] top-1/2 -translate-y-1/2 flex flex-col items-center z-10">
                            <div class="w-8 h-24 bg-emerald-900/80 border-2 border-emerald-500 rounded flex items-center justify-center mb-2 shadow-[0_0_15px_rgba(16,185,129,0.4)]">
                                <i data-lucide="shield" class="w-5 h-5 text-emerald-400"></i>
                            </div>
                            <div class="text-emerald-400 font-bold text-center">Internal<br>Firewall</div>
                        </div>

                        <!-- Traffic Line LAN -->
                        <div class="absolute left-[32rem] right-16 top-1/2 -translate-y-1/2 h-1 bg-emerald-500/50"></div>

                        <!-- Internal LAN -->
                        <div class="absolute right-4 top-1/4 bottom-1/4 w-32 bg-emerald-900/20 border-2 border-emerald-500/50 border-dashed rounded-xl flex flex-col items-center justify-center z-0">
                            <div class="absolute -top-6 text-emerald-400 font-bold tracking-widest uppercase">Internal LAN</div>
                            
                            <div class="flex flex-col gap-4 z-10">
                                <div class="bg-slate-800 px-3 py-2 rounded border border-slate-600 flex items-center gap-2">
                                    <i data-lucide="database" class="w-4 h-4 text-emerald-300"></i> DB Srv
                                </div>
                                <div class="bg-slate-800 px-3 py-2 rounded border border-slate-600 flex items-center gap-2">
                                    <i data-lucide="users" class="w-4 h-4 text-emerald-300"></i> Staff PCs
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="mt-6 info-box border-amber-500 bg-amber-500/5">
                        <strong class="text-amber-400">Security Benefit</strong>
                        <p class="text-sm">If an attacker breaches the Web Server in the DMZ, they still face the Internal Firewall before they can access sensitive databases or staff computers. The Web Server is isolated.</p>
                    </div>
                `
            },
            {
                title: "3. NAT & Proxies",
                content: `
                    <div class="grid md:grid-cols-2 gap-6">
                        <div>
                            <h4 class="text-blue-400 font-bold mb-2">Network Address Translation</h4>
                            <p class="text-sm text-slate-400 mb-4">NAT was designed to save IP space, but acts as a de facto security layer.</p>
                            <ul class="text-sm text-slate-400 space-y-2 mb-6">
                                <li><strong>SNAT (Source NAT / Masquerading):</strong> Rewrites the source IP of outgoing packets to the router's public IP. Internal topology is hidden from the internet.</li>
                                <li><strong>DNAT (Destination NAT / Port Forwarding):</strong> Allows external users to hit a specific port on the router's public IP and be forwarded to a specific internal machine.</li>
                            </ul>
                        </div>
                        <div>
                            <h4 class="text-purple-400 font-bold mb-2">Proxies</h4>
                            <p class="text-sm text-slate-400 mb-4">Proxies terminate connections on behalf of another machine.</p>
                            <ul class="text-sm text-slate-400 space-y-2 mb-6">
                                <li><strong>Forward Proxy:</strong> Sits in front of <em>clients</em>. It fetches internet resources for internal users, acting as a filter and cache.</li>
                                <li><strong>Reverse Proxy:</strong> Sits in front of <em>servers</em>. It receives internet requests and distributes them to internal servers (Load Balancing, SSL Termination, WAF). E.g. Nginx, HAProxy.</li>
                            </ul>
                        </div>
                    </div>
                `
            }
        ]
    },
    security_protocols: {
        title: "Security Protocols",
        icon: "lock",
        intro: "Understanding the cryptographic protocols that secure data in transit across untrusted networks.",
        sections: [
            {
                title: "1. Encryption Fundamentals",
                content: `
                    <div class="comparison-grid">
                        <div class="comparison-card border-slate-600">
                            <h4 class="text-slate-200">Symmetric Encryption</h4>
                            <p class="text-sm text-slate-400">Uses a <strong>single shared key</strong> to both encrypt and decrypt data. Like a safe with one physical key.</p>
                            <ul class="text-sm mt-3 space-y-1 text-slate-400">
                                <li><strong>Pros:</strong> Extremely fast, low CPU overhead. Used for bulk data transfer.</li>
                                <li><strong>Cons:</strong> How do you securely share the key across the internet?</li>
                                <li><strong>Examples:</strong> AES-256, ChaCha20.</li>
                            </ul>
                        </div>
                        <div class="comparison-card border-slate-600">
                            <h4 class="text-slate-200">Asymmetric Encryption</h4>
                            <p class="text-sm text-slate-400">Uses a <strong>key pair (Public Key & Private Key)</strong>. What the public key encrypts, only the private key can decrypt.</p>
                            <ul class="text-sm mt-3 space-y-1 text-slate-400">
                                <li><strong>Pros:</strong> Solves the key sharing problem. Public keys can be safely distributed.</li>
                                <li><strong>Cons:</strong> Mathematically heavy, very slow. Cannot be used for bulk data.</li>
                                <li><strong>Examples:</strong> RSA, ECC (Elliptic Curve).</li>
                            </ul>
                        </div>
                    </div>
                    <div class="info-box border-blue-500 bg-blue-500/5 mt-4">
                        <strong class="text-blue-400">Modern Hybrid Approach</strong>
                        <p class="text-sm text-slate-300">Modern protocols (like TLS and SSH) use <strong>Asymmetric encryption</strong> to securely verify identity and exchange a temporary "session key". Then, they switch to <strong>Symmetric encryption</strong> using that session key for the actual fast data transfer.</p>
                    </div>
                `
            },
            {
                title: "2. TLS / SSL (HTTPS)",
                content: `
                    <p class="text-slate-300 mb-4">Transport Layer Security (the successor to SSL) secures HTTP traffic. It ensures three things: <strong>Encryption</strong> (data is hidden), <strong>Authentication</strong> (the server is who it claims to be), and <strong>Integrity</strong> (data wasn't tampered with).</p>
                    
                    <div class="bg-slate-900/50 p-6 rounded-xl border border-slate-800 mt-4">
                        <h4 class="text-emerald-400 font-bold mb-4">The TLS Handshake (Simplified)</h4>
                        <ol class="list-decimal pl-5 text-sm text-slate-400 space-y-3">
                            <li><strong>Client Hello:</strong> Browser says "I want to connect securely. Here are the ciphers I support."</li>
                            <li><strong>Server Hello & Certificate:</strong> Server picks a cipher and sends its Digital Certificate (containing its Public Key).</li>
                            <li><strong>Authentication:</strong> Browser verifies the certificate against trusted Certificate Authorities (CAs).</li>
                            <li><strong>Key Exchange:</strong> They use asymmetric math (Diffie-Hellman) to secretly agree on a symmetric <strong>Session Key</strong>.</li>
                            <li><strong>Encrypted Data:</strong> Both sides switch to symmetric AES encryption using the Session Key. HTTP traffic begins.</li>
                        </ol>
                    </div>
                `
            },
            {
                title: "3. Other Vital Protocols",
                content: `
                    <table class="mt-4">
                        <thead>
                            <tr>
                                <th>Protocol</th>
                                <th>Port</th>
                                <th>Purpose</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><code class="text-blue-400">SSH (Secure Shell)</code></td>
                                <td>TCP 22</td>
                                <td>Cryptographic network protocol for operating network services securely over an unsecured network. Heavily used for remote Linux terminal access. Replaces Telnet.</td>
                            </tr>
                            <tr>
                                <td><code class="text-amber-400">SFTP / SCP</code></td>
                                <td>TCP 22</td>
                                <td>Secure file transfer protocols that piggyback on top of the SSH protocol. (FTP is insecure and unencrypted).</td>
                            </tr>
                            <tr>
                                <td><code class="text-emerald-400">IPsec</code></td>
                                <td>Layer 3</td>
                                <td>Secures IP communications by authenticating and encrypting each IP packet. Used primarily for Site-to-Site VPNs.</td>
                            </tr>
                            <tr>
                                <td><code class="text-slate-400">WPA3</code></td>
                                <td>Wireless</td>
                                <td>The newest security certification for Wi-Fi networks, providing individualized data encryption and robust protection against brute-force dictionary attacks.</td>
                            </tr>
                        </tbody>
                    </table>
                `
            }
        ]
    },
    zero_trust: {
        title: "Zero Trust & Modern Security",
        icon: "fingerprint",
        intro: "Moving beyond perimeter defenses to identity-based, micro-segmented security architecture.",
        sections: [
            {
                title: "1. The Zero Trust Paradigm",
                content: `
                    <p class="text-slate-300 mb-4">Historically, networks operated on a "Castle and Moat" model: if you passed the external firewall (the moat), you were trusted inside the corporate network (the castle). This allowed malware or attackers to move freely (lateral movement) once inside.</p>
                    
                    <div class="info-box border-rose-500 bg-rose-500/5">
                        <strong class="text-rose-400">"Never Trust, Always Verify"</strong>
                        <p class="text-sm text-slate-300">Zero Trust assumes the internal network is just as hostile as the public internet. No implicit trust is granted based on IP address or network location. Every request must be authenticated, authorized, and continuously validated.</p>
                    </div>
                `
            },
            {
                title: "2. Micro-segmentation & Modern Controls",
                content: `
                    <div class="grid md:grid-cols-2 gap-6 mt-4">
                        <div class="bg-slate-900/40 p-6 rounded-xl border border-slate-700">
                            <h4 class="text-blue-400 font-bold mb-2">Micro-segmentation</h4>
                            <p class="text-sm text-slate-400">Breaking the network down into the smallest possible security zones (down to individual VMs or Containers) and applying strict firewalls between them. If one web server is compromised, the attacker cannot reach the database server next to it.</p>
                        </div>
                        <div class="bg-slate-900/40 p-6 rounded-xl border border-slate-700">
                            <h4 class="text-emerald-400 font-bold mb-2">Cloud-Native Implementation (eBPF)</h4>
                            <p class="text-sm text-slate-400">In modern Kubernetes/Container environments, micro-segmentation is enforced using <strong>Network Policies</strong>. Tools like <strong>Cilium</strong> use eBPF (Extended Berkeley Packet Filter) to enforce high-performance firewall rules directly inside the Linux Kernel.</p>
                        </div>
                    </div>
                `
            }
"""

# We want to replace the final `    }\n};` with `new_tabs + "\n};"`
# Let's find the position of the last `};`
last_brace_idx = content.rfind("};")
if last_brace_idx != -1:
    # Before the `};` we should have `    }\n` or similar. Let's just do a regex replace for the end of the JSON object.
    
    # We can inject it right before `};`
    # Let's verify what's immediately before `};`
    pre_text = content[:last_brace_idx].rstrip() # removes trailing whitespace
    # pre_text now ends with `}` which closes `vpn_architectures`.
    # Actually wait. `vpn_architectures` ends with:
    #         ]
    #     }
    # };
    
    # Let's just do:
    # Find `    }\n};` and replace with `new_tabs + "\n};"`
    modified_content = re.sub(r'    }\n};\s*const navTabs', new_tabs + '\n};\n\n        const navTabs', content)
    
    with open("Network_Security_Guide.html", "w") as f:
        f.write(modified_content)
        
    print("Injection successful.")
else:
    print("Could not find };")

