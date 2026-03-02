<?php
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
?>