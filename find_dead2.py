import glob
import re
import os

html_files = glob.glob("*.html")
html_files += ['convert_to_wp.py']
existing_pages = set([os.path.basename(f) for f in glob.glob("*.html")])

href_pattern = re.compile(r'href=["\']([^"\']+)["\']')

for filepath in html_files:
    # Skip temporary test sites or files not in our immediate control if needed
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            matches = href_pattern.findall(line)
            for href in matches:
                # ignore absolute urls and hashes and basic asset files
                if href.startswith('http') or href.startswith('//') or href.startswith('mailto:') or href.startswith('tel:') or href.startswith('#') or href.endswith('.css') or href.endswith('.js') or href.endswith('.png') or href.endswith('.jpg') or href.endswith('.svg') or href.startswith('assets/'):
                    continue
                
                # Check if it contains '#', remove the anchor part
                clean_href = href.split('#')[0]
                
                if clean_href == '':
                    continue
                
                if clean_href not in existing_pages and clean_href != 'convert_to_wp.py':
                    print(f"Missing Link Target: {filepath}:{i} -> href='{href}'")

