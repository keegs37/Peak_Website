<?php
/* Template Name: Business */
get_header();
?>
<main>
            <!-- Page Header -->
            <section class="page-header">
                <div class="container">
                    <h1>Keeping You Connected</h1>
                    <p>Keeping pace in today's business world requires reliable, high-speed broadband internet.
                        Customize your professional solutions with PEAK's Fiber and Fixed Wireless options.</p>
                </div>
            </section>

            <!-- Services Grid -->
            <section class="services-overview">
                <div class="container">
                    <div class="section-header text-center animate-on-scroll">
                        <h2>Business Internet Solutions</h2>
                        <p style="max-width: 700px; margin: 0 auto;">Discover the difference that PEAK can make for your
                            team's productivity. Offering everything from blazing fast gigabit Internet to PBX phone
                            services.</p>
                    </div>

                    <div class="biz-services-grid">
                        <!-- Advanced Internet -->
                        <div class="biz-card animate-on-scroll">
                            <div class="biz-card-icon"><i class="ph ph-globe"></i></div>
                            <h3>Advanced Internet</h3>
                            <p>Fully customized professional Internet solutions including shared fiber or dedicated
                                fiber connections tailored to the specific size and requirements of your organization.
                            </p>
                            <a href="<?php echo esc_url( home_url( '/biz-advanced-internet' ) ); ?>" class="biz-card-link">Learn More <i
                                    class="ph ph-arrow-right"></i></a>
                        </div>

                        <!-- Fixed Wireless -->
                        <div class="biz-card animate-on-scroll" style="transition-delay: 100ms;">
                            <div class="biz-card-icon"><i class="ph ph-broadcast"></i></div>
                            <h3>Fixed Wireless</h3>
                            <p>Get the reliable broadband connection you need from a shared frequency to a
                                fully-dedicated and licensed network anywhere in our robust coverage area.</p>
                            <a href="<?php echo esc_url( home_url( '/biz-fixed-wireless' ) ); ?>" class="biz-card-link">Learn More <i
                                    class="ph ph-arrow-right"></i></a>
                        </div>

                        <!-- Advanced Voice -->
                        <div class="biz-card animate-on-scroll" style="transition-delay: 200ms;">
                            <div class="biz-card-icon"><i class="ph ph-phone-call"></i></div>
                            <h3>Advanced Voice</h3>
                            <p>Crystal-clear, reliable, affordable IP telephone services for your organization. Take
                                advantage of professional features including voicemail, call waiting, and more.</p>
                            <a href="<?php echo esc_url( home_url( '/biz-advanced-voice' ) ); ?>" class="biz-card-link">Learn More <i
                                    class="ph ph-arrow-right"></i></a>
                        </div>

                        <!-- Hosted PBX -->
                        <div class="biz-card animate-on-scroll" style="transition-delay: 300ms;">
                            <div class="biz-card-icon"><i class="ph ph-phone-list"></i></div>
                            <h3>Hosted PBX Services</h3>
                            <p>PEAK's hosted PBX boasts a full range of features to customize a state-of-the-art phone
                                system that meets your modern business communications needs.</p>
                            <a href="<?php echo esc_url( home_url( '/biz-hosted-pbx' ) ); ?>" class="biz-card-link">Learn More <i
                                    class="ph ph-arrow-right"></i></a>
                        </div>

                        <!-- Carrier Services -->
                        <div class="biz-card animate-on-scroll" style="transition-delay: 400ms;">
                            <div class="biz-card-icon"><i class="ph ph-buildings"></i></div>
                            <h3>Carrier Services</h3>
                            <p>Enterprise connectivity for multiple locations using our robust network. Options include
                                Dedicated Internet Access (DIA), Ethernet Transport, and Circuit Leases.</p>
                            <a href="<?php echo esc_url( home_url( '/biz-carrier-services' ) ); ?>" class="biz-card-link">Learn More <i
                                    class="ph ph-arrow-right"></i></a>
                        </div>

                        <!-- Colocation -->
                        <div class="biz-card animate-on-scroll" style="transition-delay: 500ms;">
                            <div class="biz-card-icon"><i class="ph ph-server"></i></div>
                            <h3>Server Colocation</h3>
                            <p>System security and continuous connectivity for your mission-critical applications in our
                                fully redundant facility with instant scalability capabilities.</p>
                            <a href="<?php echo esc_url( home_url( '/biz-colocation' ) ); ?>" class="biz-card-link">Learn More <i
                                    class="ph ph-arrow-right"></i></a>
                        </div>
                    </div>
                </div>
            </section>

            <!-- CTA Section -->
            <section class="cta-section animate-on-scroll">
                <div class="container">
                    <div class="cta-box">
                        <h2>Get PEAK Business Solutions Today!</h2>
                        <p>Call to receive a customized business needs assessment. Or fill out our form and our
                            enterprise team will reach out directly to build your solution.</p>

                        <a href="tel:541-754-7325" class="cta-phone">541-754-7325</a>

                        <a href="mailto:info@peakinternet.com" class="btn btn-primary"
                            style="padding: 16px 32px; font-size: 1.125rem; display: inline-flex;">Request Custom
                            Quote</a>
                    </div>
                </div>
            </section>
        </main>
<?php
get_footer();
?>