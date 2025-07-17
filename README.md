# ScienceLogic-API

I've put togther some scripts that I've been using with the ScienceLogic API
I have created functions for the request calls, within this file you will need to update the SL1 API URL, username and password.

*Work in progress, bare with me please....*

1. Start by copying 'sciencelogic_api_functions.py' to your Python working folder.
2. Edit the file and update the root URL to reflect your SL1 server, then add in suitable credentials.
3. Any new python scripts can then import sciencelogic_api_functions.

## What it does - the functions
1.  get_api(uri) - the basic get
    device_details = get_api('/api/device/1')
2.  get_api2(uri) - adds the total and returned values from the search
    devices, total, returned = get_api2('/api/device?filter.0.organization.eq=22')
3.  get_slow(uri) - Good for cleared events, as it can timeout
    cleared_events = get_slow('/api/cleared_events')
4.  post_api(uri,data) - posting JSON to a URI
    post_api('/api/device/1', {"alerts": "0"})
5.  post_api2(uri,data)
    The same as above but with no headers. I can't remeber the use case but i needed it once.
6.  delete_api(url) - remove an entitiy by URI
    delete_api('/api/device/1')
7.  epoch2human(string) - becasue epoch timestamps suck
    timestamp = epoch2human('1730377347')
8.  get_classes() - Returns a large dictionary of device classes, saves looking stuff up.
9.  get_cugs() - Dictionary of the CUGs
10. get_orgs() - Dictionary of Organisations
11. alert_status(severity) - Translate eseverity (numerical string) to English (minor,major, etc)
12. post_gql(gql) - Post QGL to SL
    As it says, I wanted a Pythonic way to post QGL.

## Examples scripts and Graphing SL1 data

Any script starting with the word Graph does just that, graph data. I've included a few examples that hopefully deal with the various data structures that SL1 returns.
You'll need [Pandas](https://pandas.pydata.org) and [Matplotlib](https://matplotlib.org) installed to plot the graphs and [Dominate](https://github.com/Knio/dominate) for the html creation. 



## SL1 API documentation 
1. [ScienceLogic API documentation](https://docs.sciencelogic.com/latest/Content/Web_Content_Dev_and_Integration/ScienceLogic_API/api_intro.htm)
2. [ScienceLogic API schema](https://documenter.getpostman.com/view/4238205/SWE56ysV)
3. [ScienceLogic GitHub](https://github.com/ScienceLogic)
4. [SLAM-UG](https://gitlab.com/slam-ug)
