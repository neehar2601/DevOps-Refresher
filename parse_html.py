with open("/home/neehar/learning_devops/Linux/linux_permissions.html", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "<!-- User Account Creation Deep Dive -->" in line:
        print(f"Deep Dive starts at {i}")
    if "<!-- Modifying Permissions & Ownership -->" in line:
        print(f"Modifying Permissions starts at {i}")
    if "<!-- Users & Groups Tab -->" in line:
        print(f"Users & Groups Tab starts at {i}")
