import sys

html_content = """    <!-- Text Editors (Vim) -->
    <section id="sec-editors" class="tab-content hidden space-y-12 fade-in">
      
      <div class="flex items-center gap-4 border-b border-slate-700 pb-4">
        <div class="p-3 bg-blue-500/10 rounded-xl">
          <i data-lucide="edit-3" class="w-8 h-8 text-blue-500"></i>
        </div>
        <h2 class="text-2xl font-bold text-white">Text Editors (Vim)</h2>
      </div>

      <!-- Overview -->
      <div class="bg-slate-800 border border-slate-700 rounded-2xl p-6 shadow-lg">
        <h3 class="text-xl font-semibold text-white mb-4 flex items-center gap-2">
          <i data-lucide="terminal" class="w-5 h-5 text-blue-400"></i>
          The <code class="bg-slate-900 text-blue-300 px-2 py-0.5 rounded ml-2">vim</code> Command
        </h3>
        <p class="text-slate-300 leading-relaxed mb-4">
          The <code class="text-amber-400">vim</code> command invokes the Vim editor. When entered without a file name as an argument, it opens a welcome screen by default. To open a file, use the syntax <code class="text-emerald-400 bg-slate-900 px-2 py-0.5 rounded">vim {file name}</code>. If the file does not exist, vim creates a file by the name specified and opens it for editing. The Vim editor supports multiple files being opened simultaneously.
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
          
          <!-- Modes -->
          <div class="bg-slate-900/50 p-5 rounded-xl border border-slate-700/50">
            <h4 class="text-lg font-semibold text-white mb-3">Vim Modes</h4>
            <p class="text-slate-400 text-sm mb-4">The default mode is <strong>Command</strong> mode. You can switch to different modes using keystrokes.</p>
            <ul class="space-y-3">
              <li class="flex items-start gap-3 text-sm">
                <span class="px-2 py-1 bg-amber-500/20 text-amber-400 font-mono rounded text-xs mt-0.5 w-16 text-center">Insert</span>
                <span class="text-slate-300">Allows users to insert text by typing.</span>
              </li>
              <li class="flex items-start gap-3 text-sm">
                <span class="px-2 py-1 bg-blue-500/20 text-blue-400 font-mono rounded text-xs mt-0.5 w-16 text-center">Execute</span>
                <span class="text-slate-300">Allows users to execute commands (starting with <code class="text-white">:</code>).</span>
              </li>
              <li class="flex items-start gap-3 text-sm">
                <span class="px-2 py-1 bg-emerald-500/20 text-emerald-400 font-mono rounded text-xs mt-0.5 w-16 text-center">Command</span>
                <span class="text-slate-300">Default mode. Perform editing actions using single keystrokes.</span>
              </li>
              <li class="flex items-start gap-3 text-sm">
                <span class="px-2 py-1 bg-purple-500/20 text-purple-400 font-mono rounded text-xs mt-0.5 w-16 text-center">Visual</span>
                <span class="text-slate-300">Highlight or select text for copying, deleting, etc.</span>
              </li>
            </ul>
          </div>

          <!-- Mode Switching -->
          <div class="bg-slate-900/50 p-5 rounded-xl border border-slate-700/50">
            <h4 class="text-lg font-semibold text-white mb-3">Switching Modes</h4>
            <div class="space-y-2">
              <div class="flex items-center justify-between p-2 hover:bg-slate-800 rounded-lg transition-colors text-sm">
                <span class="text-slate-300">Insert mode (left of cursor)</span>
                <code class="text-amber-400 bg-slate-950 px-2 py-1 rounded">i</code>
              </div>
              <div class="flex items-center justify-between p-2 hover:bg-slate-800 rounded-lg transition-colors text-sm">
                <span class="text-slate-300">Insert mode (end of line)</span>
                <code class="text-amber-400 bg-slate-950 px-2 py-1 rounded">A</code>
              </div>
              <div class="flex items-center justify-between p-2 hover:bg-slate-800 rounded-lg transition-colors text-sm">
                <span class="text-slate-300">Insert mode (new line below)</span>
                <code class="text-amber-400 bg-slate-950 px-2 py-1 rounded">o</code>
              </div>
              <div class="flex items-center justify-between p-2 hover:bg-slate-800 rounded-lg transition-colors text-sm">
                <span class="text-slate-300">Visual mode (character)</span>
                <code class="text-purple-400 bg-slate-950 px-2 py-1 rounded">v</code>
              </div>
              <div class="flex items-center justify-between p-2 hover:bg-slate-800 rounded-lg transition-colors text-sm">
                <span class="text-slate-300">Execute mode</span>
                <code class="text-blue-400 bg-slate-950 px-2 py-1 rounded">:</code>
              </div>
              <div class="flex items-center justify-between p-2 hover:bg-slate-800 rounded-lg transition-colors text-sm">
                <span class="text-slate-300 font-medium">Return to Command mode</span>
                <code class="text-emerald-400 bg-slate-950 px-2 py-1 rounded">Esc</code>
              </div>
            </div>
          </div>
          
        </div>
      </div>

      <!-- Grid of commands -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        <!-- Execute Mode Commands -->
        <div class="bg-slate-800 border border-slate-700 rounded-2xl p-5 shadow-lg">
          <h3 class="text-lg font-semibold text-white mb-4 flex items-center gap-2">
            <i data-lucide="play-circle" class="w-5 h-5 text-emerald-400"></i>
            Execute Commands
          </h3>
          <p class="text-sm text-slate-400 mb-4">Start by typing <code class="text-white">:</code> in Command mode.</p>
          <div class="space-y-2">
            <div class="flex flex-col p-2 bg-slate-900/50 rounded-lg border border-slate-700/50">
              <code class="text-amber-400 font-bold mb-1">:w {file}</code>
              <span class="text-slate-300 text-xs">Saves a file.</span>
            </div>
            <div class="flex flex-col p-2 bg-slate-900/50 rounded-lg border border-slate-700/50">
              <code class="text-emerald-400 font-bold mb-1">:q</code>
              <span class="text-slate-300 text-xs">Quits (if no changes since last save).</span>
            </div>
            <div class="flex flex-col p-2 bg-slate-900/50 rounded-lg border border-slate-700/50">
              <code class="text-rose-400 font-bold mb-1">:q!</code>
              <span class="text-slate-300 text-xs">Quits, ignoring changes.</span>
            </div>
            <div class="flex flex-col p-2 bg-slate-900/50 rounded-lg border border-slate-700/50">
              <code class="text-blue-400 font-bold mb-1">:wq</code>
              <span class="text-slate-300 text-xs">Saves current file and exits.</span>
            </div>
            <div class="flex flex-col p-2 bg-slate-900/50 rounded-lg border border-slate-700/50">
              <code class="text-purple-400 font-bold mb-1">ZZ</code>
              <span class="text-slate-300 text-xs">Writes if changes made & quits (no colon).</span>
            </div>
          </div>
        </div>

        <!-- Motions -->
        <div class="bg-slate-800 border border-slate-700 rounded-2xl p-5 shadow-lg">
          <h3 class="text-lg font-semibold text-white mb-4 flex items-center gap-2">
            <i data-lucide="move" class="w-5 h-5 text-blue-400"></i>
            Motions (Navigation)
          </h3>
          <p class="text-sm text-slate-400 mb-4">Single-key shortcuts used in Command mode.</p>
          <div class="space-y-1 text-sm">
            <div class="flex justify-between items-center p-1.5 hover:bg-slate-700/50 rounded">
              <span class="text-slate-300">Left, Down, Up, Right</span>
              <code class="text-amber-400 bg-slate-900 px-1.5 rounded">h, j, k, l</code>
            </div>
            <div class="flex justify-between items-center p-1.5 hover:bg-slate-700/50 rounded">
              <span class="text-slate-300">Start / End of line</span>
              <code class="text-amber-400 bg-slate-900 px-1.5 rounded">^ / $</code>
            </div>
            <div class="flex justify-between items-center p-1.5 hover:bg-slate-700/50 rounded">
              <span class="text-slate-300">Next / Prev word</span>
              <code class="text-amber-400 bg-slate-900 px-1.5 rounded">w / b</code>
            </div>
            <div class="flex justify-between items-center p-1.5 hover:bg-slate-700/50 rounded">
              <span class="text-slate-300">First / Last line</span>
              <code class="text-emerald-400 bg-slate-900 px-1.5 rounded">gg / Shift+G</code>
            </div>
            <div class="flex justify-between items-center p-1.5 hover:bg-slate-700/50 rounded">
              <span class="text-slate-300">Top / Bottom of screen</span>
              <code class="text-blue-400 bg-slate-900 px-1.5 rounded">Shift+H / Shift+L</code>
            </div>
            <div class="flex justify-between items-center p-1.5 hover:bg-slate-700/50 rounded">
              <span class="text-slate-300">Go to specific line</span>
              <code class="text-purple-400 bg-slate-900 px-1.5 rounded">{line} Shift+G</code>
            </div>
          </div>
        </div>

        <!-- Editing Operators -->
        <div class="bg-slate-800 border border-slate-700 rounded-2xl p-5 shadow-lg">
          <h3 class="text-lg font-semibold text-white mb-4 flex items-center gap-2">
            <i data-lucide="scissors" class="w-5 h-5 text-rose-400"></i>
            Editing Operators
          </h3>
          <p class="text-sm text-slate-400 mb-4">Manipulate text (case-sensitive!).</p>
          <div class="space-y-1 text-sm">
            <div class="flex justify-between items-center p-1.5 hover:bg-slate-700/50 rounded">
              <span class="text-slate-300">Cut character</span>
              <code class="text-amber-400 bg-slate-900 px-1.5 rounded">x</code>
            </div>
            <div class="flex justify-between items-center p-1.5 hover:bg-slate-700/50 rounded">
              <span class="text-slate-300">Delete current line</span>
              <code class="text-rose-400 bg-slate-900 px-1.5 rounded">dd</code>
            </div>
            <div class="flex justify-between items-center p-1.5 hover:bg-slate-700/50 rounded">
              <span class="text-slate-300">Paste (below / above)</span>
              <code class="text-blue-400 bg-slate-900 px-1.5 rounded">p / P</code>
            </div>
            <div class="flex justify-between items-center p-1.5 hover:bg-slate-700/50 rounded">
              <span class="text-slate-300">Search forward / backward</span>
              <code class="text-emerald-400 bg-slate-900 px-1.5 rounded">/text  ?text</code>
            </div>
            <div class="flex justify-between items-center p-1.5 hover:bg-slate-700/50 rounded">
              <span class="text-slate-300">Yank (copy) line</span>
              <code class="text-amber-400 bg-slate-900 px-1.5 rounded">yy</code>
            </div>
            <div class="flex justify-between items-center p-1.5 hover:bg-slate-700/50 rounded">
              <span class="text-slate-300">Undo (latest / line)</span>
              <code class="text-purple-400 bg-slate-900 px-1.5 rounded">u / U</code>
            </div>
          </div>
        </div>

      </div>
    </section>
"""

with open("/home/neehar/learning_devops/Linux/linux_commands.html", "r") as f:
    content = f.read()

# Insert before </main>
content = content.replace("  </main>", html_content + "\n  </main>")

# Add the new tab
tab_replacement = """      { id: 'docs', title: 'Help & Docs', icon: 'book-open' },
      { id: 'editors', title: 'Text Editors', icon: 'edit-3' }
    ];"""
content = content.replace("      { id: 'docs', title: 'Help & Docs', icon: 'book-open' }\n    ];", tab_replacement)

with open("/home/neehar/learning_devops/Linux/linux_commands.html", "w") as f:
    f.write(content)

