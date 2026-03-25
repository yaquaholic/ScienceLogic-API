## SL API - Device alerts by Organisation ID
## 
## Richard Graham
## 2021 03 08
##
############################

#!/usr/bin/env python

from sciencelogic_api_functions import get_api
import time
import sys


#Find last 100 events for OrgID = 12
url = "/api/cleared_event?limit=100&order.date_last=desc&filter.0.organization.eq=12"

#Create set to store hostnames in
hosts_set = set()

eventsdata = get_api(url)

for event in eventsdata:
    event_url = event["URI"]
    description = event["description"]
    
    data = get_api(event_url)

    device = data["aligned_resource_name"]
    msg = data["message"]
    durl = data["aligned_resource"]
    firstepoch = int(data["date_first"])
    lastepoch = int(data["date_last"])
    first = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(firstepoch))
    last = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(lastepoch))
        

    #Get device details
    details = get_api(durl)
    ip = details["ip"]

    uptime_url = durl + '/detail/'
    up = get_api(uptime_url)

    uptime = int(up['snmp_data']['sysuptime'])
    secs_day = 60 * 60 * 24
    secs_hour = 60 * 60
    secs_min = 60

    days = uptime // secs_day
    hours = ( uptime - (days * secs_day)) // secs_hour
    mins = ( uptime - (days * secs_day) - (hours * secs_hour)) // secs_min
                
    print (last + "," + device + "," + ip + "," + msg + "," + str(days) + " d " + str(hours) + " h " + str(mins) + " m.")




