from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time

driver = webdriver.Chrome("C:\\data\\chromedriver\\chromedriver_74.0.3729.6.exe")

r = []
r.append("Source")
r.append("Destination")
r.append("Duration")
r.append("Route")
r.append("Stations")
r.append("Interchanges")
r.append("Normal Fare")
r.append("Concessional Fare(Sunday and national holiday)")

with open("HyderabadRouteInfo.csv", "a", newline='') as writeFile:
    f = csv.writer(writeFile)
    f.writerow([r[0]] + [r[1]] + [r[2]] + [r[3]] + [r[4]] + [r[5]] + [r[6]] + [r[7]])
    writeFile.close()

driver.get("https://www.metrotraintimings.com/Hyderabad/Hyderabad-Metro-Rail-Timings.htm")
v = driver.find_element_by_id("from_station").find_elements_by_tag_name("option")
u = []
count = 0

for i in range(1, len(v)):
    u.append(v[i].text)

print(len(u))

for i in range(0, len(u)):
    for j in range(0, len(u)):
        if i == j:
            continue
        driver.get("https://www.metrotraintimings.com/Hyderabad/Hyderabad-Metro-Rail-Timings.htm")
        driver.find_element_by_id("from_station").send_keys(u[i])
        driver.find_element_by_id("to_station").send_keys(u[j])
        driver.find_element_by_class_name("button").click()
        time.sleep(2)

        count = count + 1

        v = driver.find_elements_by_tag_name("tbody")
        z = v[1].find_elements_by_tag_name("tr")

        freq = 0
        route = ""
        source = u[i]
        destination = u[j]
        fare = ""
        timeTaken = ""
        k = 0
        curr = ""
        stations = 0
        interchanges = 0
        duration = 0
        dur = ""

        str = z[0].text.split(" ")
        freq = str[4]

        for k in range(2, len(z)):
            stations = stations + 1
            td = z[k].find_elements_by_tag_name("td")
            col = td[1].find_element_by_tag_name("svg")
            s = col.get_attribute("innerHTML")
            ind1 = s.find("fill") + 6
            ind2 = s.find(">") - 1
            color = s[ind1:ind2]
            if k == 2:
                curr = color
                route = route + "@" + curr + ":" + td[2].text + ":"
            else:
                if curr == color:
                    route = route + td[2].text + ":"
                else:
                    interchanges = interchanges + 1
                    curr = color
                    route = route + ";@" + curr + ":" + td[2].text + ":"

            if k == 2:
                firstTrain = td[3].text
                lastTrain = td[4].text
            if k == len(z) - 1:
                g = td[6].text.split(" ")
                fare = g[2]
                timeTaken = td[7].text
                tt = timeTaken.split(":")
                hr = tt[0]
                hr = hr[2:len(hr)]
                min = tt[1].strip()
                duration = int(hr) * 60 + int(min)
                dur = duration.__str__()
                dur = dur + " Min"

        writeFile = open("HyderabadRouteInfo.csv", "a", newline='')
        f = csv.writer(writeFile)
        f.writerow([source] + [destination] + [dur] + [route] + [stations] + [interchanges] + [fare] + [fare])
        writeFile.close()

        print(count)

driver.quit()
