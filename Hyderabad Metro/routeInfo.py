from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time

driver = webdriver.Chrome("C:\\data\\chromedriver\\chromedriver_74.0.3729.6.exe")

r = []
r.append("Source")
r.append("Destination")
r.append("Route")
r.append("Interchanges")
r.append("Fare")
r.append("Time")

with open("HyderabadRouteInfo.csv", "a", newline='') as writeFile:
    f = csv.writer(writeFile)
    f.writerow([r[0]] + [r[1]] + [r[2]] + [r[3]] + [r[4]] + [r[5]])
    writeFile.close()

driver.get("https://www.metrotraintimings.com/Hyderabad/Hyderabad-Metro-Rail-Timings.htm")
v = driver.find_element_by_id("from_station").find_elements_by_tag_name("option")
u = []
for i in range(1, len(v)):
    u.append(v[i].text)
for i in range(0, len(u)):
    for j in range(0, len(u)):
        if i == j:
            continue
        driver.get("https://www.metrotraintimings.com/Hyderabad/Hyderabad-Metro-Rail-Timings.htm")
        driver.find_element_by_id("from_station").send_keys(u[i])
        driver.find_element_by_id("to_station").send_keys(u[j])
        driver.find_element_by_class_name("button").click()
        time.sleep(2)
        v = driver.find_elements_by_tag_name("tbody")
        x = v[0].find_elements_by_tag_name("tr")
        print(len(x))
        break
    break
