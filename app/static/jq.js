
// using jquery to operate the DOM and deal with http.
function getHistory(){
    return $("#history-value").text();
}

function printHistory(history) {
     $("#history-value").text(history)
}
function getOutput() {
    return $("#output-value").text();
}

function convertToNumber(numStr) {
    return Number(numStr);
}

function printOutput(output) {
    $("#output-value").text(output);
}

$(".operator").each(
    function(index, e) {
        $(this).click(
            function() {
                var op = this.id;
                if(op == "=") {
                    var history = getHistory() + getOutput();

                    var url = "http://127.0.0.1:5000/calculate";
                    var encodeData = window.btoa(history);
                    $.post(
                        url,
                        {expr:encodeData},
                        function (data, status){
                            printHistory("");
                            printOutput(data);
                        }
                    )
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
            }
        );
    }
);

$(".number").each(
    function(index, e) {
        $(this).click( function(){
            var output  = getOutput();
            if (output != NaN){
                output = output + this.id;
                printOutput(output);
            }
        });
    }
);

