import csv

readFile = open("redLine.csv", "r", newline='')
l = list(readFile)

r = []
# r.append("Route")
writeFile = open("column1.csv", "a", newline='')
f = csv.writer(writeFile)
# f.writerow([r[0]])

for i in range(0, len(l)):
    v = l[i].split(",")
    route = v[4]
    route = route.replace("<Change Here>", "")
    route = route.replace("::", ":")
    f.writerow([route])

writeFile.close()
