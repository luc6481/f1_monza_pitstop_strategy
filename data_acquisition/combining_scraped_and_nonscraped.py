import pandas as pd

nonscrapedcsv = pd.read_csv("CHANGE_ME")

scrapedcsv = pd.read_csv("CHANGE_ME")

for i in range(len(nonscrapedcsv), len(nonscrapedcsv) + len(scrapedcsv)-2):
    nonscrapedcsv.loc[i] = scrapedcsv.loc[i-277]

nonscrapedcsv = nonscrapedcsv.reset_index(drop = True)

#putting the final data into a csv!!
nonscrapedcsv.to_csv("CHANGE_ME", index = False)
