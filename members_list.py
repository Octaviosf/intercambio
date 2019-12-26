"""
Create list of members
"""
import pandas as pd
import os.path 
import random as random

def init_list():
	""" initialize list of members """
	members = []

	print('Enter name of member and numerical ID.\nWhen finished enter \'quit now\'.')
	name, NID = input('name NID: ').split()

	while name != 'quit':
		# create random number
		rand_num = random.randrange(1, 99)
		members.append([name, int(NID), (rand_num*int(NID))%100])
		name, NID = input('name NID: ').split()

	members = pd.DataFrame(members, columns = ['Name', 'NID', 'RID'])

	members.to_csv('members.csv', index=False)

	return members

def existence(file_path):
	"""
	checks for existence of file
	"""

	file_ = os.path.isfile(file_path)
	return file_

def members_list():

	# check for existence of members list
	file_ = input('Does members file exist? (y or n): ')

	# read existing list
	while file_ == False or file_ == 'y':
		path = input('Enter file-path: ')
		file_ = existence(path)
		if not file_:
			print('file-path incorrect.')
		elif file_:
			members = pd.read_csv(path)
			print(members.to_string())
			break

	# create list
	if file_ == 'n':
		members = init_list()
		print(members.to_string())

	return members

# members = members_list()	
