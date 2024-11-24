const express = require("express");
const router = express.Router();

//middleware

const authMiddleware = function (req, res, next) {
  console.log("Auth to site");

  req.user = { userId: 1, role: "student" };

  if (req.user) {
    next();
  } else {
    res.json({
      success: false,
      message: "Not a valid User",
    });
  }
};

const isStudentMiddleware = function (req, res, next) {
  console.log("Inside Student Middleware");

  if (req.user.role === "student") {
    next();
  } else {
    res.json({
      success: false,
      message: "Access Denied , Only for Students",
    });
  }
};

const isAdminMiddleware = function (req, res, next) {
  console.log("Inside Admin Middleware");

  if (req.user.role === "admin") {
    next();
  } else {
    res.json({
      success: false,
      message: "Access Denied , Only for Admins",
    });
  }
};

//routes

router.get("/student", authMiddleware, isStudentMiddleware, (req, res) => {
  console.log("Inside Student route");
  res.send("Student Portal");
});

router.get("/admin", authMiddleware, isAdminMiddleware, (req, res) => {
  console.log("Inside Admin route");
  res.send("Admin Portal");
});

module.exports = router;
