// Back-to-top button
const backToTop = document.getElementById('back-to-top');
window.addEventListener('scroll', () => {
    if (window.scrollY > 200) backToTop.classList.add('show');
    else backToTop.classList.remove('show');
});
backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Smooth scroll for internal links accounting for sticky header
document.querySelectorAll('main a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const targetId = this.getAttribute('href').substring(1);
        const targetEl = document.getElementById(targetId);
        const headerOffset = document.querySelector('header').offsetHeight + 8;
        if (targetEl) {
            e.preventDefault();
            const elementPosition = targetEl.getBoundingClientRect().top + window.pageYOffset;
            const offsetPosition = elementPosition - headerOffset;
            window.scrollTo({ top: offsetPosition, behavior: 'smooth' });
        }
    });
});

// === HOME BUTTON ===
const homeButton = document.getElementById('home-button');

// Scroll behavior for home button
window.addEventListener('scroll', () => {
    if (window.scrollY > 200) homeButton.classList.add('show');
    else homeButton.classList.remove('show');
});

// Click behavior for home button
homeButton.addEventListener('click', () => {
    const isGitHub = window.location.hostname.includes('github.io');
    const repoPrefix = isGitHub ? '/' + window.location.pathname.split('/')[1] + '/' : '/';
    window.location.href = repoPrefix + 'index.html';
});
