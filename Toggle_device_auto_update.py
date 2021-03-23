## SL API - Toggle Auto Update (nightly discvovery)
##          Controlling overnight interface rediscovery
##          With multithreaded execution (~ X10 faster)
## 2021 03 23

import sciencelogic_api_functions as sl
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time

start = time()
processes = []

#Devices by OrgID and toggle auto_update
toggle = 1 #find devices with it enabled, 0 for disabled and lose '&filter.0.auto_update.eq=?' if you care not
url = '/api/device?limit=150&filter.0.organization.eq=79&filter.0.auto_update.eq=1'
devices = sl.get_api(url)

data = {"auto_update": "0"}      # where zero = disable

#Create 20 execution workers, using post_api()
with ThreadPoolExecutor(max_workers=20) as executor:
    for device in devices:
        processes.append(executor.submit(sl.post_api, device['URI'], data))

for task in as_completed(processes):
    task.result()

print(f'Time taken: {time() - start}')
