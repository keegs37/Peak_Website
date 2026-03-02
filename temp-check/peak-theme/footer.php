        <!-- Footer -->
        <footer class="main-footer">
            <div class="container footer-content">
                <div class="footer-brand">
                    <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="brand-logo footer-logo">
                        <span class="logo-peak">PEAK</span>
                        <span class="logo-internet">INTERNET</span>
                    </a>
                    <p>Demand PEAK performance. Delivering reliable gigabit internet to the Willamette Valley since 1999.</p>
                    <div class="social-links">
                        <a href="#"><i class="ph-fill ph-facebook-logo"></i></a>
                        <a href="#"><i class="ph-fill ph-twitter-logo"></i></a>
                        <a href="#"><i class="ph-fill ph-instagram-logo"></i></a>
                    </div>
                </div>

                <div class="footer-links">
                    <div class="link-group">
                        <h4>Services</h4>
                        <a href="<?php echo esc_url( home_url( '/internet-plans' ) ); ?>#fiber">PEAK Fiber</a>
                        <a href="<?php echo esc_url( home_url( '/internet-plans' ) ); ?>#wireless">Fixed Wireless</a>
                        <a href="<?php echo esc_url( home_url( '/advanced-services' ) ); ?>#wifi">Total Home Wi-Fi</a>
                        <a href="<?php echo esc_url( home_url( '/advanced-services' ) ); ?>#tv">Streaming TV</a>
                        <a href="<?php echo esc_url( home_url( '/business' ) ); ?>">Business Internet</a>
                    </div>
                    <div class="link-group">
                        <h4>Support</h4>
                        <a href="<?php echo esc_url( home_url( '/support' ) ); ?>">Contact Us</a>
                        <a href="https://peak.smarthub.coop/Login.html" target="_blank">Pay My Bill</a>
                        <a href="http://speedtest.peakinternet.com:7076/" target="_blank">Check Speed</a>
                        <a href="<?php echo esc_url( home_url( '/financial-assistance' ) ); ?>">Financial Assistance</a>
                        <a href="<?php echo esc_url( home_url( '/support' ) ); ?>">Tech Support</a>
                    </div>
                    <div class="link-group">
                        <h4>Company</h4>
                        <a href="<?php echo esc_url( home_url( '/about' ) ); ?>">Our Mission</a>
                        <a href="<?php echo esc_url( home_url( '/careers' ) ); ?>">Careers</a>
                        <a href="<?php echo esc_url( home_url( '/news' ) ); ?>">News</a>
                        <a href="<?php echo esc_url( home_url( '/disclosures' ) ); ?>">Disclosures</a>
                    </div>
                </div>
            </div>
            <div class="container footer-bottom">
                <p>&copy; <?php echo date('Y'); ?> PEAK Internet. All rights reserved.</p>
                <div class="bottom-links">
                    <a href="<?php echo esc_url( home_url( '/disclosures' ) ); ?>">Privacy Policy</a>
                    <a href="<?php echo esc_url( home_url( '/disclosures' ) ); ?>">Terms of Service</a>
                </div>
            </div>
        </footer>
    </div>
    <?php wp_footer(); ?>
</body>
</html>
