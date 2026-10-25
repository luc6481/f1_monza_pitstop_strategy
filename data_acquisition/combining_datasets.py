#imports library
import pandas as pd

#puts the csv files into variables I can use in my code
pitstopcsv = pd.read_csv("CHANGE_ME")
standingscsv = pd.read_csv("CHANGE_ME")

keep_cols_laps2 = ['DriverId', 'GridPosition', 'ChangeInPosition', 'Year']


#combines the position and pitstop datasets that I created into one big dataset (adds new data onto the same line as the driver)
for i in range(len(pitstopcsv)):
    for j in range(len(standingscsv)):
        if (pitstopcsv.loc[i, "driverId"] == standingscsv.loc[j, "DriverId"]) and (pitstopcsv.loc[i, "Year"] == standingscsv.loc[j, "Year"]):
            pitstopcsv.loc[i, "GridPosition"] = standingscsv.loc[j, "GridPosition"]
            pitstopcsv.loc[i, "ChangeInPosition"] = standingscsv.loc[j, "ChangeInPosition"]


#puts this data into a new csv
pitstopcsv.to_csv("CHANGE_ME", index = False)
    