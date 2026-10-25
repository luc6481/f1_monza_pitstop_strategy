import pandas as pd

########################################################################################################################################

def combining_pitstop_data(added_data):
    for i in range(len(added_data)):
        counter_list = []
        for j in range(len(added_data)):
            if (added_data.loc[i, "DriverId"] == added_data.loc[j, 'DriverId']) and (added_data.loc[i, "Year"] == added_data.loc[j, 'Year']) :
                value = int(added_data.loc[j, 'LapNum'])
                counter_list.append(value)

        if len(counter_list) == 1:
            added_data.loc[i, "NumberOfStops"] = 1
            added_data.loc[i, "FirstPitstopLapNumber"] = counter_list[0]
            added_data.loc[i, "SecondPitstopLapNumber"] = 10000
            added_data.loc[i, "ThirdPitstopLapNumber"] = 100000

        elif len(counter_list) == 2:
            added_data.loc[i, "NumberOfStops"] = 2
            added_data.loc[i, "FirstPitstopLapNumber"] = counter_list[0]
            added_data.loc[i, "SecondPitstopLapNumber"] = counter_list[1]
            added_data.loc[i, "ThirdPitstopLapNumber"] = 100000

        elif len(counter_list) == 3:
            added_data.loc[i, "NumberOfStops"] = 3
            added_data.loc[i, "FirstPitstopLapNumber"] = counter_list[0]
            added_data.loc[i, "SecondPitstopLapNumber"] = counter_list[1]
            added_data.loc[i, "ThirdPitstopLapNumber"] = counter_list[2]
    return added_data

########################################################################################################################################

df_totalcsv = pd.read_csv("CHANGE_ME")
df_totalcsv = pd.DataFrame(df_totalcsv)

df_dnfcsv = pd.read_csv("CHANGE_ME")
df_dnfcsv = pd.DataFrame(df_dnfcsv)


for i in range(len(df_totalcsv)):
    lines_remove = []
    for j in range(len(df_dnfcsv)):
        if (df_totalcsv.loc[i, "DriverId"] == df_dnfcsv.loc[j, "DriverId"]) and (df_totalcsv.loc[i, "Year"] == df_dnfcsv.loc[j, "Year"]):
            lines_remove.append(i)
    for m in range(len(lines_remove)):
        for n in range(len(lines_remove) - 1):
            if lines_remove[m] == lines_remove[n+1]:
                lines_remove.pop(n+1)
    for k in range(len(lines_remove)):
        df_totalcsv = df_totalcsv.drop(index = [lines_remove[k]])
        
df_totalcsv = df_totalcsv.reset_index(drop = True)

for i in range(len(df_totalcsv)):
    lines_remove = []
    for j in range(i +1, 355):
        if (df_totalcsv.loc[i, "DriverId"] == df_totalcsv.loc[j +1, "DriverId"]) and (df_totalcsv.loc[i, "Year"] == df_totalcsv.loc[j +1, "Year"]) and (df_totalcsv.loc[i, "LapNum"] == df_totalcsv.loc[j +1, "LapNum"]):
            lines_remove.append(i)
    for m in range(len(lines_remove)):
        for n in range(len(lines_remove) - 1):
            if lines_remove[m] == lines_remove[n+1]:
                lines_remove.pop(n+1)
    for k in range(len(lines_remove)):
        df_totalcsv = df_totalcsv.drop(index = [lines_remove[k]])

df_totalcsv = df_totalcsv.reset_index(drop = True)


df_totalcsv = combining_pitstop_data(df_totalcsv)

for i in range(len(df_totalcsv)):
    lines_remove = []
    for j in range(i +1, 342):
        if (df_totalcsv.loc[i, "DriverId"] == df_totalcsv.loc[j +1, "DriverId"]) and (df_totalcsv.loc[i, "Year"] == df_totalcsv.loc[j +1, "Year"]):
            lines_remove.append(i)
    for m in range(len(lines_remove)):
        for n in range(len(lines_remove) - 1):
            try:
                if lines_remove[m] == lines_remove[n+1]:
                    lines_remove.pop(n+1)
            except IndexError:
                pass
    for k in range(len(lines_remove)):
        df_totalcsv = df_totalcsv.drop(index = [lines_remove[k]])

df_totalcsv = df_totalcsv.reset_index(drop = True)

df_totalcsv.drop(["LapNum"], axis = 1, inplace = True)

df_totalcsv.to_csv("CHANGE_ME", index = False)