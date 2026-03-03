import glob
import re

html_files = glob.glob("*.html")
html_files = [f for f in html_files if f not in ['current_peak.html', 'temp_scraped.html', 'temp_scraped_2.html']]

count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Remove Utility Bar and Main Navigation
    content = re.sub(r'<!-- Utility Bar -->.*?</div>\s*<!-- Main Navigation -->.*?</header>', '', content, flags=re.DOTALL)
    
    # Alternatively, if they don't have Utility bar but have header
    content = re.sub(r'<!-- Main Navigation -->.*?</header>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- Utility Bar -->.*?</div>', '', content, flags=re.DOTALL) # in case it's alone? The first regex handles contiguous. Wait, but the <div class="utility-bar"> is closed by a </div>. Finding exactly </div> is hard with regex.
    
    # Better to use string bounds or known tags based on `<header>` and `<footer>` and `<div class="utility-bar">`
    content = re.sub(r'<div class="utility-bar">.*?</div>\s*</header>', '', content, flags=re.DOTALL) # This regex is safe? No, let's use BeautifulSoup or a tighter regex.
    
    pass
