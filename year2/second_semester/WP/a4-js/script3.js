function sortTable(colIndex) {
    const table = document.getElementById("my-table");
    const tbody = table.tBodies[0];
    const rows = Array.from(tbody.rows);
    const isAscending = table.getAttribute(`data-sort-${colIndex}`) === "asc";

    // Sort rows based on the values in the column
    rows.sort((rowA, rowB) => {
        const valueA = rowA.cells[colIndex].textContent;
        const valueB = rowB.cells[colIndex].textContent;
        return valueA.localeCompare(valueB);
    });

    // Reverse the order if we were already sorted in ascending order
    if (isAscending) {
        rows.reverse();
        table.setAttribute(`data-sort-${colIndex}`, "desc");
    } else {
        table.setAttribute(`data-sort-${colIndex}`, "asc");
    }

    // Reattach the sorted rows to the table
    tbody.innerHTML = "";
    for (const row of rows) {
        tbody.appendChild(row);
    }
}