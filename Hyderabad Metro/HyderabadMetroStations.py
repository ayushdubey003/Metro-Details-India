from selenium import webdriver
import csv

driver = webdriver.Chrome("C:\\data\\chromedriver\\chromedriver_74.0.3729.6.exe")
driver.get("https://en.wikipedia.org/wiki/List_of_Hyderabad_Metro_stations")

writeFile = open("HyderabadMetroStations.csv", "w", newline='')
f = csv.writer(writeFile)
f.writerow(["Station Name"] + ["Line"] + ["Opened"] + ["Layout"])

u = driver.find_element_by_xpath("//*[@id=\"mw-content-text\"]/div/table[2]")
v = u.find_elements_by_tag_name("tr")

currStation = ""
line = ""
currOpened = ""
currLayout = ""

for i in range(1, len(v)):
    x = v[i].find_elements_by_tag_name("td")
    if len(x) == 7:
        currStation = x[0].text
        line = x[2].text
        currOpened = x[3].text
        currLayout = x[4].text
    else:
        line = x[0].text
    print(currStation + " " + line + " " + currOpened + " " + currLayout)
    f.writerow([currStation] + [line] + [currOpened] + [currLayout])

writeFile.close()
