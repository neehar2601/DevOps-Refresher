import json

with open("Networking/Networking-Tools-Guide.html", "r") as f:
    content = f.read()

# Extract top part
top_part = content.split("const contentData = {")[0]

# Extract bottom part (after the end of contentData)
# We know it ends before "let activeTab"
bottom_part_idx = content.find("        let activeTab = Object.keys(contentData)[0];")
# Find the closing "};" before activeTab
while content[bottom_part_idx - 1] != '}':
    bottom_part_idx -= 1
bottom_part_idx -= 1 # point to '}'
bottom_part = content[bottom_part_idx:]

# Customize top part
top_part = top_part.replace("Networking Tools Guide", "Network Security Guide")
top_part = top_part.replace("Linux Networking Tools\n                Complete Guide", "Network Security & VPN Guide")
top_part = top_part.replace("Linux Networking Tools Complete Guide", "Network Security & VPN Guide")
top_part = top_part.replace("Network Security Guide - Networking Hub", "Network Security Guide")
# wait, title replacement
top_part = top_part.replace("<title>Networking Tools Guide", "<title>Network Security Guide")


vpn_content = """const contentData = {
    vpn_basics: {
        title: "Virtual Private Networks (VPN)",
        icon: "shield-check",
        intro: "A Virtual Private Network (VPN) creates a secure, encrypted connection (tunnel) over a less secure network, such as the public internet.",
        sections: [
            {
                title: "What is a VPN?",
                content: `
                    <p>A VPN extends a private network across a public network, allowing users to send and receive data across shared or public networks as if their computing devices were directly connected to the private network. This provides enhanced security, privacy, and access to internal resources.</p>
                    
                    <div class="my-8 bg-slate-950/50 p-6 rounded-xl border border-slate-800">
                        <h4 class="text-sm font-bold text-slate-400 mb-4 uppercase tracking-wider text-center">How a VPN Tunnel Works</h4>
                        <div class="flex items-center justify-center gap-2 font-mono text-center overflow-x-auto pb-2">
                            <div class="flex flex-col items-center">
                                <div class="text-emerald-400 text-xl md:text-2xl font-bold bg-slate-900/80 px-4 py-3 rounded border border-emerald-500/30 flex items-center gap-2">
                                    <i data-lucide="laptop" class="w-5 h-5"></i> Remote Client
                                </div>
                                <div class="text-xs uppercase tracking-wider text-emerald-400/80 mt-2 font-sans font-bold">Unsecured Network (Home/Cafe)</div>
                            </div>
                            
                            <div class="flex flex-col items-center flex-1 px-4 min-w-[150px]">
                                <div class="w-full relative h-8 flex items-center">
                                    <!-- Outer tube (The Internet) -->
                                    <div class="absolute inset-0 border-y-2 border-slate-700 w-full rounded-sm"></div>
                                    <!-- Inner tube (The Encrypted VPN Tunnel) -->
                                    <div class="absolute left-0 right-0 h-4 top-2 bg-blue-500/20 border-y border-blue-400 border-dashed rounded-full overflow-hidden">
                                        <div class="w-full h-full bg-gradient-to-r from-transparent via-blue-400/50 to-transparent animate-[simBarShift_2s_linear_infinite]"></div>
                                    </div>
                                    <i data-lucide="lock" class="absolute left-1/2 -translate-x-1/2 w-4 h-4 text-blue-400 bg-slate-900 rounded-full"></i>
                                </div>
                                <div class="text-xs uppercase tracking-wider text-blue-400/80 mt-3 font-sans font-bold">Encrypted VPN Tunnel over Internet</div>
                            </div>
                            
                            <div class="flex flex-col items-center">
                                <div class="text-amber-400 text-xl md:text-2xl font-bold bg-slate-900/80 px-4 py-3 rounded border border-amber-500/30 flex items-center gap-2">
                                    <i data-lucide="server" class="w-5 h-5"></i> VPN Gateway
                                </div>
                                <div class="text-xs uppercase tracking-wider text-amber-400/80 mt-2 font-sans font-bold">Corporate Network (Secure)</div>
                            </div>
                        </div>
                    </div>
                `
            },
            {
                title: "Primary Types of VPNs",
                content: `
                    <div class="comparison-grid">
                        <div class="comparison-card border-blue-500/30">
                            <h4 class="text-blue-400 flex items-center gap-2"><i data-lucide="users" class="w-5 h-5"></i> Remote Access VPN</h4>
                            <p class="text-sm text-slate-400">Connects individual users (e.g., remote workers) securely to a private corporate network over the internet. The user typically needs a VPN client software installed on their device.</p>
                            <ul class="text-sm mt-3 space-y-1">
                                <li><strong>Client:</strong> Requires VPN software (e.g., Cisco AnyConnect, OpenVPN client).</li>
                                <li><strong>Use Case:</strong> Employee working from home accessing internal company tools.</li>
                                <li><strong>Common Protocols:</strong> SSL/TLS, IPsec.</li>
                            </ul>
                        </div>
                        <div class="comparison-card border-emerald-500/30">
                            <h4 class="text-emerald-400 flex items-center gap-2"><i data-lucide="network" class="w-5 h-5"></i> Site-to-Site VPN</h4>
                            <p class="text-sm text-slate-400">Connects entire networks to each other. For example, connecting a branch office network to the main headquarters network. The connection is handled seamlessly by routers.</p>
                            <ul class="text-sm mt-3 space-y-1">
                                <li><strong>Client:</strong> No client software needed on user devices; handled by the VPN Gateway/Router.</li>
                                <li><strong>Use Case:</strong> A retail branch connecting to the central corporate datacenter.</li>
                                <li><strong>Common Protocols:</strong> IPsec, GRE.</li>
                            </ul>
                        </div>
                    </div>
                `
            },
            {
                title: "Common VPN Protocols",
                content: `
                    <table>
                        <thead>
                            <tr>
                                <th>Protocol</th>
                                <th>Layer</th>
                                <th>Description & Purpose</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><code class="text-blue-400">IPsec</code><br><span class="text-xs text-slate-500">(Internet Protocol Security)</span></td>
                                <td>Layer 3 (Network)</td>
                                <td>Highly secure suite of protocols widely used for Site-to-Site VPNs. Operates at the network layer, meaning it encrypts the entire IP packet. Complex to configure but very robust.</td>
                            </tr>
                            <tr>
                                <td><code class="text-amber-400">SSL/TLS</code><br><span class="text-xs text-slate-500">(Secure Sockets Layer)</span></td>
                                <td>Layer 4+ (Transport/App)</td>
                                <td>Used predominantly for Remote Access VPNs (like OpenVPN). Much easier to deploy because it can operate through standard web browsers (HTTPS) and passes easily through NAT/firewalls.</td>
                            </tr>
                            <tr>
                                <td><code class="text-emerald-400">WireGuard</code></td>
                                <td>Layer 3 (Network)</td>
                                <td>A modern, extremely fast, and lean VPN protocol. It uses state-of-the-art cryptography and has a tiny codebase compared to IPsec/OpenVPN, making it easier to audit and highly performant.</td>
                            </tr>
                            <tr>
                                <td><code class="text-slate-400">L2TP/IPsec</code><br><span class="text-xs text-slate-500">(Layer 2 Tunneling Protocol)</span></td>
                                <td>Layer 2 + Layer 3</td>
                                <td>L2TP does not provide encryption itself, so it is almost always paired with IPsec. It's an older protocol that is widely supported natively on mobile devices and legacy operating systems.</td>
                            </tr>
                        </tbody>
                    </table>
                `
            }
        ]
    }
"""

final_html = top_part + vpn_content + bottom_part

with open("Networking/Network_Security_Guide.html", "w") as f:
    f.write(final_html)

