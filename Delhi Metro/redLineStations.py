from selenium import webdriver
import csv
import time

driver = webdriver.Chrome("C:\\data\\chromedriver\\chromedriver_74.0.3729.6.exe")
try:
    driver.get("https://en.wikipedia.org/wiki/Red_Line_(Delhi_Metro)")
except:
    exit()
r = []
r.append("Station Name")
r.append("Phase")
r.append("Opening")
r.append("Interchange connection")
r.append("Station Layout")
r.append("Platform Level Type")
r.append("Depot Connection")
r.append("Depot Layout")

with open("redLineStations.csv", "a", newline='') as writeFile:
    f = csv.writer(writeFile)
    f.writerow([r[0]] + [r[1]] + [r[2]] + [r[3]] + [r[4]] + [r[5]] + [r[6]] + [r[7]])
    writeFile.close()

u = []
v = []
try:
    u = driver.find_elements_by_class_name("wikitable")
    v = u[1].find_elements_by_tag_name("tr")
except Exception as e:
    quit(1)
for i in range(3, len(v)):
    w = v[i].find_elements_by_tag_name("td")
    writeFile = open("redLineStations.csv", "a", newline='')
    s = []
    for j in range(1, len(w)):
        if j == 2:
            continue
        s.append(w[j].text)
    f = csv.writer(writeFile)
    if len(s) == 8:
        f.writerow([s[0]] + [s[1]] + [s[2]] + [s[3]] + [s[4]] + [s[5]] + [s[6]] + [s[7]])
    writeFile.close()
driver.quit()
