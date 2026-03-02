import glob
import re

html_files = glob.glob("*.html")
html_files = [f for f in html_files if f not in ['current_peak.html']]

count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace href="something.html" or href="something.html#anchor"
    # with href="/something/" or href="/something/#anchor"
    # We need to handle index.html specially -> href="/"
    
    def replacer(match):
        filename = match.group(1)
        anchor = match.group(2)
        if filename == 'index':
            return f'href="/{anchor}"'
        else:
            return f'href="/{filename}/{anchor}"'
            
    # Also fix the header/footer PHP generated links if any exist in the HTML files? No, the HTML files have raw HTML.
    
    new_content = re.sub(r'href="([^"]+)\.html(#?.*?)"', replacer, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated links in {filepath}")
        count += 1

print(f"Updated {count} files.")
