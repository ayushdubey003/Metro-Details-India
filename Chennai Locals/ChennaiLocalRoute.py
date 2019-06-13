import time

from selenium import webdriver
import csv

driver = webdriver.Chrome("C:\\data\\chromedriver\\chromedriver_74.0.3729.6.exe")
driver.get("https://www.metrotraintimings.com/Chennai/")

writeFile = open("ChennaiLocalRouteInfo.csv", "w", newline='')
f = csv.writer(writeFile)
f.writerow(
    ["Id"] + ["TrainNo"] + ["SourceCode"] + ["DestinationCode"] + ["Cars"] + ["DepartureTime"] + ["ArrivalTime"] + [
        "Type"] + [
        "DaysOfRun"])

u = driver.find_element_by_id("contentcolumn").find_elements_by_tag_name("p")
v = u[2].find_elements_by_tag_name("a")
stations = []
for i in range(0, len(v)):
    stations.append(v[i].text)

id = 0
trainNo = ""
src = ""
dest = ""
cars = "NA"
dept = ""
arr = ""
dor = ""

for i in range(0, len(stations)):
    for j in range(0, 2):
        if i == j:
            continue
        id = id + 1
        driver.get("https://www.metrotraintimings.com/Chennai/")
        driver.find_element_by_id("from_station").send_keys(stations[i])
        time.sleep(1)
        driver.find_element_by_id("to_station").send_keys(stations[j])
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id=\"formtrain\"]/table/tbody/tr[2]/td[3]/select").send_keys("Weekdays")
        time.sleep(1)
        driver.find_element_by_tag_name("button").click()
        time.sleep(1)
        try:
            table = driver.find_element_by_id("contentcolumn").find_elements_by_tag_name("table")
            tr = table[1].find_elements_by_tag_name("tr")
            for k in range(2, len(tr)):
                td = tr[k].find_elements_by_tag_name("td")
                trainNo = td[1].text
                src = td[3].text
                dest = td[5].text
                dept = td[4].text
                arr = td[6].text
                runson = td[2].text
                if runson.find("All") >= 0:
                    dor = "Monday@Tuesday@Wednesday@Thursday@Friday@Saturday@Sunday"
                else:
                    dor = "Monday@Tuesday@Wednesday@Thursday@Friday@Saturday"
            print(id)
            f.writerow([id.__str__()] + [trainNo] + [src] + [dest] + [cars] + [dept] + [arr] + ["Locals"] + [dor])

        except Exception as e:
            id = id - 1
            print(e.__str__())
            continue
    break

driver.quit()
