import serial.tools.list_ports
import serial  # 导入串口通信模块
import re


class DataObjects:
    def __init__(self, Port, BPS=9600):
        self.Portname = Port[0]
        self.Portinfo = Port[1]
        self.Portid = Port[2]
        self.ComP = serial.Serial(Port[0], int(BPS), bytesize=8, parity=serial.PARITY_NONE, stopbits=1)
        self.PortCheck()
        return None

    def PortName(self):
        return self.Portname

    def PortID(self):
        return self.Portid

    def PortInfo(self):
        return self.Portinfo

    def PortHealth(self):
        return True if self.PortCheck(NoPrint=False) else False

    def PortCheck(self, NoPrint=True):
        if self.ComP.isOpen():  # 判断串口是否打开
            self.ComP.flushInput()
            if NoPrint:
                print(self.Portname, "has opened and has been flushed")
            return self.ComP
        else:
            return False

    def DataChange(self, data):
        tail = re.sub(u"([^\u0041-\u007a])", "", data).upper()
        num = float(data.replace(tail, ""))
        if tail[0] == "K":
            num *= 1000
        elif tail[0] == "M":
            num *= 1000000
        return round(num, 2)

    def PortRead(self):
        portData = self.ComP.readline().decode('utf-8').rstrip()
        portData = self.DataChange(portData)
        return portData
