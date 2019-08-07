import pandas as pd

#find all neurodegenerative and mental health disorders
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

def all_central_pain():
	df = pd.read_csv("self_report_central.csv")
	df2 = pd.read_csv("hosp_record_central.csv")

	result = pd.concat([df, df2]).drop_duplicates().reset_index(drop=True)

	result.to_csv("all_central_pain.csv", index = False)

def IDPs_central_pain():
	df = pd.read_csv("all_central_pain.csv", low_memory = False)
	df2 = pd.read_csv("IDPs_table2.csv")

	result = pd.merge(df, df2, on = ['FID'])

	result.to_csv("all_central_pain_wIDPs.csv", index = False)

#remove from OA
def compare_OA():
	df = pd.read_csv("all_central_pain_wIDPs.csv", low_memory = False)
	df2 = pd.read_csv("OA_and_3mon_pain_compare.csv", low_memory = False)

	result = df2[~df2.eid.isin(df.eid.values)]

	result.to_csv('OA_wo_central_pain.csv', index = False)

def main():
	#find_central_pain()
	#all_central_pain()
	#IDPs_central_pain()
	#compare_OA()
main()





