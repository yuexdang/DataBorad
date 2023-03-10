from pyecharts import options as opts
from pyecharts.charts import Line
from  pyecharts.commons.utils import JsCode

# Offline Env
# import sys
# sys.path.append("..")
# from Test.FackData import PortWrite_Fack

DataDic = {"Time": []}

# 浅色配色
# colorSet = ["#a5dee5", "#e0f9b5", "#fefdca", "#ffcfdf", "#cca8e9", "#c3bef0", "#cadefc"]

# 深色配色
# colorSet = ["#17b978", "#2eb872", "#27296d", "#5e63b6", "#a393eb", "#11d3bc", "#7f4a88"]

# 自定义配色1
colorSet = ["#f36838", "#808080", "#1685a9", "#21a675", "#725e82", "#eacd76"]

def Get_Mix(WaitData):
    global colorSet

    mix_line = Line()

    mix_line.add_xaxis(
        [str(_t) for _t in WaitData["Time"]]
        
    )

    for num, data in enumerate(WaitData):
        if data == "Time":
            pass
        else:
            mix_line.add_yaxis(
                data,  WaitData[data],
                is_smooth=True,
                color=colorSet[num-1],

            )



    mix_line.set_series_opts(
        # areastyle_opts=opts.AreaStyleOpts(opacity=0.05),
        linestyle_opts=opts.LineStyleOpts(width=2.5),



        label_opts=opts.LabelOpts(
            is_show=False,
                                  ),
    )


    mix_line.set_global_opts(
        legend_opts=opts.LegendOpts(
            pos_top='bottom',
        ),

        xaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            is_scale=False,
            boundary_gap=False,
        ),
        yaxis_opts=opts.AxisOpts(
            boundary_gap=False,
        ),
    )
    return mix_line



def Get_Single(WaitData, SingleID, MaxPort):
    # print(WaitData)
    single_line = Line()

    single_line.add_xaxis(
        [str(_t) for _t in WaitData["Time"]]
    )

    single_line.add_yaxis(
            list(WaitData.keys())[SingleID], WaitData[list(WaitData.keys())[SingleID]],
            is_smooth=True,
            color=colorSet[MaxPort-SingleID]
        )



    single_line.set_series_opts(
        # areastyle_opts=opts.AreaStyleOpts(opacity=0.05),
        linestyle_opts=opts.LineStyleOpts(width=2.5),
        label_opts=opts.LabelOpts(is_show=False),
    )

    single_line.set_global_opts(
        legend_opts=opts.LegendOpts(
            pos_top='bottom'
        ),

        xaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            is_scale=False,
            boundary_gap=False,
        ),
    )
    return single_line


def DataSelect(WaitData, MaxSize):
    global DataDic
    for _Data in WaitData:
        if _Data in DataDic.keys():
            if len(DataDic[_Data]) > MaxSize:
                DataDic[_Data].pop(0)
                if len(DataDic[_Data]) > MaxSize:
                    DataDic[_Data].pop(0)
            DataDic[_Data].append(WaitData[_Data])
        else:
            DataDic[_Data] = [WaitData[_Data]]
    
    return DataDic