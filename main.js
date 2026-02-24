document.addEventListener('DOMContentLoaded', () => {
    // Toggle Button Logic
    const btnResidential = document.getElementById('btn-residential');
    const btnBusiness = document.getElementById('btn-business');

    btnResidential.addEventListener('click', () => {
        btnResidential.classList.add('active');
        btnBusiness.classList.remove('active');
        // Logic to switch view to residential can go here
    });

    btnBusiness.addEventListener('click', () => {
        btnBusiness.classList.add('active');
        btnResidential.classList.remove('active');
        window.location.href = "https://www.peakinternet.com/business/";
    });

    // Smooth reveal for sections
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up-visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.animate-on-scroll').forEach(section => {
        section.classList.add('fade-in-up');
        observer.observe(section);
    });

});
