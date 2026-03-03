import glob
import re

html_files = glob.glob("*.html")
html_files = [f for f in html_files if f not in ['current_peak.html', 'temp_scraped.html', 'temp_scraped_2.html']]

count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Remove header area
    content = re.sub(r'<!-- Utility Bar -->.*?</header>', '', content, flags=re.DOTALL)
    
    # Remove footer area
    content = re.sub(r'<!-- Footer -->.*?</footer>', '', content, flags=re.DOTALL)
    
    # Remove <main> tags themselves if they are empty wrappers?
    # Actually, keeping <main> is fine, or replacing <main> with nothing.
    # The user just said "remove the header and footer html"
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned {filepath}")
        count += 1

print(f"Total cleaned: {count}")
