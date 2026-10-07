import re

with open("/home/neehar/learning_devops/Linux/linux_permissions.html", "r") as f:
    html = f.read()

# The block to remove is from "      <!-- User Account Creation Deep Dive -->" to the end of its enclosing div.
# We can use regex to find and remove all instances.
pattern = re.compile(r'      <!-- User Account Creation Deep Dive -->.*?</div>\s+</div>\s+</div>', re.DOTALL)

html_cleaned = pattern.sub('', html)

# Let's save it to see if it cleanly removes all 4 instances.
with open("/home/neehar/learning_devops/Linux/linux_permissions.html", "w") as f:
    f.write(html_cleaned)
