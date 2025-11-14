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

function smoothScrollWithOffset(target) {
    const element = document.querySelector(target);
    if (!element) return;

    // Find any sticky element (header, nav, toolbar...)
    const sticky = document.querySelector('[data-sticky], header, nav');
    const offset = sticky ? sticky.offsetHeight : 0;

    const targetPosition = element.getBoundingClientRect().top + window.pageYOffset;
    const scrollPosition = targetPosition - offset;

    window.scrollTo({
        top: scrollPosition,
        behavior: 'smooth'
    });
}

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const hash = this.getAttribute('href');
        if (hash.length > 1) {
            e.preventDefault();
            smoothScrollWithOffset(hash);
        }
    });
});

// --- Shared function to make a table sortable ---
function makeTableSortable(table) {
    const headers = table.querySelectorAll('th');
    headers.forEach((header, index) => {
        header.style.cursor = 'pointer';
        header.addEventListener('click', () => sortTableByColumn(table, index));
    });

    function sortTableByColumn(table, columnIndex) {
        const tbody = table.tBodies[0];
        const rows = Array.from(tbody.querySelectorAll('tr'));
        const isNumeric = rows.every(row => !isNaN(row.cells[columnIndex].innerText.trim()));

        const currentIsAscending = table.dataset.sortCol == columnIndex && table.dataset.sortDir === 'asc';
        const direction = currentIsAscending ? 'desc' : 'asc';

        rows.sort((a, b) => {
            let aText = a.cells[columnIndex].innerText.trim();
            let bText = b.cells[columnIndex].innerText.trim();

            if (isNumeric) {
                return direction === 'asc' ? aText - bText : bText - aText;
            } else {
                return direction === 'asc' ? aText.localeCompare(bText) : bText.localeCompare(aText);
            }
        });

        rows.forEach(row => tbody.appendChild(row));

        table.dataset.sortCol = columnIndex;
        table.dataset.sortDir = direction;

        // Update header classes for arrow indicator
        table.querySelectorAll('th').forEach((th, idx) => {
            th.classList.remove('sorted-asc', 'sorted-desc');
            if (idx === columnIndex) {
                th.classList.add(direction === 'asc' ? 'sorted-asc' : 'sorted-desc');
            }
        });
    }
}

// --- Shared function to initialize the Poteri della Forza page ---
function initPoteriDellaForza() {
    const table = document.querySelector('#tabella-poteri');
    if (table) {
        makeTableSortable(table);
    }

    const searchInput = document.getElementById('table-search');
    if (searchInput && table) {
        searchInput.addEventListener('input', () => {
            const filter = searchInput.value.toLowerCase();
            const rows = table.tBodies[0].querySelectorAll('tr');
            rows.forEach(row => {
                const text = row.innerText.toLowerCase();
                row.style.display = text.includes(filter) ? '' : 'none';
            });
        });
    }
}


