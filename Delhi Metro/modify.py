import csv
from difflib import SequenceMatcher
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


readFile = open("DelhiMetroStations.csv", "r", newline='')
r = csv.reader(readFile)
l = list(r)

li = []

for i in range(1, len(l)):
    v = l[i]
    s = v[0]
    li.append(s)

readFile.close()

readFile = open("DelhiMetroRouteInfo.csv", "r", newline='')
r = csv.reader(readFile)
l = list(r)
readFile.close()

writeFile = open("column.csv", "w", newline='')
f = csv.writer(writeFile)
f.writerow(["Station Name"])

stations = []
co = 0
for i in range(1, len(l)):
    v = l[i]
    co = co + 1
    if co == 224:
        co = 1
    if co == 1:
        stations.append(v[0])

for i in range(0, len(li)):
    ma = 0.0
    app = ""
    app = process.extractOne(li[i], stations)
    print(li[i])
    print(app)
    f.writerow([app.__getitem__(0)])
