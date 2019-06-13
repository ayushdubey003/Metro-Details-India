from selenium import webdriver
import csv

driver = webdriver.Chrome("C:\\data\\chromedriver\\chromedriver_74.0.3729.6.exe")
driver.get("http://www.mmts.in/timetable.html")

writeFile = open("HyderabadLocalRouteInfo.csv", "w", newline='')
f = csv.writer(writeFile)
f.writerow(["Id"] + ["TrainNo"] + ["SourceCode"] + ["DestinationCode"] + ["Cars"] + ["StartingFrom"] + ["EndAt"] +
           ["DepartureTime"] + ["ArrivalTime"] + ["Type"] + ["Quota"] + ["DaysOfRun"])

u = driver.find_element_by_id("timingsTable")

trainNo = []
src = ""
dest = ""
initSrc = ""
endDest = ""
type = "Locals"
quota = []
daysOfRun = []
dict = []
stations = []

v = u.find_elements_by_tag_name("tr")
o = v[0].text.split(" ")

for i in range(1, len(o)):
    ind = o[i].find("*")
    if ind >= 0:
        s = o[i]
        trainNo.append(s[0:ind])
        daysOfRun.append("N")
    else:
        trainNo.append(o[i])
        daysOfRun.append("Y")

o = v[1].text.split(" ")
for i in range(0, len(o)):
    ind = o[i].find("M")
    if ind >= 0:
        quota.append("Ladies")
    else:
        quota.append("General")

for i in range(2, len(v)):
    o = v[i].text.split(" ")
    stations.append(o[0])
    timings = ""
    for j in range(1, len(o)):
        t = o[j]
        if len(t.strip()) == 0:
            print("Skipped")
            continue
        z = t.split(":")
        k = 0
        try:
            k = int(z[0])
        except Exception as e:
            continue

        aorp = ""
        if k < 12:
            aorp = "AM"
        else:
            aorp = "PM"
        k = k - 12
        if k == 0:
            k = 12
        if k < 0:
            k = k + 12
        t = k.__str__() + ":" + z[1] + aorp + "|"

        timings = timings + "|" + t
    dict.append(timings)

id = 0
initSrc = stations[0]
endDest = stations[len(stations) - 1]

for i in range(0, len(stations)):
    for j in range(i + 1, len(stations)):
        dept = dict[i].split("||")
        arr = dict[j].split("||")
        src = stations[i]
        dest = stations[j]
        for l in range(0, len(arr)):
            if arr[l].find("|") >= 0:
                arr[l] = arr[l].replace("|", "")
            if dept[l].find("|") >= 0:
                dept[l] = dept[l].replace("|", "")

        for l in range(0, len(arr)):
            id = id + 1
            da = ""
            if daysOfRun[l] == "Y":
                da = "Monday@Tuesday@Wednesday@Thursday@Friday@Saturday@Sunday"
            else:
                da = "Monday@Tuesday@Wednesday@Thursday@Friday@Saturday"
            f.writerow(
                [id.__str__()] + [trainNo[l]] + [src] + [dest] + ["NA"] + [initSrc] + [endDest] + [
                    dept[l]] + [arr[l]] + [type] + [quota[l]] + [da])

u = driver.find_element_by_id("Table1")

trainNo = []
src = ""
dest = ""
initSrc = ""
endDest = ""
type = "Locals"
quota = []
daysOfRun = []
dict = []
stations = []

v = u.find_elements_by_tag_name("tr")
o = v[0].text.split(" ")

for i in range(1, len(o)):
    ind = o[i].find("*")
    if ind >= 0:
        s = o[i]
        trainNo.append(s[0:ind])
        daysOfRun.append("N")
    else:
        trainNo.append(o[i])
        daysOfRun.append("Y")

o = v[1].text.split(" ")
for i in range(0, len(o)):
    ind = o[i].find("M")
    if ind >= 0:
        quota.append("Ladies")
    else:
        quota.append("General")

for i in range(2, len(v)):
    o = v[i].text.split(" ")
    stations.append(o[0])
    timings = ""
    for j in range(1, len(o)):
        t = o[j]
        if len(t.strip()) == 0:
            print("Skipped")
            continue
        z = t.split(":")
        k = 0
        try:
            k = int(z[0])
        except Exception as e:
            continue

        aorp = ""
        if k < 12:
            aorp = "AM"
        else:
            aorp = "PM"
        k = k - 12
        if k == 0:
            k = 12
        if k < 0:
            k = k + 12
        t = k.__str__() + ":" + z[1] + aorp + "|"

        timings = timings + "|" + t
    dict.append(timings)

initSrc = stations[0]
endDest = stations[len(stations) - 1]

for i in range(0, len(stations)):
    for j in range(i + 1, len(stations)):
        dept = dict[i].split("||")
        arr = dict[j].split("||")
        src = stations[i]
        dest = stations[j]
        for l in range(0, len(arr)):
            if arr[l].find("|") >= 0:
                arr[l] = arr[l].replace("|", "")
            if dept[l].find("|") >= 0:
                dept[l] = dept[l].replace("|", "")

        for l in range(0, len(arr)):
            id = id + 1
            da = ""
            if daysOfRun[l] == "Y":
                da = "Monday@Tuesday@Wednesday@Thursday@Friday@Saturday@Sunday"
            else:
                da = "Monday@Tuesday@Wednesday@Thursday@Friday@Saturday"
            f.writerow(
                [id.__str__()] + [trainNo[l]] + [src] + [dest] + ["NA"] + [initSrc] + [endDest] + [
                    dept[l]] + [arr[l]] + [type] + [quota[l]] + [da])

u = driver.find_element_by_id("Table2")

trainNo = []
src = ""
dest = ""
initSrc = ""
endDest = ""
type = "Locals"
quota = []
daysOfRun = []
dict = []
stations = []

v = u.find_elements_by_tag_name("tr")
o = v[0].text.split(" ")

for i in range(1, len(o)):
    ind = o[i].find("*")
    if ind >= 0:
        s = o[i]
        trainNo.append(s[0:ind])
        daysOfRun.append("N")
    else:
        trainNo.append(o[i])
        daysOfRun.append("Y")

o = v[1].text.split(" ")
for i in range(0, len(o)):
    ind = o[i].find("M")
    if ind >= 0:
        quota.append("Ladies")
    else:
        quota.append("General")

for i in range(2, len(v)):
    o = v[i].text.split(" ")
    stations.append(o[0])
    timings = ""
    for j in range(1, len(o)):
        t = o[j]
        if len(t.strip()) == 0:
            print("Skipped")
            continue
        z = t.split(":")
        k = 0
        try:
            k = int(z[0])
        except Exception as e:
            continue

        aorp = ""
        if k < 12:
            aorp = "AM"
        else:
            aorp = "PM"
        k = k - 12
        if k == 0:
            k = 12
        if k < 0:
            k = k + 12
        t = k.__str__() + ":" + z[1] + aorp + "|"

        timings = timings + "|" + t
    dict.append(timings)

initSrc = stations[0]
endDest = stations[len(stations) - 1]

for i in range(0, len(stations)):
    for j in range(i + 1, len(stations)):
        dept = dict[i].split("||")
        arr = dict[j].split("||")
        src = stations[i]
        dest = stations[j]
        for l in range(0, len(arr)):
            if arr[l].find("|") >= 0:
                arr[l] = arr[l].replace("|", "")
            if dept[l].find("|") >= 0:
                dept[l] = dept[l].replace("|", "")
            print(arr[l] + " " + dept[l])

        for l in range(0, len(arr)):
            id = id + 1
            da = ""
            if daysOfRun[l] == "Y":
                da = "Monday@Tuesday@Wednesday@Thursday@Friday@Saturday@Sunday"
            else:
                da = "Monday@Tuesday@Wednesday@Thursday@Friday@Saturday"
            f.writerow(
                [id.__str__()] + [trainNo[l]] + [src] + [dest] + ["NA"] + [initSrc] + [endDest] + [
                    dept[l]] + [arr[l]] + [type] + [quota[l]] + [da])

u = driver.find_element_by_id("Table3")

trainNo = []
src = ""
dest = ""
initSrc = ""
endDest = ""
type = "Locals"
quota = []
daysOfRun = []
dict = []
stations = []

v = u.find_elements_by_tag_name("tr")
o = v[0].text.split(" ")

for i in range(1, len(o)):
    ind = o[i].find("*")
    if ind >= 0:
        s = o[i]
        trainNo.append(s[0:ind])
        daysOfRun.append("N")
    else:
        trainNo.append(o[i])
        daysOfRun.append("Y")

o = v[1].text.split(" ")
for i in range(0, len(o)):
    ind = o[i].find("M")
    if ind >= 0:
        quota.append("Ladies")
    else:
        quota.append("General")

for i in range(2, len(v)):
    o = v[i].text.split(" ")
    stations.append(o[0])
    timings = ""
    for j in range(1, len(o)):
        t = o[j]
        if len(t.strip()) == 0:
            print("Skipped")
            continue
        z = t.split(":")
        k = 0
        try:
            k = int(z[0])
        except Exception as e:
            continue

        aorp = ""
        if k < 12:
            aorp = "AM"
        else:
            aorp = "PM"
        k = k - 12
        if k == 0:
            k = 12
        if k < 0:
            k = k + 12
        t = k.__str__() + ":" + z[1] + aorp + "|"

        timings = timings + "|" + t
    dict.append(timings)

initSrc = stations[0]
endDest = stations[len(stations) - 1]

for i in range(0, len(stations)):
    for j in range(i + 1, len(stations)):
        dept = dict[i].split("||")
        arr = dict[j].split("||")
        src = stations[i]
        dest = stations[j]
        for l in range(0, len(arr)):
            if arr[l].find("|") >= 0:
                arr[l] = arr[l].replace("|", "")
            if dept[l].find("|") >= 0:
                dept[l] = dept[l].replace("|", "")

        for l in range(0, len(arr)):
            id = id + 1
            da = ""
            if daysOfRun[l] == "Y":
                da = "Monday@Tuesday@Wednesday@Thursday@Friday@Saturday@Sunday"
            else:
                da = "Monday@Tuesday@Wednesday@Thursday@Friday@Saturday"
            f.writerow(
                [id.__str__()] + [trainNo[l]] + [src] + [dest] + ["NA"] + [initSrc] + [endDest] + [
                    dept[l]] + [arr[l]] + [type] + [quota[l]] + [da])

writeFile.close()
driver.quit()
