import sys

html_content = """
      <!-- User Account Creation Deep Dive -->
      <div class="mt-6 bg-slate-800 border border-slate-700 rounded-2xl p-6 shadow-lg">
        <h3 class="text-xl font-semibold text-white mb-4 border-b border-slate-700 pb-2 flex items-center gap-2">
          <i data-lucide="user-plus" class="w-5 h-5 text-purple-400"></i>
          Creating User Accounts
        </h3>
        
        <p class="text-slate-300 text-sm mb-6 leading-relaxed">
          A user account is a collection of information that defines a user on a system. It includes the username, password, groups, and access rights. 
          When an account is created, it is assigned a unique <strong class="text-white">User ID (UID)</strong>. Usernames and UIDs must be completely unique on the computer. By default, a <strong class="text-white">User Private Group (UPG)</strong> is also created with the same name as the user.
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
          <!-- useradd vs adduser -->
          <div class="bg-slate-900/50 p-5 rounded-xl border border-slate-700/50">
            <h4 class="text-lg font-bold text-purple-400 font-mono mb-3">useradd vs adduser</h4>
            <ul class="space-y-4 text-sm">
              <li>
                <code class="text-purple-300 font-mono bg-slate-950 px-1.5 py-0.5 rounded block mb-1">useradd</code>
                <p class="text-slate-400">A low-level utility. It creates the user and private group, but by default it <strong>does not</strong> create a home directory or prompt for a password. (An account with no password is disabled).</p>
              </li>
              <li>
                <code class="text-purple-300 font-mono bg-slate-950 px-1.5 py-0.5 rounded block mb-1">adduser</code>
                <p class="text-slate-400">A high-level, interactive script. It automatically sets up the home directory, prompts you to set a password, and asks for optional contact information.</p>
              </li>
            </ul>
          </div>

          <!-- Special / System Accounts -->
          <div class="bg-slate-900/50 p-5 rounded-xl border border-slate-700/50">
            <h4 class="text-lg font-bold text-purple-400 mb-3">Special / Daemon Accounts</h4>
            <p class="text-slate-400 text-sm mb-3">
              Some accounts aren't intended for real people, but are instead used by services or daemons (like a backup service). 
            </p>
            <ul class="list-disc list-inside text-slate-400 text-sm space-y-2 mb-3">
              <li>They typically have a UID less than 1000 (e.g., 998).</li>
              <li>They usually do not have a home directory.</li>
            </ul>
            <div class="bg-slate-950 p-3 rounded border border-slate-800">
              <code class="text-emerald-400 text-xs font-mono">sudo useradd -r backup_account</code>
              <p class="text-slate-500 text-xs mt-1">The <code>-r</code> flag creates a system account.</p>
            </div>
          </div>
        </div>

        <!-- Important Files -->
        <div class="bg-slate-900/30 p-5 rounded-xl border border-slate-700">
          <h4 class="text-md font-semibold text-slate-200 mb-3">Important Identity Files (Viewable via <code class="text-purple-400 text-sm">sudo cat</code>)</h4>
          <div class="space-y-3 text-sm">
            <div class="flex items-start gap-3">
              <code class="text-amber-400 font-mono w-32 flex-shrink-0">/etc/passwd</code>
              <span class="text-slate-400">Contains user details: Username, UID, primary GID, home directory path, and default shell (e.g., <code class="text-slate-300">/bin/bash</code>).</span>
            </div>
            <div class="flex items-start gap-3">
              <code class="text-amber-400 font-mono w-32 flex-shrink-0">/etc/group</code>
              <span class="text-slate-400">Contains group details: Group name, password placeholder, GID, and a list of supplementary users in the group.</span>
            </div>
          </div>
        </div>
      </div>
"""

with open("/home/neehar/learning_devops/Linux/linux_permissions.html", "r") as f:
    content = f.read()

# Insert before </section>\n\n  </main>
content = content.replace("      </div>\n    </section>", "      </div>" + html_content + "\n    </section>")

with open("/home/neehar/learning_devops/Linux/linux_permissions.html", "w") as f:
    f.write(content)

