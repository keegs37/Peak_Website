<?php
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
?>