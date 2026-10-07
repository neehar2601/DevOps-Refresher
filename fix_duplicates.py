with open("/home/neehar/learning_devops/Linux/linux_permissions.html", "r") as f:
    lines = f.readlines()

out_lines = []
skip = False
div_depth = 0

for i, line in enumerate(lines):
    if "<!-- User Account Creation Deep Dive -->" in line:
        skip = True
        div_depth = 0
        continue
    
    if skip:
        if "<div" in line:
            div_depth += line.count("<div")
        if "</div" in line:
            div_depth -= line.count("</div")
        
        # We also need to stop skipping if we hit the end of the block.
        # The block is entirely contained within a div that starts right after the comment.
        # Wait, the line after the comment is `<div class="mt-6 bg-slate-800 ...`
        if div_depth == 0 and "</div" in line:
            # We reached the end of the block
            skip = False
        continue
    
    out_lines.append(line)

with open("/home/neehar/learning_devops/Linux/linux_permissions_cleaned.html", "w") as f:
    f.writelines(out_lines)

