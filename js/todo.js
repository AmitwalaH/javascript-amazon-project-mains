let todo = (prompt(`What would you like to do?`))

let n = "new";
let l = "list";
let d = "delete";
let q = "quit";

let newTodo = []

while (todo !== q) {
    if (todo === n) {
        let newitem = prompt("Add a new list to Todo")
        newTodo.push(newitem)
    }
    else if(todo === l){
        console.log("Here is your to-do list:");
        for(let i = 0; i < newTodo.length; i++){
            console.log(`${i}: ${newTodo[i]}`)
        }
    }
    else if(todo === d){
        let deleteIndex = prompt("Enter the index number")
        if (!isNaN(deleteIndex) && deleteIndex >= 0 && deleteIndex < newTodo.length) {
            newTodo.splice(deleteIndex, 1);
            console.log("Item deleted successfully.");
        }
    }
        todo = (prompt(`What would you like to do?`))
}

console.log("Quitting the to-do list app. Goodbye!");
