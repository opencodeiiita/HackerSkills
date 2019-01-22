const express = require("express");
const request = require("request");
const bodyParser = require("body-parser");
const DOMParser = require("dom-parser");
const striptags = require("striptags");

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.set("view engine", "ejs");

var data = null;

app.get("/", (req, res) => {
    res.render("search.ejs");
});

app.post("/jobs", (req, res) => {
    var loc = req.body.loc;
    var desc = req.body.desc;
    var url =
        "https://jobs.github.com/positions.json?description=" +
        desc +
        "&location=" +
        loc;

    request(url, (err, response, body) => {
        if (err) {
            console.log(err);
        } else {
            var parsedata = JSON.parse(body);
            data = parsedata;
            res.redirect("/jobs");
        }
    });
});

var array = [];
app.get("/jobs", (req, res) => {
    // var value = "";
    data.forEach(function(dt) {
        dt["description"] = striptags(dt["description"]);
    });

    res.render("result.ejs", { data: data });
});

app.listen(5000);
