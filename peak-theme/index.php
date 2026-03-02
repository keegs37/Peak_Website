<?php
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
?>