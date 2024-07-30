// let maximum = parseInt(prompt("Enter the maximum number"))
// while (!maximum) {
//     maximum = parseInt(prompt("Enter the valid number"))
// }

// const targetNum = Math.floor(Math.random() * maximum) + 1;
// console.log(targetNum);
// let guess = parseInt(prompt("Enter your first guess"));
// let attempt = 1;

// while (guess !== targetNum) {
//     attempt++;
//     if (guess > targetNum) {
//        guess = parseInt(prompt("Too High! Enter a new guess"))
//     }else{
//         guess = parseInt(prompt("Too Low! Enter a new guess"))
//     }
// }

// console.log(`You Got It! , After ${attempt} attempts`);

const locate = {
    locs0 : [1,"Mumbai"],
    locs1 : [2,"Mahuva"],
    locs2 : [3,"Surat"],
    locs3 : [4,"Kerala"],
};

for (const iterat in locate) {
    console.log(locate[iterat]);
}