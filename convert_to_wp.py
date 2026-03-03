import os
import re
import shutil
import base64

THEME_DIR = 'peak-theme'

def setup_theme_dir():
    if not os.path.exists(THEME_DIR):
        os.makedirs(THEME_DIR)
    
    # Copy assets, css, js
    if os.path.exists('assets'):
        if os.path.exists(os.path.join(THEME_DIR, 'assets')):
            shutil.rmtree(os.path.join(THEME_DIR, 'assets'))
        shutil.copytree('assets', os.path.join(THEME_DIR, 'assets'))
    if os.path.exists('styles.css'):
        shutil.copy('styles.css', os.path.join(THEME_DIR, 'styles.css'))
    if os.path.exists('main.js'):
        shutil.copy('main.js', os.path.join(THEME_DIR, 'main.js'))

def write_style_css():
    with open('styles.css', 'r', encoding='utf-8') as f:
        main_css = f.read()
        
    wp_header = """/*
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
"""
    
    with open(os.path.join(THEME_DIR, 'style.css'), 'w', encoding='utf-8') as f:
        f.write(wp_header + "\n/* === MAIN THEME STYLES IMPORTED DIRECTLY === */\n" + main_css)

def write_functions_php():
    content = """<?php
function peak_theme_enqueue_styles() {
    // Enqueue the main unified style.css
    wp_enqueue_style( 'peak-main-style', get_stylesheet_uri(), array(), '1.1' );
    wp_enqueue_style( 'peak-google-fonts', 'https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Inter:wght@400;500;600&display=swap', false );
    
    // Phosphor Icons
    wp_enqueue_script( 'phosphor-icons', 'https://unpkg.com/@phosphor-icons/web', array(), null, false );
    
    // Main JS
    wp_enqueue_script( 'peak-main-js', get_template_directory_uri() . '/main.js', array(), '1.0', true );
}
add_action( 'wp_enqueue_scripts', 'peak_theme_enqueue_styles' );

function peak_theme_setup() {
    // Translation Readiness
    load_theme_textdomain( 'peak-internet', get_template_directory() . '/languages' );

    add_theme_support( 'title-tag' );
    add_theme_support( 'post-thumbnails' );
    
    // HTML5 Support for a11y
    add_theme_support( 'html5', array(
        'search-form',
        'comment-form',
        'comment-list',
        'gallery',
        'caption',
        'style',
        'script'
    ) );
    
    // Editor Styles
    add_theme_support( 'editor-styles' );
    add_editor_style( 'styles.css' );

    // Block Editor Supports
    add_theme_support( 'wp-block-styles' );
    add_theme_support( 'align-wide' );
    add_theme_support( 'responsive-embeds' );

    // Custom Logo
    add_theme_support( 'custom-logo', array(
        'height'      => 80,
        'width'       => 250,
        'flex-width'  => true,
        'flex-height' => true,
    ) );

    register_nav_menus( array(
        'primary' => __( 'Primary Menu', 'peak-internet' ),
        'footer_services' => __( 'Footer Services', 'peak-internet' ),
        'footer_support' => __( 'Footer Support', 'peak-internet' ),
        'footer_company' => __( 'Footer Company', 'peak-internet' ),
    ) );
}
add_action( 'after_setup_theme', 'peak_theme_setup' );

// Footer Menu Fallbacks
function peak_footer_services_fallback() {
    echo '<ul class="footer-menu-ul">';
    echo '<li><a href="' . esc_url( home_url( '/internet-plans#fiber' ) ) . '">PEAK Fiber</a></li>';
    echo '<li><a href="' . esc_url( home_url( '/internet-plans#wireless' ) ) . '">Fixed Wireless</a></li>';
    echo '<li><a href="' . esc_url( home_url( '/advanced-services#wifi' ) ) . '">Total Home Wi-Fi</a></li>';
    echo '<li><a href="' . esc_url( home_url( '/business' ) ) . '">Business Internet</a></li>';
    echo '</ul>';
}

function peak_footer_support_fallback() {
    echo '<ul class="footer-menu-ul">';
    echo '<li><a href="' . esc_url( home_url( '/support' ) ) . '">Contact Us</a></li>';
    echo '<li><a href="https://peak.smarthub.coop/Login.html" target="_blank">Pay My Bill</a></li>';
    echo '<li><a href="http://speedtest.peakinternet.com:7076/" target="_blank">Check Speed</a></li>';
    echo '<li><a href="' . esc_url( home_url( '/financial-assistance' ) ) . '">Financial Assistance</a></li>';
    echo '<li><a href="' . esc_url( home_url( '/support' ) ) . '">Tech Support</a></li>';
    echo '</ul>';
}

function peak_footer_company_fallback() {
    echo '<ul class="footer-menu-ul">';
    echo '<li><a href="' . esc_url( home_url( '/about' ) ) . '">Our Mission</a></li>';
    echo '<li><a href="' . esc_url( home_url( '/careers' ) ) . '">Careers</a></li>';
    echo '<li><a href="' . esc_url( home_url( '/news' ) ) . '">News</a></li>';
    echo '<li><a href="' . esc_url( home_url( '/disclosures' ) ) . '">Disclosures</a></li>';
    echo '</ul>';
}

// Register Sidebar / Widget Area
function peak_theme_widgets_init() {
    register_sidebar( array(
        'name'          => __( 'Service Sidebar', 'peak-internet' ),
        'id'            => 'service-sidebar',
        'description'   => __( 'Widgets in this area will be shown on the "Service / Product Detail" template.', 'peak-internet' ),
        'before_widget' => '<div id="%1$s" class="service-widget-area %2$s">',
        'after_widget'  => '</div>',
        'before_title'  => '<h2 class="widgettitle">',
        'after_title'   => '</h2>',
    ) );
    
    register_sidebar( array(
        'name'          => __( 'Blog Sidebar', 'peak-internet' ),
        'id'            => 'blog-sidebar',
        'description'   => __( 'Widgets in this area will be shown on standard posts and archives.', 'peak-internet' ),
        'before_widget' => '<div id="%1$s" class="service-widget-area %2$s">',
        'after_widget'  => '</div>',
        'before_title'  => '<h2 class="widgettitle">',
        'after_title'   => '</h2>',
    ) );
}
add_action( 'widgets_init', 'peak_theme_widgets_init' );

// Register Custom Block Patterns
function peak_register_block_patterns() {
    register_block_pattern_category(
        'peak-elements',
        array( 'label' => __( 'PEAK Elements', 'peak-internet' ) )
    );

    // Hero Banner Pattern
    register_block_pattern(
        'peak/hero-banner',
        array(
            'title'       => __( 'Hero Banner', 'peak-internet' ),
            'description' => _x( 'A full-width primary hero banner.', 'Block pattern description', 'peak-internet' ),
            'content'     => '
                <!-- wp:html -->
                <section class="hero-section">
                    <div class="container hero-content">
                        <div class="hero-text">
                            <h1>Fast, Reliable Internet for Your Home</h1>
                            <p>Experience gigabit speeds with local support and no data caps. Upgrade to PEAK today.</p>
                            <div class="hero-cta">
                                <a href="https://peak.smarthub.coop/Shop.html" target="_blank" class="btn btn-primary">Check Availability</a>
                                <a href="internet-plans.html" class="btn btn-secondary">View Plans</a>
                            </div>
                        </div>
                    </div>
                </section>
                <!-- /wp:html -->
            ',
            'categories'  => array( 'peak-elements', 'header' ),
        )
    );

    // Feature Grid Pattern
    register_block_pattern(
        'peak/feature-grid',
        array(
            'title'       => __( 'Feature Grid', 'peak-internet' ),
            'description' => _x( 'A 3-column responsive grid with icons.', 'Block pattern description', 'peak-internet' ),
            'content'     => '
                <!-- wp:html -->
                <section class="features-section bg-light">
                    <div class="container">
                        <div class="section-header text-center">
                            <h2>Why Choose PEAK</h2>
                            <p>We are a local cooperative dedicated to bringing the best connection to our community.</p>
                        </div>
                        <div class="features-grid">
                            <div class="feature-card">
                                <div class="feature-icon"><i class="ph ph-rocket-launch"></i></div>
                                <h3>Gigabit Speeds</h3>
                                <p>Symmetrical upload and download speeds up to 1000 Mbps.</p>
                            </div>
                            <div class="feature-card">
                                <div class="feature-icon"><i class="ph ph-infinity"></i></div>
                                <h3>No Data Caps</h3>
                                <p>Stream, game, and download as much as you want without limits or overage fees.</p>
                            </div>
                            <div class="feature-card">
                                <div class="feature-icon"><i class="ph ph-headset"></i></div>
                                <h3>Local Support</h3>
                                <p>24/7 technical support from our local team based right here in the Willamette Valley.</p>
                            </div>
                        </div>
                    </div>
                </section>
                <!-- /wp:html -->
            ',
            'categories'  => array( 'peak-elements', 'columns' ),
        )
    );
    
    // Call to Action Pattern
    register_block_pattern(
        'peak/cta-banner',
        array(
            'title'       => __( 'Call to Action Banner', 'peak-internet' ),
            'description' => _x( 'A centered call to action section.', 'Block pattern description', 'peak-internet' ),
            'content'     => '
                <!-- wp:html -->
                <section class="cta-section" style="text-align: center; padding: 80px 0; background: var(--color-bg-mute); border-radius: var(--radius-lg); margin: 60px 0;">
                    <h2>Ready to get started?</h2>
                    <p style="margin-bottom: 24px;">Check your address or speak with our local team today.</p>
                    <a href="https://peak.smarthub.coop/Shop.html" target="_blank" class="btn btn-primary">Check Availability</a>
                </section>
                <!-- /wp:html -->
            ',
            'categories'  => array( 'peak-elements' ),
        )
    );
}
add_action( 'init', 'peak_register_block_patterns' );

// No static auto-import here - it is dynamically generated and appended by Python


// Add custom classes to nav menu links
function peak_add_menu_link_class( $atts, $item, $args ) {
    if ( property_exists( $args, 'link_class' ) && !empty($args->link_class) ) {
        if ( isset( $atts['class'] ) ) {
            $atts['class'] .= ' ' . $args->link_class;
        } else {
            $atts['class'] = $args->link_class;
        }
    }
    return $atts;
}
add_filter( 'nav_menu_link_attributes', 'peak_add_menu_link_class', 1, 3 );
"""
    with open(os.path.join(THEME_DIR, 'functions.php'), 'w', encoding='utf-8') as f:
        f.write(content)

def write_header_php():
    content = """<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="<?php bloginfo('description'); ?>">
    <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
    <?php wp_body_open(); ?>
    <div id="app-root">
        <!-- Utility Bar -->
        <div class="utility-bar">
            <div class="container utility-content">
                <div class="utility-left">
                    <span><i class="ph ph-phone"></i> <?php esc_html_e( '24/7 Support: 541-754-PEAK (7325)', 'peak-internet' ); ?></span>
                </div>
                <div class="utility-right">
                    <a href="https://webmail.peak.org/" target="_blank"><i class="ph ph-envelope"></i> <?php esc_html_e( 'Web Mail', 'peak-internet' ); ?></a>
                    <a href="https://peak.smarthub.coop/Login.html" target="_blank"><i class="ph ph-user"></i> <?php esc_html_e( 'My Account', 'peak-internet' ); ?></a>
                </div>
            </div>
        </div>

        <!-- Main Navigation -->
        <header class="main-header">
            <div class="container header-content">
                <?php if ( has_custom_logo() ) : ?>
                    <div class="site-logo"><?php the_custom_logo(); ?></div>
                <?php else : ?>
                    <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="brand-logo" rel="home">
                        <span class="logo-peak"><?php esc_html_e( 'PEAK', 'peak-internet' ); ?></span>
                        <span class="logo-internet"><?php esc_html_e( 'INTERNET', 'peak-internet' ); ?></span>
                    </a>
                <?php endif; ?>

                <div class="segment-toggle">
                    <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="toggle-btn <?php echo (is_front_page() || !is_page('business')) ? 'active' : ''; ?>" id="btn-residential"><?php esc_html_e( 'Residential', 'peak-internet' ); ?></a>
                    <a href="<?php echo esc_url( home_url( '/business' ) ); ?>" class="toggle-btn <?php echo is_page('business') ? 'active' : ''; ?>" id="btn-business"><?php esc_html_e( 'Business', 'peak-internet' ); ?></a>
                </div>

                <?php
                wp_nav_menu( array(
                    'theme_location' => 'primary',
                    'container'      => 'nav',
                    'container_class'=> 'main-nav',
                    'menu_class'     => 'main-nav-ul',
                    'link_class'     => 'nav-link',
                    'fallback_cb'    => false,
                ) );
                ?>

                <div class="header-actions">
                    <a href="https://peak.smarthub.coop/Shop.html" target="_blank" class="btn btn-primary"><?php esc_html_e( 'Check Availability', 'peak-internet' ); ?></a>
                </div>
            </div>
        </header>
"""
    with open(os.path.join(THEME_DIR, 'header.php'), 'w', encoding='utf-8') as f:
        f.write(content)

def write_footer_php():
    content = """        <!-- Footer -->
        <footer class="main-footer">
            <div class="container footer-content">
                <div class="footer-brand">
                    <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="brand-logo footer-logo" rel="home">
                        <span class="logo-peak"><?php esc_html_e( 'PEAK', 'peak-internet' ); ?></span>
                        <span class="logo-internet"><?php esc_html_e( 'INTERNET', 'peak-internet' ); ?></span>
                    </a>
                    <p><?php esc_html_e( 'Demand PEAK performance. Delivering reliable gigabit internet to the Willamette Valley since 1999.', 'peak-internet' ); ?></p>
                    <div class="social-links">
                        <a href="https://www.facebook.com/peakinternet/" target="_blank"><span class="screen-reader-text"><?php esc_html_e( 'Facebook', 'peak-internet' ); ?></span><i class="ph-fill ph-facebook-logo" aria-hidden="true"></i></a>
                        <a href="https://twitter.com/peakinternet/" target="_blank"><span class="screen-reader-text"><?php esc_html_e( 'Twitter', 'peak-internet' ); ?></span><i class="ph-fill ph-twitter-logo" aria-hidden="true"></i></a>
                        <a href="https://www.youtube.com/user/PeakInternet" target="_blank"><span class="screen-reader-text"><?php esc_html_e( 'YouTube', 'peak-internet' ); ?></span><i class="ph-fill ph-youtube-logo" aria-hidden="true"></i></a>
                    </div>
                </div>

                <div class="footer-links">
                    <div class="link-group">
                        <h4><?php esc_html_e( 'Services', 'peak-internet' ); ?></h4>
                        <?php
                        wp_nav_menu( array(
                            'theme_location' => 'footer_services',
                            'container'      => false,
                            'menu_class'     => 'footer-menu-ul',
                            'fallback_cb'    => 'peak_footer_services_fallback',
                        ) );
                        ?>
                    </div>
                    <div class="link-group">
                        <h4><?php esc_html_e( 'Support', 'peak-internet' ); ?></h4>
                        <?php
                        wp_nav_menu( array(
                            'theme_location' => 'footer_support',
                            'container'      => false,
                            'menu_class'     => 'footer-menu-ul',
                            'fallback_cb'    => 'peak_footer_support_fallback',
                        ) );
                        ?>
                    </div>
                    <div class="link-group">
                        <h4><?php esc_html_e( 'Company', 'peak-internet' ); ?></h4>
                        <?php
                        wp_nav_menu( array(
                            'theme_location' => 'footer_company',
                            'container'      => false,
                            'menu_class'     => 'footer-menu-ul',
                            'fallback_cb'    => 'peak_footer_company_fallback',
                        ) );
                        ?>
                    </div>
                </div>
            </div>
            <div class="container footer-bottom">
                <p>&copy; <?php echo esc_html( date('Y') ); ?> <?php esc_html_e( 'PEAK Internet. All rights reserved.', 'peak-internet' ); ?></p>
                <div class="bottom-links">
                    <a href="<?php echo esc_url( home_url( '/disclosures' ) ); ?>"><?php esc_html_e( 'Privacy Policy', 'peak-internet' ); ?></a>
                    <a href="<?php echo esc_url( home_url( '/disclosures' ) ); ?>"><?php esc_html_e( 'Terms of Service', 'peak-internet' ); ?></a>
                </div>
            </div>
        </footer>
    </div>
    <?php wp_footer(); ?>
</body>
</html>
"""
    with open(os.path.join(THEME_DIR, 'footer.php'), 'w', encoding='utf-8') as f:
        f.write(content)

def convert_html_files():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    pages_php = """
// Auto-Import Pages and HTML directly into Database on Activation
function peak_theme_auto_import_pages() {
    // Only run this heavy import script once. Uses WP options table to track.
    if ( get_option( 'peak_theme_imported_v6' ) ) {
        return;
    }

    $pages_to_create = array(
"""

    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        match = re.search(r'<main.*?>(.*?)</main>', content, re.DOTALL | re.IGNORECASE)
        
        if match:
            main_content = match.group(1).strip()
            main_content = main_content.replace('href="assets/', 'href="/wp-content/themes/peak-theme/assets/')
            main_content = main_content.replace('src="assets/', 'src="/wp-content/themes/peak-theme/assets/')
            main_content = re.sub(r'href="([^"]+)\.html(#?.*?)"', "href=\"/\\1/\\2\"", main_content)
            
            if html_file == 'index.html':
                page_title = 'Home'
                slug = 'home'
            else:
                page_title = html_file.replace('.html', '').replace('-', ' ').title()
                slug = html_file.replace('.html', '')
                
            template_name = 'template-full-width.php'
            
            # Wrap in WP Block comments so the editor doesn't freak out and strip styles
            wp_block_content = f"""<!-- wp:group {{"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group">
<!-- wp:html -->
{main_content}
<!-- /wp:html -->
</div>
<!-- /wp:group -->"""
            
            b64_html = base64.b64encode(wp_block_content.encode('utf-8')).decode('utf-8')
            
            pages_php += f"""        array(
            'title'    => '{page_title}',
            'slug'     => '{slug}',
            'template' => '{template_name}',
            'content'  => base64_decode('{b64_html}')
        ),
"""

    pages_php += """    );

    foreach ( $pages_to_create as $page_data ) {
        // Query to find real published/draft page, avoiding items in the Trash
        $args = array(
            'name'        => $page_data['slug'],
            'post_type'   => 'page',
            'post_status' => array('publish', 'draft'),
            'numberposts' => 1
        );
        $existing_pages = get_posts($args);
        
        if ( empty($existing_pages) ) {
            // Create brand new page
            $new_page_id = wp_insert_post( array(
                'post_title'     => $page_data['title'],
                'post_name'      => $page_data['slug'],
                'post_content'   => $page_data['content'],
                'post_status'    => 'publish',
                'post_type'      => 'page',
                'post_author'    => 1,
            ) );
            
            if ( $new_page_id && !is_wp_error( $new_page_id ) ) {
                update_post_meta( $new_page_id, '_wp_page_template', $page_data['template'] );
            }
        } else {
            // Force Update existing page to inject the missing layout!
            $existing_page_id = $existing_pages[0]->ID;
            wp_update_post( array(
                'ID'           => $existing_page_id,
                'post_content' => $page_data['content']
            ) );
            update_post_meta( $existing_page_id, '_wp_page_template', $page_data['template'] );
        }
    }

    // Set Front Page
    $home_page = get_page_by_title( 'Home' );
    if ( isset( $home_page->ID ) ) {
        update_option( 'show_on_front', 'page' );
        update_option( 'page_on_front', $home_page->ID );
    }
    
    // Tag this version as successfully imported so it doesn't overwrite future user edits
    update_option( 'peak_theme_imported_v6', true );

    // Clear permalink structure cache so new pages resolve
    flush_rewrite_rules();
}
// Using admin_init guarantees it fires when the user views the dashboard
add_action( 'admin_init', 'peak_theme_auto_import_pages' );
"""
    # Simply append this whole dynamic script to the end of functions.php
    with open(os.path.join(THEME_DIR, 'functions.php'), 'a', encoding='utf-8') as f:
        f.write(pages_php)

def write_index_php():
    content = """<?php
get_header();
?>
<main id="primary" class="site-main">
    <div class="container generic-page-container">
        <?php
        if ( have_posts() ) {
            while ( have_posts() ) {
                the_post();
                ?>
                <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
                    <?php echo '<h1 class="entry-title"><a href="' . esc_url( get_permalink() ) . '">' . get_the_title() . '</a></h1>'; ?>
                    <div class="entry-content">
                        <?php the_content(); ?>
                    </div>
                </article>
                <?php
            }
        } else {
            echo '<p>' . esc_html__( 'No posts found.', 'peak-internet' ) . '</p>';
        }
        ?>
    </div>
</main>
<?php
get_footer();
?>"""
    with open(os.path.join(THEME_DIR, 'index.php'), 'w', encoding='utf-8') as f:
        f.write(content)

def write_page_php():
    content = """<?php
/**
 * Default Page Template
 */
get_header();
?>
<main id="primary" class="site-main">
    <div class="container generic-page-container">
        <?php
        while ( have_posts() ) :
            the_post();
            ?>
            <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
                <?php echo '<h1 class="entry-title">' . get_the_title() . '</h1>'; ?>
                <div class="entry-content">
                    <?php the_content(); ?>
                </div>
            </article>
            <?php
        endwhile;
        ?>
    </div>
</main>
<?php
get_footer();
?>"""
    with open(os.path.join(THEME_DIR, 'page.php'), 'w', encoding='utf-8') as f:
        f.write(content)

def write_single_php():
    content = """<?php
/**
 * Default Post (News/Blog) Template
 */
get_header();
?>
<main id="primary" class="site-main">
    <div class="container generic-page-container">
        <?php
        while ( have_posts() ) :
            the_post();
            ?>
            <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
                <style>.post-meta { color: var(--color-text-mute); font-size: 0.875rem; margin-bottom: 24px; }</style>
                <?php echo '<h1 class="entry-title">' . get_the_title() . '</h1>'; ?>
                <div class="post-meta">
                    <?php 
                    printf( 
                        esc_html__( 'Published on %s', 'peak-internet' ), 
                        get_the_date() 
                    ); 
                    ?>
                </div>
                
                <?php if ( has_post_thumbnail() ) : ?>
                    <div class="post-thumbnail" style="margin-bottom: 32px;">
                        <?php the_post_thumbnail('large', array('style' => 'width: 100%; height: auto; border-radius: 16px; object-fit: cover; max-height: 400px;')); ?>
                    </div>
                <?php endif; ?>
                
                <div class="entry-content">
                    <?php the_content(); ?>
                </div>
                
                <?php
                if ( comments_open() || get_comments_number() ) :
                    comments_template();
                endif;
                ?>
            </article>
            <?php
        endwhile;
        ?>
    </div>
</main>
<?php
get_footer();
?>"""
    with open(os.path.join(THEME_DIR, 'single.php'), 'w', encoding='utf-8') as f:
        f.write(content)


def write_specialized_templates_php():
    # 1. Full Width Template
    full_width = """<?php
/**
 * Template Name: Full Width (No Container)
 * Description: A full-width page template for building marketing landing pages using the block editor.
 */
?>
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
    <?php wp_body_open(); ?>
    
    <?php
    while ( have_posts() ) :
        the_post();
        the_content();
    endwhile;
    ?>
    
    <?php wp_footer(); ?>
</body>
</html>
"""
    with open(os.path.join(THEME_DIR, 'template-full-width.php'), 'w', encoding='utf-8') as f:
        f.write(full_width)

    # 2. Service Detail with Sidebar Template
    service_sidebar = """<?php
/**
 * Template Name: Service / Product Detail (With Sidebar)
 * Description: A standard side-by-side layout for detailing specific internet services or packages.
 */
get_header();
?>
<main>
    <div class="container template-service-sidebar">
        <div class="template-content">
            <?php
            while ( have_posts() ) :
                the_post();
                echo '<h1>' . get_the_title() . '</h1>';
                the_content();
            endwhile;
            ?>
        </div>
        
        <aside class="template-sidebar">
            <?php if ( is_active_sidebar( 'service-sidebar' ) ) : ?>
                <?php dynamic_sidebar( 'service-sidebar' ); ?>
            <?php else : ?>
                <div class="service-widget-area">
                    <h2 class="widgettitle">Need Help?</h2>
                    <p>Go to <strong>Appearance > Widgets</strong> in the WordPress dashboard to add elements to this sidebar.</p>
                </div>
            <?php endif; ?>
        </aside>
    </div>
</main>
<?php
get_footer();
?>"""
    with open(os.path.join(THEME_DIR, 'template-service-sidebar.php'), 'w', encoding='utf-8') as f:
        f.write(service_sidebar)

    # 3. Support / Knowledge Base Article
    support_article = """<?php
/**
 * Template Name: Knowledge Base / Support Article
 * Description: A narrow, clean reading template for technical guides.
 */
get_header();
?>
<main>
    <div class="support-article-container">
        <div class="support-article-header">
            <span class="badge">Support Article</span>
            <h1><?php the_title(); ?></h1>
            <p style="color: var(--color-text-mute);">Last updated: <?php the_modified_date(); ?></p>
        </div>
        
        <div class="support-article-content">
            <?php
            while ( have_posts() ) :
                the_post();
                the_content();
            endwhile;
            ?>
        </div>
        
        <div style="border-top: 1px solid var(--color-border); margin-top: 60px; padding-top: 40px; text-align: center;">
            <p>Still need help? <a href="<?php echo esc_url( home_url( '/support' ) ); ?>" style="font-weight: 600; color: var(--color-primary);">Contact Support</a></p>
        </div>
    </div>
</main>
<?php
get_footer();
?>"""
    with open(os.path.join(THEME_DIR, 'template-support-article.php'), 'w', encoding='utf-8') as f:
        f.write(support_article)

def write_core_templates_php():
    # 1. 404 Template
    four_o_four = """<?php
/**
 * The template for displaying 404 pages (not found)
 */
get_header();
?>
<main id="primary" class="site-main">
    <div class="container generic-page-container" style="text-align: center; padding: 120px 0;">
        <h1 class="page-title" style="font-size: 6rem; color: var(--color-primary); margin-bottom: 0;">404</h1>
        <h2><?php esc_html_e( 'Oops! That page can&rsquo;t be found.', 'peak-internet' ); ?></h2>
        <p><?php esc_html_e( 'It looks like nothing was found at this location. Maybe try a search?', 'peak-internet' ); ?></p>
        <div style="max-width: 500px; margin: 40px auto 0;">
            <?php get_search_form(); ?>
        </div>
    </div>
</main>
<?php
get_footer();
?>"""
    with open(os.path.join(THEME_DIR, '404.php'), 'w', encoding='utf-8') as f:
        f.write(four_o_four)

    # 2. Search Results Template
    search_php = """<?php
/**
 * The template for displaying search results pages
 */
get_header();
?>
<main id="primary" class="site-main">
    <div class="container generic-page-container">
        <?php if ( have_posts() ) : ?>
            <header class="page-header" style="margin-bottom: 40px; border-bottom: 1px solid var(--color-border); padding-bottom: 24px;">
                <h1 class="page-title">
                    <?php
                    /* translators: %s: search query. */
                    printf( esc_html__( 'Search Results for: %s', 'peak-internet' ), '<span>' . get_search_query() . '</span>' );
                    ?>
                </h1>
            </header>

            <?php
            while ( have_posts() ) :
                the_post();
                ?>
                <article id="post-<?php the_ID(); ?>" <?php post_class(); ?> style="margin-bottom: 40px;">
                    <h2 class="entry-title"><a href="<?php echo esc_url( get_permalink() ); ?>" style="color: var(--color-primary-dark);"><?php the_title(); ?></a></h2>
                    <div class="entry-summary">
                        <?php the_excerpt(); ?>
                    </div>
                </article>
                <?php
            endwhile;

            the_posts_navigation();

        else :
            ?>
            <section class="no-results not-found">
                <header class="page-header">
                    <h1 class="page-title"><?php esc_html_e( 'Nothing Found', 'peak-internet' ); ?></h1>
                </header>
                <div class="page-content">
                    <p><?php esc_html_e( 'Sorry, but nothing matched your search terms. Please try again with some different keywords.', 'peak-internet' ); ?></p>
                    <?php get_search_form(); ?>
                </div>
            </section>
            <?php
        endif;
        ?>
    </div>
</main>
<?php
get_footer();
?>"""
    with open(os.path.join(THEME_DIR, 'search.php'), 'w', encoding='utf-8') as f:
        f.write(search_php)
        
    # 3. Archive Template
    archive_php = """<?php
/**
 * The template for displaying archive pages
 */
get_header();
?>
<main id="primary" class="site-main">
    <div class="container generic-page-container">
        <?php if ( have_posts() ) : ?>
            <header class="page-header" style="margin-bottom: 40px; border-bottom: 1px solid var(--color-border); padding-bottom: 24px;">
                <?php
                the_archive_title( '<h1 class="page-title">', '</h1>' );
                the_archive_description( '<div class="archive-description">', '</div>' );
                ?>
            </header>

            <?php
            while ( have_posts() ) :
                the_post();
                ?>
                <article id="post-<?php the_ID(); ?>" <?php post_class(); ?> style="margin-bottom: 40px;">
                    <h2 class="entry-title"><a href="<?php echo esc_url( get_permalink() ); ?>" style="color: var(--color-primary-dark);"><?php the_title(); ?></a></h2>
                    <div class="entry-summary">
                        <?php the_excerpt(); ?>
                    </div>
                </article>
                <?php
            endwhile;

            the_posts_navigation();

        else :
            ?>
            <section class="no-results not-found">
                <header class="page-header">
                    <h1 class="page-title"><?php esc_html_e( 'Nothing Found', 'peak-internet' ); ?></h1>
                </header>
                <div class="page-content">
                    <p><?php esc_html_e( 'It seems we can&rsquo;t find what you&rsquo;re looking for. Perhaps searching can help.', 'peak-internet' ); ?></p>
                    <?php get_search_form(); ?>
                </div>
            </section>
            <?php
        endif;
        ?>
    </div>
</main>
<?php
get_footer();
?>"""
    with open(os.path.join(THEME_DIR, 'archive.php'), 'w', encoding='utf-8') as f:
        f.write(archive_php)

if __name__ == '__main__':
    setup_theme_dir()
    write_style_css()
    write_functions_php()
    write_header_php()
    write_footer_php()
    convert_html_files()
    write_index_php()
    write_page_php()
    write_single_php()
    write_specialized_templates_php()
    write_core_templates_php()
    print("Theme conversion completed successfully!")
