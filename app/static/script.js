
function getHistory(){
    return document.getElementById("history-value").innerText;
}

function printHistory(history) {
    document.getElementById("history-value").innerText = history;
}
function getOutput() {
    return document.getElementById("output-value").innerText;
}

function convertToNumber(numStr) {
    return Number(numStr);
}

function printOutput(output) {
    document.getElementById("output-value").innerText=output;
}

function httpGet(theUrl, expr)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "POST", theUrl, false ); // false for synchronous request
    xmlHttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    var data = 'expr=' + expr;
    xmlHttp.send(data);
    return xmlHttp.responseText;
}

var operator = document.getElementsByClassName("operator");

for(var i =0;i<operator.length;i++){
    operator[i].addEventListener('click',function() {
        var op = this.id;

        if(op == "=") {
            var history = getHistory() + getOutput();

            var url = "http://127.0.0.1:5000/calculate";
            var encodeData = window.btoa(history);
            var responseText = httpGet(url, encodeData);
            printHistory("");
            printOutput(responseText);
        }
        else if(op == "clear") {
           printOutput("");
           printHistory("");
        }
        else if(op == "backspace") {
            var output = getOutput();
            output = output.slice(0, -1);
            printOutput(output);
        }
        else{
            var history = getHistory() + getOutput() + op;
            printHistory(history);
            printOutput("");
        }
    });
}

var number = document.getElementsByClassName("number");

for(var i = 0; i < number.length; i++) {
    number[i].addEventListener('click', function(){
        var output  = getOutput();
        if (output != NaN){
            output = output + this.id;
            printOutput(output);
        }
    });
}