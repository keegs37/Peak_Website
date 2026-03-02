<?php
/* Template Name: Tech Home */
get_header();
?>
<main>

            <section class="page-header" style="background-color: var(--color-primary-dark); color: white; padding: 100px 0; text-align: center;">
                <div class="container">
                    <h1 style="font-size: 3.5rem; margin-bottom: 24px; color: white;">Tech Home Support</h1>
                    <p style="font-size: 1.25rem; max-width: 800px; margin: 0 auto; opacity: 0.9;">Discover more about Tech Home Support and how it can benefit you.</p>
                </div>
            </section>
            
            <section class="content-section" style="padding: 80px 0;">
                <div class="container" style="max-width: 800px;">
                    <h2 class="animate-on-scroll" style="color: var(--color-primary-dark); margin-bottom: 20px;">Tech Home Support Services</h2>
                    <p class="animate-on-scroll" style="color: var(--color-text-mute); line-height: 1.8; margin-bottom: 20px;">
                        A complete home technology service that makes it easy to set up, use, protect and enjoy your Internet-enabled devices anytime and anywhere. 
                    </p>
                    <p class="animate-on-scroll" style="color: var(--color-text-mute); line-height: 1.8; margin-bottom: 20px; transition-delay: 100ms;">
                        Say goodbye to the frustration of managing your connected household. Contact our 24/7 technical support hotline for hands-on, concierge assistance with troubleshooting devices, network security, and internet connectivity issues.
                    </p>
                    <a href="<?php echo esc_url( home_url( '/support' ) ); ?>" class="btn btn-outline dark mt-4 animate-on-scroll">Contact Tech Support</a>
                </div>
            </section>

</main>
<?php
get_footer();
?>