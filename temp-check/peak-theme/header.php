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
                    <span><i class="ph ph-phone"></i> 24/7 Support: 541-754-PEAK (7325)</span>
                </div>
                <div class="utility-right">
                    <a href="https://webmail.peak.org/" target="_blank"><i class="ph ph-envelope"></i> Web Mail</a>
                    <a href="https://peak.smarthub.coop/Login.html" target="_blank"><i class="ph ph-user"></i> My Account</a>
                </div>
            </div>
        </div>

        <!-- Main Navigation -->
        <header class="main-header">
            <div class="container header-content">
                <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="brand-logo">
                    <span class="logo-peak">PEAK</span>
                    <span class="logo-internet">INTERNET</span>
                </a>

                <div class="segment-toggle">
                    <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="toggle-btn <?php echo (is_front_page() || !is_page('business')) ? 'active' : ''; ?>" id="btn-residential">Residential</a>
                    <a href="<?php echo esc_url( home_url( '/business' ) ); ?>" class="toggle-btn <?php echo is_page('business') ? 'active' : ''; ?>" id="btn-business">Business</a>
                </div>

                <nav class="main-nav">
                    <a href="<?php echo esc_url( home_url( '/internet-plans' ) ); ?>" class="nav-link">Internet Plans</a>
                    <a href="<?php echo esc_url( home_url( '/advanced-services' ) ); ?>" class="nav-link">TV & Voice</a>
                    <a href="<?php echo esc_url( home_url( '/support' ) ); ?>" class="nav-link">Support</a>
                </nav>

                <div class="header-actions">
                    <a href="https://peak.smarthub.coop/Shop.html" target="_blank" class="btn btn-primary">Check Availability</a>
                </div>
            </div>
        </header>
