"""
Create list of participants
"""
import pandas as pd
import os.path 

def init_list():
	""" initialize list of participants """
	members = []

	print('Enter name of participant and numerical ID.\nWhen finished enter \'quit now\'.')
	name, NID = input('name NID: ').split()

	while name != 'quit':
		members.append([name, NID])
		name, NID = input('name NID: ').split()

	members = pd.DataFrame(members, columns = ['Name', 'NID'])

	print(members)
	return members

def existence(file_path):
	"""
	checks for existence of file
	"""

	file_ = os.path.isfile(file_path)
	return file_

# check for existence of participants list
file_ = input('Does participants file exist? (y or n): ')

while file_ == False or file_ == 'y':
	path = input('Enter file-path: ')
	file_ = existence(path)
	if not file_:
		print('file-path incorrect.')

	participants = pd.read_csv(path)

if file_ == 'n':
	participants = init_list()
####

filename = input('Enter filename of participants list
file_exists = existence('~/programs/python/intercambio/participants.csv')
if file_exists:
	participants = pd.read_csv(

# Initialize via user input
print(fam)




