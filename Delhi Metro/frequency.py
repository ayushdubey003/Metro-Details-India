from selenium import webdriver
import csv

driver = webdriver.Chrome("C:\\data\\chromedriver\\chromedriver_74.0.3729.6.exe")

driver.get("http://www.delhimetrorail.com/TRAINFREQUENCY.aspx")

r = []
r.append("Line")
r.append("Section")
r.append("Peak Hours on Weekdays")
r.append("Peak Hours on Saturday")
r.append("Peak Hours on Sunday")
r.append("Off Peak Hours on Weekdays")
r.append("Off Peak Hours on Saturday")
r.append("Off Peak Hours on Sunday")

with open("frequency.csv", "a", newline='') as writeFile:
    f = csv.writer(writeFile)
    f.writerow([r[0]] + [r[1]] + [r[2]] + [r[3]] + [r[4]] + [r[5]] + [r[6]] + [r[7]])
writeFile.close()
u = driver.find_element_by_xpath(
    "//*[@id=\"aspnetForm\"]/div[5]/div/div/div/div[2]/div/div[2]/div/table/tbody").find_elements_by_tag_name("tr")

curr = ""
for i in range(3, len(u)):
    v = u[i].find_elements_by_tag_name("td")
    writeFile = open("frequency.csv", "a", newline='')
    if len(v) == 8:
        curr = v[0].text
        f = csv.writer(writeFile)
        f.writerow(
            [curr] + [v[1].text] + [v[2].text] + [v[3].text] + [v[4].text] + [v[5].text] + [v[6].text] + [v[7].text])
    else:
        f = csv.writer(writeFile)
        f.writerow(
            [curr] + [v[0].text] + [v[1].text] + [v[2].text] + [v[3].text] + [v[4].text] + [v[5].text] + [v[6].text])
    writeFile.close()
driver.quit()
