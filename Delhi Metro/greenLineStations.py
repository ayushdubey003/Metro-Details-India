from selenium import webdriver
import csv
import time

driver = webdriver.Chrome("C:\\data\\chromedriver\\chromedriver_74.0.3729.6.exe")
try:
    driver.get("https://en.wikipedia.org/wiki/Green_Line_(Delhi_Metro)")
except:
    exit()
r = []
r.append("Station Name")
r.append("Opening")
r.append("Interchange connection")
r.append("Station Layout")
r.append("Depot Connection")
r.append("Depot Layout")

with open("greenLineStations.csv", "a", newline='') as writeFile:
    f = csv.writer(writeFile)
    f.writerow([r[0]] + [r[1]] + [r[2]] + [r[3]] + [r[4]] + [r[5]])
    writeFile.close()

u = []
v = []
try:
    u = driver.find_element_by_xpath("//*[@id=\"mw-content-text\"]/div/table[4]")
    v = u.find_elements_by_tag_name("tr")
except Exception as e:
    print(str(Exception))
for i in range(3, len(v)):
    w = v[i].find_elements_by_tag_name("td")
    writeFile = open("greenLineStations.csv", "a", newline='')
    s = []
    for j in range(1, len(w)):
        if j == 2:
            continue
        s.append(w[j].text)
    f = csv.writer(writeFile)
    if len(s) == 6:
        f.writerow([s[0]] + [s[1]] + [s[2]] + [s[3]] + [s[4]] + [s[5]])
    writeFile.close()

try:
    u = driver.find_element_by_xpath("// *[ @ id = \"mw-content-text\"] / div / table[5]")
    v = u.find_elements_by_tag_name("tr")
except Exception as e:
    print(str(Exception))
for i in range(3, len(v)):
    w = v[i].find_elements_by_tag_name("td")
    writeFile = open("greenLineStations.csv", "a", newline='')
    s = []
    for j in range(1, len(w)):
        if j == 2:
            continue
        s.append(w[j].text)
    f = csv.writer(writeFile)
    if len(s) == 6:
        f.writerow([s[0]] + [s[1]] + [s[2]] + [s[3]] + [s[4]] + [s[5]])
    writeFile.close()
driver.quit()
