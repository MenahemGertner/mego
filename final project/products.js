const express = require("express");
const router = express.Router();

router.post("/", (req, res) => {
  res.send("Create Product");
});

router.get("/new", (req, res) => {
  res.send("Get Product");
});

module.exports = router;
