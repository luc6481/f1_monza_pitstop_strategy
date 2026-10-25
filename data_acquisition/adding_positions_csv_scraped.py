import fastf1 as ff1
import pandas as pd
import numpy as np
from fastf1.ergast import Ergast


######################################################################################################################################
def same_data_type(added_data):
    for i in range(len(added_data)):
        
        try:
            added_data.loc[i, 'ClassifiedPosition'] = float(added_data.loc[i, 'ClassifiedPosition'])
        except ValueError:
            added_data = added_data.drop(index = [i])

    return added_data

def change_in_position(added_data):
    for i in range(len(added_data)):
        added_data.loc[i, "ChangeInPosition"] = added_data.loc[i, 'GridPosition'] - added_data.loc[i, 'ClassifiedPosition']
        
    return added_data
#######################################################################################################################################

years = [1994, 1995, 1996, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]


keep_cols_laps = ['LastName', 'ClassifiedPosition', 'GridPosition', 'Status', 'Year']

all_data = []

for i in range(len(years)):
    #creates my dataframe
    session_data = ff1.get_session(years[i], "Italy", "R")
    session_data.load()
    dataframe_session = session_data.results.copy()


    #deletes the columns i dont need
    dataframe_session = dataframe_session[[c for c in keep_cols_laps if c in dataframe_session.columns]]


    #resets the index of the rows (labels them correctly by number)
    dataframe_session = dataframe_session.reset_index(drop = True)

    dataframe_session['Year'] = years[i]

    dataframe_session = same_data_type(dataframe_session)
    
    dataframe_session = change_in_position(dataframe_session)

    all_data.append(dataframe_session)


#combined the data into one big dataset
all_data = pd.concat(all_data)


#resets the index of the rows (labels them correctly by number)
all_data = all_data.reset_index(drop = True)


for i in range(len(all_data)):
    print(all_data.loc[i, "LastName"])
    all_data.loc[i, "LastName"] = str(all_data.loc[i, "LastName"])[:3].upper()
    

#resets the index of the rows (labels them correctly by number)
all_data = all_data.reset_index(drop = True)

all_data.to_csv("CHANGE_ME", index = False)