// AniRank - Main JS

// Animasi card saat masuk viewport
document.addEventListener('DOMContentLoaded', () => {
    // Lazy reveal cards
    const cards = document.querySelectorAll('.anime-card, .anime-card-h, .char-card');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, i) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, i * 40);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
        observer.observe(card);
    });

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        navbar.style.boxShadow = window.scrollY > 20
            ? '0 4px 30px rgba(0,0,0,0.4)'
            : 'none';
    });
});
