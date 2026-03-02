<?php
/* Template Name: Advanced Services */
get_header();
?>
<main>
            <!-- Page Header -->
            <section class="page-header">
                <div class="container">
                    <h1>Advanced Services</h1>
                    <p>Complete your connected home with our suite of premium add-ons.</p>
                </div>
            </section>

            <section class="container animate-on-scroll">
                <div class="services-grid-page">
                    <!-- Wi-Fi -->
                    <div class="service-card" id="wifi">
                        <div class="s-icon"><i class="ph ph-router"></i></div>
                        <h2>Total Home Wi-Fi</h2>
                        <p>When you sign up for PEAK Fiber or Fixed Wireless Internet service, our Total Home Standard
                            Wi-Fi plan with top-tech Wi-Fi equipment is included! For larger homes, upgrade to our
                            Premium Total Managed Wi-Fi. Access and control your home network from your smart phone or
                            tablet with our CommandIQ Suite.</p>
                        <a href="<?php echo esc_url( home_url( \'/home-wifi\' ) ); ?>" class="btn btn-outline dark w-full text-center" style="display:block;">Learn More</a>
                    </div>

                    <!-- Tech Home -->
                    <div class="service-card" id="tech-home">
                        <div class="s-icon"><i class="ph ph-shield-plus"></i></div>
                        <h2>Tech Home Support</h2>
                        <p>A complete home technology service that makes it easy to set up, use, protect and enjoy your
                            Internet-enabled devices anytime and anywhere. Say goodbye to the frustration of managing
                            your connected household.</p>
                        <a href="<?php echo esc_url( home_url( \'/tech-home\' ) ); ?>" class="btn btn-outline dark w-full text-center" style="display:block;">Learn More</a>
                    </div>

                    <!-- Streaming TV -->
                    <div class="service-card" id="tv">
                        <div class="s-icon"><i class="ph ph-television"></i></div>
                        <h2>Streaming TV Integration</h2>
                        <p>With our gigabit speeds, streaming your favorite shows from any platform is seamless. Say
                            goodbye to buffering and experience crystal clear 4K entertainment across all your devices
                            simultaneously. We also partner with DirecTV.</p>
                        <a href="<?php echo esc_url( home_url( \'/streaming-tv\' ) ); ?>" class="btn btn-outline dark w-full text-center" style="display:block;">Explore Options</a>
                    </div>

                    <!-- Advanced Voice -->
                    <div class="service-card" id="voice">
                        <div class="s-icon"><i class="ph ph-phone-call"></i></div>
                        <h2>Advanced Voice VoIP</h2>
                        <p>Reliable, crystal clear voice services for your home or business. Enjoy modern features like
                            voicemail-to-email, simultaneous ring, and call routing, all managed through our easy-to-use
                            Phone Management Portal.</p>
                        <a href="https://peak.ucvoiceportal.com/portal/" target="_blank"
                            class="btn btn-outline dark w-full text-center" style="display:block;">Phone Portal</a>
                    </div>
                </div>
            </section>
        </main>
<?php
get_footer();
?>