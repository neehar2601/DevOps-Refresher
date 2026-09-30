import re

with open("Network_Security_Guide.html", "r") as f:
    content = f.read()

# I want to find where `vpn_architectures` ends.
# I will do a regex to extract everything up to the end of `vpn_architectures`
# Fortunately, I know the structure.
match = re.search(r'(const contentData = \{.*?\n    vpn_architectures: \{.*?\n        \]\n    \})', content, re.DOTALL)
if match:
    base_content = match.group(1)
    
    deep_dive_content = """
    ,
    core_principles: {
        title: "Core Security Principles",
        icon: "key",
        intro: "The fundamental concepts that dictate all security engineering and infrastructure design.",
        sections: [
            {
                title: "1. The CIA Triad",
                content: `
                    <p class="text-slate-300 mb-6">At the heart of all security strategies is the CIA Triad. Every security control you implement is designed to protect one or more of these three pillars.</p>
                    <div class="grid md:grid-cols-3 gap-4 mb-8">
                        <div class="bg-slate-900/40 p-5 rounded-xl border border-slate-700 hover:border-blue-500/50 transition-colors">
                            <h4 class="text-blue-400 font-bold mb-2 flex items-center gap-2"><i data-lucide="eye-off" class="w-4 h-4"></i> Confidentiality</h4>
                            <p class="text-xs text-slate-400">Ensuring data is accessible <strong>only</strong> by authorized users or systems.</p>
                            <p class="text-[10px] text-slate-500 mt-2"><strong>Controls:</strong> Encryption (AES, TLS), Access Controls, Passwords.</p>
                        </div>
                        <div class="bg-slate-900/40 p-5 rounded-xl border border-slate-700 hover:border-emerald-500/50 transition-colors">
                            <h4 class="text-emerald-400 font-bold mb-2 flex items-center gap-2"><i data-lucide="shield-check" class="w-4 h-4"></i> Integrity</h4>
                            <p class="text-xs text-slate-400">Maintaining the accuracy and consistency of data by preventing unauthorized modification.</p>
                            <p class="text-[10px] text-slate-500 mt-2"><strong>Controls:</strong> Hashing (SHA-256), Digital Signatures, File Integrity Monitoring (FIM).</p>
                        </div>
                        <div class="bg-slate-900/40 p-5 rounded-xl border border-slate-700 hover:border-amber-500/50 transition-colors">
                            <h4 class="text-amber-400 font-bold mb-2 flex items-center gap-2"><i data-lucide="activity" class="w-4 h-4"></i> Availability</h4>
                            <p class="text-xs text-slate-400">Ensuring systems and data are accessible to authorized users when needed.</p>
                            <p class="text-[10px] text-slate-500 mt-2"><strong>Controls:</strong> Load Balancing, High Availability (HA) Clusters, DDoS Protection, Backups.</p>
                        </div>
                    </div>
                `
            },
            {
                title: "2. Identity & Access Management (IAM)",
                content: `
                    <div class="space-y-6">
                        <div class="bg-slate-900/50 p-6 rounded-xl border border-slate-800">
                            <h4 class="text-slate-200 font-bold mb-3">Authentication vs Authorization</h4>
                            <ul class="text-sm text-slate-400 space-y-3">
                                <li class="flex items-start gap-3">
                                    <div class="mt-1"><i data-lucide="user-check" class="w-4 h-4 text-emerald-400"></i></div>
                                    <div>
                                        <strong class="text-emerald-400">Authentication (AuthN):</strong> Verifying <em>who you are</em>. (e.g., Logging in with a username, password, and MFA code).
                                    </div>
                                </li>
                                <li class="flex items-start gap-3">
                                    <div class="mt-1"><i data-lucide="unlock" class="w-4 h-4 text-blue-400"></i></div>
                                    <div>
                                        <strong class="text-blue-400">Authorization (AuthZ):</strong> Verifying <em>what you are allowed to do</em> once logged in. (e.g., User is logged in, but are they allowed to DELETE a database table?).
                                    </div>
                                </li>
                            </ul>
                        </div>

                        <div class="grid md:grid-cols-2 gap-6">
                            <div class="bg-slate-900/40 p-6 rounded-xl border border-slate-700">
                                <h4 class="text-purple-400 font-bold mb-2">Role-Based Access Control (RBAC)</h4>
                                <p class="text-sm text-slate-400">Instead of assigning permissions to individuals (which scales poorly), permissions are assigned to <strong>Roles</strong> (e.g., "Developer", "Admin", "Read-Only"). Users are then assigned to those roles.</p>
                            </div>
                            <div class="bg-slate-900/40 p-6 rounded-xl border border-slate-700">
                                <h4 class="text-rose-400 font-bold mb-2">Principle of Least Privilege</h4>
                                <p class="text-sm text-slate-400">A security principle stating that a user, program, or process should have only the bare minimum privileges necessary to perform its intended function. No more.</p>
                            </div>
                        </div>
                    </div>
                `
            }
        ]
    },
    cloud_security: {
        title: "Cloud & Network Controls",
        icon: "cloud-lightning",
        intro: "How network boundaries and traffic control are enforced in modern Cloud (AWS/Azure/GCP) environments.",
        sections: [
            {
                title: "1. Security Groups vs NACLs: Deep Dive",
                content: `
                    <p class="text-slate-300 mb-6">In AWS and similar cloud environments, network security is divided into two distinct layers. Understanding how they interact is crucial for DevOps engineers.</p>
                    
                    <div class="bg-slate-900/40 p-6 rounded-xl border border-slate-700 mb-6">
                        <h4 class="text-blue-400 font-bold mb-4">Packet Evaluation Flow</h4>
                        <ol class="list-decimal pl-5 text-sm text-slate-400 space-y-4">
                            <li><strong>Internet Gateway (IGW):</strong> A packet enters the VPC from the internet.</li>
                            <li><strong>Route Table:</strong> The router determines the target Subnet for the packet.</li>
                            <li><strong>Network ACL (NACL):</strong> The packet hits the NACL bounding the Subnet. The NACL evaluates its rules in numerical order (e.g., Rule 100, then 200). It is <strong>stateless</strong>, meaning if it allows the packet in, it <em>does not</em> automatically allow the response packet out. An explicit outbound rule is required.</li>
                            <li><strong>Security Group (SG):</strong> If the NACL allows the packet, it proceeds to the EC2 instance's Security Group. SGs are <strong>stateful</strong>. If the SG allows inbound traffic on port 443, the connection is tracked in a state table. When the server replies, the outbound traffic is automatically allowed, regardless of outbound SG rules.</li>
                            <li><strong>EC2 Instance:</strong> The packet finally reaches the operating system.</li>
                        </ol>
                    </div>

                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-sm text-slate-400">
                            <thead class="bg-slate-800 text-slate-200">
                                <tr>
                                    <th class="p-3 rounded-tl-lg">Feature</th>
                                    <th class="p-3 text-emerald-400">Security Groups (SGs)</th>
                                    <th class="p-3 text-blue-400 rounded-tr-lg">Network ACLs (NACLs)</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-800/50 bg-slate-900/50">
                                <tr>
                                    <td class="p-3 font-bold text-slate-300">Level of Operation</td>
                                    <td class="p-3">Operates at the <strong>Instance/VM</strong> level. (Virtual Firewall)</td>
                                    <td class="p-3">Operates at the <strong>Subnet</strong> level. (Subnet Boundary)</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-bold text-slate-300">Statefulness</td>
                                    <td class="p-3"><strong class="text-emerald-400">Stateful:</strong> Return traffic is automatically allowed.</td>
                                    <td class="p-3"><strong class="text-blue-400">Stateless:</strong> Return traffic must be explicitly permitted.</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-bold text-slate-300">Rule Logic</td>
                                    <td class="p-3"><strong>Allow rules only.</strong> Implicit Deny all else. Rules evaluated as a whole.</td>
                                    <td class="p-3">Supports both <strong>Allow and Deny</strong> rules. Processed in numbered order.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                `
            },
            {
                title: "2. Dynamic Secrets Management",
                content: `
                    <p class="text-slate-300 mb-4">Hardcoding database credentials in application code is a catastrophic risk. Modern DevOps replaces hardcoded secrets with <strong>Secrets Managers</strong> (like HashiCorp Vault).</p>
                    
                    <div class="bg-slate-900/50 p-6 rounded-xl border border-slate-800">
                        <h4 class="text-emerald-400 font-bold mb-4">How HashiCorp Vault Works (Architecture)</h4>
                        <ol class="list-decimal pl-5 text-sm text-slate-400 space-y-3">
                            <li><strong>Identity Authentication:</strong> When an application boots up, it authenticates with Vault using a machine identity (e.g., an AWS IAM Role, or Kubernetes Service Account) rather than a password.</li>
                            <li><strong>Requesting a Secret:</strong> The application asks Vault for the database password.</li>
                            <li><strong>Dynamic Secret Generation:</strong> Instead of returning a static password, Vault connects to the database itself and generates a <em>brand new</em> database user and password on the fly, specific to this exact application instance.</li>
                            <li><strong>Time-to-Live (TTL):</strong> Vault attaches a TTL (e.g., 1 hour) to the password and hands it to the application.</li>
                            <li><strong>Revocation:</strong> When the 1 hour expires, Vault automatically deletes that user from the database. If an attacker stole the password from memory, it becomes useless almost immediately.</li>
                        </ol>
                    </div>
                `
            }
        ]
    },
    firewalls_dmz_nat: {
        title: "Firewalls, Proxies & NAT",
        icon: "shield",
        intro: "A deep dive into perimeter defense mechanisms and packet filtering.",
        sections: [
            {
                title: "1. The Mechanics of a Stateful Firewall",
                content: `
                    <p class="text-slate-300 mb-4">Unlike basic routers which filter blindly based on IPs and Ports (stateless), a <strong>Stateful Firewall</strong> tracks the lifecycle of every network connection passing through it.</p>
                    
                    <div class="bg-slate-900/40 p-6 rounded-xl border border-slate-700 mb-6">
                        <h4 class="text-amber-400 font-bold mb-3">The Connection Tracking Table (Conntrack)</h4>
                        <p class="text-sm text-slate-400 mb-4">When a user initiates an HTTP request to a web server through a stateful firewall, the firewall creates an entry in its state table. It monitors the TCP handshake (SYN, SYN-ACK, ACK).</p>
                        
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs text-slate-300 overflow-x-auto">
                            <table class="w-full text-left">
                                <thead class="text-slate-500 border-b border-slate-700">
                                    <tr>
                                        <th class="pb-2">Protocol</th>
                                        <th class="pb-2">Source IP:Port</th>
                                        <th class="pb-2">Dest IP:Port</th>
                                        <th class="pb-2">State</th>
                                        <th class="pb-2">Timeout</th>
                                    </tr>
                                </thead>
                                <tbody class="text-emerald-400">
                                    <tr>
                                        <td class="pt-2">TCP</td>
                                        <td class="pt-2">192.168.1.50:54321</td>
                                        <td class="pt-2">93.184.216.34:443</td>
                                        <td class="pt-2">ESTABLISHED</td>
                                        <td class="pt-2">432000s</td>
                                    </tr>
                                    <tr>
                                        <td class="pt-2 text-blue-400">UDP</td>
                                        <td class="pt-2 text-blue-400">192.168.1.50:53</td>
                                        <td class="pt-2 text-blue-400">8.8.8.8:53</td>
                                        <td class="pt-2 text-blue-400">UNREPLIED</td>
                                        <td class="pt-2 text-blue-400">30s</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <p class="text-sm text-slate-400 mt-4">Because the firewall <em>knows</em> the connection is "ESTABLISHED", it automatically allows the inbound HTTP response from the server back to the user without needing an explicit inbound rule. It also tracks Sequence numbers to prevent TCP hijacking.</p>
                    </div>
                `
            },
            {
                title: "2. Forward vs Reverse Proxies",
                content: `
                    <p class="text-slate-300 mb-4">A proxy is a server that acts as an intermediary for requests from clients seeking resources from other servers.</p>
                    
                    <div class="grid md:grid-cols-2 gap-6">
                        <div class="bg-slate-900/40 p-6 rounded-xl border border-slate-700">
                            <h4 class="text-purple-400 font-bold mb-3 flex items-center gap-2"><i data-lucide="arrow-right-circle" class="w-5 h-5"></i> Forward Proxy</h4>
                            <p class="text-sm text-slate-400 mb-4">Protects the <strong>Client</strong>. It sits inside a corporate network and fetches internet resources on behalf of internal users.</p>
                            <ul class="text-sm text-slate-400 space-y-2">
                                <li><strong>Anonymity:</strong> The internet only sees the IP of the proxy, not the internal user.</li>
                                <li><strong>Content Filtering:</strong> The proxy can block access to malicious or non-work-related websites.</li>
                                <li><strong>Caching:</strong> If 100 users request the same file, the proxy downloads it once and serves it locally 99 times.</li>
                            </ul>
                        </div>
                        <div class="bg-slate-900/40 p-6 rounded-xl border border-slate-700">
                            <h4 class="text-rose-400 font-bold mb-3 flex items-center gap-2"><i data-lucide="arrow-left-circle" class="w-5 h-5"></i> Reverse Proxy (e.g., Nginx)</h4>
                            <p class="text-sm text-slate-400 mb-4">Protects the <strong>Server</strong>. It sits in front of backend web servers and handles all incoming internet traffic.</p>
                            <ul class="text-sm text-slate-400 space-y-2">
                                <li><strong>SSL Termination:</strong> The proxy handles the heavy math of decrypting HTTPS traffic, then forwards unencrypted HTTP traffic to backend servers, saving their CPU.</li>
                                <li><strong>Load Balancing:</strong> Distributes incoming traffic across dozens of backend servers.</li>
                                <li><strong>WAF:</strong> Can inspect the decrypted HTTP payload for SQL injection before passing it to the backend.</li>
                            </ul>
                        </div>
                    </div>
                `
            }
        ]
    },
    security_protocols: {
        title: "Cryptographic Protocols",
        icon: "lock",
        intro: "A technical deep dive into encryption math and how TLS secures the web.",
        sections: [
            {
                title: "1. The Mechanics of Encryption",
                content: `
                    <div class="bg-slate-900/50 p-6 rounded-xl border border-slate-800 mb-6">
                        <h4 class="text-blue-400 font-bold mb-3">Symmetric Encryption (e.g., AES-256)</h4>
                        <p class="text-sm text-slate-400 mb-3">Uses a single shared key. Data is chopped into "blocks" (e.g., 128 bits) and mathematically scrambled (substituted and permuted) over multiple "rounds" using the key.</p>
                        <ul class="text-sm text-slate-400 list-disc pl-5 mb-4">
                            <li><strong>Performance:</strong> Exceptionally fast. Can be processed in hardware by modern CPUs (AES-NI). Used for encrypting hard drives and bulk data streams.</li>
                            <li><strong>The Flaw:</strong> If Alice and Bob have never met, how does Alice securely send Bob the key over the internet without an attacker intercepting it?</li>
                        </ul>

                        <h4 class="text-emerald-400 font-bold mb-3 mt-6">Asymmetric Encryption (e.g., RSA, ECC)</h4>
                        <p class="text-sm text-slate-400 mb-3">Solves the key exchange problem using mathematically linked key pairs (Public and Private keys).</p>
                        <ul class="text-sm text-slate-400 list-disc pl-5">
                            <li><strong>The Math:</strong> Based on one-way mathematical trapdoors (like multiplying two massive prime numbers is easy, but factoring the resulting massive number back into primes is impossibly hard).</li>
                            <li><strong>Mechanism:</strong> Bob generates a key pair. He shares his Public Key with the world. Alice encrypts her message using Bob's Public Key. Once encrypted, <strong>only Bob's Private Key</strong> can decrypt it—not even Alice can decrypt her own message once locked.</li>
                            <li><strong>Performance:</strong> Very slow. Thousands of times slower than Symmetric encryption.</li>
                        </ul>
                    </div>
                `
            },
            {
                title: "2. The TLS 1.3 Handshake",
                content: `
                    <p class="text-slate-300 mb-4">Transport Layer Security uses <em>both</em> forms of encryption to get the best of both worlds. Here is the exact flow when you visit an HTTPS website:</p>
                    
                    <div class="bg-slate-950 p-6 rounded-xl border border-slate-800 font-mono text-xs text-slate-300">
                        <ol class="space-y-4">
                            <li>
                                <div class="text-emerald-400 font-bold">1. Client Hello</div>
                                <div class="text-slate-400">The browser sends a message to the server proposing cryptographic suites (e.g., TLS 1.3, AES-256-GCM, Elliptic Curve Diffie-Hellman) and a random string of bytes.</div>
                            </li>
                            <li>
                                <div class="text-blue-400 font-bold">2. Server Hello & Certificate</div>
                                <div class="text-slate-400">The server agrees on a cipher suite and sends its <strong>Digital Certificate</strong> (which contains the server's Public Key, cryptographically signed by a trusted Certificate Authority like Let's Encrypt).</div>
                            </li>
                            <li>
                                <div class="text-purple-400 font-bold">3. Authentication (Browser-side)</div>
                                <div class="text-slate-400">The browser verifies the Certificate Authority's signature against its internal list of trusted CAs. If valid, the browser trusts that the Public Key actually belongs to the server (preventing Man-in-the-Middle).</div>
                            </li>
                            <li>
                                <div class="text-amber-400 font-bold">4. Key Exchange (Diffie-Hellman)</div>
                                <div class="text-slate-400">Both sides use complex asymmetric math to independently calculate a shared <strong>"Pre-Master Secret"</strong> without ever actually transmitting it over the wire. From this secret, they derive the <strong>Symmetric Session Key</strong>.</div>
                            </li>
                            <li>
                                <div class="text-rose-400 font-bold">5. Secure Channel Established</div>
                                <div class="text-slate-400">The asymmetric heavy lifting is done. Both sides now switch to fast, symmetric AES encryption using the Session Key. HTTP traffic begins flowing securely.</div>
                            </li>
                        </ol>
                    </div>
                `
            }
        ]
    },
    ids_monitoring: {
        title: "Intrusion & Monitoring",
        icon: "radar",
        intro: "Visibility is the key to defense. Understanding how to detect, prevent, and log anomalous network activity.",
        sections: [
            {
                title: "1. IDS vs IPS Methodology",
                content: `
                    <p class="text-slate-300 mb-6">Firewalls evaluate headers (IPs/Ports). Intrusion systems (IDS/IPS) perform <strong>Deep Packet Inspection (DPI)</strong>, analyzing the actual payload of the traffic.</p>
                    
                    <div class="grid md:grid-cols-2 gap-6 mb-6">
                        <div class="bg-slate-900/40 p-6 rounded-xl border border-slate-700">
                            <h4 class="text-blue-400 font-bold mb-2">Signature-Based Detection</h4>
                            <p class="text-sm text-slate-400 mb-2">Operates like antivirus software. It maintains a massive database of known attack signatures (specific byte sequences of malware, exploit payloads, or SQL injection strings).</p>
                            <p class="text-sm text-slate-500 mt-2"><strong>Pros:</strong> Fast, highly accurate, low false positives.<br><strong>Cons:</strong> Completely blind to "Zero-Day" attacks that have no known signature yet.</p>
                        </div>
                        <div class="bg-slate-900/40 p-6 rounded-xl border border-slate-700">
                            <h4 class="text-purple-400 font-bold mb-2">Anomaly-Based Detection</h4>
                            <p class="text-sm text-slate-400 mb-2">Uses Machine Learning to establish a baseline of "normal" network behavior over weeks (e.g., bandwidth usage, protocol ratios). It alerts on statistical deviations.</p>
                            <p class="text-sm text-slate-500 mt-2"><strong>Pros:</strong> Can catch brand new Zero-Day exploits and insider threats.<br><strong>Cons:</strong> Computationally heavy, high rate of false positives if network behavior changes legitimately.</p>
                        </div>
                    </div>
                `
            },
            {
                title: "2. SIEM & Log Correlation",
                content: `
                    <h4 class="text-emerald-400 font-bold mb-2">Security Information and Event Management (SIEM)</h4>
                    <p class="text-sm text-slate-400 mb-4">A SIEM (e.g., Splunk, Elastic Security) is a massive data pipeline that centralizes logs from across the entire infrastructure to detect complex attacks that a single firewall would miss.</p>
                    
                    <div class="bg-slate-950 p-6 rounded-xl border border-slate-800">
                        <h5 class="text-slate-300 font-bold mb-3">The SIEM Pipeline:</h5>
                        <ul class="text-sm text-slate-400 space-y-3 list-decimal pl-5">
                            <li><strong>Ingestion:</strong> Agents (like Filebeat/Fluentd) installed on servers and firewalls stream logs to the central SIEM.</li>
                            <li><strong>Parsing & Normalization:</strong> The SIEM parses raw logs (using Grok/Regex) into standardized JSON. A Windows logon event and a Linux SSH event are mapped to the same generic "authentication_success" field.</li>
                            <li><strong>Correlation Rules:</strong> The security team writes rules. For example: <em>"If a user fails login 5 times on the VPN, and then successfully logs in, and then immediately accesses a high-value database within 2 minutes -> Generate Critical Alert."</em></li>
                            <li><strong>SOAR (Orchestration):</strong> Modern SIEMs can automatically trigger a script to block the attacker's IP on the firewall without human intervention.</li>
                        </ul>
                    </div>
                `
            }
        ]
    },
    devsecops: {
        title: "DevSecOps Pipeline",
        icon: "refresh-cw",
        intro: "Integrating security testing into the CI/CD deployment lifecycle (Shift-Left).",
        sections: [
            {
                title: "1. The Shift-Left Philosophy",
                content: `
                    <p class="text-slate-300 mb-6">In legacy environments, security was tested at the end of development. If a major flaw was found, release was delayed by weeks. <strong>Shift-Left</strong> integrates automated security testing directly into the developer's Git workflows.</p>
                `
            },
            {
                title: "2. Anatomy of a Secure CI/CD Pipeline",
                content: `
                    <div class="bg-slate-900/50 p-6 rounded-xl border border-slate-800 font-mono text-sm">
                        <p class="text-slate-400 mb-4">When a developer pushes code to GitHub, the following automated pipeline triggers. If any step fails, the deployment is blocked.</p>
                        
                        <div class="space-y-4">
                            <div class="border-l-2 border-slate-600 pl-4 relative">
                                <div class="absolute w-3 h-3 bg-slate-500 rounded-full -left-[7px] top-1"></div>
                                <div class="text-blue-400 font-bold">1. Secrets Scanning (e.g., TruffleHog)</div>
                                <div class="text-xs text-slate-400">Scans the commit history for AWS keys, API tokens, or hardcoded passwords using entropy analysis and regex.</div>
                            </div>
                            
                            <div class="border-l-2 border-slate-600 pl-4 relative">
                                <div class="absolute w-3 h-3 bg-slate-500 rounded-full -left-[7px] top-1"></div>
                                <div class="text-emerald-400 font-bold">2. SAST - Static Analysis (e.g., SonarQube)</div>
                                <div class="text-xs text-slate-400">Analyzes the raw source code without running it (White-box). Detects buffer overflows, missing input validation (SQLi), and bad crypto libraries.</div>
                            </div>

                            <div class="border-l-2 border-slate-600 pl-4 relative">
                                <div class="absolute w-3 h-3 bg-slate-500 rounded-full -left-[7px] top-1"></div>
                                <div class="text-amber-400 font-bold">3. SCA - Software Composition Analysis</div>
                                <div class="text-xs text-slate-400">Scans the package.json / requirements.txt. Compares third-party open-source dependencies against the CVE database to ensure no vulnerable libraries (like Log4j) are imported.</div>
                            </div>

                            <div class="border-l-2 border-slate-600 pl-4 relative">
                                <div class="absolute w-3 h-3 bg-slate-500 rounded-full -left-[7px] top-1"></div>
                                <div class="text-purple-400 font-bold">4. IaC Scanning (e.g., Checkov, tfsec)</div>
                                <div class="text-xs text-slate-400">Scans the Terraform/CloudFormation code. Blocks deployment if it detects a public S3 bucket or a Security Group open to 0.0.0.0/0.</div>
                            </div>

                            <div class="border-l-2 border-transparent pl-4 relative">
                                <div class="absolute w-3 h-3 bg-slate-500 rounded-full -left-[7px] top-1"></div>
                                <div class="text-rose-400 font-bold">5. DAST - Dynamic Analysis (e.g., OWASP ZAP)</div>
                                <div class="text-xs text-slate-400">The application is compiled and deployed to a staging environment. The DAST tool actively attacks it (Black-box), throwing malformed HTTP requests and XSS payloads to observe how the running app responds.</div>
                            </div>
                        </div>
                    </div>
                `
            }
        ]
    }
    """

    # We concatenate base_content, deep_dive_content, and the javascript closing/rendering part.
    # The javascript rendering part:
    js_footer = """
};

        const navTabs = document.getElementById('nav-tabs');
        const contentContainer = document.getElementById('content-container');
        let activeTab = 'vpn_basics';

        function renderTabs() {
            navTabs.innerHTML = Object.entries(contentData).map(([id, data]) => `
                <button onclick="switchTab('${id}')" 
                    id="tab-${id}"
                    class="tab-btn px-4 py-2 rounded-lg text-sm font-medium transition-all whitespace-nowrap flex items-center gap-2
                    ${activeTab === id ? 'bg-blue-600/20 text-blue-400 border border-blue-500/30 shadow-lg shadow-blue-500/20' : 'text-slate-400 hover:text-white hover:bg-slate-800 border border-transparent'}">
                    <i data-lucide="${data.icon}" class="w-4 h-4"></i>
                    ${data.title}
                </button>
            `).join('');
            lucide.createIcons();
        }

        function switchTab(tabId) {
            if (activeTab === tabId) return;
            activeTab = tabId;
            renderTabs();
            renderContent();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function renderContent() {
            const data = contentData[activeTab];
            let contentHtml = `
                <div class="fade-in">
                    <div class="mb-8">
                        <h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3 tracking-tight">${data.title}</h1>
                        <p class="text-lg text-slate-400 leading-relaxed">${data.intro}</p>
                    </div>
            `;

            data.sections.forEach(section => {
                contentHtml += `
                    <section class="space-y-6">
                        ${section.title ? `<h2 class="text-2xl font-bold text-white mb-4">${section.title}</h2>` : ''}
                        <div class="prose prose-invert max-w-none">
                            ${section.content}
                        </div>
                    </section>
                `;
            });

            contentHtml += `</div>`;
            contentContainer.innerHTML = contentHtml;
            lucide.createIcons();
        }

        // Setup back to top button visibility based on scroll
        window.addEventListener('scroll', () => {
            const backToTopBtn = document.querySelector('.back-to-top');
            if (window.scrollY > 500) {
                backToTopBtn.style.opacity = '1';
                backToTopBtn.style.pointerEvents = 'auto';
            } else {
                backToTopBtn.style.opacity = '0';
                backToTopBtn.style.pointerEvents = 'none';
            }
        });

        document.querySelector('.back-to-top').addEventListener('click', (e) => {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

        // Initialize 
        let backToTopBtn = document.querySelector('.back-to-top');
        backToTopBtn.style.opacity = '0';
        backToTopBtn.style.pointerEvents = 'none';

        lucide.createIcons();
        renderTabs();
        renderContent();
    </script>
</body>

</html>
"""

    final_content = base_content + deep_dive_content + js_footer
    
    # Wait! base_content contains the start of the file all the way to `vpn_architectures: { ... }`.
    # Let's ensure the regex actually worked. We will write to a temp file first.
    with open("Network_Security_Guide_temp.html", "w") as f:
        f.write(final_content)
        
    print("Injection successful.")
else:
    print("Could not find the match for base_content!")

