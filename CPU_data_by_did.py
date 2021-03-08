## Extracting CPU data for CSC CUG Colector no 2 (aka 7247)
## And plot a nice graph for it. 
## 2021 03 08

from sciencelogic_api_functions import get_api, post_api
import pandas as pd
import matplotlib.pyplot as plt
import time

#Graph options
pd.set_option("display.max.columns", None)
plt.rcParams["figure.figsize"] = (15,5)

#Get data
duration = '192h'
url = '/api/device/6738/performance_data/7247/data?duration=' + duration + '&hide_options=1'

cpu_data = get_api(url)
data = pd.DataFrame(cpu_data['data'])
data.index=(pd.to_datetime(data.index,unit='s'))

title = "CSC01SLC02 CPU Data for the past " + duration
graph = data.plot()
graph.set_title(title)
plt.minorticks_on()
plt.ylabel('%age utilisation')
plt.xlabel('Date time')
plt.savefig('CSC CUG - SLC02_cpu.jpg')
plt.show()
