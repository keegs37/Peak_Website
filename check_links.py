import re

with open("convert_to_wp.py", "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for how it converts html links
matches = re.finditer(r'replace\s*\(.*\.html', content)
for m in matches:
    print(content[m.start()-50:m.end()+50])
