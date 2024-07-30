const boxes = document.querySelectorAll(".play")

const rst = document.querySelector("#reset")

let win = document.querySelector('.dot');

let newbtn = document.querySelector("#ngame")

let count = 0;

const winPatterns = [
    [0, 1, 2],
    [0, 3, 6],
    [0, 4, 8],
    [1, 4, 7],
    [2, 5, 8],
    [2, 4, 6],
    [3, 4, 5],
    [6, 7, 8],
  ];

let turno = true;

const draw = () => {
        win.innerText = "Draw!, start new game.."
        disabledbtn();
}

const reset = () => {
    turno = true;
    enabledbtn();
    win.innerText = "TIC TAC TOE!";
    count = 0;
}

boxes.forEach((box) => {
    box.addEventListener("click", () => {
        if (turno) {
            box.innerText = "O";
            turno = false;
            count++;
        }
        else{
            box.innerText = "X";
            turno = true;
            count++;
        }
        box.disabled = true;
        let isWinner = checkWinner();

        if(count === 9 && !isWinner){
            draw();
        }
        
        checkWinner();
    });
});

const disabledbtn = () => {
    for (let box of boxes) {
        box.disabled = true;
    }
}

const enabledbtn = () => {
    for (let box of boxes) {
        box.disabled = false;
        box.innerText = " ";
    }
}

const showWinner = (winner) => {
    win.innerText = `Congrulation, Winner is ${winner}`;
    disabledbtn();
    // reset();
}

const checkWinner = () => {
    for (let pattern of winPatterns) {
      let pos1Val = boxes[pattern[0]].innerText;
      let pos2Val = boxes[pattern[1]].innerText;
      let pos3Val = boxes[pattern[2]].innerText;
  
      if (pos1Val != "" && pos2Val != "" && pos3Val != "") {
        if (pos1Val === pos2Val && pos2Val === pos3Val) {
          showWinner(pos1Val);
          return true;
        }
      }
    }
  };

ngame.addEventListener('click',reset);
rst.addEventListener('click' ,reset)

console.log(count);