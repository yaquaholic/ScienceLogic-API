## Testing SL api functions
## 2021 03 05

#!/usr/bin/env python

from sciencelogic_api_functions import get_api
import time

#Test searching for devices
print("\nTesting device search get_api()")
url = '/api/device?limit=5'
data = get_api(url)

for device in data:
    #print(device)
    url = device['URI']
    details = get_api(url)

    print(details['name'] + " (" + details['ip'] + ")")

#Test a single device
print("\nTesting device get_api()")
url = '/api/device/553'
device = get_api(url)

print(device["name"] + " (" + device['ip'] +")")


#Test searching for events
print("\nTesting cleared events search get_api()")
#url = '/api/cleared_event?limit=5&order.date_last=desc'
url = '/api/cleared_event?order.date_last=desc&filter.0.aligned_resource%2Fdevice.eq=9393&filter.0.message.contains=Te2%2F1%2F3'
events = get_api(url)

for event in events:
    #print(event)
    url = event['URI']
    details = get_api(url)
    last = int(details['date_last'])
    last = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last))

    print(details['aligned_resource_name'] + " " + details['message'] + " last seen at " + last )
