# ScienceLogic-API

I've put togther some scripts that I've been using with the ScienceLogic API
I have created functions for the request calls, within this file you will need to update the SL1 API URL, username and password.

*Work in progress, bare with me please....*

1. Start by copying 'sciencelogic_api_functions.py' to your Python working folder.
2. Edit the file and update the root URL to reflect your SL1 server, then add in suitable credentials.
3. Any new python scripts can then import sciencelogic_api_functions.


## Graphing SL1 data

Any script starting with the word Graph does just that, graph data. I've included a few examples that hopefully deal with the various data structures that SL1 returns.
You'll need [Pandas](https://pandas.pydata.org) and [Matplotlib](https://matplotlib.org) installed to plot the graphs and [Dominate](https://github.com/Knio/dominate) for the html creation. 


## Updating SL1

Adding, deleting or modfiying with the API.
*Work in progress*


## SL1 API documentation 
1. [ScienceLogic API documentation](https://docs.sciencelogic.com/latest/Content/Web_Content_Dev_and_Integration/ScienceLogic_API/api_intro.htm)
2. [ScienceLogic API schema](https://documenter.getpostman.com/view/4238205/SWE56ysV)
3. [ScienceLogic GitHub](https://github.com/ScienceLogic)
4. [SLAM-UG](https://gitlab.com/slam-ug)
