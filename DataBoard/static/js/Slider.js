var TimeRotate = document.getElementById('TimeRotate');
var Xline = document.getElementById('Xline');

+

function($, window) {

    var start_Rotate = document.getElementById("Rot").innerText
    var start_Xli = document.getElementById("Xli").innerText
    noUiSlider.create(TimeRotate, {
        start: start_Rotate,
        connect: "lower",
        step: 0.1,
        range: {
            'min': 0.1,
            'max': 10
        }
    });

    noUiSlider.create(Xline, {
        start: start_Xli,
        connect: "lower",
        step: 1,
        range: {
            'min': 5,
            'max': 100
        }
    });
    var sliders = {};
    sliders.init = function() {};
    window.sliders = sliders;
}(jQuery, window);
// initialize app

+

function($) {
    sliders.init();
}(jQuery);


ChangeTimeRotate();
ChangeXline();

function getElementByXpath(xpath) {
    var element = document.evaluate(xpath, document).iterateNext();
    return element;
}

function ChangeTimeRotate() {
    var TimeRotate = getElementByXpath('//div[@id="TimeRotate"]/div//div[@role="slider"]').ariaValueText
    document.getElementById("Rotate").innerText = TimeRotate;
}

function ChangeXline() {
    var Xline = getElementByXpath('//div[@id="Xline"]/div//div[@role="slider"]').ariaValueText;
    document.getElementById("line").innerText = Xline;
}

function SendTimeRotate() {
    var TimeRotate = getElementByXpath('//div[@id="TimeRotate"]/div//div[@role="slider"]').ariaValueText
//    document.getElementById("Rot").innerText = TimeRotate;
    document.getElementById("resume").disabled = "True";
    document.getElementById("pause").disabled = "True";
    PostData("Rotate", TimeRotate)
}

function SendXline() {
    var Xline = getElementByXpath('//div[@id="Xline"]/div//div[@role="slider"]').ariaValueText

    PostData("show_Data", Xline)
}


function PostData(ChangeKey, ChangeValue) {
    var PD = {
        [ChangeKey]: ChangeValue,
    };
    $.ajax({
        type: "POST",
        url: "/conf",
        data: JSON.stringify(PD),
        contentType: 'application/json',
        success: function(data) {},
    });
}

function SaveText() {
    var TextMsg = document.getElementById("SaveText").value;
    document.getElementById("InforText").innerText = TextMsg;
    PostData("InforText", TextMsg)
}

