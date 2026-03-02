<?php
/* Template Name: Support */
get_header();
?>
<main>
            <!-- Page Header -->
            <section class="page-header">
                <div class="container">
                    <h1>We're Here to Help</h1>
                    <p>24/7 technical support and customer service for all PEAK Internet customers.</p>
                </div>
            </section>

            <section class="container animate-on-scroll">
                <div class="support-section">
                    <!-- Contact Info -->
                    <div class="contact-card">
                        <h2>Contact Information</h2>

                        <div class="contact-method">
                            <i class="ph-fill ph-phone-call"></i>
                            <div>
                                <span>541-754-PEAK (7325)</span>
                                <p>24/7 Technical Support & Customer Care</p>
                            </div>
                        </div>

                        <div class="contact-method">
                            <i class="ph-fill ph-envelope-simple"></i>
                            <div>
                                <span>support@peakinternet.com</span>
                                <p>Typical response time: 24-48 hours</p>
                            </div>
                        </div>

                        <div class="contact-method">
                            <i class="ph-fill ph-map-pin"></i>
                            <div>
                                <span>Headquarters</span>
                                <p>Willamette Valley, Oregon</p>
                            </div>
                        </div>
                    </div>

                    <!-- Quick Links -->
                    <div class="quick-links-card">
                        <h2>Support Resources</h2>
                        <div class="links-grid">
                            <a href="<?php echo esc_url( home_url( \'/https://peak.smarthub.coop/Shop\' ) ); ?>" target="_blank" class="support-link-btn">
                                <i class="ph ph-credit-card"></i> Pay My Bill
                            </a>
                            <a href="http://speedtest.peakinternet.com:7076/" target="_blank" class="support-link-btn">
                                <i class="ph ph-gauge"></i> Run Speed Test
                            </a>
                            <a href="https://www.peakinternet.com/residential/internet/fiberhood-watch/" target="_blank"
                                class="support-link-btn">
                                <i class="ph ph-binoculars"></i> Check My FiberHood
                            </a>
                            <a href="https://webmail.peak.org/" target="_blank" class="support-link-btn">
                                <i class="ph ph-envelope"></i> Access Web Mail
                            </a>
                            <a href="https://www.peakinternet.com/financial-assistance/" target="_blank"
                                class="support-link-btn">
                                <i class="ph ph-hand-coins"></i> Financial Assistance
                            </a>
                            <a href="https://peak.ucvoiceportal.com/portal/" target="_blank" class="support-link-btn">
                                <i class="ph ph-phone"></i> Phone Portal
                            </a>
                        </div>
                    </div>
                </div>
            </section>
        </main>
<?php
get_footer();
?>