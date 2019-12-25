"""
Create list of participants
"""
import pandas as pd

# Initialize via user input
fam = []

print('Enter name of member and numerical ID.\nWhen finished enter \'quit now\'.')

member, NID = input('member_name, NID: ').split()

while member != 'quit':
	fam.append([member, NID])
	member, NID = input('member_name, NID: ').split()

print(fam)




