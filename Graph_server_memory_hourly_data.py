################################################################################
## Script to extract memory utilisation data
##   for DID 13745 
##
## Rich Graham
## 2021 03 15
################################################################################

import sciencelogic_api_functions as sl
import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime

#Extract CPU data
duration = '90d'
url = '/api/device/13745/performance_data/1012/normalized_hourly?duration=' + duration +'&hide_options=1'

datestamp = datetime.date.today()

cpu_data = sl.get_api(url)
data = pd.DataFrame(cpu_data['data']['0'])
data.index=(pd.to_datetime(data.index,unit='s'))
data = data.astype(float)

#Graph options
pd.set_option("display.max.columns", None)
plt.rcParams["figure.figsize"] = (15,5)
title = "DB_Server Memory Data for the past " + duration + " taken: " + str(datestamp)
graph = data.plot()
graph.set_title(title)
plt.minorticks_on()
plt.ylabel('%age utilisation')
plt.xlabel('Date time')
plt.savefig('DB_Server_memory_' + duration + '_' + str(datestamp) + '.jpg')
plt.show()
