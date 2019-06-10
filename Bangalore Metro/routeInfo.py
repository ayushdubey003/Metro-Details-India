import time

from selenium import webdriver
import csv

driver = webdriver.Chrome("C:\\data\\chromedriver\\chromedriver_74.0.3729.6.exe")

driver.get("http://fare.bmrc.co.in/")

v = driver.find_element_by_id("MainContent_cmbFrom").find_elements_by_tag_name("option")
u = []
for i in range(1, len(v)):
    u.append(v[i].text)

r = []
r.append("Source")
r.append("Destination")
r.append("Route")
r.append("Time")
r.append("Fare")

writeFile = open("BangaloreRouteInfo.csv", "a", newline='')
f = csv.writer(writeFile)
f.writerow([r[0]] + [r[1]] + [r[2]] + [r[3]] + [r[4]])
writeFile.close()

time.sleep(1)

for i in range(0, len(u)):
    for j in range(0, len(u)):
        if i == j:
            continue
        driver.get("https://maps.google.com")
        
        driver.find_element_by_id("searchbox-directions").click()
