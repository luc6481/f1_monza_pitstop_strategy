#importing libraries
import pandas as pd

#putting the csv file into a variable that I will use in my code
basecsv = pd.read_csv("CHANGE_ME")


#goes through each year and adds the safety car, red flag, and rain data to each line
for i in range(len(basecsv)):
    if basecsv.loc[i, "Year"] == 2011:
        basecsv.loc[i, "SafetyCar"] = True
        basecsv.loc[i, "RedFlag"] = False
        basecsv.loc[i, "Rain"] = False

    elif basecsv.loc[i, "Year"] == 2012:
        basecsv.loc[i, "SafetyCar"] = False
        basecsv.loc[i, "RedFlag"] = False
        basecsv.loc[i, "Rain"] = False

    elif basecsv.loc[i, "Year"] == 2013:
        basecsv.loc[i, "SafetyCar"] = False
        basecsv.loc[i, "RedFlag"] = False
        basecsv.loc[i, "Rain"] = False

    elif basecsv.loc[i, "Year"] == 2014:
        basecsv.loc[i, "SafetyCar"] = False
        basecsv.loc[i, "RedFlag"] = False
        basecsv.loc[i, "Rain"] = False

    elif basecsv.loc[i, "Year"] == 2015:
        basecsv.loc[i, "SafetyCar"] = False
        basecsv.loc[i, "RedFlag"] = False
        basecsv.loc[i, "Rain"] = False

    elif basecsv.loc[i, "Year"] == 2016:
        basecsv.loc[i, "SafetyCar"] = False
        basecsv.loc[i, "RedFlag"] = False
        basecsv.loc[i, "Rain"] = False

    elif basecsv.loc[i, "Year"] == 2017:
        basecsv.loc[i, "SafetyCar"] = False
        basecsv.loc[i, "RedFlag"] = False
        basecsv.loc[i, "Rain"] = False
        
    elif basecsv.loc[i, "Year"] == 2018:
        basecsv.loc[i, "SafetyCar"] = True
        basecsv.loc[i, "RedFlag"] = False
        basecsv.loc[i, "Rain"] = True
        
    elif basecsv.loc[i, "Year"] == 2019:
        basecsv.loc[i, "SafetyCar"] = True
        basecsv.loc[i, "RedFlag"] = False
        basecsv.loc[i, "Rain"] = False
        
    elif basecsv.loc[i, "Year"] == 2020:
        basecsv.loc[i, "SafetyCar"] = True 
        basecsv.loc[i, "RedFlag"] = True
        basecsv.loc[i, "Rain"] = False
        
    elif basecsv.loc[i, "Year"] == 2021:
        basecsv.loc[i, "SafetyCar"] = True
        basecsv.loc[i, "RedFlag"] = False
        basecsv.loc[i, "Rain"] = False
        
    elif basecsv.loc[i, "Year"] == 2022:
        basecsv.loc[i, "SafetyCar"] = True
        basecsv.loc[i, "RedFlag"] = False
        basecsv.loc[i, "Rain"] = False
        
    elif basecsv.loc[i, "Year"] == 2023:
        basecsv.loc[i, "SafetyCar"] = False
        basecsv.loc[i, "RedFlag"] = False
        basecsv.loc[i, "Rain"] = False
        
    elif basecsv.loc[i, "Year"] == 2024:
        basecsv.loc[i, "SafetyCar"] = False
        basecsv.loc[i, "RedFlag"] = False
        basecsv.loc[i, "Rain"] = False
        
    elif basecsv.loc[i, "Year"] == 2025:
        basecsv.loc[i, "SafetyCar"] = False
        basecsv.loc[i, "RedFlag"] = False
        basecsv.loc[i, "Rain"] = False
        
    elif basecsv.loc[i, "Year"] == 2026:
        basecsv.loc[i, "SafetyCar"] = False
        basecsv.loc[i, "RedFlag"] = True
        basecsv.loc[i, "Rain"] = False
        

#puts all of this data into a csv file
basecsv.to_csv("CHANGE_ME", index = False)