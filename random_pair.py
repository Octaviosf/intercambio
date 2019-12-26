import pandas as pd
pd.options.mode.chained_assignment = None
import random

def random_pair(members):
	"""
	members: dataframe of members
	returns: dataframe of random member pairs
	"""

	# split list randomly by sorting by random number
	members.sort_values(by=['RID'], inplace=True)
	members.reset_index(drop=True, inplace=True)

	n_members = members.shape[0]
	n_half = n_members // 2

	givers_1 = members.iloc[:n_half, :]
	givers_2 = members.iloc[n_half:, :]
	receivers_1 = givers_2.copy(deep=True)
	receivers_2 = givers_1.copy(deep=True)

	# create non-duplicate random numbers list
	r_g1_col = random.sample(range(n_half), n_half) 
	r_g2_col = random.sample(range(n_half), n_half) 
	r_r1_col = random.sample(range(n_half), n_half) 
	r_r2_col = random.sample(range(n_half), n_half) 

	# append random columns to dfs
	givers_1.loc[:,'RID'] = r_g1_col
	givers_2.loc[:,'RID'] = r_g2_col
	receivers_1.loc[:,'RID'] = r_r1_col
	receivers_2.loc[:,'RID'] = r_r2_col
	 
	# rename columns
	givers_1.rename(columns={"Name": "giver"}, inplace = True)
	givers_2.rename(columns={"Name": "giver"}, inplace = True)
	receivers_1.rename(columns={"Name": "receiver"}, inplace = True)
	receivers_2.rename(columns={"Name": "receiver"}, inplace = True)

	# merge dataframes
	g_1 = givers_1.merge(receivers_1, left_on='RID', right_on='RID')
	g_2 = givers_2.merge(receivers_2, left_on='RID', right_on='RID')

	# sort dfs
	g_1.sort_values(by=['RID'], inplace = True)
	g_2.sort_values(by=['RID'], inplace = True)

	# reset indices
	g_1.reset_index(drop=True, inplace=True)
	g_2.reset_index(drop=True, inplace=True)

	# remove columns
	g_1 = g_1.loc[:,['giver','receiver']]
	g_2 = g_2.loc[:,['giver','receiver']]

	# append dfs
	random_pair = g_1.append(g_2)

	return random_pair

