const searchInput = document.getElementById("searchInput");

if (searchInput) {


searchInput.addEventListener("keyup", function () {

    const filter = this.value.toLowerCase();

    const rows = document.querySelectorAll("#patientsTable tbody tr");

    rows.forEach(row => {

        const text = row.innerText.toLowerCase();

        row.style.display = text.includes(filter) ? "" : "none";

    });

});
}