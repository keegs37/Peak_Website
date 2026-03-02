import glob
import re

html_files = glob.glob("*.html")
html_files += ['convert_to_wp.py']

href_pattern = re.compile(r'href="([^"]+)"')

for filepath in html_files:
    # Skip temporary test sites or files not in our immediate control if needed
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            matches = href_pattern.findall(line)
            for href in matches:
                if href == '#' or href == '' or '.html#' in href:
                    pass # We will check this
                
                # Let's print all hrefs that are exactly '#' or empty, or point to files that don't exist
                if href == '#' or href == '':
                    print(f"{filepath}:{i+1} -> {href} (Context: {line.strip()})")

