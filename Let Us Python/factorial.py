#!/usr/bin/env python

inp = int(input('type number base for factorial calculation\n'))

fact = 1
for i in range(1,inp):
    fact = fact * (i + 1)

print(fact)