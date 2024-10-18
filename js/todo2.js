const toListNames = [];

function addTheName() {
  let listName = document.querySelector(".js-list-name");
  let listDate = document.querySelector(".js-list-date");
  let dispName = document.querySelector(".js-add-name");
  const names = listName.value;
  const dates = listDate.value;

  if (names.trim() !== "") {
    toListNames.push({
      name: names,
      dueDate: dates,
    }); // Add the new name to the list if not empty
  }

  let allListNames = "";

  toListNames.forEach(function (todoObj, index) {
    // const todoObj = toListNames[i];
    // const namesL = todoObj.name;
    // const datesL = todoObj.dueDate;
    const { name, dueDate } = todoObj; //Destructing
    let listTo = `<p>
      ${name} ${dueDate}
      <button onclick="deleteName(${index})">Delete</button>
    </p>`;
    allListNames += listTo;
  });

  dispName.innerHTML = allListNames;
  listName.value = ""; // Clear the input field after adding a name
}

function deleteName(index) {
  toListNames.splice(index, 1); // Remove the name at the given index
  addTheName(); // Refresh the list
}
