import glob

html_files = glob.glob("*.html")
html_files = [f for f in html_files if f not in ['current_peak.html']]

count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('href="styles.css"', 'href="/wp-content/themes/peak-theme/styles.css"')
    new_content = new_content.replace('src="main.js"', 'src="/wp-content/themes/peak-theme/main.js"')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated CSS/JS references in {count} files.")
