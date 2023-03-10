console.log("Loading...")
var time = 0.1;

let nIntervId;
var standEval = eval;

B_pause = document.getElementById("pause");
B_resume = document.getElementById("resume");
B_reset = document.getElementById("reset");
time_data = document.getElementById("time_data");
PortTable = document.getElementById("PortTable");

B_pause.addEventListener("click", pause_button);
B_reset.addEventListener("click", reset_button);
B_resume.addEventListener("click", resume_button);

var FirstPage;


var chart, allPort;

// DOM After
window.onload = function() {

    FirstPage = document.getElementById("FirstPage").innerText;
    time = parseFloat(document.getElementById("Rot").innerText) * 1000;
    console.log(FirstPage, time)
    if(FirstPage == "Start") {
        console.log("Hi2")
        DataRender();
    }
}

//Page Leave
window.onbeforeunload = function() {
    pauseData();
}

function DataRender() {

    // 大图渲染模板加载
    chart = echarts.init(document.getElementById('mix_line'), 'white', {
        renderer: 'canvas'
    });
    // 小图渲染模板加载
    ChildChart();
    // 总数记录
    allPort = PortNumber();
    Circulation();
}

function Circulation() {
    checkData();
    fetchData(chart);
//    if (time != parseFloat(document.getElementById("Rot").innerText) * 1000) {
//        time = parseFloat(document.getElementById("Rot").innerText) * 1000;
//    }
    for (var k = 0; k < allPort; k++) {
        fetchSingleData(k);
    };
}


function fetchData() {
    $.ajax({
        type: "GET",
        url: "/MixChart",
        dataType: 'json',
        success: function(result) {
            chart.setOption(result);
        }
    });
};

function resumeData() {
    $.ajax({
        type: "GET",
        url: "/resume",
        dataType: 'json',
        success: function(result) {}
    });
};

function pauseData() {
    $.ajax({
        type: "GET",
        url: "/pause",
        dataType: 'json',
        success: function(result) {}
    });
};

function resetData() {
    $.ajax({
        type: "GET",
        url: "/reset",
        dataType: 'json',
        success: function(result) {}
    });
};

function reset_button() {

    clearInterval(nIntervId);
    nIntervId = null;
    resetData();

    location.reload();
};

function pause_button() {
    B_resume.classList.remove('hidden-button');
    B_pause.classList.add('hidden-button');

    pauseData();

    clearInterval(nIntervId);
    nIntervId = null;
};

function resume_button() {
    if(FirstPage != "Start") {
        DataRender();
    } else {
        clearInterval(nIntervId);
        nIntervId = null;
    }
    B_resume.classList.add('hidden-button');
    B_pause.classList.remove('hidden-button');
    resumeData();
    Circulation();
    if (!nIntervId) {

        nIntervId = setInterval(Circulation, time);
    }
};


function checkData() {
    $.ajax({
        url: "/data",
        type: 'get',
        timeout: 1000,
        success: function(data) {
            var infos = JSON.parse(data);
            var content = '';

            for (var i in infos) {

                if (i == "Time") {

                } else {
                    var content = content + '<tr>\
                    <td class="text-dark text-semibold">' + i + '</td>\
                    <td class="text-dark text-semibold">' + infos[i] + '</td>\
                </tr>';
                };
            }

            time_data.innerText = infos["Time"];
            PortTable.innerHTML = content;
        }
    });
}

function PortNumber() {
    var result;
    $.ajax({
        url: "/portNum",
        type: 'get',
        timeout: 1000,
        async: false,
        success: function(data) {
            // console.log(data)
            result = data;
        },
        error: function() {
            result = 0;
        }
    });
    return result;
}

function ChildChart() {
    // 用于生成子图
    // 1.生成每个子图的变量，并绑定id
    // 2.根据id完善div
    // 3.div渲染图表，ajax传参更新画面

    var Port_num = PortNumber();

    for (var i = 0; i < Port_num; i++) {
        var chartname = "chart" + i;
        var chartid = "Cline" + i;
        standEval(`var ${chartname}= echarts.init(document.getElementById('${chartid}'), 'white', {renderer: 'canvas'});`)
    }
}

function fetchSingleData(number) {
    var chartName = "chart" + number;
    $.ajax({
        url: "/fetch/" + number,
        type: 'get',
        timeout: 1000,
        success: function(result) {
            standEval(`${chartName}.setOption(${result});`);
        }
    });
}

function CloseSend() {
    console.log("stop");
    pause_button();
}