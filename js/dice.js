document.addEventListener("DOMContentLoaded", function() {
    var randomNumber1 = Math.floor(Math.random() * 6) + 1; // Generates random number between 1 and 6
    var randomDiceImage = "dice" + randomNumber1 + ".png"; // Generates string like "dice1.png" to "dice6.png"
    var randomImageSource = "images/" + randomDiceImage; // Generates full path like "images/dice1.png" to "images/dice6.png"

    var image1 = document.querySelectorAll("img")[0];
    if (image1) { // Check if image1 is defined
        image1.setAttribute("src", randomImageSource); // Sets the src attribute of the first <img> element
    }

    var randomNumber2 = Math.floor(Math.random() * 6) + 1;
    var randomImageSource2 = "images/dice" + randomNumber2 + ".png";
    
    var image2 = document.querySelectorAll("img")[1];
    if (image2) { // Check if image2 is defined
        image2.setAttribute("src", randomImageSource2); // Sets the src attribute of the second <img> element
    }

    var resultText = document.querySelector("h1");
    if (resultText) { // Check if h1 element is defined
        // Determine winner
        if (randomNumber1 > randomNumber2) {
            resultText.innerHTML = "🚩 Player 1 Wins!";
        } else if (randomNumber2 > randomNumber1) {
            resultText.innerHTML = "Player 2 Wins! 🚩";
        } else {
            resultText.innerHTML = "Draw!";
        }
    }
});
