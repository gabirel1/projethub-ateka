const http = require('http')
const express = require('express')
const fs = require('fs').promises;
var cors = require('cors')
const bodyParser = require('body-parser');

const app = express();
const portExpress = 3000;
const host = 'localhost'
const port = 80
app.use(cors())
app.use(bodyParser());

var autologin = "";

const requestListener = function (req, res) {
    fs.readFile("./index.html")
        .then(contents => {
            res.setHeader("Content-Type", "text/html");
            res.writeHead(200);
            res.end(contents);
        })
};

app.route('/autologin')
    .get((req, res) => {
        res.json({token: autologin});
    })
    .post((req, res) => {
        console.log(req.body);
        const token = req.body.token;
        console.log(token);
        autologin = token.slice(25);
        if (token == null) {
            res.status(202);
            res.send(false);
        } else {
            res.status(201);
            res.send(true);
        }
    });

app.listen(portExpress);

const server = http.createServer(requestListener);

server.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
});