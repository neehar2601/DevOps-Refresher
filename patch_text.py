import sys

html_content = """    <!-- Text Processing & Regex -->
    <section id="sec-text" class="tab-content hidden space-y-12 fade-in">
      
      <div class="flex items-center gap-4 border-b border-slate-700 pb-4">
        <div class="p-3 bg-pink-500/10 rounded-xl">
          <i data-lucide="file-text" class="w-8 h-8 text-pink-500"></i>
        </div>
        <h2 class="text-2xl font-bold text-white">Text Processing & Diff</h2>
      </div>

      <!-- File Comparison & Diff -->
      <div class="bg-slate-800 border border-slate-700 rounded-2xl p-6 shadow-lg">
        <h3 class="text-xl font-semibold text-white mb-4 flex items-center gap-2">
          <i data-lucide="split-square-horizontal" class="w-5 h-5 text-pink-400"></i>
          File Comparison Utilities
        </h3>
        <p class="text-slate-300 leading-relaxed mb-6">
          Linux provides powerful utilities to compare files, find differences, and merge changes. 
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- diff -->
          <div class="bg-slate-900/50 p-5 rounded-xl border border-slate-700/50">
            <h4 class="text-lg font-bold text-amber-400 font-mono mb-2">diff</h4>
            <p class="text-slate-300 text-sm mb-3">Compares two files line by line and outputs the differences. It shows what needs to be changed to make the files identical.</p>
            <div class="bg-slate-950 p-3 rounded-lg border border-slate-800">
              <code class="text-sm text-slate-300">diff file1.txt file2.txt</code>
            </div>
          </div>

          <!-- vimdiff -->
          <div class="bg-slate-900/50 p-5 rounded-xl border border-slate-700/50">
            <h4 class="text-lg font-bold text-blue-400 font-mono mb-2">vimdiff</h4>
            <p class="text-slate-300 text-sm mb-3">Opens multiple files in Vim using split windows, highlighting differences side-by-side. Excellent for interactive resolving.</p>
            <div class="bg-slate-950 p-3 rounded-lg border border-slate-800">
              <code class="text-sm text-slate-300">vimdiff file1.txt file2.txt</code>
            </div>
          </div>
        </div>
      </div>

      <!-- Analysis & Spelling -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        
        <!-- wc -->
        <div class="bg-slate-800 border border-slate-700 rounded-2xl p-6 shadow-lg">
          <h3 class="font-bold text-white mb-3 text-lg border-b border-slate-700 pb-2 flex items-center gap-2">
            <i data-lucide="bar-chart-2" class="w-5 h-5 text-emerald-400"></i>
            Word Count (wc)
          </h3>
          <p class="text-slate-400 text-sm mb-4">
            Prints newline, word, and byte counts for a file.
          </p>
          <ul class="space-y-3 text-sm">
            <li class="flex items-center justify-between p-2 bg-slate-900/50 rounded border border-slate-700/50">
              <span class="text-slate-300">Line count</span>
              <code class="text-emerald-400 font-mono bg-slate-950 px-2 py-1 rounded">wc -l file.txt</code>
            </li>
            <li class="flex items-center justify-between p-2 bg-slate-900/50 rounded border border-slate-700/50">
              <span class="text-slate-300">Word count</span>
              <code class="text-emerald-400 font-mono bg-slate-950 px-2 py-1 rounded">wc -w file.txt</code>
            </li>
            <li class="flex items-center justify-between p-2 bg-slate-900/50 rounded border border-slate-700/50">
              <span class="text-slate-300">Byte count</span>
              <code class="text-emerald-400 font-mono bg-slate-950 px-2 py-1 rounded">wc -c file.txt</code>
            </li>
          </ul>
        </div>

        <!-- aspell -->
        <div class="bg-slate-800 border border-slate-700 rounded-2xl p-6 shadow-lg">
          <h3 class="font-bold text-white mb-3 text-lg border-b border-slate-700 pb-2 flex items-center gap-2">
            <i data-lucide="spell-check" class="w-5 h-5 text-purple-400"></i>
            Spell Checker (aspell)
          </h3>
          <p class="text-slate-400 text-sm mb-4">
            An interactive spell checker that can scan a file, highlight misspelled words, and suggest replacements.
          </p>
          <div class="p-3 bg-slate-900/50 rounded-lg border border-slate-700/50 mb-3 text-center">
            <code class="text-purple-400 font-mono text-sm">aspell check file.txt</code>
          </div>
          <p class="text-slate-400 text-xs italic">
            This will open an interactive prompt asking you to Replace, Ignore, or Add words to your dictionary.
          </p>
        </div>

      </div>

      <!-- Regular Expressions -->
      <div class="bg-slate-800 border border-slate-700 rounded-2xl p-6 shadow-lg">
        <h3 class="text-xl font-semibold text-white mb-4 flex items-center gap-2">
          <i data-lucide="asterisk" class="w-5 h-5 text-amber-500"></i>
          Regular Expressions (Regex)
        </h3>
        <p class="text-slate-300 leading-relaxed mb-6">
          A regular expression is a sequence of characters that specifies a search pattern. They are extensively used with commands like <code class="text-amber-400 bg-slate-900 px-1.5 py-0.5 rounded text-sm">grep</code>, <code class="text-amber-400 bg-slate-900 px-1.5 py-0.5 rounded text-sm">sed</code>, and <code class="text-amber-400 bg-slate-900 px-1.5 py-0.5 rounded text-sm">awk</code>.
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          
          <div class="space-y-3 text-sm">
            <h4 class="text-white font-medium mb-2">Common Special Characters</h4>
            
            <div class="flex items-center gap-3 p-2 bg-slate-900/50 rounded-lg border border-slate-700/50">
              <code class="text-amber-400 font-bold bg-slate-950 px-2 py-1 rounded">.</code>
              <span class="text-slate-300">Matches any single character.</span>
            </div>
            
            <div class="flex items-center gap-3 p-2 bg-slate-900/50 rounded-lg border border-slate-700/50">
              <code class="text-amber-400 font-bold bg-slate-950 px-2 py-1 rounded">*</code>
              <span class="text-slate-300">Matches zero or more of the preceding character. (<code class="text-emerald-400">.*</code> matches anything).</span>
            </div>
            
            <div class="flex items-center gap-3 p-2 bg-slate-900/50 rounded-lg border border-slate-700/50">
              <code class="text-amber-400 font-bold bg-slate-950 px-2 py-1 rounded">^</code>
              <span class="text-slate-300">Matches the beginning of a line.</span>
            </div>
            
            <div class="flex items-center gap-3 p-2 bg-slate-900/50 rounded-lg border border-slate-700/50">
              <code class="text-amber-400 font-bold bg-slate-950 px-2 py-1 rounded">$</code>
              <span class="text-slate-300">Matches the end of a line.</span>
            </div>
            
            <div class="flex items-center gap-3 p-2 bg-slate-900/50 rounded-lg border border-slate-700/50">
              <code class="text-amber-400 font-bold bg-slate-950 px-2 py-1 rounded">\</code>
              <span class="text-slate-300">Escape character (treats next character literally).</span>
            </div>
          </div>

          <div class="space-y-3">
            <h4 class="text-white font-medium mb-2 text-sm">Using Regex with grep</h4>
            
            <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-700 text-sm">
              <p class="text-slate-400 mb-2">Find lines starting with "111" and ending with "SL":</p>
              <code class="block text-emerald-400 font-mono mb-2">grep '^111.*SL$' leave_log.txt</code>
              <p class="text-xs text-slate-500">The <code class="text-slate-300">.*</code> bridges the gap between the start and end by matching any sequence of characters.</p>
            </div>
            
            <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-700 text-sm">
              <p class="text-slate-400 mb-2">Use Extended Regex (<code class="text-amber-400">-E</code> or <code class="text-amber-400">egrep</code>) for complex braces/brackets:</p>
              <code class="block text-emerald-400 font-mono mb-2">grep -E '1{3}' leave_log.txt</code>
              <p class="text-xs text-slate-500">Finds exactly three "1"s in a row.</p>
            </div>
            
            <div class="bg-slate-900/80 p-4 rounded-xl border border-slate-700 text-sm">
              <p class="text-slate-400 mb-2">Inverse Matching (exclude pattern):</p>
              <code class="block text-emerald-400 font-mono mb-2">grep -v '111' leave_log.txt</code>
              <p class="text-xs text-slate-500">Returns all lines that do <strong class="text-slate-300">not</strong> contain "111".</p>
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
tab_replacement = """      { id: 'editors', title: 'Text Editors', icon: 'edit-3' },
      { id: 'text', title: 'Text Processing', icon: 'file-text' }
    ];"""
content = content.replace("      { id: 'editors', title: 'Text Editors', icon: 'edit-3' }\n    ];", tab_replacement)

with open("/home/neehar/learning_devops/Linux/linux_commands.html", "w") as f:
    f.write(content)

