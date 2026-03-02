import re

with open("business.html", "r", encoding="utf-8") as f:
    content = f.read()

# Extract from <style> to </style>
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if style_match:
    custom_css = style_match.group(1).strip()
    with open("styles.css", "a", encoding="utf-8") as f:
        f.write("\n\n/* === Business Page Styles === */\n")
        f.write(custom_css)
    print("Appended business.html styles to styles.css!")
else:
    print("Could not find <style> block in business.html")
