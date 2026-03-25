## SL API - Finding components devices
##          Need to resolve the SQL Servers root devices for OrgID 14
## 
## Richard Graham
## 2021 05 13
##
############################

#!/usr/bin/env python

import sciencelogic_api_functions as sl
import time
import datetime

#Search for Softcat Windows devcies
url = '/api/device?limit=20&filter.0.organization.eq=14&filter.0.class_type%2Fdescription.contains=Windows'
devices, total, returned = sl.get_api2(url)
print("Working with " + str(returned) + " from a total of " + str(total) + " devices.")

#Search by device for relationships.
for device in devices:
    did = device['URI'].replace('/api/device/','')
    print("Parent: " + device['description'])
    
    relationship_url = '/api/relationship?limit=100&filter.0.parent_device.eq=' + did

    data, total, returned = sl.get_api2(relationship_url)

    print("found " + str(total))

    for relationship in data:
        r_url = relationship['URI']
        print("Relationship url " + r_url)
        r_data = sl.get_api(r_url)
        child = r_data['child_device']
        print("Child url " + child)
        child_info = sl.get_api(child)
        if (child_info):
            print("Parent: " + device['description'] + "- Child: " + child_info['name'])
            child_did = child.replace('/api/device/','')
            print("        Child DID: " + child)

            
    print(" ")


