## Find flapping devices, from CSC CUG and re-assign to new collector group
## Troubleshotting the seemingly constant false alerts we're seeing. 
## 2021 03 15

#!/usr/bin/env python

from sciencelogic_api_functions import get_api, post_api

device_list = []
cug_list = ['/api/collector_group/3', '/api/collector_group/8']

#Flapping cleared events (policy 4011)
limit = 100
print("Collecting the last " + str(limit) + " cleared flapping events. \n")
url = '/api/cleared_event?limit=' + str(limit) + '&order.date_last=desc&filter.0.event_policy.eq=%2Fapi%2Fevent_policy%2F4011'
events = get_api(url)

for event in events:
    event_url = event['URI']
    event_details = get_api(event_url)
    
    device_url = event_details['aligned_resource']
    device_list.append(device_url)

#Make list unique values only
print("Events collected, making list unique for next step \n")
device_list = set(device_list)

for device_url in device_list:
    device_details = get_api(device_url)
    did = device_url.replace('/api/device/','')

    name = device_details['name']
    cug = device_details['collector_group']
    


    if cug in cug_list:
        print("\n" + name + " " + did + " is currently in " + cug )
        data = {'collector_group': '/api/collector_group/14'}
        print("Updating CUG for " + name + "\n")
        
        ## Update CUG to 14
        #post_api(device_url,data)
        
    else:
        print( name + " is in " + cug + " so ignore it" )
        
        

    

    
    

    

