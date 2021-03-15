################################################################################
## Script to extract CPU utilisation data
##   for SCT01APP01 aka 8831 
##   as CSV and JPG and produce html to display it
##
## Rich Graham
## 2021 03 01
################################################################################

import sciencelogic_api_functions as sl
import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime

#Extract CPU data
duration = '90d'
url = '/api/device/6738/performance_data/7247/normalized_hourly?duration=' + duration + '&hide_options=1'

datestamp = datetime.date.today()

cpu_data = sl.get_api(url)
data = pd.DataFrame(cpu_data['data']['0'])
data.index=(pd.to_datetime(data.index,unit='s'))
data = data.astype(float)

#Graph options
pd.set_option("display.max.columns", None)
plt.rcParams["figure.figsize"] = (15,5)
title = "SCT01APP01 CPU Data for the past " + duration + " taken: " + str(datestamp)
graph = data.plot()
graph.set_title(title)
plt.minorticks_on()
plt.ylabel('%age utilisation')
plt.xlabel('Date time')
plt.savefig('C:/Users/GrahamR/Downloads/CSC01SLC02_cpu_' + duration + '_' + str(datestamp) + '.jpg')
plt.show()
