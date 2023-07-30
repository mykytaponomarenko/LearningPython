#!/usr/bin/env python

# print out all Armstrong numbers between 1 and 500

for i in range(1, 501):
    k = str(i)
    q = 0
    for c in k:
        q = q + int(c) ** 3
    if i == q:
        print(k, 'is armstrong number')
#    else:
#        print(k, 'vs', q)
