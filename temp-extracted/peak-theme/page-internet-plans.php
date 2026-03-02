<?php
/* Template Name: Internet Plans */
get_header();
?>
<main>
            <!-- Page Header -->
            <section class="page-header">
                <div class="container">
                    <h1>Internet Plans</h1>
                    <p>Find the perfect speed for your home in the Mid-Willamette Valley.</p>
                </div>
            </section>

            <section class="plan-details-section">
                <div class="container">
                    <!-- Fiber -->
                    <div class="plan-row animate-on-scroll" id="fiber">
                        <div class="plan-info">
                            <div class="badge"><i class="ph-fill ph-lightning"></i> Most Reliable</div>
                            <h2>PEAK Fiber</h2>
                            <p>PEAK is building Fiber in East Linn county in the communities of Lebanon and Albany,
                                bringing you incredibly fast, symmetrical speeds up to 1GIG and beyond.</p>

                            <div class="plan-metrics">
                                <div class="metric">
                                    <h4>100Mbps - 1Gig</h4>
                                    <span>Symmetrical Speeds</span>
                                </div>
                                <div class="metric">
                                    <h4>Unlimited</h4>
                                    <span>No Data Caps</span>
                                </div>
                            </div>

                            <ul class="plan-features" style="margin-bottom: 30px;">
                                <li><i class="ph-fill ph-check-circle"></i> Unaffected by weather conditions</li>
                                <li><i class="ph-fill ph-check-circle"></i> Best for 4K streaming and competitive gaming
                                </li>
                                <li><i class="ph-fill ph-check-circle"></i> Total Home Standard Wi-Fi included</li>
                                <li><i class="ph-fill ph-check-circle"></i> Price for Life Guarantee eligible</li>
                            </ul>

                            <button class="btn btn-primary">Check Fiber Availability</button>
                        </div>
                        <div class="plan-image">
                            <img src="<?php echo get_template_directory_uri(); ?>/assets/fiber.png" alt="Family enjoying high-speed fiber internet in a smart home">
                        </div>
                    </div>

                    <!-- Fixed Wireless -->
                    <div class="plan-row animate-on-scroll" id="wireless">
                        <div class="plan-info">
                            <div class="badge" style="background-color: var(--color-text-mute); color: white;"><i
                                    class="ph-fill ph-wifi-high"></i> Widest Coverage</div>
                            <h2>Fixed Wireless</h2>
                            <p>Even in remote areas of the Mid-Willamette Valley, PEAK Fixed Wireless can bring you
                                reliable speeds. We pride ourselves on serving underserved areas in Linn, Lane, Benton,
                                Polk, and Marion counties.</p>

                            <div class="plan-metrics">
                                <div class="metric">
                                    <h4>3Mbps - 30Mbps</h4>
                                    <span>Dependable Speeds</span>
                                </div>
                                <div class="metric">
                                    <h4>Unlimited</h4>
                                    <span>No Data Caps</span>
                                </div>
                            </div>

                            <ul class="plan-features" style="margin-bottom: 30px;">
                                <li><i class="ph-fill ph-check-circle"></i> Rapid deployment and installation</li>
                                <li><i class="ph-fill ph-check-circle"></i> Reaches rural areas where fiber hasn't gone
                                    yet</li>
                                <li><i class="ph-fill ph-check-circle"></i> Total Home Standard Wi-Fi included</li>
                                <li><i class="ph-fill ph-check-circle"></i> Price for Life Guarantee eligible</li>
                            </ul>

                            <button class="btn btn-outline dark">See Wireless Availability</button>
                        </div>
                        <div class="plan-image">
                            <img src="<?php echo get_template_directory_uri(); ?>/assets/wireless.png"
                                alt="A modern rural home with fixed wireless internet capability">
                        </div>
                    </div>
                </div>
            </section>
        </main>
<?php
get_footer();
?>