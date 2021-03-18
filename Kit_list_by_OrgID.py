## Customer kit list
## 2021 03 18
## Rich

#!/usr/bin/env python

import sciencelogic_api_functions as sl
import csv

results = []

#Search for devices under org_id = 11
url = '/api/device?limit=500&filter.0.organization.eq=11'

#Get the devices
devices = sl.get_api(url)

#Get details for each device
for device in devices:
    d_url = device['URI']
    details = sl.get_api(d_url)
    #Get device details
    name = details['name']
    ip = details['ip']
    devclass = details['class_type']
    #Vendor and type
    more = sl.get_api(devclass)
    vendor = more['class']
    ctype = more['description']
    results.append({"IP": ip, "Name": name, "Vendor": vendor, "Version": ctype})

#Then create CSV file with the results
with open('Kit_list.csv', mode='w', newline='') as csv_file:
    fieldnames = ['IP', 'Name', 'Venndor', 'Version']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for line in results:
        writer.writerow(line)
