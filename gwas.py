import pandas as pd
import numpy as np


def find_central_pain():
	df = pd.read_csv('clinical_columns_regID.csv')

	bipolar_self = ['1291']
	bipolar_hosp = ['F310', 'F311', 'F312', 'F313', 'F314', 'F315', 'F316', 'F317', 'F318', 'F319']
	schiz_self = ['1289']
	schiz_hosp = ['F200', 'F201', 'F202', 'F203', 'F204', 'F205', 'F206', 'F208', 'F209']
	fibro_self = ['1542']
	fibro_hosp = ['M7970', 'M7971', 'M7974', 'M7975', 'M7978', 'M7979']
	stroke_self = ['1081']
	stroke_hosp = ['G463', 'G464']
	MS_self = ['1261']
	MS_hosp = ['G35']
	alz_self = ['1263']
	alz_hosp = ['G300', 'G301', 'G308', 'G309']
	atrophy_hosp = ['G310']
	hunt_hosp = ['G10']
	park_self = ['1262']
	park_hosp = ['F023', 'G20']
	dementia_hosp = ['F020', 'F028']
	other_hosp = ['F068', 'F069', 'F078', 'F079']

	self_report_array = bipolar_self + schiz_self + fibro_self + stroke_self + MS_self + alz_self + park_self
	hosp_record_array = bipolar_hosp + schiz_hosp + fibro_hosp + stroke_hosp + MS_hosp + alz_hosp + atrophy_hosp + hunt_hosp + park_hosp + dementia_hosp + other_hosp

	file2 = df.loc[(df['20002-0.0'].isin(self_report_array)) | (df['20002-0.1'].isin(self_report_array)) | (df['20002-0.2'].isin(self_report_array)) | (df['20002-0.3'].isin(self_report_array)) | (df['20002-0.4'].isin(self_report_array)) | (df['20002-0.5'].isin(self_report_array)) | (df['20002-0.6'].isin(self_report_array)) | (df['20002-0.7'].isin(self_report_array)) | (df['20002-0.8'].isin(self_report_array)) | (df['20002-0.9'].isin(self_report_array)) | (df['20002-0.10'].isin(self_report_array))]
	file3 = df.loc[(df['41202-0.0'].isin(hosp_record_array)) | (df['41202-0.1'].isin(hosp_record_array)) | (df['41202-0.2'].isin(hosp_record_array)) | (df['41202-0.3'].isin(hosp_record_array)) | (df['41202-0.4'].isin(hosp_record_array)) | (df['41202-0.5'].isin(hosp_record_array)) | (df['41202-0.6'].isin(hosp_record_array)) | (df['41202-0.7'].isin(hosp_record_array)) | (df['41202-0.8'].isin(hosp_record_array)) | (df['41202-0.9'].isin(hosp_record_array)) | (df['41202-0.10'].isin(hosp_record_array))] 

	file2.to_csv('self_report_central.csv', index = False)
	file3.to_csv('hosp_record_central.csv', index = False)


def find_periph_pain():
	df = pd.read_csv('clinical_columns_regID.csv')

	OA_self = ['1465']
	other_athrosis_array = ['M1900', 'M1901', 'M1902', 'M1903', 'M1904', 'M1905', 'M1906', 'M1907', 'M1908', 'M1909']
	coxarthrosis_array = ['M160', 'M161', 'M162', 'M164', 'M165', 'M166', 'M167', 'M169']
	gonarthrosis_array = ['M170', 'M171', 'M172', 'M173', 'M174', 'M175', 'M179']

	otherRA_hosp = ['M0680', 'M0681', 'M0682', 'M0685', 'M0686', 'M0687', 'M0688', 'M0689', 'M0690', 'M0691', 'M0692', 'M0693', 'M0694', 'M0695', 'M0696', 'M0697', 'M0698', 'M0699']
	RA_self = ['1464']
	seroposRA_hosp = ['M0580', 'M0582', 'M0583', 'M0584', 'M0586', 'M0587', 'M0588', 'M0589', 'M0590', 'M0591', 'M0592', 'M0593', 'M0594', 'M0595', 'M0596', 'M0597', 'M0598', 'M0599']
	seronegRA_hosp = ['M0600', 'M0601', 'M0602', 'M0603', 'M0604', 'M0605', 'M0606', 'M0607', 'M0608', 'M0609']

	BP_self = ['1534']
	BP_hosp = ['M54.50', 'M54.52', 'M54.53', 'M54.54', 'M54.55', 'M54.56', 'M54.57', 'M54.58', 'M54.59']

	otherOA = ['M1981', 'M1983', 'M1984', 'M1985', 'M1986', 'M1987', 'M1988', 'M1989', 'M1990', 'M1991', 'M1992', 'M1993', 'M1994', 'M1995', 'M1996', 'M1997', 'M1998', 'M1999']
	handOA = ['M180', 'M181', 'M182', 'M183', 'M185', 'M189']
	genOA = ['M1500']

	self_report_array = RA_self + BP_self + OA_self
	hosp_record_array = otherRA_hosp + seroposRA_hosp + seronegRA_hosp + BP_hosp + otherOA + handOA + genOA + other_athrosis_array + coxarthrosis_array + gonarthrosis_array

	file2 = df.loc[(df['20002-0.0'].isin(self_report_array)) | (df['20002-0.1'].isin(self_report_array)) | (df['20002-0.2'].isin(self_report_array)) | (df['20002-0.3'].isin(self_report_array)) | (df['20002-0.4'].isin(self_report_array)) | (df['20002-0.5'].isin(self_report_array)) | (df['20002-0.6'].isin(self_report_array)) | (df['20002-0.7'].isin(self_report_array)) | (df['20002-0.8'].isin(self_report_array)) | (df['20002-0.9'].isin(self_report_array)) | (df['20002-0.10'].isin(self_report_array))]
	file3 = df.loc[(df['41202-0.0'].isin(hosp_record_array)) | (df['41202-0.1'].isin(hosp_record_array)) | (df['41202-0.2'].isin(hosp_record_array)) | (df['41202-0.3'].isin(hosp_record_array)) | (df['41202-0.4'].isin(hosp_record_array)) | (df['41202-0.5'].isin(hosp_record_array)) | (df['41202-0.6'].isin(hosp_record_array)) | (df['41202-0.7'].isin(hosp_record_array)) | (df['41202-0.8'].isin(hosp_record_array)) | (df['41202-0.9'].isin(hosp_record_array)) | (df['41202-0.10'].isin(hosp_record_array))] 

	file2.to_csv('self_report_periph2.csv', index = False)
	file3.to_csv('hosp_record_periph2.csv', index = False)

def combine():
	df = pd.read_csv("self_report_periph2.csv")
	df2 = pd.read_csv("hosp_record_periph2.csv")

	result = pd.concat([df, df2]).drop_duplicates().reset_index(drop=True)

	result.to_csv("all_periph_pain2.csv", index = False)

def three_mon_check():
	df = pd.read_csv('yes_pain.csv')
	df2 = pd.read_csv('all_periph_pain2.csv')

	result = pd.merge(df, df2, on = ['eid'])

	result.to_csv('periph_3mon2.csv', index = False)

def no_cent_pain_check():
	df = pd.read_csv("all_central_pain.csv", low_memory = False)
	df2 = pd.read_csv("periph_3mon2.csv", low_memory = False)

	result = df2[~df2.eid.isin(df.eid.values)]

	result.to_csv('periph_3mon_nocent2.csv', index = False)

def add_gwas_pain():
	df = pd.read_csv('periph_3mon_nocent2.csv', low_memory=False)

	df.insert(2, 'gwas', 2)

	df.to_csv('gwas_pain_group.csv', index = False)

def sort():
	df = pd.read_csv('gwas.csv')
	df2 = pd.read_csv('gwas_pain_group.csv')

	df = df.set_index('eid')
	df = df.reindex(index=df2['eid'])
	df = df.reset_index()

	df.to_csv('gwas2.csv', index=False)

def add_gwas1_PG_label():
	df = pd.read_csv("gwas.csv",)
	df2 = pd.read_csv("gwas2.csv")


	#for idx, row1 in df.iterrows():
	#	for idx, row2 in df2.iterrows():
	#		if row1.eid == row2.eid:
	#			df.set_value(idx, 'gwas1', 2) 
	#df.to_csv("gwas3.csv", index = False)


	#for idx, row in df.iterrows():
	#if df.eid.isin(df2.eid):
	#	df.set_value(idx, 'gwas1', 2)
	#df.to_csv("gwas3.csv", index = False)


	#m = df.merge(df2, how='left', on=['eid'])
	#df['gwas1'] = df['gwas1'].mask(m, 2)
	#df.to_csv("gwas3.csv", index = False)



	#v = df.set_index(['eid'])
	#m = v.index.get_indexer(pd.MultiIndex.from_arrays([df2.eid])) == 1
	#df.loc[m, 'gwas1'] = 2
	#df.to_csv("gwas3.csv", index = False)

	idx_cols = ['eid']
	mask = df.set_index(idx_cols).index.isin(df2.set_index(idx_cols).index)
	df['gwas1'].where(~mask, 1, inplace=True)
	df.to_csv("gwas3.csv", index = False)


def find_control():
	df = pd.read_csv("clinical_columns_regID.csv", low_memory = False, delimiter=',', encoding="utf-8-sig")
	#print(df.head())
	rheumatoid_arthritis_array = ['M0680', 'M0681', 'M0682', 'M0685', 'M0686', 'M0687', 'M0688', 'M0689', 'M0690', 'M0691', 'M0692', 'M0693', 'M0694', 'M0695', 'M0696', 'M0697', 'M0698', 'M0699']
	other_athrosis_array = ['M1900', 'M1901', 'M1902', 'M1903', 'M1904', 'M1905', 'M1906', 'M1907', 'M1908', 'M1909']
	coxarthrosis_array = ['M160', 'M161', 'M162', 'M164', 'M165', 'M166', 'M167', 'M169']
	gonarthrosis_array = ['M170', 'M171', 'M172', 'M173', 'M174', 'M175', 'M179']
	arthritis_array = coxarthrosis_array + gonarthrosis_array + rheumatoid_arthritis_array + other_athrosis_array
	#file2 = df.loc[df["41202-0.0"] == 'M161']
	#file2 = df.loc[df['eid'] == 1400897]
	file2 = df.loc[(df['41202-0.0'].isnull()) & (df['41202-0.1'].isnull()) & (df['41202-0.2'].isnull()) & (df['41202-0.3'].isnull()) & (df['41202-0.4'].isnull()) & (df['41202-0.5'].isnull()) & (df['41202-0.6'].isnull()) & (df['41202-0.7'].isnull()) & (df['41202-0.8'].isnull()) & (df['41202-0.9'].isnull()) & (df['41202-0.10'].isnull()) & (df['20002-0.0'].isnull()) & (df['20002-0.1'].isnull()) & (df['20002-0.2'].isnull()) & (df['20002-0.3'].isnull()) & (df['20002-0.4'].isnull()) & (df['20002-0.5'].isnull()) & (df['20002-0.6'].isnull()) & (df['20002-0.7'].isnull()) & (df['20002-0.8'].isnull()) & (df['20002-0.9'].isnull()) & (df['20002-0.10'].isnull())]
	file2.to_csv('control_allrecords2.csv', index =False)

def pain_check2():
	df = pd.read_csv('no_pain.csv')
	df2 = pd.read_csv('control_allrecords2.csv')

	result = pd.merge(df, df2, on = ['eid'])

	result.to_csv('control_no_pain2.csv')

	

def add_gwas1_CG_label():
	df = pd.read_csv("gwas3.csv",)
	df2 = pd.read_csv("gwas2.csv")

	idx_cols = ['eid']
	mask = df.set_index(idx_cols).index.isin(df2.set_index(idx_cols).index)
	df['gwas1'].where(~mask, 1, inplace=True)
	df.to_csv("gwas4.csv", index = False)


def add_gwas1():
	df = pd.read_csv("gwas4.csv")
	df2 = pd.read_csv("gwas_pain_group.csv")
	df3 = pd.read_csv("control_no_pain2.csv")

	df.insert(2, 'gwas1', 'NA')

	mask1 = df.set_index('eid').index.isin(df2.set_index('eid').index)
	df['gwas1'].where(~mask1, 2, inplace = True)
	mask2 = df.set_index('eid').index.isin(df3.set_index('eid').index)
	df['gwas1'].where(~mask2, 1, inplace = True)

	df.to_csv('gwas_phenotypes.csv', index = False)

def add_gwas2():
	df = pd.read_csv("gwas_phenotypes.csv")
	df2 = pd.read_csv("all_periph_pain_final.csv")
	df3 = pd.read_csv("control_final.csv")

	df.insert(3, 'gwas2', np.nan)

	mask1 = df.set_index('eid').index.isin(df2.set_index('eid').index)
	df['gwas2'].where(~mask1, 2, inplace = True)
	mask2 = df.set_index('eid').index.isin(df3.set_index('eid').index)
	df['gwas2'].where(~mask2, 1, inplace = True)

	df.to_csv('gwas_phenotypes.csv', index = False)

def test_col():
	df = pd.read_csv('gwas_phenotypes.csv')

	df.insert(4, 'gwas3', 'NA')

	df.to_csv('test.csv', index = False)

def test_na():
	df = pd.read_csv('gwas_phenotypes.csv')

	df.replace('', np.nan, inplace = True)

	print(df.head())
	df.to_csv('na_test.csv', index = False)



def find_nocent_pain():
	df = pd.read_csv('clinical_columns_regID.csv')

	bipolar_self = ['1291']
	bipolar_hosp = ['F310', 'F311', 'F312', 'F313', 'F314', 'F315', 'F316', 'F317', 'F318', 'F319']
	schiz_self = ['1289']
	schiz_hosp = ['F200', 'F201', 'F202', 'F203', 'F204', 'F205', 'F206', 'F208', 'F209']
	fibro_self = ['1542']
	fibro_hosp = ['M7970', 'M7971', 'M7974', 'M7975', 'M7978', 'M7979']
	stroke_self = ['1081']
	stroke_hosp = ['G463', 'G464']
	MS_self = ['1261']
	MS_hosp = ['G35']
	alz_self = ['1263']
	alz_hosp = ['G300', 'G301', 'G308', 'G309']
	atrophy_hosp = ['G310']
	hunt_hosp = ['G10']
	park_self = ['1262']
	park_hosp = ['F023', 'G20']
	dementia_hosp = ['F020', 'F028']
	other_hosp = ['F068', 'F069', 'F078', 'F079']

	self_report_array = bipolar_self + schiz_self + fibro_self + stroke_self + MS_self + alz_self + park_self
	hosp_record_array = bipolar_hosp + schiz_hosp + fibro_hosp + stroke_hosp + MS_hosp + alz_hosp + atrophy_hosp + hunt_hosp + park_hosp + dementia_hosp + other_hosp

	file2 = df.loc[(~df['20002-0.0'].isin(self_report_array)) | (~df['20002-0.1'].isin(self_report_array)) | (~df['20002-0.2'].isin(self_report_array)) | (~df['20002-0.3'].isin(self_report_array)) | (~df['20002-0.4'].isin(self_report_array)) | (~df['20002-0.5'].isin(self_report_array)) | (~df['20002-0.6'].isin(self_report_array)) | (~df['20002-0.7'].isin(self_report_array)) | (~df['20002-0.8'].isin(self_report_array)) | (~df['20002-0.9'].isin(self_report_array)) | (~df['20002-0.10'].isin(self_report_array))]
	file3 = df.loc[(~df['41202-0.0'].isin(hosp_record_array)) | (~df['41202-0.1'].isin(hosp_record_array)) | (~df['41202-0.2'].isin(hosp_record_array)) | (~df['41202-0.3'].isin(hosp_record_array)) | (~df['41202-0.4'].isin(hosp_record_array)) | (~df['41202-0.5'].isin(hosp_record_array)) | (~df['41202-0.6'].isin(hosp_record_array)) | (~df['41202-0.7'].isin(hosp_record_array)) | (~df['41202-0.8'].isin(hosp_record_array)) | (~df['41202-0.9'].isin(hosp_record_array)) | (~df['41202-0.10'].isin(hosp_record_array))] 

	file2.to_csv('self_report_nocentral.csv', index = False)
	file3.to_csv('hosp_record_nocentral.csv', index = False)

def combine1():
	df = pd.read_csv("self_report_nocentral.csv")
	df2 = pd.read_csv("hosp_record_nocentral.csv")

	result = pd.concat([df, df2]).drop_duplicates().reset_index(drop=True)

	result.to_csv("all_nocent_pain.csv", index = False)


def find_noperiph_pain():
	df = pd.read_csv('clinical_columns_regID.csv')

	OA_self = ['1465']
	other_athrosis_array = ['M1900', 'M1901', 'M1902', 'M1903', 'M1904', 'M1905', 'M1906', 'M1907', 'M1908', 'M1909']
	coxarthrosis_array = ['M160', 'M161', 'M162', 'M164', 'M165', 'M166', 'M167', 'M169']
	gonarthrosis_array = ['M170', 'M171', 'M172', 'M173', 'M174', 'M175', 'M179']

	otherRA_hosp = ['M0680', 'M0681', 'M0682', 'M0685', 'M0686', 'M0687', 'M0688', 'M0689', 'M0690', 'M0691', 'M0692', 'M0693', 'M0694', 'M0695', 'M0696', 'M0697', 'M0698', 'M0699']
	RA_self = ['1464']
	seroposRA_hosp = ['M0580', 'M0582', 'M0583', 'M0584', 'M0586', 'M0587', 'M0588', 'M0589', 'M0590', 'M0591', 'M0592', 'M0593', 'M0594', 'M0595', 'M0596', 'M0597', 'M0598', 'M0599']
	seronegRA_hosp = ['M0600', 'M0601', 'M0602', 'M0603', 'M0604', 'M0605', 'M0606', 'M0607', 'M0608', 'M0609']

	BP_self = ['1534']
	BP_hosp = ['M54.50', 'M54.52', 'M54.53', 'M54.54', 'M54.55', 'M54.56', 'M54.57', 'M54.58', 'M54.59']

	otherOA = ['M1981', 'M1983', 'M1984', 'M1985', 'M1986', 'M1987', 'M1988', 'M1989', 'M1990', 'M1991', 'M1992', 'M1993', 'M1994', 'M1995', 'M1996', 'M1997', 'M1998', 'M1999']
	handOA = ['M180', 'M181', 'M182', 'M183', 'M185', 'M189']
	genOA = ['M1500']

	self_report_array = RA_self + BP_self + OA_self
	hosp_record_array = otherRA_hosp + seroposRA_hosp + seronegRA_hosp + BP_hosp + otherOA + handOA + genOA + other_athrosis_array + coxarthrosis_array + gonarthrosis_array

	file2 = df.loc[(~df['20002-0.0'].isin(self_report_array)) | (~df['20002-0.1'].isin(self_report_array)) | (~df['20002-0.2'].isin(self_report_array)) | (~df['20002-0.3'].isin(self_report_array)) | (~df['20002-0.4'].isin(self_report_array)) | (~df['20002-0.5'].isin(self_report_array)) | (~df['20002-0.6'].isin(self_report_array)) | (~df['20002-0.7'].isin(self_report_array)) | (~df['20002-0.8'].isin(self_report_array)) | (~df['20002-0.9'].isin(self_report_array)) | (~df['20002-0.10'].isin(self_report_array))]
	file3 = df.loc[(~df['41202-0.0'].isin(hosp_record_array)) | (~df['41202-0.1'].isin(hosp_record_array)) | (~df['41202-0.2'].isin(hosp_record_array)) | (~df['41202-0.3'].isin(hosp_record_array)) | (~df['41202-0.4'].isin(hosp_record_array)) | (~df['41202-0.5'].isin(hosp_record_array)) | (~df['41202-0.6'].isin(hosp_record_array)) | (~df['41202-0.7'].isin(hosp_record_array)) | (~df['41202-0.8'].isin(hosp_record_array)) | (~df['41202-0.9'].isin(hosp_record_array)) | (~df['41202-0.10'].isin(hosp_record_array))] 

	file2.to_csv('self_report_noperiph.csv', index = False)
	file3.to_csv('hosp_record_noperiph.csv', index = False)


def combine2():
	df = pd.read_csv("self_report_noperiph.csv")
	df2 = pd.read_csv("hosp_record_noperiph.csv")

	result = pd.concat([df, df2]).drop_duplicates().reset_index(drop=True)

	result.to_csv("all_noperiph_pain.csv", index = False)

def combine3():
	df = pd.read_csv('all_nocent_pain.csv')
	df2 = pd.read_csv('all_noperiph_pain.csv')

	result = pd.concat([df, df2]).drop_duplicates().reset_index(drop=True)

	result.to_csv('loose_control.csv', index=False)

def pain_check3():
	df = pd.read_csv('no_pain.csv')
	df2 = pd.read_csv('loose_control.csv')

	result = pd.merge(df, df2, on = ['eid'])

	result.to_csv('loose_control_no_pain.csv', index=False)

def IDPs_add():
	df = pd.read_csv('loose_control_no_pain.csv')
	df2 = pd.read_csv("IDPs_table2.csv")

	result = pd.merge(df, df2, on = ['FID'])

	result.to_csv("loose_control_IDPs.csv", index = False)

def add_gwas3():
	df = pd.read_csv("gwas_phenotypes.csv")
	df2 = pd.read_csv("all_periph_pain_final.csv")
	df3 = pd.read_csv("loose_control_IDPs.csv")

	df.insert(4, 'gwas3', np.nan)

	mask1 = df.set_index('eid').index.isin(df2.set_index('eid').index)
	df['gwas3'].where(~mask1, 2, inplace = True)
	mask2 = df.set_index('eid').index.isin(df3.set_index('eid').index)
	df['gwas3'].where(~mask2, 1, inplace = True)

	df.to_csv('gwas_phenotypes.csv', index = False)

def add_gwas4():
	df = pd.read_csv("gwas_phenotypes.csv")
	df2 = pd.read_csv("gwas_pain_group.csv")
	df3 = pd.read_csv("loose_control_no_pain.csv")

	df.insert(5, 'gwas4', np.nan)

	mask1 = df.set_index('eid').index.isin(df2.set_index('eid').index)
	df['gwas4'].where(~mask1, 2, inplace = True)
	mask2 = df.set_index('eid').index.isin(df3.set_index('eid').index)
	df['gwas4'].where(~mask2, 1, inplace = True)

	df.to_csv('gwas_phenotypes.csv', index = False)

def three_mon_check2():
	df = pd.read_csv('yes_pain.csv')
	df2 = pd.read_csv('hosp_record_periph2.csv')

	result = pd.merge(df, df2, on = ['eid'])

	result.to_csv('periph_3mon3.csv', index = False)

def no_cent_pain_check2():
	df = pd.read_csv("hosp_record_central.csv", low_memory = False)
	df2 = pd.read_csv("periph_3mon3.csv", low_memory = False)

	result = df2[~df2.eid.isin(df.eid.values)]

	result.to_csv('hosp_rec_periph.csv', index = False)

def add_gwas5():
	df = pd.read_csv("gwas_phenotypes.csv")
	df2 = pd.read_csv("hosp_rec_periph.csv")
	df3 = pd.read_csv("control_no_pain2.csv")

	df.insert(6, 'gwas5', np.nan)

	mask1 = df.set_index('eid').index.isin(df2.set_index('eid').index)
	df['gwas5'].where(~mask1, 2, inplace = True)
	mask2 = df.set_index('eid').index.isin(df3.set_index('eid').index)
	df['gwas5'].where(~mask2, 1, inplace = True)

	df.to_csv('gwas_phenotypes.csv', index = False)


def test_na():
	df = pd.read_csv('gwas_phenotypes.csv')

	df.replace(np.nan, 'NA', inplace = True)

	print(df.head())
	df.to_csv('na_test.csv', index = False)

def find_central_pain():
	df = pd.read_csv('clinical_columns_regID.csv')

	bipolar_self = ['1291']
	bipolar_hosp = ['F310', 'F311', 'F312', 'F313', 'F314', 'F315', 'F316', 'F317', 'F318', 'F319']
	schiz_self = ['1289']
	schiz_hosp = ['F200', 'F201', 'F202', 'F203', 'F204', 'F205', 'F206', 'F208', 'F209']
	fibro_self = ['1542']
	fibro_hosp = ['M7970', 'M7971', 'M7974', 'M7975', 'M7978', 'M7979']
	stroke_self = ['1081']
	stroke_hosp = ['G463', 'G464']
	MS_self = ['1261']
	MS_hosp = ['G35']
	alz_self = ['1263']
	alz_hosp = ['G300', 'G301', 'G308', 'G309']
	atrophy_hosp = ['G310']
	hunt_hosp = ['G10']
	park_self = ['1262']
	park_hosp = ['F023', 'G20']
	dementia_hosp = ['F020', 'F028']
	other_hosp = ['F068', 'F069', 'F078', 'F079']

	self_report_array = bipolar_self + schiz_self + fibro_self + stroke_self + MS_self + alz_self + park_self
	hosp_record_array = bipolar_hosp + schiz_hosp + fibro_hosp + stroke_hosp + MS_hosp + alz_hosp + atrophy_hosp + hunt_hosp + park_hosp + dementia_hosp + other_hosp

	file2 = df.loc[(df['20002-0.0'].isin(self_report_array)) | (df['20002-0.1'].isin(self_report_array)) | (df['20002-0.2'].isin(self_report_array)) | (df['20002-0.3'].isin(self_report_array)) | (df['20002-0.4'].isin(self_report_array)) | (df['20002-0.5'].isin(self_report_array)) | (df['20002-0.6'].isin(self_report_array)) | (df['20002-0.7'].isin(self_report_array)) | (df['20002-0.8'].isin(self_report_array)) | (df['20002-0.9'].isin(self_report_array)) | (df['20002-0.10'].isin(self_report_array))]
	file3 = df.loc[(df['41202-0.0'].isin(hosp_record_array)) | (df['41202-0.1'].isin(hosp_record_array)) | (df['41202-0.2'].isin(hosp_record_array)) | (df['41202-0.3'].isin(hosp_record_array)) | (df['41202-0.4'].isin(hosp_record_array)) | (df['41202-0.5'].isin(hosp_record_array)) | (df['41202-0.6'].isin(hosp_record_array)) | (df['41202-0.7'].isin(hosp_record_array)) | (df['41202-0.8'].isin(hosp_record_array)) | (df['41202-0.9'].isin(hosp_record_array)) | (df['41202-0.10'].isin(hosp_record_array))] 

	file2.to_csv('self_report_central.csv', index = False)
	file3.to_csv('hosp_record_central.csv', index = False)

def combine_cent():
	df = pd.read_csv("self_report_central.csv")
	df2 = pd.read_csv("hosp_record_central.csv")

	result = pd.concat([df, df2]).drop_duplicates().reset_index(drop=True)

	result.to_csv("all_central_pain.csv", index = False)

#all peripheral pain is all_periph_pain2.csv

def no_cent_pain_check3():
	df = pd.read_csv("clinical_columns_regID.csv", low_memory = False)
	df2 = pd.read_csv("all_central_pain.csv", low_memory = False)

	result = df[~df.eid.isin(df2.eid.values)]

	result.to_csv('remove_cent_loose.csv', index = False)

def no_periph_pain_check():
	df = pd.read_csv("remove_cent_loose.csv", low_memory = False)
	df2 = pd.read_csv("all_periph_pain2.csv", low_memory = False)

	result = df[~df.eid.isin(df2.eid.values)]

	result.to_csv('remove_record_pain.csv', index = False)

def three_mon_check3():
	df = pd.read_csv('yes_pain.csv')
	df2 = pd.read_csv('remove_record_pain.csv')

	result = df2[~df2.eid.isin(df.eid.values)]

	result.to_csv('loose_control2.csv', index = False)

def IDPs_add2():
	df = pd.read_csv('loose_control2.csv')
	df2 = pd.read_csv("IDPs_table2.csv")

	result = pd.merge(df, df2, on = ['FID'])

	result.to_csv("loose_control2_IDPs.csv", index = False)

def add_gwas3_redo():
	df = pd.read_csv("gwas_phenotypes_fixed.csv")
	df2 = pd.read_csv("all_periph_pain_final.csv")
	df3 = pd.read_csv("loose_control2_IDPs.csv")

	df.insert(5, 'gwas3', np.nan)

	mask1 = df.set_index('eid').index.isin(df2.set_index('eid').index)
	df['gwas3'].where(~mask1, 2, inplace = True)
	mask2 = df.set_index('eid').index.isin(df3.set_index('eid').index)
	df['gwas3'].where(~mask2, 1, inplace = True)

	df.to_csv('gwas_phenotypes_fixed.csv', index = False)

def add_gwas4_redo():
	df = pd.read_csv("gwas_phenotypes_fixed.csv")
	df2 = pd.read_csv("gwas_pain_group.csv")
	df3 = pd.read_csv("loose_control2.csv")

	df.insert(6, 'gwas4', np.nan)

	mask1 = df.set_index('eid').index.isin(df2.set_index('eid').index)
	df['gwas4'].where(~mask1, 2, inplace = True)
	mask2 = df.set_index('eid').index.isin(df3.set_index('eid').index)
	df['gwas4'].where(~mask2, 1, inplace = True)

	df.to_csv('gwas_phenotypes_fixed.csv', index = False)

def add_na1():
	df = pd.read_csv('gwas_phenotypes_fixed.csv')

	df.replace(np.nan, 'NA', inplace = True)

	print(df.head())
	df.to_csv('gwas_phenotypes_fixed_na.csv', index = False)

def add_na2():
	df = pd.read_csv('gwas_phenotypes_just34.csv')

	df.replace(np.nan, 'NA', inplace = True)

	print(df.head())
	df.to_csv('gwas_phenotypes_just34_na.csv', index = False)


def add_gwas4_redo2():
	df = pd.read_csv("gwas.csv")
	df2 = pd.read_csv("gwas_pain_group.csv")
	df3 = pd.read_csv("loose_control2.csv")

	df.insert(2, 'gwas4', np.nan)

	mask1 = df.set_index('eid').index.isin(df2.set_index('eid').index)
	df['gwas4'].where(~mask1, 2, inplace = True)
	mask2 = df.set_index('eid').index.isin(df3.set_index('eid').index)
	df['gwas4'].where(~mask2, 1, inplace = True)

	df.to_csv('gwas4.csv', index = False)



def main():
	#find_periph_pain()
	#combine()
	#three_mon_check()
	#no_cent_pain_check()
	#add_gwas_pain()
	#sort()
	#add_gwas1_PG_label()
	#find_control()
	#pain_check2()
	#add_gwas1_CG_label()
	#add_gwas1()
	#add_gwas2()
	#find_nocent_pain()
	#combine1()
	#find_noperiph_pain()
	#combine2()
	#combine3()
	#pain_check3()
	#IDPs_add()
	#add_gwas3()
	#add_gwas4()
	#three_mon_check2()
	#no_cent_pain_check2()
	#add_gwas5()
	#test_na()
	#find_central_pain()
	#ombine_cent()
	#no_cent_pain_check3()
	#no_periph_pain_check()
	#three_mon_check3()
	#IDPs_add2()
	#add_gwas3_redo()
	#add_gwas4_redo()
	#add_na1()
	#add_na2()
	add_gwas4_redo2()
main()




#gwas1 is normal PG and CG criteria but over entire UKB population
#gwas2 is original PG and CG groups with everyone else being NA
#gwas3 is original PG and loose controls who have IDPs
#gwas4 is normal explanded pain group and all loose controls 
#gwas5 is people from pain group who reported through hospital records and normal expanded CG


