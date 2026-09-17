with open("Networking-Tools-Guide.html", "r") as f:
    lines = f.readlines()

# Extract the shell
html_shell = "".join(lines[:317]) # 0 to 316 (which is line 317)

# Replace titles and text
html_shell = html_shell.replace("<title>Networking Tools Guide - Networking Hub</title>", "<title>Network Security Guide - Networking Hub</title>")
html_shell = html_shell.replace("Networking Tools <span class=\"text-blue-400 font-light hidden sm:inline\">Guide</span>", "Network Security <span class=\"text-blue-400 font-light hidden sm:inline\">Guide</span>")
html_shell = html_shell.replace("Comprehensive Networking Command Reference", "Comprehensive Security Architecture Reference")
html_shell = html_shell.replace("The complete interactive guide covering essential command-line tools for Windows and Linux. Learn how to troubleshoot connectivity, resolve DNS, analyze routing, and capture packets.", "The complete interactive guide covering essential network security concepts, from firewalls and VPN architectures to modern DevSecOps, Cloud Security, and Zero Trust paradigms.")

with open("Network_Security_Guide.html", "r") as f:
    js_content = f.read()

# Make sure js_content doesn't have duplicate <script> if we already have it.
# Actually, the original Network_Security_Guide.html starts directly with `const contentData = {` right now because I overwrote it.
if js_content.startswith("const contentData = {"):
    with open("Network_Security_Guide.html", "w") as f:
        f.write(html_shell + "\n" + js_content)
    print("Fixed!")
else:
    print("Does not start with const contentData")
