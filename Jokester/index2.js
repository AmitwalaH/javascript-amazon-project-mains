const express = require("express");
const app = express();
const port = 8100;

app.get("/", (req, res) => {
  res.send("Got The Blessing from GOD!!");
});

app.listen(port, () => {
  console.log(`Listening ot Port No, ${port}`);
});
