import requests
from bs4 import BeautifulSoup
import pandas as pd

#NO 1997
years = [1994, 1995, 1996, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]

mysterious_number = [616, 632, 651, 684, 699, 60, 717, 734, 750, 767, 785, 804, 820, 838, 855, 873]

driver_1994=[]
lap_num_1994=[]
driver_1995=[]
lap_num_1995=[]
driver_1996=[]
lap_num_1996=[]
driver_1998=[]
lap_num_1998=[]
driver_1999=[]
lap_num_1999=[]
driver_2000=[]
lap_num_2000=[]
driver_2001=[]
lap_num_2001=[]
driver_2002=[]
lap_num_2002=[]
driver_2003=[]
lap_num_2003=[]
driver_2004=[]
lap_num_2004=[]
driver_2005=[]
lap_num_2005=[]
driver_2006=[]
lap_num_2006=[]
driver_2007=[]
lap_num_2007=[]
driver_2008=[]
lap_num_2008=[]
driver_2009=[]
lap_num_2009=[]
driver_2010=[]
lap_num_2010=[]

all_driver_years = [driver_1994, driver_1995, driver_1996, driver_1998, driver_1999, driver_2000, driver_2001, driver_2002, driver_2003, driver_2004, driver_2005, driver_2006, driver_2007, driver_2008, driver_2009, driver_2010]
all_lap_years = [lap_num_1994, lap_num_1995, lap_num_1996, lap_num_1998, lap_num_1999, lap_num_2000, lap_num_2001, lap_num_2002, lap_num_2003, lap_num_2004, lap_num_2005, lap_num_2006, lap_num_2007, lap_num_2008, lap_num_2009, lap_num_2010]

#all driver dnfs
dnf_94 =[]
dnf_95 =[]
dnf_96 =[]
dnf_98 =[]
dnf_99 =[]
dnf_00 =[]
dnf_01 =[]
dnf_02 =[]
dnf_03 =[]
dnf_04 =[]
dnf_05 =[]
dnf_06 =[]
dnf_07 =[]
dnf_08 =[]
dnf_09 =[]
dnf_10 =[]

all_dnf_years = [dnf_94, dnf_95, dnf_96, dnf_98, dnf_99, dnf_00, dnf_01, dnf_02, dnf_03, dnf_04, dnf_05, dnf_06, dnf_07, dnf_08, dnf_09, dnf_10]
for i in range(len(years)):
    url = "https://www.formula1.com/en/results/" +str(years[i]) + "/races/" + str(mysterious_number[i]) + "/italy/pit-stop-summary"
    
    html = requests.get(url).text
    
    soup = BeautifulSoup(html, "html.parser")


    rows = soup.select("tr")
    
    for row in rows:
        cells = row.find_all("td")
    
        if len(cells) >= 2:
            driver = cells[2].get_text(strip=True)
            if years[i] == 1994:
                driver_1994.append(driver)
            elif years[i] == 1995:
                driver_1995.append(driver)
            elif years[i] == 1996:
                driver_1996.append(driver)
            elif years[i] == 1998:
                driver_1998.append(driver)
            elif years[i] == 1999:
                driver_1999.append(driver)
            elif years[i] == 2000:
                driver_2000.append(driver)
            elif years[i] == 2001:
                driver_2001.append(driver)
            elif years[i] == 2002:
                driver_2002.append(driver)
            elif years[i] == 2003:
                driver_2003.append(driver)
            elif years[i] == 2004:
                driver_2004.append(driver)
            elif years[i] == 2005:
                driver_2005.append(driver)
            elif years[i] == 2006:
                driver_2006.append(driver)
            elif years[i] == 2007:
                driver_2007.append(driver)
            elif years[i] == 2008:
                driver_2008.append(driver)
            elif years[i] == 2009:
                driver_2009.append(driver)
            elif years[i] == 2010:
                driver_2010.append(driver)

            lap = cells[4].get_text(strip=True)
        
            if years[i] == 1994:
                lap_num_1994.append(lap)
            elif years[i] == 1995:
                lap_num_1995.append(lap)
            elif years[i] == 1996:
                lap_num_1996.append(lap)
            elif years[i] == 1998:
                lap_num_1998.append(lap)
            elif years[i] == 1999:
                lap_num_1999.append(lap)
            elif years[i] == 2000:
                lap_num_2000.append(lap)
            elif years[i] == 2001:
                lap_num_2001.append(lap)
            elif years[i] == 2002:
                lap_num_2002.append(lap)
            elif years[i] == 2003:
                lap_num_2003.append(lap)
            elif years[i] == 2004:
                lap_num_2004.append(lap)
            elif years[i] == 2005:
                lap_num_2005.append(lap)
            elif years[i] == 2006:
                lap_num_2006.append(lap)
            elif years[i] == 2007:
                lap_num_2007.append(lap)
            elif years[i] == 2008:
                lap_num_2008.append(lap)
            elif years[i] == 2009:
                lap_num_2009.append(lap)
            elif years[i] == 2010:
                lap_num_2010.append(lap)

data = {'DriverId': driver_1994,
        'LapNum': lap_num_1994,
        'Year': [1994]*len(driver_1994)}

df = pd.DataFrame(data)

for j in range(len(years)):
    for i in range(len(all_driver_years[j])):
        df.loc[len(df)] = [all_driver_years[j][i], all_lap_years[j][i], years[j]]

for i in range(len(df)):
    df.loc[i, "DriverId"] = df.loc[i, "DriverId"][-3:]


for i in range(len(years)):
    url = "https://www.formula1.com/en/results/" +str(years[i]) + "/races/" + str(mysterious_number[i]) + "/italy/race-result"
    
    html = requests.get(url).text
    
    soup = BeautifulSoup(html, "html.parser")


    rows = soup.select("tr")
    
    for row in rows:
        cells = row.find_all("td")

        if len(cells) >= 2:
            status = cells[5].get_text(strip=True)

            if status == "DNF":

                driver = cells[2].get_text(strip=True)

                if years[i] == 1994:
                    dnf_94.append(driver)
                elif years[i] == 1995:
                    dnf_95.append(driver)
                elif years[i] == 1996:
                    dnf_96.append(driver)
                elif years[i] == 1998:
                    dnf_98.append(driver)
                elif years[i] == 1999:
                    dnf_99.append(driver)
                elif years[i] == 2000:
                    dnf_00.append(driver)
                elif years[i] == 2001:
                    dnf_01.append(driver)
                elif years[i] == 2002:
                    dnf_02.append(driver)
                elif years[i] == 2003:
                    dnf_03.append(driver)
                elif years[i] == 2004:
                    dnf_04.append(driver)
                elif years[i] == 2005:
                    dnf_05.append(driver)
                elif years[i] == 2006:
                    dnf_06.append(driver)
                elif years[i] == 2007:
                    dnf_07.append(driver)
                elif years[i] == 2008:
                    dnf_08.append(driver)
                elif years[i] == 2009:
                    dnf_09.append(driver)
                elif years[i] == 2010:
                    dnf_10.append(driver)


data2 = {'DriverId': dnf_94,
        'Year': [1994]*len(dnf_94)}

df2 = pd.DataFrame(data2)

for j in range(len(years)):
    for i in range(len(all_dnf_years[j])):
        df2.loc[len(df2)] = [all_dnf_years[j][i], years[j]]

for i in range(len(df2)):
    df2.loc[i, "DriverId"] = df2.loc[i, "DriverId"][-3:]

df.to_csv("CHANGE_ME", index = False)
df2.to_csv("CHANGE_ME", index = False)

