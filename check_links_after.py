import glob
import re

html_files = glob.glob("*.html")
html_files = [f for f in html_files if f not in ['current_peak.html']]

for filepath in html_files[:1]:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"--- {filepath} ---")
    
    # Just print the nav area to see the links
    match = re.search(r'<nav class="main-nav">(.*?)</nav>', content, re.DOTALL)
    if match:
        print(match.group(1))
