<?php
/* Template Name: Financial Assistance */
get_header();
?>
<main>
            <!-- Page Header -->
            <section class="page-header">
                <div class="container">
                    <h1>Financial Assistance</h1>
                    <p>Programs to keep you connected.</p>
                </div>
            </section>

            <!-- Content -->
            <section class="assistance-content">
                <div class="container">
                    <div class="content-block animate-on-scroll">
                        <h2>Keeping Our Community Connected</h2>
                        <p>At PEAK Internet, we believe that everyone deserves reliable access to high-speed internet.
                            We actively participate in programs designed to make broadband services more affordable for
                            eligible households.</p>

                        <div class="alert-box">
                            <h4><i class="ph ph-info"></i> Oregon Lifeline Program</h4>
                            <p>PEAK Internet is a participant in the Oregon Lifeline Program. Oregon Lifeline provides a
                                monthly discount of up to $19.95 on Broadband service for qualifying low-income
                                families. If you would like to inquire or apply to the Oregon Lifeline program, please
                                visit the <a href="https://www.oregon.gov/puc/pages/oregon-lifeline.aspx"
                                    target="_blank" style="text-decoration: underline; color: inherit;">Oregon Public
                                    Utility Commission’s Lifeline</a> website.</p>
                        </div>

                        <div class="alert-box"
                            style="background: rgba(107, 114, 128, 0.1); border-left-color: #6B7280;">
                            <h4 style="color: #4B5563;"><i class="ph ph-clock-counter-clockwise"></i> Affordable
                                Connectivity Program (ACP) Update</h4>
                            <p style="color: #374151;">The federal Affordable Connectivity Program has ended funding as
                                of early 2024. However, PEAK Internet continues to work with local agencies and
                                state-level subsidy programs like Oregon Lifeline.</p>
                        </div>

                        <h3>How to get help:</h3>
                        <div class="steps-container">
                            <div class="step">
                                <div class="step-number">1</div>
                                <div class="step-content">
                                    <h4>Contact Our Team</h4>
                                    <p>Call our support line at <strong>541-754-7325</strong> and speak with a
                                        representative about currently active state or local subsidies that apply to
                                        Benton, Lane, Linn, Lincoln, Polk, or Marion counties.</p>
                                </div>
                            </div>

                            <div class="step">
                                <div class="step-number">2</div>
                                <div class="step-content">
                                    <h4>Verify Eligibility</h4>
                                    <p>Our team will help you determine if you qualify based on your enrollment in
                                        qualifying assistance programs (like SNAP, Medicaid, or SSI) or based on
                                        household income guidelines.</p>
                                </div>
                            </div>

                            <div class="step">
                                <div class="step-number">3</div>
                                <div class="step-content">
                                    <h4>Apply Discount</h4>
                                    <p>Once your eligibility is verified, we will automatically apply the approved
                                        subsidy discount directly to your monthly PEAK Internet invoice.</p>
                                </div>
                            </div>
                        </div>

                        <div style="text-align: center; margin-top: 40px;">
                            <a href="<?php echo esc_url( home_url( \'/support\' ) ); ?>" class="btn btn-primary"
                                style="padding: 16px 32px; font-size: 1.125rem;">Contact Support Now</a>
                        </div>
                    </div>
                </div>
            </section>
        </main>
<?php
get_footer();
?>