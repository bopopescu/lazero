// #!/usr/bin/nodejs
// undefined
// var 
var http=require('http');
// var crypto = require('crypto');
// the heck.
// it would be hard if browsing the fucking thing.
// i mean PDF.
// and still don't know how to get it right.
// but we can do this, by remote access.
// the shell! yeah!
// var crypto = require('crypto'); 
// return it via web or clipboard.
// whatever.
var demo="f7775beb-0059-45e3-9ca9-53f67e075fe7";
// you can set the command, without using mouse at all.
// without taking risk there's no meaning at all.
var server = http.createServer((function (request, response) {// never read the request?
    response.writeHead(200,
        { "Content-Type": "text/plain" });
    // var k = uuidv4();
    var k = {"uuid":demo,"command":"document.all"};
    // you should invoke another program.
    // better print it out.
    // or put it into the clipboard.
    // maybe? maybe not.
    response.end(JSON.stringify(k));
    // JSON.parse(k);
    // get it parsed, or report error.
}));
server.listen(7001);