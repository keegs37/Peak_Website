import re

with open("convert_to_wp.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the broken PHP generator logic with a standard absolute path relative to the root
old_regex = r'main_content = re.sub\(r\'href="(?:\^"|\[\^"\])\+\\\\.html\(#\?\.\*\?\)"\', "href=\\\\"<\?php echo esc_url\( home_url\( \'/\\\\1\\\\2\' \) \); \?>\\\\"", main_content\)'
# The actual string from the file is:
# main_content = re.sub(r'href="([^"]+)\.html(#?.*?)"', "href=\"<?php echo esc_url( home_url( '/\\1\\2' ) ); ?>\"", main_content)

content = content.replace(
    'main_content = re.sub(r\'href="([^"]+)\.html(#?.*?)"\', "href=\\"<?php echo esc_url( home_url( \'/\\\\1\\\\2\' ) ); ?>\\"", main_content)',
    'main_content = re.sub(r\'href="([^"]+)\.html(#?.*?)"\', "href=\\"/\\\\1/\\\\2\\"", main_content)'
)

# Also fix the img/assets SRC replacements! WP post content CANNOT have PHP in it either!
content = content.replace(
    'main_content = main_content.replace(\'href="assets/\', \'href="<?php echo get_template_directory_uri(); ?>/assets/\')',
    'main_content = main_content.replace(\'href="assets/\', \'href="/wp-content/themes/peak-theme/assets/\')'
)
content = content.replace(
    'main_content = main_content.replace(\'src="assets/\', \'src="<?php echo get_template_directory_uri(); ?>/assets/\')',
    'main_content = main_content.replace(\'src="assets/\', \'src="/wp-content/themes/peak-theme/assets/\')'
)

with open("convert_to_wp.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated link replacement logic!")
