from selenium import webdriver
import csv

driver = webdriver.Chrome("C:\\data\\chromedriver\\chromedriver_74.0.3729.6.exe")

driver.get("https://en.wikipedia.org/wiki/List_of_Delhi_Metro_stations")
try:
    u = driver.find_element_by_xpath("//*[@id=\"mw-content-text\"]/div/table[2]/tbody").find_elements_by_tag_name("tr")
except Exception as e:
    exit(1)

r = []
r.append("Station Name")
r.append("Line")
r.append("Opened")
r.append("Layout")

with open("DelhiMetroStations.csv", "a", newline='') as writeFile:
    f = csv.writer(writeFile)
    f.writerow([r[0]] + [r[1]] + [r[2]] + [r[3]])
    writeFile.close()

curr = ""
for i in range(0, len(u)):
    v = u[i].find_elements_by_tag_name("td")
    writeFile = open("DelhiMetroStations.csv", "a", newline='')
    f = csv.writer(writeFile)
    l = []
    if len(v) == 8:
        curr = v[0].text
        for i in range(0, 5):
            if i == 1:
                continue
            l.append(v[i].text)
    else:
        l.append(curr)
        for i in range(0, 4):
            l.append(v[i].text)
    f.writerow([l[0]] + [l[1]] + [l[2]] + [l[3]])
    writeFile.close()
driver.quit()
