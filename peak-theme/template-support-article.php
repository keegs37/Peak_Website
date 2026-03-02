<?php
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
?>