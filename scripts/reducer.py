#!/usr/bin/env python
from sys import stdin

"""reducer function
gets a list of customers and sales grouped by cust_id
sums up sales by customer and updates sales per state
"""

stateSum = 0
states = {}

for line in sys.stdin:
    try:
        line = line.strip()
        customerid,state,price = line.split(",")
        if state == "-1":
            #New (unknown) state, calculate totals
            stateSum = stateSum + float(price)
            # print '%5.2f' % stateSum
        else:
            #State identified, add it to dictionary
            states[state] = states.get(state,0) + stateSum
            stateSum = 0
            # print '%s: %5.2f' % (state,stateSum)
    
    #This module is used by app that does not manage error handling
    except:
        pass

try:
    for key in states:
        print '%s,%0.2f' % (key, states[key])

except:
    pass
