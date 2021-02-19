## SL API - Device Failed Availability Check v2
## 
## Richard Graham
## 2021 01 28
##
############################

#!/usr/bin/env python

import requests
from requests.auth import HTTPBasicAuth
import urllib3
import json
import time
import sys

#Connection details
root = "https://"
user = ''
passwd = ''


#Disable TLS errors from the output
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
PYTHONWARNINGS="ignore:Unverified HTTPS request"


#Find last 100 "Docker Container" events
search = "/api/cleared_event?limit=100&order.date_last=desc&filter.0.organization.eq=12"
url = root + search

#Create set to store hostnames in
hosts_set = set()

r = requests.get(
    url,
    auth=HTTPBasicAuth(user,passwd),
    verify=False
                )
if r.status_code == 200:
    eventsdata = r.json()["result_set"]
    event_count = r.json()["total_returned"]
    event_total = r.json()["total_matched"]
    print("Working on the last " + str(event_count) + " from a total of " + str(event_total) + " events")
    
else:
    print("HTML ERROR: " + str(r.status_code))
    sys.exit()

for event in eventsdata:
    url = event["URI"]
    description = event["description"]
    #print ( "1. Event: " + description )
    eventsearch = root + url

    r = requests.get(
        eventsearch,
        auth=HTTPBasicAuth(user,passwd),
        verify=False
                    )
    if r.status_code == 200:
        device = r.json()["aligned_resource_name"]
        msg = r.json()["message"]
        durl = r.json()["aligned_resource"]
        firstepoch = int(r.json()["date_first"])
        lastepoch = int(r.json()["date_last"])
        first = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(firstepoch))
        last = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(lastepoch))
        

        #Get device details
        details_url = root + durl
        #did = durl.replace('/api/device/','')
        ra = requests.get( details_url, auth=HTTPBasicAuth(user,passwd), verify=False )

        if ra.status_code == 200:
            details = ra.json()
            ip = details["ip"]
            
            uptime_url = details_url + '/detail/'
            up = requests.get( uptime_url, auth=HTTPBasicAuth(user,passwd),verify=False )

            if up.status_code == 200:
                uptime = int(up.json()['snmp_data']['sysuptime'])
                secs_day = 60 * 60 * 24
                secs_hour = 60 * 60
                secs_min = 60

                days = uptime // secs_day
                hours = ( uptime - (days * secs_day)) // secs_hour
                mins = ( uptime - (days * secs_day) - (hours * secs_hour)) // secs_min
                
            print (last + "," + device + "," + ip + "," + msg + "," + str(days) + " d " + str(hours) + " h " + str(mins) + " m.")




