import re

main_content = '<a href="biz-advanced-internet.html">Learn More</a>'
main_content = re.sub(r'href="([^"]+)\.html(#?.*?)"', "href=\"<?php echo esc_url( home_url( '/\\1\\2' ) ); ?>\"", main_content)

print(main_content)
