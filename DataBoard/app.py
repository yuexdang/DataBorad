from flask import Flask, render_template, request, abort
from flask_apscheduler import APScheduler
from json import dumps

from PortGet import DataPush
from GlobalEdit.CSVGet import CsvReader
from GlobalEdit.JsGene import DataSelect, Get_Mix, Get_Single
from GlobalEdit.InitOpts import ConfObject

# Offline Env Func
# from Test.FackData import PortWrite_Fack, TimeClean

# Object Variable
conf_path = "./conf.ini"
Conf = ConfObject(conf_path)
scheduler = APScheduler()
DT = DataPush.InitPort

# Temporary Global Variable
Time_now = float(Conf.FileDic["Rotate"])
reset_sign = False
Data_per = {}
Temp_Data = {"Time": []}
FirstPage = ""

# 计时异步任务，用于持续读取数据
@scheduler.task('interval', id='GetPort', seconds=float(Conf.FileDic["Rotate"]), misfire_grace_time=3600)
def date_flush():
    global Time_now, Temp_Data, reset_sign, Data_per

    # Product Env
    Data_per = DataPush.PortWrite(DT, Conf.FileDic["Filename"].replace("^", " "), isSave=Conf.FileDic["isSave"], PortTime=Time_now, FileURL=Conf.FileDic["FileURL"].replace("^", " "))
    # print(Data_per)
    Temp_Data = DataSelect(Data_per, int(float(Conf.FileDic["show_Data"])))
    # print(Temp_Data)

    # # Offline Env
    # Data_per = PortWrite_Fack(1,1,1)
    # Temp_Data= DataSelect(Data_per,30)

    if reset_sign:
        Time_now = float(Conf.FileDic["Rotate"])
        Temp_Data = {"Time": []}
        reset_sign = False
        print("已重置")

    Time_now = round(Time_now + float(Conf.FileDic["Rotate"]), 1)
    return None

app = Flask(__name__, static_folder="static")


# 图图
@app.route("/")
def GetPlot():
    SonDatas = []
    for num, data in enumerate(DT):
        SonDatas.append([num, data.PortName()])
        # print(SonDatas)
    return render_template("DataPlot.html",
                           InforText=Conf.FileDic['InforText'],
                           Time=Time_now,
                           SonDatas=SonDatas,
                           FirstPage=FirstPage,
                           showData=int(float(Conf.FileDic["show_Data"])),
                           Rotate=Conf.FileDic["Rotate"],
                           )

# 获得当前数据
@app.route("/data")
def D_Get():
    infos = Data_per
    return dumps(infos)

# 端口总数
@app.route("/portNum")
def portNum():
    # Offline Env
    # return dumps(FackData.send)

    # Product Env
    return dumps(len(DT))

# 大图数据更新
@app.route("/MixChart")
def get_bar_chart():
    c = Get_Mix(Temp_Data)
    return c.dump_options_with_quotes()

# 小图数据更新
@app.route("/fetch/<int:Did>")
def single_Data(Did):
    # print(Temp_Data, Did+1, len(DT))
    try:
        d = Get_Single(Temp_Data, Did+1, len(DT))
        return d.dump_options_with_quotes()
    except:
        abort(500)
        return


# 仅获取一次数据，调试用
@app.route("/GetData")
def DataShow():
    """
    查看当前电阻值
    """
    try:
        print(Conf.FileDic)
        text = "T={}时的电阻:".format(Data_per['Time'])
        for num, data in enumerate(Data_per):
            if data == 'Time':
                pass
            else:
                text += "\n R{} = {}Ω &nbsp\n".format(num, Data_per[data])
        return text
    except:
        return "当前时间：{}请检查硬件设备链接或打开记录器".format(Time_now)

# 恢复数据读取
@app.route("/resume")
def ResumeTask():
    global FirstPage

    scheduler.resume_job("GetPort")

    FirstPage = "Start"
    text = "已恢复任务，当前时间：{}".format(Time_now)
    return text

# 暂停数据读取
@app.route("/pause")
def PauseTask():
    scheduler.pause_job("GetPort")

    text = "已暂停任务，当前时间：{}".format(Time_now)
    return text

# 数据重启
@app.route("/reset")
def ResetMode():
    global reset_sign, Temp_Data, FirstPage, DT
    DT = DataPush.InitPort
    reset_sign = True
    Temp_Data = {"Time": []}
    FirstPage = ''

    scheduler.pause_job("GetPort")

    return "任务已重启，时间已归零"

# 路由监控
@app.route("/RouteCheck")
def RouteCheck():
    scheduler.pause_job("GetPort")
    routes = []
    for _port in DT:
        routes.append(
            {
                "name": _port.PortName(),
                "id": _port.PortID(),
                "info": _port.PortInfo(),
                "stateSign": "badge-gradient-success" if _port.PortHealth else "badge-warning",
                "state": "状态正常" if _port.PortHealth else "状态异常",
            }
        )
    return render_template("Route.html",
                           routes=routes)


# CSV数据展示
@app.route("/csvData")
def csvData():
    scheduler.pause_job("GetPort")

    port_name = ["时间"]
    for data in DT:
        port_name.append(data.PortName())
    data = CsvReader(r"{}\{}".format(Conf.FileDic["FileURL"].replace("^", " "), Conf.FileDic["Filename"].replace("^", " ")), None)
    # print([Conf.FileDic["FileURL"], Conf.FileDic["Filename"]])
    return render_template("CsvData.html", 
                           title=port_name, 
                           csvDatas=data,
                           FileInfo=[Conf.FileDic["FileURL"].replace("^", " "), Conf.FileDic["Filename"].replace("^", " ")],
                           SaveSwitch=Conf.FileDic['isSave'],
                           )


# 设置更改
@app.route("/conf", methods=["GET", "POST"])
def conf_Change():
    if request.method == "POST":
        data = request.json
        Conf.FileChange(data)


    return "Success"

if __name__ == "__main__":
    scheduler.start()
    scheduler.pause_job("GetPort")

    app.run()