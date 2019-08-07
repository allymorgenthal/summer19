import pandas as pd
import numpy as np

def add_age():
	df = pd.read_csv('add_rfm.csv', low_memory = False)
	df2 = pd.read_csv("ukb24295.csv", usecols = ['eid', '21022-0.0'])

	result = pd.merge(df, df2, on = ['eid'])

	result.to_csv('recruit_age_rfm.csv', index = False)

def add_age2():
	df = pd.read_csv('OA_and_3mon_pain.csv', low_memory = False)
	df2 = pd.read_csv("ukb24295.csv", usecols = ['eid', '21022-0.0'])

	result = pd.merge(df, df2, on = ['eid'])

	result.to_csv('OA_w_age.csv', index = False)

def add_age3():
	df = pd.read_csv('control_no_pain.csv', low_memory = False)
	df2 = pd.read_csv("ukb24295.csv", usecols = ['eid', '21022-0.0'])

	result = pd.merge(df, df2, on = ['eid'])

	result.to_csv('control_w_age.csv', index = False)

def add_age4():
	df = pd.read_csv('final_periph_pain2.csv', low_memory = False)
	df2 = pd.read_csv("ukb24295.csv", usecols = ['eid', '21022-0.0'])

	result = pd.merge(df, df2, on = ['eid'])

	result.to_csv('periph_wage.csv', index = False)

def add_age5():
	df = pd.read_csv('loose_control2_IDPs.csv', low_memory = False)
	df2 = pd.read_csv("ukb24295.csv", usecols = ['eid', '21022-0.0'])

	result = pd.merge(df, df2, on = ['eid'])

	result.to_csv('loose_control2_wage.csv', index = False)

def main():
	#add_age()
	#add_age2()
	#add_age3()
	#add_age4()
	add_age5()
main()