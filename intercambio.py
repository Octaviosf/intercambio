"""
Problem:
    Randomly pair person A with person B where A and B are not the same.
"""
import pandas as pd
from members_list import members_list
from random_pair import random_pair

# load members dataframe
members = members_list()

# randomly pair members
pairings = random_pair(members)
pairings.reset_index(drop=True, inplace=True)
 
print()
print(pairings[pairings['receiver'] != 'Alex'].to_string())
print('\n')

# print giver of mine
ready = input('If ready to see my giver, then enter y: ')

while ready != 'y':
	ready = input('If ready to see my giver, then enter y: ')
	if ready == 'y':
		break

my_giver = pairings.loc[pairings['receiver'] == 'Alex']

print('\nThe giver of Alex is:')
print(my_giver.to_string())
