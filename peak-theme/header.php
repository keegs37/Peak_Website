<!DOCTYPE html>
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
