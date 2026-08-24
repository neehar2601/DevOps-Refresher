# Dynamic Back Navigation for DevOps Learning Hub Pages

Whenever you add a link to navigate from one child page to another (cross-linking) anywhere across the DevOps Learning Hub, you MUST implement the Dynamic Back Button pattern so the user can easily return to the page they just came from.

## The Pattern

### 1. The Link (Source Page)
When adding an `<a>` tag that links to another child page, append the `?ref=<page_id>` query parameter to the URL.
The `<page_id>` should be a short identifier for the current page (e.g., `fs` for filesystem, `pkg` for package management, `net` for networking).

Example:
```html
<a href="linux_commands.html?ref=fs#sec-file-ops">View Commands</a>
```

### 2. The Header (Target Page)
The target page MUST have a header containing a flex container with two back links:
1. The dynamic back link (hidden by default).
2. The standard "Back to Linux Hub" link (with a `home` icon).

Example structure:
```html
<div class="flex items-center space-x-4">
  <a id="back-dynamic" href="linux_filesystem.html" class="hidden items-center gap-2 text-sm text-pink-400 hover:text-pink-300 transition-colors border-r border-slate-700 pr-4">
    <i data-lucide="arrow-left" class="w-4 h-4"></i>
    <span class="hidden sm:inline">Back to Filesystem</span>
  </a>
  <a href="linux_index.html" class="flex items-center gap-2 text-sm text-slate-400 hover:text-emerald-400 transition-colors">
    <i data-lucide="home" class="w-4 h-4"></i>
    <span class="hidden sm:inline">Linux Hub</span>
  </a>
</div>
```

### 3. The Javascript (Target Page)
The target page MUST contain Javascript that parses the `?ref` query parameter and unhides the dynamic back button if a known reference is found.

Example JS:
```javascript
// Dynamic back button logic
const urlParams = new URLSearchParams(window.location.search);
if (urlParams.get('ref') === 'fs') {
    const dynBack = document.getElementById('back-dynamic');
    if (dynBack) {
        // Optionally update the href/text dynamically if you want to support multiple referrers with one element
        dynBack.classList.remove('hidden');
        dynBack.classList.add('flex');
    }
}
```

Whenever requested to cross-link pages or create a new page, ALWAYS apply this pattern.
