import glob

# Check business.html content around the colocation tile and the links
with open("business.html", "r", encoding="utf-8") as f:
    content = f.read()

import re
matches = re.findall(r'<div class="biz-card.*?</p>.*?</div', content, re.DOTALL)
for i, match in enumerate(matches):
    print(f"--- Card {i} ---")
    print(match[:200] + "... " + match[-100:])
