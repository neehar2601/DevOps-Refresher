import re

with open("/home/neehar/learning_devops/Linux/linux_permissions.html", "r") as f:
    content = f.read()

# The block to remove starts with "      <!-- User Account Creation Deep Dive -->"
# and ends with "      </div>" (the outer div of that block).
# Let's write a regex that matches the block.
# Actually, the block ends exactly before "    </section>" if it's the last thing in the section,
# or before "    <!-- Modifying Permissions & Ownership -->" etc.

pattern = re.compile(r'      <!-- User Account Creation Deep Dive -->.*?      </div>\n', re.DOTALL)
# Wait, there are multiple </div> in the block.
