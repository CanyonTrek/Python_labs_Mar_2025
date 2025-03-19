#! /usr/bin/python

#                    1         2         3         4         5
#          012345678901234567890123456789012345678901234567890
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print("-" * len(Belgium)) # Q1
print(Belgium.replace(',', ':')) # Q2
pop = int(Belgium[8:16])
pop_city = int(Belgium[26:32])
print("Population=", pop + pop_city) # Q3
print("-" * len(Belgium)) # Q4