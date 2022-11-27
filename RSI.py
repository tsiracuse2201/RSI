#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import ipywidgets as widgets
import json            
import urllib.request  
import urllib.parse
import re
import datetime
import finnhub
now_ns = time.time_ns()
now = 1669390200
#test value
bfr = now - 840
ticker = 'AAPL'
query = '?'
apikey = 'c9nclciad3if6tl7i78g'
link = 'https://finnhub.io/api/v1/stock/candle'
params = urllib.parse.urlencode({'token':'c9nclciad3if6tl7i78g', 'symbol':ticker,'resolution':1,'from':bfr , 'to':now})
t = (link + query + params)
print(t)
response_object = urllib.request.urlopen(t)
response_string = response_object.read()
response_as_dictionary = json.loads(response_string)
change_in_price_list = []
price_list = response_as_dictionary['c']
i = 1
j = 0
gains = 0
losses = 0
while i <=14:
    change = price_list[j]-price_list[i]
    if change>0:
        gains+=change
    else:
        losses+=change
    change_in_price_list.append(change)
    i+=1
    j+=1

avg_gain = gains/14
avg_loss = (losses/14)*(-1)
rs = avg_gain/avg_loss
rsi = 100 - 100/(1+rs)
print(rsi)


# In[ ]:




