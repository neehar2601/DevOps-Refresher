import sys

html_content = """
      <!-- File Viewing Utilities -->
      <div class="bg-slate-800 border border-slate-700 rounded-2xl p-6 shadow-lg">
        <h3 class="text-xl font-semibold text-white mb-4 flex items-center gap-2">
          <i data-lucide="eye" class="w-5 h-5 text-indigo-400"></i>
          File Viewing Utilities
        </h3>
        <p class="text-slate-300 leading-relaxed mb-6">
          Tools used to quickly read or stream the contents of files directly to the standard output.
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <!-- cat -->
          <div class="bg-slate-900/50 p-4 rounded-xl border border-slate-700/50 flex flex-col">
            <h4 class="text-md font-bold text-indigo-400 font-mono mb-1">cat</h4>
            <p class="text-slate-300 text-sm mb-2 flex-grow">Concatenates files and prints them to the standard output. Commonly used to quickly view small files.</p>
            <code class="text-xs text-slate-400 bg-slate-950 p-2 rounded">cat file.txt</code>
          </div>
          
          <!-- tac -->
          <div class="bg-slate-900/50 p-4 rounded-xl border border-slate-700/50 flex flex-col">
            <h4 class="text-md font-bold text-indigo-400 font-mono mb-1">tac</h4>
            <p class="text-slate-300 text-sm mb-2 flex-grow">The reverse of <code class="text-indigo-300">cat</code>. Prints lines of a file in reverse order (last line first).</p>
            <code class="text-xs text-slate-400 bg-slate-950 p-2 rounded">tac file.txt</code>
          </div>

          <!-- head -->
          <div class="bg-slate-900/50 p-4 rounded-xl border border-slate-700/50 flex flex-col">
            <h4 class="text-md font-bold text-indigo-400 font-mono mb-1">head</h4>
            <p class="text-slate-300 text-sm mb-2 flex-grow">Outputs the first part of files (default is the first 10 lines). Use <code class="text-indigo-300">-n</code> to specify lines.</p>
            <code class="text-xs text-slate-400 bg-slate-950 p-2 rounded">head -n 20 file.txt</code>
          </div>

          <!-- tail -->
          <div class="bg-slate-900/50 p-4 rounded-xl border border-slate-700/50 flex flex-col">
            <h4 class="text-md font-bold text-indigo-400 font-mono mb-1">tail</h4>
            <p class="text-slate-300 text-sm mb-2 flex-grow">Outputs the last part of files. The <code class="text-indigo-300">-f</code> flag is incredibly useful for following live log files.</p>
            <code class="text-xs text-slate-400 bg-slate-950 p-2 rounded">tail -f /var/log/syslog</code>
          </div>
        </div>
      </div>

      <!-- Text Manipulation Utilities -->
      <div class="bg-slate-800 border border-slate-700 rounded-2xl p-6 shadow-lg">
        <h3 class="text-xl font-semibold text-white mb-4 flex items-center gap-2">
          <i data-lucide="scissors" class="w-5 h-5 text-amber-500"></i>
          Text Filtering & Manipulation
        </h3>
        <p class="text-slate-300 leading-relaxed mb-6">
          Commands for extracting, sorting, and transforming text data, commonly used together via pipelines (<code class="text-amber-400">|</code>).
        </p>

        <div class="space-y-4">
          <!-- sort & uniq -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-slate-900/50 p-4 rounded-xl border border-slate-700/50">
              <h4 class="text-md font-bold text-amber-400 font-mono mb-1">sort</h4>
              <p class="text-slate-300 text-sm mb-2">Sorts lines of text files alphanumerically. Use <code class="text-amber-300">-r</code> for reverse and <code class="text-amber-300">-n</code> for numeric sort.</p>
              <code class="text-xs text-slate-400 bg-slate-950 p-2 rounded block">sort names.txt</code>
            </div>
            
            <div class="bg-slate-900/50 p-4 rounded-xl border border-slate-700/50">
              <h4 class="text-md font-bold text-amber-400 font-mono mb-1">uniq</h4>
              <p class="text-slate-300 text-sm mb-2">Deletes or reports duplicate <em>adjacent</em> lines. Almost always used immediately after <code class="text-amber-300">sort</code>.</p>
              <code class="text-xs text-slate-400 bg-slate-950 p-2 rounded block">sort names.txt | uniq</code>
            </div>
          </div>

          <!-- cut, tr, unexpand -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="bg-slate-900/50 p-4 rounded-xl border border-slate-700/50">
              <h4 class="text-md font-bold text-amber-400 font-mono mb-1">cut</h4>
              <p class="text-slate-300 text-sm mb-2">Removes sections from each line. Use <code class="text-amber-300">-d</code> for delimiter and <code class="text-amber-300">-f</code> for field.</p>
              <code class="text-xs text-slate-400 bg-slate-950 p-2 rounded block">cut -d',' -f1 data.csv</code>
            </div>

            <div class="bg-slate-900/50 p-4 rounded-xl border border-slate-700/50">
              <h4 class="text-md font-bold text-amber-400 font-mono mb-1">tr</h4>
              <p class="text-slate-300 text-sm mb-2">Translates or deletes characters from standard input.</p>
              <code class="text-xs text-slate-400 bg-slate-950 p-2 rounded block">cat file | tr 'a-z' 'A-Z'</code>
            </div>

            <div class="bg-slate-900/50 p-4 rounded-xl border border-slate-700/50">
              <h4 class="text-md font-bold text-amber-400 font-mono mb-1">unexpand</h4>
              <p class="text-slate-300 text-sm mb-2">Converts groups of white spaces (spaces) into tabs.</p>
              <code class="text-xs text-slate-400 bg-slate-950 p-2 rounded block">unexpand -a file.txt</code>
            </div>
          </div>
        </div>
      </div>
"""

with open("/home/neehar/learning_devops/Linux/linux_commands.html", "r") as f:
    content = f.read()

# Insert before <!-- Regular Expressions -->
content = content.replace("      <!-- Regular Expressions -->", html_content + "\n      <!-- Regular Expressions -->")

with open("/home/neehar/learning_devops/Linux/linux_commands.html", "w") as f:
    f.write(content)

