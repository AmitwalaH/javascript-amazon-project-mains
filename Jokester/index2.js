const express = require("express");
const app = express();
const port = 8100;

app.set('views engine','ejs')

app.get("/", (req, res) => {
  res.render("home.ejs");
});

app.listen(port, () => {
  console.log(`Listening ot Port No, ${port}`);
});
