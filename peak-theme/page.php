<?php
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
?>