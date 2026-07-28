/* =============================================================
   Shared site-wide JavaScript
   Used by: index.html, git/git_index.html, docker/*.html
   ============================================================= */

// ── S3 link switcher ─────────────────────────────────────────
const ABS_BASE = "http://devops-refresher-ngn2501.s3-website.us-east-2.amazonaws.com/";

function setRelativeLinks() {
  document.querySelectorAll("a[data-rel]").forEach(a => a.setAttribute("href", a.getAttribute("data-rel")));
  const el = document.getElementById("linkStatus");
  if (el) el.textContent = "Link mode: relative";
}

function setAbsoluteLinks() {
  document.querySelectorAll("a[data-rel]").forEach(a => a.setAttribute("href", ABS_BASE + a.getAttribute("data-rel")));
  const el = document.getElementById("linkStatus");
  if (el) el.textContent = "Link mode: absolute (" + ABS_BASE + ")";
}

document.addEventListener("DOMContentLoaded", function () {
  const relBtn = document.getElementById("useRelativeBtn");
  const absBtn = document.getElementById("useAbsoluteBtn");
  if (relBtn) relBtn.addEventListener("click", setRelativeLinks);
  if (absBtn) absBtn.addEventListener("click", setAbsoluteLinks);
  setRelativeLinks();

  // Initialise Lucide icons on any page that loads the Lucide CDN
  if (typeof lucide !== "undefined") lucide.createIcons();
});

// ── Tab navigation (shared across all pages) ─────────────────
function showTab(tabName) {
  document.querySelectorAll(".tab-content").forEach(c => c.classList.remove("active"));
  document.querySelectorAll(".tab-btn, .tab").forEach(b => b.classList.remove("active"));

  const selected = document.getElementById(tabName);
  if (selected) selected.classList.add("active");

  if (event && event.target) event.target.classList.add("active");
  window.scrollTo({ top: 0, behavior: "smooth" });
}

// ── Toast helpers ─────────────────────────────────────────────
let _toastTimer = null;

function toast(html) {
  const t = document.getElementById("toast");
  if (!t) return;
  // Support both custom-CSS pages (display:block) and Tailwind pages (hidden class)
  t.innerHTML = html;
  t.style.display = "block";
  t.classList.remove("hidden");
  clearTimeout(_toastTimer);
  _toastTimer = setTimeout(() => {
    t.style.display = "none";
    t.classList.add("hidden");
  }, 3400);
}

function showToast(msg) { toast(msg); }

function comingSoon(name, desc) {
  toast("<strong>" + name + "</strong> is coming soon. " + (desc || ""));
}
