function initPoteriScripts() {
    const tables = document.querySelectorAll('.sortable');

    tables.forEach(table => {
        const headers = table.querySelectorAll('th');
        headers.forEach((header, index) => {
            header.style.cursor = 'pointer';
            header.addEventListener('click', () => sortTableByColumn(table, index));
        });
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

        table.querySelectorAll('th').forEach((th, idx) => {
            th.classList.remove('sorted-asc', 'sorted-desc');
            if (idx === columnIndex) {
                th.classList.add(direction === 'asc' ? 'sorted-asc' : 'sorted-desc');
            }
        });
    }

    // Search bar
    const searchInput = document.getElementById('table-search');
    if (searchInput) {
        searchInput.addEventListener('input', () => {
            const filter = searchInput.value.toLowerCase();
            tables.forEach(table => {
                const rows = table.tBodies[0].querySelectorAll('tr');
                rows.forEach(row => {
                    const text = row.innerText.toLowerCase();
                    row.style.display = text.includes(filter) ? '' : 'none';
                });
            });
        });
    }
}

// If opened directly as full page → run automatically
if (document.readyState !== 'loading') {
    initPoteriScripts();
} else {
    document.addEventListener('DOMContentLoaded', initPoteriScripts);
}