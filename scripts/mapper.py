#!/usr/bin/env python
from sys import stdin

"""mapper function:
reads csv-formatted customer and sales files
and streams data out for reducer consumption
"""

#Iterate over standard input
for line in sys.stdin:
    try:
        customerid = "-1"
        state = "-1"
        price = "-1"
		
        line = line.strip()
        splits = line.split(",")	
        if len(splits) == 6:  
            #Reading Customers data file
            customerid = splits[0]
            state = splits[4]
        else:
            #Reading Sales data file
            customerid = splits[1]
            price = splits[2]
		
            print "%s,%s,%s" % (customerid,state,price)

    #This module is used by app that does not manage error handling
    except:
        pass
