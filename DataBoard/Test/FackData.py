import random, time

FackTime = 0
send = 6

def TimeClean():
    global FackTime
    FackTime = 0
    return FackTime

def TimeUp():
    global FackTime
    FackTime = round(FackTime+0.1, 1)
    return FackTime

def PortWrite_Fack(PortOBJList, FileName, PortTime, isSave=True, FileURL=r".\CsvDir\\"):
    global FackTime, send
    
    name = ["Time"]
    data = [FackTime]
    
    TimeUp()
    for i in range(send):
        name.append("COM{}".format(i+1))
        data.append(random.randint(100,500))
    # time.sleep(0.1)
    return dict(zip(name, data))
    # return name,data
# for i in range(10):
#     print(PortWrite_Fack(1,1,1))

class Fack_Data:
    def __init__(self,name) -> None:
        self.name = name
        return None
    
    def Fack_name(self):
        return self.name


def DT_Fack():
    return [Fack_Data(i) for i in range(send)]