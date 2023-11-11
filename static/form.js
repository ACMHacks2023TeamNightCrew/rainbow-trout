let showCourseModal = new bootstrap.Modal(document.getElementById("courseInfoModal"), {
    keyboard: true,
    backdrop: true
});

const generateCourseCheckbox = function(courseId) {
    let li = document.createElement("li");
    let input = document.createElement("input");
    let label = document.createElement("label");

    li.appendChild(input);
    li.appendChild(label);

    input.setAttribute("id", `check-box-${courseId}`);
    input.setAttribute("type", `checkbox`);
    input.setAttribute("name", `check-box-${courseId}`);
    input.setAttribute("class", "form-check-input");

    label.setAttribute("for", `check-box-${courseId}`);
    label.setAttribute("class", "form-check-label clickable");
    label.innerHTML = "&nbsp" + courseId;

    label.addEventListener("click", (evt) => {
        showCourseModal.show();
        evt.preventDefault();
    });

    return li;
}


document.getElementById("majorSelector").addEventListener("change", async(evt) => {
    let selector = document.getElementById("majorSelector");
    let major = selector.value;

    if (major !== "Computer Science B.S.") {
        alert(`Sorry, only the Computer Science B.S. major is currently supported`);
        return;
    }

    document.querySelectorAll(".hide-if-not-cs").forEach((el) => el.classList.remove("d-none"))
});