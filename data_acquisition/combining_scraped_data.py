import pandas as pd

positioncsv = pd.read_csv("CHANGE_ME")

scrapedcsv = pd.read_csv("CHANGE_ME")


for i in range(len(scrapedcsv)):
    for j in range(len(positioncsv)):
        if (scrapedcsv.loc[i, "DriverId"] == positioncsv.loc[j, "LastName"]) and (scrapedcsv.loc[i, "Year"] == positioncsv.loc[j, "Year"]):
            scrapedcsv.loc[i, "GridPosition"] = positioncsv.loc[j, "GridPosition"]
            scrapedcsv.loc[i, "ChangeInPosition"] = positioncsv.loc[j, "ChangeInPosition"]

        elif (scrapedcsv.loc[i, "DriverId"] == "HAK") and (positioncsv.loc[j, "LastName"] =="HÄK") and (scrapedcsv.loc[i, "Year"] == positioncsv.loc[j, "Year"]):
            scrapedcsv.loc[i, "GridPosition"] = positioncsv.loc[j, "GridPosition"]
            scrapedcsv.loc[i, "ChangeInPosition"] = positioncsv.loc[j, "ChangeInPosition"]

        elif (scrapedcsv.loc[i, "DriverId"] == "JAR") and (positioncsv.loc[j, "LastName"] =="JÄR") and (scrapedcsv.loc[i, "Year"] == positioncsv.loc[j, "Year"]):
            scrapedcsv.loc[i, "GridPosition"] = positioncsv.loc[j, "GridPosition"]
            scrapedcsv.loc[i, "ChangeInPosition"] = positioncsv.loc[j, "ChangeInPosition"]

        elif (scrapedcsv.loc[i, "DriverId"] == "RAI") and (positioncsv.loc[j, "LastName"] =="RÄI") and (scrapedcsv.loc[i, "Year"] == positioncsv.loc[j, "Year"]):
            scrapedcsv.loc[i, "GridPosition"] = positioncsv.loc[j, "GridPosition"]
            scrapedcsv.loc[i, "ChangeInPosition"] = positioncsv.loc[j, "ChangeInPosition"]

        elif (scrapedcsv.loc[i, "DriverId"] == "DIG") and (positioncsv.loc[j, "LastName"] =="DI ") and (scrapedcsv.loc[i, "Year"] == positioncsv.loc[j, "Year"]):
            scrapedcsv.loc[i, "GridPosition"] = positioncsv.loc[j, "GridPosition"]
            scrapedcsv.loc[i, "ChangeInPosition"] = positioncsv.loc[j, "ChangeInPosition"]

        elif (scrapedcsv.loc[i, "DriverId"] == "DLR") and (positioncsv.loc[j, "LastName"] =="DE ") and (scrapedcsv.loc[i, "Year"] == positioncsv.loc[j, "Year"]):
            scrapedcsv.loc[i, "GridPosition"] = positioncsv.loc[j, "GridPosition"]
            scrapedcsv.loc[i, "ChangeInPosition"] = positioncsv.loc[j, "ChangeInPosition"]

        elif (scrapedcsv.loc[i, "DriverId"] == "HUL") and (positioncsv.loc[j, "LastName"] =="HÜL") and (scrapedcsv.loc[i, "Year"] == positioncsv.loc[j, "Year"]):
            scrapedcsv.loc[i, "GridPosition"] = positioncsv.loc[j, "GridPosition"]
            scrapedcsv.loc[i, "ChangeInPosition"] = positioncsv.loc[j, "ChangeInPosition"]

        elif (scrapedcsv.loc[i, "DriverId"] == "MOY") and (positioncsv.loc[j, "LastName"] =="PAB") and (scrapedcsv.loc[i, "Year"] == positioncsv.loc[j, "Year"]):
            scrapedcsv.loc[i, "GridPosition"] = positioncsv.loc[j, "GridPosition"]
            scrapedcsv.loc[i, "ChangeInPosition"] = positioncsv.loc[j, "ChangeInPosition"]
            
scrapedcsv = scrapedcsv.reset_index(drop = True)

for i in range(len(scrapedcsv)):
    scrapedcsv.loc[i, "Rain"] = False
    scrapedcsv.loc[i, "SafetyCar"] = False
    scrapedcsv.loc[i, "RedFlag"] = False

for i in range(len(scrapedcsv)):
    if scrapedcsv.loc[i, "Year"] == 2008:
        scrapedcsv.loc[i, "Rain"] = True
    elif scrapedcsv.loc[i, "Year"] == 2000:
        scrapedcsv.loc[i, "SafetyCar"] = True

#putting the final scraped data into a csv
scrapedcsv.to_csv("CHANGE_ME", index = False)
    