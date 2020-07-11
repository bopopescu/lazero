// ==UserScript==
// @name     Lazero Helper Script
// @version  1
// @grant    none
// ==/UserScript==

// everytime having a different value.
// create a cronjob then.
// or register a service.
//  so this time we only use clipboard, or something alike?
// what do you expect? on_clipboard_change?
// uuid can be used here.
// might be useful.
// some pages such as extension config are not accessiblt.
// but anyway, it is getting close to the truth.
// wait till fully loaded?
console.log("LAZERO HELPER SCRIPT\n    -\n   |               ___  __  __\n  / \\  |    /|  /  ___ |   |  |\n \\  _\\ |__ / | /__ ___ |   |__|\n\nTo make everything\nexecutable, analyzable, controllable.");
// back again. doing random stuff here.
// not too goddamn bad?
const copyToClipboard = str => {
    const el = document.createElement('textarea');  // Create a <textarea> element
    el.value = str;                                 // Set its value to the string that you want copied
    el.setAttribute('readonly', '');                // Make it readonly to be tamper-proof
    el.style.position = 'absolute';
    el.style.left = '-9999px';                      // Move outside the screen to make it invisible
    document.body.appendChild(el);                  // Append the <textarea> element to the HTML document
    const selected =
        document.getSelection().rangeCount > 0        // Check if there is any content selected previously
            ? document.getSelection().getRangeAt(0)     // Store selection if found
            : false;                                    // Mark as false to know no selection existed before
    el.select();                                    // Select the <textarea> content
    document.execCommand('copy');                   // Copy - only works as a result of a user action (e.g. click events)
    document.body.removeChild(el);                  // Remove the <textarea> element
    if (selected) {                                 // If a selection existed before copying
        document.getSelection().removeAllRanges();    // Unselect everything on the HTML document
        document.getSelection().addRange(selected);   // Restore the original selection
    }
};
const Http = new XMLHttpRequest();
const url = 'http://localhost:7000';
Http.open("GET", url);
Http.send();

// making it portable?
var uuid = null;
Http.onreadystatechange = (e) => {
    var xk = Http.responseText;
    if (xk) {
        console.log("Session UUID: " + xk);
        uuid = xk;

        var d = document.all;
        // is that string?
        // can we copy something else?
        // by encoding?
        // that is a function notation.
        // and this is not joking.
        // do you need to end the entire thing?
        // or refreshing the entire thing?

        // can we access the console?
        // can we do it?
        var ki = d.length;
        var json = [{"LAZERO_HELPER_PROGRAM":uuid}];
        for (var i = 0; i < ki; i++) {
            var p = d[i];
            var j = { "innerHtml": d[i].innerHTML, "outerHTML": d[i].outerHTML };
            json.push(j);
        }
        //d=JSON.stringify(d);
        copyToClipboard(JSON.stringify(json));

    }
}
// what is that anyway?
// if request failed?
// without network card?


// you can simply post the first one please???
// don't be silly.
// we shall also have access to the clipboard somehow.
// check notation?
// get uuid?