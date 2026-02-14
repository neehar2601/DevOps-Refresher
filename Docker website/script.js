// Optional: switch between relative links and absolute S3 URLs
// Put your S3 static website base URL (or CloudFront) below.
const ABS_BASE = "http://devops-refresher-ngn2501.s3-website.us-east-2.amazonaws.com/";

function setRelativeLinks() {
  document.querySelectorAll("a[data-rel]").forEach(a => {
    a.setAttribute("href", a.getAttribute("data-rel"));
  });
  const linkStatus = document.getElementById("linkStatus");
  if (linkStatus) {
    linkStatus.textContent = "Link mode: relative";
  }
}

function setAbsoluteLinks() {
  document.querySelectorAll("a[data-rel]").forEach(a => {
    a.setAttribute("href", ABS_BASE + a.getAttribute("data-rel"));
  });
  const linkStatus = document.getElementById("linkStatus");
  if (linkStatus) {
    linkStatus.textContent = "Link mode: absolute (" + ABS_BASE + ")";
  }
}

// Initialize when DOM is loaded
document.addEventListener("DOMContentLoaded", function() {
  const useRelativeBtn = document.getElementById("useRelativeBtn");
  const useAbsoluteBtn = document.getElementById("useAbsoluteBtn");
  
  if (useRelativeBtn) {
    useRelativeBtn.addEventListener("click", setRelativeLinks);
  }
  
  if (useAbsoluteBtn) {
    useAbsoluteBtn.addEventListener("click", setAbsoluteLinks);
  }
  
  // Default to relative links (best for same-prefix S3 hosting).
  setRelativeLinks();
});
