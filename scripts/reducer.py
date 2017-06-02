#!/usr/bin/env python

import sys

stateSum = 0
states = {}

for line in sys.stdin:
        try:
                line = line.strip()
                customerid,state,price = line.split(",")
                if state == "-1": #new state
                        stateSum = stateSum + float(price)
                        # print '%5.2f' % stateSum
                else:
                        #know state, add it to dictionary
                        states[state] = states.get(state,0) + stateSum
                        stateSum = 0
                        # print '%s: %5.2f' % (state,stateSum)
        except:
                pass

try:
        for key in states:
                print '%s,%0.2f' % (key, states[key])

except:
        pass
