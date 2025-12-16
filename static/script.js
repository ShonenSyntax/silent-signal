// Wait until the page is fully loaded
document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("reportForm");
    const textarea = document.getElementById("reportInput");
    const button = form.querySelector("button");

    form.addEventListener("submit", function (event) {

        //Prevent empty submissions
        if (textarea.value.trim() === "") {
            event.preventDefault(); // stops form submission
            alert("Please describe the issue before submitting.");
            return;
        }

        //Disable button to avoid double submit
        button.disabled = true;
        button.innerText = "Submitting...";
    });

});