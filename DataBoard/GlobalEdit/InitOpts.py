# DataCopy
'''
isSave = True
DataBoardInfo = "页面说明文字,加入后续的单位说明:SignInfor"
'''

class ConfObject:
    def __init__(self, FileURL):
        self.FileURL = FileURL
        self.FileDic = self.GetInit()
        return None

    def GetInit(self):
        with open(self.FileURL, "r", encoding="utf-8") as F:
            conf = dict(ini.replace(" ", "").replace("\n", "").split("=") for ini in F.readlines() if "=" in ini)
            F.close()
            return conf

    def FileChange(self, ChangeInfo):
        with open(self.FileURL, "w", encoding="utf-8") as F:
            for key in ChangeInfo:
                self.FileDic[key] = ChangeInfo[key]
            for k in self.FileDic:
                if k in ChangeInfo.keys():
                    self.FileDic[k] = ChangeInfo[k]
                F.writelines("{} = {}\n".format(k, self.FileDic[k]))
            F.close()
            return




# Offline Env
# a = ConfObject("../conf.ini")
# print(a.FileDic)
#
# a.FileChange({"isSave": 'False', 'isGet': '123'})
# print(a.FileDic)