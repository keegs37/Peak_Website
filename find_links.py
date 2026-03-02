import os
import glob
import re

html_files = glob.glob("*.html")
existing_pages = set([os.path.basename(f) for f in html_files])
print(f"Total existing pages: {len(existing_pages)}")

links = set()
href_pattern = re.compile(r'href="([^"]+)"', re.IGNORECASE)

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        matches = href_pattern.findall(content)
        for href in matches:
            # Ignore absolute URLs, mailtos, tel, and anchor links on the same page
            if (not href.startswith('http') and 
                not href.startswith('mailto:') and 
                not href.startswith('tel:') and 
                not href.startswith('#')):
                # Remove query params or anchors from local file paths
                path = href.split('?')[0].split('#')[0]
                if path:
                    links.add(path)

print(f"Total unique relative links found: {len(links)}")

missing = set()
for link in links:
    # If the link doesn't match an existing file
    if link not in existing_pages and not link.endswith('/'):
        # Some links might be to a directory without trailing slash, but here we expect .html
        missing.add(link)

print("\nMissing pages:")
for m in sorted(missing):
    print(m)
