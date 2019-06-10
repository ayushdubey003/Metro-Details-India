from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time

driver = webdriver.Chrome("C:\\data\\chromedriver\\chromedriver_74.0.3729.6.exe")

r = []
r.append("Source")
r.append("Destination")
r.append("Duration")
r.append("Stations")
r.append("Route")
r.append("Interchanges")
r.append("Normal Fare")
r.append("Concessional Fare(Sunday and national holiday)")

with open("DelhiRouteInfo.csv", "a", newline='') as writeFile:
    f = csv.writer(writeFile)
    f.writerow([r[0]] + [r[1]] + [r[2]] + [r[3]] + [r[4]] + [r[5]] + [r[6]] + [r[7]])
    writeFile.close()

driver.get("http://delhimetrorail.com")
u = driver.find_element_by_id("ctl00_MainContent_ddlFromStation").text
v = u.split("\n")
for i in range(168, len(v)):
    v[i] = v[i].strip()
    for j in range(0, len(v)):
        if i == j:
            continue
        writeFile = open("DelhiRouteInfo.csv", "a", newline='')
        try:
            driver.find_element_by_id("ctl00_MainContent_ddlFromStation").send_keys(v[i])
            driver.find_element_by_id("ctl00_MainContent_ddlToStation").send_keys(v[j])
            driver.find_element_by_id("ctl00_MainContent_btnShowFare").click()
            time.sleep(2)
            duration = driver.find_element_by_xpath("//*[@id=\"Preffered\"]/div[1]/ul/li[1]").text.split("-")
            stations = driver.find_element_by_xpath("//*[@id=\"Preffered\"]/div[1]/ul/li[2]").text.split("-")
            interchange = driver.find_element_by_xpath("//*[@id=\"Preffered\"]/div[1]/ul/li[3]").text.split("-")
            route = driver.find_elements_by_xpath("//*[@id=\"Preffered\"]/div[2]")
            inte = route[0].text.split("\n")
            inter = ""
            for k in range(0, len(inte)):
                inter = inter + inte[k] + ":"
            print(inter)
            nfare = driver.find_element_by_xpath("//*[@id=\"Preffered\"]/div[1]/div/div[1]/div[2]").text
            cfare = driver.find_element_by_xpath("//*[@id=\"Preffered\"]/div[1]/div/div[2]/div[2]").text
            f = csv.writer(writeFile)
            print(v[i] + " " + v[j])
            f.writerow([v[i]] + [v[j]] + [duration[1]] + [stations[1]] + [inter] + [interchange[1]] + [nfare] + [cfare])
            writeFile.close()
        except Exception as e:
            j = j - 1
            driver.get("http://delhimetrorail.com")
            continue
        driver.get("http://delhimetrorail.com")
