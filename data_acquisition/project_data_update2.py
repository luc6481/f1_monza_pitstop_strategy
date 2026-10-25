#importing libraries that I need
import fastf1 as ff1
import pandas as pd
import numpy as np
from fastf1.ergast import Ergast

#this keeps the data on a cache instead of pulling it each time
ff1.Cache.enable_cache("CHANGE_ME")

#this initializes the Ergast API ?
ergast = Ergast()

#-----------------------------------------------------------------------------------------
#list section


#these are the lists that hold the drivers that did not finish or got disqualified each year
dnf_2011 = ["ricciardo", "perez", "kobayashi", "sutil", 'webber', 'ambrosio', 'petrov', 'rosberg','liuzzi' ]
dnf_2012 = ['webber', 'hulkenberg', 'vettel', 'button', 'vergne']
dnf_2013 = ['sutil', 'vergne', 'resta']
dnf_2014 = ['alonso', 'chilton']
dnf_2015 = ['rosberg', 'alonso', 'grosjean', 'maldonado']
dnf_2016 = ['kvyat', 'wehrlein', 'jolyon_palmer', 'nasr']
dnf_2017 = ['alonso', 'ericsson', 'vandoorne', 'jolyon_palmer']
dnf_2018 = ['ricciardo', 'alonso', 'brendon_hartley', 'grosjean']
dnf_2019 = ['kevin_magnussen', 'kvyat', 'sainz']
dnf_2020 = ['max_verstappen', 'leclerc', 'kevin_magnussen', 'vettel']
dnf_2021 = ['mazepin', 'hamilton', 'max_verstappen', 'gasly', 'tsunoda']
dnf_2022 = ['ricciardo', 'stroll', 'alonso', 'vettel']
dnf_2023 = ['ocon', 'tsunoda']
dnf_2024 = ['tsunoda']
dnf_2025 = ['alonso', 'hulkenberg']
dnf_2026 = ['stroll', 'alonso', 'leclerc']

#this combined all of the years above into one list, making it lists inside of a list
all_years_dnfs = [dnf_2011, dnf_2012, dnf_2013, dnf_2014, dnf_2015, dnf_2016, dnf_2017, dnf_2018, dnf_2019, dnf_2020, dnf_2021, dnf_2022, dnf_2023, dnf_2024, dnf_2025, dnf_2026]

#this stores all of the data from each race
all_data = []

#this stores the years that I want to take data from
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
#this stores the round number that Monza was each year
rounds = [13, 13, 12, 13, 12, 14, 13, 14, 14, 8, 14, 16, 14, 16, 16, 13]

#this is the list of columns that I want to keep at the end
keep_cols_laps = ['DriverId', 'ClassifiedPosition', 'GridPosition', 'Status', 'Year']
keep_cols_laps2 = ['DriverId', 'GridPosition', 'ChangeInPosition', 'Year']
#_____________________________________________________________________________________________________________________________________
#function section

#filters out drivers that did not finish a race or finished with a huge gap (e.g. driver finished 13 laps behind)
def filtering_data(year_dataset, added_data):
    for i in range(len(added_data)):
        for j in range(len(year_dataset)):
            if added_data.loc[i, "DriverId"] == year_dataset[j]:
                added_data = added_data.drop(index = [i])
                break
    added_data = added_data.reset_index(drop = True)
    return added_data

#this changes all of the data to floats to make it the same data type
def same_data_type(added_data):
    for i in range(len(added_data)):
        
        added_data.loc[i, 'ClassifiedPosition'] = float(added_data.loc[i, 'ClassifiedPosition'])

    return added_data

#this calculates the change in position of the drivers from the start to the end
def change_in_position(added_data):
    for i in range(len(added_data)):
        added_data.loc[i, "ChangeInPosition"] = added_data.loc[i, 'GridPosition'] - added_data.loc[i, 'ClassifiedPosition']
        
    return added_data

#____________________________________________________________________________________________________________________________________


#goes through each year and organizes the data
for i in range(len(years)):


    #loads and saves the data I want
    session_data = ff1.get_session(years[i], rounds[i], "R")
    session_data.load()
    dataframe_session = session_data.results.copy()


    #deletes the columns i dont need
    dataframe_session = dataframe_session[[c for c in keep_cols_laps if c in dataframe_session.columns]]

    #resets the index of the rows (labels them correctly by number)
    dataframe_session = dataframe_session.reset_index(drop = True)

    #filters out DNFs
    dataframe_session = filtering_data(all_years_dnfs[i], dataframe_session)

    #adds the correct year to the column
    dataframe_session['Year'] = years[i]

    #makes all of the data the same data type
    dataframe_session = same_data_type(dataframe_session)

    #calculates the change in position of the driver
    dataframe_session = change_in_position(dataframe_session)

    #deletes the columns I no longer need (different than earlier, I needed some of these for organizing the data)
    dataframe_session = dataframe_session[[c for c in keep_cols_laps2 if c in dataframe_session.columns]]

    #adds the data to a giant list
    all_data.append(dataframe_session)

#combined the data into one big dataset
all_data = pd.concat(all_data)

#resets the index of the rows (labels them correctly by number)
all_data = all_data.reset_index(drop = True)

#puts the data into a csv file!
all_data.to_csv("CHANGE_ME", index = False)

