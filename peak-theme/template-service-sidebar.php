<?php
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
?>