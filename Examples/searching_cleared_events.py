## SL API - Events for org_id and date filter.
## As the API uses epoch time, not ISO 8601.
## Damn you ScienceLogic, damn you.
##
## Rich Graham
## 2021-05-07
#################################################

#!/usr/bin/env python

import sciencelogic_api_functions as sl
import time
import datetime

#ISO 8601 to epoch time, adjust as required
date_time = '2021-05-06 00:00:00'
pattern = '%Y-%m-%d %H:%M:%S'
epoch = int(time.mktime(time.strptime(date_time, pattern)))
#print(epoch)

#API search
limit = 1000
limit = '?limit=' + str(limit)
filter_date = '&filter.0.date_last.min=' + str(epoch)
filter_org = '&filter.0.organization.eq=36'
filter_order = '&order.date_last=desc'
url = '/api/cleared_event' + limit + filter_order + filter_date + filter_org

data, total, returned = sl.get_api2(url)


for event in data:
    event_url = event["URI"]
    description = event["description"]
    details = sl.get_api(event_url)

    device = details['aligned_resource_name']
    alert = details['message']
    last = details['date_last']
    last = datetime.datetime.fromtimestamp(int(last)).strftime('%Y-%m-%d %H:%M:%S')
    severity = details['severity']
    print(last +": "+ device +": "+ alert +": "+ severity)


