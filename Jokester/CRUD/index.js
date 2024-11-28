const express = require("express");
const { v4: uuid } = require("uuid");
const path = require("path");
const methodOverride = require("method-override");
const app = express();
uuid();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(methodOverride("_method"));
app.set("views", __dirname);
app.set("view engine", "ejs");

let comments = [
  {
    id: uuid(),
    username: "phil_dunphy",
    comment: "I’m the cool dad, that’s my thing!",
  },
  {
    id: uuid(),
    username: "claire_dunphy",
    comment: "Why can’t anyone just follow my system?",
  },
  {
    id: uuid(),
    username: "jay_pritchett",
    comment: "I built a business with my bare hands, so don’t lecture me!",
  },
  {
    id: uuid(),
    username: "gloria_pritchett",
    comment: "I love my family, even if they drive me crazy sometimes!",
  },
  {
    id: uuid(),
    username: "mitchell_pritchett",
    comment: "Parenting is hard, but it’s worth every moment.",
  },
  {
    id: uuid(),
    username: "cameron_tucker",
    comment: "I bring the drama, and I’m proud of it!",
  },
  {
    id: uuid(),
    username: "haley_dunphy",
    comment: "Shopping is my cardio, and no one can change my mind.",
  },
  {
    id: uuid(),
    username: "alex_dunphy",
    comment: "Books are better company than most people.",
  },
  {
    id: uuid(),
    username: "luke_dunphy",
    comment: "Why think before doing when you can just do?",
  },
  {
    id: uuid(),
    username: "manny_delgado",
    comment: "Life is poetry, and I live it one stanza at a time.",
  },
];

app.get("/comments", (req, res) => {
  res.render("comment", { comments });
});

app.get("/comments/new", (req, res) => {
  res.render("new");
});

app.post("/comments", (req, res) => {
  const { username, comment } = req.body;
  comments.push({ username, comment, id: uuid() });
  res.redirect("/comments");
});

app.get("/comments/:id", (req, res) => {
  const { id } = req.params;
  const comment = comments.find((c) => c.id === id);
  res.render("show", { comment });
});

app.get("/comments/:id/edit", (req, res) => {
  const { id } = req.params;
  const comment = comments.find((c) => c.id === id);
  res.render("edit", { comment });
});

app.patch("/comments/:id", (req, res) => {
  const { id } = req.params;
  const newCommentText = req.body.comment;
  const foundComment = comments.find((c) => c.id === id);
  foundComment.comment = newCommentText;
  res.redirect("/comments");
});

app.delete("/comments/:id", (req, res) => {
  const { id } = req.params;
  comments = comments.filter((c) => c.id !== id);
  res.redirect("/comments");
});

app.listen(9100, () => {
  console.log("Listening on Port No. 9100");
});
