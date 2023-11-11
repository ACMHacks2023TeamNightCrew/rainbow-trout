document.getElementById("majorSelector").addEventListener("change", async(evt) => {
    let selector = document.getElementById("majorSelector");
    let major = selector.value;
    let majorRequirementsRes = await fetch(`/majorLists/${major}.json`);
    let majorRequirements = await majorRequirementsRes.json();

    let courseList = document.getElementById("completedCoursesList");
    courseList.innerHTML = "";

    for (let requirement of majorRequirements) {
        let requirementString = requirement;
        if (requirement.constructor === Array) {
            requirementString = requirement.join(" or ");
        }
        courseList.insertAdjacentHTML("beforeend", `
        <li>
            <input id="check-box-${requirementString}" type="checkbox" name="check-box-${requirementString}" class="form-check-input"/>
            <label for="check-box-${requirementString}" class="form-check-label">${requirementString}</label>
        </li>
        `)
    }
});