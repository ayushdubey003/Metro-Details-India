from selenium import webdriver
import csv

driver = webdriver.Chrome("C:\\data\\chromedriver\\chromedriver_74.0.3729.6.exe")
driver.get("https://www.metrotraintimings.com/Chennai/Chennai-Metro-Rail-Timings.htm")

writeFile = open("ChennaiMetroStations.csv", "w", newline='')
f = csv.writer(writeFile)

f.writerow(["Station Name"] + ["Line"])

p = driver.find_elements_by_tag_name("p")
stations = p[0].text.split("\n")
green = stations[1].split(",")
blue = stations[4].split(",")

for i in range(0, len(green)):
    f.writerow([green[i].strip()] + ["Green Line"])

for i in range(0, len(blue)):
    f.writerow([blue[i].strip()] + ["Blue Line"])

writeFile.close()
driver.quit()
