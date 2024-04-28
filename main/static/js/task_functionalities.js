function addTask() {
    const newTask = document.createElement("div");
    newTask.classList.add("task-div")

    const newForm = document.createElement("form");
    newForm.method = "post";

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.classList.add("task-complete");
    checkbox.setAttribute("id", "task-1");
    checkbox.alt = "Task Done";
    checkbox.name = "task_done";

    const newLabel = document.createElement("label");
    newLabel.setAttribute("for", "task-1");
    newLabel.classList.add("checkbox-label");

    newForm.appendChild(checkbox);
    newForm.appendChild(newLabel);

    newTask.appendChild(newForm);

    const taskCollection = document.getElementById("task-collection");
    taskCollection.appendChild(newTask);
}