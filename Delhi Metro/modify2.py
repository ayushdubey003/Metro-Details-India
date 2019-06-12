import csv

readFile = open("redLine.csv", "r", newline='')
l = list(readFile)

r = []
r.append("Route")
writeFile = open("column1.csv", "a", newline='')
f = csv.writer(writeFile)
f.writerow([r[0]])

for i in range(0, len(l)):
    v = l[i].split(",")
    route = v[4].split(":")
    colors = v[8].split(":")
    newRoute = colors[0] + "@" + route[0] + ":"
    curr = 0
    for j in range(1, len(route)):
        if route[j].find("<") >= 0:
            curr = curr + 1
            newRoute = newRoute + route[j] + ";" + colors[curr] + "@"
        else:
            newRoute = newRoute + route[j] + ":"
    f.writerow([newRoute])

writeFile.close()