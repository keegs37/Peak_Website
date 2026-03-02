<?php
/* Template Name: News */
get_header();
?>
<main>
            <!-- Page Header -->
            <section class="page-header">
                <div class="container">
                    <h1>PEAK News</h1>
                    <p>Updates, community events, and network enhancements.</p>
                </div>
            </section>

            <!-- News Grid -->
            <section class="news-section">
                <div class="container">
                    <div class="news-grid">

                        <!-- Article 1 -->
                        <article class="news-card animate-on-scroll">
                            <div class="news-image"
                                style="background-color: #2F3C7E; background-image: url('assets/fiber.png'); background-blend-mode: multiply;">
                                <div class="news-category">Case Study</div>
                                <i class="ph ph-laptop"></i>
                            </div>
                            <div class="news-content">
                                <h3 class="news-title">Making Remote Learning Possible in Rural Oregon</h3>
                                <p class="news-excerpt">The pandemic served as a perfect acid test for connectivity
                                    around the world... In the Mid-Willamette Valley area in Oregon, the decades-old,
                                    substandard home Internet infrastructure stood out in stark relief very quickly.</p>
                                <a href="https://www.peakinternet.com/devpk/wp-content/uploads/2023/01/Zayo-Case-Study-PEAK-Internet.pdf"
                                    target="_blank" class="news-link">Read Full Case Study <i
                                        class="ph ph-arrow-right"></i></a>
                            </div>
                        </article>

                        <!-- Article 2 -->
                        <article class="news-card animate-on-scroll" style="transition-delay: 100ms;">
                            <div class="news-image" style="background-color: #10B981;">
                                <div class="news-category">Expansion</div>
                                <i class="ph ph-globe-hemisphere-west"></i>
                            </div>
                            <div class="news-content">
                                <div class="news-date"><i class="ph ph-calendar-blank"></i> Dec 13, 2022</div>
                                <h3 class="news-title">PEAK Internet to install fiber optic lines in Lebanon</h3>
                                <p class="news-excerpt">Linn County Commissioners approved a tax-exempt bond program
                                    that will help PEAK Internet run more than 101 miles of high-speed fiber optic lines
                                    in the city of Lebanon, greatly increasing Internet speed opportunities for homes
                                    and businesses alike.</p>
                                <a href="#" class="news-link">Read Full Article <i class="ph ph-arrow-right"></i></a>
                            </div>
                        </article>

                        <!-- Article 3 -->
                        <article class="news-card animate-on-scroll" style="transition-delay: 200ms;">
                            <div class="news-image" style="background-color: #3B82F6;">
                                <div class="news-category">News</div>
                                <i class="ph ph-newspaper"></i>
                            </div>
                            <div class="news-content">
                                <div class="news-date"><i class="ph ph-calendar-blank"></i> Nov 23, 2022</div>
                                <h3 class="news-title">Fiber Internet coming to Lebanon households</h3>
                                <p class="news-excerpt">Lebanon will be first in the mid-Willamette Valley to get
                                    enterprise-level fiber-optic internet to every home in city limits. The city signed
                                    an agreement Nov. 9 with Corvallis-based PEAK Internet that will allow the company
                                    to start covering Lebanon in fiber lines in 2023.</p>
                                <a href="<?php echo esc_url( home_url( \'/https://democratherald.com/business/technology/fiber-internet-coming-to-lebanon-households/article_b0038e7a-6788-11ed-be0a-2ba0bfac0f6a\' ) ); ?>"
                                    target="_blank" class="news-link">Read full article at DemocratHerald.com <i
                                        class="ph ph-arrow-right"></i></a>
                            </div>
                        </article>

                    </div>

                    <!-- Pagination -->
                    <div class="pagination animate-on-scroll" style="transition-delay: 300ms;">
                        <button class="page-btn"><i class="ph ph-caret-left"></i></button>
                        <button class="page-btn active">1</button>
                        <button class="page-btn">2</button>
                        <button class="page-btn">3</button>
                        <button class="page-btn"><i class="ph ph-caret-right"></i></button>
                    </div>
                </div>
            </section>
        </main>
<?php
get_footer();
?>