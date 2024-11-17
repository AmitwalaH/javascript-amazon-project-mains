const express = require("express");
const app = express();

const port = 9100;

const item = require("./routes/dummy");

app.use("/api", item);

// app.get("/", (req, res) => {
//   console.log("We Got a New Request!!");
//   res.send("We got ur response, Stay tuned!!!");
// });

// app.get("/ssend", (req, res) => {
//   res.sendFile("./index.html", {
//     root:__dirname
//   });
// });
// app.get("/", (req, res) => {
//   console.log("We Got a New Request!!");
//   res.json("We got ur response, Stay tuned!!!");
// });

app.listen(port, () => {
  console.log("Listening ot Port No, 9100");
});
