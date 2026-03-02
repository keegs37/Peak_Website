import os
import re

# Read a base page to use as template, e.g., about.html
template_file = "about.html"
with open(template_file, "r", encoding="utf-8") as f:
    content = f.read()

# Extract header and footer
header_match = re.search(r'(.*?<main>)', content, re.DOTALL | re.IGNORECASE)
footer_match = re.search(r'(</main>.*)', content, re.DOTALL | re.IGNORECASE)

if header_match and footer_match:
    header = header_match.group(1)
    footer = footer_match.group(1)
    
    # Modify header title specifically for this page
    header = re.sub(r'<title>.*?</title>', '<title>PEAK Internet to install fiber optic lines in Lebanon | PEAK News</title>', header)
    
    main_content = """
            <!-- Page Header -->
            <section class="page-header" style="background-color: var(--color-primary-dark); color: white; padding: 80px 0; text-align: center;">
                <div class="container">
                    <div style="display: inline-block; background: var(--color-primary); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.875rem; font-weight: 600; text-transform: uppercase; margin-bottom: 16px;">Expansion</div>
                    <h1 style="color: white; font-size: 3rem; margin-bottom: 16px;">PEAK Internet to install fiber optic lines in Lebanon</h1>
                    <p style="font-size: 1.125rem; opacity: 0.9;"><i class="ph ph-calendar-blank"></i> December 13, 2022</p>
                </div>
            </section>

            <!-- Content Area -->
            <section style="padding: 80px 0; background-color: var(--color-bg-surface);">
                <div class="container" style="max-width: 800px; margin: 0 auto; line-height: 1.8; font-size: 1.125rem; color: var(--color-text-main);">
                    <img src="https://www.peakinternet.com/devpk/wp-content/uploads/2020/08/header-bg.png" alt="Lebanon Fiber Expansion" style="width: 100%; border-radius: var(--radius-lg); margin-bottom: 40px; box-shadow: var(--shadow-sm);">
                    
                    <p style="margin-bottom: 24px;">Linn County Commissioners approved a tax-exempt bond program that will help PEAK Internet run more than 101 miles of high-speed fiber optic lines in the city of Lebanon, greatly increasing Internet speed opportunities for homes and businesses alike.</p>
                    
                    <p style="margin-bottom: 24px;">The $10 million bond will be completely repaid by PEAK Internet, but the county's sponsorship provides a lower interest rate for the locally-owned cooperative. No county tax dollars are at risk.</p>
                    
                    <h3 style="color: var(--color-primary-dark); font-size: 1.75rem; margin: 40px 0 20px;">Enterprise-level connectivity for every home</h3>
                    
                    <p style="margin-bottom: 24px;">This expansion marks a significant milestone for the Mid-Willamette Valley. Lebanon will be the first in the region to get enterprise-level fiber-optic internet available directly to every home within the city limits. This fiber-to-the-home (FTTH) initiative means symmetrical upload and download speeds capable of gigabit performance and beyond.</p>
                    
                    <p style="margin-bottom: 24px;">"This is a game-changer for economic development, remote work, and education in our community," said a PEAK Internet representative. "We're not just upgrading an old network; we are building an entirely new, state-of-the-art infrastructure from the ground up."</p>
                    
                    <div style="background-color: var(--color-bg-mute); padding: 32px; border-left: 4px solid var(--color-primary); border-radius: 0 var(--radius-sm) var(--radius-sm) 0; margin: 40px 0;">
                        <h4 style="color: var(--color-primary-dark); margin-bottom: 12px; font-size: 1.25rem;">Why Fiber?</h4>
                        <ul style="list-style: none; padding: 0;">
                            <li style="margin-bottom: 8px; display: flex; align-items: start; gap: 12px;"><i class="ph-fill ph-check-circle" style="color: var(--color-primary); margin-top: 4px;"></i> Future-proof bandwidth capable of supporting dozens of devices simultaneously.</li>
                            <li style="margin-bottom: 8px; display: flex; align-items: start; gap: 12px;"><i class="ph-fill ph-check-circle" style="color: var(--color-primary); margin-top: 4px;"></i> Symmetrical speeds (upload as fast as download), crucial for cloud backups and video conferencing.</li>
                            <li style="display: flex; align-items: start; gap: 12px;"><i class="ph-fill ph-check-circle" style="color: var(--color-primary); margin-top: 4px;"></i> Increased home values associated with gigabit-ready communities.</li>
                        </ul>
                    </div>
                    
                    <p style="margin-bottom: 24px;">Construction is expected to begin in early 2023, with the first neighborhoods lighting up later in the year. Residents can check their availability and pre-register for service at PEAK's SmartHub portal.</p>
                    
                    <div style="margin-top: 60px; padding-top: 40px; border-top: 1px solid var(--color-border); display: flex; justify-content: space-between; align-items: center;">
                        <a href="news.html" class="btn btn-outline dark"><i class="ph ph-arrow-left" style="margin-right: 8px;"></i> Back to News</a>
                        <div style="display: flex; gap: 16px;">
                            <a href="#" style="color: var(--color-text-mute); font-size: 1.5rem;"><i class="ph-fill ph-facebook-logo"></i></a>
                            <a href="#" style="color: var(--color-text-mute); font-size: 1.5rem;"><i class="ph-fill ph-twitter-logo"></i></a>
                            <a href="#" style="color: var(--color-text-mute); font-size: 1.5rem;"><i class="ph-fill ph-linkedin-logo"></i></a>
                        </div>
                    </div>
                </div>
            </section>
"""
    
    full_html = header + main_content + footer
    
    with open("news-lebanon-fiber.html", "w", encoding="utf-8") as out:
        out.write(full_html)
    print("Successfully created news-lebanon-fiber.html")
else:
    print("Could not match header/footer in the template.")
