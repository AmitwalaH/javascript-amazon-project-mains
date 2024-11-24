const express = require("express");
const app = express();
const port = 3000;

app.use(express.json());
// express.json();

const loggingMiddleware = function (req, res, next) {
  console.log("Logging to site");
  next();
};
// app.use(loggingMiddleware);
const authMiddleware = function (req, res, next) {
  console.log("Auth to site");
  next();
};
// app.use(authMiddleware);
const validateMiddleware = function (req, res, next) {
  console.log("Validate to site");
  next();
};
// app.use(validateMiddleware);

const route = require('./routes')
//mounting the routes
app.use('/api',route)

app.get("/", (req, res) => {
  console.log(req.body);
  res.send("Hello World!");
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
