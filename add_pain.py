import pandas as pd
import csv

def find_pain_cols():
	df = pd.read_csv("ukb24295.csv", usecols = ['eid', '2956-0.0', '2956-1.0', '2956-2.0', '3404-0.0',  '3404-1.0',  '3404-2.0', '3414-0.0', '3414-1.0', '3414-2.0', '3571-0.0', '3571-1.0', '3571-2.0', '3741-0.0',  '3741-1.0', '3741-2.0', '3773-0.0',  '3773-1.0', '3773-2.0', '3799-0.0', '3799-1.0', '3799-2.0', '4067-0.0', '4067-1.0', '4067-2.0']) 
	df.to_csv('pain_cols.csv', index = False)

#find people who reported having 3+ months of pain
def find_pos_pain():
	df = pd.read_csv('pain_cols.csv')

#	for idx, row in df.iterrows():
#		for column in df:
#			if row.column == 1:
#					with open('yes_pain.csv', mode = 'w') as yespain_file:
#						writer = csv.writer(yespain_file, delimiter = ',', quotechar = '"')
#						writer.writerow(row)


	df2 = df[(df.values == 1).any(1)] #find people who said yes (1) to at least one type of pain
	df2.to_csv('yes_pain.csv')

def find_neg_pain():
	df = pd.read_csv('pain_cols.csv')
	
	df2 = df[df.isnull()] # find people who said nothing to these questions
	df2.to_csv('no_pain.csv')


def pain_check():
	df = pd.read_csv('yes_pain.csv')
	df2 = pd.read_csv('OA_10col_wIDPs.csv')

	result = pd.merge(df, df2, on = ['eid'])

	result.to_csv('OA_and_3mon_pain.csv')

def pain_check2():
	df = pd.read_csv('no_pain.csv')
	df2 = pd.read_csv('control_10col_wIDPs.csv')

	result = pd.merge(df, df2, on = ['eid'])

	result.to_csv('control_no_pain.csv')






def main():
	#find_pain_cols()
	#find_pos_pain()
	#pain_check()
	#find_neg_pain()
	#pain_check2()
	#find_central_pain()
	#all_central_pain()
	#remove_central_pain()
main()




































