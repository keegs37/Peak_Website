import os
import re

with open("convert_to_wp.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the write_style_css definition
# In the original python, it writes a hardcoded string to style.css. 
# We'll replace it to read from styles.css

new_func = """def write_style_css():
    with open('styles.css', 'r', encoding='utf-8') as f:
        main_css = f.read()
        
    wp_header = \"\"\"/*
Theme Name: PEAK Internet
Theme URI: https://peakinternet.com/
Author: PEAK Internet
Author URI: https://peakinternet.com/
Description: Custom WordPress theme for PEAK Internet
Version: 1.0
Text Domain: peak-internet
*/

.main-nav-ul {
    display: flex;
    gap: 32px;
    list-style: none;
    margin: 0;
    padding: 0;
}
.footer-menu-ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 12px;
}
.footer-menu-ul li a {
    color: #9CA3AF;
    transition: color 150ms ease;
    text-decoration: none;
}
.footer-menu-ul li a:hover {
    color: #FFF;
}

/* =========================================
   GENERIC PAGE & EDITOR STYLES
======================================== */
.generic-page-container {
    padding: 60px 0;
    max-width: 800px;
    margin: 0 auto;
}

.generic-page-container h1, 
.template-content h1,
.support-article-content h1 { font-size: 2.5rem; margin-bottom: 24px; color: var(--color-primary-dark); }
.generic-page-container h2,
.template-content h2,
.support-article-content h2 { font-size: 2rem; margin-top: 40px; margin-bottom: 16px; color: var(--color-primary-dark); }
.generic-page-container h3,
.template-content h3,
.support-article-content h3 { font-size: 1.5rem; margin-top: 32px; margin-bottom: 16px; }
.generic-page-container p,
.template-content p,
.support-article-content p { margin-bottom: 24px; font-size: 1.125rem; color: var(--color-text-main); }
.generic-page-container ul, .generic-page-container ol,
.template-content ul, .template-content ol,
.support-article-content ul, .support-article-content ol { margin-bottom: 24px; padding-left: 24px; font-size: 1.125rem; }
.generic-page-container li,
.template-content li,
.support-article-content li { margin-bottom: 8px; }
.generic-page-container img,
.template-content img,
.support-article-content img { max-width: 100%; height: auto; border-radius: var(--radius-md); box-shadow: var(--shadow-sm); margin: 32px 0; }
.generic-page-container figure,
.template-content figure,
.support-article-content figure { margin: 32px 0; }
.generic-page-container figcaption,
.template-content figcaption,
.support-article-content figcaption { text-align: center; color: var(--color-text-mute); font-size: 0.875rem; margin-top: 8px; }

/* Block Alignments */
.aligncenter { display: block; margin: 0 auto; }
.alignwide { max-width: 1000px; margin-left: auto; margin-right: auto; }
.alignfull { margin-left: calc(-100vw / 2 + 100% / 2); margin-right: calc(-100vw / 2 + 100% / 2); max-width: 100vw; width: 100vw; }

.custom-logo {
    max-height: 40px;
    width: auto;
}

/* Accessibility / Screen Readers */
.screen-reader-text {
    border: 0;
    clip: rect(1px, 1px, 1px, 1px);
    clip-path: inset(50%);
    height: 1px;
    margin: -1px;
    overflow: hidden;
    padding: 0;
    position: absolute;
    width: 1px;
    word-wrap: normal !important;
}

.screen-reader-text:focus {
    background-color: #f1f1f1;
    border-radius: 3px;
    box-shadow: 0 0 2px 2px rgba(0, 0, 0, 0.6);
    clip: auto !important;
    clip-path: none;
    color: #21759b;
    display: block;
    font-size: 14px;
    font-size: 0.875rem;
    font-weight: bold;
    height: auto;
    left: 5px;
    line-height: normal;
    padding: 15px 23px 14px;
    text-decoration: none;
    top: 5px;
    width: auto;
    z-index: 100000;
}

/* =========================================
   SPECIALIZED TEMPLATE STYLES
======================================== */

/* Styles for Service Sidebar */
.template-service-sidebar {
    display: flex;
    flex-wrap: wrap;
    gap: 40px;
    padding: 60px 0;
}

.template-content {
    flex: 1;
    min-width: 0; /* Prevents flex blowout */
}

.template-sidebar {
    width: 100%;
    max-width: 350px;
    flex-shrink: 0;
}

.service-widget-area {
    background-color: var(--color-bg-mute);
    padding: 32px;
    border-radius: var(--radius-md);
    margin-bottom: 24px;
}

.service-widget-area h2.widgettitle {
    font-size: 1.25rem;
    margin-bottom: 16px;
    border-bottom: 2px solid var(--color-primary);
    padding-bottom: 8px;
    display: inline-block;
}

.service-widget-area ul {
    list-style: none;
    padding: 0;
}

.service-widget-area li {
    margin-bottom: 12px;
}

.service-widget-area a {
    color: var(--color-primary);
    font-weight: 500;
}

.service-widget-area a:hover {
    color: var(--color-primary-dark);
}

/* Styles for Support Article */
.support-article-container {
    max-width: 700px; /* Narrower for optimal reading */
    margin: 0 auto;
    padding: 80px 0;
}

.support-article-header {
    text-align: center;
    margin-bottom: 48px;
}

.support-article-header .badge {
    background-color: var(--color-primary-light);
    color: #FFF;
    padding: 4px 12px;
    border-radius: var(--radius-pill);
    font-size: 0.875rem;
    font-weight: 600;
    margin-bottom: 16px;
    display: inline-block;
}

@media (max-width: 768px) {
    .template-service-sidebar {
        flex-direction: column;
    }
    .template-sidebar {
        max-width: 100%;
    }
}
\"\"\"
    
    with open(os.path.join(THEME_DIR, 'style.css'), 'w', encoding='utf-8') as f:
        f.write(wp_header + "\\n/* === MAIN THEME STYLES IMPORTED DIRECTLY === */\\n" + main_css)
"""

# replace the old function completely by regex or split
start_idx = content.find("def write_style_css():")
end_idx = content.find("def write_functions_php():")

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + new_func + "\n" + content[end_idx:]
    with open("convert_to_wp.py", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Replaced write_style_css")
else:
    print("Could not find function bounds")
