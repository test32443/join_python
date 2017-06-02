#!/usr/bin/env python

import sys

# read from standard input
for line in sys.stdin:
	try:
		customerid = "-1"
		state = "-1"
		price = "-1"
		
		line = line.strip()
		splits = line.split(",")	
		if len(splits) == 6:  #customers data
			customerid = splits[0]
			state = splits[4]
		else:   #sales data
			customerid = splits[1]
			price = splits[2]
		
		print '%s,%s,%s' % (customerid,state,price)
	
	except:
		pass
