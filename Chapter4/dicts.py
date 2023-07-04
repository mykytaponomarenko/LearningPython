#!/usr/bin/env python

D = {'food' : 'Spam', 'quantity' : 4, 'color' : 'pink'}
print(D)
print(D['food']) # same as index in sequences but key instead

D['quantity'] += 1
print(D)

# Keys can be created by assignment
D['name'] = 'Mykyta'
print(D)
