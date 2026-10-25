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
keep_cols_laps = ['driverId', 'stop','year','pitstop_lap1', 'pitstop_lap2','pitstop_lap3', "Year"]

#---------------------------------------------------------------------------------------------
#function section


#this filters out the drivers that did not finish/ got disqualified from a race
def filtering_data(year_dataset, added_data):
    for i in range(len(added_data)):
        for j in range(len(year_dataset)):
            if added_data["driverId"].loc[i] == year_dataset[j]:
                added_data = added_data.drop(index = [i])
                
                break
    added_data = added_data.reset_index(drop = True)
    return added_data

#this takes out repeat pitstop rows and instead puts each pitstop into a new column; it also gives the final number of pitstops
def combining_pitstop_data(added_data):
    driver_name = []
    try:
        for i in range(len(added_data)):
            counter_list = []
            row_number = []
            if added_data.loc[i, 'driverId'] in driver_name:
                pass
            else:
                for j in range(len(added_data)):
                    if added_data.loc[i, "driverId"] == added_data.loc[j, 'driverId']:
                        value = int(added_data.loc[j, 'lap'])
                        counter_list.append(value)
                        row_number.append(int(j))
                        driver_name.append(added_data.loc[j, 'driverId'])

                #if it has 1 pitstop
                if len(counter_list) == 1:
                    added_data.loc[i, "pitstop_lap1"] = counter_list[0]
                    added_data.loc[i, "pitstop_lap2"] = 'NA'
                    added_data.loc[i, "pitstop_lap3"] = 'NA'

                #if it has 2 pitstops
                elif len(counter_list) == 2:
                    
                    added_data.loc[i, "stop"] = 2
                    added_data.loc[i, "pitstop_lap1"] = counter_list[0]
                    added_data.loc[i, "pitstop_lap2"] = counter_list[1]
                    added_data.loc[i, "pitstop_lap3"] = 'NA'

                    added_data = added_data.drop(index = [row_number[1]])
                    added_data = added_data.reset_index(drop = True)

                #if it has 3 pitstops
                elif len(counter_list) == 3:
                    added_data.loc[i, "stop"] = 3
                    added_data.loc[i, "pitstop_lap1"] = counter_list[0]
                    added_data.loc[i, "pitstop_lap2"] = counter_list[1]
                    added_data.loc[i, "pitstop_lap3"] = counter_list[2]

                    added_data = added_data.drop(index = [row_number[1], row_number[2]])
                    added_data = added_data.reset_index(drop = True)

    except KeyError:
        pass

    #resets the number ordering
    added_data = added_data.reset_index(drop = True)
    return added_data



#----------------------------------------------------------------------------------------------
#main code section

#this goes through all of the years, loads the data, and organizes it
for i in range(len(years)):

    #takes the data using the api
    data = ergast.get_pit_stops(season= years[i], round = rounds[i], result_type= 'pandas')

    #turns it into a pandas dataframe
    data = pd.DataFrame(data.content[0])

    #calls the function that gets rid of drivers that I dont want to use
    data = filtering_data(all_years_dnfs[i], data)

    #creates the year column with the correct year 
    data['Year'] = years[i]

    #did this because it stops an error (something about cant put a none value into the list)
    data['pitstop_lap1'] = ''
    data['pitstop_lap2'] = ''
    data['pitstop_lap3'] = ''

    #calls the function that makes new columns with the pitstop data
    data = combining_pitstop_data(data)

    #adds the data into one big list
    all_data.append(data)
    
#combined the data into one big dataset
all_data = pd.concat(all_data)

#deletes the columns i dont need
all_data = all_data[[c for c in keep_cols_laps if c in all_data.columns]]

#resets the index of the rows (labels them correctly by number)
all_data = all_data.reset_index(drop = True)

#puts the data into a csv file on my computer
all_data.to_csv("CHANGE_ME", index = False)