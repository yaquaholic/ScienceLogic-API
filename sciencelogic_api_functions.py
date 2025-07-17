## SL SPI call functions to simplify API scripts.
## 2025 07 16
## Richard Graham
##
## To use from your script call: 
##                               import sciencelogic_api_functions as sl
##                               from sciencelogic_api_functions import get_api
##                               from sciencelogic_api_functions import get_api, delete_api
##

#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import urllib3
import time
import datetime as dt

#Connection details
root = 'https://your-site'
user = 'api-user'
passwd = 'password' 

## API Functions

# get_api(url) - url in '/api/xxxx' format
#                returns data, with logic that if it sees result_set in the data
#                it will just return the data from within the result_set
def get_api(url):
    
    #Disable TLS errors from the output
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    PYTHONWARNINGS="ignore:Unverified HTTPS request"

    r = requests.get( root + url, auth=HTTPBasicAuth(user,passwd),verify=False,timeout=60 )

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
#                 returns data, total_matched total_returnedand
#                 with logic that if it sees result_set in the data
#                 usage:
#                        data, total, returned = sl.get_api2(url)
def get_api2(url):
    
    #Disable TLS errors from the output
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    PYTHONWARNINGS="ignore:Unverified HTTPS request"

    r = requests.get( root + url, auth=HTTPBasicAuth(user,passwd),verify=False,timeout=60 )

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
#                         returns success/failure
def post_api(url,data):

    #Disable TLS errors from the output
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    PYTHONWARNINGS="ignore:Unverified HTTPS request"

    r = requests.post(root + url, auth=HTTPBasicAuth(user,passwd),verify=False,json=data)

    if r.status_code >= 200 and r.status_code <= 202:
        #print("API post succesfull.")
        data = r.json()
        return data
    else:
        print("API post failed - Error: " + str(r.status_code))

# post_api(url, upload) - url in '/api/xxxx' format
#                       - data in json format, e.g. {"alerts": "0"}
#                         returns success/failure
def post_api2(url,data,headers=""):

    #Disable TLS errors from the output
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    PYTHONWARNINGS="ignore:Unverified HTTPS request"

    r = requests.post(root + url, auth=HTTPBasicAuth(user,passwd), verify=False, data=data, headers=headers )

    if r.status_code >= 200 and r.status_code <= 202:
        print("API post succesfull.")
    else:
        print("API post failed - Error: " + str(r.status_code))
        print(str(r.text))


# delete_api(url) - url in '/api/xxxx' format
#                   returns success/failure
def delete_api(url):

    #Disable TLS errors from the output
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    PYTHONWARNINGS="ignore:Unverified HTTPS request"

    r = requests.delete( root + url, auth=HTTPBasicAuth(user,passwd),verify=False,timeout=30 )

    if r.status_code >= 200 and r.status_code < 300:
        print("API delete successful.")
    else:
        print("API delete failed - Error: " + str(r.status_code))
    

def get_slow(url):
    
    #Disable TLS errors from the output
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    PYTHONWARNINGS="ignore:Unverified HTTPS request"

    r = requests.get( root + url, auth=HTTPBasicAuth(user,passwd),verify=False,timeout=None )

    if r.status_code == 200:
        data = r.json()

        if "result_set" in data:
            data = data["result_set"]
            return data
        else:
            return data      
    else:
        print("API call failed - Error: " + str(r.status_code))

def epoch2human(string):
    #Convert SL epoch date values to timedate
    date = dt.datetime.fromtimestamp(int(string)).strftime('%Y-%m-%d %H:%M:%S')
    return date

def get_classes():
    
    classes = get_api('/api/device_class?limit=7000')
    class_dict = dict()

    for clss in classes:
        uri = clss['URI']
        name = clss['description']
        class_dict[uri] = name

    return class_dict

def get_cugs():
    
    cugs = get_api('/api/collector_group')
    cugs_dict = dict()

    for cug in cugs:
        uri = cug['URI']
        name = cug['description']
        cugs_dict[uri] = name

    return cugs_dict

def get_orgs():
    
    orgs = get_api('/api/organization')
    orgs_dict = dict()
    
    for org in orgs:
        uri = org['URI']
        name = org['description']
        orgs_dict[uri] = name
    
    return orgs_dict

## event severity (string) to status text
def alert_status(severity):
    if severity == '0':
        status = 'Healthy'
    elif severity == '1':
        status = 'Notice'
    elif severity == '2':
        status = 'Minor'
    elif severity == '3':
        status = 'Major'
    elif severity == '4':
        status = 'Critical'
    else: 
        status = 'N/A'

    return status

def post_gql(gql):
    
    #Disable TLS errors from the output
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    PYTHONWARNINGS="ignore:Unverified HTTPS request"

    r = requests.post( 'https://softcat-mon.sciencelogic.net/gql', auth=HTTPBasicAuth(user,passwd),verify=False,timeout=60, json = gql )

    if r.status_code == 200:
        data = r.json()

        if "result_set" in data:
            data = data["result_set"]
            return data
        else:
            return data      
    else:
        print("API call failed - Error: " + str(r.status_code))
