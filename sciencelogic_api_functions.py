## SL SPI call functions to simplify API scripts.
## 2021 03 05
## Rich Graham
##
## To use from your script call: from sciencelogic_api_functions import *
##                               from sciencelogic_api_functions import get_api
##                               from sciencelogic_api_functions import get_api, delete_api

#!/usr/bin/env python

import requests
from requests.auth import HTTPBasicAuth
import urllib3
import time

#Connection details
root = 'https://<url>'
user = '<api-user>'
passwd = '<api-passwd>'

## API Functions

# get_api(url) - url in '/api/xxxx' format
#                returns data, with logic that if it sees result_set in the data
#                it will just return the data from within the result_set
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
    

# post_api(url, upload) - url in '/api/xxxx' format
#                       - data in json format, e.g. {"alerts": "0"}
#                         returns success/failure
def post_api(url,data):

    #Disable TLS errors from the output
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    PYTHONWARNINGS="ignore:Unverified HTTPS request"

    r = requests.post(root + url,auth=HTTPBasicAuth(user,passwd),verify=False,json=data)
    time.sleep(0.2)

    if r.status_code == 200:
        print("API post succesfull.")
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
        print("API delete succesfull.")
    else:
        print("API delete failed - Error: " + str(r.status_code))
    



