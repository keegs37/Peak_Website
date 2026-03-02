import os

with open('styles.css', 'r', encoding='utf-8') as f:
    main_css = f.read()

# Make sure WP Header is at the top of the combined CSS
wp_header = """/*
Theme Name: PEAK Internet
Theme URI: https://peakinternet.com/
Author: PEAK Internet
Author URI: https://peakinternet.com/
Description: Custom WordPress theme for PEAK Internet
Version: 1.0
Text Domain: peak-internet
*/

"""

combined_css = wp_header + main_css

# We will modify convert_to_wp.py to just use this
