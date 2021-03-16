##############################################################
## Script to extract interface utilisation data
##  as CSV and JPG and produce html to display it
##
## Rich Graham
## 2021 03 16
##
## You'll need to ensure that a folder called Cisco-5548-01/
##
##############################################################

#!/usr/bin/env python

import sciencelogic_api_functions as sl
import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime
import glob
from dominate import document
from dominate.tags import *

pd.set_option("display.max.columns", None)
plt.rcParams["figure.figsize"] = (12,5)

#Get data for Cisco-5548-01 
url = "/api/device/4540/interface?limit=10&filter.0.name.begins_with=port-channel&filter.0.alias.begins_with=New%20P'series%20VPC"
interfaces = sl.get_api(url)

for interface in interfaces:
    name = interface['description']
    data_url = interface['URI'] + '/interface_data/data?duration=7d&hide_options=1'
    iid = interface['URI'].replace('/api/device/4540/interface','')

    i_data = sl.get_api(data_url)

    data1 = pd.DataFrame(i_data['data'])
    data1.index=(pd.to_datetime(data1.index,unit='s'))
    data1 = data1.rename(columns={'d_octets_in': 'Mbps_in', 'd_octets_out': 'Mbps_out'})
    #Convert octets into bits and then convert into Mbits (5 min poll) 
    data1['Mbps_in'] = data1['Mbps_in'].apply(lambda x: x/1000000*8/300)
    data1['Mbps_out'] = data1['Mbps_out'].apply(lambda x: x/1000000*8/300)

    title = "Cisco-5548-01 \n" + name
    graph = data1.plot()
    graph.set_title(title)
    plt.minorticks_on()
    plt.ylabel('Mbps')
    plt.xlabel('Date time')
    plt.savefig('Cisco-5548-01/' + name + '.jpg')

    data1.to_csv('Cisco-5548-01/' + name + '.csv')


#Create a simple html page to display the graphs
photos1 = glob.glob('Cisco-5548-01/*.jpg')

with document(title='Cisco-5548-01') as doc:
    h1('Cisco-5548-01')
    for path in photos1:
        div(img(src=path), _class='photo')


with open('Cisco-5548-01.html', 'w') as f:
    f.write(doc.render())

