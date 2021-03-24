## SL SPI call functions to simplify API scripts.
## 2021 03 23
## Rich Graham
## v 0.2 - added line breaks to post_api() and delte_api() functions
## v 0.3 - get_api2() adding total_matched and total_returned serach values to the returned data 
##         usage: data, total, returned = sl.get_api2(url)
##
## To use from your script call:
##    import sciencelogic_api_functions as sl
##

#!/usr/bin/env python

import requests
from requests.auth import HTTPBasicAuth
import urllib3
import time

#Connection details
root = 'https://your-site'
user = 'api-user'
passwd = 'password'

## API Functions

# get_api(url) - url in '/api/xxxx' format
#              - returns data, with logic that if it sees result_set in the data
#              - it will just return the data from within the result_set
def get_api(url):
    
    #Disable TLS errors from the output
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    PYTHONWARNINGS="ignore:Unverified HTTPS request"

    r = requests.get( root + url, auth=HTTPBasicAuth(user,passwd),verify=False,timeout=10 )
    time.sleep(0.2)

    if r.status_code == 200:
        data = r.json()

        if "result_set" in data:
            data = data["result_set"]
            return data
        else:
            return data      
    else:
        print("API call failed - Error: " + str(r.status_code))

        
# get_api2(url) - url in '/api/xxxx' format
#                 returns data, total_matched and total_returned search values
#                 with logic that if it sees result_set in the data
#                 usage:
#                        data, total_matched, total_returned = sl.get_api(url)
def get_api2(url):
    
    #Disable TLS errors from the output
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    PYTHONWARNINGS="ignore:Unverified HTTPS request"

    r = requests.get( root + url, auth=HTTPBasicAuth(user,passwd),verify=False,timeout=10 )
    time.sleep(0.2)

    if r.status_code == 200:
        data = r.json()
        total = data["total_matched"]
        returned = data["total_returned"]

        if "result_set" in data:
            data = data["result_set"]
            return data, total, returned
        else:
            return data, total, returned      
    else:
        print("API call failed - Error: " + str(r.status_code))
        
        
# post_api(url, upload) - url in '/api/xxxx' format
#                       - data in json format, e.g. {"alerts": "0"}
#                       - returns success/failure
def post_api(url,data):

    #Disable TLS errors from the output
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    PYTHONWARNINGS="ignore:Unverified HTTPS request"

    r = requests.post(root + url,auth=HTTPBasicAuth(user,passwd),verify=False,json=data)
    time.sleep(0.2)

    if r.status_code == 200:
        print("API post succesfull. "+ url +"\n")
    else:
        print("API post failed - Error: " + str(r.status_code))


# delete_api(url) - url in '/api/xxxx' format
#                   returns success/failure
def delete_api(url):

    #Disable TLS errors from the output
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    PYTHONWARNINGS="ignore:Unverified HTTPS request"

    r = requests.delete( root + url, auth=HTTPBasicAuth(user,passwd),verify=False,timeout=10 )
    time.sleep(0.2)

    if r.status_code == 200:
        print("API delete succesfull. "+ url +"\n")
    else:
        print("API delete failed - Error: " + str(r.status_code))
    
