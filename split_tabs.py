import re

with open("/home/neehar/learning_devops/Linux/linux_permissions.html", "r") as f:
    html = f.read()

# Replace <main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 w-full space-y-10">
html = html.replace('w-full space-y-10">', 'w-full">\n    <!-- Tabs Navigation -->\n    <div class="mb-10">\n      <div class="border-b border-slate-800">\n        <nav class="flex space-x-2 overflow-x-auto py-3 no-scrollbar" id="nav-tabs">\n        </nav>\n      </div>\n    </div>\n\n    <!-- Permissions Tab -->\n    <div id="sec-permissions" class="tab-content space-y-10 active">')

# Wrap the first 3 sections into Permissions Tab.
# Find where Identity Management starts.
identity_idx = html.find('<!-- Identity Management -->')

if identity_idx != -1:
    # Insert closing div for sec-permissions and opening div for sec-users
    html = html[:identity_idx] + '    </div>\n\n    <!-- Users & Groups Tab -->\n    <div id="sec-users" class="tab-content hidden space-y-10">\n    ' + html[identity_idx:]

# Find the end of the users section
main_end_idx = html.find('  </main>')
if main_end_idx != -1:
    html = html[:main_end_idx] + '    </div>\n' + html[main_end_idx:]

# Change all <section> to <div> or just keep them as sections inside the tab-content div.
# No need to change section tags inside the tab-content divs.

# Add JS logic for tabs right before the existing lucide.createIcons();
js_logic = """
    const tabs = [
      { id: 'permissions', title: 'File Permissions & Ownership', icon: 'lock' },
      { id: 'users', title: 'Users & Groups', icon: 'users' }
    ];
    let currentTab = window.location.hash ? window.location.hash.replace('#sec-', '') : tabs[0].id;
    if (!tabs.find(t => t.id === currentTab)) currentTab = tabs[0].id;
    
    function renderTabs() {
        const nav = document.getElementById('nav-tabs');
        nav.innerHTML = '';
        tabs.forEach(tab => {
            const isActive = currentTab === tab.id;
            const btn = document.createElement('button');
            btn.className = `tab-btn flex items-center space-x-2 px-4 py-3 text-sm font-semibold rounded-t-lg transition-colors whitespace-nowrap border-b-2 ${isActive ? 'text-amber-400 bg-slate-800/50 border-amber-400' : 'text-slate-400 hover:text-slate-100 hover:bg-slate-800/50 border-transparent'}`;
            btn.onclick = () => { currentTab = tab.id; renderTabs(); renderContent(); };
            btn.innerHTML = `<i data-lucide="${tab.icon}" class="w-4 h-4"></i><span>${tab.title}</span>`;
            nav.appendChild(btn);
        });
        if (typeof lucide !== 'undefined') lucide.createIcons();
    }
    
    function renderContent() {
        document.querySelectorAll('.tab-content').forEach(c => {
            c.classList.add('hidden');
            c.classList.remove('active');
        });
        document.getElementById('sec-' + currentTab).classList.remove('hidden');
        document.getElementById('sec-' + currentTab).classList.add('active');
        window.location.hash = 'sec-' + currentTab;
    }
    renderTabs();
    renderContent();
    
    """

html = html.replace('lucide.createIcons();', js_logic + '\n    lucide.createIcons();', 1)

# Add custom CSS for tabs
style_idx = html.find('</style>')
if style_idx != -1:
    html = html[:style_idx] + '    .tab-content { animation: fadeIn 0.3s ease-in-out; }\n    @keyframes fadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }\n' + html[style_idx:]

with open("/home/neehar/learning_devops/Linux/linux_permissions.html", "w") as f:
    f.write(html)
