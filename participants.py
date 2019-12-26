"""
Create list of participants
"""
import pandas as pd
import os.path 

def file_exists = existence(file_path):
	"""
	checks for existence of file
	"""

	file_exists = os.path.isfile()
	return file_exists

# check for existence of participants list
file_exists = input('Does participants file exist? (y or n): ')
if file_exists:
	path = input('Enter filepath: ')
	participants = pd.read_csv(path)
else:
	participants = init_list()

filename = input('Enter filename of participants list
file_exists = existence('~/programs/python/intercambio/participants.csv')
if file_exists:
	participants = pd.read_csv(

# Initialize via user input
fam = []

print('Enter name of member and numerical ID.\nWhen finished enter \'quit now\'.')

member, NID = input('member_name, NID: ').split()

while member != 'quit':
	fam.append([member, NID])
	member, NID = input('member_name, NID: ').split()

print(fam)




