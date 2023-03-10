

def CsvReader(File, TitleMsg):
    lines = []
    try:
        with open(File, 'r', encoding="utf-8") as F:
            while True:
                line = F.readline()
                if not line:
                    break
                else:
                    lines.append(line.replace("\n", "").split(","))
            F.close()
    except IOError:
        pass
    return lines

