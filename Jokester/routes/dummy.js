const express = require("express");
const router = express.Router();

router.get("/", (req,res) => {
  res.send('GET Response!!')
});
router.post("/items", (req,res) => {
    res.json({x:1,y:2,z:3})
});
router.put("/items/:id", (req,res) => {
    res.send('PUT Response!!')
});
router.delete("/items/:id", (req,res) => {
    res.send('DELETE Response!!')
});

module.exports = router;