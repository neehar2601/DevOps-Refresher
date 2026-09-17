import re

with open("Network_Security_Guide.html", "r") as f:
    content = f.read()

new_tabs = """
    },
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
                title: "1. Security Groups vs NACLs",
                content: `
                    <p class="text-slate-300 mb-6">In cloud environments (like AWS VPCs), traditional firewalls are abstracted into two main layers of defense: Security Groups and Network ACLs.</p>
                    
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
                                    <td class="p-3">Operates at the <strong>Instance/VM</strong> level.</td>
                                    <td class="p-3">Operates at the <strong>Subnet</strong> level.</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-bold text-slate-300">Statefulness</td>
                                    <td class="p-3"><strong class="text-emerald-400">Stateful:</strong> If you allow inbound traffic on Port 80, the return outbound traffic is automatically allowed.</td>
                                    <td class="p-3"><strong class="text-blue-400">Stateless:</strong> You must explicitly write rules for both inbound AND outbound traffic.</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-bold text-slate-300">Rule Logic</td>
                                    <td class="p-3"><strong>Allow rules only.</strong> All other traffic is implicitly denied by default.</td>
                                    <td class="p-3">Supports both <strong>Allow and Deny</strong> rules. Processed in numbered order (e.g., Rule #100 evaluates before #200).</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-bold text-slate-300">Primary Use Case</td>
                                    <td class="p-3">Defining what a specific application/server can talk to. (e.g., Web Server SG allows inbound 443).</td>
                                    <td class="p-3">Broad subnet-level defense. (e.g., Blocking a specific malicious IP block from entering the entire subnet).</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                `
            },
            {
                title: "2. Secrets Management",
                content: `
                    <div class="info-box border-rose-500 bg-rose-500/5 mb-6">
                        <strong class="text-rose-400">The Problem: Hardcoded Credentials</strong>
                        <p class="text-sm text-slate-300">Historically, developers hardcoded database passwords or API keys directly into configuration files or source code. If the code was leaked or pushed to a public GitHub repository, the entire infrastructure was compromised.</p>
                    </div>

                    <h4 class="text-blue-400 font-bold mb-3">The Solution: Vaults & Dynamic Secrets</h4>
                    <p class="text-sm text-slate-400 mb-4">In a DevOps lifecycle, credentials must be handled programmatically by machines. Tools like <strong>HashiCorp Vault</strong>, <strong>AWS Secrets Manager</strong>, or <strong>Azure Key Vault</strong> are used to centrally manage secrets.</p>
                    
                    <ul class="text-sm text-slate-400 space-y-2 list-disc pl-5">
                        <li><strong>Encryption at Rest:</strong> The vault stores secrets heavily encrypted.</li>
                        <li><strong>Programmatic Retrieval:</strong> The application authenticates with the Vault (using an IAM role or token) at runtime to fetch the database password in memory.</li>
                        <li><strong>Dynamic Secrets:</strong> Advanced vaults can generate short-lived, temporary passwords on the fly (e.g., a DB password that expires in 1 hour). If the secret is leaked, it becomes useless quickly.</li>
                    </ul>
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
                title: "1. IDS vs IPS",
                content: `
                    <p class="text-slate-300 mb-6">Firewalls decide whether to allow a packet through based on IP/Port. Intrusion systems look deeper—they inspect the <strong>payload</strong> of the packet for known malicious signatures or anomalous behavioral patterns (like someone attempting a SQL Injection).</p>
                    
                    <div class="grid md:grid-cols-2 gap-6 mb-6">
                        <div class="bg-slate-900/40 p-6 rounded-xl border border-slate-700">
                            <h4 class="text-amber-400 font-bold mb-2 flex items-center gap-2"><i data-lucide="eye" class="w-5 h-5"></i> IDS (Intrusion Detection System)</h4>
                            <p class="text-sm text-slate-400 mb-2"><strong>Passive Monitoring.</strong> An IDS receives a copy of the network traffic (via a span port or packet mirror).</p>
                            <p class="text-sm text-slate-400">It analyzes the traffic and raises an alert if it detects an attack, but it <strong>cannot stop</strong> the attack because it is not inline with the traffic flow.</p>
                        </div>
                        <div class="bg-slate-900/40 p-6 rounded-xl border border-slate-700">
                            <h4 class="text-rose-400 font-bold mb-2 flex items-center gap-2"><i data-lucide="shield-alert" class="w-5 h-5"></i> IPS (Intrusion Prevention System)</h4>
                            <p class="text-sm text-slate-400 mb-2"><strong>Active Blocking.</strong> An IPS sits directly inline with the traffic flow (often built into a Next-Gen Firewall).</p>
                            <p class="text-sm text-slate-400">If it detects an attack payload, it immediately drops the packet and resets the connection, stopping the attack in its tracks.</p>
                        </div>
                    </div>
                `
            },
            {
                title: "2. SIEM & Centralized Logging",
                content: `
                    <h4 class="text-blue-400 font-bold mb-2">Security Information and Event Management (SIEM)</h4>
                    <p class="text-sm text-slate-400 mb-4">In a sprawling network, you might have hundreds of servers, firewalls, routers, and applications, all generating log files. If an attacker breaches the network, they will likely touch multiple systems.</p>
                    
                    <p class="text-sm text-slate-400 mb-6">A <strong>SIEM</strong> (like Splunk, ELK Stack, or Datadog Security) aggregates logs from <em>all</em> devices into a centralized dashboard. It uses correlation rules and AI to connect the dots. For example:</p>

                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs text-slate-300">
                        <div class="text-slate-500 mb-2">// How a SIEM correlates events to detect a breach:</div>
                        <div class="text-blue-400">1. Firewall Log: 50 failed SSH login attempts from an external IP in Russia.</div>
                        <div class="text-rose-400">2. Firewall Log: 1 successful SSH login from the same IP (Brute force successful).</div>
                        <div class="text-emerald-400">3. Server OS Log: User 'admin' escalated to 'root' privileges.</div>
                        <div class="text-amber-400">4. Network Log: Server initiated a massive 5GB outbound data transfer to an unknown IP.</div>
                        <div class="mt-4 text-rose-500 font-bold">=> SIEM ALERT GENERATED: Likely Data Exfiltration via Compromised Host.</div>
                    </div>
                `
            }
        ]
    },
    devsecops: {
        title: "DevSecOps & CI/CD",
        icon: "refresh-cw",
        intro: "Integrating security directly into the software development and deployment lifecycle.",
        sections: [
            {
                title: "1. The 'Shift-Left' Paradigm",
                content: `
                    <p class="text-slate-300 mb-4">Historically, security was the final phase before a product was released. If a critical vulnerability was found by the security team at the very end, developers had to rip apart the code to fix it, causing massive delays.</p>
                    <p class="text-slate-300 mb-6"><strong>"Shift-Left"</strong> means moving security testing to the left on the timeline—integrating it as early as the coding phase and automating it within the CI/CD pipeline.</p>
                `
            },
            {
                title: "2. Automated Pipeline Security Testing",
                content: `
                    <div class="grid md:grid-cols-2 gap-6 mb-6">
                        <div class="bg-slate-900/40 p-6 rounded-xl border border-slate-700">
                            <h4 class="text-purple-400 font-bold mb-2">SAST (Static Analysis)</h4>
                            <p class="text-sm text-slate-400 mb-2">Static Application Security Testing (White-Box Testing).</p>
                            <p class="text-sm text-slate-400">Scans the application's <strong>source code</strong> at rest (before compiling) to find known vulnerabilities, hardcoded secrets, or bad coding practices (like missing input validation that causes SQL injection). Tools include SonarQube.</p>
                        </div>
                        <div class="bg-slate-900/40 p-6 rounded-xl border border-slate-700">
                            <h4 class="text-emerald-400 font-bold mb-2">DAST (Dynamic Analysis)</h4>
                            <p class="text-sm text-slate-400 mb-2">Dynamic Application Security Testing (Black-Box Testing).</p>
                            <p class="text-sm text-slate-400">Interacts with the application while it is <strong>running</strong> in a staging environment. It simulates attacks (like submitting malicious payloads to web forms) from the outside to see how the app behaves.</p>
                        </div>
                    </div>
                `
            },
            {
                title: "3. Infrastructure as Code (IaC) Security",
                content: `
                    <p class="text-slate-300 mb-4">In modern DevOps, networks and servers are provisioned using code (e.g., Terraform, AWS CloudFormation, Ansible). This is extremely powerful, but a single typo can deploy 1,000 servers with a port 22 open to the world.</p>
                    
                    <ul class="text-sm text-slate-400 space-y-2 list-disc pl-5">
                        <li><strong>IaC Scanning:</strong> Tools like <em>Checkov</em> or <em>tfsec</em> scan Terraform files inside the CI/CD pipeline.</li>
                        <li><strong>Pipeline Blockers:</strong> If the IaC scanner detects a misconfiguration (e.g., an S3 bucket is set to 'Public Read', or a Security Group allows '0.0.0.0/0'), the pipeline fails automatically. The infrastructure is <strong>never deployed</strong> until the code is fixed.</li>
                    </ul>
                `
            }
        ]
    }
"""

last_brace_idx = content.rfind("};")
if last_brace_idx != -1:
    # Inject right before `};`
    modified_content = re.sub(r'    }\n};\s*const navTabs', new_tabs + '\n};\n\n        const navTabs', content)
    
    with open("Network_Security_Guide.html", "w") as f:
        f.write(modified_content)
        
    print("Injection successful.")
else:
    print("Could not find };")

