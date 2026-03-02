        <!-- Footer -->
        <footer class="main-footer">
            <div class="container footer-content">
                <div class="footer-brand">
                    <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="brand-logo footer-logo" rel="home">
                        <span class="logo-peak"><?php esc_html_e( 'PEAK', 'peak-internet' ); ?></span>
                        <span class="logo-internet"><?php esc_html_e( 'INTERNET', 'peak-internet' ); ?></span>
                    </a>
                    <p><?php esc_html_e( 'Demand PEAK performance. Delivering reliable gigabit internet to the Willamette Valley since 1999.', 'peak-internet' ); ?></p>
                    <div class="social-links">
                        <a href="https://www.facebook.com/peakinternet/" target="_blank"><span class="screen-reader-text"><?php esc_html_e( 'Facebook', 'peak-internet' ); ?></span><i class="ph-fill ph-facebook-logo" aria-hidden="true"></i></a>
                        <a href="https://twitter.com/peakinternet/" target="_blank"><span class="screen-reader-text"><?php esc_html_e( 'Twitter', 'peak-internet' ); ?></span><i class="ph-fill ph-twitter-logo" aria-hidden="true"></i></a>
                        <a href="https://www.youtube.com/user/PeakInternet" target="_blank"><span class="screen-reader-text"><?php esc_html_e( 'YouTube', 'peak-internet' ); ?></span><i class="ph-fill ph-youtube-logo" aria-hidden="true"></i></a>
                    </div>
                </div>

                <div class="footer-links">
                    <div class="link-group">
                        <h4><?php esc_html_e( 'Services', 'peak-internet' ); ?></h4>
                        <?php
                        wp_nav_menu( array(
                            'theme_location' => 'footer_services',
                            'container'      => false,
                            'menu_class'     => 'footer-menu-ul',
                            'fallback_cb'    => 'peak_footer_services_fallback',
                        ) );
                        ?>
                    </div>
                    <div class="link-group">
                        <h4><?php esc_html_e( 'Support', 'peak-internet' ); ?></h4>
                        <?php
                        wp_nav_menu( array(
                            'theme_location' => 'footer_support',
                            'container'      => false,
                            'menu_class'     => 'footer-menu-ul',
                            'fallback_cb'    => 'peak_footer_support_fallback',
                        ) );
                        ?>
                    </div>
                    <div class="link-group">
                        <h4><?php esc_html_e( 'Company', 'peak-internet' ); ?></h4>
                        <?php
                        wp_nav_menu( array(
                            'theme_location' => 'footer_company',
                            'container'      => false,
                            'menu_class'     => 'footer-menu-ul',
                            'fallback_cb'    => 'peak_footer_company_fallback',
                        ) );
                        ?>
                    </div>
                </div>
            </div>
            <div class="container footer-bottom">
                <p>&copy; <?php echo esc_html( date('Y') ); ?> <?php esc_html_e( 'PEAK Internet. All rights reserved.', 'peak-internet' ); ?></p>
                <div class="bottom-links">
                    <a href="<?php echo esc_url( home_url( '/disclosures' ) ); ?>"><?php esc_html_e( 'Privacy Policy', 'peak-internet' ); ?></a>
                    <a href="<?php echo esc_url( home_url( '/disclosures' ) ); ?>"><?php esc_html_e( 'Terms of Service', 'peak-internet' ); ?></a>
                </div>
            </div>
        </footer>
    </div>
    <?php wp_footer(); ?>
</body>
</html>
