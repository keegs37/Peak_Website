<?php
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
?>