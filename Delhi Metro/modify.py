import csv
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


readFile = open("DelhiMetroStations.csv", "r", newline='')
r = csv.reader(readFile)
l = list(r)

d = {}

for i in range(1, len(l)):
    v = l[i]
    s = v[1]
    ind = s.find("Line")
    s = s[0:ind]
    s = s.strip()
    key = v[0].lower()
    if key in d:
        f = d[key]
        f = f + "|" + s
        d[key] = f
    else:
        d[key] = s

readFile.close()

readFile = open("DelhiMetroRouteInfo.csv", "r", newline='')
r = csv.reader(readFile)
l = list(r)
readFile.close()

d1 = {"Red": 0,
      "Yellow": 0,
      "Blue": 0,
      "Green": 0,
      "Violet": 0,
      "Orange": 0,
      "Pink": 0,
      "Magenta": 0,
      "Grey": 0}

writeFile = open("column.csv", "a", newline='')
f = csv.writer(writeFile)
f.writerow(["Lines"])
writeFile.close()

for i in range(1, len(l)):
    o = l[i]
    z = int(o[5].strip())
    color = ""
    if z > 0:
        f = o[4]
        x = f.split(":")
        res = -1
        for j in range(0, len(x)):
            ma = 0.0
            ind = x[j].find("<")
            for key in d:
                z = similar(key, x[j].lower())
                if z > ma:
                    ma = z
                    res = key
            arr = d[res].split("|")
            if ind < 0:
                for k in range(0, len(arr)):
                    d1[arr[k]] = d1[arr[k]] + 1
            elif ind >= 0:
                for k in range(0, len(arr)):
                    d1[arr[k]] = d1[arr[k]] + 1
                ma1 = 0
                co = ""
                for key in d1:
                    if int(d1[key]) > ma1:
                        ma1 = d1[key]
                        co = key
                    d1[key] = 0
                color = color + co + ":"
            if j == len(x) - 1:
                ma1 = 0
                co = ""
                for key in d1:
                    if int(d1[key]) > ma1:
                        ma1 = d1[key]
                        co = key
                    d1[key] = 0
                color = color + co + ":"
    else:
        f = o[4]
        x = f.split(":")
        res = -1
        for j in range(0, len(x)):
            ma = 0.0
            for key in d:
                z = similar(key, x[j].lower())
                if z > ma:
                    ma = z
                    res = key
            arr = d[res].split("|")
            if j == len(x) - 1:
                for k in range(0, len(arr)):
                    d1[arr[k]] = d1[arr[k]] + 1
                ma1 = 0
                co = ""
                for key in d1:
                    if int(d1[key]) > ma1:
                        ma1 = d1[key]
                        co = key
                        d1[key] = 0
                color = color + co + ":"
    writeFile = open("column.csv", "a", newline='')
    f = csv.writer(writeFile)
    print(color)
    f.writerow([color])
    writeFile.close()
