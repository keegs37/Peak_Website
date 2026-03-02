import glob
import re

html_files = glob.glob("*.html")
html_files = [f for f in html_files if f not in ['current_peak.html']]

count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace href="assets/" with href="/wp-content/themes/peak-theme/assets/"
    # and src="assets/" with src="/wp-content/themes/peak-theme/assets/"
    
    new_content = content.replace('href="assets/', 'href="/wp-content/themes/peak-theme/assets/')
    new_content = new_content.replace('src="assets/', 'src="/wp-content/themes/peak-theme/assets/')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated assets in {filepath}")
        count += 1

print(f"Updated assets in {count} files.")
