import csv

from selenium import webdriver

driver = webdriver.Chrome("C:\\data\\chromedriver\\chromedriver_74.0.3729.6.exe")
mUrl = "https://www.metrotraintimings.com/Chennai/mrts-Train-no-"

readFile = open("ChennaiLocalRouteInfo.csv", "r", newline='')
r = csv.reader(readFile)
l = list(r)
s = set()

for i in range(1, len(l)):
    x = l[i]
    s.add(x[1])

d = {}
print(len(l))

# for trainNo in s:
#     url = mUrl + trainNo + ".htm"
#     driver.get(url)
#     try:
#         div = driver.find_element_by_id("contentcolumn")
#         table = driver.find_elements_by_tag_name("table")
#         tbody = table[1].find_element_by_tag_name("tbody")
#         tr = tbody.find_elements_by_tag_name("tr")
#         td = tr[1].find_elements_by_tag_name("td")
#         src = td[2].text.strip()
#         td = tr[len(tr) - 1].find_elements_by_tag_name("td")
#         dest = td[2].text.strip()
#         d[trainNo] = src + ":" + dest
#     except Exception as e:
#         continue
#
# writeFile = open("ChennaiLocalEndpoints.csv", "w", newline='')
# f = csv.writer(writeFile)
# f.writerow(["Source"] + ["Destination"])
# writeFile.close()
#
# for i in range(1, len(l)):
#     x = l[i]
#     trainNo = x[1]
#     endpoints = d[trainNo].split(":")
#     src = endpoints[0]
#     dest = endpoints[1]
#     writeFile = open("ChennaiLocalEndpoints.csv", "a", newline='')
#     f = csv.writer(writeFile)
#     f.writerow([src] + [dest])
#     writeFile.close()
