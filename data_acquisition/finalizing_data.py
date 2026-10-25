#importing libraries
import pandas as pd

#putting the data from the csv into a variable
extradatacsv = pd.read_csv("CHANGE_ME")

#adds the high numbers for when no pitstops were taken (don't want it to think the data was missing)
for i in range(len(extradatacsv)):

    if extradatacsv.loc[i, "stop"] == 2:
        extradatacsv.loc[i, "pitstop_lap3"] = 100000
    elif extradatacsv.loc[i,"stop"] == 1:
        extradatacsv.loc[i, "pitstop_lap2"] = 10000
        extradatacsv.loc[i, "pitstop_lap3"] = 100000

    #making all of the first lap numbers floats
    extradatacsv.loc[i, "pitstop_lap1"] = float(extradatacsv.loc[i, "pitstop_lap1"])

#renaming the columns to names that are clearer
extradatacsv = extradatacsv.rename(columns={'stop': 'NumberOfStops', 'pitstop_lap1' : 'FirstPitstopLapNumber', 'pitstop_lap2' : 'SecondPitstopLapNumber' , 'pitstop_lap3' : 'ThirdPitstopLapNumber', 'driverId': "DriverId"})
    
    
#putting the final (original) data into a csv
extradatacsv.to_csv("CHANGE_ME", index = False)