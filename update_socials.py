import os
import glob

old_social_links = """                    <div class="social-links">
                        <a href="#"><i class="ph-fill ph-facebook-logo"></i></a>
                        <a href="#"><i class="ph-fill ph-twitter-logo"></i></a>
                        <a href="#"><i class="ph-fill ph-instagram-logo"></i></a>
                    </div>"""

new_social_links = """                    <div class="social-links">
                        <a href="https://www.facebook.com/peakinternet/" target="_blank"><i class="ph-fill ph-facebook-logo"></i></a>
                        <a href="https://twitter.com/peakinternet/" target="_blank"><i class="ph-fill ph-twitter-logo"></i></a>
                        <a href="https://www.youtube.com/user/PeakInternet" target="_blank"><i class="ph-fill ph-youtube-logo"></i></a>
                    </div>"""

for filepath in glob.glob("*.html"):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_social_links in content:
        content = content.replace(old_social_links, new_social_links)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Replaced in {filepath}")
