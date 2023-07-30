#!/usr/bin/env python

# Population of a town today is 100000. The population has increased steadily at the rate of 10 % 
# per year for last 10 years. Determine the population at the end of each year in the last decade.

population = 100000
rate = 1.1 

print('year 0 : %s' %population )

for i in range(1,11):
    population = int(population * rate)
    print('year', i, ':', population)