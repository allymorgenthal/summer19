import pandas as pd
import numpy as np

def calc_rfm_all():
	df = pd.read_csv('combine_OA_control_labels.csv')

	df.insert(30, 'rfm', np.nan)

	#gender = '31-0.0'
	#height = '50-0.0'
	#waist = '48-0.0'
	
	#for row1 in df.itertuples():
	#	for row2 in df2.itertuples():
	for idx, row1 in df.iterrows():
		if row1.gender == 0:
			rfm = 76 - (20 * (row1.height/row1.waist))
			df.set_value(idx, 'rfm', rfm)
		elif row1.gender == 1:
			rfm = 64 - (20 * (row1.height/row1.waist))
			df.set_value(idx, 'rfm', rfm)

	df.to_csv('add_rfm.csv', index = False)


def calc_rfm_OA():
	df = pd.read_csv('OA_w_age.csv')

	df.insert(31, 'rfm', np.nan)

	#gender = '31-0.0'
	#height = '50-0.0'
	#waist = '48-0.0'
	
	#for row1 in df.itertuples():
	#	for row2 in df2.itertuples():
	for idx, row1 in df.iterrows():
		if row1.gender == 0:
			rfm = 76 - (20 * (row1.height/row1.waist))
			df.set_value(idx, 'rfm', rfm)
		elif row1.gender == 1:
			rfm = 64 - (20 * (row1.height/row1.waist))
			df.set_value(idx, 'rfm', rfm)

	df.to_csv('add_rfm.csv', index = False)

def calc_rfm_control():
	df = pd.read_csv('combine_OA_control_labels.csv')

	df.insert(31, 'rfm', np.nan)

	#gender = '31-0.0'
	#height = '50-0.0'
	#waist = '48-0.0'
	
	#for row1 in df.itertuples():
	#	for row2 in df2.itertuples():
	for idx, row1 in df.iterrows():
		if row1.gender == 0:
			rfm = 76 - (20 * (row1.height/row1.waist))
			df.set_value(idx, 'rfm', rfm)
		elif row1.gender == 1:
			rfm = 64 - (20 * (row1.height/row1.waist))
			df.set_value(idx, 'rfm', rfm)

	df.to_csv('add_rfm.csv', index = False)

def calc_rfm_periph():
	df = pd.read_csv('periph_wage.csv')

	df.insert(6, 'rfm', np.nan)

	#gender = '31-0.0'
	#height = '50-0.0'
	#waist = '48-0.0'
	
	#for row1 in df.itertuples():
	#	for row2 in df2.itertuples():
	for idx, row1 in df.iterrows():
		if row1.gender == 0:
			rfm = 76 - (20 * (row1.height/row1.waist))
			df.set_value(idx, 'rfm', rfm)
		elif row1.gender == 1:
			rfm = 64 - (20 * (row1.height/row1.waist))
			df.set_value(idx, 'rfm', rfm)

	df.to_csv('periph_rfm_age.csv', index = False)


def calc_rfm_loose():
	df = pd.read_csv('loose_control2_wage.csv')

	df.insert(6, 'rfm', np.nan)

	#gender = '31-0.0'
	#height = '50-0.0'
	#waist = '48-0.0'
	
	#for row1 in df.itertuples():
	#	for row2 in df2.itertuples():
	for idx, row1 in df.iterrows():
		if row1.gender == 0:
			rfm = 76 - (20 * (row1.height/row1.waist))
			df.set_value(idx, 'rfm', rfm)
		elif row1.gender == 1:
			rfm = 64 - (20 * (row1.height/row1.waist))
			df.set_value(idx, 'rfm', rfm)

	df.to_csv('loose_rfm_age.csv', index = False)

def main():
	#calc_rfm_all()
	#calc_rfm_periph()
	calc_rfm_loose()
main()