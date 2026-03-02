<?php
/* Template Name: Careers */
get_header();
?>
<main>
            <!-- Page Header -->
            <section class="page-header">
                <div class="container">
                    <h1>Join the PEAK Team</h1>
                    <p>The strength of PEAK Internet lies in its employees. The people who work for PEAK contribute to
                        the vitality, creativity, knowledge, expertise, and dedication that make our organization an
                        exciting and challenging place to work. Our employees care about our customers, their community,
                        and each other, and it shows in their work, in their attitude, and in their actions.</p>
                    <p style="margin-top: 12px; font-size: 0.9rem; opacity: 0.9;">Any offer of employment with PEAK is
                        conditional on providing proof of identity and work eligibility within the US, passing a drug
                        test, successfully completing a background check, and signing the company's confidentiality,
                        work product, and non-solicitation agreement.</p>
                </div>
            </section>

            <!-- Benefits -->
            <section class="benefits-section">
                <div class="container">
                    <div class="section-header text-center animate-on-scroll">
                        <h2>Why Work at PEAK?</h2>
                        <p>We take care of our employees so they can take care of our community.</p>
                    </div>

                    <div class="benefits-grid">
                        <div class="benefit-item animate-on-scroll">
                            <div class="benefit-icon"><i class="ph ph-heartbeat"></i></div>
                            <h4>Health & Wellness</h4>
                            <p>Comprehensive health, dental, and vision insurance options for you and your family.</p>
                        </div>
                        <div class="benefit-item animate-on-scroll" style="transition-delay: 100ms;">
                            <div class="benefit-icon"><i class="ph ph-piggy-bank"></i></div>
                            <h4>Retirement</h4>
                            <p>Competitive 401(k) matching program to help you plan for the future.</p>
                        </div>
                        <div class="benefit-item animate-on-scroll" style="transition-delay: 200ms;">
                            <div class="benefit-icon"><i class="ph ph-airplane-tilt"></i></div>
                            <h4>Time Off</h4>
                            <p>Generous paid time off and paid holidays so you can recharge.</p>
                        </div>
                        <div class="benefit-item animate-on-scroll" style="transition-delay: 300ms;">
                            <div class="benefit-icon"><i class="ph ph-wifi-high"></i></div>
                            <h4>Employee Connectivity</h4>
                            <p>Discounted or free high-speed internet services for employees living in our footprint.
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Open Positions -->
            <section class="careers-section">
                <div class="container">
                    <div class="section-header text-center animate-on-scroll">
                        <h2>Current Openings</h2>
                        <p>Explore our available roles and join a company dedicated to local service.</p>
                    </div>

                    <div class="jobs-container">
                        <!-- BambooHR Dynamic Job Board Embed -->
                        <div id="BambooHR" data-domain="peak.bamboohr.com" data-version="1.0.0" data-departmentId=""
                            class="animate-on-scroll" style="width: 100%; min-height: 300px;"></div>
                        <script src="https://peak.bamboohr.com/js/embed.js" type="text/javascript" async defer></script>

                        <!-- Example format for when a job is available:
                        <div class="job-card animate-on-scroll">
                            <div class="job-header">
                                <div>
                                    <h3 class="job-title">Network Engineer</h3>
                                    <div class="job-meta">
                                        <span><i class="ph ph-map-pin"></i> Corvallis, OR</span>
                                        <span><i class="ph ph-clock"></i> Full-Time</span>
                                    </div>
                                </div>
                                <button class="btn btn-primary">Apply Now</button>
                            </div>
                            <p class="job-description">We are seeking a skilled Network Engineer to design, implement, maintain, and support our growing network infrastructure. You will be part of a systems engineering team that is responsible for designing and developing scalable, maintainable, highly available network architectures...</p>
                        </div>
                        -->
                    </div>
                </div>
            </section>
        </main>
<?php
get_footer();
?>