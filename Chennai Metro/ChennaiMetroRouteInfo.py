import time

from selenium import webdriver
import csv

driver = webdriver.Chrome("C:\\data\\chromedriver\\chromedriver_74.0.3729.6.exe")
driver.get("https://www.metrotraintimings.com/Chennai/Chennai-Metro-Rail-Timings.htm")

writeFile = open("ChennaiMetroRouteInfo.csv", "w", newline='')
f = csv.writer(writeFile)

f.writerow(
    ["Source"] + ["Destination"] + ["Duration"] + ["Route"] + ["Stations"] + ["Interchanges"] + ["Normal Fare"] + [
        "Concessional Fare(Sunday and national holiday)"])

stations = driver.find_element_by_id("from_station").text.split("\n")

src = ""
dest = ""
dur = 0
route = ""
numst = 0
interchanges = 0
fare = ""
duration = ""

for i in range(1, len(stations) - 1):
    for j in range(1, len(stations) - 1):
        driver.get("https://www.metrotraintimings.com/Chennai/Chennai-Metro-Rail-Timings.htm")
        if i == j:
            continue
        src = stations[i]
        dest = stations[j]
        route = ""
        interchanges = 0
        numst = 0

        driver.find_element_by_id("from_station").send_keys(src)
        time.sleep(1)
        driver.find_element_by_id("to_station").send_keys(dest)
        time.sleep(1)
        driver.find_element_by_tag_name("button").click()
        time.sleep(2)
        tbody = driver.find_element_by_id("txtHint").find_elements_by_tag_name("tbody")
        tr = tbody[0].find_elements_by_tag_name("tr")
        curr = ""
        for k in range(2, len(tr)):
            dur = 0
            numst = numst + 1
            td = tr[k].find_elements_by_tag_name("td")
            svg = td[1].find_element_by_tag_name("svg")
            html = svg.get_attribute("innerHTML")
            ind = html.find("fill")
            ind1 = html.find("\">")
            color = html[ind + 6:ind1]
            if k == 2:
                curr = color
                route = route + "@" + curr + ":" + td[2].text + ":"
                continue
            if curr == color:
                route = route + td[2].text + ":"
            else:
                interchanges = interchanges + 1
                curr = color
                route = route + ";@" + curr + ":" + td[2].text + ":"
            if k == len(tr) - 1:
                fr = td[6].text.strip()
                tt = td[7].text.split(":")
                fare = fr[1:len(fr)]
                hr = tt[0]
                hr = hr[1:len(hr)]
                hrs = int(hr)
                if hrs > 0:
                    dur = dur + 60
                dur = dur + int(tt[1])
                duration = dur.__str__() + "Min"
        writeFile = open("ChennaiMetroRouteInfo.csv", "w", newline='')
        f = csv.writer(writeFile)
        f.writerow(
            [src] + [dest] + [duration] + [route] + [numst.__str__()] + [interchanges.__str__()] + [fare.strip()])
        writeFile.close()

writeFile.close()
driver.quit()
