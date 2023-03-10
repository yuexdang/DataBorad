import PortGet.DataGet as DataGet

import serial.tools.list_ports

import csv, os

FileExist = False

InitPort = [DataGet.DataObjects(_port) for _port in list(serial.tools.list_ports.comports()) if "蓝牙链接上的标准串行" not in _port[1]]

def FileCheckExist(FileURL):
    global FileExist
    if os.path.exists(FileURL):
        print("Exist")
    else:
        os.mkdir(FileURL)
        print("Create FileDir:", FileURL)
    FileExist = True
    return


def PortWrite(PortOBJList, FileName, PortTime, FileURL, isSave=False):
    
    if not FileExist:
        FileCheckExist(FileURL)

    name = ["Time"]
    data = [PortTime]

    with open(FileURL+"\\"+FileName, 'a+', encoding='utf-8', newline='') as new_file:
        csv_writer = csv.writer(new_file)
        for PortOBJ in PortOBJList:
            _d = PortOBJ.PortRead()
            data.append(_d)

            name.append(PortOBJ.PortName())
        if isSave == "True":
            csv_writer.writerow(data)
        else:
            pass
        new_file.close()

    return dict(zip(name, data))


