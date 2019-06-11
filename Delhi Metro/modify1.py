import csv

readFile = open("DelhiMetroRouteInfo.csv", "r", newline='')
l = list(readFile)

r = []
r.append("Route")
writeFile = open("column1.csv", "a", newline='')
f = csv.writer(writeFile)
f.writerow([r[0]])

for i in range(1, len(l)):
    v = l[i].split(",")
    route = v[3]
    route = route.replace("<Change Here>", "")
    route = route.replace("::", ":")
    f.writerow([route])

writeFile.close()
