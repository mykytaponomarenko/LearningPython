#!/usr/bin/env python

# print all prime numbers from 1 to 300

print('1', end=', ')

for num in range(1, 301):
  for divider in range(2, num):
    if (num % divider) == 0:
      break
    else:
      if num == divider + 1 :
        print(num, end=', ')

