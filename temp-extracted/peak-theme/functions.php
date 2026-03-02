<?php
function peak_theme_enqueue_styles() {
    wp_enqueue_style( 'peak-main-style', get_template_directory_uri() . '/styles.css', array(), '1.0' );
    wp_enqueue_style( 'peak-wp-style', get_stylesheet_uri(), array('peak-main-style'), '1.0' );
    wp_enqueue_style( 'peak-google-fonts', 'https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Inter:wght@400;500;600&display=swap', false );
    
    // Phosphor Icons
    wp_enqueue_script( 'phosphor-icons', 'https://unpkg.com/@phosphor-icons/web', array(), null, false );
    
    // Main JS
    wp_enqueue_script( 'peak-main-js', get_template_directory_uri() . '/main.js', array(), '1.0', true );
}
add_action( 'wp_enqueue_scripts', 'peak_theme_enqueue_styles' );

function peak_theme_setup() {
    add_theme_support( 'title-tag' );
    add_theme_support( 'post-thumbnails' );
    register_nav_menus( array(
        'primary' => __( 'Primary Menu', 'peak-internet' ),
        'footer_services' => __( 'Footer Services', 'peak-internet' ),
        'footer_support' => __( 'Footer Support', 'peak-internet' ),
        'footer_company' => __( 'Footer Company', 'peak-internet' ),
    ) );
}
add_action( 'after_setup_theme', 'peak_theme_setup' );
